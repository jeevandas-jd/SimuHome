from src.simulator.domain.clusters.base import Cluster
from src.simulator.domain.result import Result, ResultBuilder, ErrorCode
from enum import IntEnum


class NumberOfRinsesEnum(IntEnum):
    

    NONE = 0
    NORMAL = 1
    EXTRA = 2
    MAX = 3


class SpinSpeed(IntEnum):
    

    LOW = 0
    MEDIUM = 1
    HIGH = 2
    EXTRA_HIGH = 3


class LaundryWasherControlsCluster(Cluster):
    

    FEATURE_SPIN = 0x01
    FEATURE_RINSE = 0x02


    MODE_SPIN_SPEEDS = {
        "Delicate": [SpinSpeed.LOW, SpinSpeed.MEDIUM],
        "Normal": [SpinSpeed.LOW, SpinSpeed.MEDIUM, SpinSpeed.HIGH],
        "Heavy": [SpinSpeed.MEDIUM, SpinSpeed.HIGH, SpinSpeed.EXTRA_HIGH],
        "Whites": [
            SpinSpeed.LOW,
            SpinSpeed.MEDIUM,
            SpinSpeed.HIGH,
            SpinSpeed.EXTRA_HIGH,
        ],
        "Quick Normal": [SpinSpeed.HIGH, SpinSpeed.EXTRA_HIGH],
        "Heavy Whites": [SpinSpeed.HIGH, SpinSpeed.EXTRA_HIGH],
    }

    MODE_RINSES = {
        "Delicate": [NumberOfRinsesEnum.NORMAL, NumberOfRinsesEnum.EXTRA],
        "Normal": [
            NumberOfRinsesEnum.NONE,
            NumberOfRinsesEnum.NORMAL,
            NumberOfRinsesEnum.EXTRA,
        ],
        "Heavy": [
            NumberOfRinsesEnum.NORMAL,
            NumberOfRinsesEnum.EXTRA,
            NumberOfRinsesEnum.MAX,
        ],
        "Whites": [
            NumberOfRinsesEnum.NORMAL,
            NumberOfRinsesEnum.EXTRA,
            NumberOfRinsesEnum.MAX,
        ],
        "Quick Normal": [NumberOfRinsesEnum.NONE, NumberOfRinsesEnum.NORMAL],
        "Heavy Whites": [NumberOfRinsesEnum.EXTRA, NumberOfRinsesEnum.MAX],
    }

    def __init__(self, features: int = FEATURE_SPIN | FEATURE_RINSE):
        super().__init__(cluster_id="LaundryWasherControls")

        self.features = features
        self.device = None


        self.attributes = {}


        if features & self.FEATURE_SPIN:
            self.attributes.update(
                {
                    "SpinSpeeds": [
                        SpinSpeed.LOW,
                        SpinSpeed.MEDIUM,
                        SpinSpeed.HIGH,
                        SpinSpeed.EXTRA_HIGH,
                    ],
                    "SpinSpeedCurrent": SpinSpeed.MEDIUM,
                }
            )


        if features & self.FEATURE_RINSE:
            self.attributes.update(
                {
                    "NumberOfRinses": NumberOfRinsesEnum.NORMAL,
                    "SupportedRinses": [
                        NumberOfRinsesEnum.NONE,
                        NumberOfRinsesEnum.NORMAL,
                        NumberOfRinsesEnum.EXTRA,
                        NumberOfRinsesEnum.MAX,
                    ],
                }
            )


        if features & self.FEATURE_SPIN:
            self.readonly_attributes.add("SpinSpeeds")
        if features & self.FEATURE_RINSE:
            self.readonly_attributes.add("SupportedRinses")


    def set_device_reference(self, device):
        
        self.device = device

    def _is_device_running(self) -> bool:
        
        if not self.device:
            return False

        try:
            from src.simulator.domain.clusters.operational_state import OperationalStateEnum

            operational_state = self.device.get_attribute(
                1, "OperationalState", "OperationalState"
            )
            return operational_state == OperationalStateEnum.RUNNING
        except Exception as error:
            raise RuntimeError(
                "Failed to read OperationalState for laundry washer controls"
            ) from error

    def write_attribute(self, attribute_id: str, value) -> Result:
        

        try:
            device_running = self._is_device_running()
        except RuntimeError as error:
            return ResultBuilder.internal_error(error)


        if device_running:
            if attribute_id in ["SpinSpeedCurrent", "NumberOfRinses"]:
                return Result.fail(
                    ErrorCode.INVALID_STATE,
                    f"Cannot change {attribute_id} while device is running",
                    "Stop the device before changing operational settings",
                )


        if attribute_id == "SpinSpeedCurrent":
            if not (self.features & self.FEATURE_SPIN):
                return Result.fail(
                    ErrorCode.ATTRIBUTE_NOT_FOUND,
                    "SpinSpeedCurrent not supported",
                    "SPIN feature not enabled",
                )

            spin_speeds = self.attributes.get("SpinSpeeds", [])


            if value is None:
                self.attributes[attribute_id] = None
                return Result.ok(
                    {
                        "cluster": self.cluster_id,
                        "attribute": attribute_id,
                        "old_value": self.attributes.get(attribute_id),
                        "new_value": None,
                    }
                )


            if isinstance(value, SpinSpeed):
                if value not in spin_speeds:
                    return Result.fail(
                        ErrorCode.CONSTRAINT_ERROR,
                        f"Invalid spin speed: {value}",
                        f"Supported speeds: {spin_speeds}",
                    )
            elif isinstance(value, int):
                if value < 0 or value >= len(spin_speeds):
                    return Result.fail(
                        ErrorCode.CONSTRAINT_ERROR,
                        f"Invalid spin speed index: {value}",
                        f"Valid range: 0-{len(spin_speeds)-1} or None",
                    )
                value = spin_speeds[value]
            else:
                return Result.fail(
                    ErrorCode.CONSTRAINT_ERROR,
                    f"Invalid spin speed value: {value}",
                    "Must be SpinSpeed enum or int index",
                )


        elif attribute_id == "NumberOfRinses":
            if not (self.features & self.FEATURE_RINSE):
                return Result.fail(
                    ErrorCode.ATTRIBUTE_NOT_FOUND,
                    "NumberOfRinses not supported",
                    "RINSE feature not enabled",
                )

            supported_rinses = self.attributes.get("SupportedRinses", [])


            if value not in supported_rinses:
                return Result.fail(
                    ErrorCode.CONSTRAINT_ERROR,
                    f"Invalid rinse setting: {value}",
                    f"Supported values: {supported_rinses}",
                )


        return super().write_attribute(attribute_id, value)

    def update_spin_speeds_for_mode(self, mode_label: str):
        
        if not (self.features & self.FEATURE_SPIN):
            return


        new_speeds = self.MODE_SPIN_SPEEDS.get(
            mode_label,
            [SpinSpeed.LOW, SpinSpeed.MEDIUM, SpinSpeed.HIGH, SpinSpeed.EXTRA_HIGH],
        )


        old_speeds = self.attributes.get("SpinSpeeds", [])
        self.attributes["SpinSpeeds"] = new_speeds


        current_speed = self.attributes.get("SpinSpeedCurrent")
        if current_speed is not None and current_speed not in new_speeds:
            self.attributes["SpinSpeedCurrent"] = (
                new_speeds[0] if new_speeds else None
            )

    def update_supported_rinses_for_mode(self, mode_label: str):
        
        if not (self.features & self.FEATURE_RINSE):
            return


        new_rinses = self.MODE_RINSES.get(
            mode_label,
            [
                NumberOfRinsesEnum.NONE,
                NumberOfRinsesEnum.NORMAL,
                NumberOfRinsesEnum.EXTRA,
                NumberOfRinsesEnum.MAX,
            ],
        )


        self.attributes["SupportedRinses"] = new_rinses


        current_rinse = self.attributes.get("NumberOfRinses")
        if current_rinse not in new_rinses:
            self.attributes["NumberOfRinses"] = (
                new_rinses[0] if new_rinses else NumberOfRinsesEnum.NORMAL
            )
