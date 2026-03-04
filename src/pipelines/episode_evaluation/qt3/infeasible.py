from __future__ import annotations

from typing import Dict, Any, List
from src.pipelines.episode_evaluation.common import (
    evaluate_required_actions,
    extract_steps,
    extract_final_answer,
    run_judge_panel,
)
from src.agents.providers import LLMProvider
from prompts.qt3.infeasible.evaluation import SYSTEM_PROMPT, USER_PROMPT_TEMPLATE


def evaluate(payload: Dict[str, Any], judge_llms: List[LLMProvider]) -> Dict[str, Any]:
    query = payload["episode"]["query"]
    goals = payload["episode"]["eval"]["goals"]
    steps = extract_steps(payload)
    final_answer = extract_final_answer(steps)

    try:
        required_actions_result = evaluate_required_actions(payload)
    except ValueError as e:
        return {
            "score": -1,
            "error_type": f"Required Actions Schema Error: {e}",
            "required_actions": [],
            "judge": [],
        }

    tools_ok = all(action["invoked"] for action in required_actions_result)

    score = 0
    if not tools_ok:
        return {
            "score": score,
            "error_type": "Required Actions Failure",
            "required_actions": required_actions_result,
            "judge": [],
        }

    if not final_answer:
        return {
            "score": score,
            "error_type": "Final Response Failure",
            "required_actions": required_actions_result,
            "judge": [],
        }

    system = SYSTEM_PROMPT

    user = USER_PROMPT_TEMPLATE.format(
        query=query,
        goals=str(goals),
        react_steps=str(steps),
        final_answer=final_answer,
    )

    judge_result = run_judge_panel(judge_llms, system, user)

    return {
        "score": judge_result["score"],
        "error_type": judge_result["error_type"],
        "required_actions": required_actions_result,
        "judge": judge_result["judge"],
    }
