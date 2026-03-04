from src.simulator.domain.clusters.base import Cluster
from src.simulator.domain.result import Result, ErrorCode


class DrynessLevelEnum:
    LOW = 0
    NORMAL = 1
    EXTRA = 2
    MAX = 3

    @classmethod
    def all_levels(cls):
        return [cls.LOW, cls.NORMAL, cls.EXTRA, cls.MAX]

    @classmethod
    def label(cls, value: int) -> str:
        mapping = {
            cls.LOW: "Low",
            cls.NORMAL: "Normal",
            cls.EXTRA: "Extra",
            cls.MAX: "Max",
        }
        return mapping.get(value, f"Unknown({value})")


class LaundryDryerControlsCluster(Cluster):
    

    def __init__(self):
        super().__init__(cluster_id="LaundryDryerControls")
        self.device = None
        self.attributes = {
            "SupportedDrynessLevels": DrynessLevelEnum.all_levels(),

            "SelectedDrynessLevel": DrynessLevelEnum.NORMAL,
        }

        self.readonly_attributes = {"SupportedDrynessLevels"}

    def set_device_reference(self, device):
        self.device = device

    def _is_device_running(self) -> bool:
        if not self.device:
            return False
        try:
            from src.simulator.domain.clusters.operational_state import OperationalStateEnum

            state = self.device.get_attribute(1, "OperationalState", "OperationalState")
            return state == OperationalStateEnum.RUNNING
        except Exception:
            return False

    def write_attribute(self, attribute_id: str, value):  # type: ignore[override]

        if attribute_id == "SelectedDrynessLevel" and self._is_device_running():
            return Result.fail(
                ErrorCode.INVALID_STATE,
                "Cannot change SelectedDrynessLevel while device is running",
                "Stop the device before changing dryness level",
            )

        if attribute_id == "SelectedDrynessLevel":
            if value is None:

                old = self.attributes.get(attribute_id)
                self.attributes[attribute_id] = None
                return Result.ok(
                    {
                        "cluster": self.cluster_id,
                        "attribute": attribute_id,
                        "old_value": old,
                        "new_value": None,
                    }
                )
            if value not in self.attributes["SupportedDrynessLevels"]:
                return Result.fail(
                    ErrorCode.CONSTRAINT_ERROR,
                    f"Invalid dryness level {value}",
                    f"Supported: {self.attributes['SupportedDrynessLevels']} or None",
                )
        return super().write_attribute(attribute_id, value)
