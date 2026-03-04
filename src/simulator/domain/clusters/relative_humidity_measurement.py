from src.simulator.domain.clusters.base import Cluster
from src.simulator.domain.result import Result
from typing import Optional
import random


class RelativeHumidityMeasurementCluster(Cluster):
    

    def __init__(
        self,
        MinMeasuredValue: Optional[int] = None,
        MaxMeasuredValue: Optional[int] = None,
        Tolerance: Optional[int] = None,
    ):
        super().__init__(cluster_id="RelativeHumidityMeasurement")

        if MinMeasuredValue is not None:
            if MinMeasuredValue < 0 or MinMeasuredValue > 9999:
                raise ValueError(
                    f"MinMeasuredValue {MinMeasuredValue} out of range [0, 9999]"
                )

        if MaxMeasuredValue is not None:
            if MaxMeasuredValue < 1 or MaxMeasuredValue > 10000:
                raise ValueError(
                    f"MaxMeasuredValue {MaxMeasuredValue} out of range [1, 10000]"
                )

        if MinMeasuredValue is not None and MaxMeasuredValue is not None:
            if MaxMeasuredValue <= MinMeasuredValue:
                raise ValueError(
                    f"MaxMeasuredValue {MaxMeasuredValue} must be greater than MinMeasuredValue {MinMeasuredValue}"
                )

        if Tolerance is not None:
            if Tolerance < 0 or Tolerance > 2048:
                raise ValueError(f"Tolerance {Tolerance} out of range [0, 2048]")


        self.attributes = {
            "MeasuredValue": None,
            "MinMeasuredValue": MinMeasuredValue,
            "MaxMeasuredValue": MaxMeasuredValue,
            "Tolerance": Tolerance,
        }

        self._rng = random.Random(0)

        self.readonly_attributes = {
            "MeasuredValue",
            "MinMeasuredValue",
            "MaxMeasuredValue",
            "Tolerance",
        }


        if MinMeasuredValue is not None and MaxMeasuredValue is not None:

            default_value = (MinMeasuredValue + MaxMeasuredValue) // 2
            self._update_measured_value(default_value)

    def _validate_measurement_constraints(self) -> bool:
        
        min_val = self.attributes["MinMeasuredValue"]
        max_val = self.attributes["MaxMeasuredValue"]
        measured_val = self.attributes["MeasuredValue"]


        if min_val is not None and max_val is not None:
            if max_val <= min_val:
                return False


        if max_val is not None and measured_val is not None:
            if measured_val > max_val:
                return False


        if min_val is not None and measured_val is not None:
            if measured_val < min_val:
                return False

        return True

    def _update_measured_value(self, value: Optional[int]) -> Result:
        

        old_value = self.attributes["MeasuredValue"]


        if value is None:
            self.attributes["MeasuredValue"] = None
            return Result.ok(
                {
                    "cluster": self.cluster_id,
                    "attribute": "MeasuredValue",
                    "value": None,
                    "humidity_percent": None,
                }
            )


        if not isinstance(value, int) or value < 0 or value > 65535:
            return Result.fail(
                error_code="INVALID_VALUE",
                error_message=f"MeasuredValue {value} not valid uint16",
                error_detail="MeasuredValue must be uint16 (0-65535)",
            )


        if value > 10000:
            return Result.fail(
                error_code="INVALID_VALUE",
                error_message=f"Humidity value {value} exceeds 100% (10000)",
                error_detail="Humidity cannot exceed 100% relative humidity",
            )


        self.attributes["MeasuredValue"] = value


        if not self._validate_measurement_constraints():

            self.attributes["MeasuredValue"] = old_value
            min_val = self.attributes["MinMeasuredValue"]
            max_val = self.attributes["MaxMeasuredValue"]
            return Result.fail(
                error_code="CONSTRAINT_ERROR",
                error_message=f"MeasuredValue {value} violates constraints",
                error_detail=f"Valid range: {min_val} to {max_val}",
            )


        return Result.ok(
            {
                "cluster": self.cluster_id,
                "attribute": "MeasuredValue",
                "value": value,
                "humidity_percent": value / 100.0 if value is not None else None,
            }
        )

    def get_humidity_percent(self) -> Optional[float]:
        
        measured = self.attributes["MeasuredValue"]
        return measured / 100.0 if measured is not None else None

    def get_measurement_range_percent(self) -> tuple[Optional[float], Optional[float]]:
        
        min_val = self.attributes["MinMeasuredValue"]
        max_val = self.attributes["MaxMeasuredValue"]

        min_percent = min_val / 100.0 if min_val is not None else None
        max_percent = max_val / 100.0 if max_val is not None else None

        return (min_percent, max_percent)

    def get_tolerance_percent(self) -> Optional[float]:
        
        Tolerance = self.attributes["Tolerance"]
        return Tolerance / 100.0 if Tolerance is not None else None

    def is_measurement_in_tolerance_range(self, test_value: int) -> bool:
        
        measured = self.attributes["MeasuredValue"]
        Tolerance = self.attributes["Tolerance"]

        if measured is None or Tolerance is None:
            return False

        return (measured - Tolerance) <= test_value <= (measured + Tolerance)

    def set_humidity_percent(self, percent: float) -> Result:
        
        if percent < 0.0 or percent > 100.0:
            return Result.fail(
                error_code="INVALID_VALUE",
                error_message=f"Humidity percent {percent} out of range",
                error_detail="Valid range: 0.0 to 100.0",
            )


        value = int(round(percent * 100))
        return self._update_measured_value(value)

    def _simulate_humidity_change(
        self, target_humidity: Optional[int] = None
    ) -> Result:
        
        current = self.attributes["MeasuredValue"]
        min_val = self.attributes["MinMeasuredValue"] or 0
        max_val = self.attributes["MaxMeasuredValue"] or 10000

        if current is None:

            current = (min_val + max_val) // 2

        if target_humidity is None:

            change = self._rng.randint(-100, 100)
            new_value = max(min_val, min(max_val, current + change))
        else:

            diff = target_humidity - current
            change = max(-50, min(50, diff // 10))
            new_value = max(min_val, min(max_val, current + change))

        return self._update_measured_value(new_value)

    def on_time_tick(self):
        

        self._simulate_humidity_change()
