from __future__ import annotations

import random
from typing import Any, Dict, List, Optional, Tuple

from src.pipelines.episode_generation.core.guard_registry import (
    is_readonly,
    get_value_bins,
    get_value_range,
    get_enum_values,
    validate_relations,
)


def _get_flat(
    state: Dict[str, Any], endpoint_id: int, cluster_id: str, attribute_id: str
) -> Any:
    if state is None:
        return None
    return state.get(f"{endpoint_id}.{cluster_id}.{attribute_id}")


def _pick_from_bins(
    rng: random.Random, bins: Tuple[Tuple[int, int], ...], current: Optional[int]
) -> Optional[int]:
    if not bins:
        return None

    candidate_bins: List[Tuple[int, int]] = list(bins)
    if isinstance(current, int):
        for lo, hi in bins:
            if lo <= current <= hi and len(candidate_bins) > 1:
                candidate_bins = [b for b in bins if b != (lo, hi)]
                break
    lo, hi = rng.choice(candidate_bins)
    return lo if lo == hi else rng.randint(lo, hi)


def _pick_from_range(
    rng: random.Random, lo: int, hi: int, step: int, current: Optional[int]
) -> Optional[int]:
    if lo > hi or step <= 0:
        return None
    values = list(range(lo, hi + 1, step))
    if len(values) == 0:
        return None
    if isinstance(current, int) and current in values and len(values) > 1:
        values = [v for v in values if v != current]
    return rng.choice(values)


def _choose_fancontrol_candidate(
    *, rng: random.Random, device_type: str, state: Dict[str, Any]
) -> Optional[Dict[str, Any]]:
    endpoint_id = 1
    cluster_id = "FanControl"

    onoff = _get_flat(state, endpoint_id, "OnOff", "OnOff")
    if isinstance(onoff, bool) and not onoff:
        return {
            "api": {
                "api_type": "execute_command",
                "endpoint_id": endpoint_id,
                "cluster_id": "OnOff",
                "command_id": "On",
                "args": {},
            }
        }

    bins = get_value_bins(device_type, cluster_id, "PercentSetting")
    current = _get_flat(state, endpoint_id, cluster_id, "PercentSetting")
    value = _pick_from_bins(rng, bins, current)
    if value is not None and not is_readonly(cluster_id, "PercentSetting"):
        if current != value:
            return {
                "api": {
                    "api_type": "write_attribute",
                    "endpoint_id": endpoint_id,
                    "cluster_id": cluster_id,
                    "attribute_id": "PercentSetting",
                    "value": int(value),
                }
            }

    direction = rng.choice([0, 1])
    return {
        "api": {
            "api_type": "execute_command",
            "endpoint_id": endpoint_id,
            "cluster_id": cluster_id,
            "command_id": "Step",
            "args": {"Direction": direction},
        }
    }


def _choose_levelcontrol_candidate(
    *, rng: random.Random, device_type: str, state: Dict[str, Any]
) -> Optional[Dict[str, Any]]:
    endpoint_id = 1
    cluster_id = "LevelControl"

    onoff = _get_flat(state, endpoint_id, "OnOff", "OnOff")
    if isinstance(onoff, bool) and not onoff:
        return {
            "api": {
                "api_type": "execute_command",
                "endpoint_id": endpoint_id,
                "cluster_id": "OnOff",
                "command_id": "On",
                "args": {},
            }
        }

    min_level = _get_flat(state, endpoint_id, cluster_id, "MinLevel") or 1
    max_level = _get_flat(state, endpoint_id, cluster_id, "MaxLevel") or 254
    level = _pick_from_range(rng, int(min_level), int(max_level), 10, None)
    if level is None:
        return None
    return {
        "api": {
            "api_type": "execute_command",
            "endpoint_id": endpoint_id,
            "cluster_id": cluster_id,
            "command_id": "MoveToLevel",
            "args": {"Level": int(level)},
        }
    }


def _choose_thermostat_candidate(
    *, rng: random.Random, device_type: str, state: Dict[str, Any]
) -> Optional[Dict[str, Any]]:

    endpoint_id = 4 if device_type == "heat_pump" else 1
    cluster_id = "Thermostat"

    current_mode = _get_flat(state, endpoint_id, cluster_id, "SystemMode")
    if device_type == "air_conditioner":
        target_mode = 0x03  
        if current_mode != target_mode and not is_readonly(cluster_id, "SystemMode"):
            return {
                "api": {
                    "api_type": "write_attribute",
                    "endpoint_id": endpoint_id,
                    "cluster_id": cluster_id,
                    "attribute_id": "SystemMode",
                    "value": target_mode,
                }
            }
    elif device_type == "heat_pump":
        target_mode = 0x04  
        if current_mode != target_mode and not is_readonly(cluster_id, "SystemMode"):
            return {
                "api": {
                    "api_type": "write_attribute",
                    "endpoint_id": endpoint_id,
                    "cluster_id": cluster_id,
                    "attribute_id": "SystemMode",
                    "value": target_mode,
                }
            }
    else:

        enum_vals = list(get_enum_values(device_type, cluster_id, "SystemMode"))
        if enum_vals:
            choices = [v for v in enum_vals if v != current_mode] or enum_vals
            mode = int(rng.choice(choices))
            if not is_readonly(cluster_id, "SystemMode"):
                return {
                    "api": {
                        "api_type": "write_attribute",
                        "endpoint_id": endpoint_id,
                        "cluster_id": cluster_id,
                        "attribute_id": "SystemMode",
                        "value": mode,
                    }
                }

    def _pick_setpoint(attr: str) -> Optional[int]:
        r = get_value_range(device_type, cluster_id, attr)
        if not r:
            return None
        lo, hi, step = r
        current = _get_flat(state, endpoint_id, cluster_id, attr)
        return _pick_from_range(
            rng, lo, hi, step, current if isinstance(current, int) else None
        )

    if device_type == "air_conditioner":
        attr = "OccupiedCoolingSetpoint"
        val = _pick_setpoint(attr)
        if val is not None and not is_readonly(cluster_id, attr):
            current = _get_flat(state, endpoint_id, cluster_id, attr)
            if current != val:
                proposed = {(endpoint_id, cluster_id, attr): int(val)}
                if validate_relations(
                    device_type=device_type, current=state, proposed_changes=proposed
                ):
                    return {
                        "api": {
                            "api_type": "write_attribute",
                            "endpoint_id": endpoint_id,
                            "cluster_id": cluster_id,
                            "attribute_id": attr,
                            "value": int(val),
                        }
                    }

    if device_type == "heat_pump":
        attr = "OccupiedHeatingSetpoint"
        val = _pick_setpoint(attr)
        if val is not None and not is_readonly(cluster_id, attr):
            current = _get_flat(state, endpoint_id, cluster_id, attr)
            if current != val:
                proposed = {(endpoint_id, cluster_id, attr): int(val)}
                if validate_relations(
                    device_type=device_type, current=state, proposed_changes=proposed
                ):
                    return {
                        "api": {
                            "api_type": "write_attribute",
                            "endpoint_id": endpoint_id,
                            "cluster_id": cluster_id,
                            "attribute_id": attr,
                            "value": int(val),
                        }
                    }

    for attr in ("OccupiedHeatingSetpoint", "OccupiedCoolingSetpoint"):
        val = _pick_setpoint(attr)
        if val is not None and not is_readonly(cluster_id, attr):
            current = _get_flat(state, endpoint_id, cluster_id, attr)
            if current != val:
                proposed = {(endpoint_id, cluster_id, attr): int(val)}
                if validate_relations(
                    device_type=device_type, current=state, proposed_changes=proposed
                ):
                    return {
                        "api": {
                            "api_type": "write_attribute",
                            "endpoint_id": endpoint_id,
                            "cluster_id": cluster_id,
                            "attribute_id": attr,
                            "value": int(val),
                        }
                    }

    return None


def _choose_tv_channel_candidate(
    *, rng: random.Random, device_type: str, state: Dict[str, Any]
) -> Optional[Dict[str, Any]]:
    endpoint_id = 1
    cluster_id = "Channel"

    onoff = _get_flat(state, endpoint_id, "OnOff", "OnOff")
    if isinstance(onoff, bool) and not onoff:
        return {
            "api": {
                "api_type": "execute_command",
                "endpoint_id": endpoint_id,
                "cluster_id": "OnOff",
                "command_id": "On",
                "args": {},
            }
        }

    count = rng.choice([-1, 1])
    return {
        "api": {
            "api_type": "execute_command",
            "endpoint_id": endpoint_id,
            "cluster_id": cluster_id,
            "command_id": "SkipChannel",
            "args": {"count": count},
        }
    }


def _choose_dishwasher_candidate(
    *, rng: random.Random, state: Dict[str, Any]
) -> Optional[Dict[str, Any]]:
    endpoint_id = 1

    onoff = _get_flat(state, endpoint_id, "OnOff", "OnOff")
    if isinstance(onoff, bool) and not onoff:
        if rng.random() < 0.9:
            return {
                "api": {
                    "api_type": "execute_command",
                    "endpoint_id": endpoint_id,
                    "cluster_id": "OnOff",
                    "command_id": "On",
                    "args": {},
                }
            }
        return None

    op_state = _get_flat(state, endpoint_id, "OperationalState", "OperationalState")

    if op_state in (1, 2):
        if rng.random() < 0.2:
            return {
                "api": {
                    "api_type": "execute_command",
                    "endpoint_id": endpoint_id,
                    "cluster_id": "OperationalState",
                    "command_id": "Stop",
                    "args": {},
                }
            }
        if op_state == 2 and rng.random() < 0.6:
            return {
                "api": {
                    "api_type": "execute_command",
                    "endpoint_id": endpoint_id,
                    "cluster_id": "OperationalState",
                    "command_id": "Resume",
                    "args": {},
                }
            }
        return None

    if op_state == 0:
        if rng.random() < 0.6:
            modes = _get_flat(state, endpoint_id, "DishwasherMode", "SupportedModes")
            if isinstance(modes, list) and modes:
                pick = rng.choice(modes)
                if isinstance(pick, dict):
                    mode_value = pick.get("mode")
                    if isinstance(mode_value, int) and not isinstance(mode_value, bool):
                        new_mode = mode_value
                    else:
                        new_mode = None
                else:
                    new_mode = None
            else:
                new_mode = None
            if new_mode is not None:
                return {
                    "api": {
                        "api_type": "execute_command",
                        "endpoint_id": endpoint_id,
                        "cluster_id": "DishwasherMode",
                        "command_id": "ChangeToMode",
                        "args": {"new_mode": int(new_mode)},
                    }
                }

        return {
            "api": {
                "api_type": "execute_command",
                "endpoint_id": endpoint_id,
                "cluster_id": "OperationalState",
                "command_id": "Start",
                "args": {},
            }
        }
    return None


def _choose_washer_candidate(
    *, rng: random.Random, state: Dict[str, Any]
) -> Optional[Dict[str, Any]]:
    endpoint_id = 1

    onoff = _get_flat(state, endpoint_id, "OnOff", "OnOff")
    if isinstance(onoff, bool) and not onoff:
        if rng.random() < 0.9:
            return {
                "api": {
                    "api_type": "execute_command",
                    "endpoint_id": endpoint_id,
                    "cluster_id": "OnOff",
                    "command_id": "On",
                    "args": {},
                }
            }
        return None

    op_state = _get_flat(state, endpoint_id, "OperationalState", "OperationalState")

    if op_state in (1, 2):

        if rng.random() < 0.2:
            return {
                "api": {
                    "api_type": "execute_command",
                    "endpoint_id": endpoint_id,
                    "cluster_id": "OperationalState",
                    "command_id": "Stop",
                    "args": {},
                }
            }
        if op_state == 2 and rng.random() < 0.6:
            return {
                "api": {
                    "api_type": "execute_command",
                    "endpoint_id": endpoint_id,
                    "cluster_id": "OperationalState",
                    "command_id": "Resume",
                    "args": {},
                }
            }
        return None

    if op_state == 0:
        if rng.random() < 0.6:
            modes = _get_flat(state, endpoint_id, "LaundryWasherMode", "SupportedModes")
            if isinstance(modes, list) and modes:
                pick = rng.choice(modes)
                if isinstance(pick, dict):
                    mode_value = pick.get("mode")
                    if isinstance(mode_value, int) and not isinstance(mode_value, bool):
                        new_mode = mode_value
                    else:
                        new_mode = None
                else:
                    new_mode = None
            else:
                new_mode = None
            if new_mode is not None:
                return {
                    "api": {
                        "api_type": "execute_command",
                        "endpoint_id": endpoint_id,
                        "cluster_id": "LaundryWasherMode",
                        "command_id": "ChangeToMode",
                        "args": {"new_mode": int(new_mode)},
                    }
                }

        return {
            "api": {
                "api_type": "execute_command",
                "endpoint_id": endpoint_id,
                "cluster_id": "OperationalState",
                "command_id": "Start",
                "args": {},
            }
        }
    return None


def _choose_dryer_candidate(
    *, rng: random.Random, state: Dict[str, Any]
) -> Optional[Dict[str, Any]]:
    endpoint_id = 1

    onoff = _get_flat(state, endpoint_id, "OnOff", "OnOff")
    if isinstance(onoff, bool) and not onoff:
        if rng.random() < 0.9:
            return {
                "api": {
                    "api_type": "execute_command",
                    "endpoint_id": endpoint_id,
                    "cluster_id": "OnOff",
                    "command_id": "On",
                    "args": {},
                }
            }
        return None

    op_state = _get_flat(state, endpoint_id, "OperationalState", "OperationalState")

    if op_state in (1, 2):
        r = rng.random()
        if r < 0.2:
            return {
                "api": {
                    "api_type": "execute_command",
                    "endpoint_id": endpoint_id,
                    "cluster_id": "OperationalState",
                    "command_id": "Stop",
                    "args": {},
                }
            }
        if op_state == 2 and r < 0.8:
            return {
                "api": {
                    "api_type": "execute_command",
                    "endpoint_id": endpoint_id,
                    "cluster_id": "OperationalState",
                    "command_id": "Resume",
                    "args": {},
                }
            }
        return None

    if op_state == 0:
        roll = rng.random()
        if roll < 0.5:
            levels = _get_flat(
                state, endpoint_id, "LaundryDryerControls", "SupportedDrynessLevels"
            )
            new_level = None
            try:
                if isinstance(levels, list) and levels:
                    new_level = int(rng.choice(levels))
            except Exception:
                new_level = None
            if new_level is not None:
                return {
                    "api": {
                        "api_type": "write_attribute",
                        "endpoint_id": endpoint_id,
                        "cluster_id": "LaundryDryerControls",
                        "attribute_id": "SelectedDrynessLevel",
                        "value": int(new_level),
                    }
                }
        return {
            "api": {
                "api_type": "execute_command",
                "endpoint_id": endpoint_id,
                "cluster_id": "OperationalState",
                "command_id": "Start",
                "args": {},
            }
        }
    return None


def _choose_rvc_candidate(
    *, rng: random.Random, device_type: str, state: Dict[str, Any]
) -> Optional[Dict[str, Any]]:
    _ = device_type
    endpoint_id = 1
    run_mode = _get_flat(state, endpoint_id, "RVCRunMode", "CurrentMode")
    rvc_state = _get_flat(state, endpoint_id, "RVCOperationalState", "OperationalState")
    run_supported = _get_flat(state, endpoint_id, "RVCRunMode", "SupportedModes")
    clean_supported = _get_flat(state, endpoint_id, "RVCCleanMode", "SupportedModes")

    TAG_IDLE = 0x4000
    TAG_CLEANING = 0x4001
    TAG_MAPPING = 0x4002

    OP_RUNNING = 0x01
    OP_PAUSED = 0x02
    OP_SEEKING_CHARGER = 0x40
    OP_CHARGING = 0x41
    OP_DOCKED = 0x42

    def _extract_mode_ids(supported_modes: Any) -> list[int]:
        mode_ids: list[int] = []
        if not isinstance(supported_modes, list):
            return mode_ids
        for mode_entry in supported_modes:
            if not isinstance(mode_entry, dict):
                continue
            raw_mode = mode_entry.get("Mode")
            if isinstance(raw_mode, int):
                mode_ids.append(int(raw_mode))
        return mode_ids

    def _extract_modes_with_tag(supported_modes: Any, target_tag: int) -> list[int]:
        mode_ids: list[int] = []
        if not isinstance(supported_modes, list):
            return mode_ids

        for mode_entry in supported_modes:
            if not isinstance(mode_entry, dict):
                continue

            raw_mode = mode_entry.get("Mode")
            if not isinstance(raw_mode, int):
                continue

            tags = mode_entry.get("ModeTags")
            if not isinstance(tags, list):
                continue

            normalized_tags = {int(tag) for tag in tags if isinstance(tag, int)}
            if target_tag in normalized_tags:
                mode_ids.append(int(raw_mode))

        return mode_ids

    idle_modes = _extract_modes_with_tag(run_supported, TAG_IDLE)
    cleaning_modes = _extract_modes_with_tag(run_supported, TAG_CLEANING)
    mapping_modes = _extract_modes_with_tag(run_supported, TAG_MAPPING)
    non_idle_modes = cleaning_modes + [m for m in mapping_modes if m not in cleaning_modes]
    clean_mode_ids = _extract_mode_ids(clean_supported)

    current_mode: Optional[int] = int(run_mode) if isinstance(run_mode, int) else None
    is_idle = current_mode in idle_modes if current_mode is not None else True

    options: list[tuple[str, str, Dict[str, Any]]] = []

    if rvc_state == OP_RUNNING:
        if current_mode is not None and not is_idle and idle_modes:
            options.append(
                ("RVCRunMode", "ChangeToMode", {"new_mode": int(rng.choice(idle_modes))})
            )
        options.extend(
            [
                ("RVCOperationalState", "Pause", {}),
                ("RVCOperationalState", "GoHome", {}),
            ]
        )

    elif rvc_state == OP_PAUSED:
        options.extend(
            [
                ("RVCOperationalState", "Resume", {}),
                ("RVCOperationalState", "GoHome", {}),
            ]
        )

    elif rvc_state == OP_SEEKING_CHARGER:
        options.append(("RVCOperationalState", "Pause", {}))

    elif rvc_state in (OP_CHARGING, OP_DOCKED):
        if current_mode is not None and not is_idle:
            options.append(("RVCOperationalState", "Resume", {}))
        elif non_idle_modes:
            options.append(
                (
                    "RVCRunMode",
                    "ChangeToMode",
                    {"new_mode": int(rng.choice(non_idle_modes))},
                )
            )
        if clean_mode_ids and (is_idle or current_mode is None):
            options.append(
                (
                    "RVCCleanMode",
                    "ChangeToMode",
                    {"mode": int(rng.choice(clean_mode_ids))},
                )
            )

    else:
        if non_idle_modes:
            options.append(
                (
                    "RVCRunMode",
                    "ChangeToMode",
                    {"new_mode": int(rng.choice(non_idle_modes))},
                )
            )
        if clean_mode_ids and (is_idle or current_mode is None):
            options.append(
                (
                    "RVCCleanMode",
                    "ChangeToMode",
                    {"mode": int(rng.choice(clean_mode_ids))},
                )
            )

    if not options:
        return None

    cluster_id, command_id, args = rng.choice(options)
    return {
        "api": {
            "api_type": "execute_command",
            "endpoint_id": endpoint_id,
            "cluster_id": cluster_id,
            "command_id": command_id,
            "args": args,
        }
    }


def _choose_temperature_control_candidate(
    *, rng: random.Random, device_type: str, state: Dict[str, Any]
) -> Optional[Dict[str, Any]]:
    
    endpoint_id = 1
    cluster_id = "TemperatureControl"

    min_temp = _get_flat(state, endpoint_id, cluster_id, "MinTemperature")
    max_temp = _get_flat(state, endpoint_id, cluster_id, "MaxTemperature")
    current = _get_flat(state, endpoint_id, cluster_id, "TemperatureSetpoint")
    step = _get_flat(state, endpoint_id, cluster_id, "Step") or 100

    try:
        lo = int(min_temp) if isinstance(min_temp, int) else 500
        hi = int(max_temp) if isinstance(max_temp, int) else 3000
        step = int(step)
    except Exception:
        lo, hi, step = 500, 3000, 100

    value = _pick_from_range(
        rng,
        lo,
        hi,
        step,
        current if isinstance(current, int) else None,
    )
    if value is None:
        return None

    return {
        "api": {
            "api_type": "execute_command",
            "endpoint_id": endpoint_id,
            "cluster_id": cluster_id,
            "command_id": "SetTemperature",
            "args": {"target_temperature": int(value)},
        }
    }


def _choose_window_covering_candidate(
    *, rng: random.Random, device_type: str, state: Dict[str, Any]
) -> Optional[Dict[str, Any]]:
    
    endpoint_id = 1
    cluster_id = "WindowCovering"

    safety = _get_flat(state, endpoint_id, cluster_id, "SafetyStatus")
    if isinstance(safety, int) and safety != 0:
        return {
            "api": {
                "api_type": "execute_command",
                "endpoint_id": endpoint_id,
                "cluster_id": cluster_id,
                "command_id": "StopMotion",
                "args": {},
            }
        }

    current = _get_flat(
        state, endpoint_id, cluster_id, "CurrentPositionLiftPercent100ths"
    )
    if not isinstance(current, int):
        current = 0

    choice = rng.choice(["UpOrOpen", "DownOrClose", "GoToLiftPercentage"])
    if choice in ("UpOrOpen", "DownOrClose"):
        return {
            "api": {
                "api_type": "execute_command",
                "endpoint_id": endpoint_id,
                "cluster_id": cluster_id,
                "command_id": choice,
                "args": {},
            }
        }

    target = current
    for _ in range(3):
        candidate_val = rng.randint(0, 10000)
        if candidate_val != current:
            target = candidate_val
            break
    if target == current:
        target = 0 if current != 0 else 10000

    return {
        "api": {
            "api_type": "execute_command",
            "endpoint_id": endpoint_id,
            "cluster_id": cluster_id,
            "command_id": "GoToLiftPercentage",
            "args": {"lift_percent_100ths": int(target)},
        }
    }


def _choose_electrical_sensor_candidate(
    *, rng: random.Random, device_type: str, state: Dict[str, Any]
) -> Optional[Dict[str, Any]]:
    _ = (rng, device_type, state)
    return None


def _choose_onoff_candidate(
    *, rng: random.Random, device_type: str, state: Dict[str, Any]
) -> Optional[Dict[str, Any]]:
    endpoint_id = 1
    cluster_id = "OnOff"

    current = _get_flat(state, endpoint_id, cluster_id, "OnOff")
    if isinstance(current, bool):
        cmd = "On" if not current else "Off"
    else:
        cmd = rng.choice(["On", "Off"])
    return {
        "api": {
            "api_type": "execute_command",
            "endpoint_id": endpoint_id,
            "cluster_id": cluster_id,
            "command_id": cmd,
            "args": {},
        }
    }


def sample_candidate(
    *,
    device_type: str,
    device_id: str,
    state_flat: Dict[str, Any],
    seed: Optional[int] = None,
) -> Optional[Dict[str, Any]]:
    
    rng = random.Random(seed)

    if device_type == "dimmable_light":

        onoff_flag = _get_flat(state_flat, 1, "OnOff", "OnOff")
        if isinstance(onoff_flag, bool) and not onoff_flag:
            return _choose_onoff_candidate(
                rng=rng, device_type=device_type, state=state_flat
            )
        cand = _choose_levelcontrol_candidate(
            rng=rng, device_type=device_type, state=state_flat
        )
        return cand or _choose_onoff_candidate(
            rng=rng, device_type=device_type, state=state_flat
        )

    if device_type == "air_purifier":
        return _choose_fancontrol_candidate(
            rng=rng, device_type=device_type, state=state_flat
        )

    if device_type == "air_conditioner":

        onoff_flag = _get_flat(state_flat, 1, "OnOff", "OnOff")
        if isinstance(onoff_flag, bool) and not onoff_flag:
            return _choose_onoff_candidate(
                rng=rng, device_type=device_type, state=state_flat
            )
        cand = _choose_thermostat_candidate(
            rng=rng, device_type=device_type, state=state_flat
        )
        return cand or _choose_fancontrol_candidate(
            rng=rng, device_type=device_type, state=state_flat
        )

    if device_type == "humidifier":
        return _choose_fancontrol_candidate(
            rng=rng, device_type=device_type, state=state_flat
        )

    if device_type == "dehumidifier":
        return _choose_fancontrol_candidate(
            rng=rng, device_type=device_type, state=state_flat
        )

    if device_type == "tv":

        onoff_flag = _get_flat(state_flat, 1, "OnOff", "OnOff")
        if isinstance(onoff_flag, bool) and not onoff_flag:
            return _choose_onoff_candidate(
                rng=rng, device_type=device_type, state=state_flat
            )
        return _choose_tv_channel_candidate(
            rng=rng, device_type=device_type, state=state_flat
        )

    if device_type == "heat_pump":

        return _choose_thermostat_candidate(
            rng=rng, device_type=device_type, state=state_flat
        )

    if device_type == "dishwasher":
        return _choose_dishwasher_candidate(rng=rng, state=state_flat)
    if device_type == "laundry_washer":
        return _choose_washer_candidate(rng=rng, state=state_flat)
    if device_type == "laundry_dryer":
        return _choose_dryer_candidate(rng=rng, state=state_flat)

    if device_type == "rvc":
        return _choose_rvc_candidate(rng=rng, device_type=device_type, state=state_flat)

    if device_type in ("refrigerator", "freezer"):
        return _choose_temperature_control_candidate(
            rng=rng, device_type=device_type, state=state_flat
        )

    if device_type == "electrical_sensor":
        return _choose_electrical_sensor_candidate(
            rng=rng, device_type=device_type, state=state_flat
        )

    if device_type == "fan":

        onoff_flag = _get_flat(state_flat, 1, "OnOff", "OnOff")
        if isinstance(onoff_flag, bool) and not onoff_flag:
            return _choose_onoff_candidate(
                rng=rng, device_type=device_type, state=state_flat
            )
        return _choose_fancontrol_candidate(
            rng=rng, device_type=device_type, state=state_flat
        )

    if device_type == "on_off_light":
        return _choose_onoff_candidate(
            rng=rng, device_type=device_type, state=state_flat
        )

    if device_type == "window_covering_controller":
        return _choose_window_covering_candidate(
            rng=rng, device_type=device_type, state=state_flat
        )

    return None


__all__ = ["sample_candidate"]
