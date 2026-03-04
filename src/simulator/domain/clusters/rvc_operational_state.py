from enum import IntEnum
import math
from typing import Any, Optional

from src.simulator.domain.clusters.base import Cluster
from src.simulator.domain.result import ErrorCode, Result


class OperationalState(IntEnum):
    STOPPED = 0x00
    RUNNING = 0x01
    PAUSED = 0x02
    ERROR = 0x03
    SEEKING_CHARGER = 0x40
    CHARGING = 0x41
    DOCKED = 0x42


class ErrorState(IntEnum):
    NO_ERROR = 0x00
    UNABLE_TO_START_OR_RESUME = 0x01
    UNABLE_TO_COMPLETE_OPERATION = 0x02
    COMMAND_INVALID_IN_STATE = 0x03
    FAILED_TO_FIND_CHARGING_DOCK = 0x40
    STUCK = 0x41
    DUST_BIN_MISSING = 0x42
    DUST_BIN_FULL = 0x43
    WATER_TANK_EMPTY = 0x44
    WATER_TANK_MISSING = 0x45
    WATER_TANK_LID_OPEN = 0x46
    MOP_CLEANING_PAD_MISSING = 0x47


class RVCOperationalStateCluster(Cluster):
    CLUSTER_REVISION = 3

    def __init__(self):
        super().__init__(cluster_id="RVCOperationalState")

        self.device: Optional[Any] = None
        self._phase_durations_sec = {
            "Cleaning": 1800,
            "Mapping": 1800,
            "SeekingCharger": 10,
            "Docked": 5,
        }
        self._countdown_elapsed_seconds = 0.0
        self._paused_from_state: Optional[int] = None

        self.attributes: dict[str, Any] = {
            "PhaseList": None,
            "CurrentPhase": None,
            "CountdownTime": None,
            "OperationalStateList": [
                {"operational_state_id": int(OperationalState.STOPPED)},
                {"operational_state_id": int(OperationalState.RUNNING)},
                {"operational_state_id": int(OperationalState.PAUSED)},
                {"operational_state_id": int(OperationalState.ERROR)},
                {"operational_state_id": int(OperationalState.SEEKING_CHARGER)},
                {"operational_state_id": int(OperationalState.CHARGING)},
                {"operational_state_id": int(OperationalState.DOCKED)},
            ],
            "OperationalState": int(OperationalState.STOPPED),
            "OperationalError": {"error_state_id": int(ErrorState.NO_ERROR)},
            "ClusterRevision": self.CLUSTER_REVISION,
        }

        self.readonly_attributes = {
            "PhaseList",
            "CurrentPhase",
            "CountdownTime",
            "OperationalStateList",
            "OperationalState",
            "OperationalError",
            "ClusterRevision",
        }

        self.commands = {
            "Pause": self._pause,
            "Resume": self._resume,
            "GoHome": self._go_home,
        }

    def set_device_reference(self, device: Any) -> None:
        self.device = device

    def _set_error(self, error_state: ErrorState) -> None:
        self.attributes["OperationalError"] = {"error_state_id": int(error_state)}

    def _clear_error(self) -> None:
        self._set_error(ErrorState.NO_ERROR)

    def _set_state(self, state: OperationalState) -> None:
        self.attributes["OperationalState"] = int(state)
        if int(state) != int(OperationalState.PAUSED):
            self._paused_from_state = None

    def _response(self, error_state: ErrorState) -> Result:
        self._set_error(error_state)
        return Result.ok(
            {
                "command_response_state": {
                    "error_state_id": int(error_state),
                },
                "operational_state": self.attributes["OperationalState"],
            }
        )

    def _current_state(self) -> Optional[int]:
        value = self.attributes.get("OperationalState")
        if isinstance(value, int):
            return int(value)
        return None

    def _require_run_mode_idle(self) -> Result:
        if self.device is None:
            return Result.fail(
                ErrorCode.INVALID_STATE,
                "RVC device reference is not set",
            )

        run_mode_cluster = getattr(self.device, "run_mode", None)
        if run_mode_cluster is None:
            return Result.fail(
                ErrorCode.INVALID_STATE,
                "RVCRunMode cluster is not available",
            )

        current_mode = run_mode_cluster.attributes.get("CurrentMode")
        if not isinstance(current_mode, int):
            return Result.fail(
                ErrorCode.INVALID_STATE,
                "RVCRunMode.CurrentMode is malformed",
            )

        return Result.ok(bool(run_mode_cluster.is_idle_mode(current_mode)))

    def _set_run_mode_idle(self) -> None:
        if self.device is None:
            raise RuntimeError("RVC device reference is not set")
        self.device.set_run_mode_idle()

    def _set_phase(self, phase_list: list[str], phase_index: int) -> None:
        self.attributes["PhaseList"] = phase_list
        self.attributes["CurrentPhase"] = phase_index

        phase_name = phase_list[phase_index]
        self.attributes["CountdownTime"] = int(self._phase_durations_sec.get(phase_name, 0))
        self._countdown_elapsed_seconds = 0.0
        self._paused_from_state = None

        if phase_name in ("Cleaning", "Mapping"):
            self._set_state(OperationalState.RUNNING)
        elif phase_name == "SeekingCharger":
            self._set_state(OperationalState.SEEKING_CHARGER)
        elif phase_name == "Docked":
            self._set_state(OperationalState.DOCKED)

    def start_operation(self, run_phase: str) -> None:
        if run_phase not in ("Cleaning", "Mapping"):
            run_phase = "Cleaning"
        self._clear_error()
        self._paused_from_state = None
        self._set_phase([run_phase, "SeekingCharger", "Docked"], 0)

    def begin_seek_charger(self) -> None:
        phase_list_raw = self.attributes.get("PhaseList")
        if not isinstance(phase_list_raw, list) or not phase_list_raw:
            phase_list = ["SeekingCharger", "Docked"]
        else:
            phase_list = [str(p) for p in phase_list_raw if isinstance(p, str)]
            if "SeekingCharger" not in phase_list:
                phase_list.append("SeekingCharger")
            if "Docked" not in phase_list:
                phase_list.append("Docked")

        self._clear_error()
        self._paused_from_state = None
        self._set_phase(phase_list, phase_list.index("SeekingCharger"))
        self._set_run_mode_idle()

    def stop_operation(self) -> None:
        self._set_state(OperationalState.STOPPED)
        self._clear_error()
        self.attributes["CurrentPhase"] = None
        self.attributes["CountdownTime"] = None
        self._countdown_elapsed_seconds = 0.0
        self._paused_from_state = None

    def _pause(self) -> Result:
        state = self._current_state()
        if state is None:
            return Result.fail(
                ErrorCode.INVALID_STATE,
                "OperationalState is malformed",
            )

        if state == int(OperationalState.PAUSED):
            return self._response(ErrorState.NO_ERROR)

        if state in (int(OperationalState.RUNNING), int(OperationalState.SEEKING_CHARGER)):
            self._paused_from_state = int(state)
            self._set_state(OperationalState.PAUSED)
            return self._response(ErrorState.NO_ERROR)

        return self._response(ErrorState.COMMAND_INVALID_IN_STATE)

    def _resume(self) -> Result:
        state = self._current_state()
        if state is None:
            return Result.fail(
                ErrorCode.INVALID_STATE,
                "OperationalState is malformed",
            )

        if state == int(OperationalState.RUNNING):
            return self._response(ErrorState.NO_ERROR)

        if state == int(OperationalState.PAUSED):
            resume_state = self._paused_from_state
            if resume_state not in (
                int(OperationalState.RUNNING),
                int(OperationalState.SEEKING_CHARGER),
            ):
                resume_state = int(OperationalState.RUNNING)
            self._set_state(OperationalState(resume_state))
            return self._response(ErrorState.NO_ERROR)

        if state in (int(OperationalState.CHARGING), int(OperationalState.DOCKED)):
            run_mode_idle_result = self._require_run_mode_idle()
            if not run_mode_idle_result.success:
                return run_mode_idle_result

            if bool(run_mode_idle_result.data):
                return self._response(ErrorState.COMMAND_INVALID_IN_STATE)
            self._set_state(OperationalState.RUNNING)
            return self._response(ErrorState.NO_ERROR)

        return self._response(ErrorState.COMMAND_INVALID_IN_STATE)

    def _go_home(self) -> Result:
        state = self._current_state()
        if state is None:
            return Result.fail(
                ErrorCode.INVALID_STATE,
                "OperationalState is malformed",
            )

        if state == int(OperationalState.SEEKING_CHARGER):
            return self._response(ErrorState.NO_ERROR)

        if state in (int(OperationalState.CHARGING), int(OperationalState.DOCKED)):
            return self._response(ErrorState.COMMAND_INVALID_IN_STATE)

        if state == int(OperationalState.STOPPED):
            run_mode_idle_result = self._require_run_mode_idle()
            if not run_mode_idle_result.success:
                return run_mode_idle_result
            if not bool(run_mode_idle_result.data):
                return self._response(ErrorState.COMMAND_INVALID_IN_STATE)

        if state not in (
            int(OperationalState.STOPPED),
            int(OperationalState.RUNNING),
            int(OperationalState.PAUSED),
        ):
            return self._response(ErrorState.COMMAND_INVALID_IN_STATE)

        self.begin_seek_charger()
        return self._response(ErrorState.NO_ERROR)

    def _advance_phase_if_needed(self) -> None:
        phase_list = self.attributes.get("PhaseList")
        current_phase = self.attributes.get("CurrentPhase")

        if not isinstance(phase_list, list) or not isinstance(current_phase, int):
            return

        next_phase = current_phase + 1
        if next_phase < len(phase_list):
            self._set_phase(phase_list, next_phase)
            if phase_list[next_phase] == "Docked":
                self._set_run_mode_idle()
            return

        self.stop_operation()
        self._set_run_mode_idle()

    def on_time_tick(self, tick_interval: float = 0.1) -> None:
        countdown = self.attributes.get("CountdownTime")
        if countdown is None:
            return

        if isinstance(countdown, bool) or not isinstance(countdown, (int, float)):
            return

        countdown_seconds = float(countdown)
        if not math.isfinite(countdown_seconds):
            return

        state = self._current_state()
        if state in (
            int(OperationalState.PAUSED),
            int(OperationalState.STOPPED),
            int(OperationalState.ERROR),
            int(OperationalState.CHARGING),
        ):
            return

        normalized_countdown = int(max(0, math.ceil(countdown_seconds)))
        self.attributes["CountdownTime"] = normalized_countdown

        if normalized_countdown <= 0:
            self._advance_phase_if_needed()
            return

        self._countdown_elapsed_seconds += max(0.0, float(tick_interval))
        elapsed_seconds = int(self._countdown_elapsed_seconds)
        if elapsed_seconds <= 0:
            return

        self._countdown_elapsed_seconds -= float(elapsed_seconds)
        remaining = max(0, normalized_countdown - elapsed_seconds)
        self.attributes["CountdownTime"] = int(remaining)
        if remaining <= 0:
            self._advance_phase_if_needed()
