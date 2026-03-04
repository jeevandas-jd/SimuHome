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
from prompts.qt4_1.infeasible.generation import SYSTEM_PROMPT, USER_PROMPT


def _format_asserts_description(asserts: List[Dict[str, Any]]) -> str:
    
    descriptions = []

    for assert_item in asserts:
        attribute = assert_item.get("attribute", "")
        value = assert_item.get("value")
        value_type = assert_item.get("value_type", "")
        description = assert_item.get("description", "")

        if "OnOff" in attribute and value is True:
            descriptions.append("turn on")
        elif "OnOff" in attribute and value is False:
            descriptions.append("turn off")
        elif "LevelControl.CurrentLevel" in attribute:
            if value_type == "percent":
                descriptions.append(f"set to {value} percent")
            else:
                descriptions.append(f"set level to {value}")
        elif "ColorControl" in attribute:
            descriptions.append(f"change color")
        elif description:
            descriptions.append(description.lower())

    if not descriptions:
        return "control"
    elif len(descriptions) == 1:
        return descriptions[0]
    else:
        return " and ".join(descriptions)


def build_qt4_1_infeasible_messages(
    payload: Dict[str, Any],
) -> List[Message]:
    
    conflict_data = payload["temporal_conflict"]
    goals = payload["eval"]["goals"]
    user_location = format_room_name(payload.get("user_location", ""))

    target = goals[0]["targets"][0]
    target_name = format_device_name(
        target["device_type"], extract_device_number(target["device_id"])
    )
    target_room = format_room_name(target["room_id"])

    asserts = target.get("asserts", [])
    action_description = _format_asserts_description(asserts)

    expected_minutes = conflict_data["expected_at"]
    conflict_time = format_absolute_time(
        conflict_data["base_time"], conflict_data["conflict_at"]
    )
    conflict_time = format_time_12h(conflict_time)

    user_prompt = USER_PROMPT.format(
        user_location=user_location,
        target_name=target_name,
        target_room=target_room,
        action_description=action_description,
        expected_minutes=expected_minutes,
        conflict_time=conflict_time,
    )
    return [
        Message(role="system", content=SYSTEM_PROMPT),
        Message(role="user", content=user_prompt),
    ]

__all__ = ["build_qt4_1_infeasible_messages"]
