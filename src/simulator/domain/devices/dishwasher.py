from src.simulator.domain.devices.base import Device
from src.simulator.domain.clusters.basic_information import BasicInformationCluster
from src.simulator.domain.clusters.onoff import OnOffCluster
from src.simulator.domain.clusters.operational_state import OperationalStateCluster, OperationalStateEnum
from src.simulator.domain.clusters.dishwasher_mode import DishwasherModeCluster
from src.simulator.domain.clusters.dishwasher_alarm import DishwasherAlarmCluster
import math
from typing import cast


class Dishwasher(Device):
    

    PHASE_DURATION_RATIOS = [
        1 / 9,
        5 / 9,
        2 / 9,
        1 / 9,
    ]

    MODE_CYCLE_DURATIONS = {
        "Normal": 5400,
        "Heavy Duty": 7200,
        "Light Wash": 3600,
        "Quick Wash": 1800,
        "Low Energy": 5400,
        "Silent": 5400,
    }

    def __init__(self, device_id: str):
        super().__init__(
            device_id,
            "dishwasher",
            BasicInformationCluster(
                vendor_name="LG Electronics",
                vendor_id=1,
                product_name="Dishwasher",
                product_id=0x0075,
            ),
        )
        onoff = OnOffCluster(features=OnOffCluster.FEATURE_DF)
        onoff.set_dead_front_callback(self._handle_dead_front_state)
        self.add_cluster(1, onoff)
        self._initial_countdown = 0
        self._was_running = False

        operational_state = OperationalStateCluster(
            supported_commands=["Pause", "Resume", "Start", "Stop"]
        )
        operational_state.set_phase_list(
            ["Pre-wash", "Main wash", "Rinse", "Dry", "Complete"]
        )
        self.add_cluster(1, operational_state)

        dishwasher_mode = DishwasherModeCluster()
        self.add_cluster(1, dishwasher_mode)

        dishwasher_alarm = DishwasherAlarmCluster()
        self.add_cluster(1, dishwasher_alarm)

        self._setup_cluster_coordination()

        original_start = self.operational_state._start  # type: ignore[attr-defined]

        def wrapped_start():
            from src.simulator.domain.result import Result, ErrorCode

            if self.onoff.is_in_dead_front_state():
                return Result.fail(
                    ErrorCode.COMMAND_EXECUTION_ERROR,
                    "Cannot start cycle in dead front state",
                    "Device must be powered on (OnOff = True) to start cycle",
                )
            result = original_start()
            if result.success:
                self._initialize_cycle_after_start()
            return result

        self.operational_state._start = wrapped_start  # type: ignore[attr-defined]
        if "Start" in self.operational_state.commands:
            self.operational_state.commands["Start"] = wrapped_start

    def _setup_cluster_coordination(self):
        self.operational_state = cast(
            OperationalStateCluster, self.endpoints[1]["OperationalState"]
        )
        self.onoff = cast(OnOffCluster, self.endpoints[1]["OnOff"])
        self.dishwasher_mode = cast(
            DishwasherModeCluster, self.endpoints[1]["DishwasherMode"]
        )
        self.dishwasher_alarm = cast(
            DishwasherAlarmCluster, self.endpoints[1]["DishwasherAlarm"]
        )

        self.dishwasher_mode.set_device_reference(self)

    def _handle_dead_front_state(self, is_dead_front: bool):
        if is_dead_front:
            self._set_dead_front_values()
        else:
            self._restore_normal_values()

    def _set_dead_front_values(self):
        if "OperationalState" in self.endpoints[1]:
            self.operational_state.attributes.update(
                {
                    "PhaseList": None,
                    "CurrentPhase": None,
                    "CountdownTime": None,
                    "OperationalState": OperationalStateEnum.STOPPED,
                    "OperationalError": {
                        "error_state_id": 0,
                    },
                }
            )

    def _restore_normal_values(self):
        if "OperationalState" in self.endpoints[1]:
            self.operational_state.set_phase_list(
                ["Pre-wash", "Main wash", "Rinse", "Dry", "Complete"]
            )

    def _initialize_cycle_after_start(self):
        phase_list = self.operational_state.attributes.get("PhaseList") or []
        if phase_list:
            self.operational_state.set_current_phase(0)
        current_mode_label = self.dishwasher_mode.get_current_mode_label()
        duration = self.MODE_CYCLE_DURATIONS.get(current_mode_label, 5400)
        self.operational_state.set_countdown_time(duration)
        self._initial_countdown = duration
        self._was_running = True

    def on_time_tick(self):
        self.operational_state.on_time_tick(tick_interval=self.tick_interval)

        self._update_cycle_progress()
        self._handle_cycle_completion()

    def _handle_cycle_completion(self):
        current_state = self.operational_state.attributes.get("OperationalState")
        countdown = self.operational_state.attributes.get("CountdownTime")

        if current_state == OperationalStateEnum.STOPPED and countdown is None and self._was_running:
            self._was_running = False

    def _update_cycle_progress(self):
        current_state = self.operational_state.attributes.get("OperationalState")
        if current_state != OperationalStateEnum.RUNNING:
            return

        phase_list_raw = self.operational_state.attributes.get("PhaseList")
        if not isinstance(phase_list_raw, list):
            return
        phase_list = [phase for phase in phase_list_raw if isinstance(phase, str)]
        if not phase_list:
            return

        current_phase_raw = self.operational_state.attributes.get("CurrentPhase")
        countdown_raw = self.operational_state.attributes.get("CountdownTime")

        if isinstance(countdown_raw, bool) or not isinstance(countdown_raw, (int, float)):
            return
        countdown_seconds = float(countdown_raw)
        if not math.isfinite(countdown_seconds):
            return
        remaining_seconds = int(max(0, math.ceil(countdown_seconds)))
        if remaining_seconds <= 0:
            return

        if isinstance(current_phase_raw, bool):
            return
        if isinstance(current_phase_raw, int):
            if not (0 <= current_phase_raw < len(phase_list)):
                return
            current_phase_idx = int(current_phase_raw)
        elif isinstance(current_phase_raw, str):
            try:
                current_phase_idx = phase_list.index(current_phase_raw)
            except ValueError:
                return
        else:
            return

        baseline_raw = getattr(self, "_initial_countdown", None)
        if isinstance(baseline_raw, bool) or not isinstance(baseline_raw, int) or baseline_raw <= 0:
            self._initial_countdown = remaining_seconds
            total_duration = remaining_seconds
        else:
            total_duration = baseline_raw
            if remaining_seconds > total_duration:
                self._initial_countdown = remaining_seconds
                total_duration = remaining_seconds

        if total_duration <= 0:
            return

        elapsed_time = max(0, total_duration - remaining_seconds)
        progress = min(1.0, max(0.0, float(elapsed_time) / float(total_duration)))

        phase_count = min(len(phase_list), len(self.PHASE_DURATION_RATIOS))
        if phase_count <= 0:
            return

        target_phase_idx = phase_count - 1
        cumulative_ratio = 0.0
        for i in range(phase_count):
            cumulative_ratio += float(self.PHASE_DURATION_RATIOS[i])
            if progress <= cumulative_ratio:
                target_phase_idx = i
                break

        if target_phase_idx > current_phase_idx and target_phase_idx < len(phase_list):
            self.operational_state.set_current_phase(target_phase_idx)
