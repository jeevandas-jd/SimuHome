from __future__ import annotations

from typing import Any, Dict, List

from src.pipelines.episode_generation.shared.messages import Message
from src.pipelines.episode_generation.shared.formatting import (
    extract_device_number,
    format_room_name,
    format_device_name,
    get_anchor_finish_phrase,
)
from prompts.qt4_2.feasible.generation import SYSTEM_PROMPT, USER_PROMPT


def _format_anchor_timing(
    anchor_device_type: str,
    anchor_alias: str,
    anchor_room: str,
    relation: str,
    offset_minutes: int,
) -> str:
    
    finish_phrase = get_anchor_finish_phrase(anchor_device_type)
    room_name = format_room_name(anchor_room)

    if relation == "before":
        return f"{offset_minutes} minutes before the {anchor_alias} in the {room_name} {finish_phrase}"
    else:
        return f"{offset_minutes} minutes after the {anchor_alias} in the {room_name} {finish_phrase}"


def build_qt4_2_feasible_messages(payload: Dict[str, Any]) -> List[Message]:
    
    goals = payload.get("eval", {}).get("goals", [])


    goal = goals[0]
    when = goal.get("when", {})
    anchor = goal.get("anchor", {})
    targets = goal.get("targets", [])

    anchor_room = anchor.get("room_id", "")
    anchor_device_type = anchor.get("device_type", "")
    anchor_device_id = anchor.get("device_id", "")
    anchor_device_number = extract_device_number(anchor_device_id)
    anchor_alias = format_device_name(anchor_device_type, anchor_device_number)

    relation = when.get("relation", "after")
    offset_minutes = when.get("offset_minutes", 0)

    timing_phrase = _format_anchor_timing(
        anchor_device_type, anchor_alias, anchor_room, relation, offset_minutes
    )

    lines = []
    for i, target in enumerate(targets, 1):
        room_id = target.get("room_id", "")
        device_id = target.get("device_id", "")
        device_type = target.get("device_type", "")
        asserts = target.get("asserts", [])

        device_number = extract_device_number(device_id)
        device_name = format_device_name(device_type, device_number)
        room_name = format_room_name(room_id)

        action_descriptions = []
        for assert_item in asserts:
            desc = assert_item.get("description", "").strip()
            if desc:
                action_descriptions.append(desc)

        lines.append(f"{i}. {device_name} in the {room_name}")
        lines.append(f"   -> {' + '.join(action_descriptions)}")

    targets_text = "\n".join(lines)
    user_prompt = USER_PROMPT.format(
        timing_phrase=timing_phrase,
        targets=targets_text,
    )

    return [
        Message(role="system", content=SYSTEM_PROMPT),
        Message(role="user", content=user_prompt),
    ]

__all__ = [
    "build_qt4_2_feasible_messages",
    "_format_anchor_timing",
]
