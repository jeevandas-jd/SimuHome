from __future__ import annotations

from dataclasses import dataclass
from enum import IntEnum
from typing import Optional
import time

from src.simulator.domain.clusters.base import Cluster
from src.simulator.domain.result import ErrorCode, Result


INT64_MAX_62 = 1 << 62


class MeasurementTypeEnum(IntEnum):
    ELECTRICAL_ENERGY = 0x00


class ElectricalEnergyMeasurementFeature(IntEnum):
    IMPORTED_ENERGY = 0x01
    EXPORTED_ENERGY = 0x02
    CUMULATIVE_ENERGY = 0x04
    PERIODIC_ENERGY = 0x08


@dataclass
class EnergyMeasurementStruct:
    Energy: int
    StartTimestamp: Optional[int] = None
    EndTimestamp: Optional[int] = None
    StartSystime: Optional[int] = None
    EndSystime: Optional[int] = None


@dataclass
class CumulativeEnergyResetStruct:
    ImportedResetTimestamp: Optional[int] = None
    ExportedResetTimestamp: Optional[int] = None
    ImportedResetSystime: Optional[int] = None
    ExportedResetSystime: Optional[int] = None


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


class ElectricalEnergyMeasurementCluster(Cluster):
    CLUSTER_REVISION = 1

    FEATURE_IMPE = int(ElectricalEnergyMeasurementFeature.IMPORTED_ENERGY)
    FEATURE_EXPE = int(ElectricalEnergyMeasurementFeature.EXPORTED_ENERGY)
    FEATURE_CUME = int(ElectricalEnergyMeasurementFeature.CUMULATIVE_ENERGY)
    FEATURE_PERE = int(ElectricalEnergyMeasurementFeature.PERIODIC_ENERGY)

    def __init__(
        self,
        *,
        feature_map: int = 0,
        include_cumulative_energy_reset: bool = False,
    ):
        super().__init__(cluster_id="ElectricalEnergyMeasurement")

        self.feature_map: int = int(feature_map)
        self._validate_feature_map()

        self.attributes: dict[str, object] = {
            "Accuracy": self._build_default_accuracy(),
            "FeatureMap": self.feature_map,
            "ClusterRevision": self.CLUSTER_REVISION,
        }

        if self._supports(self.FEATURE_IMPE | self.FEATURE_CUME):
            self.attributes["CumulativeEnergyImported"] = None

        if self._supports(self.FEATURE_EXPE | self.FEATURE_CUME):
            self.attributes["CumulativeEnergyExported"] = None

        if self._supports(self.FEATURE_IMPE | self.FEATURE_PERE):
            self.attributes["PeriodicEnergyImported"] = None

        if self._supports(self.FEATURE_EXPE | self.FEATURE_PERE):
            self.attributes["PeriodicEnergyExported"] = None

        if include_cumulative_energy_reset and self.has_feature(self.FEATURE_CUME):
            self.attributes["CumulativeEnergyReset"] = None

        self.readonly_attributes: set[str] = set(self.attributes.keys())
        self.commands: dict[str, object] = {}

    def has_feature(self, feature: int) -> bool:
        return (self.feature_map & int(feature)) != 0

    def _supports(self, required_features: int) -> bool:
        return (self.feature_map & int(required_features)) == int(required_features)

    def _validate_feature_map(self) -> None:
        has_direction = bool(self.feature_map & (self.FEATURE_IMPE | self.FEATURE_EXPE))
        has_measurement_kind = bool(
            self.feature_map & (self.FEATURE_CUME | self.FEATURE_PERE)
        )
        if has_direction != has_measurement_kind:
            raise ValueError(
                "Imported/Exported and Cumulative/Periodic features must be configured together"
            )

    def _build_default_accuracy(self) -> MeasurementAccuracyStruct:
        return MeasurementAccuracyStruct(
            MeasurementType=MeasurementTypeEnum.ELECTRICAL_ENERGY,
            Measured=True,
            MinMeasuredValue=0,
            MaxMeasuredValue=INT64_MAX_62,
            AccuracyRanges=[
                MeasurementAccuracyRangeStruct(
                    RangeMin=0,
                    RangeMax=INT64_MAX_62,
                    PercentTypical=200,
                    PercentMin=100,
                    PercentMax=500,
                )
            ],
        )

    def _current_epoch_seconds(self) -> int:
        return int(time.time())

    def _current_systime_ms(self) -> int:
        return int(time.monotonic() * 1000)

    def _validate_energy_value(self, energy_mwh: object) -> Result | None:
        if not isinstance(energy_mwh, int):
            return Result.fail(
                ErrorCode.INVALID_ARGUMENT,
                "Energy value must be an integer",
            )
        if energy_mwh < 0:
            return Result.fail(
                ErrorCode.INVALID_ARGUMENT,
                "Energy value cannot be negative",
            )
        if energy_mwh > INT64_MAX_62:
            return Result.fail(
                ErrorCode.INVALID_ARGUMENT,
                f"Energy value exceeds maximum {INT64_MAX_62}",
            )
        return None

    def update_cumulative_energy_imported(self, energy_mwh: int) -> Result:
        if "CumulativeEnergyImported" not in self.attributes:
            return Result.fail(
                ErrorCode.INVALID_STATE,
                "CumulativeEnergyImported is not implemented",
            )

        validation_error = self._validate_energy_value(energy_mwh)
        if validation_error:
            return validation_error

        old_value = self.attributes["CumulativeEnergyImported"]
        self.attributes["CumulativeEnergyImported"] = EnergyMeasurementStruct(
            Energy=energy_mwh,
            EndTimestamp=self._current_epoch_seconds(),
            EndSystime=self._current_systime_ms(),
        )

        return Result.ok(
            {
                "measurement_type": "CumulativeEnergyImported",
                "old_energy": old_value.Energy if isinstance(old_value, EnergyMeasurementStruct) else None,
                "new_energy": energy_mwh,
            }
        )

    def update_cumulative_energy_exported(self, energy_mwh: int) -> Result:
        if "CumulativeEnergyExported" not in self.attributes:
            return Result.fail(
                ErrorCode.INVALID_STATE,
                "CumulativeEnergyExported is not implemented",
            )

        validation_error = self._validate_energy_value(energy_mwh)
        if validation_error:
            return validation_error

        old_value = self.attributes["CumulativeEnergyExported"]
        self.attributes["CumulativeEnergyExported"] = EnergyMeasurementStruct(
            Energy=energy_mwh,
            EndTimestamp=self._current_epoch_seconds(),
            EndSystime=self._current_systime_ms(),
        )

        return Result.ok(
            {
                "measurement_type": "CumulativeEnergyExported",
                "old_energy": old_value.Energy if isinstance(old_value, EnergyMeasurementStruct) else None,
                "new_energy": energy_mwh,
            }
        )

    def update_periodic_energy_imported(
        self, energy_mwh: int, start_timestamp: int, end_timestamp: int
    ) -> Result:
        if "PeriodicEnergyImported" not in self.attributes:
            return Result.fail(
                ErrorCode.INVALID_STATE,
                "PeriodicEnergyImported is not implemented",
            )

        validation_error = self._validate_energy_value(energy_mwh)
        if validation_error:
            return validation_error

        if not isinstance(start_timestamp, int) or not isinstance(end_timestamp, int):
            return Result.fail(
                ErrorCode.INVALID_ARGUMENT,
                "Periodic timestamps must be integers",
            )
        if end_timestamp <= start_timestamp:
            return Result.fail(
                ErrorCode.INVALID_ARGUMENT,
                "End timestamp must be greater than start timestamp",
            )

        old_value = self.attributes["PeriodicEnergyImported"]
        end_systime = self._current_systime_ms()
        start_systime = max(0, end_systime - ((end_timestamp - start_timestamp) * 1000))

        self.attributes["PeriodicEnergyImported"] = EnergyMeasurementStruct(
            Energy=energy_mwh,
            StartTimestamp=start_timestamp,
            EndTimestamp=end_timestamp,
            StartSystime=start_systime,
            EndSystime=end_systime,
        )

        return Result.ok(
            {
                "measurement_type": "PeriodicEnergyImported",
                "old_energy": old_value.Energy if isinstance(old_value, EnergyMeasurementStruct) else None,
                "new_energy": energy_mwh,
            }
        )

    def update_periodic_energy_exported(
        self, energy_mwh: int, start_timestamp: int, end_timestamp: int
    ) -> Result:
        if "PeriodicEnergyExported" not in self.attributes:
            return Result.fail(
                ErrorCode.INVALID_STATE,
                "PeriodicEnergyExported is not implemented",
            )

        validation_error = self._validate_energy_value(energy_mwh)
        if validation_error:
            return validation_error

        if not isinstance(start_timestamp, int) or not isinstance(end_timestamp, int):
            return Result.fail(
                ErrorCode.INVALID_ARGUMENT,
                "Periodic timestamps must be integers",
            )
        if end_timestamp <= start_timestamp:
            return Result.fail(
                ErrorCode.INVALID_ARGUMENT,
                "End timestamp must be greater than start timestamp",
            )

        old_value = self.attributes["PeriodicEnergyExported"]
        end_systime = self._current_systime_ms()
        start_systime = max(0, end_systime - ((end_timestamp - start_timestamp) * 1000))

        self.attributes["PeriodicEnergyExported"] = EnergyMeasurementStruct(
            Energy=energy_mwh,
            StartTimestamp=start_timestamp,
            EndTimestamp=end_timestamp,
            StartSystime=start_systime,
            EndSystime=end_systime,
        )

        return Result.ok(
            {
                "measurement_type": "PeriodicEnergyExported",
                "old_energy": old_value.Energy if isinstance(old_value, EnergyMeasurementStruct) else None,
                "new_energy": energy_mwh,
            }
        )

    def reset_cumulative_energy(self) -> Result:
        if not self.has_feature(self.FEATURE_CUME):
            return Result.fail(
                ErrorCode.INVALID_STATE,
                "Cumulative energy feature is not enabled",
            )

        end_timestamp = self._current_epoch_seconds()
        end_systime = self._current_systime_ms()

        if "CumulativeEnergyImported" in self.attributes:
            self.attributes["CumulativeEnergyImported"] = EnergyMeasurementStruct(
                Energy=0,
                EndTimestamp=end_timestamp,
                EndSystime=end_systime,
            )

        if "CumulativeEnergyExported" in self.attributes:
            self.attributes["CumulativeEnergyExported"] = EnergyMeasurementStruct(
                Energy=0,
                EndTimestamp=end_timestamp,
                EndSystime=end_systime,
            )

        if "CumulativeEnergyReset" in self.attributes:
            reset_value = CumulativeEnergyResetStruct()
            if self.has_feature(self.FEATURE_IMPE):
                reset_value.ImportedResetTimestamp = end_timestamp
                reset_value.ImportedResetSystime = end_systime
            if self.has_feature(self.FEATURE_EXPE):
                reset_value.ExportedResetTimestamp = end_timestamp
                reset_value.ExportedResetSystime = end_systime
            self.attributes["CumulativeEnergyReset"] = reset_value

        return Result.ok({"reset": True})

    def __str__(self) -> str:
        return (
            "ElectricalEnergyMeasurementCluster("
            f"FeatureMap=0x{self.feature_map:02X}, "
            f"Attributes={len(self.attributes)})"
        )
