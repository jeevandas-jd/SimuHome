from __future__ import annotations

import random
from typing import Any, Dict

from src.pipelines.episode_generation.core.home_config_initializer import (
    HomeConfigInitializer,
)
from src.pipelines.episode_generation.core.home_augmenter import augment_home
from src.pipelines.episode_generation.core.seed_utils import derive_subseed, ensure_seed
from src.pipelines.episode_generation.shared.targets_registry import (
    load_registry,
    build_target_assert,
)
from src.pipelines.episode_generation.shared.goals import (
    deduplicate_required_actions,
    remove_consecutive_duplicate_asserts,
)
from src.pipelines.episode_generation.shared.payload_assembler import assemble_payload
from src.pipelines.episode_generation.shared.selectors import (
    sample_non_op_device,
    sample_user_location,
)
from src.pipelines.episode_generation.shared.time_utils import (
    minutes_to_ticks,
    get_tolerance_ticks,
    ticks_to_minutes,
)


def build_qt4_1_feasible_payload(
    *, seed: int,
    home_schema: dict[str, object],
    base_time: str = "2025-08-23 00:00:00"
) -> Dict[str, Any]:
    
    seed = ensure_seed(seed, context="qt4-1 feasible payload")
    rng = random.Random(seed)

    base_cfg = HomeConfigInitializer(
        seed=seed,
        base_time=base_time,
        home_spec=home_schema,
    ).create_config()

    targets = sample_non_op_device(snapshot=dict(base_cfg), rng=rng, k=2)
    exclude_devices_by_room = {room_id: [dev["device_id"]] for room_id, dev in targets}

    snapshot = augment_home(
        home_config=base_cfg,
        seed=seed,
        exclude_devices_by_room=exclude_devices_by_room,
    )

    user_location = sample_user_location(snapshot, rng=rng)
    tick_interval = float(snapshot.get("tick_interval", 0.1))
    tolerance_ticks = get_tolerance_ticks(
        tolerance_seconds=30, tick_interval=tick_interval
    )
    registry = load_registry()
    required_actions = []
    goals = []
    for target_room_id, target_device in targets:
        required_actions.append(
            {"tool": "get_room_devices", "params": {"room_id": target_room_id}}
        )

        sampled_minutes = rng.sample(range(5, 31), 3)

        current_tick = 0
        for idx, sampled_minute in enumerate(sampled_minutes[:-1]):
            target_asserts = build_target_assert(
                device_type=target_device["device_type"],
                state_flat=target_device["attributes"],
                registry=registry,
                seed=derive_subseed(
                    seed, "qt4-1", "target-assert", target_room_id, idx
                ),
            )
            goal = {
                "when": {
                    "reference_tick": current_tick,
                    "reference_minutes": ticks_to_minutes(current_tick, tick_interval),
                    "relation": "after",
                    "offset_ticks": minutes_to_ticks(sampled_minute, tick_interval),
                    "offset_minutes": sampled_minute,
                    "at_tick": current_tick
                    + minutes_to_ticks(sampled_minute, tick_interval),
                    "at_minutes": ticks_to_minutes(
                        current_tick + minutes_to_ticks(sampled_minute, tick_interval),
                        tick_interval,
                    ),
                    "tolerance_ticks": tolerance_ticks,
                },
                "anchor": {},
                "targets": [
                    {
                        "room_id": target_room_id,
                        "device_id": target_device["device_id"],
                        "device_type": target_device["device_type"],
                        "asserts": target_asserts,
                    }
                ],
            }
            goals.append(goal)
            current_tick += minutes_to_ticks(sampled_minute, tick_interval)
        goals = remove_consecutive_duplicate_asserts(goals)

        if "1.OnOff.OnOff" in target_device["attributes"] and (rng.random() < 0.5):
            goals.append(
                {
                    "when": {
                        "reference_tick": current_tick,
                        "reference_minutes": ticks_to_minutes(
                            current_tick, tick_interval
                        ),
                        "relation": "after",
                        "offset_ticks": minutes_to_ticks(
                            sampled_minutes[-1], tick_interval
                        ),
                        "offset_minutes": sampled_minutes[-1],
                        "at_tick": current_tick
                        + minutes_to_ticks(sampled_minutes[-1], tick_interval),
                        "at_minutes": ticks_to_minutes(
                            current_tick
                            + minutes_to_ticks(sampled_minutes[-1], tick_interval),
                            tick_interval,
                        ),
                        "tolerance_ticks": tolerance_ticks,
                    },
                    "anchor": {},
                    "targets": [
                        {
                            "room_id": target_room_id,
                            "device_id": target_device["device_id"],
                            "device_type": target_device["device_type"],
                            "asserts": [
                                {
                                    "attribute": "1.OnOff.OnOff",
                                    "value": False,
                                    "value_type": "bool",
                                    "description": "power off",
                                }
                            ],
                        }
                    ],
                }
            )

    goals.sort(key=lambda g: g["when"]["at_tick"])
    required_actions = deduplicate_required_actions(required_actions)
    return assemble_payload(
        seed=seed,
        query_type="qt4-1",
        case="feasible",
        snapshot=snapshot,
        user_location=user_location,
        required_actions=required_actions,
        goals=goals,
    )


__all__ = [
    "build_qt4_1_feasible_payload",
]
