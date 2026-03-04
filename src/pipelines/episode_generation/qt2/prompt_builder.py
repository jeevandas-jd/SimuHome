from __future__ import annotations
from typing import Any, Dict, List

from src.pipelines.episode_generation.shared.messages import Message
from src.pipelines.episode_generation.shared.formatting import format_room_name
from prompts.qt2.feasible.generation import SYSTEM_PROMPT, USER_PROMPT, ROOM_SECTION_HEADER, ROOM_STATE_LINE


_ROOM_STATE_DISPLAY = {
    "temperature": "temperature",
    "humidity": "humidity",
    "illuminance": "lighting",
    "pm10": "air quality",
}

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


def build_qt2_messages(payload: Dict[str, Any]) -> List[Message]:
    
    user_location = format_room_name(payload.get("user_location", ""))
    goals = payload.get("eval", {}).get("goals", [])
    current_time = payload.get("initial_home_config", {}).get("base_time", "")

    room_groups = _group_goals_by_room(goals)

    room_states = ""
    for room_id, room_goals in room_groups.items():
        room_name = format_room_name(room_id)
        room_states += ROOM_SECTION_HEADER.format(room_name=room_name)

        for goal in room_goals:
            room_state = goal.get("room_state", "")
            direction = goal.get("direction", "")
            display_state = _ROOM_STATE_DISPLAY.get(room_state, room_state)
            room_states += ROOM_STATE_LINE.format(room_state=display_state, direction=direction)


    user_prompt = USER_PROMPT.format(
        user_location=user_location,
        current_time=current_time,
        room_states=room_states,
    )
    return [
        Message(role="system", content=SYSTEM_PROMPT),
        Message(role="user", content=user_prompt),
    ]
