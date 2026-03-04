from src.simulator.domain.clusters.base import Cluster
from src.simulator.domain.result import Result, ErrorCode
from enum import IntEnum
from typing import Any


class WindowCoveringType(IntEnum):
    

    ROLLER_SHADE = 0
    ROLLER_SHADE_2_MOTOR = 1
    ROLLER_SHADE_EXTERIOR = 2
    ROLLER_SHADE_EXTERIOR_2_MOTOR = 3
    DRAPERY = 4
    AWNING = 5
    SHUTTER = 6
    TILT_BLIND_TILT_ONLY = 7
    TILT_BLIND_LIFT_AND_TILT = 8
    PROJECTOR_SCREEN = 9
    UNKNOWN = 255


class EndProductType(IntEnum):
    

    ROLLER_SHADE = 0
    ROMAN_SHADE = 1
    BALLOON_SHADE = 2
    WOVEN_WOOD = 3
    PLEATED_SHADE = 4
    CELLULAR_SHADE = 5
    LAYERED_SHADE = 6
    LAYERED_SHADE_2D = 7
    SHEER_SHADE = 8
    TILT_ONLY_INTERIOR_BLIND = 9
    INTERIOR_BLIND = 10
    VERTICAL_BLIND_STRIP_CURTAIN = 11
    INTERIOR_VENETIAN_BLIND = 12
    EXTERIOR_VENETIAN_BLIND = 13
    LATERAL_LEFT_CURTAIN = 14
    LATERAL_RIGHT_CURTAIN = 15
    CENTRAL_CURTAIN = 16
    ROLLER_SHUTTER = 17
    EXTERIOR_VERTICAL_SCREEN = 18
    AWNING_TERRACE_PATIO = 19
    AWNING_VERTICAL_SCREEN = 20
    TILT_ONLY_PERGOLA = 21
    SWINGING_SHUTTER = 22
    SLIDING_SHUTTER = 23
    UNKNOWN = 255


class ConfigStatusBitmap:
    

    OPERATIONAL = 0x01
    ONLINE_RESERVED = 0x02
    LIFT_MOVEMENT_REVERSED = 0x04
    LIFT_POSITION_AWARE = 0x08
    TILT_POSITION_AWARE = 0x10
    LIFT_ENCODER_CONTROLLED = 0x20
    TILT_ENCODER_CONTROLLED = 0x40


class ModeBitmap:
    

    MOTOR_DIRECTION_REVERSED = 0x01
    CALIBRATION_MODE = 0x02
    MAINTENANCE_MODE = 0x04
    LED_FEEDBACK = 0x08


class OperationalStatusBitmap:
    

    GLOBAL_NOT_MOVING = 0x00
    GLOBAL_OPENING = 0x01
    GLOBAL_CLOSING = 0x02
    GLOBAL_RESERVED = 0x03


    LIFT_NOT_MOVING = 0x00
    LIFT_OPENING = 0x04
    LIFT_CLOSING = 0x08
    LIFT_RESERVED = 0x0C


    TILT_NOT_MOVING = 0x00
    TILT_OPENING = 0x10
    TILT_CLOSING = 0x20
    TILT_RESERVED = 0x30


class SafetyStatusBitmap:
    

    REMOTE_LOCKOUT = 0x0001
    TAMPER_DETECTION = 0x0002
    FAILED_COMMUNICATION = 0x0004
    POSITION_FAILURE = 0x0008
    THERMAL_PROTECTION = 0x0010
    OBSTACLE_DETECTED = 0x0020
    POWER = 0x0040
    STOP_INPUT = 0x0080
    MOTOR_JAMMED = 0x0100
    HARDWARE_FAILURE = 0x0200
    MANUAL_OPERATION = 0x0400
    PROTECTION = 0x0800


class WindowCoveringCluster(Cluster):
    

    FULL_TRAVEL_TIME_TENTHS = 30

    def __init__(self, start_position_percent_100ths: int = 0):
        super().__init__(cluster_id="WindowCovering")


        self._supports_lift = True
        self._supports_tilt = False
        self._supports_pa_lift = True
        self._supports_pa_tilt = False
        self._supports_absolute = False


        self.attributes = {
            "Type": WindowCoveringType.ROLLER_SHADE,
            "ConfigStatus": ConfigStatusBitmap.OPERATIONAL,
            "OperationalStatus": OperationalStatusBitmap.GLOBAL_NOT_MOVING,
            "EndProductType": EndProductType.ROLLER_SHADE,
            "Mode": ModeBitmap.MOTOR_DIRECTION_REVERSED,

            "SafetyStatus": 0,

            "CurrentPositionLiftPercent100ths": int(start_position_percent_100ths),
            "TargetPositionLiftPercent100ths": int(start_position_percent_100ths),
            "NumberOfActuationsLift": 0,
        }


        self.readonly_attributes = {
            "Type",
            "ConfigStatus",
            "OperationalStatus",
            "EndProductType",
            "SafetyStatus",
        }


        self.commands = {
            "UpOrOpen": self._up_or_open,
            "DownOrClose": self._down_or_close,
            "StopMotion": self._stop_motion,
            "GoToLiftPercentage": self._go_to_lift_percentage,
        }


        self._motion_state = {
            "active": False,
            "start_position": 0,
            "target_position": 0,
            "start_time": 0.0,
            "duration_tenths": 0,
        }

        self.device = None

    def write_attribute(self, attribute_id: str, value: Any) -> Result:
        
        if attribute_id == "TargetPositionLiftPercent100ths":

            if not isinstance(value, int):
                return Result.fail(
                    ErrorCode.VALIDATION_ERROR,
                    "Invalid parameter type for TargetPositionLiftPercent100ths",
                    f"Expected int 0-10000, got {type(value).__name__}",
                )
            return self._go_to_lift_percentage(value)

        return super().write_attribute(attribute_id, value)

    def get_status_info(self) -> dict:
        
        current_pos = self.attributes["CurrentPositionLiftPercent100ths"]
        target_pos = self.attributes["TargetPositionLiftPercent100ths"]
        operational_status = self.attributes["OperationalStatus"]
        safety_status = self.attributes["SafetyStatus"]


        if operational_status == OperationalStatusBitmap.GLOBAL_NOT_MOVING:
            motion_status = "stopped"
        elif operational_status == OperationalStatusBitmap.GLOBAL_OPENING:
            motion_status = "opening (moving up)"
        elif operational_status == OperationalStatusBitmap.GLOBAL_CLOSING:
            motion_status = "closing (moving down)"
        else:
            motion_status = f"unknown (0x{operational_status:02X})"


        safety_issues = []
        if safety_status != 0:
            if safety_status & SafetyStatusBitmap.REMOTE_LOCKOUT:
                safety_issues.append("remote lockout")
            if safety_status & SafetyStatusBitmap.OBSTACLE_DETECTED:
                safety_issues.append("obstacle detected")
            if safety_status & SafetyStatusBitmap.MOTOR_JAMMED:
                safety_issues.append("motor jammed")
            if safety_status & SafetyStatusBitmap.HARDWARE_FAILURE:
                safety_issues.append("hardware failure")


        return {
            "current_position": current_pos,
            "current_percentage": current_pos / 100,
            "target_position": target_pos,
            "target_percentage": target_pos / 100,
            "motion_status": motion_status,
            "is_moving": self._motion_state["active"],
            "safety_status": safety_status,
            "safety_issues": safety_issues,
            "is_safe_to_operate": safety_status == 0,
            "actuation_count": self.attributes["NumberOfActuationsLift"],
            "covering_type": self.attributes["Type"],
            "end_product_type": self.attributes["EndProductType"],
            "available_commands": list(self.commands.keys()),
            "position_description": self._get_position_description(current_pos),
        }

    def _get_position_description(self, position: int) -> str:
        
        percentage = position / 100
        if position == 0:
            return "fully open"
        elif position == 10000:
            return "fully closed"
        elif position < 2500:
            return f"mostly open ({percentage}%)"
        elif position < 5000:
            return f"partially open ({percentage}%)"
        elif position < 7500:
            return f"partially closed ({percentage}%)"
        else:
            return f"mostly closed ({percentage}%)"

    def validate_command_parameters(self, command_name: str, **kwargs) -> Result:
        
        if command_name not in self.commands:
            available_commands = ", ".join(self.commands.keys())
            return Result.fail(
                ErrorCode.VALIDATION_ERROR,
                f"Unknown command '{command_name}'. Available commands: {available_commands}",
            )

        if command_name == "GoToLiftPercentage":
            if "lift_percent_100ths" not in kwargs:
                return Result.fail(
                    ErrorCode.VALIDATION_ERROR,
                    f"Missing required parameter 'lift_percent_100ths' for {command_name} command. "
                    f"Expected: integer value 0-10000 (0.01% units, where 0=fully open, 10000=fully closed)",
                )

            lift_value = kwargs["lift_percent_100ths"]
            if not isinstance(lift_value, int):
                return Result.fail(
                    ErrorCode.VALIDATION_ERROR,
                    f"Invalid parameter type for 'lift_percent_100ths': expected int, got {type(lift_value).__name__}. "
                    f"Value must be integer 0-10000 (0.01% units)",
                )

            if not (0 <= lift_value <= 10000):
                return Result.fail(
                    ErrorCode.VALIDATION_ERROR,
                    f"Parameter 'lift_percent_100ths' out of range: {lift_value}. "
                    f"Valid range: 0-10000. Examples: 0=open, 2500=25% closed, 5000=50% closed, 10000=fully closed",
                )

        elif command_name in ["UpOrOpen", "DownOrClose", "StopMotion"]:

            unexpected_params = [k for k in kwargs.keys() if k != "command_name"]
            if unexpected_params:
                return Result.fail(
                    ErrorCode.VALIDATION_ERROR,
                    f"Command '{command_name}' does not accept parameters, but received: {unexpected_params}. "
                    f"This command should be called without additional parameters.",
                )

        return Result.ok(
            {"validation": "passed", "command": command_name, "parameters": kwargs}
        )

    def on_time_tick(self):
        
        self._process_lift_motion()

    def _process_lift_motion(self):
        
        if not self._motion_state["active"]:
            return


        if not self.device or not self.device.home:

            elapsed_time = self._motion_state["duration_tenths"]
        else:
            elapsed_time = (
                self.device.home.current_time - self._motion_state["start_time"]
            ) * 10

        duration = self._motion_state["duration_tenths"]

        if elapsed_time >= duration:

            final_position = self._motion_state["target_position"]
            self.attributes["CurrentPositionLiftPercent100ths"] = final_position

            self.attributes["TargetPositionLiftPercent100ths"] = final_position
            self._motion_state["active"] = False
            self.attributes["OperationalStatus"] = (
                OperationalStatusBitmap.GLOBAL_NOT_MOVING
            )

        else:

            progress = elapsed_time / duration if duration > 0 else 1.0
            start_pos = self._motion_state["start_position"]
            target_pos = self._motion_state["target_position"]


            current_position = int(start_pos + (target_pos - start_pos) * progress)
            self.attributes["CurrentPositionLiftPercent100ths"] = current_position

    def _go_to_lift_percentage(self, lift_percent_100ths: int) -> Result:
        

        if not isinstance(lift_percent_100ths, int):
            return Result.fail(
                ErrorCode.VALIDATION_ERROR,
                f"Invalid parameter type: lift_percent_100ths must be int, got {type(lift_percent_100ths).__name__}. "
                f"Valid range: 0-10000 (0.01% units, where 0=fully open, 10000=fully closed)",
            )


        safety_status = self.attributes["SafetyStatus"]
        if safety_status != 0:
            safety_reasons = []
            if safety_status & SafetyStatusBitmap.REMOTE_LOCKOUT:
                safety_reasons.append("remote lockout")
            if safety_status & SafetyStatusBitmap.TAMPER_DETECTION:
                safety_reasons.append("tamper detection")
            if safety_status & SafetyStatusBitmap.FAILED_COMMUNICATION:
                safety_reasons.append("communication failure")
            if safety_status & SafetyStatusBitmap.POSITION_FAILURE:
                safety_reasons.append("position sensor failure")
            if safety_status & SafetyStatusBitmap.THERMAL_PROTECTION:
                safety_reasons.append("thermal protection")
            if safety_status & SafetyStatusBitmap.OBSTACLE_DETECTED:
                safety_reasons.append("obstacle detected")
            if safety_status & SafetyStatusBitmap.POWER:
                safety_reasons.append("power issue")
            if safety_status & SafetyStatusBitmap.STOP_INPUT:
                safety_reasons.append("stop input active")
            if safety_status & SafetyStatusBitmap.MOTOR_JAMMED:
                safety_reasons.append("motor jammed")
            if safety_status & SafetyStatusBitmap.HARDWARE_FAILURE:
                safety_reasons.append("hardware failure")
            if safety_status & SafetyStatusBitmap.MANUAL_OPERATION:
                safety_reasons.append("manual operation mode")
            if safety_status & SafetyStatusBitmap.PROTECTION:
                safety_reasons.append("protection mode active")

            return Result.fail(
                ErrorCode.COMMAND_EXECUTION_ERROR,
                f"Window covering safety lockout active (status: 0x{safety_status:04X}). "
                f"Reason(s): {', '.join(safety_reasons)}. "
                f"Clear safety issues before attempting movement commands.",
            )


        if not (0 <= lift_percent_100ths <= 10000):
            return Result.fail(
                ErrorCode.VALIDATION_ERROR,
                f"lift_percent_100ths parameter out of valid range: {lift_percent_100ths}. "
                f"Valid range: 0-10000 (0.01% units). "
                f"Examples: 0=fully open/up, 2500=25% closed, 5000=50% closed, 10000=fully closed/down. "
                f"Current position: {self.attributes['CurrentPositionLiftPercent100ths']} "
                f"({self.attributes['CurrentPositionLiftPercent100ths']/100}%)",
            )

        current_pos = self.attributes["CurrentPositionLiftPercent100ths"]
        target_pos = lift_percent_100ths


        if current_pos == target_pos:
            return Result.ok(
                {
                    "status": "Already at target position",
                    "current_position": current_pos,
                    "current_percentage": current_pos / 100,
                    "message": f"Window covering is already at {current_pos/100}% position",
                }
            )


        travel_distance_ratio = abs(target_pos - current_pos) / 10000.0
        duration = int(self.FULL_TRAVEL_TIME_TENTHS * travel_distance_ratio)

        if duration == 0:
            duration = 1


        existing_motion = self._motion_state["active"]
        if existing_motion:
            self._stop_motion()


        if self.device and self.device.home:
            start_time = self.device.home.current_time
        else:
            start_time = 0

        self._motion_state = {
            "active": True,
            "start_position": current_pos,
            "target_position": target_pos,
            "start_time": start_time,
            "duration_tenths": duration,
        }

        self.attributes["TargetPositionLiftPercent100ths"] = target_pos
        self.attributes["NumberOfActuationsLift"] += 1

        direction = "opening" if target_pos < current_pos else "closing"
        direction_detail = "up/open" if target_pos < current_pos else "down/close"


        if direction == "opening":
            self.attributes["OperationalStatus"] = (
                OperationalStatusBitmap.GLOBAL_OPENING
            )
        else:
            self.attributes["OperationalStatus"] = (
                OperationalStatusBitmap.GLOBAL_CLOSING
            )

        return Result.ok(
            {
                "status": "Movement started",
                "direction": direction,
                "direction_detail": direction_detail,
                "start_position": current_pos,
                "start_percentage": current_pos / 100,
                "target_position": target_pos,
                "target_percentage": target_pos / 100,
                "estimated_duration_sec": duration / 10.0,
                "travel_distance_percent": abs(target_pos - current_pos) / 100,
                "interrupted_existing_motion": existing_motion,
                "actuation_count": self.attributes["NumberOfActuationsLift"],
            }
        )

    def _up_or_open(self) -> Result:
        

        current_pos = self.attributes["CurrentPositionLiftPercent100ths"]


        safety_status = self.attributes["SafetyStatus"]
        if safety_status != 0:
            return Result.fail(
                ErrorCode.COMMAND_EXECUTION_ERROR,
                f"Cannot execute UpOrOpen command: Safety lockout active (0x{safety_status:04X}). "
                f"Clear safety issues before attempting to open the window covering.",
            )


        if current_pos == 0:
            return Result.ok(
                {
                    "status": "Already fully open",
                    "current_position": 0,
                    "current_percentage": 0.0,
                    "message": "Window covering is already at fully open position (0%)",
                }
            )

        result = self._go_to_lift_percentage(0)
        if result.success:

            result.data.update(
                {
                    "command": "UpOrOpen",
                    "command_description": "Move to fully open position (0%)",
                    "previous_position": current_pos,
                    "previous_percentage": current_pos / 100,
                }
            )

        return result

    def _down_or_close(self) -> Result:
        

        current_pos = self.attributes["CurrentPositionLiftPercent100ths"]


        safety_status = self.attributes["SafetyStatus"]
        if safety_status != 0:
            return Result.fail(
                ErrorCode.COMMAND_EXECUTION_ERROR,
                f"Cannot execute DownOrClose command: Safety lockout active (0x{safety_status:04X}). "
                f"Clear safety issues before attempting to close the window covering.",
            )


        if current_pos == 10000:
            return Result.ok(
                {
                    "status": "Already fully closed",
                    "current_position": 10000,
                    "current_percentage": 100.0,
                    "message": "Window covering is already at fully closed position (100%)",
                }
            )

        result = self._go_to_lift_percentage(10000)
        if result.success:

            result.data.update(
                {
                    "command": "DownOrClose",
                    "command_description": "Move to fully closed position (100%)",
                    "previous_position": current_pos,
                    "previous_percentage": current_pos / 100,
                }
            )

        return result

    def _stop_motion(self) -> Result:
        
        current_pos = self.attributes["CurrentPositionLiftPercent100ths"]
        target_pos = self.attributes["TargetPositionLiftPercent100ths"]
        was_moving = self._motion_state["active"]

        if not was_moving:
            return Result.ok(
                {
                    "status": "No motion to stop",
                    "current_position": current_pos,
                    "current_percentage": current_pos / 100,
                    "operational_status": self.attributes["OperationalStatus"],
                    "message": "Window covering is already stopped",
                }
            )


        original_start = self._motion_state.get("start_position", current_pos)
        original_target = self._motion_state.get("target_position", target_pos)


        self._motion_state["active"] = False


        stopped_position = self.attributes["CurrentPositionLiftPercent100ths"]
        self.attributes["TargetPositionLiftPercent100ths"] = stopped_position
        self.attributes["OperationalStatus"] = OperationalStatusBitmap.GLOBAL_NOT_MOVING


        if original_start != original_target:
            completed_distance = abs(stopped_position - original_start)
            total_distance = abs(original_target - original_start)
            completion_percent = (
                (completed_distance / total_distance * 100)
                if total_distance > 0
                else 100
            )
        else:
            completion_percent = 100

        return Result.ok(
            {
                "status": "Motion stopped",
                "stopped_at": stopped_position,
                "stopped_percentage": stopped_position / 100,
                "was_moving_from": original_start,
                "was_moving_from_percentage": original_start / 100,
                "was_moving_to": original_target,
                "was_moving_to_percentage": original_target / 100,
                "motion_completion_percent": round(completion_percent, 1),
                "operational_status": "stopped",
                "message": f"Window covering stopped at {stopped_position/100}% position "
                f"({completion_percent:.1f}% of intended movement completed)",
            }
        )
