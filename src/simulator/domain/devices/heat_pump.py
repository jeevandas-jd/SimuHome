from src.simulator.domain.clusters.device_energy_management import (
    DeviceEnergyManagementCluster,
    ESATypeEnum,
)
from src.simulator.domain.clusters.power_source import (
    PowerSourceCluster,
    PowerSourceEnum,
    PowerSourceStatusEnum,
)
from src.simulator.domain.clusters.thermostat import ThermostatCluster
from src.simulator.domain.clusters.electrical_power_measurement import (
    ElectricalPowerMeasurementCluster,
    PowerModeEnum,
)
from src.simulator.domain.clusters.electrical_energy_measurement import (
    ElectricalEnergyMeasurementCluster,
)
from src.simulator.domain.clusters.descriptor import DescriptorCluster
from src.simulator.domain.devices.base import Device
from src.simulator.domain.clusters.basic_information import BasicInformationCluster
from src.simulator.domain.result import Result, ResultBuilder, ErrorCode


class HeatPump(Device):
    

    def __init__(self, device_id: str):
        super().__init__(
            device_id,
            "heat_pump",
            BasicInformationCluster(
                vendor_name="Heat Pump",
                vendor_id=1,
                product_name="Heat Pump",
                product_id=0x0309,
            ),
        )
        power_source = PowerSourceCluster(
            power_source=PowerSourceEnum.MAINS,
            status=PowerSourceStatusEnum.STANDBY,
            features=PowerSourceCluster.FEATURE_WIRED,
        )
        power_source.set_description("AC Grid Connection")
        power_source.update_wired_voltage(220000)
        power_source.attributes["WiredNominalVoltage"] = 220000
        power_source.set_wired_present(True)
        self.add_cluster(1, power_source)


        power_source_descriptor = DescriptorCluster()
        power_source_descriptor.add_tag("Grid")
        self.add_cluster(1, power_source_descriptor)


        from src.simulator.domain.clusters.power_topology import PowerTopologyCluster


        power_topology = PowerTopologyCluster(
            features=PowerTopologyCluster.FEATURE_NODE
        )
        self.add_cluster(2, power_topology)


        power_measurement = ElectricalPowerMeasurementCluster(
            power_mode=PowerModeEnum.AC,
            feature_map=ElectricalPowerMeasurementCluster.FEATURE_ALTC,
            optional_attributes={
                "Voltage",
                "ActiveCurrent",
                "RMSVoltage",
                "RMSCurrent",
                "RMSPower",
                "Frequency",
                "PowerFactor",
                "ApparentPower",
            },
        )

        power_measurement.attributes["Voltage"] = (
            230000
        )
        power_measurement.attributes["ActiveCurrent"] = (
            15000
        )
        power_measurement.attributes["ActivePower"] = (
            3450000
        )


        power_measurement.attributes["RMSVoltage"] = 230000
        power_measurement.attributes["RMSCurrent"] = 15000
        power_measurement.attributes["RMSPower"] = 3450000
        power_measurement.attributes["Frequency"] = 50000
        power_measurement.attributes["PowerFactor"] = 9500
        power_measurement.attributes["ApparentPower"] = (
            3631580
        )
        self.add_cluster(
            2, power_measurement
        )

        energy_measurement = ElectricalEnergyMeasurementCluster(
            feature_map=(
                ElectricalEnergyMeasurementCluster.FEATURE_IMPE
                | ElectricalEnergyMeasurementCluster.FEATURE_CUME
                | ElectricalEnergyMeasurementCluster.FEATURE_PERE
            ),
        )
        self.add_cluster(2, energy_measurement)


        electrical_descriptor = DescriptorCluster()
        electrical_descriptor.add_tag("ElectricalSensor")
        self.add_cluster(2, electrical_descriptor)


        energy_management = DeviceEnergyManagementCluster(
            features=DeviceEnergyManagementCluster.FEATURE_PA,
            esa_type=ESATypeEnum.SPACE_HEATING,
            esa_can_generate=False,
        )

        energy_management.set_power_limits(
            abs_min_power=1000000, abs_max_power=8000000
        )
        self.add_cluster(3, energy_management)


        energy_mgmt_descriptor = DescriptorCluster()
        energy_mgmt_descriptor.add_tag("EnergyManagement")
        self.add_cluster(3, energy_mgmt_descriptor)


        thermostat = ThermostatCluster()
        self.add_cluster(4, thermostat)


        thermostat_descriptor = DescriptorCluster()
        thermostat_descriptor.add_tag("RoomThermostat")
        self.add_cluster(4, thermostat_descriptor)


        self.device_composition = {
            "heat_pump_device_id": 0x0309,
            "endpoints": {
                0: {"device_type": "Root", "description": "Root device endpoint"},
                1: {
                    "device_type": 0x0011,
                    "description": "Power Source Device - AC Grid Connection",
                },
                2: {
                    "device_type": 0x0510,
                    "description": "Electrical Sensor Device - Grid Measurement",
                },
                3: {
                    "device_type": 0x050D,
                    "description": "Device Energy Management Device",
                },
                4: {
                    "device_type": 0x0301,
                    "description": "Thermostat Device - Room Control",
                },
            },
            "mandatory_features": {
                "power_source_wired": True,
                "electrical_sensor_ac": True,
                "power_adjustment": True,
                "voltage_measurement": True,
                "active_current_measurement": True,
            },
            "optional_features": {
                "imported_energy": True,
                "cumulative_energy": True,
                "thermostat_control": True,
            },
        }

    def get_cluster(self, endpoint_id: int, cluster_id: str):
        
        if endpoint_id in self.endpoints:
            for stored_cluster_id, cluster in self.endpoints[endpoint_id].items():
                cluster_name = getattr(cluster, "CLUSTER_NAME", None)
                if isinstance(cluster_name, str) and cluster_name == cluster_id:
                    return cluster
                if stored_cluster_id == cluster_id or str(stored_cluster_id) == cluster_id:
                    return cluster
        return None

    def get_grid_power_consumption(self) -> float:
        cluster = self.get_cluster(2, "ElectricalPowerMeasurement")
        if not cluster:
            return 0.0

        raw_power = cluster.attributes.get("ActivePower")
        if not isinstance(raw_power, int):
            return 0.0

        return float(raw_power) / 1000.0

    def get_energy_consumption_today(self) -> float:
        cluster = self.get_cluster(2, "ElectricalEnergyMeasurement")
        if not cluster:
            return 0.0

        imported = cluster.attributes.get("CumulativeEnergyImported")
        if not imported or not hasattr(imported, "Energy"):
            return 0.0

        energy_value = getattr(imported, "Energy", 0)
        if not isinstance(energy_value, int):
            return 0.0

        return float(energy_value) / 1_000_000.0

    def __str__(self) -> str:
        
        power = self.get_grid_power_consumption()
        energy = self.get_energy_consumption_today()

        thermostat_cluster = self.get_cluster(4, "Thermostat")
        heating_setpoint = "N/A"
        if thermostat_cluster:
            setpoint_raw = thermostat_cluster.attributes.get(
                "OccupiedHeatingSetpoint", 0
            )
            heating_setpoint = f"{setpoint_raw / 100.0:.1f}°C"

        return (
            f"HeatPump(ID={self.device_id}, "
            f"Power={power:.1f}W, "
            f"Energy Today={energy:.2f}kWh, "
            f"Heating Setpoint={heating_setpoint})"
        )

    def _check_power_source_dependency(self) -> Result:
        
        power_source_cluster = self.get_cluster(1, "PowerSource")
        if not power_source_cluster:
            return Result.fail(
                ErrorCode.DEPENDENCY_VIOLATION,
                "Power source dependency violation",
                "Power source cluster not found. Cannot verify power status.",
            )

        power_status = power_source_cluster.attributes.get(
            "Status", PowerSourceStatusEnum.UNSPECIFIED
        )
        if power_status in [
            PowerSourceStatusEnum.UNSPECIFIED,
            PowerSourceStatusEnum.UNAVAILABLE,
        ]:
            return Result.fail(
                ErrorCode.DEPENDENCY_VIOLATION,
                "Power source dependency violation",
                f"Cannot perform operation when power source status is {power_status.name}. Power source must be ACTIVE or STANDBY.",
            )

        return Result.ok()

    def _check_power_source_dependency_for_attribute(
        self, endpoint_id: int, cluster_id: str, attribute_id: str
    ) -> Result:
        

        power_dependent_clusters = {
            "DeviceEnergyManagement": ["PowerAdjustmentCapability", "Forecast"],
            "Thermostat": [
                "OccupiedHeatingSetpoint",
                "OccupiedCoolingSetpoint",
                "SystemMode",
            ],
            "ElectricalPowerMeasurement": [
                "ActivePower",
                "ReactivePower",
                "ApparentPower",
                "Voltage",
                "ActiveCurrent",
            ],
        }

        if (
            cluster_id in power_dependent_clusters
            and attribute_id in power_dependent_clusters[cluster_id]
        ):
            return self._check_power_source_dependency()

        return Result.ok()

    def _execute_power_dependent_command(
        self, endpoint_id: int, cluster_id: str, command_id: str, **args
    ) -> Result:
        
        dependency_check = self._check_power_source_dependency()
        if not dependency_check.success:
            return dependency_check

        return super().execute_command(endpoint_id, cluster_id, command_id, **args)

    def _check_energy_management_dependency(
        self, endpoint_id: int, cluster_id: str, command_id: str
    ) -> Result:
        

        energy_management_dependent = ["Thermostat", "ElectricalPowerMeasurement"]

        if cluster_id in energy_management_dependent:
            energy_cluster = self.get_cluster(3, "DeviceEnergyManagement")
            if energy_cluster:

                power_capability = energy_cluster.attributes.get(
                    "PowerAdjustmentCapability"
                )
                if power_capability and hasattr(
                    power_capability, "power_adjust_capability"
                ):

                    if cluster_id == "Thermostat" and command_id in [
                        "SetpointRaiseLower"
                    ]:
                        return Result.fail(
                            ErrorCode.DEPENDENCY_VIOLATION,
                            "Energy management dependency violation",
                            "Cannot modify thermostat settings while power adjustment is active. Energy management is controlling the device.",
                        )

        return Result.ok()

    def execute_command(
        self, endpoint_id: int, cluster_id: str, command_id: str, **args
    ) -> Result:
        

        energy_check = self._check_energy_management_dependency(
            endpoint_id, cluster_id, command_id
        )
        if not energy_check.success:
            return energy_check


        if cluster_id in ["DeviceEnergyManagement", "Thermostat"]:
            return self._execute_power_dependent_command(
                endpoint_id, cluster_id, command_id, **args
            )

        else:
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


        dependency_check = self._check_power_source_dependency_for_attribute(
            endpoint_id, cluster_id, attribute_id
        )
        if not dependency_check.success:
            return dependency_check


        constraint_check = self._check_special_constraints(
            endpoint_id, cluster_id, attribute_id, value
        )
        if not constraint_check.success:
            return constraint_check

        return super().write_attribute(endpoint_id, cluster_id, attribute_id, value)

    def _check_special_constraints(
        self, endpoint_id: int, cluster_id: str, attribute_id: str, value
    ) -> Result:
        

        if cluster_id == "Thermostat":
            return self._check_thermostat_constraints(attribute_id, value)


        elif cluster_id == "DeviceEnergyManagement":
            return self._check_energy_management_constraints(attribute_id, value)

        return Result.ok()

    def _check_thermostat_constraints(self, attribute_id: str, value) -> Result:
        

        thermostat_cluster = self.get_cluster(4, "Thermostat")
        if not thermostat_cluster:
            return Result.ok()


        if attribute_id == "OccupiedHeatingSetpoint":

            if value < 700 or value > 3000:
                return Result.fail(
                    ErrorCode.VALIDATION_ERROR,
                    "Temperature constraint violation",
                    f"Heating setpoint {value/100:.1f}°C is outside allowed range (7.0°C to 30.0°C)",
                )

        elif attribute_id == "OccupiedCoolingSetpoint":

            if value < 1600 or value > 3200:
                return Result.fail(
                    ErrorCode.VALIDATION_ERROR,
                    "Temperature constraint violation",
                    f"Cooling setpoint {value/100:.1f}°C is outside allowed range (16.0°C to 32.0°C)",
                )

        elif attribute_id == "SystemMode":

            valid_modes = [0, 1, 3, 4]
            if value not in valid_modes:
                return Result.fail(
                    ErrorCode.VALIDATION_ERROR,
                    "System mode constraint violation",
                    f"System mode {value} is not valid. Valid modes: {valid_modes}",
                )

        return Result.ok()

    def _check_energy_management_constraints(self, attribute_id: str, value) -> Result:
        

        energy_cluster = self.get_cluster(3, "DeviceEnergyManagement")
        if not energy_cluster:
            return Result.ok()


        if attribute_id == "AbsMinPower":

            if value < 1000000 or value > 8000000:
                return Result.fail(
                    ErrorCode.VALIDATION_ERROR,
                    "Power limit constraint violation",
                    f"AbsMinPower {value/1000000:.1f}kW is outside allowed range (1.0kW to 8.0kW)",
                )

        elif attribute_id == "AbsMaxPower":

            if value < 1000000 or value > 8000000:
                return Result.fail(
                    ErrorCode.VALIDATION_ERROR,
                    "Power limit constraint violation",
                    f"AbsMaxPower {value/1000000:.1f}kW is outside allowed range (1.0kW to 8.0kW)",
                )


            abs_min = energy_cluster.attributes.get("AbsMinPower", 1000000)
            if value <= abs_min:
                return Result.fail(
                    ErrorCode.VALIDATION_ERROR,
                    "Power limit constraint violation",
                    f"AbsMaxPower {value/1000000:.1f}kW must be greater than AbsMinPower {abs_min/1000000:.1f}kW",
                )

        return Result.ok()
