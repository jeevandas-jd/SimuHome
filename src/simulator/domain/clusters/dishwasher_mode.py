from src.simulator.domain.clusters.base import Cluster
from src.simulator.domain.result import Result, ResultBuilder, ErrorCode
from enum import IntEnum
from typing import Any


class DishwasherModeTag(IntEnum):
    

    AUTO = 0x0000
    QUICK = 0x0001
    QUIET = 0x0002
    LOW_NOISE = 0x0003
    LOW_ENERGY = 0x0004
    VACATION = 0x0005
    MIN = 0x0006
    MAX = 0x0007
    NIGHT = 0x0008
    DAY = 0x0009
    NORMAL = 0x4000
    HEAVY = 0x4001
    LIGHT = 0x4002


class DishwasherMode(IntEnum):
    

    NORMAL = 0
    HEAVY_DUTY = 1
    LIGHT_WASH = 2
    QUICK_WASH = 3
    LOW_ENERGY = 4
    SILENT = 5


class DishwasherModeCluster(Cluster):
    

    def __init__(self, features: int = 0):
        super().__init__(cluster_id="DishwasherMode")

        self.features = features
        self.device = None


        self.attributes = {
            "SupportedModes": [
                {
                    "label": "Normal",
                    "mode": DishwasherMode.NORMAL,
                    "ModeTags": [DishwasherModeTag.NORMAL],
                },
                {
                    "label": "Heavy Duty",
                    "mode": DishwasherMode.HEAVY_DUTY,
                    "ModeTags": [DishwasherModeTag.HEAVY],
                },
                {
                    "label": "Light Wash",
                    "mode": DishwasherMode.LIGHT_WASH,
                    "ModeTags": [DishwasherModeTag.LIGHT],
                },
                {
                    "label": "Quick Wash",
                    "mode": DishwasherMode.QUICK_WASH,
                    "ModeTags": [DishwasherModeTag.QUICK],
                },
                {
                    "label": "Low Energy",
                    "mode": DishwasherMode.LOW_ENERGY,
                    "ModeTags": [DishwasherModeTag.LOW_ENERGY],
                },
                {
                    "label": "Silent",
                    "mode": DishwasherMode.SILENT,
                    "ModeTags": [DishwasherModeTag.QUIET, DishwasherModeTag.LOW_NOISE],
                },
            ],
            "CurrentMode": DishwasherMode.NORMAL,
        }


        self.readonly_attributes = {"SupportedModes"}


        self.commands = {
            "ChangeToMode": self._change_to_mode,
        }

        self.mode_change_callback = None

    def set_device_reference(self, device):
        
        self.device = device

    def set_mode_change_callback(self, callback):
        
        self.mode_change_callback = callback

    def _is_device_running(self) -> bool:
        
        if not self.device:
            return False

        try:
            from src.simulator.domain.clusters.operational_state import (
                OperationalStateEnum,
            )

            operational_state = self.device.get_attribute(
                1, "OperationalState", "OperationalState"
            )
            return operational_state == OperationalStateEnum.RUNNING
        except Exception as error:
            raise RuntimeError(
                "Failed to read OperationalState for dishwasher mode"
            ) from error

    def _change_to_mode(self, new_mode: int) -> Result:
        
        try:
            device_running = self._is_device_running()
        except RuntimeError as error:
            return ResultBuilder.internal_error(error)

        if device_running:
            return Result.fail(
                ErrorCode.INVALID_STATE,
                "Cannot change mode while device is running",
                "Stop the device before changing mode",
            )

        supported_modes_raw = self.attributes.get("SupportedModes")
        if not isinstance(supported_modes_raw, list):
            return ResultBuilder.internal_error(
                RuntimeError("SupportedModes attribute is malformed")
            )
        supported_modes: list[dict[str, Any]] = supported_modes_raw

        valid_modes: list[int] = []
        for mode in supported_modes:
            raw_mode = mode.get("mode")
            if isinstance(raw_mode, IntEnum):
                valid_modes.append(int(raw_mode))
            elif isinstance(raw_mode, int):
                valid_modes.append(raw_mode)
        if new_mode not in valid_modes:
            return Result.fail(
                ErrorCode.INVALID_ARGUMENT,
                f"Invalid mode: {new_mode}",
                f"Supported modes: {valid_modes}",
            )

        old_mode_raw = self.attributes.get("CurrentMode")
        if isinstance(old_mode_raw, IntEnum):
            old_mode_value = int(old_mode_raw)
        elif isinstance(old_mode_raw, int):
            old_mode_value = old_mode_raw
        else:
            return ResultBuilder.internal_error(
                RuntimeError("CurrentMode attribute is malformed")
            )
        self.attributes["CurrentMode"] = DishwasherMode(new_mode)

        if self.mode_change_callback:
            self.mode_change_callback(new_mode)

        mode_label = str(new_mode)
        for mode in supported_modes:
            raw_mode = mode.get("mode")
            if isinstance(raw_mode, IntEnum):
                mode_value = int(raw_mode)
            elif isinstance(raw_mode, int):
                mode_value = raw_mode
            else:
                continue

            if mode_value == new_mode:
                raw_label = mode.get("label")
                if isinstance(raw_label, str) and raw_label.strip():
                    mode_label = raw_label
                break

        return Result.ok(
            {
                "old_mode": old_mode_value,
                "new_mode": new_mode,
                "mode_label": mode_label,
            }
        )

    def get_current_mode_label(self) -> str:
        
        current_mode_raw = self.attributes.get("CurrentMode")
        if isinstance(current_mode_raw, IntEnum):
            current_mode = int(current_mode_raw)
        elif isinstance(current_mode_raw, int):
            current_mode = current_mode_raw
        else:
            return "Unknown"

        supported_modes_raw = self.attributes.get("SupportedModes")
        if not isinstance(supported_modes_raw, list):
            return "Unknown"

        for mode in supported_modes_raw:
            if not isinstance(mode, dict):
                continue

            raw_mode = mode.get("mode")
            if isinstance(raw_mode, IntEnum):
                mode_value = int(raw_mode)
            elif isinstance(raw_mode, int):
                mode_value = raw_mode
            else:
                continue

            if mode_value == current_mode:
                label = mode.get("label")
                if isinstance(label, str):
                    return label

        return "Unknown"
