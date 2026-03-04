from __future__ import annotations

from typing import Any, Dict, List

from src.pipelines.episode_generation.shared.messages import Message
from src.pipelines.episode_generation.shared.formatting import (
    extract_device_number,
    format_room_name,
    format_device_name,
)
from prompts.qt4_3.feasible.generation import (
    SYSTEM_PROMPT_PAUSE_AT_ANCHOR_END,
    SYSTEM_PROMPT_DELAYED_START,
    SYSTEM_PROMPT_ALIGN_END_WITH_ANCHOR,
    USER_PROMPT_PAUSE_AT_ANCHOR_END,
    USER_PROMPT_DELAYED_START,
    USER_PROMPT_ALIGN_END_WITH_ANCHOR,
)


_IMPLICIT_ASSERT_ATTRS: frozenset[str] = frozenset({
    "1.OnOff.OnOff",
    "1.OperationalState.OperationalState",
    "1.RVCOperationalState.OperationalState",
})

def _detect_scenario(payload: Dict[str, Any]) -> str:
    
    return payload.get("meta", {}).get("scenario", "unknown")


def _extract_pause_scenario_data(payload: Dict[str, Any]) -> Dict[str, Any]:
    
    goals = payload.get("eval", {}).get("goals", [])

    pre_goal = next(
        (g for g in goals if g.get("when", {}).get("tolerance_ticks", 0) == 0), None
    )
    main_goal = next(
        (g for g in goals if g.get("when", {}).get("tolerance_ticks", 0) > 0), None
    )

    if not main_goal:
        raise ValueError("No main goal with tolerance found in pause scenario")

    anchor = main_goal.get("anchor", {})
    anchor_room = anchor.get("room_id", "")
    anchor_device_type = anchor.get("device_type", "")
    anchor_device_id = anchor.get("device_id", "")
    anchor_device_number = extract_device_number(anchor_device_id)

    targets = main_goal.get("targets", [])
    if not targets:
        raise ValueError("No targets found in main goal")

    target = targets[0]
    target_room = target.get("room_id", "")
    target_device_type = target.get("device_type", "")
    target_device_id = target.get("device_id", "")
    target_device_number = extract_device_number(target_device_id)

    pre_asserts = []
    if pre_goal and pre_goal.get("targets"):
        pre_target = pre_goal.get("targets", [{}])[0]
        pre_asserts = pre_target.get("asserts", [])

    main_asserts = target.get("asserts", [])

    return {
        "anchor": {
            "room": anchor_room,
            "type": anchor_device_type,
            "id": anchor_device_id,
            "number": anchor_device_number,
        },
        "target": {
            "room": target_room,
            "type": target_device_type,
            "id": target_device_id,
            "number": target_device_number,
        },
        "requirements": {"start_asserts": pre_asserts, "pause_asserts": main_asserts},
    }


def _extract_delayed_start_data(payload: Dict[str, Any]) -> Dict[str, Any]:
    
    goals = payload["eval"]["goals"]

    anchor_goal = goals[1]
    anchor_device = anchor_goal["anchor"]
    target_device = anchor_goal["targets"][0]

    offset_minutes = anchor_goal["when"]["offset_minutes"]

    start_asserts = []
    if target_device.get("asserts"):
        for assert_item in target_device["asserts"]:
            start_asserts.append(
                {
                    "attribute": assert_item["attribute"],
                    "value": assert_item["value"],
                    "description": assert_item["description"],
                }
            )

    return {
        "anchor": {
            "type": anchor_device["device_type"],
            "number": extract_device_number(anchor_device["device_id"]),
            "room": anchor_device["room_id"],
        },
        "target": {
            "type": target_device["device_type"],
            "number": extract_device_number(target_device["device_id"]),
            "room": target_device["room_id"],
        },
        "timing": {"delay_minutes": offset_minutes},
        "requirements": {"start_asserts": start_asserts},
    }


def build_pause_at_anchor_end_messages(payload: Dict[str, Any]) -> List[Message]:
    

    scenario_data = _extract_pause_scenario_data(payload)

    anchor = scenario_data["anchor"]
    target = scenario_data["target"]
    anchor_name = format_device_name(anchor["type"], anchor["number"])
    target_name = format_device_name(target["type"], target["number"])
    anchor_room = format_room_name(anchor["room"])
    target_room = format_room_name(target["room"])

    requirements = scenario_data["requirements"]
    start_asserts = requirements.get("start_asserts", [])
    pause_asserts = requirements.get("pause_asserts", [])

    assert_text = ""
    if start_asserts:
        assert_text += f"1. Start and run {target_name}\n"
        for assert_item in start_asserts:
            if assert_item.get("attribute") not in _IMPLICIT_ASSERT_ATTRS:
                desc = assert_item.get("description", "").strip()
                if desc:
                    assert_text += f"   -> {desc}\n"
    if pause_asserts:
        assert_text += f"2. When {anchor_name} finishes -> Pause {target_name}\n"
        for assert_item in pause_asserts:
            if assert_item.get("attribute") not in _IMPLICIT_ASSERT_ATTRS:
                desc = assert_item.get("description", "").strip()
                if desc:
                    assert_text += f"   -> {desc}\n"

    user_prompt = USER_PROMPT_PAUSE_AT_ANCHOR_END.format(
        anchor_name=anchor_name,
        anchor_room=anchor_room,
        target_name=target_name,
        target_room=target_room,
        assert_text=assert_text,
    )

    return [
        Message(role="system", content=SYSTEM_PROMPT_PAUSE_AT_ANCHOR_END),
        Message(role="user", content=user_prompt),
    ]


def build_delayed_start_messages(payload: Dict[str, Any]) -> List[Message]:
    

    scenario_data = _extract_delayed_start_data(payload)

    anchor = scenario_data["anchor"]
    target = scenario_data["target"]
    anchor_name = format_device_name(anchor["type"], anchor["number"])
    target_name = format_device_name(target["type"], target["number"])
    anchor_room = format_room_name(anchor["room"])
    target_room = format_room_name(target["room"])
    delay_minutes = scenario_data["timing"]["delay_minutes"]

    requirements = scenario_data["requirements"]
    start_asserts = requirements.get("start_asserts", [])

    assert_text = ""
    if start_asserts:
        for assert_item in start_asserts:
            desc = assert_item.get("description", "").strip()
            if desc:
                assert_text += f"   -> {desc}\n"

    user_prompt = USER_PROMPT_DELAYED_START.format(
        anchor_name=anchor_name,
        anchor_room=anchor_room,
        target_name=target_name,
        target_room=target_room,
        assert_text=assert_text,
        delay_minutes=delay_minutes,
    )

    return [
        Message(role="system", content=SYSTEM_PROMPT_DELAYED_START),
        Message(role="user", content=user_prompt),
    ]


def _extract_align_end_data(payload: Dict[str, Any]) -> Dict[str, Any]:
    
    goals = payload["eval"]["goals"]

    anchor_goal = goals[1]
    anchor_device = anchor_goal["anchor"]
    target_device = anchor_goal["targets"][0]

    pre_goal = goals[0]
    main_goal = goals[1]

    start_asserts = []
    end_asserts = []

    if pre_goal["targets"][0].get("asserts"):
        for assert_item in pre_goal["targets"][0]["asserts"]:
            start_asserts.append(
                {
                    "attribute": assert_item["attribute"],
                    "value": assert_item["value"],
                    "description": assert_item["description"],
                }
            )

    if main_goal["targets"][0].get("asserts"):
        for assert_item in main_goal["targets"][0]["asserts"]:
            end_asserts.append(
                {
                    "attribute": assert_item["attribute"],
                    "value": assert_item["value"],
                    "description": assert_item["description"],
                }
            )

    return {
        "anchor": {
            "type": anchor_device["device_type"],
            "number": extract_device_number(anchor_device["device_id"]),
            "room": anchor_device["room_id"],
        },
        "target": {
            "type": target_device["device_type"],
            "number": extract_device_number(target_device["device_id"]),
            "room": target_device["room_id"],
        },
        "requirements": {"start_asserts": start_asserts, "end_asserts": end_asserts},
    }


def build_align_end_with_anchor_messages(payload: Dict[str, Any]) -> List[Message]:
    

    scenario_data = _extract_align_end_data(payload)

    anchor = scenario_data["anchor"]
    target = scenario_data["target"]
    anchor_name = format_device_name(anchor["type"], anchor["number"])
    target_name = format_device_name(target["type"], target["number"])
    anchor_room = format_room_name(anchor["room"])
    target_room = format_room_name(target["room"])


    requirements = scenario_data["requirements"]
    start_asserts = requirements.get("start_asserts", [])
    end_asserts = requirements.get("end_asserts", [])

    start_assert_text = ""
    if start_asserts:
        for assert_item in start_asserts:
            desc = assert_item.get("description", "").strip()
            if desc:
                start_assert_text += f"   -> {desc}\n"

    end_assert_text = ""
    if end_asserts:
        for assert_item in end_asserts:
            desc = assert_item.get("description", "").strip()
            if desc:
                end_assert_text += f"   -> {target_name} {desc}\n"

    user_prompt = USER_PROMPT_ALIGN_END_WITH_ANCHOR.format(
        anchor_name=anchor_name,
        anchor_room=anchor_room,
        target_name=target_name,
        target_room=target_room,
        start_assert_text=start_assert_text,
        end_assert_text=end_assert_text,
    )

    return [
        Message(role="system", content=SYSTEM_PROMPT_ALIGN_END_WITH_ANCHOR),
        Message(role="user", content=user_prompt),
    ]


def build_qt4_3_feasible_messages(payload: Dict[str, Any]) -> List[Message]:
    
    scenario = _detect_scenario(payload)

    if scenario == "pause_at_anchor_end":
        return build_pause_at_anchor_end_messages(payload)
    elif scenario == "delayed_start":
        return build_delayed_start_messages(payload)
    elif scenario == "align_end_with_anchor":
        return build_align_end_with_anchor_messages(payload)
    else:
        raise ValueError(f"Unknown scenario: {scenario}")


__all__ = [
    "build_qt4_3_feasible_messages",
    "build_pause_at_anchor_end_messages",
    "build_delayed_start_messages",
    "build_align_end_with_anchor_messages",
    "_detect_scenario",
    "_extract_pause_scenario_data",
    "_extract_delayed_start_data",
    "_extract_align_end_data",
]
