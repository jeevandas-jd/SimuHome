from src.simulator.domain.aggregators.base import Aggregator


class IlluminanceAggregator(Aggregator):
    def __init__(
        self,
        agg_id: str,
        current_value: float,
        baseline_value: float,
        interested_device_types: list[str],
        unit: str = "lux",
        tick_interval: float = 0.1,
    ):
        super().__init__(
            agg_id=agg_id,
            agg_type="illuminance",
            current_value=current_value,
            baseline_value=baseline_value,
            interested_device_types=interested_device_types,
            unit=unit,
            tick_interval=tick_interval,
        )

    def _get_device_state_signature(self, device):
        
        try:
            
            if device.device_type == "on_off_light":
                state = (device.get_attribute(1, "OnOff", "OnOff"),)
            else:  
                state = (
                    device.get_attribute(1, "OnOff", "OnOff"),
                    device.get_attribute(1, "LevelControl", "CurrentLevel"),
                )
            return hash(state)
        except Exception as error:
            raise RuntimeError(
                f"Failed to compute illuminance signature for device '{device.device_id}'"
            ) from error

    def _recalculate(self):
        
        total_illuminance = self.baseline_value  

        for device_id, device in self.monitored_devices.items():
            contribution = self._get_device_contribution(device)
            total_illuminance += contribution

        self.current_value = total_illuminance

    def _get_device_contribution(self, device):
        
        is_on = device.get_attribute(1, "OnOff", "OnOff")
        if not is_on:
            return 0.0

        
        if device.device_type == "on_off_light":
            return 500.0

        
        level = device.get_attribute(1, "LevelControl", "CurrentLevel") or 0
        brightness_percent = level / 254.0  
        return brightness_percent * 500

    def _on_time_tick_extra(self):
        
        
        pass

    def _iter_relevant_clusters_for_exact_batch(self, device):
        return (
            device.get_cluster(1, "OnOff"),
            device.get_cluster(1, "LevelControl"),
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

        self.sync_environment_to_devices()
        return True

    def get_illuminance_level(self):
        
        if self.current_value < 50:
            return "dark"
        elif self.current_value < 200:
            return "dim"
        elif self.current_value < 500:
            return "normal"
        elif self.current_value < 1000:
            return "bright"
        else:
            return "very bright"

    def sync_environment_to_devices(self):
        
        
        pass

    def sync_device_sensor_from_env(self, device):
        
        
        pass
