from src.simulator.domain.devices.base import Device
from src.simulator.domain.clusters.basic_information import BasicInformationCluster
from src.simulator.domain.clusters.onoff import OnOffCluster
from src.simulator.domain.clusters.fan_control import FanControlCluster
from src.simulator.domain.result import Result, ErrorCode


class Fan(Device):
    def __init__(self, device_id: str):
        super().__init__(
            device_id,
            "fan",
            BasicInformationCluster(
                vendor_name="LG Electronics",
                vendor_id=1,
                product_name="Fan",
                product_id=0x0002,
            ),
        )

        self.add_cluster(1, OnOffCluster())
        self.add_cluster(1, FanControlCluster())

    def _check_power_dependency(self) -> Result:
        power_status = self.get_attribute(1, "OnOff", "OnOff")
        if not power_status:
            return Result.fail(
                ErrorCode.DEPENDENCY_VIOLATION,
                "Power dependency violation",
                "Cannot perform operation when power is OFF. Turn on the fan first.",
            )
        return Result.ok()

    def _check_power_dependency_for_attribute(self, cluster_id: str, attribute_id: str) -> Result:
        power_dependent_attributes = {
            "FanControl": ["FanMode", "PercentSetting"],
        }
        if cluster_id in power_dependent_attributes and attribute_id in power_dependent_attributes[cluster_id]:
            return self._check_power_dependency()
        return Result.ok()

    def _execute_power_dependent_command(self, cluster_id: str, command_id: str, **args) -> Result:
        dep = self._check_power_dependency()
        if not dep.success:
            return dep
        return super().execute_command(1, cluster_id, command_id, **args)

    def execute_command(self, endpoint_id: int, cluster_id: str, command_id: str, **args) -> Result:  # type: ignore[override]
        if cluster_id == "FanControl":
            return self._execute_power_dependent_command(cluster_id, command_id, **args)
        return super().execute_command(endpoint_id, cluster_id, command_id, **args)

    def write_attribute(self, endpoint_id: int, cluster_id: str, attribute_id: str, value):  # type: ignore[override]
        if self._is_readonly_attribute(endpoint_id, cluster_id, attribute_id):
            return Result.fail(
                ErrorCode.READ_ONLY,
                f"{attribute_id} attribute is read-only",
                f"Cannot modify {attribute_id} attribute in {cluster_id} cluster. This attribute is read-only and managed by the system.",
            )
        if endpoint_id == 1:
            dep = self._check_power_dependency_for_attribute(cluster_id, attribute_id)
            if not dep.success:
                return dep
        return super().write_attribute(endpoint_id, cluster_id, attribute_id, value)
