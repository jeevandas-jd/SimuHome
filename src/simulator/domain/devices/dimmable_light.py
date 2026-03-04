from src.simulator.domain.devices.base import Device
from src.simulator.domain.clusters.basic_information import BasicInformationCluster
from src.simulator.domain.clusters.onoff import OnOffCluster
from src.simulator.domain.clusters.level_control import LevelControlCluster

from src.simulator.domain.result import Result, ErrorCode


class DimmableLight(Device):

    def __init__(self, device_id):
        super().__init__(
            device_id,
            "dimmable_light",
            BasicInformationCluster(
                vendor_name="LG Electronics",
                vendor_id=1,
                product_name="Dimmable Light",
                product_id=3,
            ),
        )

        self.add_cluster(1, OnOffCluster(features=OnOffCluster.FEATURE_LT))

        level_cluster = LevelControlCluster(time_aware=True)
        level_cluster.set_device_reference(self)
        self.add_cluster(1, level_cluster)

    def _check_power_dependency(self) -> Result:
        power_status = self.get_attribute(1, "OnOff", "OnOff")
        if not power_status:
            return Result.fail(
                ErrorCode.DEPENDENCY_VIOLATION,
                "Power dependency violation",
                "Cannot perform operation when power is OFF. Turn on the light first.",
            )
        return Result.ok()

    def _check_power_dependency_for_attribute(
        self, cluster_id: str, attribute_id: str
    ) -> Result:
        power_dependent_attributes = {
            "LevelControl": [
                "CurrentLevel",
                "OnLevel",
                "DefaultMoveRate",
                "StartUpCurrentLevel",
            ]
        }

        if (
            cluster_id in power_dependent_attributes
            and attribute_id in power_dependent_attributes[cluster_id]
        ):
            return self._check_power_dependency()

        return Result.ok()

    def execute_command(
        self, endpoint_id: int, cluster_id: str, command_id: str, **args
    ) -> Result:
        if cluster_id == "OnOff":
            was_on = self.get_attribute(1, "OnOff", "OnOff")
            result = super().execute_command(endpoint_id, cluster_id, command_id, **args)
            if result.success:
                is_on = self.get_attribute(1, "OnOff", "OnOff")
                if was_on != is_on:
                    level_cluster = self.get_cluster(1, "LevelControl")
                    if level_cluster and hasattr(level_cluster, "on_onoff_change"):
                        level_cluster.on_onoff_change(bool(is_on))
            return result


        if cluster_id == "LevelControl":
            return super().execute_command(endpoint_id, cluster_id, command_id, **args)

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
