from src.simulator.domain.devices.base import Device
from src.simulator.domain.clusters.basic_information import BasicInformationCluster
from src.simulator.domain.clusters.onoff import OnOffCluster
from src.simulator.domain.result import Result, ResultBuilder, ErrorCode


class OnOffLight(Device):

    def __init__(self, device_id):
        super().__init__(
            device_id,
            "on_off_light",
            BasicInformationCluster(
                vendor_name="LG Electronics",
                vendor_id=1,
                product_name="On/Off Light",
                product_id=4,
            ),
        )

        self.add_cluster(1, OnOffCluster())

    def write_attribute(
        self, endpoint_id: int, cluster_id: str, attribute_id: str, value
    ) -> Result:
        

        if self._is_readonly_attribute(endpoint_id, cluster_id, attribute_id):
            return Result.fail(
                ErrorCode.READ_ONLY,
                f"{attribute_id} attribute is read-only",
                f"Cannot modify {attribute_id} attribute in {cluster_id} cluster. This attribute is read-only and managed by the system.",
            )

        return super().write_attribute(endpoint_id, cluster_id, attribute_id, value)
