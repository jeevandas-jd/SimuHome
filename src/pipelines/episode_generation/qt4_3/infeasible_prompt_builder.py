from __future__ import annotations

from typing import Any, Dict, List

from src.pipelines.episode_generation.shared.messages import Message
from src.pipelines.episode_generation.shared.formatting import (
    extract_device_number,
    format_device_name,
    format_room_name,
)
from src.pipelines.episode_generation.shared.time_utils import (
    format_time_12h,
    format_absolute_time,
)
from src.pipelines.episode_generation.qt4_3.feasible_prompt_builder import (
    _IMPLICIT_ASSERT_ATTRS,
)
from prompts.qt4_3.infeasible.generation import (
    SYSTEM_PROMPT_ABSOLUTE_TIME_MISMATCH,
    SYSTEM_PROMPT_COMPLETION_VS_PAUSE,
    SYSTEM_PROMPT_DELAY_TIME_MISMATCH,
    SYSTEM_PROMPT_IMPOSSIBLE_EARLY_END,
    USER_PROMPT_ABSOLUTE_TIME_MISMATCH,
    USER_PROMPT_COMPLETION_VS_PAUSE,
    USER_PROMPT_DELAY_TIME_MISMATCH,
    USER_PROMPT_IMPOSSIBLE_EARLY_END,
)


def _build_assert_text(asserts: List[Dict[str, Any]], target_name: str) -> str:
    lines = []
    for assert_item in asserts:
        if assert_item.get("attribute") in _IMPLICIT_ASSERT_ATTRS:
            continue
        desc = assert_item.get("description", "").strip()
        if desc:
            lines.append(f"   -> {desc}")
    return "\n".join(lines) + "\n" if lines else ""


def build_qt4_3_infeasible_messages(payload: Dict[str, Any]) -> List[Message]:
    conflict_data = payload["temporal_conflict"]
    conflict_type = conflict_data["type"]
    goals = payload["eval"]["goals"]

    anchor = goals[0]["anchor"]
    target = goals[0]["targets"][0]

    anchor_name = format_device_name(
        anchor["device_type"], extract_device_number(anchor["device_id"])
    )
    target_name = format_device_name(
        target["device_type"], extract_device_number(target["device_id"])
    )
    anchor_room = format_room_name(anchor["room_id"])
    target_room = format_room_name(target["room_id"])

    current_time = format_absolute_time(conflict_data["base_time"], 0)

    if conflict_type == "absolute_time_mismatch":
        conflict_time = format_absolute_time(
            conflict_data["base_time"], conflict_data["conflict_at"]
        )
        assert_text = _build_assert_text(target.get("asserts", []), target_name)

        system_prompt = SYSTEM_PROMPT_ABSOLUTE_TIME_MISMATCH
        user_prompt = USER_PROMPT_ABSOLUTE_TIME_MISMATCH.format(
            current_time=format_time_12h(current_time),
            anchor_name=anchor_name,
            anchor_room=anchor_room,
            target_name=target_name,
            target_room=target_room,
            conflict_time=format_time_12h(conflict_time),
            assert_text=assert_text,
        )

    elif conflict_type == "completion_vs_pause":
        system_prompt = SYSTEM_PROMPT_COMPLETION_VS_PAUSE
        user_prompt = USER_PROMPT_COMPLETION_VS_PAUSE.format(
            current_time=format_time_12h(current_time),
            anchor_name=anchor_name,
            anchor_room=anchor_room,
            target_name=target_name,
            target_room=target_room,
        )

    elif conflict_type == "delay_time_mismatch":
        delay = conflict_data["delay_minutes"]
        conflict_time = format_absolute_time(
            conflict_data["base_time"], conflict_data["conflict_at"]
        )
        anchor_end_time = format_absolute_time(
            conflict_data["base_time"], conflict_data["conflict_at"] - delay
        )
        assert_text = _build_assert_text(target.get("asserts", []), target_name)

        system_prompt = SYSTEM_PROMPT_DELAY_TIME_MISMATCH
        user_prompt = USER_PROMPT_DELAY_TIME_MISMATCH.format(
            current_time=format_time_12h(current_time),
            anchor_name=anchor_name,
            anchor_room=anchor_room,
            target_name=target_name,
            target_room=target_room,
            anchor_end_time=format_time_12h(anchor_end_time),
            delay=delay,
            assert_text=assert_text,
        )

    elif conflict_type == "impossible_early_end":
        conflict_time = format_absolute_time(
            conflict_data["base_time"], conflict_data["conflict_at"]
        )
        assert_text = _build_assert_text(target.get("asserts", []), target_name)

        system_prompt = SYSTEM_PROMPT_IMPOSSIBLE_EARLY_END
        user_prompt = USER_PROMPT_IMPOSSIBLE_EARLY_END.format(
            current_time=format_time_12h(current_time),
            anchor_name=anchor_name,
            anchor_room=anchor_room,
            target_name=target_name,
            target_room=target_room,
            conflict_time=format_time_12h(conflict_time),
            assert_text=assert_text,
        )

    else:
        raise ValueError(f"Unknown conflict type: {conflict_type}")

    return [
        Message(role="system", content=system_prompt),
        Message(role="user", content=user_prompt),
    ]


__all__ = ["build_qt4_3_infeasible_messages"]
