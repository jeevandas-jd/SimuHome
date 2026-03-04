from __future__ import annotations

import random
from typing import Any, Dict, List
import copy
from src.pipelines.episode_generation.core.home_config_initializer import (
    HomeConfigInitializer,
)
from src.pipelines.episode_generation.core.home_augmenter import augment_home
from src.pipelines.episode_generation.core.seed_utils import ensure_seed
from src.pipelines.episode_generation.shared.goals import (
    remove_device_types_from_room,
    sample_metric_direction_combinations,
)
from src.pipelines.episode_generation.shared.feasibility import METRIC_TO_DEVICE_TYPES
from src.pipelines.episode_generation.shared.goals import (
    deduplicate_required_actions,
)
from src.pipelines.episode_generation.shared.payload_assembler import assemble_payload
from src.pipelines.episode_generation.shared.selectors import sample_user_location


def build_qt2_infeasible_payload(
    *,
    seed: int,
    home_schema: dict[str, object],
    base_time: str = "2025-08-23 00:00:00",
) -> Dict[str, Any]:
    

    seed = ensure_seed(seed, context="qt2 infeasible payload")
    rng = random.Random(seed)

    base_cfg = HomeConfigInitializer(
        seed=seed,
        base_time=base_time,
        home_spec=home_schema,
    ).create_config()
    sample_source: Dict[str, Any] = copy.deepcopy(dict(base_cfg))

    target_nums = 1 if rng.random() < 0.5 else 2
    goals = sample_metric_direction_combinations(sample_source, rng, k=target_nums)
    if not goals:
        raise ValueError("No targets could be selected with given parameters")

    safe_base_cfg: Dict[str, Any] = copy.deepcopy(dict(base_cfg))
    for goal in goals:
        metric = goal["room_state"]
        related_device_types = METRIC_TO_DEVICE_TYPES.get(metric, [])
        if related_device_types:
            safe_base_cfg = remove_device_types_from_room(
                safe_base_cfg,
                goal["room_id"],
                related_device_types,
            )

    snapshot = augment_home(
        home_config=safe_base_cfg,
        seed=seed,
    )

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
        case="infeasible",
        snapshot=snapshot,
        user_location=user_location,
        required_actions=required_actions,
        goals=goals,
        meta_extras={
            "num_target_metrics": len(goals),
            "infeasible_family": "nonexistence",
        },
    )
