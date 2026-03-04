from __future__ import annotations

# pyright: reportPrivateUsage=false, reportUnknownVariableType=false, reportUnknownMemberType=false, reportUnknownArgumentType=false, reportUnknownLambdaType=false, reportDeprecated=false, reportUnusedCallResult=false

import json
import unittest
from copy import deepcopy
from pathlib import Path
from typing import Any, Dict, List

from src.simulator.application.device_factory import create_device
from src.simulator.application.home_initializer import (
    SimulationConfig,
    initialize_home_from_config,
)
from src.simulator.domain.home import Home


ROOT = Path(__file__).resolve().parents[2]
BENCHMARK_DIR = ROOT / "data" / "benchmark"
PARITY_EPISODES = (
    "qt1_feasible_seed_4.json",
    "qt2_feasible_seed_4.json",
    "qt3_feasible_seed_4.json",
    "qt4-1_feasible_seed_14.json",
    "qt4-2_feasible_seed_14.json",
    "qt4-3_feasible_seed_14.json",
)
SELECTIVE_PARITY_EPISODES = (
    "qt2_feasible_seed_4.json",
    "qt4-1_feasible_seed_14.json",
)
MAX_TARGET_TICK = 8000
MIN_TARGET_TICK = 1000


def _load_episode(filename: str) -> Dict[str, Any]:
    path = BENCHMARK_DIR / filename
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def _unsupported_attribute_paths(initial_config: Dict[str, Any]) -> List[str]:
    unsupported: List[str] = []
    rooms = initial_config.get("rooms")
    if not isinstance(rooms, dict):
        return unsupported

    for room_id, room_config in rooms.items():
        if not isinstance(room_config, dict):
            continue
        devices = room_config.get("devices")
        if not isinstance(devices, list):
            continue

        for device in devices:
            if not isinstance(device, dict):
                continue

            device_type = device.get("device_type")
            device_id = device.get("device_id")
            attributes = device.get("attributes")

            if not isinstance(device_type, str) or not isinstance(device_id, str):
                continue
            if not isinstance(attributes, dict):
                continue

            probe = create_device(device_type, f"schema_probe__{device_id}")
            available_clusters: set[tuple[int, str]] = set()
            for endpoint_id, cluster_map in probe.endpoints.items():
                for cluster_id in cluster_map.keys():
                    available_clusters.add((int(endpoint_id), str(cluster_id)))

            for attr_path in attributes.keys():
                if not isinstance(attr_path, str):
                    unsupported.append(
                        f"room={room_id} device={device_id} attr=<non-string>"
                    )
                    continue

                parts = attr_path.split(".")
                if len(parts) != 3:
                    unsupported.append(
                        f"room={room_id} device={device_id} attr={attr_path} (invalid format)"
                    )
                    continue

                endpoint_raw, cluster_id, _ = parts
                try:
                    endpoint_id = int(endpoint_raw)
                except ValueError:
                    unsupported.append(
                        f"room={room_id} device={device_id} attr={attr_path} (invalid endpoint)"
                    )
                    continue

                if (endpoint_id, cluster_id) not in available_clusters:
                    unsupported.append(
                        f"room={room_id} device={device_id} attr={attr_path}"
                    )

    return unsupported


def _collect_episode_schema_issues(episodes: tuple[str, ...]) -> List[str]:
    issues: List[str] = []
    for filename in episodes:
        episode = _load_episode(filename)
        initial_config = episode["initial_home_config"]
        unsupported = _unsupported_attribute_paths(initial_config)
        if not unsupported:
            continue

        preview = ", ".join(unsupported[:2])
        suffix = (
            "" if len(unsupported) <= 2 else f" ... and {len(unsupported) - 2} more"
        )
        issues.append(f"{filename}: {preview}{suffix}")

    return issues


def _build_home(initial_config: Dict[str, Any]) -> Home:
    home = Home(
        tick_interval=initial_config["tick_interval"],
        enable_aggregators=True,
        max_ticks=None,
        fast_forward=False,
        base_time=initial_config["base_time"],
    )
    init_result = initialize_home_from_config(home, SimulationConfig(**initial_config))
    if not init_result.success:
        raise RuntimeError("failed to initialize home for parity test")
    return home


def _derive_target_tick(episode: Dict[str, Any]) -> int:
    goals = (episode.get("eval") or {}).get("goals") or []
    candidates: List[int] = []

    for goal in goals:
        when = goal.get("when") if isinstance(goal, dict) else None
        if not isinstance(when, dict):
            continue
        at_tick = when.get("at_tick")
        tolerance = when.get("tolerance_ticks", 0)
        if not isinstance(at_tick, int):
            continue
        tol_val = int(tolerance) if isinstance(tolerance, int) else 0
        candidates.append(at_tick + max(0, tol_val))

    if not candidates:
        return 5000

    target = max(candidates)
    target = max(MIN_TARGET_TICK, min(MAX_TARGET_TICK, target))
    return int(target)


def _extract_relevant_rooms(episode: Dict[str, Any]) -> List[str]:
    goals = (episode.get("eval") or {}).get("goals") or []
    room_ids: set[str] = set()

    for goal in goals:
        if not isinstance(goal, dict):
            continue

        room_id = goal.get("room_id")
        if isinstance(room_id, str) and room_id:
            room_ids.add(room_id)

        anchor = goal.get("anchor")
        if isinstance(anchor, dict):
            anchor_room_id = anchor.get("room_id")
            if isinstance(anchor_room_id, str) and anchor_room_id:
                room_ids.add(anchor_room_id)

        targets = goal.get("targets") or []
        if isinstance(targets, list):
            for target in targets:
                if not isinstance(target, dict):
                    continue
                target_room_id = target.get("room_id")
                if isinstance(target_room_id, str) and target_room_id:
                    room_ids.add(target_room_id)

    return sorted(room_ids)


def _room_projection(state: Dict[str, Any], room_ids: List[str]) -> Dict[str, Any]:
    rooms = state.get("rooms") or {}
    projected: Dict[str, Any] = {}

    for room_id in room_ids:
        room_state = rooms.get(room_id)
        if not isinstance(room_state, dict):
            continue

        devices = room_state.get("devices") or []
        normalized_devices = []
        for device in devices:
            if isinstance(device, dict):
                normalized_devices.append(device)
        normalized_devices.sort(key=lambda item: str(item.get("device_id", "")))

        projected[room_id] = {
            "state": room_state.get("state"),
            "devices": normalized_devices,
        }

    return projected


def _run_reference_loop(home: Home, target_tick: int) -> None:
    process_devices = getattr(home, "_Home__process_time_aware_devices")
    process_aggregators = getattr(home, "_Home__process_aggregators")
    process_scheduler = getattr(home, "_Home__process_schedular_queue")

    steps = max(0, int(target_tick) - int(home.current_tick))
    for _ in range(steps):
        process_devices(None)
        process_aggregators(None)
        process_scheduler(start_workflow_inline=True)
        home.current_tick += 1


def _canonical_payload(payload: Dict[str, Any]) -> str:
    return json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=True)


class SimParityGuardTests(unittest.TestCase):
    def test_fast_forward_matches_reference_tick_loop_on_benchmark_samples(
        self,
    ) -> None:
        schema_issues = _collect_episode_schema_issues(PARITY_EPISODES)
        self.assertFalse(
            schema_issues,
            "Current benchmarks are incompatible with simulator schema. Regenerate data/benchmark with the current generator. "
            + " | ".join(schema_issues),
        )

        for filename in PARITY_EPISODES:
            with self.subTest(episode=filename):
                episode = _load_episode(filename)
                initial_config = episode["initial_home_config"]
                target_tick = _derive_target_tick(episode)

                home_reference = _build_home(deepcopy(initial_config))
                home_fast_forward = _build_home(deepcopy(initial_config))

                _run_reference_loop(home_reference, target_tick)
                ff_result = home_fast_forward._fast_forward_to(target_tick)

                self.assertTrue(ff_result.success)
                self.assertIsNotNone(ff_result.data)

                reference_state_result = home_reference._get_home_state()
                self.assertTrue(reference_state_result.success)
                self.assertIsNotNone(reference_state_result.data)

                reference_state = reference_state_result.data
                fast_forward_state = ff_result.data
                if not isinstance(reference_state, dict):
                    raise AssertionError("reference state must be a dict")
                if not isinstance(fast_forward_state, dict):
                    raise AssertionError("fast-forward state must be a dict")

                reference_payload = _canonical_payload(reference_state)
                fast_forward_payload = _canonical_payload(fast_forward_state)
                self.assertEqual(reference_payload, fast_forward_payload)

    def test_selective_fast_forward_matches_reference_on_relevant_rooms(self) -> None:
        schema_issues = _collect_episode_schema_issues(SELECTIVE_PARITY_EPISODES)
        self.assertFalse(
            schema_issues,
            "Current benchmarks are incompatible with simulator schema. Regenerate data/benchmark with the current generator. "
            + " | ".join(schema_issues),
        )

        for filename in SELECTIVE_PARITY_EPISODES:
            with self.subTest(episode=filename):
                episode = _load_episode(filename)
                initial_config = episode["initial_home_config"]
                target_tick = _derive_target_tick(episode)
                relevant_rooms = _extract_relevant_rooms(episode)
                self.assertTrue(relevant_rooms)

                home_reference = _build_home(deepcopy(initial_config))
                home_selective = _build_home(deepcopy(initial_config))

                _run_reference_loop(home_reference, target_tick)
                selective_result = home_selective._fast_forward_to(
                    target_tick,
                    room_ids=relevant_rooms,
                )

                self.assertTrue(selective_result.success)
                self.assertIsNotNone(selective_result.data)

                reference_state_result = home_reference._get_home_state()
                self.assertTrue(reference_state_result.success)
                self.assertIsNotNone(reference_state_result.data)

                reference_state = reference_state_result.data
                selective_state = selective_result.data
                if not isinstance(reference_state, dict):
                    raise AssertionError("reference state must be a dict")
                if not isinstance(selective_state, dict):
                    raise AssertionError("selective state must be a dict")

                ref_projection = _room_projection(reference_state, relevant_rooms)
                selective_projection = _room_projection(selective_state, relevant_rooms)

                self.assertEqual(
                    _canonical_payload(ref_projection),
                    _canonical_payload(selective_projection),
                )


if __name__ == "__main__":
    unittest.main()
