from __future__ import annotations

import random
import copy
from typing import Any, Dict, List
from src.pipelines.episode_generation.shared.goals import (
    deduplicate_required_actions,
)
from src.pipelines.episode_generation.shared.selectors import sample_user_location
from src.pipelines.episode_generation.core.home_config_initializer import (
    HomeConfigInitializer,
)
from src.pipelines.episode_generation.core.home_augmenter import augment_home
from src.pipelines.episode_generation.shared.goals import remove_devices_by_ids
from src.pipelines.episode_generation.core.device_structure import (
    get_device_readonly_attributes,
)
from src.pipelines.episode_generation.core.seed_utils import ensure_seed
from src.pipelines.episode_generation.shared.payload_assembler import assemble_payload
from src.pipelines.episode_generation.shared.room_state_goal import (
    build_room_state_goal,
)


def build_qt1_infeasible_payload(
    *,
    seed: int,
    home_schema: dict[str, object],
    base_time: str = "2025-08-23 00:00:00",
) -> Dict[str, Any]:
    seed = ensure_seed(seed, context="qt1 infeasible payload")
    rng = random.Random(seed)
    allowed_combinations = [(1, 0), (1, 1)]
    attr_targets, state_targets = rng.choice(allowed_combinations)

    excluded_device_ids = []
    goals = []
    required_actions = []

    base_cfg = HomeConfigInitializer(
        seed=seed,
        base_time=base_time,
        home_spec=home_schema,
    ).create_config()
    snapshot = augment_home(
        home_config=base_cfg,
        seed=seed,
    )

    selected_attributes = set()
    readonly_cache: Dict[str, List[tuple[int, str, str]]] = {}

    for _ in range(attr_targets):
        available_rooms = []
        for room_id, room_data in snapshot["rooms"].items():
            available_devices = [
                d
                for d in room_data["devices"]
                if d["device_id"] not in excluded_device_ids
            ]
            if available_devices:
                available_rooms.append((room_id, available_devices))

        if not available_rooms:
            break

        room_id, devices = rng.choice(available_rooms)
        device = rng.choice(devices)
        device_id = device["device_id"]
        device_type = str(device.get("device_type"))
        readonly_candidates = get_device_readonly_attributes(
            device_type, cache=readonly_cache
        )

        readonly_attrs = []
        for endpoint_id, cluster_id, attr_id in readonly_candidates:
            attr_key = f"{device_id}:{endpoint_id}.{cluster_id}.{attr_id}"
            if attr_key in selected_attributes:
                continue
            readonly_attrs.append(
                {
                    "device_id": device_id,
                    "endpoint_id": int(endpoint_id),
                    "cluster_id": cluster_id,
                    "attribute_id": attr_id,
                    "room_id": room_id,
                    "attr_key": attr_key,
                }
            )

        if readonly_attrs:
            attr = rng.choice(readonly_attrs)
            selected_attributes.add(attr["attr_key"])
            excluded_device_ids.append(device_id)

            goals.append(
                {
                    "variant": "device_attribute",
                    "room_id": room_id,
                    "device_id": device_id,
                    "device_type": device_type,
                    "attribute": f"{attr['endpoint_id']}.{attr['cluster_id']}.{attr['attribute_id']}",
                }
            )
            required_actions.append(
                {"tool": "get_room_devices", "params": {"room_id": room_id}}
            )

    selected_room_states = set()
    available_room_states = ["temperature", "humidity", "illuminance", "pm10"]

    for _ in range(state_targets):
        available_combinations = []
        for room_id in snapshot["rooms"].keys():
            for room_state in available_room_states:
                combination_key = f"{room_id}:{room_state}"
                if combination_key not in selected_room_states:
                    available_combinations.append(
                        (room_id, room_state, combination_key)
                    )

        if not available_combinations:
            break

        room_id, room_state, combination_key = rng.choice(available_combinations)
        selected_room_states.add(combination_key)

        raw_value = snapshot["rooms"][room_id]["state"][room_state]
        goals.append(build_room_state_goal(room_id, room_state, raw_value))
        required_actions.append(
            {"tool": "get_room_states", "params": {"room_id": room_id}}
        )

    base_cfg_without_device = remove_devices_by_ids(
        dict(copy.deepcopy(base_cfg)), excluded_device_ids
    )
    snapshot = augment_home(
        home_config=base_cfg_without_device,
        seed=seed,
    )

    user_location = sample_user_location(snapshot, rng=rng)
    required_actions = deduplicate_required_actions(required_actions)
    return assemble_payload(
        seed=seed,
        query_type="qt1",
        case="infeasible",
        snapshot=snapshot,
        user_location=user_location,
        required_actions=required_actions,
        goals=goals,
        meta_extras={
            "num_target_device_attributes": attr_targets,
            "num_target_room_states": state_targets,
        },
    )
