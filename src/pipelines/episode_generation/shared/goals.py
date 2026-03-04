from __future__ import annotations

from typing import Any, Dict, Iterable, List, Tuple
import copy
import random

from src.pipelines.episode_generation.shared.feasibility import (
    METRIC_TO_DEVICE_TYPES,
    DEVICE_TYPE_TO_DIRECTIONS,
    DEVICE_TYPE_TO_METRIC,
    check_metric_feasibility,
    check_env_semantic_consistency,
)


def count_rooms_and_devices(cfg: Dict[str, Any]) -> Tuple[int, int]:
    rooms = (cfg or {}).get("rooms") or {}
    num_rooms = len(rooms)
    num_devices = 0
    for r in rooms.values():
        num_devices += len(r.get("devices") or [])
    return num_rooms, num_devices


def deduplicate_required_actions(
    required_actions: List[Dict[str, Any]],
) -> List[Dict[str, Any]]:
    seen = set()
    return [
        c
        for c in required_actions
        if (k := (c["tool"], tuple(sorted(c.get("params", {}).items())))) not in seen
        and not seen.add(k)
    ]


def remove_devices_by_ids(cfg: Dict[str, Any], device_ids: List[str]) -> Dict[str, Any]:
    for _, room in cfg["rooms"].items():
        room["devices"] = [
            device
            for device in room["devices"]
            if device["device_id"] not in device_ids
        ]
    return cfg


def remove_device_types_from_room(
    cfg: Dict[str, Any], room_id: str, device_types: Iterable[str]
) -> Dict[str, Any]:
    result = copy.deepcopy(cfg)
    rooms = result.setdefault("rooms", {})
    room = rooms.get(room_id)
    if not room:
        return result
    devices = list(room["devices"])
    types_set = set(device_types)
    filtered = [device for device in devices if device["device_type"] not in types_set]
    room["devices"] = filtered
    return result


def remove_consecutive_duplicate_asserts(
    goals: List[Dict[str, Any]],
) -> List[Dict[str, Any]]:
    if not goals or len(goals) < 2:
        return goals

    filtered_goals = [goals[0]]
    for i in range(1, len(goals)):
        previous_goal = goals[i - 1]
        current_goal = goals[i]
        try:
            prev_asserts = previous_goal.get("targets", [{}])[0].get("asserts", [])
            current_asserts = current_goal.get("targets", [{}])[0].get("asserts", [])
            if prev_asserts != current_asserts:
                filtered_goals.append(current_goal)
        except (IndexError, KeyError):
            filtered_goals.append(current_goal)
    return filtered_goals


def sample_metric_direction_combinations(
    cfg: Dict[str, Any], rng: random.Random, k: int = 1
) -> List[Dict[str, str]]:
    rooms = cfg.get("rooms", {})
    combinations: List[Dict[str, str]] = []
    for room_id, room_data in rooms.items():
        devices = room_data.get("devices", [])
        for device in devices:
            device_type = device.get("device_type")
            metric = DEVICE_TYPE_TO_METRIC.get(device_type)
            directions = DEVICE_TYPE_TO_DIRECTIONS.get(device_type, [])
            if not metric or not directions:
                continue
            for direction in directions:
                if not check_env_semantic_consistency(cfg, room_id, metric, direction):
                    continue
                combinations.append(
                    {
                        "room_id": room_id,
                        "device_id": str(device.get("device_id")),
                        "device_type": str(device_type),
                        "room_state": metric,
                        "direction": direction,
                    }
                )
    return rng.sample(combinations, k=k)


def create_goals(
    cfg: Dict[str, Any], rng: random.Random, k: int = 1
) -> List[Dict[str, Any]]:
    rooms = cfg.get("rooms", {})
    combinations_by_key: Dict[Tuple[str, str], List[Dict[str, Any]]] = {}
    for room_id, room_data in rooms.items():
        devices = room_data.get("devices", [])
        for metric, device_types in METRIC_TO_DEVICE_TYPES.items():
            relevant_devices = [
                d for d in devices if d.get("device_type") in device_types
            ]
            if not relevant_devices:
                continue
            directions = ["decrease"] if metric == "pm10" else ["increase", "decrease"]
            for direction in directions:
                if not check_env_semantic_consistency(cfg, room_id, metric, direction):
                    continue
                feasibility = check_metric_feasibility(cfg, room_id, metric, direction)
                key = (room_id, metric)
                combinations_by_key.setdefault(key, []).append(
                    {
                        "room_id": room_id,
                        "room_state": metric,
                        "direction": direction,
                        "feasibility": feasibility,
                    }
                )

    all_keys = list(combinations_by_key.keys())
    feasible_keys = [
        key
        for key, candidates in combinations_by_key.items()
        if any(candidate["feasibility"] for candidate in candidates)
    ]

    if len(feasible_keys) >= k:
        selected_keys = rng.sample(feasible_keys, k=k)
    else:
        selected_keys = list(feasible_keys)
        remaining_keys = [key for key in all_keys if key not in feasible_keys]
        selected_keys.extend(rng.sample(remaining_keys, k=k - len(selected_keys)))
    selected_goals: List[Dict[str, Any]] = []
    for key in selected_keys:
        candidates = combinations_by_key[key]
        feasible_candidates = [
            candidate for candidate in candidates if candidate["feasibility"]
        ]
        sampling_pool = feasible_candidates or candidates
        selected_goals.append(rng.choice(sampling_pool))
    return selected_goals


__all__ = [
    "count_rooms_and_devices",
    "deduplicate_required_actions",
    "remove_devices_by_ids",
    "remove_device_types_from_room",
    "remove_consecutive_duplicate_asserts",
    "sample_metric_direction_combinations",
    "create_goals",
]
