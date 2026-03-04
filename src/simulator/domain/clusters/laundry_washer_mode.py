from src.simulator.domain.clusters.base import Cluster
from src.simulator.domain.result import Result, ResultBuilder, ErrorCode
from enum import IntEnum
from typing import Any


class ModeTag(IntEnum):
    QUICK = 0x0001
    NORMAL = 0x4000
    DELICATE = 0x4001
    HEAVY = 0x4002
    WHITES = 0x4003


class LaundryWasherMode(IntEnum):
    NORMAL = 0
    DELICATE = 1
    HEAVY = 2
    WHITES = 3
    QUICK_NORMAL = 4
    HEAVY_WHITES = 5


class LaundryWasherModeCluster(Cluster):
    

    FEATURE_DEPONOFF = 0x01

    def __init__(self, features: int = 0):
        super().__init__(cluster_id="LaundryWasherMode")

        self.features = features
        self.device = None


        self.attributes = {
            "SupportedModes": [
                {
                    "label": "Normal",
                    "mode": LaundryWasherMode.NORMAL,
                    "ModeTags": [ModeTag.NORMAL],
                },
                {
                    "label": "Delicate",
                    "mode": LaundryWasherMode.DELICATE,
                    "ModeTags": [ModeTag.DELICATE],
                },
                {
                    "label": "Heavy",
                    "mode": LaundryWasherMode.HEAVY,
                    "ModeTags": [ModeTag.HEAVY],
                },
                {
                    "label": "Whites",
                    "mode": LaundryWasherMode.WHITES,
                    "ModeTags": [ModeTag.WHITES],
                },
                {
                    "label": "Quick Normal",
                    "mode": LaundryWasherMode.QUICK_NORMAL,
                    "ModeTags": [
                        ModeTag.QUICK,
                        ModeTag.NORMAL,
                    ],
                },
                {
                    "label": "Heavy Whites",
                    "mode": LaundryWasherMode.HEAVY_WHITES,
                    "ModeTags": [
                        ModeTag.HEAVY,
                        ModeTag.WHITES,
                    ],
                },
            ],
            "CurrentMode": LaundryWasherMode.NORMAL,
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
            from src.simulator.domain.clusters.operational_state import OperationalStateEnum

            operational_state = self.device.get_attribute(
                1, "OperationalState", "OperationalState"
            )
            return operational_state == OperationalStateEnum.RUNNING
        except Exception as error:
            raise RuntimeError(
                "Failed to read OperationalState for laundry washer mode"
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
        self.attributes["CurrentMode"] = LaundryWasherMode(new_mode)


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
