from __future__ import annotations

import random
from typing import Any, Dict

from src.pipelines.episode_generation.core.seed_utils import derive_subseed, ensure_seed
from src.pipelines.episode_generation.qt4_2.feasible_builder import (
    build_qt4_2_feasible_payload as build_op_nonop_payload,
)
from src.pipelines.episode_generation.shared.conflict_payload_builder import (
    build_infeasible_conflict_payload,
)
from src.pipelines.episode_generation.shared.time_utils import format_absolute_time


def build_qt4_2_infeasible_payload(
    *, seed: int,
    home_schema: dict[str, object],
    base_time: str = "2025-08-23 00:00:00"
) -> Dict[str, Any]:
    
    seed = ensure_seed(seed, context="qt4-2 infeasible payload")

    feasible_payload = build_op_nonop_payload(seed=seed, base_time=base_time, home_schema=home_schema)

    rng = random.Random(derive_subseed(seed, "qt4-2", "infeasible-conflict"))
    goals = feasible_payload["eval"]["goals"]
    base_time_str = feasible_payload["initial_home_config"]["base_time"]

    goal = goals[0]
    when = goal["when"]
    relation = when["relation"]
    offset_minutes = when["offset_minutes"]
    reference_minutes = when["reference_minutes"]
    at_minutes = when["at_minutes"]

    offset = rng.choice(list(range(-20, -9)) + list(range(10, 21)))
    conflict_minutes = at_minutes + offset

    conflict_data = {
        "type": "timing_mismatch_op_nonop",
        "relation": relation,
        "offset_minutes": offset_minutes,
        "anchor_end_at": reference_minutes,
        "expected_at": at_minutes,
        "conflict_at": conflict_minutes,
        "base_time": base_time_str,
        "anchor_end_time": format_absolute_time(
            base_time_str, reference_minutes
        ).strftime("%H:%M:%S"),
        "expected_time": format_absolute_time(base_time_str, at_minutes).strftime(
            "%H:%M:%S"
        ),
        "conflict_time": format_absolute_time(base_time_str, conflict_minutes).strftime(
            "%H:%M:%S"
        ),
    }

    ordered_payload = build_infeasible_conflict_payload(
        feasible_payload=feasible_payload,
        conflict_data=conflict_data,
        keep_only_first_goal=True,
    )

    return ordered_payload


__all__ = ["build_qt4_2_infeasible_payload"]
