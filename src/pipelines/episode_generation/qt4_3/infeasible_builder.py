from __future__ import annotations

import random
from typing import Any, Dict

from src.pipelines.episode_generation.core.seed_utils import derive_subseed, ensure_seed
from src.pipelines.episode_generation.qt4_3.feasible_builder import (
    build_qt4_3_feasible_payload as build_op_op_payload,
)
from src.pipelines.episode_generation.shared.conflict_payload_builder import (
    build_infeasible_conflict_payload,
)
from src.pipelines.episode_generation.shared.time_utils import format_absolute_time


def _sample_pause_conflict(
    anchor_end_minutes: int, rng: random.Random
) -> Dict[str, Any]:
    
    conflict_type = rng.choice(["absolute_time_mismatch", "completion_vs_pause"])

    if conflict_type == "absolute_time_mismatch":
        offset = rng.randint(10, 30)
        return {
            "type": "absolute_time_mismatch",
            "anchor_end_at": anchor_end_minutes,
            "conflict_at": anchor_end_minutes + offset,
        }
    else:
        return {
            "type": "completion_vs_pause",
            "anchor_end_at": anchor_end_minutes,
            "requested_action": "completion",
        }


def _sample_delayed_conflict(
    anchor_end_minutes: int, delay_minutes: int, rng: random.Random
) -> Dict[str, Any]:
    
    normal_target_start = anchor_end_minutes + delay_minutes

    offset = rng.choice(list(range(-15, -4)) + list(range(5, 16)))

    return {
        "type": "delay_time_mismatch",
        "anchor_end_at": anchor_end_minutes,
        "delay_minutes": delay_minutes,
        "expected_at": normal_target_start,
        "conflict_at": normal_target_start + offset,
    }


def _sample_align_conflict(
    anchor_end_minutes: int, rng: random.Random
) -> Dict[str, Any]:
    

    early_minutes = rng.randint(5, 20)

    return {
        "type": "impossible_early_end",
        "anchor_end_at": anchor_end_minutes,
        "conflict_at": anchor_end_minutes - early_minutes,
    }


def _create_temporal_conflict(payload: Dict[str, Any], seed: int) -> Dict[str, Any]:
    
    rng = random.Random(seed)

    scenario = payload["meta"]["scenario"]
    base_time = payload["initial_home_config"]["base_time"]
    goals = payload["eval"]["goals"]

    anchor_end_minutes = goals[1]["when"]["reference_minutes"]

    if scenario == "pause_at_anchor_end":
        conflict_data = _sample_pause_conflict(anchor_end_minutes, rng)
    elif scenario == "delayed_start":
        delay_minutes = goals[1]["when"]["offset_minutes"]
        conflict_data = _sample_delayed_conflict(anchor_end_minutes, delay_minutes, rng)
    elif scenario == "align_end_with_anchor":
        conflict_data = _sample_align_conflict(anchor_end_minutes, rng)
    else:
        raise ValueError(f"Unknown scenario: {scenario}")

    conflict_data["base_time"] = base_time

    if "anchor_end_at" in conflict_data:
        conflict_data["anchor_end_time"] = format_absolute_time(
            base_time, conflict_data["anchor_end_at"]
        ).strftime("%H:%M:%S")
    if "target_end_at" in conflict_data:
        conflict_data["target_end_time"] = format_absolute_time(
            base_time, conflict_data["target_end_at"]
        ).strftime("%H:%M:%S")
    if "expected_at" in conflict_data:
        conflict_data["expected_time"] = format_absolute_time(
            base_time, conflict_data["expected_at"]
        ).strftime("%H:%M:%S")
    if "conflict_at" in conflict_data:
        conflict_data["conflict_time"] = format_absolute_time(
            base_time, conflict_data["conflict_at"]
        ).strftime("%H:%M:%S")

    return conflict_data


def build_qt4_3_infeasible_payload(
    *, seed: int,
    home_schema: dict[str, object],
    base_time: str = "2025-08-23 00:00:00"
) -> Dict[str, Any]:
    
    seed = ensure_seed(seed, context="qt4-3 infeasible payload")

    feasible_payload = build_op_op_payload(seed=seed, base_time=base_time, home_schema=home_schema)

    conflict_seed = derive_subseed(seed, "qt4-3", "infeasible-conflict")
    conflict_data = _create_temporal_conflict(feasible_payload, conflict_seed)

    ordered_payload = build_infeasible_conflict_payload(
        feasible_payload=feasible_payload,
        conflict_data=conflict_data,
    )

    return ordered_payload


__all__ = ["build_qt4_3_infeasible_payload"]
