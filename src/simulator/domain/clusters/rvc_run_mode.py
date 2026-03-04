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
    IDLE = 0x4000
    CLEANING = 0x4001
    MAPPING = 0x4002


class RVCOperationalStateCode(IntEnum):
    STOPPED = 0x00
    RUNNING = 0x01
    PAUSED = 0x02
    ERROR = 0x03
    SEEKING_CHARGER = 0x40
    CHARGING = 0x41
    DOCKED = 0x42


class RVCRunModeCluster(Cluster):
    CLUSTER_REVISION = 3
    FEATURE_DIRECT_MODE_CHANGE = 1 << 20

    MODE_IDLE = 1
    MODE_CLEANING = 2
    MODE_MAPPING = 3

    def __init__(self, feature_map: int = 0):
        super().__init__(cluster_id="RVCRunMode")
        self.feature_map: int = int(feature_map)
        self.device: Optional[Any] = None

        self.attributes: dict[str, Any] = {
            "SupportedModes": [
                {
                    "Label": "Idle",
                    "Mode": self.MODE_IDLE,
                    "ModeTags": [int(ModeTag.IDLE)],
                },
                {
                    "Label": "Vacuum",
                    "Mode": self.MODE_CLEANING,
                    "ModeTags": [int(ModeTag.CLEANING)],
                },
                {
                    "Label": "Mapping",
                    "Mode": self.MODE_MAPPING,
                    "ModeTags": [int(ModeTag.MAPPING)],
                },
            ],
            "CurrentMode": self.MODE_IDLE,
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

    def _find_mode_entry(self, mode_id: int) -> Optional[dict[str, Any]]:
        supported = self.attributes.get("SupportedModes")
        if not isinstance(supported, list):
            return None
        for entry in supported:
            if not isinstance(entry, dict):
                continue
            raw_mode = entry.get("Mode")
            if isinstance(raw_mode, int) and raw_mode == mode_id:
                return entry
        return None

    def _mode_has_tag(self, mode_id: int, mode_tag: ModeTag) -> bool:
        mode_entry = self._find_mode_entry(mode_id)
        if not mode_entry:
            return False
        tags = mode_entry.get("ModeTags")
        if not isinstance(tags, list):
            return False
        try:
            normalized = {int(tag) for tag in tags if isinstance(tag, int)}
        except Exception:
            return False
        return int(mode_tag) in normalized

    def mode_has_tag(self, mode_id: int, mode_tag: ModeTag) -> bool:
        return self._mode_has_tag(mode_id, mode_tag)

    def is_idle_mode(self, mode_id: int) -> bool:
        return self._mode_has_tag(mode_id, ModeTag.IDLE)

    def _require_operational_state(self) -> Result:
        if self.device is None:
            return Result.fail(
                ErrorCode.INVALID_STATE,
                "RVC device reference is not set",
            )

        operational_state_cluster = getattr(self.device, "operational_state", None)
        if operational_state_cluster is None:
            return Result.fail(
                ErrorCode.INVALID_STATE,
                "RVCOperationalState cluster is not available",
            )

        state_value = operational_state_cluster.attributes.get("OperationalState")
        if not isinstance(state_value, int):
            return Result.fail(
                ErrorCode.INVALID_STATE,
                "OperationalState attribute is malformed",
            )

        return Result.ok(int(state_value))

    def _change_to_mode(self, new_mode: int) -> Result:
        if not isinstance(new_mode, int):
            return Result.fail(
                ErrorCode.INVALID_ARGUMENT,
                "NewMode must be an integer",
            )

        if self._find_mode_entry(new_mode) is None:
            return Result.fail(
                ErrorCode.UNSUPPORTED_MODE,
                f"Unsupported run mode: {new_mode}",
            )

        current_mode_raw = self.attributes.get("CurrentMode")
        if not isinstance(current_mode_raw, int):
            return Result.fail(
                ErrorCode.INVALID_STATE,
                "CurrentMode attribute is malformed",
            )
        current_mode = int(current_mode_raw)

        if current_mode == new_mode:
            return Result.ok(
                {
                    "old_mode": current_mode,
                    "new_mode": new_mode,
                }
            )

        current_idle = self.is_idle_mode(current_mode)
        new_idle = self.is_idle_mode(new_mode)

        if (
            (self.feature_map & self.FEATURE_DIRECT_MODE_CHANGE) == 0
            and (not current_idle)
            and (not new_idle)
        ):
            return Result.fail(
                ErrorCode.INVALID_IN_MODE,
                "Direct non-idle run mode changes are not supported",
            )

        operational_state_result = self._require_operational_state()
        if not operational_state_result.success:
            return operational_state_result

        op_state = operational_state_result.data
        if not isinstance(op_state, int):
            return Result.fail(
                ErrorCode.INVALID_STATE,
                "OperationalState result payload is malformed",
            )

        if op_state in (
            RVCOperationalStateCode.PAUSED,
            RVCOperationalStateCode.SEEKING_CHARGER,
            RVCOperationalStateCode.ERROR,
        ):
            return Result.fail(
                ErrorCode.INVALID_IN_MODE,
                "Cannot change run mode in current operational state",
            )

        if op_state == RVCOperationalStateCode.RUNNING and not new_idle:
            return Result.fail(
                ErrorCode.INVALID_IN_MODE,
                "Running state only allows switching to an idle-tagged run mode",
            )

        if op_state in (
            RVCOperationalStateCode.STOPPED,
            RVCOperationalStateCode.DOCKED,
            RVCOperationalStateCode.CHARGING,
        ) and (not current_idle) and (not new_idle):
            return Result.fail(
                ErrorCode.INVALID_IN_MODE,
                "Run mode must transition through idle in the current operational state",
            )

        self.attributes["CurrentMode"] = new_mode

        if self.device is None:
            return Result.fail(
                ErrorCode.INVALID_STATE,
                "RVC device reference is not set",
            )
        self.device.on_run_mode_changed(current_mode, new_mode)

        return Result.ok(
            {
                "old_mode": current_mode,
                "new_mode": new_mode,
            }
        )
