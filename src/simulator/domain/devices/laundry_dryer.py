from typing import Optional, cast

from src.simulator.domain.devices.base import Device
from src.simulator.domain.clusters.basic_information import BasicInformationCluster
from src.simulator.domain.clusters.onoff import OnOffCluster
from src.simulator.domain.clusters.operational_state import OperationalStateCluster, OperationalStateEnum
from src.simulator.domain.clusters.laundry_dryer_controls import (
    LaundryDryerControlsCluster,
    DrynessLevelEnum,
)
from src.simulator.domain.result import Result, ErrorCode


class LaundryDryer(Device):
    

    PHASE_DURATION_RATIOS: list[float] = [2 / 10, 6 / 10, 2 / 10]


    DRYNESS_DURATIONS_MIN: dict[int, int] = {
        DrynessLevelEnum.LOW: 30,
        DrynessLevelEnum.NORMAL: 45,
        DrynessLevelEnum.EXTRA: 60,
        DrynessLevelEnum.MAX: 75,
    }

    def __init__(self, device_id: str):
        super().__init__(
            device_id,
            "laundry_dryer",
            BasicInformationCluster(
                vendor_name="Generic Vendor",
                vendor_id=1,
                product_name="Laundry Dryer",
                product_id=0x0080,
            ),
        )


        onoff = OnOffCluster(features=OnOffCluster.FEATURE_DF)
        onoff.set_dead_front_callback(self._handle_dead_front_state)
        self.add_cluster(1, onoff)


        operational_state = OperationalStateCluster(
            supported_commands=["Pause", "Resume", "Start", "Stop"]
        )
        operational_state.set_phase_list(["Heating", "Drying", "CoolDown", "Complete"])
        self.add_cluster(1, operational_state)

        controls = LaundryDryerControlsCluster()
        self.add_cluster(1, controls)


        self.operational_state = cast(
            OperationalStateCluster, self.endpoints[1]["OperationalState"]
        )
        self.onoff = cast(OnOffCluster, self.endpoints[1]["OnOff"])
        self.controls = cast(
            LaundryDryerControlsCluster, self.endpoints[1]["LaundryDryerControls"]
        )
        self._initial_countdown: int = 0
        self._was_running: bool = False

        self.controls.set_device_reference(self)


        original_start = self.operational_state._start

        def wrapped_start():  # noqa: D401

            if self.onoff.is_in_dead_front_state():
                return Result.fail(
                    ErrorCode.COMMAND_EXECUTION_ERROR,
                    "Cannot start cycle in dead front state",
                    "Device must be powered on (OnOff = True) to start cycle",
                )
            result = original_start()
            if result.success:

                self._initialize_cycle_on_start()

                phases = self._get_phase_list()
                selected_level = self.controls.attributes.get("SelectedDrynessLevel")
                level = int(selected_level) if isinstance(selected_level, int) else None
                total_minutes = (
                    self.DRYNESS_DURATIONS_MIN.get(level, 45) if level is not None else 45
                )
                command_data = result.get_data() or {}
                return Result.ok(
                    {
                        "cluster": "OperationalState",
                        "command_response_state": command_data.get("command_response_state"),
                        "operational_state": self.operational_state.attributes.get(
                            "OperationalState"
                        ),
                        "operational_state_label": "Running",
                        "cycle_info": {
                            "initial_phase": phases[0] if phases else None,
                            "dryness_level": (
                                DrynessLevelEnum.label(level)
                                if level is not None
                                else None
                            ),
                            "estimated_duration_minutes": total_minutes,
                        },
                    }
                )
            return result

        self.operational_state._start = wrapped_start  # type: ignore[attr-defined]

        if "Start" in self.operational_state.commands:
            self.operational_state.commands["Start"] = wrapped_start


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
        if "LaundryDryerControls" in self.endpoints[1]:
            self.controls.write_attribute("SelectedDrynessLevel", None)

    def _restore_normal_values(self):
        if "OperationalState" in self.endpoints[1]:
            self.operational_state.set_phase_list(
                ["Heating", "Drying", "CoolDown", "Complete"]
            )


    def _initialize_cycle_on_start(self):
        
        phases = self.operational_state.attributes.get("PhaseList", [])
        if isinstance(phases, list) and phases:
            self.operational_state.set_current_phase(0)

        selected_level = self.controls.attributes.get("SelectedDrynessLevel")
        level = int(selected_level) if isinstance(selected_level, int) else None
        total_minutes = (
            self.DRYNESS_DURATIONS_MIN.get(level, 45) if level is not None else 45
        )
        total_seconds = total_minutes * 60
        self.operational_state.set_countdown_time(total_seconds)
        self._initial_countdown = total_seconds
        self._was_running = True


    def _get_phase_list(self) -> list[str]:
        raw = self.operational_state.attributes.get("PhaseList")
        if not isinstance(raw, list):
            return []
        return [phase for phase in raw if isinstance(phase, str)]

    def _get_countdown_time(self) -> Optional[int]:
        raw = self.operational_state.attributes.get("CountdownTime")
        if isinstance(raw, (int, float)):
            return int(raw)
        return None

    def _update_cycle_progress(self):
        if (
            self.operational_state.attributes.get("OperationalState")
            != OperationalStateEnum.RUNNING
        ):
            return
        phase_list = self._get_phase_list()
        if not phase_list:
            return

        countdown = self._get_countdown_time()
        if countdown is None:
            return

        current_phase_raw = self.operational_state.attributes.get("CurrentPhase")
        if isinstance(current_phase_raw, str):
            current_phase = current_phase_raw
        elif isinstance(current_phase_raw, int):
            if 0 <= current_phase_raw < len(phase_list):
                current_phase = phase_list[current_phase_raw]
            else:
                return
        else:
            return

        try:
            idx = phase_list.index(current_phase)
        except ValueError:
            return

        total = self._initial_countdown if self._initial_countdown > 0 else countdown
        phase_durations = [int(total * r) for r in self.PHASE_DURATION_RATIOS]
        elapsed = max(total - countdown, 0)
        cumulative = 0
        boundaries = []
        for d in phase_durations:
            cumulative += d
            boundaries.append(cumulative)
        target_idx = idx
        for i, b in enumerate(boundaries):
            if elapsed <= b:
                target_idx = i
                break
        if target_idx > idx and target_idx < len(phase_list):
            self.operational_state.set_current_phase(target_idx)

    def _handle_cycle_completion(self):
        state = self.operational_state.attributes.get("OperationalState")
        countdown = self.operational_state.attributes.get("CountdownTime")
        if (
            state == OperationalStateEnum.STOPPED
            and countdown is None
            and hasattr(self, "_was_running")
        ):
            delattr(self, "_was_running")

    def on_time_tick(self):  # type: ignore[override]
        self.operational_state.on_time_tick(tick_interval=self.tick_interval)
        self._update_cycle_progress()
        self._handle_cycle_completion()
