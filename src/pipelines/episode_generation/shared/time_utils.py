from __future__ import annotations

import math
from datetime import datetime, timedelta
from typing import Any, Dict


def minutes_to_ticks(minutes: int, tick_interval: float) -> int:
    return int(
        max(1, math.ceil((float(minutes) * 60.0) / max(1e-6, float(tick_interval))))
    )


def seconds_to_ticks(seconds: int, tick_interval: float) -> int:
    return int(max(1, math.ceil((float(seconds) / max(1e-6, float(tick_interval))))))


def ticks_to_minutes(ticks: int, tick_interval: float = 0.1) -> int:
    return int(round(max(0.0, float(ticks) * float(tick_interval)) / 60.0))


def format_absolute_time(base_time: str, minutes: int) -> datetime:
    base_dt = datetime.fromisoformat(base_time)
    return base_dt + timedelta(minutes=minutes)


def format_time_12h(dt: datetime) -> str:
    hour = dt.hour
    minute = dt.minute

    if hour == 0:
        hour_str = "12"
        period = "AM"
    elif hour < 12:
        hour_str = str(hour)
        period = "AM"
    elif hour == 12:
        hour_str = "12"
        period = "PM"
    else:
        hour_str = str(hour - 12)
        period = "PM"

    if minute == 0:
        return f"{hour_str} {period}"
    else:
        return f"{hour_str}:{minute:02d} {period}"


def get_tolerance_ticks(tolerance_seconds: int, tick_interval: float = 0.1) -> int:
    return int(
        max(1, math.ceil((float(tolerance_seconds) / max(1e-6, float(tick_interval)))))
    )


def get_running_anchor_end_tick(
    *, anchor_device: Dict[str, Any], tick_interval: float
) -> int:
    attrs = anchor_device.get("attributes") or {}
    if str(anchor_device.get("device_type")) == "rvc":
        countdown_s = attrs.get("1.RVCOperationalState.CountdownTime")
    else:
        countdown_s = attrs.get("1.OperationalState.CountdownTime")

    raw_countdown: Any = countdown_s
    if isinstance(raw_countdown, bool) or not isinstance(raw_countdown, (int, float)):
        raise ValueError(
            "Running anchor requires numeric CountdownTime; received invalid type"
        )

    countdown_seconds = float(raw_countdown)
    if not math.isfinite(countdown_seconds):
        raise ValueError("Running anchor CountdownTime must be finite")
    if countdown_seconds <= 0:
        raise ValueError(
            "Running anchor CountdownTime must be > 0 for anchor end calculation"
        )

    return seconds_to_ticks(int(math.ceil(countdown_seconds)), tick_interval)


__all__ = [
    "minutes_to_ticks",
    "seconds_to_ticks",
    "ticks_to_minutes",
    "format_absolute_time",
    "format_time_12h",
    "get_tolerance_ticks",
    "get_running_anchor_end_tick",
]
