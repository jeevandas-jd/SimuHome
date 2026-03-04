
from typing import Dict, Any, Tuple, Callable
from src.simulator.domain.aggregators.base import Aggregator
from src.simulator.domain.aggregators.temperature import TemperatureAggregator
from src.simulator.domain.aggregators.pm10 import PM10Aggregator
from src.simulator.domain.aggregators.illuminance import IlluminanceAggregator
from src.simulator.domain.aggregators.humidity import HumidityAggregator

AggConfig = Tuple[Callable[..., Aggregator], Dict[str, Any]]
AGGREGATOR_REGISTRY: Dict[str, AggConfig] = {
    "temperature": (
        TemperatureAggregator,
        {
            "current_value": 2500,
            "baseline_value": 2500,
            "unit": "°C",
            "interested_device_types": ["air_conditioner", "heat_pump", "fan"],
        },
    ),
    "pm10": (
        PM10Aggregator,
        {
            "current_value": 35.0,
            "baseline_value": 35.0,
            "unit": "μg/m³",
            "interested_device_types": ["air_purifier"],
        },
    ),
    "illuminance": (
        IlluminanceAggregator,
        {
            "current_value": 1000,
            "baseline_value": 1000,
            "unit": "lux",
            "interested_device_types": ["on_off_light", "dimmable_light"],
        },
    ),
    "humidity": (
        HumidityAggregator,
        {
            "current_value": 5000,
            "baseline_value": 5000,
            "unit": "%",
            "interested_device_types": ["humidifier", "dehumidifier"],
        },
    ),
}
