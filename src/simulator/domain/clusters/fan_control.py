from src.simulator.domain.clusters.base import Cluster
from src.simulator.domain.result import Result, ErrorCode
from enum import IntEnum
from typing import Optional, List, Any


class FanMode(IntEnum):
    OFF = 0
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    ON = 4
    AUTO = 5
    SMART = 6


class FanModeSequence(IntEnum):
    OFF_LOW_MED_HIGH_AUTO = 0
    OFF_LOW_MED_HIGH = 1
    OFF_LOW_HIGH_AUTO = 2
    OFF_LOW_HIGH = 3
    OFF_HIGH_AUTO = 4
    OFF_HIGH = 5


class FanControlCluster(Cluster):
    

    def __init__(
        self,
        fan_mode_sequence: FanModeSequence = FanModeSequence.OFF_LOW_MED_HIGH,
        default_wrap: bool = True,
    ):
        super().__init__(cluster_id="FanControl")


        if fan_mode_sequence not in [e.value for e in FanModeSequence]:
            raise ValueError(f"Invalid FanModeSequence: {fan_mode_sequence}")


        self.attributes = {
            "FanMode": FanMode.OFF,
            "FanModeSequence": fan_mode_sequence,
            "PercentSetting": 0,
            "PercentCurrent": 0,
        }


        self.readonly_attributes = {"FanModeSequence", "PercentCurrent"}


        self.commands = {
            "Step": self._step,
        }


        self._sequence_config = self._get_sequence_config(fan_mode_sequence)

    def write_attribute(self, attribute_id: str, value: Any) -> Result:
        
        if attribute_id == "PercentSetting":

            if value is None:
                return Result.ok(
                    {
                        "cluster": "FanControl",
                        "attribute": "PercentSetting",
                        "unchanged": True,
                    }
                )
            try:
                new_percent = int(value)
            except Exception:
                return Result.fail(
                    ErrorCode.VALIDATION_ERROR,
                    "Invalid percentage value",
                    f"PercentSetting expects 0-100 integer, got {value}",
                )
            return self._update_percent_setting(new_percent)

        if attribute_id == "FanMode":
            return self._apply_fan_mode(value)

        return super().write_attribute(attribute_id, value)

    def _get_sequence_config(self, sequence: int) -> dict:
        
        configs = {
            FanModeSequence.OFF_LOW_MED_HIGH_AUTO: {
                "modes": [
                    FanMode.OFF,
                    FanMode.LOW,
                    FanMode.MEDIUM,
                    FanMode.HIGH,
                    FanMode.AUTO,
                ],
                "percent_mapping": {
                    FanMode.OFF: 0,
                    FanMode.LOW: 33,
                    FanMode.MEDIUM: 66,
                    FanMode.HIGH: 100,
                    FanMode.AUTO: None,
                },
            },
            FanModeSequence.OFF_LOW_MED_HIGH: {
                "modes": [FanMode.OFF, FanMode.LOW, FanMode.MEDIUM, FanMode.HIGH],
                "percent_mapping": {
                    FanMode.OFF: 0,
                    FanMode.LOW: 33,
                    FanMode.MEDIUM: 66,
                    FanMode.HIGH: 100,
                },
            },
            FanModeSequence.OFF_LOW_HIGH_AUTO: {
                "modes": [FanMode.OFF, FanMode.LOW, FanMode.HIGH, FanMode.AUTO],
                "percent_mapping": {
                    FanMode.OFF: 0,
                    FanMode.LOW: 50,
                    FanMode.HIGH: 100,
                    FanMode.AUTO: None,
                },
            },
            FanModeSequence.OFF_LOW_HIGH: {
                "modes": [FanMode.OFF, FanMode.LOW, FanMode.HIGH],
                "percent_mapping": {FanMode.OFF: 0, FanMode.LOW: 50, FanMode.HIGH: 100},
            },
            FanModeSequence.OFF_HIGH_AUTO: {
                "modes": [FanMode.OFF, FanMode.HIGH, FanMode.AUTO],
                "percent_mapping": {
                    FanMode.OFF: 0,
                    FanMode.HIGH: 100,
                    FanMode.AUTO: None,
                },
            },
            FanModeSequence.OFF_HIGH: {
                "modes": [FanMode.OFF, FanMode.HIGH],
                "percent_mapping": {FanMode.OFF: 0, FanMode.HIGH: 100},
            },
        }
        return configs.get(sequence, configs[FanModeSequence.OFF_LOW_MED_HIGH])

    def _get_step_values(self, lowest_off: bool = True) -> List[int]:
        
        config = self._sequence_config
        step_values = []

        for mode in config["modes"]:
            percent = config["percent_mapping"][mode]
            if percent is not None:
                step_values.append(percent)


        if not lowest_off and len(step_values) > 1:

            non_zero_values = [v for v in step_values if v > 0]
            if non_zero_values:
                min_non_zero = min(non_zero_values)
                step_values = [1 if v == min_non_zero else v for v in step_values]

        return sorted(step_values)

    def _step(
        self,
        Direction: int,
        Wrap: Optional[bool] = None,
        LowestOff: Optional[bool] = None,
    ) -> Result:
        

        if not isinstance(Direction, int):
            return Result.fail(
                ErrorCode.COMMAND_EXECUTION_ERROR,
                f"Invalid argument type for Step command",
                f"Expected 'Direction' as int, got {type(Direction).__name__}. "
                f"Usage: Step(Direction=0) for up or Step(Direction=1) for down",
            )

        if Wrap is not None and not isinstance(Wrap, bool):
            return Result.fail(
                ErrorCode.COMMAND_EXECUTION_ERROR,
                f"Invalid argument type for Step command",
                f"Expected 'Wrap' as bool, got {type(Wrap).__name__}. "
                f"Usage: Step(Direction=0, Wrap=True)",
            )

        if LowestOff is not None and not isinstance(LowestOff, bool):
            return Result.fail(
                ErrorCode.COMMAND_EXECUTION_ERROR,
                f"Invalid argument type for Step command",
                f"Expected 'LowestOff' as bool, got {type(LowestOff).__name__}. "
                f"Usage: Step(Direction=0, LowestOff=True)",
            )


        if Direction not in [0, 1]:
            return Result.fail(
                ErrorCode.VALIDATION_ERROR,
                "Invalid Direction",
                f"Direction must be 0(Increase/Up) or 1(Decrease/Down), got {Direction}. "
                f"Usage: Step(Direction=0) for up",
            )


        if Wrap is None:

            Wrap = True
        if LowestOff is None:
            LowestOff = True


        step_values = self._get_step_values(LowestOff)
        current_percent = self.attributes["PercentSetting"]


        if current_percent == 0:
            if Direction == 0:
                new_percent = step_values[1] if len(step_values) > 1 else step_values[0]
            else:
                new_percent = step_values[-1] if Wrap else step_values[0]
        else:

            current_index = self._find_closest_step_index(current_percent, step_values)


            if Direction == 0:
                if current_index < len(step_values) - 1:
                    new_percent = step_values[current_index + 1]
                elif Wrap:
                    new_percent = step_values[0]
                else:
                    new_percent = current_percent
            else:
                if current_index > 0:
                    new_percent = step_values[current_index - 1]
                elif Wrap:
                    new_percent = step_values[-1]
                else:
                    new_percent = current_percent


        return self._update_percent_setting(new_percent)

    def _find_closest_step_index(self, percent: int, step_values: List[int]) -> int:
        
        if not step_values:
            return 0

        closest_index = 0
        min_diff = abs(step_values[0] - percent)

        for i, step_val in enumerate(step_values):
            diff = abs(step_val - percent)
            if diff < min_diff:
                min_diff = diff
                closest_index = i

        return closest_index

    def _update_percent_setting(self, new_percent: int) -> Result:
        

        if new_percent < 0 or new_percent > 100:
            return Result.fail(ErrorCode.VALIDATION_ERROR, "Invalid percentage range")


        self.attributes["PercentSetting"] = new_percent


        self.attributes["PercentCurrent"] = new_percent


        new_fan_mode = self._percent_to_fan_mode(new_percent)
        if new_fan_mode is not None:
            self.attributes["FanMode"] = new_fan_mode

        return Result.ok(
            {
                "cluster": "FanControl",
                "attribute": "PercentSetting",
                "new_value": new_percent,
            }
        )

    def _percent_to_fan_mode(self, percent: int) -> Optional[int]:
        
        config = self._sequence_config


        for mode, mode_percent in config["percent_mapping"].items():
            if mode_percent == percent:
                return mode


        if percent == 0:
            return FanMode.OFF


        modes = config["modes"]
        percent_mapping = config["percent_mapping"]


        mode_percents = [
            (mode, pct)
            for mode, pct in percent_mapping.items()
            if pct is not None and mode in modes
        ]
        mode_percents.sort(key=lambda x: x[1])


        for i, (mode, mode_pct) in enumerate(mode_percents):
            if percent <= mode_pct:
                return mode


        if mode_percents:
            return mode_percents[-1][0]

        return FanMode.OFF

    def _supports_auto(self) -> bool:
        
        return FanMode.AUTO in self._sequence_config.get("modes", [])

    def _apply_fan_mode(self, requested_mode: int) -> Result:
        

        try:
            mode = FanMode(requested_mode)
        except Exception:
            return Result.fail(
                ErrorCode.VALIDATION_ERROR,
                "Invalid FanMode",
                f"Requested FanMode: {requested_mode}",
            )


        if mode == FanMode.ON:
            mode = FanMode.HIGH
        elif mode == FanMode.SMART:
            mode = FanMode.AUTO if self._supports_auto() else FanMode.HIGH

        supported_modes = self._sequence_config["modes"]
        if mode not in supported_modes:
            return Result.fail(
                ErrorCode.VALIDATION_ERROR,
                "Unsupported FanMode for current sequence",
                f"Supported: {[m.name for m in supported_modes]}, requested: {mode.name}",
            )


        if mode == FanMode.OFF:
            self.attributes["FanMode"] = FanMode.OFF
            self.attributes["PercentSetting"] = 0
            self.attributes["PercentCurrent"] = 0
            return Result.ok(
                {
                    "cluster": "FanControl",
                    "attribute": "FanMode",
                    "new_value": FanMode.OFF,
                }
            )


        if mode == FanMode.AUTO:
            self.attributes["FanMode"] = FanMode.AUTO
            self.attributes["PercentSetting"] = None
            return Result.ok(
                {
                    "cluster": "FanControl",
                    "attribute": "FanMode",
                    "new_value": FanMode.AUTO,
                }
            )


        percent_mapping = self._sequence_config["percent_mapping"]
        mapped_percent = percent_mapping.get(mode)
        if mapped_percent is None:

            return Result.fail(
                ErrorCode.INTERNAL_ERROR,
                "No percent mapping for mode",
                f"Mode {mode.name} has no percent mapping in current sequence",
            )

        result = self._update_percent_setting(mapped_percent)
        if result.success:

            self.attributes["FanMode"] = mode
        return result

    def __str__(self) -> str:
        
        return (
            f"FanControlCluster("
            f"Mode={self.attributes['FanMode']}, "
            f"Sequence={self.attributes['FanModeSequence']}, "
            f"PercentSetting={self.attributes['PercentSetting']}, "
            f"PercentCurrent={self.attributes['PercentCurrent']})"
        )
