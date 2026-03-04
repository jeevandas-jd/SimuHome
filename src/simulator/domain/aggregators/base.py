from collections.abc import Iterable


class Aggregator:
    def __init__(
        self,
        agg_id: str,
        agg_type: str,
        current_value: float,
        baseline_value: float,
        unit: str,
        interested_device_types: list[str],
        tick_interval: float = 0.1,
    ):
        self.agg_id = agg_id
        self.agg_type = agg_type
        self.current_value = current_value
        self.baseline_value = baseline_value
        self.unit = unit
        self.interested_device_types = interested_device_types
        self.tick_interval = tick_interval
        self.monitored_devices = {}  
        self.continuous_effects = {}  
        
        self._last_device_states = {}  
        
        self._first_sync_done = False

    def on_time_tick(self):
        
        
        if not self._first_sync_done:
            self.sync_environment_to_devices()
            self._first_sync_done = True

        
        changed_devices = self._poll_interested_devices_only()

        
        if changed_devices:
            self._recalculate()

        
        self._on_time_tick_extra()

        
        self.sync_environment_to_devices()

    def _poll_interested_devices_only(self):
        
        changed_devices = []

        for device_id, device in self.monitored_devices.items():
            if device.device_type not in self.interested_device_types:
                continue

            current_state = self._get_device_state_signature(device)
            previous_state = self._last_device_states.get(device_id)

            
            if current_state != previous_state:
                changed_devices.append(device_id)
                self._last_device_states[device_id] = current_state

        return changed_devices

    def _get_device_state_signature(self, device) -> int | None:
        
        try:
            
            all_attributes = device.get_all_attributes()
            state_tuple = tuple(sorted(all_attributes.items()))
            return hash(state_tuple)
        except Exception as error:
            raise RuntimeError(
                f"Failed to compute state signature for device '{getattr(device, 'device_id', 'unknown')}' in aggregator '{self.agg_id}'"
            ) from error

    def _recalculate(self):
        
        pass

    def _on_time_tick_extra(self):
        
        pass

    def get_current_value(self):
        
        return self.current_value

    def sync_environment_to_devices(self):
        
        pass

    def sync_device_sensor_from_env(self, device):
        
        pass

    def can_exact_batch_advance(self) -> bool:
        return False

    def _iter_relevant_clusters_for_exact_batch(self, device) -> Iterable[object]:
        return ()

    @staticmethod
    def _cluster_blocks_exact_batch(cluster: object) -> bool:
        tick_handler = getattr(cluster, "on_time_tick", None)
        if not callable(tick_handler):
            return False

        block_predicate = getattr(cluster, "blocks_exact_batch_advance", None)
        if callable(block_predicate):
            try:
                return bool(block_predicate())
            except Exception:
                return True

        return True

    def _device_blocks_exact_batch(self, device) -> bool:
        for cluster in self._iter_relevant_clusters_for_exact_batch(device):
            if cluster is None:
                continue
            if self._cluster_blocks_exact_batch(cluster):
                return True
        return False

    def exact_batch_advance(self, ticks: int) -> bool:
        return False

    def reset_sync_state(self):
        
        self._first_sync_done = False
        self._last_device_states.clear()
