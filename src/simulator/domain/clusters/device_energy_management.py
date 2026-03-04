from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any
from enum import Enum
import time

from src.simulator.domain.clusters.base import Cluster
from src.simulator.domain.result import Result, ErrorCode


class CostTypeEnum(Enum):
    

    FINANCIAL = 0
    GHG_EMISSIONS = 1
    COMFORT = 2
    TEMPERATURE = 3


class ESATypeEnum(Enum):
    

    EVSE = 0
    SPACE_HEATING = 1
    WATER_HEATING = 2
    SPACE_COOLING = 3
    SPACE_HEATING_COOLING = 4
    BATTERY_STORAGE = 5
    SOLAR_PV = 6
    FRIDGE_FREEZER = 7
    WASHING_MACHINE = 8
    DISHWASHER = 9
    COOKING = 10
    HOME_WATER_PUMP = 11
    IRRIGATION_WATER_PUMP = 12
    POOL_PUMP = 13
    OTHER = 255


class ESAStateEnum(Enum):
    

    OFFLINE = 0
    ONLINE = 1
    FAULT = 2
    POWER_ADJUST_ACTIVE = 3
    PAUSED = 4


class OptOutStateEnum(Enum):
    

    NO_OPT_OUT = 0
    LOCAL_OPT_OUT = 1
    GRID_OPT_OUT = 2
    OPT_OUT = 3


class CauseEnum(Enum):
    

    NORMAL_COMPLETION = 0
    OFFLINE = 1
    FAULT = 2
    USER_OPT_OUT = 3
    CANCELLED = 4


class AdjustmentCauseEnum(Enum):
    

    LOCAL_OPTIMIZATION = 0
    GRID_OPTIMIZATION = 1


class ForecastUpdateReasonEnum(Enum):
    

    INTERNAL_OPTIMIZATION = 0
    LOCAL_OPTIMIZATION = 1
    GRID_OPTIMIZATION = 2


class PowerAdjustReasonEnum(Enum):
    

    NO_ADJUSTMENT = 0
    LOCAL_OPTIMIZATION_ADJUSTMENT = 1
    GRID_OPTIMIZATION_ADJUSTMENT = 2


@dataclass
class CostStruct:
    

    cost_type: CostTypeEnum
    value: int
    decimal_points: int = 0
    currency: Optional[int] = None


@dataclass
class PowerAdjustStruct:
    

    min_power: int = 0
    max_power: int = 0
    min_duration: int = 0
    max_duration: int = 0


@dataclass
class PowerAdjustCapabilityStruct:
    

    power_adjust_capability: List[PowerAdjustStruct] = field(
        default_factory=list
    )
    cause: PowerAdjustReasonEnum = PowerAdjustReasonEnum.NO_ADJUSTMENT


@dataclass
class SlotStruct:
    

    min_duration: int
    max_duration: int
    default_duration: int
    electricity_energy_demanded: int = 0
    max_electricity_energy_demanded: int = 0
    min_power_demanded: int = 0
    max_power_demanded: int = 0
    min_pause_duration: int = 0
    max_pause_duration: int = 0
    manufacture_specific_data: int = 0
    nominal_power: int = 0
    min_power_adjustment: int = 0
    max_power_adjustment: int = 0
    slot_is_pausable: bool = False
    min_pausable_duration: int = 0
    costs: List[CostStruct] = field(default_factory=list)


@dataclass
class ForecastStruct:
    

    forecast_id: int
    active_slot_number: Optional[int] = None
    start_time: int = 0
    end_time: int = 0
    earliest_start_time: Optional[int] = None
    latest_end_time: Optional[int] = None
    is_pausable: bool = False
    slots: List[SlotStruct] = field(default_factory=list)
    forecast_update_reason: ForecastUpdateReasonEnum = (
        ForecastUpdateReasonEnum.INTERNAL_OPTIMIZATION
    )


@dataclass
class PowerAdjustRequest:
    

    power: int
    duration: int
    cause: AdjustmentCauseEnum


@dataclass
class StartTimeAdjustRequest:
    

    requested_start_time: int
    cause: AdjustmentCauseEnum


@dataclass
class PauseRequest:
    

    duration: int
    cause: AdjustmentCauseEnum


@dataclass
class ResumeRequest:
    

    cause: AdjustmentCauseEnum


@dataclass
class ModifyForecastRequest:
    

    forecast_id: int
    slot_adjustments: List[SlotStruct]
    cause: AdjustmentCauseEnum


@dataclass
class PowerAdjustStart:
        pass


@dataclass
class PowerAdjustEnd:
    

    cause: CauseEnum
    duration: int


@dataclass
class Paused:
        pass


@dataclass
class Resumed:
    

    cause: CauseEnum


class DeviceEnergyManagementCluster(Cluster):
    

    FEATURE_PA = 0x01
    FEATURE_PFR = 0x02
    FEATURE_SFR = 0x04
    FEATURE_CON = 0x08
    FEATURE_STA = 0x10
    FEATURE_PAU = 0x20
    FEATURE_FA = 0x40

    def __init__(
        self,
        esa_type: ESATypeEnum = ESATypeEnum.OTHER,
        esa_can_generate: bool = False,
        features: int = 0,
    ):
        
        super().__init__(cluster_id="DeviceEnergyManagement")

        self.features = features
        self._forecast_id_counter = 0


        self.attributes = {
            "ESAType": esa_type,
            "ESACanGenerate": esa_can_generate,
            "ESAState": ESAStateEnum.OFFLINE,
            "AbsMinPower": 0,
            "AbsMaxPower": 0,
        }


        self.readonly_attributes = {"ESAType", "ESACanGenerate", "AbsMinPower", "AbsMaxPower"}


        if self.has_feature(self.FEATURE_PA):
            self.attributes.update(
                {
                    "PowerAdjustmentCapability": PowerAdjustCapabilityStruct(),
                }
            )

        if self.has_feature(self.FEATURE_PFR):
            self.attributes.update(
                {
                    "Forecast": None,
                }
            )

        if self.has_feature(self.FEATURE_CON):
            self.attributes.update(
                {
                    "OptOutState": OptOutStateEnum.NO_OPT_OUT,
                }
            )

    def has_feature(self, feature: int) -> bool:
        
        return (self.features & feature) != 0

    def set_esa_state(self, state: ESAStateEnum):
        
        self.attributes["ESAState"] = state
        return Result.ok(None)

    def set_power_limits(self, abs_min_power: int, abs_max_power: int):
        
        if abs_max_power < abs_min_power:
            return Result.fail(
                ErrorCode.INVALID_ARGUMENT, "Max power must be >= min power"
            )

        self.attributes["AbsMinPower"] = abs_min_power
        self.attributes["AbsMaxPower"] = abs_max_power
        return Result.ok(None)

    def update_power_adjustment_capability(self, capabilities: List[PowerAdjustStruct]):
        
        if not self.has_feature(self.FEATURE_PA):
            return Result.fail(
                ErrorCode.UNSUPPORTED_COMMAND, "Power adjustment feature not supported"
            )

        if len(capabilities) > 8:
            return Result.fail(
                ErrorCode.INVALID_ARGUMENT,
                "Too many power adjustment capabilities (max 8)",
            )

        self.attributes["PowerAdjustmentCapability"] = PowerAdjustCapabilityStruct(
            power_adjust_capability=capabilities,
            cause=PowerAdjustReasonEnum.NO_ADJUSTMENT,
        )
        return Result.ok(None)

    def create_forecast(
        self,
        slots: List[SlotStruct],
        start_time: int,
        end_time: int,
        earliest_start_time: Optional[int] = None,
        latest_end_time: Optional[int] = None,
    ):
        
        if not self.has_feature(self.FEATURE_PFR):
            return Result.fail(
                ErrorCode.UNSUPPORTED_COMMAND,
                "Power forecast reporting feature not supported",
            )

        if not slots or len(slots) > 10:
            return Result.fail(
                ErrorCode.INVALID_ARGUMENT, "Invalid number of slots (1-10 required)"
            )

        if end_time <= start_time:
            return Result.fail(
                ErrorCode.INVALID_ARGUMENT, "End time must be after start time"
            )

        self._forecast_id_counter += 1


        is_pausable = any(slot.slot_is_pausable for slot in slots)

        forecast = ForecastStruct(
            forecast_id=self._forecast_id_counter,
            start_time=start_time,
            end_time=end_time,
            earliest_start_time=earliest_start_time,
            latest_end_time=latest_end_time,
            is_pausable=is_pausable,
            slots=slots,
            forecast_update_reason=ForecastUpdateReasonEnum.INTERNAL_OPTIMIZATION,
        )

        self.attributes["Forecast"] = forecast
        return Result.ok(forecast)

    def set_opt_out_state(self, state: OptOutStateEnum):
        
        if not self.has_feature(self.FEATURE_CON):
            return Result.fail(
                ErrorCode.UNSUPPORTED_COMMAND,
                "Constraint-based adjustment feature not supported",
            )

        self.attributes["OptOutState"] = state
        return Result.ok(None)


    def handle_power_adjust_request(self, request: PowerAdjustRequest):
        
        if not self.has_feature(self.FEATURE_PA):
            return Result.fail(
                ErrorCode.UNSUPPORTED_COMMAND, "Power adjustment not supported"
            )

        if self.attributes["ESAState"] != ESAStateEnum.ONLINE:
            return Result.fail(ErrorCode.INVALID_STATE, "ESA not online")


        abs_min_power = self.attributes["AbsMinPower"]
        abs_max_power = self.attributes["AbsMaxPower"]

        if not (abs_min_power <= request.power <= abs_max_power):
            return Result.fail(
                ErrorCode.CONSTRAINT_ERROR, "Power outside absolute limits"
            )


        capability = self.attributes.get("PowerAdjustmentCapability")
        if capability and capability.power_adjust_capability:

            compatible = False
            for cap in capability.power_adjust_capability:
                if (
                    cap.min_power <= request.power <= cap.max_power
                    and cap.min_duration <= request.duration <= cap.max_duration
                ):
                    compatible = True
                    break

            if not compatible:
                return Result.fail(
                    ErrorCode.CONSTRAINT_ERROR,
                    "No compatible power adjustment capability",
                )


        self.attributes["ESAState"] = ESAStateEnum.POWER_ADJUST_ACTIVE


        if capability:
            if request.cause == AdjustmentCauseEnum.LOCAL_OPTIMIZATION:
                capability.cause = PowerAdjustReasonEnum.LOCAL_OPTIMIZATION_ADJUSTMENT
            else:
                capability.cause = PowerAdjustReasonEnum.GRID_OPTIMIZATION_ADJUSTMENT

        return Result.ok(None)

    def handle_cancel_power_adjust_request(self):
        
        if not self.has_feature(self.FEATURE_PA):
            return Result.fail(
                ErrorCode.UNSUPPORTED_COMMAND, "Power adjustment not supported"
            )

        if self.attributes["ESAState"] == ESAStateEnum.POWER_ADJUST_ACTIVE:
            self.attributes["ESAState"] = ESAStateEnum.ONLINE


            capability = self.attributes.get("PowerAdjustmentCapability")
            if capability:
                capability.cause = PowerAdjustReasonEnum.NO_ADJUSTMENT

        return Result.ok(None)

    def handle_start_time_adjust_request(self, request: StartTimeAdjustRequest):
        
        if not self.has_feature(self.FEATURE_STA):
            return Result.fail(
                ErrorCode.UNSUPPORTED_COMMAND, "Start time adjustment not supported"
            )

        forecast = self.attributes.get("Forecast")
        if not forecast:
            return Result.fail(ErrorCode.INVALID_STATE, "No active forecast")


        if (
            forecast.earliest_start_time
            and request.requested_start_time < forecast.earliest_start_time
        ):
            return Result.fail(
                ErrorCode.CONSTRAINT_ERROR, "Requested start time too early"
            )

        if forecast.latest_end_time:
            forecast_duration = forecast.end_time - forecast.start_time
            latest_start = forecast.latest_end_time - forecast_duration
            if request.requested_start_time > latest_start:
                return Result.fail(
                    ErrorCode.CONSTRAINT_ERROR, "Requested start time too late"
                )


        time_shift = request.requested_start_time - forecast.start_time
        forecast.start_time = request.requested_start_time
        forecast.end_time += time_shift
        forecast.forecast_update_reason = (
            ForecastUpdateReasonEnum.LOCAL_OPTIMIZATION
            if request.cause == AdjustmentCauseEnum.LOCAL_OPTIMIZATION
            else ForecastUpdateReasonEnum.GRID_OPTIMIZATION
        )

        return Result.ok(None)

    def handle_pause_request(self, request: PauseRequest):
        
        if not self.has_feature(self.FEATURE_PAU):
            return Result.fail(
                ErrorCode.UNSUPPORTED_COMMAND, "Pausable feature not supported"
            )

        forecast = self.attributes.get("Forecast")
        if not forecast or not forecast.is_pausable:
            return Result.fail(ErrorCode.INVALID_STATE, "Forecast not pausable")

        if self.attributes["ESAState"] != ESAStateEnum.ONLINE:
            return Result.fail(
                ErrorCode.INVALID_STATE, "ESA not in correct state for pausing"
            )

        self.attributes["ESAState"] = ESAStateEnum.PAUSED
        return Result.ok(None)

    def handle_resume_request(self, request: ResumeRequest):
        
        if not self.has_feature(self.FEATURE_PAU):
            return Result.fail(
                ErrorCode.UNSUPPORTED_COMMAND, "Pausable feature not supported"
            )

        if self.attributes["ESAState"] != ESAStateEnum.PAUSED:
            return Result.fail(ErrorCode.INVALID_STATE, "ESA not paused")

        self.attributes["ESAState"] = ESAStateEnum.ONLINE
        return Result.ok(None)

    def handle_modify_forecast_request(self, request: ModifyForecastRequest):
        
        if not self.has_feature(self.FEATURE_FA):
            return Result.fail(
                ErrorCode.UNSUPPORTED_COMMAND, "Forecast adjustment not supported"
            )

        forecast = self.attributes.get("Forecast")
        if not forecast or forecast.forecast_id != request.forecast_id:
            return Result.fail(
                ErrorCode.INVALID_STATE, "Forecast ID mismatch or no active forecast"
            )

        if len(request.slot_adjustments) > 10:
            return Result.fail(
                ErrorCode.INVALID_ARGUMENT, "Too many slot adjustments (max 10)"
            )


        forecast.slots = request.slot_adjustments
        forecast.forecast_update_reason = (
            ForecastUpdateReasonEnum.LOCAL_OPTIMIZATION
            if request.cause == AdjustmentCauseEnum.LOCAL_OPTIMIZATION
            else ForecastUpdateReasonEnum.GRID_OPTIMIZATION
        )


        forecast.is_pausable = any(slot.slot_is_pausable for slot in forecast.slots)

        return Result.ok(None)

    def __str__(self) -> str:
        
        features_str = []
        if self.has_feature(self.FEATURE_PA):
            features_str.append("PA")
        if self.has_feature(self.FEATURE_PFR):
            features_str.append("PFR")
        if self.has_feature(self.FEATURE_SFR):
            features_str.append("SFR")
        if self.has_feature(self.FEATURE_CON):
            features_str.append("CON")
        if self.has_feature(self.FEATURE_STA):
            features_str.append("STA")
        if self.has_feature(self.FEATURE_PAU):
            features_str.append("PAU")
        if self.has_feature(self.FEATURE_FA):
            features_str.append("FA")

        features_display = ",".join(features_str) if features_str else "None"

        return (
            f"DeviceEnergyManagementCluster("
            f"ESAType={self.attributes['ESAType'].name}, "
            f"ESAState={self.attributes['ESAState'].name}, "
            f"Features=[{features_display}], "
            f"AbsMinPower={self.attributes['AbsMinPower']}, "
            f"AbsMaxPower={self.attributes['AbsMaxPower']})"
        )
