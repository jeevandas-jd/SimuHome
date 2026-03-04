from enum import IntEnum
from src.simulator.domain.clusters.base import Cluster
from src.simulator.domain.result import Result, ErrorCode
from typing import Any


class SystemMode(IntEnum):
    OFF = 0x00
    AUTO = 0x01
    COOL = 0x03
    HEAT = 0x04


class ControlSequenceOfOperationEnum(IntEnum):
    COOLING_ONLY = 0x00
    COOLING_WITH_REHEAT = 0x01
    HEATING_ONLY = 0x02
    HEATING_WITH_REHEAT = 0x03
    COOLING_AND_HEATING = 0x04
    COOLING_AND_HEATING_WITH_REHEAT = 0x05


class ThermostatCluster(Cluster):
    

    def __init__(self):
        super().__init__(cluster_id="Thermostat")


        self.attributes = {
            "LocalTemperature": 2500,
            "OccupiedCoolingSetpoint": 2000,
            "OccupiedHeatingSetpoint": 2800,
            "ControlSequenceOfOperation": ControlSequenceOfOperationEnum.COOLING_AND_HEATING,
            "SystemMode": SystemMode.OFF,
        }


        self.readonly_attributes = {"LocalTemperature"}


        self.commands = {
            "SetpointRaiseLower": self._setpoint_raise_lower,
        }

    def write_attribute(self, attribute_id: str, value: Any) -> Result:
        

        if attribute_id in ("OccupiedHeatingSetpoint", "OccupiedCoolingSetpoint"):
            if not isinstance(value, int):
                return Result.fail(
                    ErrorCode.VALIDATION_ERROR,
                    f"{attribute_id} must be int (0.01°C units)",
                )

            if not (700 <= value <= 3200):
                return Result.fail(
                    ErrorCode.VALIDATION_ERROR,
                    f"{attribute_id} out of range",
                    "Valid range: 700-3200 (0.01°C)",
                )


            if attribute_id == "OccupiedHeatingSetpoint":
                cooling = self.attributes.get("OccupiedCoolingSetpoint", 2000)
                if cooling - value < 25:
                    return Result.fail(
                        ErrorCode.VALIDATION_ERROR,
                        "Deadband violation",
                        "Cooling - Heating must be >= 0.25°C (25)",
                    )
            else:
                heating = self.attributes.get("OccupiedHeatingSetpoint", 2800)
                if value - heating < 25:
                    return Result.fail(
                        ErrorCode.VALIDATION_ERROR,
                        "Deadband violation",
                        "Cooling - Heating must be >= 0.25°C (25)",
                    )

        return super().write_attribute(attribute_id, value)

    def _setpoint_raise_lower(self, Mode, Amount) -> Result:
        

        if not isinstance(Mode, int):
            return Result.fail(
                ErrorCode.COMMAND_EXECUTION_ERROR,
                f"Invalid argument type for SetpointRaiseLower command",
                f"Expected 'Mode' as int, got {type(Mode).__name__}. "
                f"Usage: SetpointRaiseLower(Mode=0, Amount=5) where Mode: 0=Heat, 1=Cool, 2=Both",
            )

        if not isinstance(Amount, int):
            return Result.fail(
                ErrorCode.COMMAND_EXECUTION_ERROR,
                f"Invalid argument type for SetpointRaiseLower command",
                f"Expected 'Amount' as int, got {type(Amount).__name__}. "
                f"Usage: SetpointRaiseLower(Mode=0, Amount=5) where Amount is in 0.1°C units",
            )


        if Mode not in [0, 1, 2]:
            return Result.fail(
                ErrorCode.VALIDATION_ERROR,
                "Invalid Mode",
                f"Mode must be 0(Heat), 1(Cool), or 2(Both), got {Mode}. "
                f"Usage: SetpointRaiseLower(Mode=0, Amount=5)",
            )


        if Amount < -500 or Amount > 500:
            return Result.fail(
                ErrorCode.VALIDATION_ERROR,
                "Invalid Amount",
                f"Amount must be in range -500 to 500 (±50°C), got {Amount}. "
                f"Usage: SetpointRaiseLower(Mode=0, Amount=5) for 0.5°C adjustment",
            )


        if Mode == 2:
            return Result.fail(ErrorCode.VALIDATION_ERROR, "Mode=Both is not supported")

        if Mode == 0:
            current = self.attributes["OccupiedHeatingSetpoint"]
            new_value = max(700, min(3000, current + (Amount * 10)))
            self.attributes["OccupiedHeatingSetpoint"] = new_value
            return Result.ok()

        elif Mode == 1:
            current = self.attributes["OccupiedCoolingSetpoint"]
            new_value = max(1600, min(3200, current + (Amount * 10)))
            self.attributes["OccupiedCoolingSetpoint"] = new_value
            return Result.ok()

        elif Mode == 2:
            heat_current = self.attributes["OccupiedHeatingSetpoint"]
            cool_current = self.attributes["OccupiedCoolingSetpoint"]

            new_heat = max(700, min(3000, heat_current + (Amount * 10)))
            new_cool = max(1600, min(3200, cool_current + (Amount * 10)))


            if new_cool - new_heat >= 25:
                self.attributes["OccupiedHeatingSetpoint"] = new_heat
                self.attributes["OccupiedCoolingSetpoint"] = new_cool
                return Result.ok()

        return Result.fail(
            ErrorCode.VALIDATION_ERROR, "Invalid parameters for SetpointRaiseLower"
        )
