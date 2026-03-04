from __future__ import annotations

from typing import Any, Dict, List

from src.pipelines.episode_generation.shared.messages import Message
from src.pipelines.episode_generation.shared.formatting import (
    extract_device_number,
    format_room_name,
    format_device_name,
)
from prompts.qt4_1.feasible.generation import SYSTEM_PROMPT, USER_PROMPT, DEVICE_ACTION_LINE


_IMPLICIT_ASSERT_ATTRS: frozenset[str] = frozenset({
    "1.OnOff.OnOff",
    "1.OperationalState.OperationalState",
    "1.RVCOperationalState.OperationalState",
})

def _format_timing_naturally(
    reference_minutes: int, relation: str, offset_minutes: int
) -> str:
    
    if reference_minutes == 0:
        return f"{offset_minutes} minutes from now"
    else:
        if relation == "after":
            return f"{offset_minutes} minutes after the previous action"
        elif relation == "before":
            return (
                f"{offset_minutes} minutes before {reference_minutes} minutes from now"
            )
        else:
            return f"{offset_minutes} minutes {relation} {reference_minutes} minutes from now"


def build_qt4_1_feasible_messages(payload: Dict[str, Any]) -> List[Message]:
    user_location = format_room_name(payload.get("user_location", ""))
    goals = payload.get("eval", {}).get("goals", [])

    device_actions = ""

    for i, goal in enumerate(goals, 1):
        when = goal.get("when", {})
        targets = goal.get("targets", [])

        for target in targets:
            room_id = target.get("room_id", "")
            device_id = target.get("device_id", "")
            device_type = target.get("device_type", "")
            asserts = target.get("asserts", [])

            device_number = extract_device_number(device_id)
            device_name = format_device_name(device_type, device_number)
            room_name = format_room_name(room_id)

            action_descriptions = []
            for assert_item in asserts:
                if assert_item.get("attribute") in _IMPLICIT_ASSERT_ATTRS:
                    continue
                desc = assert_item.get("description", "").strip()
                if desc:
                    action_descriptions.append(desc)

            reference_minutes = when.get("reference_minutes", 0)
            relation = when.get("relation", "after")
            offset_minutes = when.get("offset_minutes", 0)

            natural_timing = _format_timing_naturally(
                reference_minutes, relation, offset_minutes
            )

            device_actions += DEVICE_ACTION_LINE.format(
                i=i,
                room_name=room_name,
                device_name=device_name,
                natural_timing=natural_timing,
                action_descriptions=" + ".join(action_descriptions),
            )

    user_prompt = USER_PROMPT.format(
        user_location=user_location,
        device_actions=device_actions,
    )
    return [
        Message(role="system", content=SYSTEM_PROMPT),
        Message(role="user", content=user_prompt),
    ]


__all__ = [
    "build_qt4_1_feasible_messages",
    "_format_timing_naturally",
]
