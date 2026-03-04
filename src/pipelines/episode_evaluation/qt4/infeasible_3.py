from __future__ import annotations

from typing import Dict, Any, List
from datetime import datetime, timedelta
from src.pipelines.episode_evaluation.common import (
    extract_steps,
    extract_reasoning_and_answer,
    run_judge_panel,
)
from src.agents.providers import LLMProvider
from prompts.qt4_3.infeasible.evaluation import (
    SYSTEM_PROMPT_ABSOLUTE_TIME_MISMATCH,
    SYSTEM_PROMPT_COMPLETION_VS_PAUSE,
    SYSTEM_PROMPT_DELAY_TIME_MISMATCH,
    SYSTEM_PROMPT_IMPOSSIBLE_EARLY_END,
    CONFLICT_CONTEXT_TEMPLATE_ABSOLUTE_TIME_MISMATCH,
    CONFLICT_CONTEXT_TEMPLATE_COMPLETION_VS_PAUSE,
    CONFLICT_CONTEXT_TEMPLATE_DELAY_TIME_MISMATCH,
    CONFLICT_CONTEXT_TEMPLATE_IMPOSSIBLE_EARLY_END,
    USER_PROMPT_TEMPLATE,
)


def evaluate(payload: Dict[str, Any], judge_llms: List[LLMProvider]) -> Dict[str, Any]:
    
    query = payload["episode"]["query"]
    goals = payload["episode"]["eval"]["goals"]
    temporal_conflict = payload["episode"]["temporal_conflict"]
    conflict_type = temporal_conflict["type"]
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

    device_info = _extract_device_info(goals)

    if conflict_type == "absolute_time_mismatch":
        system, conflict_context = _build_absolute_time_mismatch_context(
            temporal_conflict, device_info
        )

    elif conflict_type == "completion_vs_pause":
        system, conflict_context = _build_completion_vs_pause_context(
            temporal_conflict, device_info
        )

    elif conflict_type == "delay_time_mismatch":
        system, conflict_context = _build_delay_time_mismatch_context(
            temporal_conflict, device_info
        )

    elif conflict_type == "impossible_early_end":
        system, conflict_context = _build_impossible_early_end_context(
            temporal_conflict, device_info
        )

    else:
        system = (
            "You are a strict evaluator for smart-home agents handling temporal conflicts in appliance coordination scenarios.\n"
            "CONFLICT TYPE: Unknown\n"
            "Return EXACTLY ONE character: 'A' (pass) or 'B' (fail). No other text.\n\n"
            "Pass (A) IF the agent recognizes any timing conflict or provides alternatives.\n"
            "Fail (B) IF the agent ignores conflicts and proceeds without alternatives."
        )
        conflict_context = f"Unknown conflict type: {conflict_type}"

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


def _extract_device_info(goals: List[Dict[str, Any]]) -> Dict[str, Any]:
    
    if not goals:
        return {"anchor": {}, "targets": []}

    goal = goals[0]
    anchor = goal["anchor"]
    targets = goal["targets"]

    return {
        "anchor": {
            "room_id": anchor["room_id"],
            "device_id": anchor["device_id"],
            "device_type": anchor["device_type"],
        },
        "targets": [
            {
                "room_id": target["room_id"],
                "device_type": target["device_type"],
                "device_id": target["device_id"],
            }
            for target in targets
        ],
    }


def _build_absolute_time_mismatch_context(
    temporal_conflict: Dict[str, Any], device_info: Dict[str, Any]
) -> tuple[str, str]:
    

    anchor_id = device_info["anchor"]["device_id"]
    targets = device_info["targets"]
    targets_ids_list = [target["device_id"] for target in targets]
    targets_ids = (
        ", ".join(targets_ids_list)
        if len(targets_ids_list) > 1
        else targets_ids_list[0]
    )

    anchor_end_time = temporal_conflict["anchor_end_time"]
    conflict_time = temporal_conflict["conflict_time"]

    system_prompt = SYSTEM_PROMPT_ABSOLUTE_TIME_MISMATCH

    conflict_context = CONFLICT_CONTEXT_TEMPLATE_ABSOLUTE_TIME_MISMATCH.format(
        targets_ids=targets_ids,
        anchor_id=anchor_id,
        conflict_time=conflict_time,
    )

    return system_prompt, conflict_context


def _build_completion_vs_pause_context(
    temporal_conflict: Dict[str, Any], device_info: Dict[str, Any]
) -> tuple[str, str]:
    

    anchor_id = device_info["anchor"]["device_id"]
    targets = device_info["targets"]
    targets_ids_list = [target["device_id"] for target in targets]
    targets_ids = (
        ", ".join(targets_ids_list)
        if len(targets_ids_list) > 1
        else targets_ids_list[0]
    )

    system_prompt = SYSTEM_PROMPT_COMPLETION_VS_PAUSE

    conflict_context = CONFLICT_CONTEXT_TEMPLATE_COMPLETION_VS_PAUSE.format(
        anchor_id=anchor_id,
        targets_ids=targets_ids,
    )

    return system_prompt, conflict_context


def _build_delay_time_mismatch_context(
    temporal_conflict: Dict[str, Any], device_info: Dict[str, Any]
) -> tuple[str, str]:
    

    anchor_id = device_info["anchor"]["device_id"]
    targets = device_info["targets"]
    targets_ids_list = [target["device_id"] for target in targets]
    targets_ids = (
        ", ".join(targets_ids_list)
        if len(targets_ids_list) > 1
        else targets_ids_list[0]
    )

    delay_minutes = temporal_conflict["delay_minutes"]
    anchor_end_time = temporal_conflict["anchor_end_time"]
    expected_time = temporal_conflict["expected_time"]
    conflict_time = temporal_conflict["conflict_time"]
    user_misperceived_anchor_end_time = (
        datetime.strptime(conflict_time, "%H:%M:%S") - timedelta(minutes=delay_minutes)
    ).strftime("%H:%M:%S")

    system_prompt = SYSTEM_PROMPT_DELAY_TIME_MISMATCH

    conflict_context = CONFLICT_CONTEXT_TEMPLATE_DELAY_TIME_MISMATCH.format(
        targets_ids=targets_ids,
        delay_minutes=delay_minutes,
        anchor_id=anchor_id,
        user_misperceived_anchor_end_time=user_misperceived_anchor_end_time,
        anchor_end_time=anchor_end_time,
        expected_time=expected_time,
        conflict_time=conflict_time,
    )

    return system_prompt, conflict_context


def _build_impossible_early_end_context(
    temporal_conflict: Dict[str, Any], device_info: Dict[str, Any]
) -> tuple[str, str]:
    

    anchor_id = device_info["anchor"]["device_id"]
    targets = device_info["targets"]
    targets_ids_list = [target["device_id"] for target in targets]
    targets_ids = (
        ", ".join(targets_ids_list)
        if len(targets_ids_list) > 1
        else targets_ids_list[0]
    )

    anchor_end_time = temporal_conflict["anchor_end_time"]
    conflict_time = temporal_conflict["conflict_time"]

    system_prompt = SYSTEM_PROMPT_IMPOSSIBLE_EARLY_END

    conflict_context = CONFLICT_CONTEXT_TEMPLATE_IMPOSSIBLE_EARLY_END.format(
        anchor_id=anchor_id,
        targets_ids=targets_ids,
        conflict_time=conflict_time,
        anchor_end_time=anchor_end_time,
    )

    return system_prompt, conflict_context
