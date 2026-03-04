from src.simulator.domain.clusters.base import Cluster
from src.simulator.domain.result import Result, ErrorCode
from enum import IntEnum
from typing import Optional


class DishwasherAlarmBitmap(IntEnum):
    

    INFLOW_ERROR = 1 << 0
    DRAIN_ERROR = 1 << 1
    DOOR_ERROR = 1 << 2
    TEMP_TOO_LOW = 1 << 3
    TEMP_TOO_HIGH = 1 << 4
    WATER_LEVEL_ERROR = 1 << 5


class DishwasherAlarmCluster(Cluster):
    

    def __init__(self):
        super().__init__(cluster_id="DishwasherAlarm")

        self.attributes = {
            "Mask": 0,
            "Latch": 0,
            "State": 0,
            "Supported": 0x3F,
        }

        self.commands = {
            "Reset": self._reset_alarms,
            "ModifyEnabledAlarms": self._modify_enabled_alarms,
        }

        self.readonly_attributes = {"State", "Latch", "Supported"}

        self._initialize_supported_alarms()

    def _initialize_supported_alarms(self):
        supported_mask = (
            DishwasherAlarmBitmap.INFLOW_ERROR
            | DishwasherAlarmBitmap.DRAIN_ERROR
            | DishwasherAlarmBitmap.DOOR_ERROR
            | DishwasherAlarmBitmap.TEMP_TOO_LOW
            | DishwasherAlarmBitmap.TEMP_TOO_HIGH
            | DishwasherAlarmBitmap.WATER_LEVEL_ERROR
        )
        self.attributes["Supported"] = supported_mask

    def _reset_alarms(self, alarms_to_reset: Optional[int] = None) -> Result:
        if alarms_to_reset is None:
            alarms_to_reset = self.attributes["Latch"]

        if not isinstance(alarms_to_reset, int):
            return Result.fail(
                error_code=ErrorCode.INVALID_ARGUMENT,
                error_message="Alarms to reset must be an integer bitmap",
                error_detail=f"Provided value: {alarms_to_reset}",
            )

        unsupported_alarms = alarms_to_reset & ~self.attributes["Supported"]
        if unsupported_alarms:
            return Result.fail(
                error_code=ErrorCode.INVALID_ARGUMENT,
                error_message="Cannot reset unsupported alarms",
                error_detail=f"Unsupported alarm bits: {bin(unsupported_alarms)}",
            )

        old_latch = self.attributes["Latch"]


        self.attributes["Latch"] &= ~alarms_to_reset

        return Result.ok(
            {
                "cluster": self.cluster_id,
                "command": "Reset",
                "reset_alarms": alarms_to_reset,
                "old_latch": old_latch,
                "new_latch": self.attributes["Latch"],
            }
        )

    def _modify_enabled_alarms(self, mask: int) -> Result:
        if not isinstance(mask, int):
            return Result.fail(
                error_code=ErrorCode.INVALID_ARGUMENT,
                error_message="Mask must be an integer",
                error_detail=f"Provided mask: {mask}",
            )

        unsupported_alarms = mask & ~self.attributes["Supported"]
        if unsupported_alarms:
            return Result.fail(
                error_code=ErrorCode.INVALID_ARGUMENT,
                error_message="Cannot enable unsupported alarms",
                error_detail=f"Unsupported alarm bits: {bin(unsupported_alarms)}",
            )

        old_mask = self.attributes["Mask"]
        self.attributes["Mask"] = mask

        return Result.ok(
            {
                "cluster": self.cluster_id,
                "command": "ModifyEnabledAlarms",
                "old_mask": old_mask,
                "new_mask": mask,
            }
        )

    def trigger_alarm(self, alarm_bitmap: int) -> Result:
        
        if not isinstance(alarm_bitmap, int):
            return Result.fail(
                error_code=ErrorCode.INVALID_ARGUMENT,
                error_message="Alarm bitmap must be an integer",
                error_detail=f"Provided value: {alarm_bitmap}",
            )

        unsupported_alarms = alarm_bitmap & ~self.attributes["Supported"]
        if unsupported_alarms:
            return Result.fail(
                error_code=ErrorCode.INVALID_ARGUMENT,
                error_message="Cannot trigger unsupported alarms",
                error_detail=f"Unsupported alarm bits: {bin(unsupported_alarms)}",
            )

        old_state = self.attributes["State"]
        old_latch = self.attributes["Latch"]

        self.attributes["State"] |= alarm_bitmap

        enabled_triggered_alarms = alarm_bitmap & self.attributes["Mask"]
        self.attributes["Latch"] |= enabled_triggered_alarms

        triggered_alarms = []
        for alarm_bit in DishwasherAlarmBitmap:
            if alarm_bitmap & alarm_bit:
                triggered_alarms.append(
                    {
                        "alarm_bit": alarm_bit,
                        "alarm_name": alarm_bit.name,
                        "was_enabled": bool(self.attributes["Mask"] & alarm_bit),
                        "is_latched": bool(self.attributes["Latch"] & alarm_bit),
                    }
                )

        return Result.ok(
            {
                "cluster": self.cluster_id,
                "command": "TriggerAlarm",
                "triggered_alarms": triggered_alarms,
                "old_state": old_state,
                "new_state": self.attributes["State"],
                "old_latch": old_latch,
                "new_latch": self.attributes["Latch"],
            }
        )

    def clear_alarm(self, alarm_bitmap: int) -> Result:
        
        if not isinstance(alarm_bitmap, int):
            return Result.fail(
                error_code=ErrorCode.INVALID_ARGUMENT,
                error_message="Alarm bitmap must be an integer",
                error_detail=f"Provided value: {alarm_bitmap}",
            )

        old_state = self.attributes["State"]

        self.attributes["State"] &= ~alarm_bitmap

        cleared_alarms = []
        for alarm_bit in DishwasherAlarmBitmap:
            if alarm_bitmap & alarm_bit and old_state & alarm_bit:
                cleared_alarms.append(
                    {
                        "alarm_bit": alarm_bit,
                        "alarm_name": alarm_bit.name,
                        "remains_latched": bool(self.attributes["Latch"] & alarm_bit),
                    }
                )

        return Result.ok(
            {
                "cluster": self.cluster_id,
                "command": "ClearAlarm",
                "cleared_alarms": cleared_alarms,
                "old_state": old_state,
                "new_state": self.attributes["State"],
            }
        )
