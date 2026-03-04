from __future__ import annotations

from typing import Any, Dict, List

from src.pipelines.episode_generation.shared.messages import Message
from src.pipelines.episode_generation.shared.formatting import (
    extract_device_number,
    format_device_name,
    format_room_name,
    get_anchor_finish_phrase,
)
from src.pipelines.episode_generation.shared.time_utils import (
    format_time_12h,
    format_absolute_time,
)
from prompts.qt4_2.infeasible.generation import SYSTEM_PROMPT, USER_PROMPT


def build_qt4_2_infeasible_messages(payload: Dict[str, Any]) -> List[Message]:
    
    conflict_data = payload["temporal_conflict"]
    goals = payload["eval"]["goals"]
    goal = goals[0]

    anchor = goal["anchor"]
    targets = goal["targets"]

    anchor_name = format_device_name(
        anchor["device_type"], extract_device_number(anchor["device_id"])
    )
    anchor_room = format_room_name(anchor["room_id"])
    finish_phrase = get_anchor_finish_phrase(anchor["device_type"])

    relation = conflict_data["relation"]
    offset_minutes = conflict_data["offset_minutes"]
    conflict_time = format_absolute_time(
        conflict_data["base_time"], conflict_data["conflict_at"]
    )

    target_info_list = []
    for target in targets:
        target_name = format_device_name(
            target["device_type"], extract_device_number(target["device_id"])
        )
        target_room = format_room_name(target["room_id"])

        asserts = target.get("asserts", [])
        if asserts:
            setting_descriptions = []
            for assert_item in asserts:
                description = assert_item.get("description", "")
                if description:
                    setting_descriptions.append(description)

            if setting_descriptions:
                settings_text = f" ({', '.join(setting_descriptions)})"
            else:
                settings_text = ""
        else:
            settings_text = ""

        target_info_list.append(f"{target_name}{settings_text} in the {target_room}")

    relation_phrase = "after" if relation == "after" else "before"

    user_prompt = USER_PROMPT.format(
        anchor_name=anchor_name,
        anchor_room=anchor_room,
        target_info_list=', '.join(target_info_list),
        offset_minutes=offset_minutes,
        relation_phrase=relation_phrase,
        finish_phrase=finish_phrase,
        conflict_time=format_time_12h(conflict_time),
    )

    return [
        Message(role="system", content=SYSTEM_PROMPT),
        Message(role="user", content=user_prompt),
    ]


__all__ = ["build_qt4_2_infeasible_messages"]
