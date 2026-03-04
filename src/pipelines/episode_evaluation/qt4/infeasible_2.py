from __future__ import annotations

from typing import Dict, Any, List
from src.pipelines.episode_evaluation.common import (
    extract_steps,
    extract_reasoning_and_answer,
    run_judge_panel,
)
from src.agents.providers import LLMProvider
from prompts.qt4_2.infeasible.evaluation import (
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

    device_info = _extract_op_nonop_device_info(goals)
    system, conflict_context = _build_op_nonop_timing_mismatch_context(
        temporal_conflict, device_info
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


def _extract_op_nonop_device_info(goals: List[Dict[str, Any]]) -> Dict[str, Any]:
    
    if not goals:
        return {"anchor": {}, "targets": []}

    goal = goals[0]
    anchor = goal.get("anchor", {})
    targets = goal.get("targets", [])

    return {
        "anchor": {
            "device_type": anchor.get("device_type", ""),
            "room_id": anchor.get("room_id", ""),
            "device_id": anchor.get("device_id", ""),
        },
        "targets": [
            {
                "device_type": target.get("device_type", ""),
                "room_id": target.get("room_id", ""),
                "device_id": target.get("device_id", ""),
            }
            for target in targets
        ],
    }


def _build_op_nonop_timing_mismatch_context(
    temporal_conflict: Dict[str, Any], device_info: Dict[str, Any]
) -> tuple[str, str]:
    

    anchor_id = device_info["anchor"]["device_id"]
    targets = device_info["targets"]
    targets_ids_list = [target["device_id"] for target in targets]
    targets_ids = ", ".join(targets_ids_list)

    relation = temporal_conflict["relation"]
    offset_minutes = temporal_conflict["offset_minutes"]
    conflict_time = temporal_conflict["conflict_time"]
    anchor_end_time = temporal_conflict["anchor_end_time"]
    expected_time = temporal_conflict["expected_time"]

    system_prompt = SYSTEM_PROMPT

    conflict_context = CONFLICT_CONTEXT_TEMPLATE.format(
        targets_ids=targets_ids,
        anchor_id=anchor_id,
        relation=relation,
        offset_minutes=offset_minutes,
        conflict_time=conflict_time,
        anchor_end_time=anchor_end_time,
        expected_time=expected_time,
    )

    return system_prompt, conflict_context
