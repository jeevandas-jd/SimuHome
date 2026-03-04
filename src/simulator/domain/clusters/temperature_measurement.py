from src.simulator.domain.clusters.base import Cluster


class TemperatureMeasurementCluster(Cluster):
    

    def __init__(self, measured_value: int | None = None):
        super().__init__(cluster_id="TemperatureMeasurement")
        self.attributes = {
            "MeasuredValue": measured_value,
            "MinMeasuredValue": -27315,
            "MaxMeasuredValue": 32766,
        }
        self.readonly_attributes = {
            "MeasuredValue",
            "MinMeasuredValue",
            "MaxMeasuredValue",
        }
