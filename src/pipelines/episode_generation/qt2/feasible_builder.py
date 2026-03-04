from __future__ import annotations

import random
from typing import Any, Dict, List

from src.pipelines.episode_generation.core.home_config_initializer import (
    HomeConfigInitializer,
)
from src.pipelines.episode_generation.core.home_augmenter import augment_home
from src.pipelines.episode_generation.core.seed_utils import ensure_seed
from src.pipelines.episode_generation.shared.goals import create_goals
from src.pipelines.episode_generation.shared.goals import (
    deduplicate_required_actions,
)
from src.pipelines.episode_generation.shared.payload_assembler import assemble_payload
from src.pipelines.episode_generation.shared.selectors import sample_user_location


def _has_conflicting_goal_directions(goals: List[Dict[str, Any]]) -> bool:
    direction_by_key: Dict[tuple[str, str], str] = {}
    for goal in goals:
        room_id = str(goal.get("room_id", ""))
        room_state = str(goal.get("room_state", ""))
        direction = str(goal.get("direction", ""))
        key = (room_id, room_state)
        previous_direction = direction_by_key.get(key)
        if previous_direction is None:
            direction_by_key[key] = direction
            continue
        if previous_direction != direction:
            return True
    return False


def build_qt2_feasible_payload(
    *,
    seed: int,
    home_schema: dict[str, object],
    base_time: str = "2025-08-23 00:00:00",
) -> Dict[str, Any]:
    seed = ensure_seed(seed, context="qt2 feasible payload")
    rng = random.Random(seed)

    base_cfg = HomeConfigInitializer(
        seed=seed,
        base_time=base_time,
        home_spec=home_schema,
    ).create_config()

    snapshot = augment_home(
        home_config=base_cfg,
        seed=seed,
    )

    target_nums = 1 if rng.random() < 0.5 else 2
    goals = create_goals(snapshot, rng, k=target_nums)
    if not goals:
        raise ValueError("No targets could be selected with given parameters")
    if _has_conflicting_goal_directions(goals):
        raise ValueError(
            "Conflicting goal directions detected for identical room state"
        )

    all_feasible = all(goal["feasibility"] for goal in goals)
    case = "feasible" if all_feasible else "infeasible"

    meta_extras: Dict[str, Any] = {
        "num_target_metrics": len(goals),
        "feasibility": all_feasible,
    }
    if not all_feasible:
        meta_extras["infeasible_family"] = "contextual_saturation"

    user_location = sample_user_location(snapshot, rng=rng)

    required_actions: List[Dict[str, Any]] = []
    for goal in goals:
        required_actions.append(
            {"tool": "get_room_devices", "params": {"room_id": goal["room_id"]}}
        )

    required_actions = deduplicate_required_actions(required_actions)
    return assemble_payload(
        seed=seed,
        query_type="qt2",
        case=case,
        snapshot=snapshot,
        user_location=user_location,
        required_actions=required_actions,
        goals=goals,
        meta_extras=meta_extras,
    )
