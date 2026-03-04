from __future__ import annotations

from typing import Any, Dict, Tuple


def format_room_state_value(room_state: str, raw_value: Any) -> Tuple[float, str]:
    if raw_value is None:
        raise ValueError(f"room_state '{room_state}' requires a numeric value")
    try:
        numeric = float(raw_value)
    except (TypeError, ValueError) as exc:
        raise ValueError(
            f"room_state '{room_state}' requires a numeric value, got {raw_value!r}"
        ) from exc

    if room_state == "temperature":
        return round(numeric / 100.0, 2), "°C"
    if room_state == "humidity":
        return round(numeric / 100.0, 2), "%"
    if room_state == "illuminance":
        return round(numeric, 2), "lux"
    if room_state == "pm10":
        return round(numeric, 2), "μg/m³"
    return round(numeric, 2), ""


def build_room_state_goal(
    room_id: str, room_state: str, raw_value: Any
) -> Dict[str, Any]:
    display_value, unit = format_room_state_value(room_state, raw_value)
    return {
        "variant": "room_state",
        "room_id": room_id,
        "room_state": room_state,
        "current_value": display_value,
        "unit": unit,
    }


__all__ = ["format_room_state_value", "build_room_state_goal"]
