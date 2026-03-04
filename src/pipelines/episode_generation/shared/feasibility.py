from __future__ import annotations

from typing import Any, Dict, List, Tuple


PM10_DECREASE_FLOOR = 1e-6


METRIC_TO_DEVICE_TYPES: Dict[str, List[str]] = {
    "temperature": ["air_conditioner", "heat_pump"],
    "pm10": ["air_purifier"],
    "illuminance": ["dimmable_light", "on_off_light"],
    "humidity": ["humidifier", "dehumidifier"],
}


DEVICE_TYPE_TO_DIRECTIONS: Dict[str, List[str]] = {
    "air_conditioner": ["decrease"],
    "heat_pump": ["increase"],
    "dimmable_light": ["increase", "decrease"],
    "on_off_light": ["increase", "decrease"],
    "air_purifier": ["decrease"],
    "humidifier": ["increase"],
    "dehumidifier": ["decrease"],
}


DEVICE_TYPE_TO_METRIC: Dict[str, str] = {
    "air_conditioner": "temperature",
    "heat_pump": "temperature",
    "air_purifier": "pm10",
    "dimmable_light": "illuminance",
    "on_off_light": "illuminance",
    "humidifier": "humidity",
    "dehumidifier": "humidity",
}


ENV_SEMANTIC_BOUNDS: Dict[str, Dict[str, Tuple[str, float]]] = {
    "illuminance": {
        "increase": ("<", 500.0),
        "decrease": (">", 300.0),
    },
    "temperature": {
        "decrease": (">", 2000.0),
        "increase": ("<", 3000.0),
    },
    "humidity": {
        "decrease": (">", 2500.0),
        "increase": ("<", 7000.0),
    },
    "pm10": {
        "decrease": (">", 10.0),
    },
}


def check_env_semantic_consistency(
    cfg: Dict[str, Any], room_id: str, metric: str, direction: str
) -> bool:
    bound = ENV_SEMANTIC_BOUNDS.get(metric, {}).get(direction)
    if bound is None:
        return True
    state = cfg["rooms"][room_id].get("state", {})
    value = state.get(metric)
    if value is None:
        return True
    op, threshold = bound
    if op == "<":
        return float(value) < threshold
    return float(value) > threshold

def get_devices_for_metric(
    room_devices: List[Dict[str, Any]], metric: str
) -> List[Dict[str, Any]]:
    relevant_device_types = METRIC_TO_DEVICE_TYPES.get(metric, [])
    return [
        device
        for device in room_devices
        if device["device_type"] in relevant_device_types
    ]


def check_temperature_feasibility(
    cfg: Dict[str, Any], room_id: str, direction: str
) -> bool:
    room_data = cfg["rooms"][room_id]
    devices = room_data["devices"]
    current_temp = room_data["state"]["temperature"]

    temp_devices = get_devices_for_metric(devices, "temperature")

    for device in temp_devices:
        device_type = device["device_type"]
        attributes = device["attributes"]

        if direction == "decrease":
            if device_type == "air_conditioner":
                is_on = attributes["1.OnOff.OnOff"]
                system_mode = attributes["1.Thermostat.SystemMode"]
                fan_current = attributes["1.FanControl.PercentCurrent"]
                cooling_setpoint = attributes.get(
                    "1.Thermostat.OccupiedCoolingSetpoint", 0
                )

                if (
                    is_on
                    and system_mode == 3
                    and fan_current == 100
                    and current_temp <= cooling_setpoint
                ):
                    continue
                else:
                    return True
            elif device_type == "heat_pump":
                system_mode = attributes["4.Thermostat.SystemMode"]
                heating_setpoint = attributes["4.Thermostat.OccupiedHeatingSetpoint"]
                if system_mode == 4 and current_temp <= heating_setpoint:
                    return True
        elif direction == "increase":
            if device_type == "heat_pump":
                system_mode = attributes["4.Thermostat.SystemMode"]
                heating_setpoint = attributes["4.Thermostat.OccupiedHeatingSetpoint"]
                if system_mode == 4 and current_temp <= heating_setpoint:
                    continue
                else:
                    return True
            elif device_type == "air_conditioner":
                is_on = attributes["1.OnOff.OnOff"]
                system_mode = attributes["1.Thermostat.SystemMode"]
                fan_current = attributes["1.FanControl.PercentCurrent"]
                cooling_setpoint = attributes["1.Thermostat.OccupiedCoolingSetpoint"]
                if (
                    is_on
                    and system_mode == 3
                    and fan_current > 0
                    and current_temp > cooling_setpoint
                ):
                    return True

    return False


def check_illuminance_feasibility(
    cfg: Dict[str, Any], room_id: str, direction: str
) -> bool:
    room_data = cfg["rooms"][room_id]
    devices = room_data["devices"]

    light_devices = get_devices_for_metric(devices, "illuminance")

    for device in light_devices:
        device_type = device["device_type"]
        attributes = device["attributes"]
        is_on = attributes["1.OnOff.OnOff"]

        if direction == "decrease":
            if device_type == "on_off_light":
                if is_on:
                    return True
            elif device_type == "dimmable_light":
                current_level = attributes["1.LevelControl.CurrentLevel"]
                min_level = attributes["1.LevelControl.MinLevel"]
                if is_on and current_level > min_level:
                    return True
        elif direction == "increase":
            if device_type == "on_off_light":
                if not is_on:
                    return True
            elif device_type == "dimmable_light":
                if not is_on:
                    return True
                else:
                    current_level = attributes["1.LevelControl.CurrentLevel"]
                    max_level = attributes["1.LevelControl.MaxLevel"]
                    if current_level < max_level:
                        return True

    return False


def check_humidity_feasibility(
    cfg: Dict[str, Any], room_id: str, direction: str
) -> bool:
    room_data = cfg["rooms"][room_id]
    devices = room_data["devices"]
    current_humidity = room_data["state"]["humidity"]

    humidity_devices = get_devices_for_metric(devices, "humidity")

    for device in humidity_devices:
        device_type = device["device_type"]
        attributes = device["attributes"]

        if direction == "decrease":
            if device_type == "dehumidifier":
                is_on = attributes["1.OnOff.OnOff"]
                fan_current = attributes["1.FanControl.PercentCurrent"]
                if (not is_on or fan_current < 100) and current_humidity > 1000:
                    return True
            elif device_type == "humidifier":
                is_on = attributes["1.OnOff.OnOff"]
                fan_current = attributes["1.FanControl.PercentCurrent"]
                if is_on and fan_current > 0:
                    return True
        elif direction == "increase":
            if device_type == "humidifier":
                is_on = attributes["1.OnOff.OnOff"]
                fan_current = attributes["1.FanControl.PercentCurrent"]
                if (not is_on or fan_current < 100) and current_humidity < 9000:
                    return True
            elif device_type == "dehumidifier":
                is_on = attributes["1.OnOff.OnOff"]
                fan_current = attributes["1.FanControl.PercentCurrent"]
                if is_on and fan_current > 0:
                    return True

    return False


def check_pm10_feasibility(cfg: Dict[str, Any], room_id: str, direction: str) -> bool:
    room_data = cfg["rooms"][room_id]
    devices = room_data["devices"]
    try:
        current_pm10 = float(room_data["state"]["pm10"])
    except KeyError as exc:
        missing_key = exc.args[0]
        raise KeyError(
            f"Room '{room_id}' is missing required state key '{missing_key}'"
        ) from exc
    except (TypeError, ValueError) as exc:
        raise ValueError(
            f"Room '{room_id}' has a non-numeric pm10 state: {room_data['state']['pm10']!r}"
        ) from exc

    if direction != "decrease":
        return False

    if current_pm10 <= PM10_DECREASE_FLOOR:
        return False

    pm10_devices = get_devices_for_metric(devices, "pm10")
    for device in pm10_devices:
        device_type = device["device_type"]
        attributes = device["attributes"]
        if device_type == "air_purifier":
            is_on = attributes["1.OnOff.OnOff"]
            fan_current = attributes["1.FanControl.PercentCurrent"]
            if not is_on or fan_current < 100:
                return True
    return False


def check_metric_feasibility(
    cfg: Dict[str, Any], room_id: str, metric: str, direction: str
) -> bool:
    if metric == "temperature":
        return check_temperature_feasibility(cfg, room_id, direction)
    elif metric == "illuminance":
        return check_illuminance_feasibility(cfg, room_id, direction)
    elif metric == "humidity":
        return check_humidity_feasibility(cfg, room_id, direction)
    elif metric == "pm10":
        return check_pm10_feasibility(cfg, room_id, direction)
    else:
        return False


__all__ = [
    "PM10_DECREASE_FLOOR",
    "METRIC_TO_DEVICE_TYPES",
    "DEVICE_TYPE_TO_DIRECTIONS",
    "DEVICE_TYPE_TO_METRIC",
    "ENV_SEMANTIC_BOUNDS",
    "get_devices_for_metric",
    "check_temperature_feasibility",
    "check_illuminance_feasibility",
    "check_humidity_feasibility",
    "check_pm10_feasibility",
    "check_metric_feasibility",
    "check_env_semantic_consistency",
]
