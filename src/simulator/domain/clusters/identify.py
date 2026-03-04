from collections.abc import Callable
from enum import IntEnum
from typing import Any, TypeGuard, cast

from src.simulator.domain.clusters.base import Cluster
from src.simulator.domain.result import ErrorCode, Result


class IdentifyTypeEnum(IntEnum):
    NONE = 0x00
    LIGHT_OUTPUT = 0x01
    VISIBLE_INDICATOR = 0x02
    AUDIBLE_BEEP = 0x03
    DISPLAY = 0x04
    ACTUATOR = 0x05


class EffectIdentifierEnum(IntEnum):
    BLINK = 0x00
    BREATHE = 0x01
    OKAY = 0x02
    CHANNEL_CHANGE = 0x0B
    FINISH_EFFECT = 0xFE
    STOP_EFFECT = 0xFF


class EffectVariantEnum(IntEnum):
    DEFAULT = 0x00


class IdentifyCluster(Cluster):
    CLUSTER_ID: int = 0x0003
    CLUSTER_REVISION: int = 5
    FEATURE_MAP: int = 0

    _SUPPORTED_EFFECT_IDS: frozenset[int] = frozenset(
        int(effect_id) for effect_id in EffectIdentifierEnum
    )
    _EFFECT_DURATION_SECONDS: dict[EffectIdentifierEnum, int] = {
        EffectIdentifierEnum.BLINK: 1,
        EffectIdentifierEnum.BREATHE: 15,
        EffectIdentifierEnum.OKAY: 1,
        EffectIdentifierEnum.CHANNEL_CHANGE: 8,
    }

    def __init__(self, identify_type: object = IdentifyTypeEnum.VISIBLE_INDICATOR):
        super().__init__(cluster_id="Identify")

        parsed_identify_type = self._parse_identify_type(identify_type)

        self.attributes: dict[str, Any] = {
            "IdentifyTime": 0,
            "IdentifyType": int(parsed_identify_type),
            "FeatureMap": self.FEATURE_MAP,
            "ClusterRevision": self.CLUSTER_REVISION,
        }

        self.readonly_attributes: set[str] = {
            "IdentifyType",
            "FeatureMap",
            "ClusterRevision",
        }

        self.commands: dict[str, Callable[..., Result]] = {
            "Identify": self._identify,
            "TriggerEffect": self._trigger_effect,
        }

        self._tick_accumulator_seconds: float = 0.0
        self._active_effect: EffectIdentifierEnum | None = None
        self._effect_remaining_seconds: int = 0
        self._effect_tick_accumulator_seconds: float = 0.0

    @staticmethod
    def _is_uint8(value: object) -> TypeGuard[int]:
        return isinstance(value, int) and not isinstance(value, bool) and 0 <= value <= 255

    @staticmethod
    def _parse_identify_type(value: object) -> IdentifyTypeEnum:
        if isinstance(value, bool) or not isinstance(value, int):
            raise ValueError("IdentifyType must be an integer")
        return IdentifyTypeEnum(int(value))

    @classmethod
    def _parse_effect_variant_or_default(cls, value: object) -> EffectVariantEnum:
        if not cls._is_uint8(value):
            raise ValueError("EffectVariant must be uint8")
        variant_value = cast(int, value)
        if variant_value == int(EffectVariantEnum.DEFAULT):
            return EffectVariantEnum.DEFAULT
        return EffectVariantEnum.DEFAULT

    def _identify(self, IdentifyTime: object) -> Result:
        if isinstance(IdentifyTime, bool) or not isinstance(IdentifyTime, int):
            return Result.fail(
                ErrorCode.VALIDATION_ERROR,
                "Invalid IdentifyTime type",
                "IdentifyTime must be uint16 (0-65535)",
            )
        if IdentifyTime < 0 or IdentifyTime > 65535:
            return Result.fail(
                ErrorCode.VALIDATION_ERROR,
                "Invalid IdentifyTime",
                "IdentifyTime must be uint16 (0-65535)",
            )

        old_value = int(self.attributes.get("IdentifyTime", 0))
        self.attributes["IdentifyTime"] = int(IdentifyTime)
        self._tick_accumulator_seconds = 0.0

        return Result.ok(
            {
                "cluster": self.cluster_id,
                "command": "Identify",
                "old_value": old_value,
                "new_value": int(IdentifyTime),
            }
        )

    def _trigger_effect(self, EffectIdentifier: object, EffectVariant: object) -> Result:
        if not self._is_uint8(EffectIdentifier):
            return Result.fail(
                ErrorCode.VALIDATION_ERROR,
                "Invalid TriggerEffect arguments",
                "EffectIdentifier must be uint8",
            )

        try:
            _ = self._parse_effect_variant_or_default(EffectVariant)
        except ValueError as error:
            return Result.fail(
                ErrorCode.VALIDATION_ERROR,
                "Invalid TriggerEffect arguments",
                str(error),
            )

        effect_identifier_value = cast(int, EffectIdentifier)
        if effect_identifier_value not in self._SUPPORTED_EFFECT_IDS:
            return Result.fail(
                ErrorCode.CONSTRAINT_ERROR,
                "Unsupported EffectIdentifier",
                "EffectIdentifier must be one of 0x00, 0x01, 0x02, 0x0B, 0xFE, 0xFF",
            )

        effect_identifier = EffectIdentifierEnum(effect_identifier_value)

        if effect_identifier == EffectIdentifierEnum.STOP_EFFECT:
            self._active_effect = None
            self._effect_remaining_seconds = 0
            self._effect_tick_accumulator_seconds = 0.0
            return Result.ok(
                {
                    "cluster": self.cluster_id,
                    "command": "TriggerEffect",
                    "effect_identifier": int(effect_identifier),
                    "effect_variant": int(EffectVariantEnum.DEFAULT),
                }
            )

        if effect_identifier == EffectIdentifierEnum.FINISH_EFFECT:
            if self._effect_remaining_seconds <= 0:
                self._active_effect = None
            return Result.ok(
                {
                    "cluster": self.cluster_id,
                    "command": "TriggerEffect",
                    "effect_identifier": int(effect_identifier),
                    "effect_variant": int(EffectVariantEnum.DEFAULT),
                }
            )

        effect_duration = self._EFFECT_DURATION_SECONDS.get(effect_identifier)
        if effect_duration is None:
            return Result.fail(
                ErrorCode.CONSTRAINT_ERROR,
                "Unsupported EffectIdentifier",
                "EffectIdentifier must be one of 0x00, 0x01, 0x02, 0x0B, 0xFE, 0xFF",
            )

        self._active_effect = effect_identifier
        self._effect_remaining_seconds = effect_duration
        self._effect_tick_accumulator_seconds = 0.0

        return Result.ok(
            {
                "cluster": self.cluster_id,
                "command": "TriggerEffect",
                "effect_identifier": int(effect_identifier),
                "effect_variant": int(EffectVariantEnum.DEFAULT),
            }
        )

    def _advance_identify_countdown(self, elapsed_seconds: float) -> None:
        identify_time_raw = self.attributes.get("IdentifyTime", 0)
        if isinstance(identify_time_raw, bool) or not isinstance(identify_time_raw, int):
            return

        identify_time = int(identify_time_raw)
        if identify_time <= 0:
            self._tick_accumulator_seconds = 0.0
            self.attributes["IdentifyTime"] = 0
            return

        self._tick_accumulator_seconds += elapsed_seconds
        elapsed_whole_seconds = int(self._tick_accumulator_seconds)
        if elapsed_whole_seconds <= 0:
            return

        self._tick_accumulator_seconds -= float(elapsed_whole_seconds)
        remaining = max(0, identify_time - elapsed_whole_seconds)
        self.attributes["IdentifyTime"] = int(remaining)

    def _advance_effect_countdown(self, elapsed_seconds: float) -> None:
        if self._active_effect is None:
            self._effect_remaining_seconds = 0
            self._effect_tick_accumulator_seconds = 0.0
            return

        if self._effect_remaining_seconds <= 0:
            self._active_effect = None
            self._effect_remaining_seconds = 0
            self._effect_tick_accumulator_seconds = 0.0
            return

        self._effect_tick_accumulator_seconds += elapsed_seconds
        elapsed_whole_seconds = int(self._effect_tick_accumulator_seconds)
        if elapsed_whole_seconds <= 0:
            return

        self._effect_tick_accumulator_seconds -= float(elapsed_whole_seconds)
        self._effect_remaining_seconds = max(
            0, self._effect_remaining_seconds - elapsed_whole_seconds
        )
        if self._effect_remaining_seconds <= 0:
            self._active_effect = None

    def blocks_exact_batch_advance(self) -> bool:
        identify_time_raw = self.attributes.get("IdentifyTime", 0)
        identify_time = 0
        if isinstance(identify_time_raw, int) and not isinstance(identify_time_raw, bool):
            identify_time = int(identify_time_raw)

        if identify_time > 0:
            return True
        if self._active_effect is not None:
            return True
        if self._effect_remaining_seconds > 0:
            return True
        return False

    def on_time_tick(self, tick_interval: float = 0.1) -> None:
        elapsed = float(tick_interval)
        if elapsed <= 0:
            return

        self._advance_identify_countdown(elapsed)
        self._advance_effect_countdown(elapsed)
