from src.simulator.domain.aggregators.base import Aggregator


class PM10Aggregator(Aggregator):
    def __init__(
        self,
        agg_id: str,
        current_value: float,
        baseline_value: float,
        interested_device_types: list[str],
        unit: str = "μg/m³",
        tick_interval: float = 0.1,
    ):
        super().__init__(
            agg_id=agg_id,
            agg_type="pm10",
            current_value=current_value,
            baseline_value=baseline_value,
            interested_device_types=interested_device_types,
            unit=unit,
            tick_interval=tick_interval,
        )

        
        self.quality_levels = {
            "good": (0, 30),  
            "normal": (31, 80),  
            "bad": (81, 150),  
            "very_bad": (151, float("inf")),  
        }

    def _get_device_state_signature(self, device):
        
        try:
            state = (
                device.get_attribute(1, "OnOff", "OnOff"),  
                device.get_attribute(1, "FanControl", "PercentCurrent"),  
            )
            return hash(state)
        except Exception as error:
            raise RuntimeError(
                f"Failed to compute pm10 signature for device '{device.device_id}'"
            ) from error

    def _recalculate(self):
        
        for device_id, device in self.monitored_devices.items():
            self._calculate_device_effect(device)

    def _calculate_device_effect(self, device):
        
        device_id = device.device_id

        
        is_on = device.get_attribute(1, "OnOff", "OnOff")
        if is_on is False:
            self.continuous_effects.pop(device_id, None)
            return

        
        fan_percent = device.get_attribute(1, "FanControl", "PercentCurrent") or 0

        
        if fan_percent == 0:
            self.continuous_effects.pop(device_id, None)
            return

        
        purification_rate = self._calculate_purification_rate(fan_percent)
        self.continuous_effects[
            device_id
        ] = -purification_rate  

    def _calculate_purification_rate(self, fan_percent):
        
        base_rate_per_second = 5.0

        
        fan_intensity = (fan_percent / 100.0) ** 0.8

        
        baseline_value = self.baseline_value
        if baseline_value <= 0:
            concentration_ratio = 1.0
        else:
            concentration_ratio = self.current_value / baseline_value
        if concentration_ratio > 2.0:
            pollution_factor = concentration_ratio * 0.8  
        else:
            pollution_factor = min(2.0, concentration_ratio)

        return (
            base_rate_per_second * fan_intensity * pollution_factor * self.tick_interval
        )

    def _on_time_tick_extra(self):
        
        
        total_purification = sum(self.continuous_effects.values())
        self.current_value += total_purification

        
        restoration_delta = self.baseline_value - self.current_value
        restoration_rate_per_second = 0.1
        self.current_value += (
            restoration_delta * restoration_rate_per_second * self.tick_interval
        )

        self.current_value = max(0.0, self.current_value)

    def _iter_relevant_clusters_for_exact_batch(self, device):
        return (
            device.get_cluster(1, "OnOff"),
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

        total_purification = sum(self.continuous_effects.values())
        restoration_rate_per_second = 0.1
        for _ in range(steps):
            self.current_value += total_purification
            restoration_delta = self.baseline_value - self.current_value
            self.current_value += (
                restoration_delta * restoration_rate_per_second * self.tick_interval
            )
            self.current_value = max(0.0, self.current_value)

        self.sync_environment_to_devices()
        return True

    def get_air_quality_level(self):
        
        value = self.current_value

        if value <= self.quality_levels["good"][1]:
            return "good"
        elif value <= self.quality_levels["normal"][1]:
            return "normal"
        elif value <= self.quality_levels["bad"][1]:
            return "bad"
        else:
            return "very bad"

    def get_air_quality_color(self):
        
        quality = self.get_air_quality_level()
        colors = {
            "good": "#3498db",  
            "normal": "#2ecc71",  
            "bad": "#f39c12",  
            "very bad": "#e74c3c",  
        }
        return colors.get(quality, "#95a5a6")

    def get_purifier_efficiency(self):
        
        if not self.continuous_effects:
            return 0.0

        total_purification = abs(sum(self.continuous_effects.values()))
        max_theoretical = len(self.monitored_devices) * 1.0

        if max_theoretical == 0:
            return 0.0

        return min(100.0, (total_purification / max_theoretical) * 100)

    def get_status_summary(self):
        
        active_purifiers = len(
            [
                d
                for d in self.monitored_devices.values()
                if d.get_attribute(1, "FanControl", "PercentCurrent") or 0 > 0
            ]
        )

        return {
            "pm10_level": self.current_value,
            "quality_grade": self.get_air_quality_level(),
            "quality_color": self.get_air_quality_color(),
            "active_purifiers": active_purifiers,
            "total_purifiers": len(self.monitored_devices),
            "purification_efficiency": self.get_purifier_efficiency(),
            "trend": self._get_trend(),
        }

    def _get_trend(self):
        
        total_effect = sum(self.continuous_effects.values())
        restoration = (self.baseline_value - self.current_value) * 0.01
        net_change = total_effect + restoration

        if net_change < -0.1:
            return "improving"
        elif net_change > 0.1:
            return "worsening"
        else:
            return "stable"

    def simulate_external_pollution(self, intensity=1.0):
        
        pollution_increase = intensity * 10.0  
        self.current_value += pollution_increase

        return f"External pollution affected with intensity {intensity}x"

    def sync_environment_to_devices(self):
        
        
        pass

    def sync_device_sensor_from_env(self, device):
        
        
        pass
