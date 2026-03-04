from src.simulator.domain.clusters.rtcc_mode import RTCCModeCluster
from src.simulator.domain.clusters.temperature_control import FeatureFlag, TemperatureControlCluster
from src.simulator.domain.clusters.temperature_measurement import TemperatureMeasurementCluster
from src.simulator.domain.devices.base import Device
from src.simulator.domain.clusters.basic_information import BasicInformationCluster
from src.simulator.domain.clusters.descriptor import DescriptorCluster


class Freezer(Device):
    def __init__(self, device_id):
        super().__init__(
            device_id,
            "freezer",
            BasicInformationCluster(
                vendor_name="LG Electronics",
                vendor_id=1,
                product_name="Freezer",
                product_id=2,
            ),
        )
        descriptor_cluster = DescriptorCluster()
        descriptor_cluster.add_tag("Freezer")
        self.add_cluster(1, descriptor_cluster)
        self.add_cluster(1, RTCCModeCluster())
        self.temperature_control = TemperatureControlCluster(features=FeatureFlag.TN)

        self.temperature_control.attributes["TemperatureSetpoint"] = -1500
        self.temperature_control.attributes["MinTemperature"] = -2300
        self.temperature_control.attributes["MaxTemperature"] = -1500
        self.add_cluster(1, self.temperature_control)

        self.temperature_measurement = TemperatureMeasurementCluster(
            measured_value=-1500
        )
        self.add_cluster(1, self.temperature_measurement)

        self.is_compressor_on = False

    def on_time_tick(self):
        

        ASSUMED_AMBIENT_TEMP = 2200

        INSULATION_FACTOR_K = 0.004

        COOLING_POWER_PER_TICK = -45

        HYSTERESIS_BAND = 50

        setpoint = self.temperature_control.attributes.get("TemperatureSetpoint")
        current_temp = self.temperature_measurement.attributes.get("MeasuredValue")

        temp_difference = ASSUMED_AMBIENT_TEMP - current_temp
        heat_leak = temp_difference * INSULATION_FACTOR_K
        current_temp += heat_leak

        if not self.is_compressor_on and current_temp > (setpoint + HYSTERESIS_BAND):
            self.is_compressor_on = True

        elif self.is_compressor_on and current_temp <= setpoint:
            self.is_compressor_on = False

        if self.is_compressor_on:
            current_temp += COOLING_POWER_PER_TICK

        self.temperature_measurement.attributes["MeasuredValue"] = current_temp
