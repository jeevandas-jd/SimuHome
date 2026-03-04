from __future__ import annotations

import random
from typing import Any, Dict, List

from src.pipelines.episode_generation.core.home_config_initializer import (
    HomeConfigInitializer,
)
from src.pipelines.episode_generation.core.home_augmenter import augment_home
from src.pipelines.episode_generation.core.seed_utils import ensure_seed
from src.pipelines.episode_generation.shared.targets_registry import (
    load_registry,
    build_target_assert,
)
from src.pipelines.episode_generation.shared.goals import (
    deduplicate_required_actions,
    remove_devices_by_ids,
)
from src.pipelines.episode_generation.shared.payload_assembler import assemble_payload
from src.pipelines.episode_generation.shared.selectors import (
    sample_user_location,
    list_devices_in_config,
)


def build_qt3_infeasible_payload(
    *,
    seed: int,
    home_schema: dict[str, object],
    base_time: str = "2025-08-23 00:00:00",
) -> Dict[str, Any]:
    

    seed = ensure_seed(seed, context="qt3 infeasible payload")
    rng = random.Random(seed)

    base_cfg = HomeConfigInitializer(
        seed=seed,
        base_time=base_time,
        home_spec=home_schema,
    ).create_config()

    base_cfg_dict: Dict[str, Any] = dict(base_cfg)
    user_location = sample_user_location(base_cfg_dict, rng=rng)

    pool = list(list_devices_in_config(base_cfg_dict))

    targets = rng.sample(pool, k=rng.randint(1, 3))

    registry = load_registry()
    required_actions = []
    goals = []
    removed_device_ids: List[str] = []
    for target_room_id, target in targets:
        device_id = str(target.get("device_id"))
        device_type = str(target.get("device_type"))
        state_flat: Dict[str, Any] = target.get("attributes") or {}
        asserts = build_target_assert(
            device_type=device_type,
            state_flat=state_flat,
            registry=registry,
            seed=seed,
        )
        required_actions.append(
            {"tool": "get_room_devices", "params": {"room_id": target_room_id}}
        )
        goals.append(
            {
                "room_id": target_room_id,
                "device_id": device_id,
                "device_type": device_type,
                "asserts": asserts,
            }
        )
        removed_device_ids.append(device_id)

    base_cfg_without_device = remove_devices_by_ids(dict(base_cfg), removed_device_ids)
    snapshot = augment_home(
        home_config=base_cfg_without_device,
        seed=seed,
    )

    required_actions = deduplicate_required_actions(required_actions)
    return assemble_payload(
        seed=seed,
        query_type="qt3",
        case="infeasible",
        snapshot=snapshot,
        user_location=user_location,
        required_actions=required_actions,
        goals=goals,
        meta_extras={"devices_count": len(targets)},
    )
