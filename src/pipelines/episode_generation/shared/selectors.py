from __future__ import annotations

import math
from typing import Any, Dict, List, Tuple, Iterable
import random


OP_DEVICE_TYPES: Tuple[str, ...] = (
    "dishwasher",
    "laundry_washer",
    "laundry_dryer",
    "rvc",
)


def sample_user_location(snapshot: Dict[str, Any], *, rng: random.Random) -> str:
    rooms = snapshot.get("rooms")
    if not rooms:
        raise ValueError("No rooms in snapshot")
    return rng.choice(list(rooms.keys()))


def list_devices_in_config(cfg: Dict[str, Any]) -> Iterable[Tuple[str, Dict[str, Any]]]:
    rooms = (cfg or {}).get("rooms") or {}
    for rid, rc in rooms.items():
        for d in (rc.get("devices") or []):
            yield rid, d


def sample_op_device(
    snapshot: Dict[str, Any], *, rng: random.Random, sample_running_anchor: bool = False, k: int = 1
) -> List[Tuple[str, Dict[str, Any]]]:
    candidates: List[Tuple[str, Dict[str, Any]]] = []
    for room_id, devices_dict in snapshot["rooms"].items():
        for device in devices_dict["devices"]:
            if device["device_type"] not in OP_DEVICE_TYPES:
                continue
            attrs = device["attributes"]
            prefix = (
                "1.RVCOperationalState" if device["device_type"] == "rvc" else "1.OperationalState"
            )
            operational_state = attrs.get(f"{prefix}.OperationalState")
            countdown_time = attrs.get(f"{prefix}.CountdownTime")
            if (
                sample_running_anchor
                and isinstance(operational_state, int)
                and not isinstance(operational_state, bool)
                and operational_state == 1
                and isinstance(countdown_time, (int, float))
                and math.isfinite(float(countdown_time))
                and countdown_time > 0
            ):
                candidates.append((room_id, device))
            elif (
                not sample_running_anchor
                and isinstance(operational_state, int)
                and not isinstance(operational_state, bool)
                and operational_state == 0
            ):
                candidates.append((room_id, device))
            elif not sample_running_anchor:
                candidates.append((room_id, device))
    if not candidates:
        raise ValueError(
            "QT4 OP: No RUNNING OP device (incl. RVC) with positive CountdownTime found in snapshot"
        )
    return rng.sample(candidates, k=min(k, len(candidates)))


def sample_non_op_device(snapshot: Dict[str, Any], *, rng: random.Random, k: int = 1) -> List[Tuple[str, Dict[str, Any]]]:
    candidates: List[Tuple[str, Dict[str, Any]]] = []
    for room_id, devices_dict in snapshot["rooms"].items():
        for device in devices_dict["devices"]:
            device_type = device["device_type"]
            if device_type in OP_DEVICE_TYPES:
                continue
            candidates.append((room_id, device))
    if not candidates:
        raise ValueError("QT4 OP: No non-OP device found in snapshot")
    return rng.sample(candidates, k=min(k, len(candidates)))


__all__ = [
    "OP_DEVICE_TYPES",
    "sample_user_location",
    "list_devices_in_config",
    "sample_op_device",
    "sample_non_op_device",
]
