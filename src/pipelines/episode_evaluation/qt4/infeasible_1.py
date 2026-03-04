from __future__ import annotations

from typing import Dict, Any, List
from src.pipelines.episode_evaluation.common import (
    extract_steps,
    extract_reasoning_and_answer,
    run_judge_panel,
)
from src.agents.providers import LLMProvider
from prompts.qt4_1.infeasible.evaluation import (
    SYSTEM_PROMPT,
    USER_PROMPT_TEMPLATE,
    CONFLICT_CONTEXT_TEMPLATE,
)


def evaluate(payload: Dict[str, Any], judge_llms: List[LLMProvider]) -> Dict[str, Any]:
    query = payload["episode"]["query"]
    goals = payload["episode"]["eval"]["goals"]
    temporal_conflict = payload["episode"]["temporal_conflict"]
    steps = extract_steps(payload)
    reasoning_data = extract_reasoning_and_answer(steps)
    final_answer = reasoning_data["final_answer"]

    score = 0

    if not final_answer:
        return {
            "score": score,
            "error_type": "Final Response Failure",
            "required_actions": [],
            "judge": [],
        }

    system, conflict_context = _build_nonop_multi_timing_mismatch_context(
        temporal_conflict, goals
    )

    user = USER_PROMPT_TEMPLATE.format(
        query=query,
        conflict_context=conflict_context,
        reasoning_process=reasoning_data["reasoning_process"],
        final_answer=final_answer,
    )
    judge_result = run_judge_panel(judge_llms, system, user)

    return {
        "score": judge_result["score"],
        "error_type": judge_result["error_type"],
        "required_actions": [],
        "judge": judge_result["judge"],
    }


def _build_nonop_multi_timing_mismatch_context(
    temporal_conflict: Dict[str, Any], goals: List[Dict[str, Any]]
) -> tuple[str, str]:
    

    target_id = goals[0]["targets"][0]["device_id"]
    delay_minutes = temporal_conflict["expected_at"]
    current_time = temporal_conflict["base_time"]
    expected_time = temporal_conflict["expected_time"]
    conflict_time = temporal_conflict["conflict_time"]

    system_prompt = SYSTEM_PROMPT

    conflict_context = CONFLICT_CONTEXT_TEMPLATE.format(
        target_id=target_id,
        delay_minutes=delay_minutes,
        current_time=current_time,
        expected_time=expected_time,
        conflict_time=conflict_time,
    )

    return system_prompt, conflict_context
