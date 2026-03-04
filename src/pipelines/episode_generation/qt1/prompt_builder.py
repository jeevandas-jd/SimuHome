from __future__ import annotations
from typing import Any, Dict, List

from src.pipelines.episode_generation.shared.messages import Message
from src.pipelines.episode_generation.shared.formatting import (
    format_room_name,
    extract_device_number,
    format_device_name,
)
from prompts.qt1.feasible.generation import (
    SYSTEM_PROMPT,
    USER_PROMPT,
    ROOM_SECTION_HEADER,
    DEVICE_ATTRIBUTE_LINE,
    ROOM_STATE_WITH_VALUE_LINE,
    ROOM_STATE_NO_VALUE_LINE,
)


def _format_attribute_name(attribute_id: str) -> str:
    attribute_map = {
        
        "OnOff": "power status",
        "GlobalSceneControl": "scene control status",
        
        "CurrentLevel": "brightness level",
        "RemainingTime": "remaining time",
        "MinLevel": "minimum brightness",
        "MaxLevel": "maximum brightness",
        "CurrentFrequency": "current frequency",
        "MinFrequency": "minimum frequency",
        "MaxFrequency": "maximum frequency",
        
        "LocalTemperature": "current temperature",
        
        "FanModeSequence": "available fan modes",
        "PercentCurrent": "current fan speed",
        
        "MeasuredValue": "measured value",
        "MinMeasuredValue": "minimum value",
        "MaxMeasuredValue": "maximum value",
        "Tolerance": "measurement tolerance",
        
        "TemperatureSetpoint": "temperature setpoint",
        "MinTemperature": "minimum temperature",
        "MaxTemperature": "maximum temperature",
        "Step": "temperature step",
        "SelectedTemperatureLevel": "selected temperature level",
        "SupportedTemperatureLevels": "available temperature levels",
        
        "PowerMode": "power mode",
        "NumberOfMeasurementTypes": "number of measurement types",
        "Accuracy": "measurement accuracy",
        
        "CumulativeEnergyImported": "total energy imported",
        "CumulativeEnergyExported": "total energy exported",
        "PeriodicEnergyImported": "periodic energy imported",
        "PeriodicEnergyExported": "periodic energy exported",
        "CumulativeEnergyReset": "energy reset information",
        
        "OperationalState": "current operational state",
        "CurrentPhase": "current phase",
        "CountdownTime": "remaining countdown time",
        "PhaseList": "available phases",
        "OperationalStateList": "available operational states",
        "OperationalError": "operational error status",
        
        "Type": "covering type",
        "ConfigStatus": "configuration status",
        "OperationalStatus": "operational status",
        "EndProductType": "product type",
        "SafetyStatus": "safety status",
        
        "SupportedModes": "available modes",
        "CurrentMode": "current mode",
        
        "CurrentState": "playback state",
        
        "ChannelList": "available channels",
        "Lineup": "channel lineup information",
        
        "IdentifyType": "identification type",
        "FeatureMap": "feature map",
        "ClusterRevision": "cluster revision",
        
        "Order": "power source order",
        "Status": "power source status",
        "Description": "power source description",
        
        "ESAType": "energy smart appliance type",
        "ESACanGenerate": "can generate energy",
        "AbsMinPower": "absolute minimum power",
        "AbsMaxPower": "absolute maximum power",
        
        "SpinSpeeds": "available spin speeds",
        "SupportedRinses": "supported rinse options",
        "SupportedDrynessLevels": "available dryness levels",
        
        "AvailableEndpoints": "available endpoints",
        
        "VendorName": "vendor name",
        "VendorID": "vendor ID",
        "ProductName": "product name",
        "ProductID": "product ID",
    }
    return attribute_map.get(attribute_id, attribute_id.lower().replace("_", " "))


def _format_room_state(state_key: str) -> str:
    
    state_map = {
        "temperature": "temperature",
        "humidity": "humidity",
        "illuminance": "lighting",
        "pm10": "air quality",
    }
    return state_map.get(state_key, state_key)


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


def build_qt1_messages(payload: Dict[str, Any]) -> List[Message]:
    user_location = format_room_name(payload.get("user_location", ""))
    current_time = payload.get("initial_home_config", {}).get("base_time", "")
    goals = payload.get("eval", {}).get("goals", [])

    targets = ""
    room_groups = _group_goals_by_room(goals)
    for room_id, room_goals in room_groups.items():
        room_name = format_room_name(room_id)
        targets += ROOM_SECTION_HEADER.format(room_name=room_name)

        for goal in room_goals:
            variant = goal.get("variant", "")

            if variant == "device_attribute":
                device_id = goal.get("device_id", "")
                device_type = goal.get("device_type", "")
                attribute = goal.get("attribute", "")

                device_number = extract_device_number(device_id)
                device_name = format_device_name(device_type, device_number)
                attribute_name = _format_attribute_name(attribute.split(".")[-1])
                attribute_id = attribute.split(".")[-1]
                cluster_name = attribute.split(".")[-2]

                targets += DEVICE_ATTRIBUTE_LINE.format(
                    device_name=device_name,
                    attribute_name=attribute_name,
                    attribute_id=attribute_id,
                    cluster_name=cluster_name,
                )

            elif variant == "room_state":
                room_state = goal.get("room_state", "")
                current_value = goal.get("current_value")
                unit = goal.get("unit", "")

                state_name = _format_room_state(room_state)

                if current_value is not None:
                    targets += ROOM_STATE_WITH_VALUE_LINE.format(   
                        state_name=state_name,
                        current_value=current_value,
                        unit=unit,
                    )
                else:
                    targets += ROOM_STATE_NO_VALUE_LINE.format(
                        state_name=state_name
                    )


    user_prompt = USER_PROMPT.format(
        user_location=user_location,
        current_time=current_time,
        targets=targets,
    )
    return [
        Message(role="system", content=SYSTEM_PROMPT),
        Message(role="user", content=user_prompt),
    ]


__all__ = [
    "build_qt1_messages",
    "Message",
    "_format_attribute_name",
    "_format_room_state",
    "_group_goals_by_room",
]
