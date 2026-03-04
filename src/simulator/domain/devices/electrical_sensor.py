from src.simulator.domain.clusters.electrical_energy_measurement import (
    ElectricalEnergyMeasurementCluster,
)
from src.simulator.domain.clusters.electrical_power_measurement import ElectricalPowerMeasurementCluster
from src.simulator.domain.clusters.power_topology import PowerTopologyCluster
from src.simulator.domain.devices.base import Device
from src.simulator.domain.clusters.basic_information import BasicInformationCluster
from src.simulator.domain.result import Result, ResultBuilder, ErrorCode


class ElectricalSensor(Device):

    def __init__(self, device_id):
        super().__init__(
            device_id,
            "electrical_sensor",
            BasicInformationCluster(
                vendor_name="LG Electronics",
                vendor_id=1,
                product_name="Electrical Sensor",
                product_id=0x0510,
            ),
        )

        self.add_cluster(
            1, PowerTopologyCluster(features=PowerTopologyCluster.FEATURE_NODE)
        )
        self.add_cluster(1, ElectricalPowerMeasurementCluster())
        self.add_cluster(1, ElectricalEnergyMeasurementCluster())

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
