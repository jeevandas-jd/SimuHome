from __future__ import annotations

from typing import Any, Dict, List

from src.pipelines.episode_generation.shared.messages import Message
from src.pipelines.episode_generation.shared.formatting import (
    format_room_name,
    extract_device_number,
    format_device_name,
)
from prompts.qt3.feasible.generation import SYSTEM_PROMPT, USER_PROMPT, ROOM_SECTION_HEADER, DEVICE_ATTRIBUTE_LINE


def _group_goals_by_room(
    goals: List[Dict[str, Any]],
) -> Dict[str, List[Dict[str, Any]]]:
    
    room_groups = {}
    for goal in goals:
        room_id = goal.get("room_id", "")
        if room_id not in room_groups:
            room_groups[room_id] = []
        room_groups[room_id].append(goal)
    return room_groups


def build_qt3_messages(payload: Dict[str, Any]) -> List[Message]:
    user_location = format_room_name(payload.get("user_location", ""))
    goals = payload.get("eval", {}).get("goals", [])
    current_time = payload.get("initial_home_config", {}).get("base_time", "")


    lines = []

    required_end_states = ""

    room_groups = _group_goals_by_room(goals)

    for room_id, room_goals in room_groups.items():
        room_name = format_room_name(room_id)
        required_end_states += ROOM_SECTION_HEADER.format(room_name=room_name)

        for goal in room_goals:
            device_id = goal.get("device_id", "")
            device_type = goal.get("device_type", "")
            asserts = goal.get("asserts", [])

            device_number = extract_device_number(device_id)
            device_name = format_device_name(device_type, device_number)

            action_descriptions = []
            for assert_item in asserts:
                desc = assert_item.get("description", "").strip()
                if desc:
                    action_descriptions.append(desc)

            state_text = " + ".join(action_descriptions)
            required_end_states += DEVICE_ATTRIBUTE_LINE.format(device_name=device_name, required_end_states=state_text)

    user_prompt = USER_PROMPT.format(
        user_location=user_location,
        current_time=current_time,
        required_end_states=required_end_states,
    )
    return [
        Message(role="system", content=SYSTEM_PROMPT),
        Message(role="user", content=user_prompt),
    ]


__all__ = [
    "build_qt3_messages",
    "Message",
    "_group_goals_by_room",
]
