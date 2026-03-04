from __future__ import annotations

from dataclasses import dataclass
from enum import IntEnum
from typing import Optional

from src.simulator.domain.clusters.base import Cluster
from src.simulator.domain.result import ErrorCode, Result


INT64_MIN_62 = -(1 << 62)
INT64_MAX_62 = 1 << 62


class PowerModeEnum(IntEnum):
    UNKNOWN = 0
    DC = 1
    AC = 2


class ElectricalPowerMeasurementFeature(IntEnum):
    DIRECT_CURRENT = 0x01
    ALTERNATING_CURRENT = 0x02
    POLYPHASE_POWER = 0x04
    HARMONICS = 0x08
    POWER_QUALITY = 0x10


class MeasurementTypeEnum(IntEnum):
    VOLTAGE = 0x01
    ACTIVE_CURRENT = 0x02
    REACTIVE_CURRENT = 0x03
    APPARENT_CURRENT = 0x04
    ACTIVE_POWER = 0x05
    REACTIVE_POWER = 0x06
    APPARENT_POWER = 0x07
    RMS_VOLTAGE = 0x08
    RMS_CURRENT = 0x09
    RMS_POWER = 0x0A
    FREQUENCY = 0x0B
    POWER_FACTOR = 0x0C
    NEUTRAL_CURRENT = 0x0D


@dataclass
class MeasurementAccuracyRangeStruct:
    RangeMin: int
    RangeMax: int
    PercentMax: Optional[int] = None
    PercentMin: Optional[int] = None
    PercentTypical: Optional[int] = None
    FixedMax: Optional[int] = None
    FixedMin: Optional[int] = None
    FixedTypical: Optional[int] = None


@dataclass
class MeasurementAccuracyStruct:
    MeasurementType: MeasurementTypeEnum
    Measured: bool
    MinMeasuredValue: int
    MaxMeasuredValue: int
    AccuracyRanges: list[MeasurementAccuracyRangeStruct]


@dataclass
class MeasurementRangeStruct:
    MeasurementType: MeasurementTypeEnum
    Min: int
    Max: int
    StartTimestamp: Optional[int] = None
    EndTimestamp: Optional[int] = None
    MinTimestamp: Optional[int] = None
    MaxTimestamp: Optional[int] = None
    StartSystime: Optional[int] = None
    EndSystime: Optional[int] = None
    MinSystime: Optional[int] = None
    MaxSystime: Optional[int] = None


@dataclass
class HarmonicMeasurementStruct:
    Order: int
    Measurement: Optional[int] = None


class ElectricalPowerMeasurementCluster(Cluster):
    CLUSTER_REVISION = 1

    FEATURE_DIRC = int(ElectricalPowerMeasurementFeature.DIRECT_CURRENT)
    FEATURE_ALTC = int(ElectricalPowerMeasurementFeature.ALTERNATING_CURRENT)
    FEATURE_POLY = int(ElectricalPowerMeasurementFeature.POLYPHASE_POWER)
    FEATURE_HARM = int(ElectricalPowerMeasurementFeature.HARMONICS)
    FEATURE_PWRQ = int(ElectricalPowerMeasurementFeature.POWER_QUALITY)

    _ALTC_ATTRIBUTES = {
        "ReactiveCurrent",
        "ApparentCurrent",
        "ReactivePower",
        "ApparentPower",
        "RMSVoltage",
        "RMSCurrent",
        "RMSPower",
        "Frequency",
        "PowerFactor",
    }
    _HARM_ATTRIBUTES = {"HarmonicCurrents"}
    _PWRQ_ATTRIBUTES = {"HarmonicPhases"}
    _POLY_ATTRIBUTES = {"NeutralCurrent"}
    _UNCONDITIONED_OPTIONAL_ATTRIBUTES = {
        "Ranges",
        "Voltage",
        "ActiveCurrent",
    }
    _VALID_OPTIONAL_ATTRIBUTES = (
        _UNCONDITIONED_OPTIONAL_ATTRIBUTES
        | _ALTC_ATTRIBUTES
        | _HARM_ATTRIBUTES
        | _PWRQ_ATTRIBUTES
        | _POLY_ATTRIBUTES
    )

    _ATTRIBUTE_TO_MEASUREMENT_TYPE = {
        "Voltage": MeasurementTypeEnum.VOLTAGE,
        "ActiveCurrent": MeasurementTypeEnum.ACTIVE_CURRENT,
        "ReactiveCurrent": MeasurementTypeEnum.REACTIVE_CURRENT,
        "ApparentCurrent": MeasurementTypeEnum.APPARENT_CURRENT,
        "ActivePower": MeasurementTypeEnum.ACTIVE_POWER,
        "ReactivePower": MeasurementTypeEnum.REACTIVE_POWER,
        "ApparentPower": MeasurementTypeEnum.APPARENT_POWER,
        "RMSVoltage": MeasurementTypeEnum.RMS_VOLTAGE,
        "RMSCurrent": MeasurementTypeEnum.RMS_CURRENT,
        "RMSPower": MeasurementTypeEnum.RMS_POWER,
        "Frequency": MeasurementTypeEnum.FREQUENCY,
        "PowerFactor": MeasurementTypeEnum.POWER_FACTOR,
        "NeutralCurrent": MeasurementTypeEnum.NEUTRAL_CURRENT,
    }
    _MEASUREMENT_TYPE_TO_ATTRIBUTE = {
        measurement_type: attribute
        for attribute, measurement_type in _ATTRIBUTE_TO_MEASUREMENT_TYPE.items()
    }
    _MEASUREMENT_LIMITS = {
        MeasurementTypeEnum.VOLTAGE: (INT64_MIN_62, INT64_MAX_62),
        MeasurementTypeEnum.ACTIVE_CURRENT: (INT64_MIN_62, INT64_MAX_62),
        MeasurementTypeEnum.REACTIVE_CURRENT: (INT64_MIN_62, INT64_MAX_62),
        MeasurementTypeEnum.APPARENT_CURRENT: (0, INT64_MAX_62),
        MeasurementTypeEnum.ACTIVE_POWER: (INT64_MIN_62, INT64_MAX_62),
        MeasurementTypeEnum.REACTIVE_POWER: (INT64_MIN_62, INT64_MAX_62),
        MeasurementTypeEnum.APPARENT_POWER: (INT64_MIN_62, INT64_MAX_62),
        MeasurementTypeEnum.RMS_VOLTAGE: (INT64_MIN_62, INT64_MAX_62),
        MeasurementTypeEnum.RMS_CURRENT: (INT64_MIN_62, INT64_MAX_62),
        MeasurementTypeEnum.RMS_POWER: (INT64_MIN_62, INT64_MAX_62),
        MeasurementTypeEnum.FREQUENCY: (0, 1_000_000),
        MeasurementTypeEnum.POWER_FACTOR: (-10_000, 10_000),
        MeasurementTypeEnum.NEUTRAL_CURRENT: (INT64_MIN_62, INT64_MAX_62),
    }

    def __init__(
        self,
        *,
        power_mode: PowerModeEnum = PowerModeEnum.UNKNOWN,
        feature_map: int = 0,
        optional_attributes: set[str] | None = None,
    ):
        super().__init__(cluster_id="ElectricalPowerMeasurement")

        self.feature_map: int = int(feature_map)
        self._validate_feature_map()

        optional_attr_set = set(optional_attributes or set())
        self._validate_optional_attributes(optional_attr_set)

        try:
            normalized_power_mode = PowerModeEnum(int(power_mode))
        except (TypeError, ValueError):
            normalized_power_mode = PowerModeEnum.UNKNOWN

        self.attributes: dict[str, object] = {
            "PowerMode": normalized_power_mode,
            "NumberOfMeasurementTypes": 1,
            "Accuracy": [],
            "ActivePower": None,
            "FeatureMap": self.feature_map,
            "ClusterRevision": self.CLUSTER_REVISION,
        }

        for attr_name in sorted(optional_attr_set):
            self.attributes[attr_name] = [] if attr_name == "Ranges" else None

        measurement_types = self._implemented_measurement_types()
        self.attributes["NumberOfMeasurementTypes"] = len(measurement_types)
        self.attributes["Accuracy"] = [
            self._build_default_accuracy(measurement_type)
            for measurement_type in measurement_types
        ]

        self.readonly_attributes: set[str] = set(self.attributes.keys())
        self.commands: dict[str, object] = {}

    def has_feature(self, feature: int) -> bool:
        return (self.feature_map & int(feature)) != 0

    def _validate_feature_map(self) -> None:
        requires_altc = self.FEATURE_POLY | self.FEATURE_HARM | self.FEATURE_PWRQ
        if (self.feature_map & requires_altc) and not self.has_feature(self.FEATURE_ALTC):
            raise ValueError(
                "POLY, HARM, and PWRQ features require ALTC in FeatureMap"
            )

    def _validate_optional_attributes(self, optional_attributes: set[str]) -> None:
        unknown = optional_attributes - self._VALID_OPTIONAL_ATTRIBUTES
        if unknown:
            raise ValueError(f"Unsupported optional EPM attributes: {sorted(unknown)}")

        if optional_attributes & self._ALTC_ATTRIBUTES and not self.has_feature(
            self.FEATURE_ALTC
        ):
            raise ValueError("ALTC-gated attributes require ALTC feature")

        if optional_attributes & self._HARM_ATTRIBUTES and not self.has_feature(
            self.FEATURE_HARM
        ):
            raise ValueError("HARM-gated attributes require HARM feature")

        if optional_attributes & self._PWRQ_ATTRIBUTES and not self.has_feature(
            self.FEATURE_PWRQ
        ):
            raise ValueError("PWRQ-gated attributes require PWRQ feature")

        if optional_attributes & self._POLY_ATTRIBUTES and not self.has_feature(
            self.FEATURE_POLY
        ):
            raise ValueError("POLY-gated attributes require POLY feature")

    def _implemented_measurement_types(self) -> list[MeasurementTypeEnum]:
        implemented: list[MeasurementTypeEnum] = []
        for attribute_name, measurement_type in self._ATTRIBUTE_TO_MEASUREMENT_TYPE.items():
            if attribute_name in self.attributes and measurement_type not in implemented:
                implemented.append(measurement_type)
        return implemented

    def _build_default_accuracy(
        self, measurement_type: MeasurementTypeEnum
    ) -> MeasurementAccuracyStruct:
        min_value, max_value = self._MEASUREMENT_LIMITS[measurement_type]
        return MeasurementAccuracyStruct(
            MeasurementType=measurement_type,
            Measured=True,
            MinMeasuredValue=min_value,
            MaxMeasuredValue=max_value,
            AccuracyRanges=[
                MeasurementAccuracyRangeStruct(
                    RangeMin=min_value,
                    RangeMax=max_value,
                    PercentTypical=200,
                    PercentMin=100,
                    PercentMax=500,
                )
            ],
        )

    def _normalize_measurement_type(
        self, measurement_type: MeasurementTypeEnum | int
    ) -> MeasurementTypeEnum | None:
        if isinstance(measurement_type, MeasurementTypeEnum):
            return measurement_type
        if isinstance(measurement_type, int):
            try:
                return MeasurementTypeEnum(measurement_type)
            except ValueError:
                return None
        return None

    def update_measurement(
        self, measurement_type: MeasurementTypeEnum | int, value: object
    ) -> Result:
        if not isinstance(value, int):
            return Result.fail(
                ErrorCode.INVALID_ARGUMENT,
                "Measurement value must be an integer",
            )

        normalized_type = self._normalize_measurement_type(measurement_type)
        if normalized_type is None:
            return Result.fail(
                ErrorCode.INVALID_ARGUMENT,
                f"Unsupported measurement type: {measurement_type}",
            )

        attribute_name = self._MEASUREMENT_TYPE_TO_ATTRIBUTE.get(normalized_type)
        if attribute_name is None or attribute_name not in self.attributes:
            return Result.fail(
                ErrorCode.INVALID_STATE,
                f"Measurement type {normalized_type.name} is not implemented",
            )

        min_value, max_value = self._MEASUREMENT_LIMITS[normalized_type]
        if not (min_value <= value <= max_value):
            return Result.fail(
                ErrorCode.INVALID_ARGUMENT,
                f"Value {value} out of range for {normalized_type.name}",
                f"Expected range: {min_value} to {max_value}",
            )

        old_value = self.attributes.get(attribute_name)
        self.attributes[attribute_name] = value

        return Result.ok(
            {
                "measurement_type": normalized_type.name,
                "attribute": attribute_name,
                "old_value": old_value,
                "new_value": value,
            }
        )

    def add_measurement_range(self, range_data: MeasurementRangeStruct) -> Result:
        if "Ranges" not in self.attributes:
            return Result.fail(
                ErrorCode.INVALID_STATE,
                "Ranges attribute is not implemented",
                "Enable optional Ranges attribute to store measurement ranges",
            )

        normalized_type = self._normalize_measurement_type(range_data.MeasurementType)
        if normalized_type is None:
            return Result.fail(
                ErrorCode.INVALID_ARGUMENT,
                f"Unsupported range measurement type: {range_data.MeasurementType}",
            )

        attribute_name = self._MEASUREMENT_TYPE_TO_ATTRIBUTE.get(normalized_type)
        if attribute_name is None or attribute_name not in self.attributes:
            return Result.fail(
                ErrorCode.INVALID_STATE,
                f"Range measurement type {normalized_type.name} is not implemented",
            )

        range_data.MeasurementType = normalized_type

        raw_ranges = self.attributes["Ranges"]
        if not isinstance(raw_ranges, list):
            return Result.fail(
                ErrorCode.INVALID_STATE,
                "Ranges attribute has an invalid internal type",
            )

        ranges: list[MeasurementRangeStruct] = raw_ranges
        existing_index = next(
            (
                index
                for index, existing in enumerate(ranges)
                if existing.MeasurementType == normalized_type
            ),
            None,
        )

        if existing_index is None:
            raw_max_ranges = self.attributes["NumberOfMeasurementTypes"]
            if not isinstance(raw_max_ranges, int):
                return Result.fail(
                    ErrorCode.INVALID_STATE,
                    "NumberOfMeasurementTypes has an invalid internal type",
                )
            max_ranges = raw_max_ranges
            if len(ranges) >= max_ranges:
                return Result.fail(
                    ErrorCode.CONSTRAINT_ERROR,
                    f"Maximum number of ranges ({max_ranges}) reached",
                )
            ranges.append(range_data)
        else:
            ranges[existing_index] = range_data

        return Result.ok(
            {
                "measurement_type": normalized_type.name,
                "range_count": len(ranges),
            }
        )

    def __str__(self) -> str:
        power_mode = self.attributes.get("PowerMode")
        power_mode_name = (
            power_mode.name
            if isinstance(power_mode, PowerModeEnum)
            else PowerModeEnum.UNKNOWN.name
        )
        measurement_types = self.attributes.get("NumberOfMeasurementTypes", 0)
        return (
            "ElectricalPowerMeasurementCluster("
            f"FeatureMap=0x{self.feature_map:02X}, "
            f"PowerMode={power_mode_name}, "
            f"MeasurementTypes={measurement_types})"
        )
