from enum import IntEnum
from typing import Any, Optional

from src.simulator.domain.clusters.base import Cluster
from src.simulator.domain.result import ErrorCode, Result


class ModeTag(IntEnum):
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
    DEEP_CLEAN = 0x4000
    VACUUM = 0x4001
    MOP = 0x4002


class RVCCleanModeCluster(Cluster):
    CLUSTER_REVISION = 3

    MODE_VACUUM = 1
    MODE_DEEP_CLEAN = 2
    MODE_MOP = 3

    def __init__(self, feature_map: int = 0):
        super().__init__(cluster_id="RVCCleanMode")
        self.feature_map: int = int(feature_map)
        self.device: Optional[Any] = None

        self.attributes: dict[str, Any] = {
            "SupportedModes": [
                {
                    "Label": "Vacuum",
                    "Mode": self.MODE_VACUUM,
                    "ModeTags": [int(ModeTag.VACUUM)],
                },
                {
                    "Label": "Deep Clean",
                    "Mode": self.MODE_DEEP_CLEAN,
                    "ModeTags": [int(ModeTag.DEEP_CLEAN), int(ModeTag.VACUUM)],
                },
                {
                    "Label": "Mop",
                    "Mode": self.MODE_MOP,
                    "ModeTags": [int(ModeTag.MOP)],
                },
            ],
            "CurrentMode": self.MODE_VACUUM,
            "FeatureMap": self.feature_map,
            "ClusterRevision": self.CLUSTER_REVISION,
        }

        self.readonly_attributes = {
            "SupportedModes",
            "CurrentMode",
            "FeatureMap",
            "ClusterRevision",
        }
        self.commands = {
            "ChangeToMode": self._change_to_mode,
        }

    def set_device_reference(self, device: Any) -> None:
        self.device = device

    def _mode_supported(self, mode_id: int) -> bool:
        supported = self.attributes.get("SupportedModes")
        if not isinstance(supported, list):
            return False
        for entry in supported:
            if not isinstance(entry, dict):
                continue
            raw_mode = entry.get("Mode")
            if isinstance(raw_mode, int) and raw_mode == mode_id:
                return True
        return False

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

        is_idle_mode = run_mode_cluster.is_idle_mode(current_mode)
        return Result.ok(bool(is_idle_mode))

    def _change_to_mode(self, mode: int) -> Result:
        if not isinstance(mode, int):
            return Result.fail(
                ErrorCode.INVALID_ARGUMENT,
                "NewMode must be an integer",
            )

        if not self._mode_supported(mode):
            return Result.fail(
                ErrorCode.UNSUPPORTED_MODE,
                f"Unsupported clean mode: {mode}",
            )

        run_mode_idle_result = self._require_run_mode_idle()
        if not run_mode_idle_result.success:
            return run_mode_idle_result

        if not bool(run_mode_idle_result.data):
            return Result.fail(
                ErrorCode.INVALID_IN_MODE,
                "CleaningInProgress",
                "RVC Clean Mode can only be changed while RVC Run Mode is idle",
            )

        old_mode = self.attributes.get("CurrentMode")
        self.attributes["CurrentMode"] = mode

        if self.device is None:
            return Result.fail(
                ErrorCode.INVALID_STATE,
                "RVC device reference is not set",
            )
        self.device.on_clean_mode_changed(old_mode, mode)

        return Result.ok(
            {
                "old_mode": old_mode,
                "new_mode": mode,
            }
        )
