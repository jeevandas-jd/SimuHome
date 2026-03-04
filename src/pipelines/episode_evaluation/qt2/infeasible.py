from __future__ import annotations

from typing import Dict, Any, List
from src.pipelines.episode_evaluation.common import (
    evaluate_required_actions,
    extract_steps,
    extract_final_answer,
    run_judge_panel,
)
from src.agents.providers import LLMProvider
from prompts.qt2.infeasible.evaluation import (
    SYSTEM_PROMPT_INFEASIBLE,
    SYSTEM_PROMPT_NONEXISTANCE,
    USER_PROMPT_TEMPLATE_INFEASIBLE,
    USER_PROMPT_TEMPLATE_NONEXISTANCE,
)


def _get_infeasible_prompts(
    query: str,
    goals: List[Dict[str, Any]],
    react_steps: List[Dict[str, Any]],
    final_answer: str,
) -> tuple[str, str]:
    system = SYSTEM_PROMPT_INFEASIBLE

    user = USER_PROMPT_TEMPLATE_INFEASIBLE.format(
        query=query,
        goals=str(goals),
        react_steps=str(react_steps),
        final_answer=final_answer,
    )

    return system, user


def _get_nonexistance_prompts(
    query: str,
    goals: List[Dict[str, Any]],
    react_steps: List[Dict[str, Any]],
    final_answer: str,
) -> tuple[str, str]:
    system = SYSTEM_PROMPT_NONEXISTANCE

    user = USER_PROMPT_TEMPLATE_NONEXISTANCE.format(
        query=query,
        goals=str(goals),
        react_steps=str(react_steps),
        final_answer=final_answer,
    )

    return system, user


def _resolve_infeasible_family(meta: Dict[str, Any]) -> str:
    family_raw = str(meta.get("infeasible_family") or "").strip().lower()

    if family_raw == "contextual_saturation":
        return "contextual_saturation"

    if family_raw == "nonexistence":
        return "nonexistence"

    raise ValueError(
        "qt2 infeasible episodes require meta.infeasible_family to be one of "
        "['contextual_saturation', 'nonexistence']"
    )


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

    meta = payload["episode"].get("meta", {})
    family = _resolve_infeasible_family(meta)

    if family == "contextual_saturation":
        system, user = _get_infeasible_prompts(query, goals, steps, final_answer)
    else:
        system, user = _get_nonexistance_prompts(query, goals, steps, final_answer)

    judge_result = run_judge_panel(judge_llms, system, user)

    return {
        "score": judge_result["score"],
        "error_type": judge_result["error_type"],
        "required_actions": required_actions_result,
        "judge": judge_result["judge"],
    }
