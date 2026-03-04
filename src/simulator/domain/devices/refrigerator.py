from src.simulator.domain.clusters.rtcc_mode import RTCCModeCluster
from src.simulator.domain.clusters.temperature_control import FeatureFlag, TemperatureControlCluster
from src.simulator.domain.clusters.temperature_measurement import TemperatureMeasurementCluster
from src.simulator.domain.devices.base import Device
from src.simulator.domain.clusters.basic_information import BasicInformationCluster
from src.simulator.domain.clusters.descriptor import DescriptorCluster


class Refrigerator(Device):
    def __init__(self, device_id):
        super().__init__(
            device_id,
            "refrigerator",
            BasicInformationCluster(
                vendor_name="LG Electronics",
                vendor_id=1,
                product_name="Refrigerator",
                product_id=2,
            ),
        )
        descriptor_cluster = DescriptorCluster()
        descriptor_cluster.add_tag("Refrigerator")
        self.add_cluster(1, descriptor_cluster)
        self.add_cluster(1, RTCCModeCluster())
        self.temperature_control = TemperatureControlCluster(features=FeatureFlag.TN)

        self.temperature_control.attributes["TemperatureSetpoint"] = 700
        self.temperature_control.attributes["MinTemperature"] = 100
        self.temperature_control.attributes["MaxTemperature"] = 700
        self.add_cluster(1, self.temperature_control)

        self.temperature_measurement = TemperatureMeasurementCluster(measured_value=700)
        self.add_cluster(1, self.temperature_measurement)

        self.is_compressor_on = False

    def on_time_tick(self):
        

        ASSUMED_AMBIENT_TEMP = 2200
        INSULATION_FACTOR_K = 0.005
        COOLING_RATE_PER_SEC = 0.2
        HYSTERESIS_BAND = 50

        dt = self.tick_interval

        setpoint = self.temperature_control.attributes.get("TemperatureSetpoint")
        current_temp = self.temperature_measurement.attributes.get("MeasuredValue")

        temp_difference = ASSUMED_AMBIENT_TEMP - current_temp
        heat_leak = temp_difference * INSULATION_FACTOR_K * dt
        current_temp += heat_leak

        if not self.is_compressor_on and current_temp > (
            setpoint + HYSTERESIS_BAND / 2
        ):
            self.is_compressor_on = True
        elif self.is_compressor_on and current_temp <= (setpoint - HYSTERESIS_BAND / 2):
            self.is_compressor_on = False

        if self.is_compressor_on:
            cooling_per_tick_cdeg = COOLING_RATE_PER_SEC * 100.0 * dt
            current_temp -= cooling_per_tick_cdeg

        self.temperature_measurement.attributes["MeasuredValue"] = int(
            round(current_temp)
        )
