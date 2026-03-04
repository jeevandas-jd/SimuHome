from dataclasses import dataclass, field
from typing import List, Optional
from enum import Enum

from src.simulator.domain.clusters.base import Cluster
from src.simulator.domain.result import Result, ErrorCode


class PowerSourceStatusEnum(Enum):
    

    UNSPECIFIED = 0
    ACTIVE = 1
    STANDBY = 2
    UNAVAILABLE = 3


class WiredFaultTypeEnum(Enum):
    

    UNSPECIFIED = 0
    OVER_VOLTAGE = 1
    UNDER_VOLTAGE = 2


class BatFaultTypeEnum(Enum):
    

    UNSPECIFIED = 0
    OVER_TEMP = 1
    UNDER_TEMP = 2


class BatChargeFaultTypeEnum(Enum):
    

    UNSPECIFIED = 0
    AMBIENT_TOO_HOT = 1
    AMBIENT_TOO_COLD = 2
    BATTERY_TOO_HOT = 3
    BATTERY_TOO_COLD = 4
    BATTERY_ABSENT = 5
    BATTERY_OVER_VOLTAGE = 6
    BATTERY_UNDER_VOLTAGE = 7
    CHARGER_OVER_VOLTAGE = 8
    CHARGER_UNDER_VOLTAGE = 9
    SAFETY_TIMEOUT = 10


class PowerSourceEnum(Enum):
    

    UNSPECIFIED = 0
    MAINS = 1
    BATTERY = 2
    DC = 3
    EMERGENCY = 4
    EMERGENCY_MAINS = 5
    EMERGENCY_BATTERY = 6
    EMERGENCY_DC = 7


class WiredCurrentTypeEnum(Enum):
    

    AC = 0
    DC = 1


class BatChargeLevelEnum(Enum):
    

    OK = 0
    WARNING = 1
    CRITICAL = 2


class BatReplaceabilityEnum(Enum):
    

    UNSPECIFIED = 0
    NOT_REPLACEABLE = 1
    USER_REPLACEABLE = 2
    FACTORY_REPLACEABLE = 3


class BatCommonDesignationEnum(Enum):
    

    UNSPECIFIED = 0
    AAA = 1
    AA = 2
    C = 3
    D = 4
    FOUR_V5 = 5
    SIX_V0 = 6
    NINE_V0 = 7
    TWELVE_V0 = 8
    CR123A = 9
    CR2 = 10
    CR2032 = 11
    CR2450 = 12

    ONE_V5 = 13
    THREE_V0 = 14
    TWO_V5 = 15
    CR2016 = 16
    CR1632 = 17
    CR14505 = 18
    CR17335 = 19
    CR26650 = 20
    EIGHTEEN_V650 = 21
    FOURTEEN_V500 = 22
    TEN_V440 = 23
    NINE_V8AH = 24
    SEVEN_V2AH = 25
    SIX_V5AH = 26
    EIGHTEEN_V6502S = 27
    F = 28
    A23 = 29
    N = 30
    AAAA = 31
    A76 = 32
    A13 = 33
    A312 = 34
    A675 = 35
    AC41E = 36
    A10 = 37
    A5 = 38

    SC = 39
    SUB_C = 40

    PRISMATIC = 41

    LR44 = 42
    LR1130 = 43
    LR41 = 44
    LR43 = 45
    LR54 = 46
    LR1154 = 47

    CR927 = 48
    CR1025 = 49
    CR1220 = 50
    CR1616 = 51
    CR2330 = 52

    LIPO = 53
    LIFE = 54
    LICO2 = 55
    NCR18650B = 56
    ICR18650 = 57
    IMR18650 = 58


class BatApprovedChemistryEnum(Enum):
    

    UNSPECIFIED = 0
    ALKALINE = 1
    LITHIUM_CARBON_FLUORIDE = 2
    LITHIUM_CHROMIUM_OXIDE = 3
    LITHIUM_COPPER_OXIDE = 4
    LITHIUM_IRON_DISULFIDE = 5
    LITHIUM_MANGANESE_OXIDE = 6
    LITHIUM_THIONYL_CHLORIDE = 7
    MAGNESIUM = 8
    MERCURY_OXIDE = 9
    NICKEL_OXYHYDRIDE = 10
    SILVER_OXIDE = 11
    ZINC_AIR = 12
    ZINC_CARBON = 13
    ZINC_CHLORIDE = 14
    ZINC_MANGANESE_OXIDE = 15
    LITHIUM_ION = 16
    LITHIUM_ION_POLYMER = 17
    LITHIUM_IRON_PHOSPHATE = 18
    LITHIUM_SULFUR = 19
    LITHIUM_TITANATE = 20
    NICKEL_METAL_HYDRIDE = 21
    NICKEL_CADMIUM = 22


class BatChargeStateEnum(Enum):
    

    UNKNOWN = 0
    IS_CHARGING = 1
    IS_AT_FULL_CHARGE = 2
    IS_NOT_CHARGING = 3


class RadioFaultEnum(Enum):
    

    UNSPECIFIED = 0
    WIFI_FAULT = 1
    CELLULAR_FAULT = 2
    THREAD_FAULT = 3
    NFC_FAULT = 4
    BLE_FAULT = 5
    ETHERNET_FAULT = 6


class PowerSourceCurrentType(Enum):
    

    UNKNOWN = 0
    AC = 1
    DC = 2


@dataclass
class WiredFaultChangeType:
    

    current: List[WiredFaultTypeEnum] = field(default_factory=list)
    previous: List[WiredFaultTypeEnum] = field(default_factory=list)


@dataclass
class BatFaultChangeType:
    

    current: List[BatFaultTypeEnum] = field(default_factory=list)
    previous: List[BatFaultTypeEnum] = field(default_factory=list)


@dataclass
class BatChargeFaultChangeType:
    

    current: List[BatChargeFaultTypeEnum] = field(default_factory=list)
    previous: List[BatChargeFaultTypeEnum] = field(default_factory=list)


class PowerSourceCluster(Cluster):
    

    CLUSTER_ID = 0x002F
    CLUSTER_NAME = "PowerSource"
    CLUSTER_REVISION = 3


    FEATURE_WIRED = 0x01
    FEATURE_BATTERY = 0x02
    FEATURE_RECHARGEABLE = 0x04
    FEATURE_REPLACEABLE = 0x08

    def __init__(
        self,
        power_source: PowerSourceEnum = PowerSourceEnum.MAINS,
        status: PowerSourceStatusEnum = PowerSourceStatusEnum.UNSPECIFIED,
        features: int = 0,
    ):
        
        super().__init__(self.CLUSTER_NAME)

        self.power_source = power_source
        self.features = features


        self.attributes = {
            "ClusterRevision": self.CLUSTER_REVISION,
            "FeatureMap": self.features,
            "Status": status,
            "Order": 0,
            "Description": "",
            "EndpointList": [],
        }


        self.readonly_attributes = {"Order", "Status", "Description"}


        if self.has_feature(self.FEATURE_WIRED):
            self.attributes.update(
                {
                    "WiredAssessedInputVoltage": None,
                    "WiredAssessedInputFrequency": None,
                    "WiredCurrentType": WiredCurrentTypeEnum.AC,
                    "WiredAssessedCurrent": None,
                    "WiredNominalVoltage": 0,
                    "WiredMaximumCurrent": 0,
                    "WiredPresent": True,
                    "ActiveWiredFaults": [],
                }
            )

        if self.has_feature(self.FEATURE_BATTERY):
            self.attributes.update(
                {
                    "BatVoltage": None,
                    "BatPercentRemaining": None,
                    "BatTimeRemaining": None,
                    "BatChargeLevel": BatChargeLevelEnum.OK,
                    "BatReplacementNeeded": False,
                    "BatReplaceability": BatReplaceabilityEnum.UNSPECIFIED,
                    "BatPresent": True,
                    "ActiveBatFaults": [],
                    "BatReplacementDescription": "",
                    "BatCommonDesignation": BatCommonDesignationEnum.UNSPECIFIED,
                    "BatANSIDesignation": "",
                    "BatIECDesignation": "",
                    "BatApprovedChemistry": BatApprovedChemistryEnum.UNSPECIFIED,
                    "BatCapacity": 0,
                    "BatQuantity": 1,
                    "BatChargeState": BatChargeStateEnum.UNKNOWN,
                    "BatTimeToFullCharge": None,
                    "BatFunctionalWhileCharging": True,

                    "ActiveBatRadioFaults": [],
                    "BatRadioFaultHistory": [],
                }
            )

        if self.has_feature(self.FEATURE_RECHARGEABLE):
            self.attributes.update(
                {
                    "BatChargingCurrent": None,
                    "ActiveBatChargeFaults": [],
                }
            )

    def write_attribute(self, attribute_id: str, value):
        
        if attribute_id == "BatPercentRemaining":
            return self.update_battery_percentage(value)
        if attribute_id == "BatChargingCurrent":
            return self.update_charging_current(value)
        if attribute_id == "BatTimeToFullCharge":
            return self.update_time_to_full_charge(value)
        return super().write_attribute(attribute_id, value)

    def has_feature(self, feature: int) -> bool:
        
        return (self.features & feature) != 0

    def set_status(self, status: PowerSourceStatusEnum):
        
        self.attributes["Status"] = status
        return Result.ok(None)

    def set_description(self, description: str):
        
        if len(description) > 60:
            return Result.fail(
                ErrorCode.INVALID_ARGUMENT, "Description too long (max 60 chars)"
            )

        self.attributes["Description"] = description
        return Result.ok(None)

    def set_order(self, order: int):
        
        if not (0 <= order <= 255):
            return Result.fail(ErrorCode.INVALID_ARGUMENT, "Order must be 0-255")

        self.attributes["Order"] = order
        return Result.ok(None)

    def add_endpoint(self, endpoint_id: int):
        
        if not (0 <= endpoint_id <= 65535):
            return Result.fail(
                ErrorCode.INVALID_ARGUMENT, "Endpoint ID must be 0-65535"
            )

        if endpoint_id not in self.attributes["EndpointList"]:
            self.attributes["EndpointList"].append(endpoint_id)
        return Result.ok(None)

    def remove_endpoint(self, endpoint_id: int):
        
        if endpoint_id in self.attributes["EndpointList"]:
            self.attributes["EndpointList"].remove(endpoint_id)
        return Result.ok(None)

    def set_endpoint_list(self, endpoint_list: list):
        
        for endpoint_id in endpoint_list:
            if not (0 <= endpoint_id <= 65535):
                return Result.fail(
                    ErrorCode.INVALID_ARGUMENT, f"Invalid endpoint ID: {endpoint_id}"
                )

        self.attributes["EndpointList"] = endpoint_list.copy()
        return Result.ok(None)


    def update_wired_voltage(self, voltage: Optional[int]):
        
        if not self.has_feature(self.FEATURE_WIRED):
            return Result.fail(
                ErrorCode.UNSUPPORTED_COMMAND, "Wired feature not supported"
            )

        self.attributes["WiredAssessedInputVoltage"] = voltage
        return Result.ok(None)

    def update_wired_current(self, current: Optional[int]):
        
        if not self.has_feature(self.FEATURE_WIRED):
            return Result.fail(
                ErrorCode.UNSUPPORTED_COMMAND, "Wired feature not supported"
            )

        self.attributes["WiredAssessedCurrent"] = current
        return Result.ok(None)

    def update_wired_frequency(self, frequency: Optional[int]):
        
        if not self.has_feature(self.FEATURE_WIRED):
            return Result.fail(
                ErrorCode.UNSUPPORTED_COMMAND, "Wired feature not supported"
            )

        self.attributes["WiredAssessedInputFrequency"] = frequency
        return Result.ok(None)

    def set_wired_present(self, present: bool):
        
        if not self.has_feature(self.FEATURE_WIRED):
            return Result.fail(
                ErrorCode.UNSUPPORTED_COMMAND, "Wired feature not supported"
            )

        self.attributes["WiredPresent"] = present
        return Result.ok(None)

    def add_wired_fault(self, fault: WiredFaultTypeEnum):
        
        if not self.has_feature(self.FEATURE_WIRED):
            return Result.fail(
                ErrorCode.UNSUPPORTED_COMMAND, "Wired feature not supported"
            )

        if fault not in self.attributes["ActiveWiredFaults"]:
            self.attributes["ActiveWiredFaults"].append(fault)
        return Result.ok(None)

    def clear_wired_fault(self, fault: WiredFaultTypeEnum):
        
        if not self.has_feature(self.FEATURE_WIRED):
            return Result.fail(
                ErrorCode.UNSUPPORTED_COMMAND, "Wired feature not supported"
            )

        if fault in self.attributes["ActiveWiredFaults"]:
            self.attributes["ActiveWiredFaults"].remove(fault)
        return Result.ok(None)


    def update_battery_voltage(self, voltage: Optional[int]):
        
        if not self.has_feature(self.FEATURE_BATTERY):
            return Result.fail(
                ErrorCode.UNSUPPORTED_COMMAND, "Battery feature not supported"
            )

        self.attributes["BatVoltage"] = voltage
        return Result.ok(None)

    def update_battery_percentage(self, percentage: Optional[int]):
        
        if not self.has_feature(self.FEATURE_BATTERY):
            return Result.fail(
                ErrorCode.UNSUPPORTED_COMMAND, "Battery feature not supported"
            )

        if percentage is not None and not (0 <= percentage <= 100):
            return Result.fail(ErrorCode.INVALID_ARGUMENT, "Percentage must be 0-100")

        self.attributes["BatPercentRemaining"] = percentage


        if percentage is not None:
            if percentage <= 10:
                self.attributes["BatChargeLevel"] = BatChargeLevelEnum.CRITICAL
            elif percentage <= 20:
                self.attributes["BatChargeLevel"] = BatChargeLevelEnum.WARNING
            else:
                self.attributes["BatChargeLevel"] = BatChargeLevelEnum.OK

        return Result.ok(None)

    def update_battery_time_remaining(self, time_remaining: Optional[int]):
        
        if not self.has_feature(self.FEATURE_BATTERY):
            return Result.fail(
                ErrorCode.UNSUPPORTED_COMMAND, "Battery feature not supported"
            )

        self.attributes["BatTimeRemaining"] = time_remaining
        return Result.ok(None)

    def set_battery_replacement_needed(self, needed: bool):
        
        if not self.has_feature(self.FEATURE_BATTERY):
            return Result.fail(
                ErrorCode.UNSUPPORTED_COMMAND, "Battery feature not supported"
            )

        self.attributes["BatReplacementNeeded"] = needed
        return Result.ok(None)

    def set_battery_present(self, present: bool):
        
        if not self.has_feature(self.FEATURE_BATTERY):
            return Result.fail(
                ErrorCode.UNSUPPORTED_COMMAND, "Battery feature not supported"
            )

        self.attributes["BatPresent"] = present
        return Result.ok(None)

    def set_battery_charge_state(self, state: BatChargeStateEnum):
        
        if not self.has_feature(self.FEATURE_BATTERY):
            return Result.fail(
                ErrorCode.UNSUPPORTED_COMMAND, "Battery feature not supported"
            )

        self.attributes["BatChargeState"] = state
        return Result.ok(None)

    def set_battery_functional_while_charging(self, functional: bool):
        
        if not self.has_feature(self.FEATURE_BATTERY):
            return Result.fail(
                ErrorCode.UNSUPPORTED_COMMAND, "Battery feature not supported"
            )

        self.attributes["BatFunctionalWhileCharging"] = functional
        return Result.ok(None)

    def add_battery_fault(self, fault: BatFaultTypeEnum):
        
        if not self.has_feature(self.FEATURE_BATTERY):
            return Result.fail(
                ErrorCode.UNSUPPORTED_COMMAND, "Battery feature not supported"
            )

        if fault not in self.attributes["ActiveBatFaults"]:
            self.attributes["ActiveBatFaults"].append(fault)
        return Result.ok(None)

    def clear_battery_fault(self, fault: BatFaultTypeEnum):
        
        if not self.has_feature(self.FEATURE_BATTERY):
            return Result.fail(
                ErrorCode.UNSUPPORTED_COMMAND, "Battery feature not supported"
            )

        if fault in self.attributes["ActiveBatFaults"]:
            self.attributes["ActiveBatFaults"].remove(fault)
        return Result.ok(None)

    def add_battery_radio_fault(self, fault: RadioFaultEnum):
        
        if not self.has_feature(self.FEATURE_BATTERY):
            return Result.fail(
                ErrorCode.UNSUPPORTED_COMMAND, "Battery feature not supported"
            )

        if fault not in self.attributes["ActiveBatRadioFaults"]:
            self.attributes["ActiveBatRadioFaults"].append(fault)

            if fault not in self.attributes["BatRadioFaultHistory"]:
                self.attributes["BatRadioFaultHistory"].append(fault)
        return Result.ok(None)

    def clear_battery_radio_fault(self, fault: RadioFaultEnum):
        
        if not self.has_feature(self.FEATURE_BATTERY):
            return Result.fail(
                ErrorCode.UNSUPPORTED_COMMAND, "Battery feature not supported"
            )

        if fault in self.attributes["ActiveBatRadioFaults"]:
            self.attributes["ActiveBatRadioFaults"].remove(fault)
        return Result.ok(None)

    def clear_battery_radio_fault_history(self):
        
        if not self.has_feature(self.FEATURE_BATTERY):
            return Result.fail(
                ErrorCode.UNSUPPORTED_COMMAND, "Battery feature not supported"
            )

        self.attributes["BatRadioFaultHistory"] = []
        return Result.ok(None)

    def set_battery_specifications(
        self,
        capacity: int,
        quantity: int = 1,
        chemistry: BatApprovedChemistryEnum = BatApprovedChemistryEnum.UNSPECIFIED,
        designation: BatCommonDesignationEnum = BatCommonDesignationEnum.UNSPECIFIED,
        ansi_designation: str = "",
        iec_designation: str = "",
        replacement_description: str = "",
    ):
        
        if not self.has_feature(self.FEATURE_BATTERY):
            return Result.fail(
                ErrorCode.UNSUPPORTED_COMMAND, "Battery feature not supported"
            )

        if capacity < 0:
            return Result.fail(
                ErrorCode.INVALID_ARGUMENT, "Capacity must be non-negative"
            )

        if not (1 <= quantity <= 255):
            return Result.fail(ErrorCode.INVALID_ARGUMENT, "Quantity must be 1-255")

        if len(ansi_designation) > 20:
            return Result.fail(
                ErrorCode.INVALID_ARGUMENT, "ANSI designation too long (max 20 chars)"
            )

        if len(iec_designation) > 20:
            return Result.fail(
                ErrorCode.INVALID_ARGUMENT, "IEC designation too long (max 20 chars)"
            )

        if len(replacement_description) > 60:
            return Result.fail(
                ErrorCode.INVALID_ARGUMENT,
                "Replacement description too long (max 60 chars)",
            )

        self.attributes["BatCapacity"] = capacity
        self.attributes["BatQuantity"] = quantity
        self.attributes["BatApprovedChemistry"] = chemistry
        self.attributes["BatCommonDesignation"] = designation
        self.attributes["BatANSIDesignation"] = ansi_designation
        self.attributes["BatIECDesignation"] = iec_designation
        self.attributes["BatReplacementDescription"] = replacement_description

        return Result.ok(None)


    def update_charging_current(self, current: Optional[int]):
        
        if not self.has_feature(self.FEATURE_RECHARGEABLE):
            return Result.fail(
                ErrorCode.UNSUPPORTED_COMMAND, "Rechargeable feature not supported"
            )

        self.attributes["BatChargingCurrent"] = current
        return Result.ok(None)

    def update_time_to_full_charge(self, time_to_full: Optional[int]):
        
        if not self.has_feature(self.FEATURE_BATTERY):
            return Result.fail(
                ErrorCode.UNSUPPORTED_COMMAND, "Battery feature not supported"
            )

        self.attributes["BatTimeToFullCharge"] = time_to_full
        return Result.ok(None)

    def add_charge_fault(self, fault: BatChargeFaultTypeEnum):
        
        if not self.has_feature(self.FEATURE_RECHARGEABLE):
            return Result.fail(
                ErrorCode.UNSUPPORTED_COMMAND, "Rechargeable feature not supported"
            )

        if fault not in self.attributes["ActiveBatChargeFaults"]:
            self.attributes["ActiveBatChargeFaults"].append(fault)
        return Result.ok(None)

    def clear_charge_fault(self, fault: BatChargeFaultTypeEnum):
        
        if not self.has_feature(self.FEATURE_RECHARGEABLE):
            return Result.fail(
                ErrorCode.UNSUPPORTED_COMMAND, "Rechargeable feature not supported"
            )

        if fault in self.attributes["ActiveBatChargeFaults"]:
            self.attributes["ActiveBatChargeFaults"].remove(fault)
        return Result.ok(None)

    def start_charging(self):
        
        if not self.has_feature(self.FEATURE_RECHARGEABLE):
            return Result.fail(
                ErrorCode.UNSUPPORTED_COMMAND, "Rechargeable feature not supported"
            )

        if not self.attributes.get("BatPresent", False):
            return Result.fail(ErrorCode.INVALID_STATE, "Battery not present")

        self.attributes["BatChargeState"] = BatChargeStateEnum.IS_CHARGING
        return Result.ok(None)

    def stop_charging(self):
        
        if not self.has_feature(self.FEATURE_RECHARGEABLE):
            return Result.fail(
                ErrorCode.UNSUPPORTED_COMMAND, "Rechargeable feature not supported"
            )

        current_state = self.attributes.get(
            "BatChargeState", BatChargeStateEnum.UNKNOWN
        )
        if current_state == BatChargeStateEnum.IS_CHARGING:
            self.attributes["BatChargeState"] = BatChargeStateEnum.IS_NOT_CHARGING

        return Result.ok(None)

    def simulate_battery_discharge(self, discharge_rate: int = 1):
        
        if not self.has_feature(self.FEATURE_BATTERY):
            return Result.fail(
                ErrorCode.UNSUPPORTED_COMMAND, "Battery feature not supported"
            )

        current_percentage = self.attributes.get("BatPercentRemaining")
        if current_percentage is not None and current_percentage > 0:
            new_percentage = max(0, current_percentage - discharge_rate)
            self.update_battery_percentage(new_percentage)

        return Result.ok(None)

    def simulate_battery_charge(self, charge_rate: int = 1):
        
        if not self.has_feature(self.FEATURE_RECHARGEABLE):
            return Result.fail(
                ErrorCode.UNSUPPORTED_COMMAND, "Rechargeable feature not supported"
            )

        current_percentage = self.attributes.get("BatPercentRemaining")
        if current_percentage is not None and current_percentage < 100:
            new_percentage = min(100, current_percentage + charge_rate)
            self.update_battery_percentage(new_percentage)


            if new_percentage == 100:
                self.attributes["BatChargeState"] = BatChargeStateEnum.IS_AT_FULL_CHARGE
            elif self.attributes["BatChargeState"] != BatChargeStateEnum.IS_CHARGING:
                self.attributes["BatChargeState"] = BatChargeStateEnum.IS_CHARGING

        return Result.ok(None)

    def __str__(self) -> str:
        
        features_str = []
        if self.has_feature(self.FEATURE_WIRED):
            features_str.append("WIRED")
        if self.has_feature(self.FEATURE_BATTERY):
            features_str.append("BATTERY")
        if self.has_feature(self.FEATURE_RECHARGEABLE):
            features_str.append("RECHARGEABLE")
        if self.has_feature(self.FEATURE_REPLACEABLE):
            features_str.append("REPLACEABLE")

        features_display = ",".join(features_str) if features_str else "None"

        battery_info = ""
        if self.has_feature(self.FEATURE_BATTERY):
            percentage = self.attributes.get("BatPercentRemaining")
            charge_level = self.attributes.get(
                "BatChargeLevel", BatChargeLevelEnum.OK
            ).name
            battery_info = f", Battery={percentage}%({charge_level})"

        return (
            f"PowerSourceCluster("
            f"Status={self.attributes['Status'].name}, "
            f"Features=[{features_display}]"
            f"{battery_info})"
        )
