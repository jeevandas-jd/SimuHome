from src.simulator.domain.aggregators.base import Aggregator
from src.simulator.domain.devices.base import Device


class TemperatureAggregator(Aggregator):
    def __init__(
        self,
        agg_id: str,
        current_value: float,
        baseline_value: float,
        interested_device_types: list[str],
        unit: str = "°C",
        tick_interval: float = 0.1,
    ):
        super().__init__(
            agg_id=agg_id,
            agg_type="temperature",
            current_value=current_value,
            baseline_value=baseline_value,
            interested_device_types=interested_device_types,
            unit=unit,
            tick_interval=tick_interval,
        )

    def _get_thermostat_endpoint(self, device: Device):
        
        if device.device_type == "heat_pump":
            return 4  
        elif device.device_type == "air_conditioner":
            return 1  
        elif device.device_type == "fan":
            return None  
        else:
            return 1  

    def _get_device_state_signature(self, device: Device):
        
        try:
            thermostat_endpoint = self._get_thermostat_endpoint(device)

            if device.device_type == "heat_pump":
                if thermostat_endpoint is None:
                    return None
                
                state = (
                    device.get_attribute(
                        thermostat_endpoint, "Thermostat", "SystemMode"
                    ),
                    device.get_attribute(
                        thermostat_endpoint, "Thermostat", "OccupiedCoolingSetpoint"
                    ),
                    device.get_attribute(
                        thermostat_endpoint, "Thermostat", "OccupiedHeatingSetpoint"
                    ),
                    device.get_attribute(
                        2, "ElectricalPowerMeasurement", "ActivePower"
                    ),
                    
                )
            elif device.device_type == "fan":
                
                state = (
                    device.get_attribute(1, "OnOff", "OnOff"),
                    device.get_attribute(1, "FanControl", "PercentCurrent"),
                )
            else:
                if thermostat_endpoint is None:
                    return None
                
                state = (
                    device.get_attribute(1, "OnOff", "OnOff"),
                    device.get_attribute(
                        thermostat_endpoint, "Thermostat", "SystemMode"
                    ),
                    device.get_attribute(
                        thermostat_endpoint, "Thermostat", "OccupiedCoolingSetpoint"
                    ),
                    device.get_attribute(
                        thermostat_endpoint, "Thermostat", "OccupiedHeatingSetpoint"
                    ),
                    device.get_attribute(1, "FanControl", "PercentCurrent"),
                )
            return hash(state)
        except Exception as error:
            raise RuntimeError(
                f"Failed to compute temperature signature for device '{device.device_id}'"
            ) from error

    def _recalculate(self):
        
        for _, device in self.monitored_devices.items():
            self._calculate_device_effect(device)

    def _calculate_device_effect(self, device):
        
        device_id = device.device_id
        thermostat_endpoint = self._get_thermostat_endpoint(device)

        
        is_operating = False
        fan_intensity = 1.0  

        if device.device_type == "heat_pump":
            if thermostat_endpoint is None:
                self.continuous_effects.pop(device_id, None)
                return
            
            system_mode = device.get_attribute(
                thermostat_endpoint, "Thermostat", "SystemMode"
            )
            is_operating = system_mode == 0x04  
            
            if is_operating:
                
                fan_intensity = 1.0  
        elif device.device_type == "fan":
            
            is_operating = device.get_attribute(1, "OnOff", "OnOff")
            if is_operating:
                fan_percent_value = device.get_attribute(
                    1, "FanControl", "PercentCurrent"
                )
                fan_percent = (
                    50
                    if fan_percent_value is None
                    else max(0, min(100, fan_percent_value))
                )
                fan_intensity = fan_percent / 100.0
        else:
            
            is_operating = device.get_attribute(1, "OnOff", "OnOff")
            if is_operating:
                fan_percent_value = device.get_attribute(
                    1, "FanControl", "PercentCurrent"
                )
                fan_percent = (
                    50
                    if fan_percent_value is None
                    else max(0, min(100, fan_percent_value))
                )
                fan_intensity = fan_percent / 100.0

        if not is_operating:
            self.continuous_effects.pop(device_id, None)
            return

        
        if device.device_type == "fan":
            target_floor = self.baseline_value - 200  
            if self.current_value > target_floor:
                temp_diff_c = (self.current_value - target_floor) / 100.0
                
                cooling_rate_per_second_c = (
                    min(0.0002, temp_diff_c * 0.5) * fan_intensity
                )
                self.continuous_effects[device_id] = (
                    -(cooling_rate_per_second_c * 100.0)
                ) * self.tick_interval
            else:
                self.continuous_effects.pop(device_id, None)
            return

        
        if thermostat_endpoint is None:
            self.continuous_effects.pop(device_id, None)
            return
        system_mode = device.get_attribute(
            thermostat_endpoint, "Thermostat", "SystemMode"
        )
        cooling_setpoint = device.get_attribute(
            thermostat_endpoint, "Thermostat", "OccupiedCoolingSetpoint"
        )
        heating_setpoint = device.get_attribute(
            thermostat_endpoint, "Thermostat", "OccupiedHeatingSetpoint"
        )

        if system_mode == 0x03:  
            if self.current_value > cooling_setpoint:
                temp_diff = (
                    self.current_value - cooling_setpoint
                ) / 100.0  
                cooling_rate_per_second_c = min(0.0005, temp_diff * 1.0) * fan_intensity
                self.continuous_effects[device_id] = (
                    -(cooling_rate_per_second_c * 100.0) * self.tick_interval
                )
            else:
                self.continuous_effects.pop(device_id, None)

        elif system_mode == 0x04:  
            if self.current_value < heating_setpoint:
                temp_diff = (heating_setpoint - self.current_value) / 100.0
                heating_rate_per_second_c = min(0.0005, temp_diff * 1.0) * fan_intensity
                self.continuous_effects[device_id] = (
                    heating_rate_per_second_c * 100.0
                ) * self.tick_interval
            else:
                self.continuous_effects.pop(device_id, None)
        else:
            self.continuous_effects.pop(device_id, None)

    def _on_time_tick_extra(self):
        

        total_effect = sum(self.continuous_effects.values())
        self.current_value += total_effect

        
        delta = self.baseline_value - self.current_value  
        restoration_rate_per_second = 0.0002  
        
        self.current_value += delta * restoration_rate_per_second * self.tick_interval

    def _iter_relevant_clusters_for_exact_batch(self, device: Device):
        if device.device_type == "heat_pump":
            return (
                device.get_cluster(4, "Thermostat"),
                device.get_cluster(2, "ElectricalPowerMeasurement"),
            )
        if device.device_type == "fan":
            return (
                device.get_cluster(1, "OnOff"),
                device.get_cluster(1, "FanControl"),
            )

        thermostat_endpoint = self._get_thermostat_endpoint(device)
        thermostat_cluster = None
        if thermostat_endpoint is not None:
            thermostat_cluster = device.get_cluster(thermostat_endpoint, "Thermostat")
        return (
            device.get_cluster(1, "OnOff"),
            thermostat_cluster,
            device.get_cluster(1, "FanControl"),
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

        if not self._first_sync_done:
            self.sync_environment_to_devices()
            self._first_sync_done = True

        changed_devices = self._poll_interested_devices_only()
        if changed_devices:
            self._recalculate()

        total_effect = sum(self.continuous_effects.values())
        restoration_rate_per_second = 0.0002
        for _ in range(steps):
            self.current_value += total_effect
            delta = self.baseline_value - self.current_value
            self.current_value += (
                delta * restoration_rate_per_second * self.tick_interval
            )

        self.sync_environment_to_devices()
        return True

    def sync_environment_to_devices(self):
        
        for device in self.monitored_devices.values():
            self.sync_device_sensor_from_env(device)

    def sync_device_sensor_from_env(self, device):
        
        thermostat_endpoint = self._get_thermostat_endpoint(device)
        if thermostat_endpoint is None:
            return
        thermostat = device.endpoints[thermostat_endpoint].get("Thermostat")
        if thermostat:
            thermostat.attributes["LocalTemperature"] = int(self.current_value)
