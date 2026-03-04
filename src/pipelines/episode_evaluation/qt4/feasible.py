from __future__ import annotations

from typing import Any, Dict, List, Optional

from src.clients.smarthome_client import SmartHomeClient
from src.pipelines.episode_evaluation.common import (
    evaluate_required_actions,
    read_device_attr,
)
from src.agents.providers import LLMProvider


def _extract_room_ids_from_qt4_episode(payload: Dict[str, Any]) -> List[str]:
    
    room_ids = set()

    goals = payload["episode"]["eval"].get("goals", [])
    for goal in goals:
        anchor = goal.get("anchor", {})
        if anchor and "room_id" in anchor:
            anchor_room_id = anchor["room_id"]
            if anchor_room_id:
                room_ids.add(anchor_room_id)

        targets = goal.get("targets", [])
        for target in targets:
            room_id = target.get("room_id")
            if room_id:
                room_ids.add(room_id)

    return list(room_ids)


def _verify_asserts(
    state: Dict[str, Any], device_id: str, asserts: List[Dict[str, Any]]
) -> bool:
    for a in asserts:
        attr = a["attribute"]
        expected = a["value"]
        actual = read_device_attr(state, device_id, attr)
        if actual != expected:
            return False
    return True


def _describe_fast_forward_error(resp: Any) -> str:
    if not isinstance(resp, dict):
        return "invalid fast_forward_to response payload"

    status = resp.get("status")
    error = resp.get("error")

    status_code = None
    status_message = None
    if isinstance(status, dict):
        status_code = status.get("code")
        status_message = status.get("message")

    error_type = None
    error_detail = None
    if isinstance(error, dict):
        error_type = error.get("type")
        error_detail = error.get("detail")

    detail_parts = [
        "missing data in fast_forward_to response",
    ]
    if status_code is not None:
        detail_parts.append(f"status.code={status_code}")
    if status_message:
        detail_parts.append(f"status.message={status_message}")
    if error_type:
        detail_parts.append(f"error.type={error_type}")
    if error_detail:
        detail_parts.append(f"error.detail={error_detail}")

    return " | ".join(detail_parts)


def _fetch_checkpoint_state(
    client: SmartHomeClient,
    tick: int,
    room_ids: Optional[List[str]],
) -> tuple[Optional[Dict[str, Any]], Optional[str]]:
    try:
        if room_ids:
            resp = client.fast_forward_to(tick, room_ids=room_ids)
        else:
            resp = client.fast_forward_to(tick)
    except Exception as exc:
        return None, f"fast_forward_to exception: {exc}"

    checkpoint_state = resp.get("data") if isinstance(resp, dict) else None
    if not isinstance(checkpoint_state, dict):
        return None, _describe_fast_forward_error(resp)

    return checkpoint_state, None


def _verify_all_targets_at_tick(
    client: SmartHomeClient,
    tick: int,
    targets: List[Dict[str, Any]],
    room_ids: Optional[List[str]] = None,
) -> tuple[bool, bool, Optional[str]]:
    

    checkpoint_state, error_message = _fetch_checkpoint_state(client, tick, room_ids)
    if checkpoint_state is None:
        return False, False, error_message or "missing data in fast_forward_to response"

    for target in targets:
        device_id = target["device_id"]
        asserts = target["asserts"]
        if not _verify_asserts(checkpoint_state, device_id, asserts):
            return False, True, None
    return True, True, None


def _build_checkpoints(at_tick: int, tolerance_ticks: int) -> List[int]:
    tolerance_ticks = max(0, int(tolerance_ticks))
    if tolerance_ticks == 0:
        return [at_tick]

    start_tick = max(0, at_tick - tolerance_ticks)
    end_tick = at_tick + tolerance_ticks
    return list(range(start_tick, end_tick + 1))


def _resolve_monotonic_cursor_tick(
    client: SmartHomeClient, final_home_state: Optional[Dict[str, Any]]
) -> int:
    final_tick = 0
    try:
        final_tick = int((final_home_state or {}).get("current_tick", 0))
    except Exception:
        final_tick = 0

    try:
        live_state_resp = client.get_home_state()
        if isinstance(live_state_resp, dict):
            live_data = live_state_resp.get("data")
            if isinstance(live_data, dict):
                live_tick = int(live_data.get("current_tick", final_tick))
                return max(final_tick, live_tick)
    except Exception:
        pass

    return final_tick


def _apply_monotonic_window(
    checkpoints: List[int], cursor_tick: int
) -> tuple[List[int], bool, bool]:
    if not checkpoints:
        return [], False, False

    window_start = checkpoints[0]
    window_end = checkpoints[-1]
    if cursor_tick > window_end:
        return [], True, True

    filtered = [tick for tick in checkpoints if tick >= cursor_tick]
    partially_clipped = cursor_tick > window_start
    return filtered, partially_clipped, False


def evaluate(
    payload: Dict[str, Any], judge_llms: Optional[List[LLMProvider]] = None
) -> Dict[str, Any]:
    
    if judge_llms is None:
        judge_llms = []

    goals = payload["episode"]["eval"]["goals"]
    client = payload["client"]
    final_home_state = payload.get("final_home_state")

    try:
        required_actions_result = evaluate_required_actions(payload)
    except ValueError as e:
        return {
            "score": -1,
            "error_type": f"Required Actions Schema Error: {e}",
            "required_actions": [],
            "goals_eval": [],
            "total_goals": len(goals),
            "satisfied_goals": 0,
            "optimization": {
                "selective_fast_forward": True,
                "relevant_room_ids": [],
                "rooms_count": 0,
            },
        }

    tools_ok = all(action["invoked"] for action in required_actions_result)

    relevant_room_ids = _extract_room_ids_from_qt4_episode(payload)

    details = []
    all_goals_satisfied = True
    cursor_tick = _resolve_monotonic_cursor_tick(client, final_home_state)

    indexed_goals = list(enumerate(goals))
    indexed_goals.sort(key=lambda item: (int(item[1]["when"]["at_tick"]), item[0]))

    for original_idx, goal in indexed_goals:
        when = goal["when"]
        targets = goal["targets"]

        at_tick = int(when["at_tick"])
        tolerance_ticks = int(when["tolerance_ticks"])
        checkpoints = _build_checkpoints(at_tick, tolerance_ticks)
        (
            checkpoints,
            monotonic_window_partially_clipped,
            monotonic_window_missed,
        ) = _apply_monotonic_window(checkpoints, cursor_tick)

        goal_satisfied = False
        tested_ticks = []

        for checkpoint_tick in checkpoints:
            tested_ticks.append(checkpoint_tick)
            goal_ok, advanced, error_message = _verify_all_targets_at_tick(
                client, checkpoint_tick, targets, relevant_room_ids
            )
            if error_message is not None:
                return {
                    "score": -1,
                    "error_type": "Fast Forward Failure",
                    "error_detail": error_message,
                    "required_actions": required_actions_result,
                    "goals_eval": details,
                    "total_goals": len(goals),
                    "satisfied_goals": sum(1 for d in details if d.get("satisfied")),
                    "optimization": {
                        "selective_fast_forward": True,
                        "monotonic_checkpoints": True,
                        "relevant_room_ids": relevant_room_ids,
                        "rooms_count": len(relevant_room_ids)
                        if relevant_room_ids
                        else 0,
                    },
                }
            if advanced:
                cursor_tick = max(cursor_tick, checkpoint_tick)
            if goal_ok:
                goal_satisfied = True
                break

        details.append(
            {
                "goal_index": original_idx,
                "at_tick": at_tick,
                "tolerance_ticks": tolerance_ticks,
                "targets_count": len(targets),
                "tested_ticks": tested_ticks,
                "monotonic_window_clipped": len(checkpoints) == 0,
                "monotonic_window_partially_clipped": monotonic_window_partially_clipped,
                "monotonic_window_missed": monotonic_window_missed,
                "satisfied": goal_satisfied,
            }
        )

        if not goal_satisfied:
            all_goals_satisfied = False

    details = sorted(details, key=lambda item: int(item["goal_index"]))

    return {
        "score": 1 if (tools_ok and all_goals_satisfied) else 0,
        "required_actions": required_actions_result,
        "goals_eval": details,
        "total_goals": len(goals),
        "satisfied_goals": sum(1 for d in details if d["satisfied"]),
        "optimization": {
            "selective_fast_forward": True,
            "monotonic_checkpoints": True,
            "relevant_room_ids": relevant_room_ids,
            "rooms_count": len(relevant_room_ids) if relevant_room_ids else 0,
        },
    }
