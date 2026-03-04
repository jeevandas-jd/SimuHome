import logging
from typing import Dict, Any, Optional, List
from pydantic import BaseModel, Field

from src.simulator.domain.home import Home
from src.simulator.domain.result import Result, ResultBuilder, ErrorCode
from src.simulator.application.device_factory import (
    DEVICE_FACTORY,
    is_valid_device_type,
    create_device,
)

logger = logging.getLogger(__name__)


class DeviceInRoomConfig(BaseModel):
    device_id: str
    device_type: str
    attributes: Optional[Dict[str, Any]] = (
        None  
    )


class RoomConfig(BaseModel):
    state: Optional[Dict[str, float]] = (
        None  
    )
    devices: Optional[List[DeviceInRoomConfig]] = None


class SimulationConfig(BaseModel):
    tick_interval: float = Field(0.1, gt=0)
    enable_aggregators: bool = True
    max_ticks: Optional[int] = None
    fast_forward: bool = False
    base_time: str = Field(..., description="Base virtual time 'YYYY-MM-DD HH:MM:SS'")
    rooms: Optional[Dict[str, RoomConfig]] = (
        None  
    )


def _parse_attribute_path(attr_path: str) -> tuple[int, str, str]:
    
    try:
        parts = attr_path.split(".")
        if len(parts) != 3:
            raise ValueError(f"Invalid attribute path format: {attr_path}")

        endpoint_id = int(parts[0])
        cluster_id = parts[1]
        attribute_id = parts[2]
        return endpoint_id, cluster_id, attribute_id
    except Exception as e:
        raise ValueError(f"Failed to parse attribute path '{attr_path}': {e}")


def _initialize_room_state(
    home: Home, room_id: str, state_config: Dict[str, float]
) -> Result:
    
    try:
        getattr(home, "_Home__ensure_room_initialized")(room_id)

        room_aggs = home.aggregators_by_room.get(room_id, {})
        for agg_type, initial_value in state_config.items():
            if agg_type in room_aggs:
                agg = room_aggs[agg_type]
                agg.current_value = initial_value
                if hasattr(agg, "baseline_value"):
                    agg.baseline_value = initial_value

        return Result.ok({"room_id": room_id, "initialized_states": len(state_config)})

    except Exception as e:
        logger.error(f"Failed to initialize room state for '{room_id}': {e}")
        return Result.fail(
            ErrorCode.INTERNAL_ERROR,
            "Room state initialization failed",
            f"Failed to initialize room '{room_id}': {str(e)}",
        )


def _is_non_bool_int(value: Any) -> bool:
    return isinstance(value, int) and not isinstance(value, bool)


def _validate_washer_attribute_schema(device_config: DeviceInRoomConfig) -> Result:
    if device_config.device_type != "laundry_washer":
        return Result.ok()

    attrs = device_config.attributes
    if attrs is None:
        return Result.ok()
    if not isinstance(attrs, dict):
        return Result.fail(
            ErrorCode.VALIDATION_ERROR,
            "Invalid washer attribute payload",
            "laundry_washer attributes must be a mapping",
        )

    operational_state_key = "1.OperationalState.OperationalState"
    if operational_state_key in attrs and not _is_non_bool_int(
        attrs[operational_state_key]
    ):
        return Result.fail(
            ErrorCode.VALIDATION_ERROR,
            "Invalid washer operational state type",
            "1.OperationalState.OperationalState must be an integer",
        )

    current_mode_key = "1.LaundryWasherMode.CurrentMode"
    if current_mode_key in attrs and not _is_non_bool_int(attrs[current_mode_key]):
        return Result.fail(
            ErrorCode.VALIDATION_ERROR,
            "Invalid washer mode type",
            "1.LaundryWasherMode.CurrentMode must be an integer",
        )

    supported_modes_key = "1.LaundryWasherMode.SupportedModes"
    if supported_modes_key in attrs:
        supported_modes = attrs[supported_modes_key]
        if not isinstance(supported_modes, list) or not supported_modes:
            return Result.fail(
                ErrorCode.VALIDATION_ERROR,
                "Invalid washer supported modes",
                "1.LaundryWasherMode.SupportedModes must be a non-empty list",
            )

        for index, mode_entry in enumerate(supported_modes):
            if not isinstance(mode_entry, dict):
                return Result.fail(
                    ErrorCode.VALIDATION_ERROR,
                    "Invalid washer mode entry",
                    f"SupportedModes[{index}] must be a mapping",
                )

            raw_mode = mode_entry.get("mode")
            if not _is_non_bool_int(raw_mode):
                return Result.fail(
                    ErrorCode.VALIDATION_ERROR,
                    "Invalid washer mode value",
                    f"SupportedModes[{index}].mode must be an integer",
                )

            raw_tags = mode_entry.get("ModeTags")
            if not isinstance(raw_tags, list):
                return Result.fail(
                    ErrorCode.VALIDATION_ERROR,
                    "Invalid washer mode tags",
                    f"SupportedModes[{index}].ModeTags must be a list of integers",
                )
            for tag_index, tag in enumerate(raw_tags):
                if not _is_non_bool_int(tag):
                    return Result.fail(
                        ErrorCode.VALIDATION_ERROR,
                        "Invalid washer mode tag value",
                        f"SupportedModes[{index}].ModeTags[{tag_index}] must be an integer",
                    )

            raw_label = mode_entry.get("label")
            if raw_label is not None and not isinstance(raw_label, str):
                return Result.fail(
                    ErrorCode.VALIDATION_ERROR,
                    "Invalid washer mode label type",
                    f"SupportedModes[{index}].label must be a string when provided",
                )

    return Result.ok()


def _add_device_to_room(
    home: Home, room_id: str, device_config: DeviceInRoomConfig
) -> Result:
    

    if not is_valid_device_type(device_config.device_type):
        return Result.fail(
            ErrorCode.VALIDATION_ERROR,
            "Invalid device type",
            f"Unsupported device_type: {device_config.device_type}",
        )

    washer_schema_result = _validate_washer_attribute_schema(device_config)
    if not washer_schema_result.success:
        return washer_schema_result

    try:
        device = create_device(device_config.device_type, device_config.device_id)
    except Exception as e:
        logger.error(f"Failed to create device '{device_config.device_id}': {e}")
        return Result.fail(
            ErrorCode.INTERNAL_ERROR,
            "Device creation failed",
            f"Failed to create device '{device_config.device_id}': {str(e)}",
        )

    result = home._add_device(
        room_id=room_id, device=device, attributes=device_config.attributes
    )
    if not result.success:
        logger.error(
            f"Failed to add device '{device_config.device_id}' to room '{room_id}': {result.error_message}"
        )
        return result

    return Result.ok(
        {
            "device_id": device_config.device_id,
            "device_type": device_config.device_type,
            "room_id": room_id,
        }
    )


def initialize_home_from_config(home: Home, config: SimulationConfig) -> Result:
    
    if not config.rooms:
        return Result.ok(
            {"message": "Home initialized with defaults", "rooms_count": 0}
        )

    total_devices = 0
    failed_rooms = []

    for room_id, room_config in config.rooms.items():
        if room_config.devices:
            for device_config in room_config.devices:
                result = _add_device_to_room(home, room_id, device_config)
                if result.success:
                    total_devices += 1
                else:
                    logger.error(
                        f"Failed to add device '{device_config.device_id}' to room '{room_id}': {result.error_message}"
                    )
                    error_code = result.error_code or ErrorCode.VALIDATION_ERROR
                    error_detail = (
                        result.error_detail
                        or f"room={room_id}, device_id={device_config.device_id}, device_type={device_config.device_type}"
                    )
                    return Result.fail(
                        error_code,
                        "Device initialization failed",
                        error_detail,
                    )
        else:
            getattr(home, "_Home__ensure_room_initialized")(room_id)

        if room_config.state:
            state_result = _initialize_room_state(home, room_id, room_config.state)
            if not state_result.success:
                failed_rooms.append(room_id)
                logger.error(
                    f"Failed to initialize state for room '{room_id}': {state_result.error_message}"
                )

    total_rooms = len(home.devices_by_room)

    if failed_rooms:
        logger.warning(f"Some rooms had initialization issues: {failed_rooms}")

    try:
        home_state_result = home._get_home_state()
        if not home_state_result.success:
            return Result.fail(
                ErrorCode.INTERNAL_ERROR,
                "Failed to get home state after initialization",
                str(home_state_result.error_message),
            )

        home_state = home_state_result.get_data()

    except Exception as e:
        return Result.fail(
            ErrorCode.INTERNAL_ERROR, "Exception while getting home state", str(e)
        )

    return Result.ok(
        {
            "total_rooms": total_rooms,
            "total_devices": total_devices,
            "failed_rooms": failed_rooms,
            "initial_home_config": home_state,
        }
    )


def create_simple_room_config(
    devices: List[tuple[str, str]], state: Optional[Dict[str, float]] = None
) -> RoomConfig:
    
    device_configs = [
        DeviceInRoomConfig(device_id=device_id, device_type=device_type)
        for device_id, device_type in devices
    ]

    return RoomConfig(devices=device_configs, state=state)


def create_simulation_config(
    *,
    base_time: str,
    tick_interval: float = 0.1,
    rooms: Optional[Dict[str, RoomConfig]] = None,
) -> SimulationConfig:
    
    return SimulationConfig(
        tick_interval=tick_interval, rooms=rooms, base_time=base_time
    )
