from src.simulator.domain.clusters.base import Cluster
from src.simulator.domain.result import Result, ErrorCode
from enum import IntEnum
import math
from typing import List, Dict, Any, Optional, Literal


class OperationalStateEnum(IntEnum):
    

    STOPPED = 0x00
    RUNNING = 0x01
    PAUSED = 0x02
    ERROR = 0x03


class ErrorStateEnum(IntEnum):
    

    NO_ERROR = 0x00
    UNABLE_TO_START_OR_RESUME = 0x01
    UNABLE_TO_COMPLETE_OPERATION = 0x02
    COMMAND_INVALID_IN_STATE = 0x03


class OperationalStateStruct:
    

    def __init__(
        self, operational_state_id: int, operational_state_label: Optional[str] = None
    ):
        self.operational_state_id = operational_state_id

        if 0x80 <= operational_state_id <= 0xBF:
            if operational_state_label is None:
                raise ValueError(
                    "OperationalStateLabel is required for Manufacturer Specific States"
                )
            self.operational_state_label = operational_state_label
        else:

            self.operational_state_label = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        result["operational_state_id"] = int(self.operational_state_id)
        if self.operational_state_label is not None:
            result["operational_state_label"] = self.operational_state_label
        return result


class ErrorStateStruct:
    

    def __init__(
        self,
        error_state_id: int,
        error_state_label: Optional[str] = None,
        error_state_details: Optional[str] = None,
    ):
        self.error_state_id = error_state_id


        if 0x80 <= error_state_id <= 0xBF:
            if error_state_label is None:
                raise ValueError(
                    "ErrorStateLabel is required for Manufacturer Specific Errors"
                )
            self.error_state_label = error_state_label
        else:

            self.error_state_label = None


        self.error_state_details = (
            error_state_details[:64] if error_state_details else ""
        )

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        result["error_state_id"] = int(self.error_state_id)
        if self.error_state_label is not None:
            result["error_state_label"] = self.error_state_label
        if self.error_state_details:
            result["error_state_details"] = self.error_state_details
        return result


class OperationalStateCluster(Cluster):
    

    def __init__(
        self,
        supported_commands: Optional[
            List[Literal["Pause", "Resume", "Start", "Stop"]]
        ] = None,
    ):
        super().__init__(cluster_id="OperationalState")


        default_states = [
            OperationalStateStruct(OperationalStateEnum.STOPPED),
            OperationalStateStruct(OperationalStateEnum.RUNNING),
            OperationalStateStruct(OperationalStateEnum.PAUSED),
            OperationalStateStruct(OperationalStateEnum.ERROR),
        ]


        default_error = ErrorStateStruct(ErrorStateEnum.NO_ERROR)


        self.attributes: Dict[str, Any] = {
            "PhaseList": None,
            "CurrentPhase": None,
            "CountdownTime": None,
            "OperationalStateList": [
                state.to_dict() for state in default_states
            ],
            "OperationalState": OperationalStateEnum.STOPPED,
            "OperationalError": default_error.to_dict(),
        }


        self.supported_commands = supported_commands or []
        self.readonly_attributes = {
            "PhaseList",
            "CurrentPhase",
            "CountdownTime",
            "OperationalStateList",
            "OperationalState",
            "OperationalError",
        }

        self.commands: Dict[str, Any] = {}


        if "Pause" in self.supported_commands:
            self.commands["Pause"] = self._pause

            if "Resume" not in self.supported_commands:
                self.supported_commands.append("Resume")
            self.commands["Resume"] = self._resume

        if "Stop" in self.supported_commands:
            self.commands["Stop"] = self._stop

        if "Start" in self.supported_commands:
            self.commands["Start"] = self._start

            if "Stop" not in self.supported_commands:
                self.supported_commands.append("Stop")
            self.commands["Stop"] = self._stop

        if (
            "Resume" in self.supported_commands
            and "Pause" not in self.supported_commands
        ):

            self.supported_commands.append("Pause")
            self.commands["Pause"] = self._pause


        if any(
            cmd in self.supported_commands
            for cmd in ["Pause", "Stop", "Start", "Resume"]
        ):
            self.commands["OperationalCommandResponse"] = (
                self._operational_command_response
            )


        self._state_lookup: Dict[int, OperationalStateStruct] = {
            state.operational_state_id: state for state in default_states
        }
        self._countdown_elapsed_seconds = 0.0

    def _get_error_label(self, error_state_id: int) -> str:
        
        if int(error_state_id) == int(ErrorStateEnum.NO_ERROR):
            return "No Error"
        if int(error_state_id) == int(ErrorStateEnum.UNABLE_TO_START_OR_RESUME):
            return "Unable to start or resume"
        if int(error_state_id) == int(ErrorStateEnum.UNABLE_TO_COMPLETE_OPERATION):
            return "Unable to complete operation"
        if int(error_state_id) == int(ErrorStateEnum.COMMAND_INVALID_IN_STATE):
            return "Command invalid in current state"
        return f"Unknown error {error_state_id}"

    def _get_state_label(self, state_id: int) -> str:
        
        state_labels = {
            int(OperationalStateEnum.STOPPED): "Stopped",
            int(OperationalStateEnum.RUNNING): "Running",
            int(OperationalStateEnum.PAUSED): "Paused",
            int(OperationalStateEnum.ERROR): "Error",
        }
        return state_labels.get(int(state_id), f"Unknown state {state_id}")

    def _create_command_response(
        self, error_state_id: int, error_details: Optional[str] = None
    ) -> Result:
        
        error_struct = ErrorStateStruct(
            error_state_id, error_state_details=error_details
        )
        response_dict = error_struct.to_dict()

        return Result.ok(
            {
                "cluster": self.cluster_id,
                "command_response_state": response_dict,
                "operational_state": self.attributes["OperationalState"],
                "operational_state_label": self._get_state_label(
                    self.attributes["OperationalState"]
                ),
            }
        )

    def _pause(self) -> Result:
        
        current_state = self.attributes["OperationalState"]

        if current_state == OperationalStateEnum.PAUSED:
            return self._create_command_response(ErrorStateEnum.NO_ERROR)

        if current_state != OperationalStateEnum.RUNNING:
            return self._create_command_response(
                ErrorStateEnum.COMMAND_INVALID_IN_STATE
            )

        self.attributes["OperationalState"] = OperationalStateEnum.PAUSED
        return self._create_command_response(ErrorStateEnum.NO_ERROR)

    def _stop(self) -> Result:
        
        current_state = self.attributes["OperationalState"]

        if current_state == OperationalStateEnum.STOPPED:
            return self._create_command_response(ErrorStateEnum.NO_ERROR)


        self.attributes["OperationalState"] = OperationalStateEnum.STOPPED
        self.attributes["CurrentPhase"] = None
        self.attributes["CountdownTime"] = None
        self._countdown_elapsed_seconds = 0.0

        return self._create_command_response(ErrorStateEnum.NO_ERROR)

    def _start(self) -> Result:
        
        current_state = self.attributes["OperationalState"]

        if current_state == OperationalStateEnum.RUNNING:
            return self._create_command_response(ErrorStateEnum.NO_ERROR)

        if current_state != OperationalStateEnum.STOPPED:
            error_code = (
                ErrorStateEnum.UNABLE_TO_START_OR_RESUME
                if current_state == OperationalStateEnum.ERROR
                else ErrorStateEnum.COMMAND_INVALID_IN_STATE
            )
            return self._create_command_response(error_code)

        self.attributes["OperationalState"] = OperationalStateEnum.RUNNING
        self._countdown_elapsed_seconds = 0.0
        return self._create_command_response(ErrorStateEnum.NO_ERROR)

    def _resume(self) -> Result:
        
        current_state = self.attributes["OperationalState"]

        if current_state == OperationalStateEnum.RUNNING:
            return self._create_command_response(ErrorStateEnum.NO_ERROR)

        if current_state != OperationalStateEnum.PAUSED:
            error_code = (
                ErrorStateEnum.UNABLE_TO_START_OR_RESUME
                if current_state == OperationalStateEnum.ERROR
                else ErrorStateEnum.COMMAND_INVALID_IN_STATE
            )
            return self._create_command_response(error_code)

        self.attributes["OperationalState"] = OperationalStateEnum.RUNNING
        self._countdown_elapsed_seconds = 0.0
        return self._create_command_response(ErrorStateEnum.NO_ERROR)

    def _operational_command_response(
        self, command_response_state: Dict[str, Any]
    ) -> Result:
        
        return Result.ok(
            {
                "cluster": self.cluster_id,
                "command": "OperationalCommandResponse",
                "command_response_state": command_response_state,
            }
        )

    def get_current_state_info(self) -> Dict[str, Any]:
        
        current_state = self.attributes["OperationalState"]
        current_error = self.attributes["OperationalError"]

        return {
            "operational_state": current_state,
            "operational_state_label": self._get_state_label(current_state),
            "operational_error": current_error,
            "current_phase": self.attributes["CurrentPhase"],
            "countdown_time": self.attributes["CountdownTime"],
            "phase_list": self.attributes["PhaseList"],
            "is_running": current_state == OperationalStateEnum.RUNNING,
            "is_stopped": current_state == OperationalStateEnum.STOPPED,
            "is_paused": current_state == OperationalStateEnum.PAUSED,
            "has_error": current_state == OperationalStateEnum.ERROR,
            "supported_commands": self.supported_commands,
        }

    def set_error_state(
        self, error_state_id: int, error_details: Optional[str] = None
    ) -> Result:
        
        error_struct = ErrorStateStruct(
            error_state_id, error_state_details=error_details
        )
        self.attributes["OperationalState"] = OperationalStateEnum.ERROR
        self.attributes["OperationalError"] = error_struct.to_dict()
        self._countdown_elapsed_seconds = 0.0

        return Result.ok(
            {
                "cluster": self.cluster_id,
                "command": "SetErrorState",
                "error_state": error_struct.to_dict(),
            }
        )

    def clear_error_state(self) -> Result:
        
        no_error = ErrorStateStruct(ErrorStateEnum.NO_ERROR)
        self.attributes["OperationalState"] = OperationalStateEnum.STOPPED
        self.attributes["OperationalError"] = no_error.to_dict()
        self.attributes["CurrentPhase"] = None
        self.attributes["CountdownTime"] = None
        self._countdown_elapsed_seconds = 0.0

        return Result.ok(
            {
                "cluster": self.cluster_id,
                "command": "ClearErrorState",
                "operational_state": OperationalStateEnum.STOPPED,
            }
        )

    def set_phase_list(self, phases: List[str]) -> Result:
        
        if phases is not None:
            if len(phases) > 32:
                return Result.fail(
                    error_code=ErrorCode.INVALID_ARGUMENT,
                    error_message="Too many phases",
                    error_detail=f"Maximum 32 phases allowed, got {len(phases)}",
                )
            for i, phase in enumerate(phases):
                if len(phase) > 64:
                    return Result.fail(
                        error_code=ErrorCode.INVALID_ARGUMENT,
                        error_message=f"Phase name too long",
                        error_detail=f"Phase {i} '{phase}' exceeds 64 character limit",
                    )

        self.attributes["PhaseList"] = phases
        if phases is None:
            self.attributes["CurrentPhase"] = None
        else:
            current_phase = self.attributes["CurrentPhase"]
            if current_phase is not None and current_phase >= len(phases):
                self.attributes["CurrentPhase"] = None

        return Result.ok(
            {"cluster": self.cluster_id, "command": "SetPhaseList", "phases": phases}
        )

    def set_current_phase(self, phase_index: int) -> Result:
        
        phase_list = self.attributes["PhaseList"]

        if phase_index is not None:
            if phase_list is None:
                return Result.fail(
                    error_code=ErrorCode.INVALID_STATE,
                    error_message="Cannot set phase when PhaseList is null",
                )
            if not (0 <= phase_index < len(phase_list)):
                return Result.fail(
                    error_code=ErrorCode.INVALID_ARGUMENT,
                    error_message=f"Phase index {phase_index} out of range",
                    error_detail=f"Valid range: 0 to {len(phase_list) - 1}",
                )
        self.attributes["CurrentPhase"] = phase_index
        return Result.ok(
            {
                "cluster": self.cluster_id,
                "command": "SetCurrentPhase",
                "phase_index": phase_index,
            }
        )

    def set_countdown_time(self, countdown_time: Optional[int]) -> Result:
        
        if countdown_time is not None:
            if isinstance(countdown_time, bool) or not isinstance(countdown_time, int):
                return Result.fail(
                    error_code=ErrorCode.INVALID_ARGUMENT,
                    error_message="Invalid countdown time type",
                    error_detail="countdown_time must be an integer or null",
                )
            if countdown_time < 0:
                return Result.fail(
                    error_code=ErrorCode.INVALID_ARGUMENT,
                    error_message="Countdown time must be non-negative",
                    error_detail=f"countdown_time must be >= 0, got {countdown_time}",
                )
            if countdown_time > 259200:
                return Result.fail(
                    error_code=ErrorCode.INVALID_ARGUMENT,
                    error_message="Countdown time too large",
                    error_detail=f"Maximum 259200 seconds (72 hours) allowed, got {countdown_time}",
                )

        self.attributes["CountdownTime"] = countdown_time
        self._countdown_elapsed_seconds = 0.0
        return Result.ok(
            {
                "cluster": self.cluster_id,
                "command": "SetCountdownTime",
                "countdown_time": countdown_time,
            }
        )

    def on_time_tick(self, tick_interval: float = 0.1):
        
        countdown = self.attributes.get("CountdownTime")
        current_state = self.attributes.get("OperationalState")

        if current_state != OperationalStateEnum.RUNNING:
            return

        if countdown is None:
            self._countdown_elapsed_seconds = 0.0
            return

        if isinstance(countdown, bool) or not isinstance(countdown, (int, float)):
            return

        countdown_seconds = float(countdown)
        if not math.isfinite(countdown_seconds):
            return

        normalized_countdown = int(max(0, math.ceil(countdown_seconds)))
        self.attributes["CountdownTime"] = normalized_countdown

        if normalized_countdown <= 0:
            self._complete_operation()
            return

        self._countdown_elapsed_seconds += max(0.0, float(tick_interval))
        elapsed_seconds = int(self._countdown_elapsed_seconds)
        if elapsed_seconds <= 0:
            return

        self._countdown_elapsed_seconds -= float(elapsed_seconds)
        new_countdown = max(0, normalized_countdown - elapsed_seconds)
        self.attributes["CountdownTime"] = new_countdown
        if new_countdown <= 0:
            self._complete_operation()

    def _complete_operation(self):
        
        phase_list = self.attributes.get("PhaseList")
        if isinstance(phase_list, list) and len(phase_list) > 0:
            self.attributes["CurrentPhase"] = len(phase_list) - 1
        else:
            self.attributes["CurrentPhase"] = None
        self.attributes["OperationalState"] = OperationalStateEnum.STOPPED
        self.attributes["CountdownTime"] = None
        self._countdown_elapsed_seconds = 0.0
