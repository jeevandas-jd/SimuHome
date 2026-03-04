from typing import List
from src.simulator.domain.clusters.channel import Channel, ChannelCluster, ChannelType
from src.simulator.domain.clusters.keypad_input import KeypadInputCluster
from src.simulator.domain.clusters.level_control import LevelControlCluster
from src.simulator.domain.clusters.media_playback import MediaPlaybackCluster
from src.simulator.domain.devices.base import Device
from src.simulator.domain.clusters.basic_information import BasicInformationCluster
from src.simulator.domain.clusters.onoff import OnOffCluster
from src.simulator.domain.result import Result, ResultBuilder, ErrorCode


_WITH_ONOFF_COMMANDS = frozenset({
    "MoveToLevelWithOnOff",
    "MoveWithOnOff",
    "StepWithOnOff",
    "StopWithOnOff",
})

default_channels: List[Channel] = [
    Channel(
        MajorNumber=1,
        MinorNumber=0,
        Name="KBS1",
        CallSign="KBS1",
        AffiliateCallSign="KBS1",
        Identifier="kbs1",
        Type=ChannelType.TERRESTRIAL,
    ),
    Channel(
        MajorNumber=2,
        MinorNumber=0,
        Name="KBS2",
        CallSign="KBS2",
        AffiliateCallSign="KBS2",
        Identifier="kbs2",
        Type=ChannelType.TERRESTRIAL,
    ),
    Channel(
        MajorNumber=3,
        MinorNumber=0,
        Name="MBC",
        CallSign="MBC",
        AffiliateCallSign="MBC",
        Identifier="mbc",
        Type=ChannelType.TERRESTRIAL,
    ),
    Channel(
        MajorNumber=4,
        MinorNumber=0,
        Name="SBS",
        CallSign="SBS",
        AffiliateCallSign="SBS",
        Identifier="sbs",
        Type=ChannelType.TERRESTRIAL,
    ),
    Channel(
        MajorNumber=5,
        MinorNumber=0,
        Name="EBS",
        CallSign="EBS",
        AffiliateCallSign="EBS",
        Identifier="ebs",
        Type=ChannelType.TERRESTRIAL,
    ),
]


class TV(Device):

    def __init__(self, device_id):
        super().__init__(
            device_id,
            "tv",
            BasicInformationCluster(
                vendor_name="LG Electronics",
                vendor_id=1,
                product_name="TV",
                product_id=5,
            ),
        )


        self.add_cluster(1, OnOffCluster())


        self.add_cluster(1, ChannelCluster(default_channels=default_channels))


        self.add_cluster(1, MediaPlaybackCluster())


        self.add_cluster(1, KeypadInputCluster(device=self))

        level_cluster = LevelControlCluster(enable_onoff_coupling=False)
        level_cluster.set_device_reference(self)
        self.add_cluster(1, level_cluster)

    def _check_power_dependency(self) -> Result:
        
        power_status = self.get_attribute(1, "OnOff", "OnOff")
        if not power_status:
            return Result.fail(
                ErrorCode.DEPENDENCY_VIOLATION,
                "Power dependency violation",
                "Cannot perform operation when power is OFF. Turn on the TV first.",
            )
        return Result.ok()

    def _check_power_dependency_for_attribute(
        self, cluster_id: str, attribute_id: str
    ) -> Result:
        
        power_dependent_attributes = {
            "Channel": ["CurrentChannel", "TargetChannel"],
            "MediaPlayback": ["CurrentTrack", "PlaybackState"],
            "LevelControl": [
                "CurrentLevel",
                "OnLevel",
                "DefaultMoveRate",
                "StartUpCurrentLevel",
            ],
        }

        if (
            cluster_id in power_dependent_attributes
            and attribute_id in power_dependent_attributes[cluster_id]
        ):
            return self._check_power_dependency()

        return Result.ok()

    def _execute_power_dependent_command(
        self, cluster_id: str, command_id: str, **args
    ) -> Result:
        
        dependency_check = self._check_power_dependency()
        if not dependency_check.success:
            return dependency_check

        return super().execute_command(1, cluster_id, command_id, **args)

    def execute_command(
        self, endpoint_id: int, cluster_id: str, command_id: str, **args
    ) -> Result:
        if cluster_id == "LevelControl" and command_id in _WITH_ONOFF_COMMANDS:
            return super().execute_command(endpoint_id, cluster_id, command_id, **args)

        if cluster_id in ["Channel", "MediaPlayback", "LevelControl"]:
            return self._execute_power_dependent_command(cluster_id, command_id, **args)

        return super().execute_command(endpoint_id, cluster_id, command_id, **args)

    def write_attribute(
        self, endpoint_id: int, cluster_id: str, attribute_id: str, value
    ) -> Result:
        

        if self._is_readonly_attribute(endpoint_id, cluster_id, attribute_id):
            return Result.fail(
                ErrorCode.READ_ONLY,
                f"{attribute_id} attribute is read-only",
                f"Cannot modify {attribute_id} attribute in {cluster_id} cluster. This attribute is read-only and managed by the system.",
            )

        dependency_check = self._check_power_dependency_for_attribute(
            cluster_id, attribute_id
        )
        if not dependency_check.success:
            return dependency_check

        return super().write_attribute(endpoint_id, cluster_id, attribute_id, value)
