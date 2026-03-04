from src.simulator.domain.devices.base import Device
from src.simulator.domain.clusters.basic_information import BasicInformationCluster
from src.simulator.domain.clusters.onoff import OnOffCluster
from src.simulator.domain.clusters.operational_state import OperationalStateCluster, OperationalStateEnum
from src.simulator.domain.clusters.laundry_washer_mode import LaundryWasherModeCluster
from src.simulator.domain.clusters.laundry_washer_controls import LaundryWasherControlsCluster
from src.simulator.domain.clusters.temperature_control import TemperatureControlCluster
from typing import Any, Dict, cast


class LaundryWasher(Device):
    

    PHASE_DURATION_RATIOS = [
        1 / 8,
        4 / 8,
        2 / 8,
        1 / 8,
    ]

    def __init__(self, device_id: str):
        super().__init__(
            device_id,
            "laundry_washer",
            BasicInformationCluster(
                vendor_name="Samsung Electronics",
                vendor_id=1,
                product_name="Laundry Washer",
                product_id=0x0051,
            ),
        )


        onoff = OnOffCluster(features=OnOffCluster.FEATURE_DF)
        onoff.set_dead_front_callback(self._handle_dead_front_state)
        self.add_cluster(1, onoff)


        operational_state = OperationalStateCluster(
            supported_commands=["Pause", "Resume", "Start", "Stop"]
        )
        operational_state.set_phase_list(
            ["Pre-wash", "Main wash", "Rinse", "Spin", "Complete"]
        )
        self.add_cluster(1, operational_state)


        laundry_mode = LaundryWasherModeCluster()
        self.add_cluster(1, laundry_mode)


        controls = LaundryWasherControlsCluster()
        self.add_cluster(1, controls)


        temperature_control = TemperatureControlCluster()
        self.add_cluster(1, temperature_control)


        self._setup_cluster_coordination()
        self._initial_countdown: int = 0
        self._was_running: bool = False


        original_start = self.operational_state._start

        def wrapped_start():
            if self.onoff.is_in_dead_front_state():
                from src.simulator.domain.result import Result, ErrorCode

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
        self.laundry_mode = cast(
            LaundryWasherModeCluster, self.endpoints[1]["LaundryWasherMode"]
        )
        self.controls = cast(
            LaundryWasherControlsCluster, self.endpoints[1]["LaundryWasherControls"]
        )
        self.temperature_control = cast(
            TemperatureControlCluster, self.endpoints[1]["TemperatureControl"]
        )


        self.laundry_mode.set_mode_change_callback(self._on_mode_changed)


        self.laundry_mode.set_device_reference(self)
        self.controls.set_device_reference(self)

    def _on_mode_changed(self, new_mode: int):
        
        mode_label = self.laundry_mode.get_current_mode_label()
        self.controls.update_spin_speeds_for_mode(mode_label)
        self.controls.update_supported_rinses_for_mode(mode_label)

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


        if "LaundryWasherMode" in self.endpoints[1]:

            pass


        if "LaundryWasherControls" in self.endpoints[1]:
            self.controls.attributes.update(
                {
                    "SpinSpeedCurrent": None,
                    "NumberOfRinses": None,
                    "SpinSpeeds": None,
                    "SupportedRinses": None,
                }
            )


        if "TemperatureControl" in self.endpoints[1]:

            pass

    def _restore_normal_values(self):
        

        if "OperationalState" in self.endpoints[1]:
            self.operational_state.set_phase_list(
                ["Pre-wash", "Main wash", "Rinse", "Spin", "Complete"]
            )


        if "LaundryWasherControls" in self.endpoints[1]:

            self.controls.update_spin_speeds_for_mode(
                self.laundry_mode.get_current_mode_label()
            )
            self.controls.update_supported_rinses_for_mode(
                self.laundry_mode.get_current_mode_label()
            )

    def _initialize_cycle_after_start(self):
        
        phase_list = self.operational_state.attributes.get("PhaseList") or []
        if phase_list:
            self.operational_state.set_current_phase(0)
        mode_durations = {
            "Normal": 3600,
            "Delicate": 2700,
            "Heavy": 5400,
            "Whites": 3600,
            "Quick Normal": 900,
            "Heavy Whites": 5400,
        }
        current_mode = self.laundry_mode.get_current_mode_label()
        duration = mode_durations.get(current_mode, 3600)
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

        current_phase_raw = self.operational_state.attributes.get("CurrentPhase")
        countdown_raw = self.operational_state.attributes.get("CountdownTime")

        if not isinstance(current_phase_raw, int) or isinstance(current_phase_raw, bool):
            return
        if isinstance(countdown_raw, bool) or not isinstance(countdown_raw, (int, float)):
            return
        countdown = float(countdown_raw)

        phase_list_raw = self.operational_state.attributes.get("PhaseList")
        if not isinstance(phase_list_raw, list):
            return
        phase_list = [phase for phase in phase_list_raw if isinstance(phase, str)]
        if not phase_list:
            return
        if not (0 <= current_phase_raw < len(phase_list)):
            return


        total_duration = getattr(self, "_initial_countdown", 3600)


        phase_durations = [
            int(total_duration * ratio) for ratio in self.PHASE_DURATION_RATIOS
        ]

        current_phase_idx = int(current_phase_raw)


        elapsed_time = max(total_duration - countdown, 0)


        phase_boundaries = []
        cumulative_time = 0
        for duration in phase_durations:
            cumulative_time += duration
            phase_boundaries.append(cumulative_time)


        target_phase_idx = 0
        for i, boundary in enumerate(phase_boundaries):
            if elapsed_time <= boundary:
                target_phase_idx = i
                break


        if target_phase_idx > current_phase_idx and target_phase_idx < len(phase_list):

            pass
            self.operational_state.set_current_phase(target_phase_idx)

    def change_mode(self, new_mode: int) -> Dict[str, Any]:
        

        result = self.laundry_mode._change_to_mode(new_mode)

        if result.success:

            mode_label = self.laundry_mode.get_current_mode_label()
            self.controls.update_spin_speeds_for_mode(mode_label)
            self.controls.update_supported_rinses_for_mode(mode_label)

            return {
                "success": True,
                "new_mode": mode_label,
                "updated_controls": True,
            }
        else:
            return {
                "success": False,
                "error": result.error_message,
                "detail": result.error_detail,
            }
