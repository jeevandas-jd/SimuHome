from dataclasses import dataclass
from enum import IntEnum
from src.simulator.domain.clusters.base import Cluster
from src.simulator.domain.result import ErrorCode, Result


class ModeTag(IntEnum):
    AUTO = 0x0000
    QUICK = 0x0001
    QUIET = 0x0002
    LOW_ENERGY = 0x0004
    VACATION = 0x0005
    RAPID_COOL = 0x4000
    RAPID_FREEZE = 0x4001


@dataclass
class ModeOptionStruct:
    Label: str
    Mode: ModeTag
    ModeTags: list[ModeTag]


class RTCCModeCluster(Cluster):
    def __init__(self):
        super().__init__(cluster_id="RTCCMode")
        self.attributes = {
            "SupportedModes": [
                {
                    "Label": "Normal",
                    "Mode": ModeTag.AUTO,
                    "ModeTags": [
                        ModeTag.AUTO,
                    ],
                },
                {
                    "Label": "Energy Save",
                    "Mode": ModeTag.LOW_ENERGY,
                    "ModeTags": [
                        ModeTag.LOW_ENERGY,
                    ],
                },
                {
                    "Label": "Rapid Cool",
                    "Mode": ModeTag.RAPID_COOL,
                    "ModeTags": [
                        ModeTag.RAPID_COOL,
                    ],
                },
                {
                    "Label": "Rapid Freeze",
                    "Mode": ModeTag.RAPID_FREEZE,
                    "ModeTags": [
                        ModeTag.RAPID_FREEZE,
                    ],
                },
            ],
            "CurrentMode": ModeTag.AUTO,
        }
        self.readonly_attributes = {
            "SupportedModes",
            "CurrentMode",
        }
        self.commands = {
            "ChangeToMode": self._change_to_mode,
        }

    def _change_to_mode(self, mode: int) -> Result:
        for mode_entry in self.attributes["SupportedModes"]:
            if mode_entry["Mode"] == mode:

                self.attributes["CurrentMode"] = mode
                return Result.ok(
                    {
                        "Status": ErrorCode.SUCCESS,
                        "StatusText": f"Mode changed successfully to {mode_entry['Label']}",
                    }
                )
        return Result.fail(
            ErrorCode.UNSUPPORTED_MODE,
            "The requested mode is not supported. Available modes are: "
            + ", ".join(
                mode_entry["Label"] for mode_entry in self.attributes["SupportedModes"]
            ),
        )
