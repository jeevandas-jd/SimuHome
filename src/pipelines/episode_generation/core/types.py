from __future__ import annotations

from typing import Any, Dict, List, TypedDict


class DeviceInRoom(TypedDict):
    device_id: str
    device_type: str
    attributes: Dict[str, Any]


class RoomConfigDict(TypedDict, total=False):
    state: Dict[str, float]
    devices: List[DeviceInRoom]


class SimulationConfigDict(TypedDict, total=False):
    tick_interval: float
    base_time: str
    rooms: Dict[str, RoomConfigDict]
    state_bounds: "RoomStateBounds"


class IntegerRangeDict(TypedDict):
    min: int
    max: int


class NumericRangeDict(TypedDict):
    min: float
    max: float


class HomeEnvironmentSpec(TypedDict):
    temperature_c: NumericRangeDict
    humidity_pct: NumericRangeDict
    illuminance_lux: NumericRangeDict
    pm10_ugm3: NumericRangeDict


class RoomStateBounds(TypedDict):
    temperature: NumericRangeDict
    humidity: NumericRangeDict
    illuminance: NumericRangeDict
    pm10: NumericRangeDict


class HomeGenerationSpec(TypedDict):
    room_count: int
    devices_per_room: IntegerRangeDict
    environment: HomeEnvironmentSpec


__all__ = [
    "DeviceInRoom",
    "RoomConfigDict",
    "SimulationConfigDict",
    "IntegerRangeDict",
    "NumericRangeDict",
    "HomeEnvironmentSpec",
    "RoomStateBounds",
    "HomeGenerationSpec",
]
