from src.simulator.domain.clusters.base import Cluster
from src.simulator.domain.result import Result
from typing import Optional, Callable


class OnOffCluster(Cluster):
    

    FEATURE_LT = 0x01
    FEATURE_DF = 0x02

    def __init__(self, features: int = 0):
        super().__init__(cluster_id="OnOff")

        self.supported_features = features
        self.attributes = {
            "OnOff": False,
        }

        if self._supports_feature(self.FEATURE_LT):
            self.attributes.update(
                {
                    "GlobalSceneControl": True,
                    "OnTime": 0,
                    "OffWaitTime": 0,
                    "StartUpOnOff": None,
                }
            )


        self._dead_front_callback: Optional[Callable[[bool], None]] = None
        self._previous_onoff_state = False
        self.readonly_attributes = {"OnOff", "GlobalSceneControl"}

        self.commands = {"Off": self._off, "On": self._on, "Toggle": self._toggle}

    def _supports_feature(self, feature: int) -> bool:
        
        return (self.supported_features & feature) != 0

    def set_dead_front_callback(self, callback: Callable[[bool], None]):
        
        self._dead_front_callback = callback

    def is_in_dead_front_state(self) -> bool:
        
        return not self.attributes["OnOff"]

    def _notify_dead_front_change(self, entering_dead_front: bool):
        
        if self._dead_front_callback:
            self._dead_front_callback(entering_dead_front)

    def _off(self) -> Result:
        
        was_on = self.attributes["OnOff"]
        self.attributes["OnOff"] = False

        if was_on:

            if self._supports_feature(self.FEATURE_DF):
                self._notify_dead_front_change(True)


            if self._supports_feature(self.FEATURE_LT):


                pass

        return Result.ok(
            {
                "cluster": self.cluster_id,
                "command": "Off",
                "result": "Device turned off",
            }
        )

    def _on(self) -> Result:
        was_off = not self.attributes["OnOff"]
        self.attributes["OnOff"] = True

        if was_off:

            if self._supports_feature(self.FEATURE_DF):
                self._notify_dead_front_change(False)


            if self._supports_feature(self.FEATURE_LT):
                self.attributes["GlobalSceneControl"] = True

        return Result.ok(
            {
                "cluster": self.cluster_id,
                "command": "On",
                "result": "Device turned on",
            }
        )

    def _toggle(self) -> Result:

        current = self.attributes["OnOff"]
        self.attributes["OnOff"] = not current
        return Result.ok(
            {
                "cluster": self.cluster_id,
                "command": "Toggle",
                "result": f"OnOff toggled from {current} to {not current}",
            }
        )
