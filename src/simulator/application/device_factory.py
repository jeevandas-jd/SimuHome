from typing import Callable, Dict, List
from src.simulator.domain.devices.base import Device
from src.simulator.domain.devices.dehumidifier import Dehumidifier
from src.simulator.domain.devices.fan import Fan
from src.simulator.domain.devices.heat_pump import HeatPump
from src.simulator.domain.devices.humidifier import Humidifier
from src.simulator.domain.devices.laundry_washer import LaundryWasher
from src.simulator.domain.devices.laundry_dryer import LaundryDryer
from src.simulator.domain.devices.on_off_light import OnOffLight
from src.simulator.domain.devices.dimmable_light import DimmableLight
from src.simulator.domain.devices.air_conditioner import AirConditioner
from src.simulator.domain.devices.air_purifier import AirPurifier
from src.simulator.domain.devices.rvc import RVC
from src.simulator.domain.devices.tv import TV
from src.simulator.domain.devices.window_covering_controller import (
    WindowCoveringController,
)
from src.simulator.domain.devices.dishwasher import Dishwasher
from src.simulator.domain.devices.freezer import Freezer
from src.simulator.domain.devices.refrigerator import Refrigerator
from src.simulator.domain.devices.electrical_sensor import ElectricalSensor

DEVICE_FACTORY: Dict[str, Callable[..., Device]] = {
    "on_off_light": OnOffLight,
    "dimmable_light": DimmableLight,
    "air_conditioner": AirConditioner,
    "air_purifier": AirPurifier,
    "tv": TV,
    "heat_pump": HeatPump,
    "electrical_sensor": ElectricalSensor,
    "humidifier": Humidifier,
    "dehumidifier": Dehumidifier,
    "window_covering_controller": WindowCoveringController,
    "dishwasher": Dishwasher,
    "laundry_washer": LaundryWasher,
    "laundry_dryer": LaundryDryer,
    "fan": Fan,
    "rvc": RVC,
    "freezer": Freezer,
    "refrigerator": Refrigerator,
}


def get_supported_device_types() -> List[str]:
    
    return list(DEVICE_FACTORY.keys())


def is_valid_device_type(device_type: str) -> bool:
    
    return device_type in DEVICE_FACTORY


def create_device(device_type: str, device_id: str) -> Device:
    
    if not is_valid_device_type(device_type):
        supported_types = get_supported_device_types()
        raise ValueError(
            f"Unsupported device_type: {device_type}. Supported: {supported_types}"
        )

    device_cls = DEVICE_FACTORY[device_type]
    return device_cls(device_id)
