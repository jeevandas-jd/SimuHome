from __future__ import annotations

from typing import Dict, Any, List, Optional
from src.pipelines.episode_evaluation.common import evaluate_required_actions
from src.agents.providers import LLMProvider


def _extract_room_ids_from_qt2_episode(payload: Dict[str, Any]) -> List[str]:
    
    room_ids = set()

    goals = payload["episode"]["eval"].get("goals", [])
    for goal in goals:
        room_id = goal.get("room_id")
        if room_id:
            room_ids.add(room_id)

    return list(room_ids)


def evaluate(
    payload: Dict[str, Any], judge_llms: Optional[List[LLMProvider]] = None
) -> Dict[str, Any]:
    
    if judge_llms is None:
        judge_llms = []

    query = payload["episode"]["query"]
    goals = payload["episode"]["eval"]["goals"]
    initial_home_config = payload["episode"]["initial_home_config"]
    client = payload["client"]
    final_home_state = payload["final_home_state"]

    try:
        required_actions_result = evaluate_required_actions(payload)
    except ValueError as e:
        return {
            "score": -1,
            "error_type": f"Required Actions Schema Error: {e}",
            "required_actions": [],
            "direction_checks": [],
            "optimization": {
                "selective_fast_forward": True,
                "relevant_room_ids": [],
                "rooms_count": 0,
            },
        }

    tools_ok = all(action["invoked"] for action in required_actions_result)

    relevant_room_ids = _extract_room_ids_from_qt2_episode(payload)

    client.reset_simulation(initial_home_config)
    if relevant_room_ids:
        baseline_wrapped = client.fast_forward_to(
            final_home_state["current_tick"], room_ids=relevant_room_ids
        )
    else:
        baseline_wrapped = client.fast_forward_to(final_home_state["current_tick"])
    baseline_home_state = baseline_wrapped.get("data", {})

    details = []
    for goal in goals:
        room_id = goal["room_id"]
        room_state = goal["room_state"]
        direction = goal["direction"]
        baseline_value = baseline_home_state["rooms"][room_id]["state"][room_state]
        final_value = final_home_state["rooms"][room_id]["state"][room_state]

        threshold = 1e-8

        direction_ok = (
            True
            if (direction == "increase" and final_value - baseline_value >= threshold)
            or (direction == "decrease" and baseline_value - final_value >= threshold)
            else False
        )
        details.append(
            {
                "room_id": room_id,
                "room_state": room_state,
                "direction": direction,
                "from": baseline_value,
                "to": final_value,
                "ok": direction_ok,
            }
        )

    score = 1 if tools_ok and all(detail["ok"] for detail in details) else 0
    return {
        "score": score,
        "required_actions": required_actions_result,
        "direction_checks": details,
        "optimization": {
            "selective_fast_forward": True,
            "relevant_room_ids": relevant_room_ids,
            "rooms_count": len(relevant_room_ids) if relevant_room_ids else 0,
        },
    }
