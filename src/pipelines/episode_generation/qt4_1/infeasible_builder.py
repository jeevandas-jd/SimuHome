from __future__ import annotations

import random
from typing import Any, Dict

from src.pipelines.episode_generation.qt4_1.feasible_builder import (
    build_qt4_1_feasible_payload as build_nonop_multi_payload,
)
from src.pipelines.episode_generation.core.seed_utils import derive_subseed, ensure_seed
from src.pipelines.episode_generation.shared.conflict_payload_builder import (
    build_infeasible_conflict_payload,
)
from src.pipelines.episode_generation.shared.time_utils import format_absolute_time


def build_qt4_1_infeasible_payload(
    *, seed: int,
    home_schema: dict[str, object],
    base_time: str = "2025-08-23 00:00:00"
) -> Dict[str, Any]:
    
    seed = ensure_seed(seed, context="qt4-1 infeasible payload")

    feasible_payload = build_nonop_multi_payload(seed=seed, base_time=base_time, home_schema=home_schema)

    goals = feasible_payload["eval"]["goals"]
    base_time_str = feasible_payload["initial_home_config"]["base_time"]

    goal_at = goals[0]["when"]["at_minutes"]
    rng = random.Random(derive_subseed(seed, "qt4-1", "infeasible-conflict"))
    offset = rng.choice(list(range(-20, -9)) + list(range(10, 21)))

    conflict_data = {
        "type": "absolute_time_mismatch_nonop_multi",
        "expected_at": goal_at,
        "conflict_at": goal_at + offset,
        "base_time": base_time_str,
        "expected_time": format_absolute_time(base_time_str, goal_at).strftime(
            "%H:%M:%S"
        ),
        "conflict_time": format_absolute_time(base_time_str, goal_at + offset).strftime(
            "%H:%M:%S"
        ),
    }

    ordered_payload = build_infeasible_conflict_payload(
        feasible_payload=feasible_payload,
        conflict_data=conflict_data,
        keep_only_first_goal=True,
    )

    return ordered_payload


__all__ = ["build_qt4_1_infeasible_payload"]
