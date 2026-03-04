from __future__ import annotations

import math
import random
from typing import Any, Callable, Dict, List, Tuple, cast

from src.pipelines.episode_generation.core.home_config_initializer import (
    HomeConfigInitializer,
)
from src.pipelines.episode_generation.core.home_augmenter import augment_home
from src.pipelines.episode_generation.core.seed_utils import ensure_seed
from src.pipelines.episode_generation.shared.goals import (
    deduplicate_required_actions,
)
from src.pipelines.episode_generation.shared.payload_assembler import assemble_payload
from src.pipelines.episode_generation.shared.selectors import (
    sample_user_location,
    sample_op_device,
)
from src.pipelines.episode_generation.shared.time_utils import (
    minutes_to_ticks,
    get_running_anchor_end_tick,
    ticks_to_minutes,
    get_tolerance_ticks,
)
from src.simulator.domain.clusters.laundry_dryer_controls import DrynessLevelEnum


ONOFF_ATTR = "1.OnOff.OnOff"
OP_STATE_ATTR = "1.OperationalState.OperationalState"
RVC_OP_STATE_ATTR = "1.RVCOperationalState.OperationalState"


OP_STATE_STOPPED = 0
OP_STATE_RUNNING = 1
OP_STATE_PAUSED = 2

WASHER_MODE_DURATION_SECONDS: Dict[int, int] = {
    0: 3600,
    1: 2700,
    2: 5400,
    3: 3600,
    4: 900,
    5: 5400,
}


def _require_non_bool_int(value: Any, *, context: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError(f"{context} must be an integer")
    return int(value)


def _get_washer_params(
    attrs: Dict[str, Any], rng: random.Random, tick_interval: float = 0.1
) -> Tuple[int, List[Dict[str, Any]]]:
    
    modes = attrs.get("1.LaundryWasherMode.SupportedModes") or []
    if not isinstance(modes, list) or not modes:
        raise ValueError(
            "1.LaundryWasherMode.SupportedModes must be a non-empty list for laundry_washer targets"
        )

    item = rng.choice(modes) or {}
    if not isinstance(item, dict):
        raise ValueError("Laundry washer mode entry must be a mapping")

    mode_code = item.get("mode")
    mode_value = _require_non_bool_int(mode_code, context="Laundry washer mode")
    duration_seconds = WASHER_MODE_DURATION_SECONDS.get(mode_value)
    if duration_seconds is None:
        raise ValueError(f"Unsupported laundry washer mode value: {mode_value}")

    duration_ticks = max(1, int(duration_seconds / tick_interval))
    raw_label = item.get("label")
    mode_label = (
        raw_label.strip() if isinstance(raw_label, str) and raw_label.strip() else f"mode {mode_value}"
    )
    mode_assert = {
        "attribute": "1.LaundryWasherMode.CurrentMode",
        "value": mode_value,
        "description": f"{mode_label} mode",
    }
    return duration_ticks, [mode_assert]


def _get_dryer_params(
    attrs: Dict[str, Any], rng: random.Random, tick_interval: float = 0.1
) -> Tuple[int, List[Dict[str, Any]]]:
    
    dryness_duration_map = {0: 1800, 1: 2700, 2: 3600, 3: 4500}
    supported_dryness_levels = (
        attrs.get("1.LaundryDryerControls.SupportedDrynessLevels") or []
    )
    dryness = (
        int(rng.choice(supported_dryness_levels)) if supported_dryness_levels else 1
    )
    duration_ticks = int(dryness_duration_map.get(dryness, 2700) / tick_interval)
    dryness_assert = {
        "attribute": "1.LaundryDryerControls.SelectedDrynessLevel",
        "value": dryness,
        "description": f"{DrynessLevelEnum.label(dryness)} dryness level",
    }

    return duration_ticks, [dryness_assert]


def _get_rvc_params(
    attrs: Dict[str, Any], rng: random.Random, tick_interval: float = 0.1
) -> Tuple[int, List[Dict[str, Any]]]:
    
    return int(1800 / tick_interval), []


def _get_dishwasher_params(
    attrs: Dict[str, Any], rng: random.Random, tick_interval: float = 0.1
) -> Tuple[int, List[Dict[str, Any]]]:
    
    return int(5400 / tick_interval), []


def _get_default_params(
    attrs: Dict[str, Any], rng: random.Random, tick_interval: float = 0.1
) -> Tuple[int, List[Dict[str, Any]]]:
    
    return int(3600 / tick_interval), []


DEVICE_PARAM_SAMPLERS: Dict[
    str,
    Callable[[Dict[str, Any], random.Random, float], Tuple[int, List[Dict[str, Any]]]],
] = {
    "laundry_washer": _get_washer_params,
    "laundry_dryer": _get_dryer_params,
    "rvc": _get_rvc_params,
    "dishwasher": _get_dishwasher_params,
}


def _create_op_state_assert(device_type: str, state: int) -> Dict[str, Any]:
    
    attr = RVC_OP_STATE_ATTR if device_type.lower() == "rvc" else OP_STATE_ATTR
    return {
        "attribute": attr,
        "value": state,
        "description": (
            f"Running state"
            if state == OP_STATE_RUNNING
            else f"Paused state"
            if state == OP_STATE_PAUSED
            else f"Stopped state"
        ),
    }


def _sample_target_op_asserts_and_duration_ticks(
    *,
    device: Dict[str, Any],
    device_type: str,
    rng: random.Random,
    tick_interval: float = 0.1,
) -> tuple[int, list[Dict[str, Any]]]:
    
    dtype = (device_type or "").lower()
    attrs = (device or {}).get("attributes") or {}

    sampler = DEVICE_PARAM_SAMPLERS.get(dtype, _get_default_params)
    duration_ticks, custom_asserts = sampler(attrs, rng, tick_interval)

    base_asserts = []
    if dtype == "rvc":
        base_asserts.append(_create_op_state_assert(dtype, OP_STATE_RUNNING))
    else:
        if "1.OnOff" in (attrs or {}):
            base_asserts.append({"attribute": ONOFF_ATTR, "value": True})
        base_asserts.append(_create_op_state_assert(dtype, OP_STATE_RUNNING))

    return duration_ticks, base_asserts + custom_asserts


def _create_goal(
    *,
    reference_tick: int,
    relation: str,
    offset_ticks: int,
    tolerance_ticks: int,
    anchor: Dict[str, Any],
    target: Dict[str, Any],
    asserts: List[Dict[str, Any]],
    tick_interval: float = 0.1,
) -> Dict[str, Any]:
    
    return {
        "when": {
            "reference_tick": reference_tick,
            "reference_minutes": ticks_to_minutes(reference_tick, tick_interval),
            "relation": relation,
            "offset_ticks": offset_ticks,
            "offset_minutes": ticks_to_minutes(offset_ticks, tick_interval),
            "at_tick": reference_tick
            + (offset_ticks if relation == "after" else -offset_ticks),
            "at_minutes": ticks_to_minutes(
                reference_tick
                + (offset_ticks if relation == "after" else -offset_ticks),
                tick_interval,
            ),
            "tolerance_ticks": tolerance_ticks,
        },
        "anchor": anchor,
        "targets": [{**target, "asserts": asserts}],
    }


def _resolve_device_from_snapshot(
    *, snapshot: Dict[str, Any], room_id: str, device_id: str
) -> Dict[str, Any]:
    rooms = snapshot.get("rooms")
    if not isinstance(rooms, dict):
        raise ValueError("snapshot.rooms must be a mapping")
    room_data = rooms.get(room_id)
    if not isinstance(room_data, dict):
        raise ValueError(f"Room '{room_id}' not found in snapshot")
    devices = room_data.get("devices")
    if not isinstance(devices, list):
        raise ValueError(f"Room '{room_id}' has no device list in snapshot")

    for device in devices:
        if not isinstance(device, dict):
            continue
        if str(device.get("device_id")) == device_id:
            return device

    raise ValueError(
        f"Device '{device_id}' not found in snapshot room '{room_id}'"
    )


def build_qt4_3_feasible_payload(
    *, seed: int,
    home_schema: dict[str, object],
    base_time: str = "2025-08-23 00:00:00"
) -> Dict[str, Any]:
    
    seed = ensure_seed(seed, context="qt4-3 feasible payload")
    rng = random.Random(seed)

    base_cfg = HomeConfigInitializer(
        seed=seed,
        base_time=base_time,
        home_spec=home_schema,
    ).create_config()
    targets = sample_op_device(
        cast(Dict[str, Any], cast(object, base_cfg)),
        rng=rng,
        sample_running_anchor=False,
        k=1,
    )
    exclude_devices_by_room = {room_id: [dev["device_id"]] for room_id, dev in targets}
    snapshot = augment_home(
        home_config=base_cfg, seed=seed, exclude_devices_by_room=exclude_devices_by_room
    )

    user_location = sample_user_location(snapshot, rng=rng)
    tick_interval = float(snapshot.get("tick_interval", 0.1))
    tolerance_ticks = get_tolerance_ticks(
        tolerance_seconds=30, tick_interval=tick_interval
    )
    pre_goal_offset_ticks = 2 * tolerance_ticks

    anchors = sample_op_device(snapshot, rng=rng, sample_running_anchor=True)

    goals = []
    required_actions = []
    scenario = "not_set"

    for anchor_room_id, anchor_device in anchors:
        anchor_end_tick = get_running_anchor_end_tick(
            anchor_device=anchor_device, tick_interval=tick_interval
        )

        for target_room_id, target_device in targets:
            target_device_id = str(target_device["device_id"])
            resolved_target_device = _resolve_device_from_snapshot(
                snapshot=snapshot,
                room_id=target_room_id,
                device_id=target_device_id,
            )
            target_duration_ticks, running_asserts = (
                _sample_target_op_asserts_and_duration_ticks(
                    device=resolved_target_device,
                    device_type=resolved_target_device["device_type"],
                    rng=rng,
                )
            )

            anchor_info = {
                "room_id": anchor_room_id,
                "device_id": anchor_device["device_id"],
                "device_type": anchor_device["device_type"],
            }
            target_info = {
                "room_id": target_room_id,
                "device_id": target_device_id,
                "device_type": resolved_target_device["device_type"],
            }
            dtype = resolved_target_device["device_type"]

            if anchor_end_tick > target_duration_ticks:
                if rng.random() < 0.5:
                    scenario = "delayed_start"
                    n_minutes = rng.randint(5, 20)
                    delay_ticks = minutes_to_ticks(n_minutes, tick_interval)

                    pre_goal_assert = [_create_op_state_assert(dtype, OP_STATE_STOPPED)]
                    goals.append(
                        _create_goal(
                            reference_tick=anchor_end_tick + delay_ticks,
                            relation="before",
                            offset_ticks=pre_goal_offset_ticks,
                            tolerance_ticks=0,
                            anchor=anchor_info,
                            target=target_info,
                            asserts=pre_goal_assert,
                        )
                    )
                    goals.append(
                        _create_goal(
                            reference_tick=anchor_end_tick,
                            relation="after",
                            offset_ticks=delay_ticks,
                            tolerance_ticks=tolerance_ticks,
                            anchor=anchor_info,
                            target=target_info,
                            asserts=running_asserts,
                        )
                    )

                else:
                    scenario = "align_end_with_anchor"
                    goals.append(
                        _create_goal(
                            reference_tick=anchor_end_tick,
                            relation="before",
                            offset_ticks=pre_goal_offset_ticks,
                            tolerance_ticks=0,
                            anchor=anchor_info,
                            target=target_info,
                            asserts=running_asserts,
                        )
                    )
                    stopped_assert = [_create_op_state_assert(dtype, OP_STATE_STOPPED)]
                    goals.append(
                        _create_goal(
                            reference_tick=anchor_end_tick,
                            relation="after",
                            offset_ticks=0,
                            tolerance_ticks=tolerance_ticks,
                            anchor=anchor_info,
                            target=target_info,
                            asserts=stopped_assert,
                        )
                    )

            else:
                scenario = "pause_at_anchor_end"
                goals.append(
                    _create_goal(
                        reference_tick=anchor_end_tick,
                        relation="before",
                        offset_ticks=pre_goal_offset_ticks,
                        tolerance_ticks=0,
                        anchor=anchor_info,
                        target=target_info,
                        asserts=running_asserts,
                    )
                )
                paused_assert = [_create_op_state_assert(dtype, OP_STATE_PAUSED)]
                goals.append(
                    _create_goal(
                        reference_tick=anchor_end_tick,
                        relation="after",
                        offset_ticks=0,
                        tolerance_ticks=tolerance_ticks,
                        anchor=anchor_info,
                        target=target_info,
                        asserts=paused_assert,
                    )
                )

            required_actions.append(
                {"tool": "get_room_devices", "params": {"room_id": target_room_id}}
            )

    goals.sort(key=lambda g: g["when"]["at_tick"])
    required_actions = deduplicate_required_actions(required_actions)

    return assemble_payload(
        seed=seed,
        query_type="qt4-3",
        case="feasible",
        snapshot=snapshot,
        user_location=user_location,
        required_actions=required_actions,
        goals=goals,
        meta_extras={"scenario": scenario},
    )


__all__ = [
    "build_qt4_3_feasible_payload",
]
