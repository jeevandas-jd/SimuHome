from __future__ import annotations

from typing import Any, Dict, List, Optional

from src.pipelines.episode_evaluation.common import (
    evaluate_required_actions,
    read_device_attr,
)
from src.agents.providers import LLMProvider


def evaluate(
    payload: Dict[str, Any], judge_llms: Optional[List[LLMProvider]] = None
) -> Dict[str, Any]:
    

    if judge_llms is None:
        judge_llms = []

    goals = payload["episode"]["eval"]["goals"]
    final_home_state = payload["final_home_state"]

    try:
        required_actions_result = evaluate_required_actions(payload)
    except ValueError as e:
        return {
            "score": -1,
            "error_type": f"Required Actions Schema Error: {e}",
            "required_actions": [],
            "targets_eval": [],
        }

    tools_ok = all(action["invoked"] for action in required_actions_result)

    asserts_results = []
    for _, goal in enumerate(goals):
        device_id = goal["device_id"]
        asserts = goal["asserts"]
        diffs = []
        ok = True
        for a in asserts:
            attribute = a["attribute"]
            expected = a["value"]
            actual = read_device_attr(final_home_state, device_id, attribute)
            if actual != expected:
                diffs.append(
                    {"attribute": attribute, "expected": expected, "actual": actual}
                )
                ok = False
        asserts_results.append({"device_id": device_id, "ok": ok, "diffs": diffs})

    score = 1 if tools_ok and all(result["ok"] for result in asserts_results) else 0
    return {
        "score": score,
        "required_actions": required_actions_result,
        "targets_eval": asserts_results,
    }
