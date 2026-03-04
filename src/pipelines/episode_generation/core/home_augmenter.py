from __future__ import annotations

from dataclasses import asdict, is_dataclass
from enum import Enum, IntEnum
from typing import Any, Dict, List, Mapping, Optional, Tuple, cast
import random

from src.pipelines.episode_generation.core.candidate_sampler import sample_candidate
from src.pipelines.episode_generation.core.seed_utils import derive_subseed, ensure_seed
from src.simulator.application.home_initializer import (
    SimulationConfig,
    initialize_home_from_config,
)
from src.simulator.domain.home import Home
from src.simulator.domain.result import Result


REQUIRED_ROOM_STATE_KEYS: Tuple[str, ...] = (
    "temperature",
    "humidity",
    "illuminance",
    "pm10",
)


def _derive_device_seed(
    global_seed: int, room_id: str, device_type: str, device_id: str
) -> int:
    return derive_subseed(global_seed, "augment-home", room_id, device_type, device_id)


def _collect_devices_from_config(cfg: Dict[str, Any]) -> List[Tuple[str, str, str]]:
    devices: List[Tuple[str, str, str]] = []  
    rooms = cfg.get("rooms") or {}
    for room_id in sorted(rooms.keys(), key=lambda x: str(x)):
        rc = rooms.get(room_id) or {}
        for d in rc.get("devices") or []:
            did = d.get("device_id")
            dtype = d.get("device_type")
            if did and dtype:
                devices.append((room_id, str(did), str(dtype)))
    return devices


def _to_jsonable(value: Any) -> Any:
    if isinstance(value, IntEnum):
        return int(value)
    if isinstance(value, Enum):
        raw_value = value.value
        if isinstance(raw_value, (str, int, float, bool)) or raw_value is None:
            return raw_value
        return value.name
    if is_dataclass(value) and not isinstance(value, type):
        return _to_jsonable(asdict(cast(Any, value)))
    if isinstance(value, dict):
        return {str(k): _to_jsonable(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [_to_jsonable(item) for item in value]
    if isinstance(value, set):
        return [_to_jsonable(item) for item in sorted(value, key=lambda x: str(x))]
    if hasattr(value, "__dict__"):
        return _to_jsonable(vars(value))
    return value


def _sorted_dict_by_str_key(data: Dict[str, Any]) -> Dict[str, Any]:
    return {
        str(k): _to_jsonable(data[k]) for k in sorted(data.keys(), key=lambda x: str(x))
    }


def _flatten_attributes(attributes: Dict[str, Any]) -> Dict[str, Any]:
    if not attributes:
        return {}

    sample_keys = list(attributes.keys())[:3]
    is_flat = any(isinstance(k, str) and ("." in k) for k in sample_keys)
    if is_flat:
        return _sorted_dict_by_str_key(attributes)

    flattened: Dict[str, Any] = {}
    for cluster_id in sorted(attributes.keys(), key=lambda x: str(x)):
        cluster_attrs = attributes.get(cluster_id)
        if not isinstance(cluster_attrs, dict):
            continue
        for attr_id in sorted(cluster_attrs.keys(), key=lambda x: str(x)):
            flattened[f"1.{cluster_id}.{attr_id}"] = _to_jsonable(
                cluster_attrs[attr_id]
            )
    return flattened


def _get_data_or_raise(result: Result, *, context: str) -> Dict[str, Any]:
    if not result.success:
        detail = result.error_detail or result.error_message or "unknown"
        raise RuntimeError(f"{context} failed: {detail}")
    data = result.get_data() or {}
    if not isinstance(data, dict):
        raise RuntimeError(f"{context} returned invalid payload")
    return data


def _apply_device_filters(
    devices: List[Tuple[str, str, str]],
    include_devices_by_room: Optional[Dict[str, List[str]]],
    exclude_devices_by_room: Optional[Dict[str, List[str]]],
) -> List[Tuple[str, str, str]]:
    
    if include_devices_by_room and exclude_devices_by_room:
        raise ValueError(
            "include_devices_by_room and exclude_devices_by_room cannot be used together"
        )

    if include_devices_by_room:
        allowed: set[tuple[str, str]] = set()
        for room_id, dev_ids in include_devices_by_room.items():
            for did in dev_ids or []:
                allowed.add((str(room_id), str(did)))
        return [t for t in devices if (t[0], t[1]) in allowed]

    if exclude_devices_by_room:
        blocked: set[tuple[str, str]] = set()
        for room_id, dev_ids in exclude_devices_by_room.items():
            for did in dev_ids or []:
                blocked.add((str(room_id), str(did)))
        return [t for t in devices if (t[0], t[1]) not in blocked]

    return devices


def _validate_required_room_state(
    *,
    room_id: str,
    state: Mapping[str, Any],
    context: str,
) -> None:
    missing = [k for k in REQUIRED_ROOM_STATE_KEYS if k not in state]
    if missing:
        missing_joined = ", ".join(missing)
        raise ValueError(
            f"{context} room '{room_id}' state is missing required keys: {missing_joined}"
        )

    for key in REQUIRED_ROOM_STATE_KEYS:
        value = state[key]
        if not isinstance(value, (int, float)):
            raise ValueError(
                f"{context} room '{room_id}' state.{key} must be numeric, got {type(value).__name__}"
            )


def _validate_home_config_for_augmentation(home_config: Mapping[str, Any]) -> None:
    rooms = home_config.get("rooms")
    if not isinstance(rooms, Mapping) or not rooms:
        raise ValueError("home_config.rooms must be a non-empty mapping")

    for room_id in sorted(rooms.keys(), key=lambda x: str(x)):
        room_data = rooms.get(room_id)
        if not isinstance(room_data, Mapping):
            raise ValueError(f"home_config room '{room_id}' must be a mapping")

        state = room_data.get("state")
        if not isinstance(state, Mapping):
            raise ValueError(f"home_config room '{room_id}' is missing state")

        _validate_required_room_state(
            room_id=str(room_id),
            state=state,
            context="home_config",
        )


def _parse_state_bounds(
    state_bounds_raw: object,
) -> Dict[str, Tuple[float, float]] | None:
    if state_bounds_raw is None:
        return None
    if not isinstance(state_bounds_raw, Mapping):
        raise ValueError("home_config.state_bounds must be a mapping")

    actual = set(state_bounds_raw.keys())
    expected = set(REQUIRED_ROOM_STATE_KEYS)
    missing = sorted(expected - actual)
    unknown = sorted(actual - expected)
    if missing or unknown:
        parts: List[str] = []
        if missing:
            parts.append(f"missing keys: {', '.join(missing)}")
        if unknown:
            parts.append(f"unknown keys: {', '.join(unknown)}")
        raise ValueError(
            f"home_config.state_bounds has invalid shape ({'; '.join(parts)})"
        )

    bounds: Dict[str, Tuple[float, float]] = {}
    for key in REQUIRED_ROOM_STATE_KEYS:
        key_range = state_bounds_raw.get(key)
        if not isinstance(key_range, Mapping):
            raise ValueError(f"home_config.state_bounds.{key} must be a mapping")
        min_raw = key_range.get("min")
        max_raw = key_range.get("max")
        if isinstance(min_raw, bool) or not isinstance(min_raw, (int, float)):
            raise ValueError(f"home_config.state_bounds.{key}.min must be numeric")
        if isinstance(max_raw, bool) or not isinstance(max_raw, (int, float)):
            raise ValueError(f"home_config.state_bounds.{key}.max must be numeric")
        minimum = float(min_raw)
        maximum = float(max_raw)
        if minimum > maximum:
            raise ValueError(f"home_config.state_bounds.{key}.min cannot exceed max")
        bounds[key] = (minimum, maximum)

    return bounds


def _apply_state_bounds(
    config: Dict[str, Any],
    state_bounds: Dict[str, Tuple[float, float]] | None,
) -> Dict[str, Any]:
    if state_bounds is None:
        return config

    rooms = config.get("rooms")
    if not isinstance(rooms, dict):
        raise RuntimeError("snapshot config missing rooms for state bound enforcement")

    for room_id in sorted(rooms.keys(), key=lambda x: str(x)):
        room_data = rooms.get(room_id)
        if not isinstance(room_data, dict):
            raise RuntimeError(f"snapshot room '{room_id}' must be a mapping")
        state = room_data.get("state")
        if not isinstance(state, dict):
            raise RuntimeError(f"snapshot room '{room_id}' is missing state")

        for key in REQUIRED_ROOM_STATE_KEYS:
            if key not in state:
                raise RuntimeError(
                    f"snapshot room '{room_id}' state missing key '{key}'"
                )
            value = state[key]
            if isinstance(value, bool) or not isinstance(value, (int, float)):
                raise RuntimeError(
                    f"snapshot room '{room_id}' state.{key} must be numeric"
                )
            minimum, maximum = state_bounds[key]
            state[key] = max(min(float(value), maximum), minimum)

    return config


def _convert_snapshot_to_simulation_config(
    snapshot_data: Dict[str, Any], *, base_time: str
) -> Dict[str, Any]:
    
    tick_interval = snapshot_data.get("tick_interval")
    if tick_interval is None:
        raise RuntimeError("Snapshot payload is missing tick_interval")

    config: Dict[str, Any] = {
        "tick_interval": float(tick_interval),
        "base_time": str(base_time),
        "rooms": {},
    }

    rooms = snapshot_data.get("rooms") or {}
    for room_id in sorted(rooms.keys(), key=lambda x: str(x)):
        room_data = rooms.get(room_id) or {}
        room_config: Dict[str, Any] = {"devices": []}
        state = room_data.get("state")
        if not isinstance(state, dict):
            raise RuntimeError(f"Snapshot room '{room_id}' is missing state")
        try:
            _validate_required_room_state(
                room_id=str(room_id),
                state=state,
                context="snapshot",
            )
        except ValueError as exc:
            raise RuntimeError(str(exc)) from exc

        room_config["state"] = _sorted_dict_by_str_key(state)

        devices = room_data.get("devices") or []
        devices = sorted(
            devices,
            key=lambda d: (str(d.get("device_id", "")), str(d.get("device_type", ""))),
        )
        for device in devices:
            device_config: Dict[str, Any] = {
                "device_id": device.get("device_id"),
                "device_type": device.get("device_type"),
            }
            attributes = device.get("attributes", {})
            if attributes:
                flattened = _flatten_attributes(attributes)
                if flattened:
                    device_config["attributes"] = flattened

            room_config["devices"].append(device_config)
        config["rooms"][room_id] = room_config
    return config


def _initialize_home_locally(
    home_config: Dict[str, Any],
) -> Tuple[Home, Dict[str, Any]]:
    cfg = SimulationConfig(**home_config)
    home = Home(
        tick_interval=cfg.tick_interval,
        enable_aggregators=cfg.enable_aggregators,
        max_ticks=cfg.max_ticks,
        fast_forward=bool(cfg.fast_forward),
        base_time=cfg.base_time,
    )

    init_result = initialize_home_from_config(home, cfg)
    if not init_result.success:
        detail = init_result.error_detail or init_result.error_message or "unknown"
        raise RuntimeError(f"Home initialization failed: {detail}")

    snapshot_data = _get_data_or_raise(home._get_home_state(), context="home state")
    return home, snapshot_data


def augment_home(
    *,
    home_config: Mapping[str, Any],
    seed: int,
    base_url: Optional[str] = None,
    num_rounds: int = 20,
    include_devices_by_room: Optional[Dict[str, List[str]]] = None,
    exclude_devices_by_room: Optional[Dict[str, List[str]]] = None,
) -> Dict[str, Any]:
    _ = base_url

    if not isinstance(home_config, Mapping):
        raise ValueError("home_config must be a mapping")
    seed = ensure_seed(seed, context="augment_home")
    home_config_dict = dict(home_config)

    if not home_config_dict.get("base_time"):
        raise ValueError("home_config.base_time is required for augmentation")
    base_time = str(home_config_dict.get("base_time"))
    state_bounds = _parse_state_bounds(home_config_dict.pop("state_bounds", None))

    _validate_home_config_for_augmentation(home_config_dict)

    home, actual_config = _initialize_home_locally(home_config_dict)

    devices = sorted(
        _collect_devices_from_config(actual_config), key=lambda x: (x[0], x[2], x[1])
    )
    devices = _apply_device_filters(
        devices, include_devices_by_room, exclude_devices_by_room
    )

    if not devices:
        config = _convert_snapshot_to_simulation_config(
            actual_config, base_time=base_time
        )
        return _apply_state_bounds(config, state_bounds)

    rounds = max(1, int(num_rounds))
    for ridx in range(rounds):
        steps: List[Dict[str, Any]] = []

        snap_data = _get_data_or_raise(home._get_home_state(), context="home state")
        rooms = snap_data.get("rooms") or {}
        flat_by_device: Dict[str, Dict[str, Any]] = {}
        for room_id in sorted(rooms.keys(), key=lambda x: str(x)):
            rc = rooms.get(room_id) or {}
            for d in rc.get("devices") or []:
                did = d.get("device_id")
                attrs = d.get("attributes") or {}
                if did:
                    flat_by_device[str(did)] = attrs

        for room_id, device_id, device_type in devices:
            dev_seed = _derive_device_seed(seed, room_id, device_type, device_id)
            state_flat = flat_by_device.get(device_id)
            if not isinstance(state_flat, dict):
                continue
            cand = sample_candidate(
                device_type=device_type,
                device_id=device_id,
                state_flat=state_flat,
                seed=dev_seed,
            )
            if not cand or not isinstance(cand.get("api"), dict):
                continue
            api = cand["api"]
            tool = (
                "execute_command"
                if api.get("api_type") == "execute_command"
                else "write_attribute"
            )
            if tool == "execute_command":
                args: Dict[str, Any] = {
                    "device_id": device_id,
                    "endpoint_id": int(api.get("endpoint_id", 1)),
                    "cluster_id": api.get("cluster_id"),
                    "command_id": api.get("command_id"),
                    "args": api.get("args") or {},
                }
            else:
                args = {
                    "device_id": device_id,
                    "endpoint_id": int(api.get("endpoint_id", 1)),
                    "cluster_id": api.get("cluster_id"),
                    "attribute_id": api.get("attribute_id"),
                    "value": api.get("value"),
                }
            steps.append({"tool": tool, "args": args})

        if steps:
            workflow_result = home._run_workflow_now(
                steps,
                continue_on_error=True,
                record=False,
                tag=f"home_aug_round_{ridx}",
            )
            if not workflow_result.success:
                detail = (
                    workflow_result.error_detail
                    or workflow_result.error_message
                    or "unknown"
                )
                raise RuntimeError(f"Augmentation workflow failed: {detail}")

            result_rows = (workflow_result.get_data() or {}).get("results") or []
            if result_rows:
                total = len(result_rows)
                failures = sum(1 for row in result_rows if not row.get("success"))
                if failures >= total:
                    raise RuntimeError(
                        f"Augmentation round {ridx} had no successful steps ({failures}/{total})"
                    )

    rng = random.Random(seed)
    to_tick = rng.randint(300, 600)
    snapshot_data = _get_data_or_raise(
        home._fast_forward_to(to_tick), context="fast forward"
    )
    config = _convert_snapshot_to_simulation_config(snapshot_data, base_time=base_time)
    return _apply_state_bounds(config, state_bounds)


__all__ = ["augment_home"]
