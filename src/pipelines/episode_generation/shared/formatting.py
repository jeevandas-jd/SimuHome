from __future__ import annotations


def extract_device_number(device_id: str) -> str:
    
    try:
        return device_id.rsplit("_", 1)[-1]
    except Exception:
        return "1"


def format_device_name(device_type: str, device_number: str) -> str:
    
    device_map = {
        "laundry_washer": "washer",
        "laundry_dryer": "dryer",
        "dishwasher": "dishwasher",
        "rvc": "robot vacuum",
        "air_conditioner": "AC",
        "on_off_light": "light",
        "dimmable_light": "dimmer light",
        "window_covering_controller": "blinds",
        "heat_pump": "heat pump",
        "air_purifier": "air purifier",
        "dehumidifier": "dehumidifier",
        "humidifier": "humidifier",
        "tv": "TV",
        "fan": "fan",
        "refrigerator": "refrigerator",
        "freezer": "freezer",
        "electrical_sensor": "power meter",
    }
    natural_name = device_map.get(device_type, device_type.replace("_", " "))
    return f"{natural_name} {device_number}"


def format_room_name(room_id: str) -> str:
    
    return room_id.replace("_", " ")


def get_anchor_finish_phrase(device_type: str) -> str:
    
    phrases = {
        "laundry_washer": "finishes washing",
        "laundry_dryer": "finishes drying",
        "dishwasher": "finishes cleaning",
        "rvc": "finishes cleaning",
    }
    return phrases.get(device_type, "finishes its cycle")


__all__ = [
    "extract_device_number",
    "format_device_name",
    "format_room_name",
    "get_anchor_finish_phrase",
]
