from __future__ import annotations

import random
from typing import Any, Dict, List, Tuple
from src.pipelines.episode_generation.core.home_config_initializer import (
    HomeConfigInitializer,
)
from src.pipelines.episode_generation.core.home_augmenter import augment_home
from src.pipelines.episode_generation.core.seed_utils import derive_subseed, ensure_seed
from src.pipelines.episode_generation.shared.goals import (
    deduplicate_required_actions,
)
from src.pipelines.episode_generation.shared.payload_assembler import assemble_payload
from src.pipelines.episode_generation.shared.selectors import (
    sample_user_location,
    sample_op_device,
    sample_non_op_device,
)
from src.pipelines.episode_generation.shared.targets_registry import (
    load_registry,
    build_target_assert,
)
from src.pipelines.episode_generation.shared.time_utils import (
    get_running_anchor_end_tick,
    minutes_to_ticks,
    get_tolerance_ticks,
    ticks_to_minutes,
)


def _sample_when_spec(
    *, rng: random.Random, reference_tick: int, tick_interval: float
) -> Dict[str, Any]:
    offset_minutes = int(rng.randint(5, 30))
    offset_ticks = minutes_to_ticks(offset_minutes, tick_interval)
    relation = rng.choice(["before", "after"])
    if relation == "before" and offset_ticks > reference_tick:
        relation = "after"
    at_tick = (
        reference_tick + offset_ticks
        if relation == "after"
        else reference_tick - offset_ticks
    )

    tolerance_ticks = get_tolerance_ticks(
        tolerance_seconds=30, tick_interval=tick_interval
    )

    when_spec = {
        "reference_tick": reference_tick,
        "reference_minutes": ticks_to_minutes(reference_tick, tick_interval),
        "relation": str(relation),
        "offset_ticks": offset_ticks,
        "offset_minutes": offset_minutes,
        "at_tick": at_tick,
        "at_minutes": ticks_to_minutes(at_tick, tick_interval),
        "tolerance_ticks": tolerance_ticks,
    }
    return when_spec


def _form_goal_entry(
    *,
    anchor: Tuple[str, Dict[str, Any]],
    targets: List[Tuple[str, Dict[str, Any]]],
    registry: Dict[str, Any],
    seed: int,
    rng: random.Random,
    tick_interval: float,
) -> Dict[str, Any]:
    anchor_room_id, anchor_device = anchor
    targets_payload: List[Dict[str, Any]] = []
    goal_entry: Dict[str, Any] = {
        "when": {},
        "anchor": {
            "room_id": anchor_room_id,
            "device_id": anchor_device["device_id"],
            "device_type": anchor_device["device_type"],
        },
        "targets": targets_payload,
    }
    anchor_end_tick = get_running_anchor_end_tick(
        anchor_device=anchor_device, tick_interval=tick_interval
    )
    goal_entry["when"] = _sample_when_spec(
        rng=rng, reference_tick=anchor_end_tick, tick_interval=tick_interval
    )
    for idx, (target_room_id, target_device) in enumerate(targets):
        target: Dict[str, Any] = {}
        target["room_id"] = target_room_id
        target["device_id"] = target_device["device_id"]
        target["device_type"] = target_device["device_type"]
        target["asserts"] = build_target_assert(
            device_type=str(target_device["device_type"]),
            state_flat=target_device["attributes"],
            registry=registry,
            seed=derive_subseed(seed, "qt4-2", "target-assert", target_room_id, idx),
        )

        targets_payload.append(target)

    return goal_entry


def build_qt4_2_feasible_payload(
    *, seed: int, home_schema: dict[str, object], base_time: str = "2025-08-23 00:00:00"
) -> Dict[str, Any]:
    seed = ensure_seed(seed, context="qt4-2 feasible payload")
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
    user_location = sample_user_location(snapshot, rng=rng)
    anchors = sample_op_device(snapshot, rng=rng, sample_running_anchor=True, k=1)
    registry = load_registry()
    required_actions = []
    goals = []
    for idx in range(1):
        for anchor in anchors:
            targets = sample_non_op_device(snapshot, rng=rng, k=2)
            for target_room_id, _ in targets:
                required_actions.append(
                    {"tool": "get_room_devices", "params": {"room_id": target_room_id}}
                )
            goal_entry = _form_goal_entry(
                anchor=anchor,
                targets=targets,
                registry=registry,
                seed=derive_subseed(seed, "qt4-2", "goal-entry", idx),
                rng=rng,
                tick_interval=snapshot.get("tick_interval", 0.1),
            )
            goals.append(goal_entry)

    goals.sort(key=lambda g: g["when"]["at_tick"])
    required_actions = deduplicate_required_actions(required_actions)
    return assemble_payload(
        seed=seed,
        query_type="qt4-2",
        case="feasible",
        snapshot=snapshot,
        user_location=user_location,
        required_actions=required_actions,
        goals=goals,
    )


__all__ = [
    "build_qt4_2_feasible_payload",
]
