from __future__ import annotations

from typing import Any, Dict, Optional, Tuple


READONLY_ATTRIBUTES_BY_CLUSTER: Dict[str, Tuple[str, ...]] = {
    "OnOff": ("OnOff", "GlobalSceneControl"),
    "FanControl": ("PercentCurrent", "FanModeSequence"),
    "LevelControl": (
        "CurrentLevel",
        "RemainingTime",
        "MinLevel",
        "MaxLevel",
        "CurrentFrequency",
        "MinFrequency",
        "MaxFrequency",
    ),
    "Thermostat": ("LocalTemperature",),
    "RelativeHumidityMeasurement": (
        "MeasuredValue",
        "MinMeasuredValue",
        "MaxMeasuredValue",
        "Tolerance",
    ),
    "Channel": ("ChannelList", "Lineup"),
    "DeviceEnergyManagement": (
        "ESAType",
        "ESACanGenerate",
        "AbsMinPower",
        "AbsMaxPower",
    ),
    "RVCRunMode": ("SupportedModes", "CurrentMode"),
    "RVCCleanMode": ("SupportedModes", "CurrentMode"),
    "RVCOperationalState": (
        "OperationalState",
        "CurrentPhase",
        "CountdownTime",
        "OperationalError",
    ),
    "LaundryDryerControls": ("SupportedDrynessLevels",),
    "LaundryWasherControls": ("SpinSpeeds", "SupportedRinses"),
    "LaundryWasherMode": ("SupportedModes",),
    "DishwasherMode": ("SupportedModes",),
    "DishwasherAlarm": ("State", "Latch", "Supported"),
    "OperationalState": (
        "OperationalState",
        "CurrentPhase",
        "CountdownTime",
        "OperationalError",
    ),
    "RTCCMode": ("SupportedModes", "CurrentMode"),
    "TemperatureMeasurement": (
        "MeasuredValue",
        "MinMeasuredValue",
        "MaxMeasuredValue",
        "Tolerance",
    ),
    "TemperatureControl": ("MinTemperature", "MaxTemperature"),
    "Identify": ("IdentifyType", "FeatureMap", "ClusterRevision"),
}


VALUE_RANGES: Dict[Tuple[Optional[str], str, str], Tuple[int, int, int]] = {
    (None, "Thermostat", "OccupiedHeatingSetpoint"): (700, 3000, 50),
    (None, "Thermostat", "OccupiedCoolingSetpoint"): (1600, 3200, 50),
    ("refrigerator", "TemperatureMeasurement", "MeasuredValue"): (100, 700, 50),
    ("freezer", "TemperatureMeasurement", "MeasuredValue"): (-2300, -1500, 50),
}


VALUE_BINS: Dict[Tuple[Optional[str], str, str], Tuple[Tuple[int, int], ...]] = {
    (None, "FanControl", "PercentSetting"): ((0, 0), (1, 33), (34, 66), (67, 100)),
}


ENUM_VALUES: Dict[Tuple[Optional[str], str, str], Tuple[int, ...]] = {
    (None, "Thermostat", "SystemMode"): (0, 1, 3, 4),  
}


def is_readonly(cluster_id: str, attribute_id: str) -> bool:
    ro_attrs = READONLY_ATTRIBUTES_BY_CLUSTER.get(cluster_id, ())
    return attribute_id in ro_attrs


def get_value_bins(
    device_type: str, cluster_id: str, attribute_id: str
) -> Tuple[Tuple[int, int], ...]:

    key_device = (device_type, cluster_id, attribute_id)
    key_generic = (None, cluster_id, attribute_id)
    return VALUE_BINS.get(key_device) or VALUE_BINS.get(key_generic) or tuple()


def get_value_range(
    device_type: str, cluster_id: str, attribute_id: str
) -> Optional[Tuple[int, int, int]]:
    key_device = (device_type, cluster_id, attribute_id)
    key_generic = (None, cluster_id, attribute_id)
    return VALUE_RANGES.get(key_device) or VALUE_RANGES.get(key_generic)


def get_enum_values(
    device_type: str, cluster_id: str, attribute_id: str
) -> Tuple[int, ...]:
    key_device = (device_type, cluster_id, attribute_id)
    key_generic = (None, cluster_id, attribute_id)
    return ENUM_VALUES.get(key_device) or ENUM_VALUES.get(key_generic) or tuple()


def validate_relations(
    *,
    device_type: str,
    current: Dict[str, Any],
    proposed_changes: Dict[Tuple[int, str, str], Any],
) -> bool:
    
    if device_type == "heat_pump":

        def _find_value(attr: str) -> Optional[int]:

            for (ep, cl, at), v in proposed_changes.items():
                if cl == "DeviceEnergyManagement" and at == attr:
                    return int(v)

            target_suffix = f".DeviceEnergyManagement.{attr}"
            for k, v in current.items():
                if isinstance(k, str) and k.endswith(target_suffix):
                    try:
                        return int(v)
                    except Exception:
                        return None
            return None

        abs_min = _find_value("AbsMinPower")
        abs_max = _find_value("AbsMaxPower")
        if abs_min is not None and abs_max is not None:
            if not (abs_max > abs_min):
                return False
    return True


__all__ = [
    "is_readonly",
    "get_value_bins",
    "get_value_range",
    "get_enum_values",
    "validate_relations",
    "READONLY_ATTRIBUTES_BY_CLUSTER",
    "VALUE_RANGES",
    "VALUE_BINS",
    "ENUM_VALUES",
]
