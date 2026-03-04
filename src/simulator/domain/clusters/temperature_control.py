from enum import IntEnum
from src.simulator.domain.clusters.base import Cluster
from src.simulator.domain.result import Result, ErrorCode
from typing import Optional


class FeatureFlag(IntEnum):
    TN = 0x01
    TL = 0x02
    STEP = 0x04


class TemperatureControlCluster(Cluster):
    

    def __init__(self, features=FeatureFlag.TN):
        super().__init__(cluster_id="TemperatureControl")

        self.features = features


        self.attributes = {}


        if features & FeatureFlag.TN:
            self.attributes.update(
                {
                    "TemperatureSetpoint": 2000,
                    "MinTemperature": 500,
                    "MaxTemperature": 9500,
                }
            )


            if features & FeatureFlag.STEP:
                self.attributes["Step"] = 100


        if features & FeatureFlag.TL:
            self.attributes.update(
                {
                    "SelectedTemperatureLevel": 0,
                    "SupportedTemperatureLevels": [
                        "Cold",
                        "Warm",
                        "Hot",
                    ],
                }
            )
        self.readonly_attributes = {
            "TemperatureSetpoint",
            "MinTemperature",
            "MaxTemperature",
            "Step",
            "SelectedTemperatureLevel",
            "SupportedTemperatureLevels",
        }

        self.commands = {
            "SetTemperature": self._set_temperature,
        }

    def _set_temperature(
        self,
        target_temperature: Optional[int] = None,
        target_temperature_level: Optional[int] = None,
    ) -> Result:
        

        if target_temperature is not None:
            if not (self.features & FeatureFlag.TN):
                return Result.fail(
                    error_code=ErrorCode.CONSTRAINT_ERROR,
                    error_message="TN feature not supported",
                    error_detail="Device does not support Temperature Number feature",
                )

            min_temp = self.attributes["MinTemperature"]
            max_temp = self.attributes["MaxTemperature"]


            if target_temperature < min_temp or target_temperature > max_temp:
                return Result.fail(
                    error_code=ErrorCode.CONSTRAINT_ERROR,
                    error_message=f"Temperature {target_temperature/100:.1f}°C is out of range",
                    error_detail=f"Valid range: {min_temp/100:.1f}°C to {max_temp/100:.1f}°C",
                )


            if "Step" in self.attributes:
                step = self.attributes["Step"]
                if (target_temperature - min_temp) % step != 0:
                    return Result.fail(
                        error_code=ErrorCode.CONSTRAINT_ERROR,
                        error_message=f"Temperature must be in steps of {step/100:.1f}°C",
                        error_detail=f"Valid temperatures: {min_temp/100:.1f}°C + n×{step/100:.1f}°C",
                    )


            current_state = getattr(self, "_device_state", "ready")
            if current_state == "operating" and hasattr(
                self, "_allow_temp_change_during_operation"
            ):
                if not self._allow_temp_change_during_operation:
                    return Result.fail(
                        error_code=ErrorCode.INVALID_STATE,
                        error_message="Cannot change temperature during operation",
                        error_detail="Device is currently operating and cannot accept temperature changes",
                    )

            old_setpoint = self.attributes["TemperatureSetpoint"]
            self.attributes["TemperatureSetpoint"] = target_temperature

            return Result.ok(
                {
                    "cluster": self.cluster_id,
                    "command": "SetTemperature",
                    "status": "SUCCESS",
                    "target_temperature": target_temperature,
                    "old_setpoint": old_setpoint,
                    "new_setpoint": target_temperature,
                    "temperature_celsius": target_temperature / 100.0,
                }
            )


        if target_temperature_level is not None:
            if not (self.features & FeatureFlag.TL):
                return Result.fail(
                    error_code=ErrorCode.CONSTRAINT_ERROR,
                    error_message="TL feature not supported",
                    error_detail="Device does not support Temperature Level feature",
                )

            supported_levels = self.attributes["SupportedTemperatureLevels"]


            if target_temperature_level < 0 or target_temperature_level >= len(
                supported_levels
            ):
                return Result.fail(
                    error_code=ErrorCode.CONSTRAINT_ERROR,
                    error_message=f"Temperature level {target_temperature_level} is out of range",
                    error_detail=f"Valid range: 0 to {len(supported_levels) - 1}",
                )


            current_state = getattr(self, "_device_state", "ready")
            if current_state == "operating" and hasattr(
                self, "_allow_temp_change_during_operation"
            ):
                if not self._allow_temp_change_during_operation:
                    return Result.fail(
                        error_code=ErrorCode.INVALID_STATE,
                        error_message="Cannot change temperature level during operation",
                        error_detail="Device is currently operating and cannot accept temperature changes",
                    )

            old_level = self.attributes["SelectedTemperatureLevel"]
            self.attributes["SelectedTemperatureLevel"] = target_temperature_level

            return Result.ok(
                {
                    "cluster": self.cluster_id,
                    "command": "SetTemperature",
                    "status": "SUCCESS",
                    "target_temperature_level": target_temperature_level,
                    "old_level": old_level,
                    "new_level": target_temperature_level,
                    "level_name": supported_levels[target_temperature_level],
                }
            )


        return Result.fail(
            error_code=ErrorCode.INVALID_ARGUMENT,
            error_message="No valid temperature target provided",
            error_detail="Must provide either target_temperature (TN feature) or target_temperature_level (TL feature)",
        )
