from src.simulator.domain.aggregators.base import Aggregator
from src.simulator.domain.devices.base import Device


class HumidityAggregator(Aggregator):
    def __init__(
        self,
        agg_id: str,
        current_value: float,
        baseline_value: float,
        interested_device_types: list[str],
        unit: str = "%",
        tick_interval: float = 0.1,
    ):
        super().__init__(
            agg_id=agg_id,
            agg_type="humidity",
            current_value=current_value,
            baseline_value=baseline_value,
            interested_device_types=interested_device_types,
            unit=unit,
            tick_interval=tick_interval,
        )

    def _get_humidity_sensor_endpoint(self, device: Device):
        
        if device.device_type == "humidifier":
            return 2  
        elif device.device_type == "dehumidifier":
            return 2  
        else:
            return 1  

    def _get_device_state_signature(self, device: Device):
        
        try:
            humidity_endpoint = self._get_humidity_sensor_endpoint(device)

            if device.device_type == "humidifier":
                state = (
                    device.get_attribute(1, "OnOff", "OnOff"),
                    device.get_attribute(1, "FanControl", "PercentCurrent"),
                    device.get_attribute(
                        humidity_endpoint,
                        "RelativeHumidityMeasurement",
                        "MeasuredValue",
                    ),
                )
            elif device.device_type == "dehumidifier":
                state = (
                    device.get_attribute(1, "OnOff", "OnOff"),
                    device.get_attribute(1, "FanControl", "PercentCurrent"),
                    device.get_attribute(
                        humidity_endpoint,
                        "RelativeHumidityMeasurement",
                        "MeasuredValue",
                    ),
                )
            else:
                
                state = (device.get_attribute(1, "OnOff", "OnOff"),)
            return hash(state)
        except Exception as error:
            raise RuntimeError(
                f"Failed to compute humidity signature for device '{device.device_id}'"
            ) from error

    def _recalculate(self):
        
        for _, device in self.monitored_devices.items():
            self._calculate_device_effect(device)

    def _calculate_device_effect(self, device):
        
        device_id = device.device_id
        humidity_endpoint = self._get_humidity_sensor_endpoint(device)

        is_operating = device.get_attribute(1, "OnOff", "OnOff")
        if not is_operating:
            self.continuous_effects.pop(device_id, None)
            return

        percent_current = device.get_attribute(1, "FanControl", "PercentCurrent")
        if percent_current is None or percent_current == 0:  
            self.continuous_effects.pop(device_id, None)
            return

        fan_intensity = percent_current / 100.0  

        current_humidity = self.current_value

        if device.device_type == "humidifier":
            
            
            if current_humidity < 9000:  
                
                
                efficiency = max(0.1, (9000 - current_humidity) / 9000)
                humidifying_rate_per_second = 5.0 * fan_intensity * efficiency
                
                self.continuous_effects[device_id] = (
                    humidifying_rate_per_second * self.tick_interval
                )
            else:
                self.continuous_effects.pop(device_id, None)

        elif device.device_type == "dehumidifier":
            
            
            if current_humidity > 1000:  
                
                
                efficiency = max(0.1, (current_humidity - 1000) / 9000)
                dehumidifying_rate_per_second = 5.0 * fan_intensity * efficiency
                self.continuous_effects[device_id] = (
                    -dehumidifying_rate_per_second * self.tick_interval
                )
            else:
                self.continuous_effects.pop(device_id, None)
        else:
            self.continuous_effects.pop(device_id, None)

    def _on_time_tick_extra(self):
        

        total_effect = sum(self.continuous_effects.values())
        self.current_value += total_effect

        
        delta = self.baseline_value - self.current_value  
        restoration_rate_per_second = (
            0.01  
        )
        self.current_value += delta * restoration_rate_per_second * self.tick_interval

        
        self.current_value = max(0.0, min(10000.0, self.current_value))

    def _iter_relevant_clusters_for_exact_batch(self, device: Device):
        humidity_endpoint = self._get_humidity_sensor_endpoint(device)
        return (
            device.get_cluster(1, "OnOff"),
            device.get_cluster(1, "FanControl"),
            device.get_cluster(humidity_endpoint, "RelativeHumidityMeasurement"),
        )

    def can_exact_batch_advance(self) -> bool:
        for device in self.monitored_devices.values():
            if self._device_blocks_exact_batch(device):
                return False
        return True

    def exact_batch_advance(self, ticks: int) -> bool:
        steps = int(ticks)
        if steps <= 0:
            return True
        if not self.can_exact_batch_advance():
            return False

        for _ in range(steps):
            self.on_time_tick()
        return True

    def sync_environment_to_devices(self):
        
        for device in self.monitored_devices.values():
            self.sync_device_sensor_from_env(device)

    def sync_device_sensor_from_env(self, device):
        
        humidity_endpoint = self._get_humidity_sensor_endpoint(device)

        humidity_cluster = device.endpoints.get(humidity_endpoint, {}).get(
            "RelativeHumidityMeasurement"
        )
        if humidity_cluster:
            humidity_matter_units = int(self.current_value)

            min_val = humidity_cluster.attributes.get("MinMeasuredValue")
            max_val = humidity_cluster.attributes.get("MaxMeasuredValue")

            if min_val is not None:
                humidity_matter_units = max(humidity_matter_units, min_val)
            if max_val is not None:
                humidity_matter_units = min(humidity_matter_units, max_val)

            humidity_cluster.attributes["MeasuredValue"] = humidity_matter_units
