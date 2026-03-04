from __future__ import annotations

import random
from collections.abc import Mapping
from typing import Dict, List, Tuple, cast

from src.pipelines.episode_generation.core import constants as QGP_CONST
from src.pipelines.episode_generation.core.types import (
    DeviceInRoom,
    HomeGenerationSpec,
    NumericRangeDict,
    RoomConfigDict,
    RoomStateBounds,
    SimulationConfigDict,
)


class HomeConfigInitializer:
    ILLUMINANCE_RANGE: Tuple[float, float] = QGP_CONST.ILLUMINANCE_RANGE
    PM10_RANGE: Tuple[float, float] = QGP_CONST.PM10_RANGE

    TEMPERATURE_RANGE_CENTI: Tuple[int, int] = QGP_CONST.TEMPERATURE_RANGE_CENTI
    HUMIDITY_RANGE_CENTI: Tuple[int, int] = QGP_CONST.HUMIDITY_RANGE_CENTI

    MAX_ROOMS: int = QGP_CONST.MAX_ROOMS

    TEMPERATURE_STD_FRAC: float = QGP_CONST.TEMPERATURE_STD_FRAC
    HUMIDITY_STD_FRAC: float = QGP_CONST.HUMIDITY_STD_FRAC
    ILLUMINANCE_STD_FRAC: float = QGP_CONST.ILLUMINANCE_STD_FRAC
    PM10_STD_FRAC: float = QGP_CONST.PM10_STD_FRAC

    ROOM_BASE_CANDIDATES: Dict[str, Tuple[str, ...]] = {
        "living_room": (
            "air_conditioner",
            "air_purifier",
            "dehumidifier",
            "dimmable_light",
            "fan",
            "heat_pump",
            "on_off_light",
            "rvc",
            "tv",
            "window_covering_controller",
        ),
        "bathroom": (
            "air_conditioner",
            "air_purifier",
            "dehumidifier",
            "dimmable_light",
            "fan",
            "heat_pump",
            "humidifier",
            "on_off_light",
            "window_covering_controller",
            "laundry_washer",
            "laundry_dryer",
        ),
        "kitchen": (
            "air_conditioner",
            "air_purifier",
            "dehumidifier",
            "dimmable_light",
            "dishwasher",
            "fan",
            "freezer",
            "heat_pump",
            "humidifier",
            "on_off_light",
            "refrigerator",
            "window_covering_controller",
        ),
        "utility_room": (
            "air_conditioner",
            "air_purifier",
            "dehumidifier",
            "dimmable_light",
            "fan",
            "heat_pump",
            "on_off_light",
            "window_covering_controller",
            "laundry_washer",
            "laundry_dryer",
        ),
        "bedroom": (
            "air_conditioner",
            "air_purifier",
            "dehumidifier",
            "dimmable_light",
            "fan",
            "heat_pump",
            "on_off_light",
            "tv",
            "window_covering_controller",
        ),
        "dining_room": (
            "air_conditioner",
            "air_purifier",
            "dehumidifier",
            "dimmable_light",
            "fan",
            "heat_pump",
            "humidifier",
            "on_off_light",
            "window_covering_controller",
        ),
        "study_room": (
            "air_conditioner",
            "air_purifier",
            "dehumidifier",
            "dimmable_light",
            "fan",
            "heat_pump",
            "on_off_light",
            "tv",
            "window_covering_controller",
        ),
        "kids_room": (
            "air_conditioner",
            "air_purifier",
            "dehumidifier",
            "dimmable_light",
            "fan",
            "heat_pump",
            "on_off_light",
            "rvc",
            "tv",
            "window_covering_controller",
        ),
        "office": (
            "air_conditioner",
            "air_purifier",
            "dehumidifier",
            "dimmable_light",
            "fan",
            "heat_pump",
            "on_off_light",
            "rvc",
            "tv",
            "window_covering_controller",
        ),
    }

    REQUIRED_ROOMS: Tuple[str, ...] = (
        "living_room",
        "bathroom",
        "kitchen",
        "utility_room",
    )

    REQUIRED_DEVICES_BY_ROOM: Dict[str, Tuple[str, ...]] = {
        "living_room": ("on_off_light", "window_covering_controller"),
        "bathroom": ("on_off_light", "air_purifier"),
        "kitchen": ("on_off_light", "dishwasher", "freezer", "refrigerator"),
        "utility_room": ("on_off_light", "laundry_washer", "laundry_dryer"),
        "bedroom": ("on_off_light",),
        "dining_room": ("on_off_light",),
        "study_room": ("on_off_light",),
        "kids_room": ("on_off_light",),
        "office": ("on_off_light",),
    }

    def __init__(
        self,
        *,
        home_spec: Mapping[str, object],
        seed: int | None = None,
        tick_interval: float = 0.1,
        base_time: str = "2025-08-23 00:00:00",
    ) -> None:
        self._rng = random.Random(seed)
        self._tick_interval = float(tick_interval)
        self._base_time = str(base_time)

        normalized = self.validate_home_spec(home_spec)
        self._home_spec = normalized

        self._room_count = int(normalized["room_count"])
        self._min_devices_per_room = int(normalized["devices_per_room"]["min"])
        self._max_devices_per_room = int(normalized["devices_per_room"]["max"])

        temp_min_c = float(normalized["environment"]["temperature_c"]["min"])
        temp_max_c = float(normalized["environment"]["temperature_c"]["max"])
        humidity_min_pct = float(normalized["environment"]["humidity_pct"]["min"])
        humidity_max_pct = float(normalized["environment"]["humidity_pct"]["max"])

        self._temperature_range_centi = (
            self._to_centi(temp_min_c),
            self._to_centi(temp_max_c),
        )
        self._humidity_range_centi = (
            self._to_centi(humidity_min_pct),
            self._to_centi(humidity_max_pct),
        )
        self._illuminance_range = (
            float(normalized["environment"]["illuminance_lux"]["min"]),
            float(normalized["environment"]["illuminance_lux"]["max"]),
        )
        self._pm10_range = (
            float(normalized["environment"]["pm10_ugm3"]["min"]),
            float(normalized["environment"]["pm10_ugm3"]["max"]),
        )

    @classmethod
    def validate_home_spec(cls, home_spec: Mapping[str, object]) -> HomeGenerationSpec:
        return cls._validate_home_spec(home_spec)

    def create_config(self) -> SimulationConfigDict:
        rooms_to_make = self._select_rooms()
        baseline = self._generate_home_baseline()

        room_configs: Dict[str, RoomConfigDict] = {}
        supported = self._get_supported_device_types()
        for room_id in rooms_to_make:
            base = self.ROOM_BASE_CANDIDATES.get(room_id)
            candidates = tuple(t for t in (base or supported) if t in supported)
            if not candidates:
                raise RuntimeError(f"No supported device candidates for room '{room_id}'")

            devices = self._build_room_devices(room_id, candidates)
            state = self._sample_room_state(baseline)
            room_configs[room_id] = {
                "state": state,
                "devices": devices,
            }

        return {
            "tick_interval": float(self._tick_interval),
            "base_time": self._base_time,
            "rooms": room_configs,
            "state_bounds": self._state_bounds(),
        }

    def _state_bounds(self) -> RoomStateBounds:
        return {
            "temperature": self._numeric_range(
                self._temperature_range_centi[0],
                self._temperature_range_centi[1],
            ),
            "humidity": self._numeric_range(
                self._humidity_range_centi[0],
                self._humidity_range_centi[1],
            ),
            "illuminance": self._numeric_range(
                self._illuminance_range[0],
                self._illuminance_range[1],
            ),
            "pm10": self._numeric_range(
                self._pm10_range[0],
                self._pm10_range[1],
            ),
        }

    @staticmethod
    def _numeric_range(minimum: float, maximum: float) -> NumericRangeDict:
        return {
            "min": float(minimum),
            "max": float(maximum),
        }

    def _select_rooms(self) -> List[str]:
        all_rooms = list(self.ROOM_BASE_CANDIDATES.keys())
        required_rooms = [r for r in self.REQUIRED_ROOMS if r in all_rooms]
        if len(required_rooms) > self._room_count:
            raise ValueError(
                f"home.room_count={self._room_count} cannot satisfy required rooms ({len(required_rooms)})"
            )

        additional_candidates = [r for r in all_rooms if r not in required_rooms]
        additional_count = self._room_count - len(required_rooms)
        if additional_count > len(additional_candidates):
            raise ValueError(
                f"home.room_count={self._room_count} exceeds available room templates"
            )

        sampled = (
            self._rng.sample(additional_candidates, k=additional_count)
            if additional_count > 0
            else []
        )
        return required_rooms + sampled

    def _build_room_devices(
        self, room_id: str, candidates: Tuple[str, ...]
    ) -> List[DeviceInRoom]:
        allow_type_dupe_max = QGP_CONST.ALLOW_TYPE_DUPE_MAX

        max_possible = len(candidates) * allow_type_dupe_max
        sampled_count = self._rng.randint(
            self._min_devices_per_room,
            self._max_devices_per_room,
        )
        device_count = min(max(1, sampled_count), max_possible)

        required_types_all = self.REQUIRED_DEVICES_BY_ROOM.get(room_id, ())
        required_types = tuple(t for t in required_types_all if t in candidates)
        if required_types:
            device_count = max(device_count, len(required_types))
            device_count = min(device_count, self._max_devices_per_room)
            device_count = min(device_count, max_possible)

        type_to_index: Dict[str, int] = {}
        devices: List[DeviceInRoom] = []

        for dtype in required_types:
            if type_to_index.get(dtype, 0) >= allow_type_dupe_max:
                continue
            cur_idx = type_to_index.get(dtype, 0)
            type_to_index[dtype] = cur_idx + 1
            device_id = self._make_device_id(room_id, dtype, cur_idx + 1)
            devices.append({"device_id": device_id, "device_type": dtype, "attributes": {}})

        remaining_slots = max(0, device_count - len(devices))
        if remaining_slots > 0:
            sampling_pool: List[str] = []
            for dtype in candidates:
                used = type_to_index.get(dtype, 0)
                room_slots = max(0, allow_type_dupe_max - used)
                if room_slots > 0:
                    sampling_pool.extend([dtype] * room_slots)

            if sampling_pool:
                k = min(remaining_slots, len(sampling_pool))
                picked_types = self._rng.sample(sampling_pool, k=k)
                for dtype in picked_types:
                    cur_idx = type_to_index.get(dtype, 0)
                    type_to_index[dtype] = cur_idx + 1
                    device_id = self._make_device_id(room_id, dtype, cur_idx + 1)
                    devices.append(
                        {"device_id": device_id, "device_type": dtype, "attributes": {}}
                    )

        return devices

    def _sample_room_state(self, baseline: Dict[str, float]) -> Dict[str, float]:
        t_min, t_max = self._temperature_range_centi
        h_min, h_max = self._humidity_range_centi
        i_min, i_max = self._illuminance_range
        p_min, p_max = self._pm10_range

        t_std = (t_max - t_min) * self.TEMPERATURE_STD_FRAC
        h_std = (h_max - h_min) * self.HUMIDITY_STD_FRAC
        i_std = (i_max - i_min) * self.ILLUMINANCE_STD_FRAC
        p_std = (p_max - p_min) * self.PM10_STD_FRAC

        temperature = self._truncated_normal(baseline["temperature"], t_std, t_min, t_max)
        humidity = self._truncated_normal(baseline["humidity"], h_std, h_min, h_max)
        illuminance = self._truncated_normal(baseline["illuminance"], i_std, i_min, i_max)
        pm10 = self._truncated_normal(baseline["pm10"], p_std, p_min, p_max)

        return {
            "temperature": int(round(temperature)),
            "humidity": int(round(humidity)),
            "illuminance": self._round2(illuminance),
            "pm10": self._round2(pm10),
        }

    def _generate_home_baseline(self) -> Dict[str, float]:
        return {
            "temperature": int(self._rng.randint(*self._temperature_range_centi)),
            "humidity": int(self._rng.randint(*self._humidity_range_centi)),
            "illuminance": self._rng.uniform(*self._illuminance_range),
            "pm10": self._rng.uniform(*self._pm10_range),
        }

    def _truncated_normal(
        self, mean: float, std: float, min_val: float, max_val: float
    ) -> float:
        if std <= 0:
            return max(min(mean, max_val), min_val)

        value = self._rng.normalvariate(mean, std)
        if value < min_val:
            return min_val
        if value > max_val:
            return max_val
        return value

    @staticmethod
    def _round2(value: float) -> float:
        return round(float(value), 2)

    @staticmethod
    def _to_centi(value: float) -> int:
        return int(round(float(value) * 100.0))

    @staticmethod
    def _make_device_id(room_id: str, device_type: str, index: int) -> str:
        return f"{room_id}_{device_type}_{index}"

    @staticmethod
    def _get_supported_device_types() -> Tuple[str, ...]:
        try:
            from src.simulator.application.device_factory import get_supported_device_types

            types = tuple(get_supported_device_types())
            if not types:
                raise RuntimeError("No supported device types available")
            return tuple(sorted(types))
        except Exception as exc:
            raise RuntimeError("Failed to load supported device types") from exc

    @classmethod
    def _validate_home_spec(cls, home_spec: Mapping[str, object]) -> HomeGenerationSpec:
        cls._require_exact_keys(
            home_spec,
            key_name="home",
            expected=("room_count", "devices_per_room", "environment"),
        )

        room_count = cls._require_int(home_spec.get("room_count"), "home.room_count")
        min_room_count = len(cls.REQUIRED_ROOMS)
        max_room_count = min(cls.MAX_ROOMS, len(cls.ROOM_BASE_CANDIDATES))
        if room_count < min_room_count or room_count > max_room_count:
            raise ValueError(
                f"home.room_count must be between {min_room_count} and {max_room_count}"
            )

        devices_per_room = cls._require_mapping(
            home_spec.get("devices_per_room"),
            "home.devices_per_room",
        )
        cls._require_exact_keys(
            devices_per_room,
            key_name="home.devices_per_room",
            expected=("min", "max"),
        )
        min_devices = cls._require_int(
            devices_per_room.get("min"),
            "home.devices_per_room.min",
        )
        max_devices = cls._require_int(
            devices_per_room.get("max"),
            "home.devices_per_room.max",
        )
        if min_devices < 1:
            raise ValueError("home.devices_per_room.min must be >= 1")
        if min_devices > max_devices:
            raise ValueError("home.devices_per_room.min cannot exceed max")
        if max_devices > QGP_CONST.MAX_DEVICES_PER_ROOM:
            raise ValueError(
                f"home.devices_per_room.max must be <= {QGP_CONST.MAX_DEVICES_PER_ROOM}"
            )

        max_required_devices = cls._max_required_devices_per_room()
        if max_devices < max_required_devices:
            raise ValueError(
                f"home.devices_per_room.max must be >= {max_required_devices} to satisfy required devices"
            )

        environment = cls._require_mapping(home_spec.get("environment"), "home.environment")
        cls._require_exact_keys(
            environment,
            key_name="home.environment",
            expected=(
                "temperature_c",
                "humidity_pct",
                "illuminance_lux",
                "pm10_ugm3",
            ),
        )

        temp_min, temp_max = cls._validate_numeric_range(
            environment.get("temperature_c"),
            key_name="home.environment.temperature_c",
            lower=cls.TEMPERATURE_RANGE_CENTI[0] / 100.0,
            upper=cls.TEMPERATURE_RANGE_CENTI[1] / 100.0,
        )
        humidity_min, humidity_max = cls._validate_numeric_range(
            environment.get("humidity_pct"),
            key_name="home.environment.humidity_pct",
            lower=cls.HUMIDITY_RANGE_CENTI[0] / 100.0,
            upper=cls.HUMIDITY_RANGE_CENTI[1] / 100.0,
        )
        illuminance_min, illuminance_max = cls._validate_numeric_range(
            environment.get("illuminance_lux"),
            key_name="home.environment.illuminance_lux",
            lower=cls.ILLUMINANCE_RANGE[0],
            upper=cls.ILLUMINANCE_RANGE[1],
        )
        pm10_min, pm10_max = cls._validate_numeric_range(
            environment.get("pm10_ugm3"),
            key_name="home.environment.pm10_ugm3",
            lower=cls.PM10_RANGE[0],
            upper=cls.PM10_RANGE[1],
        )

        return {
            "room_count": room_count,
            "devices_per_room": {
                "min": min_devices,
                "max": max_devices,
            },
            "environment": {
                "temperature_c": {
                    "min": temp_min,
                    "max": temp_max,
                },
                "humidity_pct": {
                    "min": humidity_min,
                    "max": humidity_max,
                },
                "illuminance_lux": {
                    "min": illuminance_min,
                    "max": illuminance_max,
                },
                "pm10_ugm3": {
                    "min": pm10_min,
                    "max": pm10_max,
                },
            },
        }

    @classmethod
    def _max_required_devices_per_room(cls) -> int:
        counts: List[int] = []
        for room_id in cls.REQUIRED_ROOMS:
            required_types = cls.REQUIRED_DEVICES_BY_ROOM.get(room_id, ())
            candidate_types = cls.ROOM_BASE_CANDIDATES.get(room_id, ())
            valid_required = [t for t in required_types if t in candidate_types]
            counts.append(len(valid_required))
        return max(counts) if counts else 1

    @staticmethod
    def _require_mapping(raw: object, key_name: str) -> Mapping[str, object]:
        if not isinstance(raw, Mapping):
            raise ValueError(f"{key_name} must be a mapping")
        for key in raw.keys():
            if not isinstance(key, str):
                raise ValueError(f"{key_name} keys must be strings")
        return cast(Mapping[str, object], raw)

    @staticmethod
    def _require_int(raw: object, key_name: str) -> int:
        if isinstance(raw, bool) or not isinstance(raw, int):
            raise ValueError(f"{key_name} must be an integer")
        return raw

    @staticmethod
    def _require_number(raw: object, key_name: str) -> float:
        if isinstance(raw, bool) or not isinstance(raw, (int, float)):
            raise ValueError(f"{key_name} must be a number")
        return float(raw)

    @classmethod
    def _validate_numeric_range(
        cls,
        raw: object,
        *,
        key_name: str,
        lower: float,
        upper: float,
    ) -> Tuple[float, float]:
        mapping = cls._require_mapping(raw, key_name)
        cls._require_exact_keys(mapping, key_name=key_name, expected=("min", "max"))

        minimum = cls._require_number(mapping.get("min"), f"{key_name}.min")
        maximum = cls._require_number(mapping.get("max"), f"{key_name}.max")
        if minimum > maximum:
            raise ValueError(f"{key_name}.min cannot exceed max")
        if minimum < lower or maximum > upper:
            raise ValueError(f"{key_name} must be within [{lower}, {upper}]")

        return minimum, maximum

    @staticmethod
    def _require_exact_keys(
        mapping: Mapping[str, object],
        *,
        key_name: str,
        expected: Tuple[str, ...],
    ) -> None:
        expected_set = set(expected)
        actual_set = set(mapping.keys())
        missing = sorted(expected_set - actual_set)
        unknown = sorted(actual_set - expected_set)

        if missing or unknown:
            parts: List[str] = []
            if missing:
                parts.append(f"missing keys: {', '.join(missing)}")
            if unknown:
                parts.append(f"unknown keys: {', '.join(unknown)}")
            detail = "; ".join(parts)
            raise ValueError(f"{key_name} has invalid shape ({detail})")
