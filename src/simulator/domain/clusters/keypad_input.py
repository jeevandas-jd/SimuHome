from __future__ import annotations

import time
from enum import IntEnum
from typing import Any, Protocol

from src.simulator.domain.clusters.base import Cluster
from src.simulator.domain.clusters.channel import ChannelCluster
from src.simulator.domain.clusters.level_control import LevelControlCluster
from src.simulator.domain.clusters.media_playback import (
    MediaPlaybackCluster,
    PlaybackStateEnum,
)
from src.simulator.domain.result import ErrorCode, Result, ResultBuilder


class _DeviceLike(Protocol):
    endpoints: dict[int, dict[str, Cluster]]

    def get_attribute(
        self, endpoint_id: int, cluster_id: str, attribute_id: str
    ) -> Any: ...

    def execute_command(
        self, endpoint_id: int, cluster_id: str, command_id: str, **args: Any
    ) -> Result: ...


class StatusEnum(IntEnum):
    SUCCESS = 0
    UNSUPPORTED_KEY = 1
    INVALID_KEY_IN_CURRENT_STATE = 2


class CecKeyCodeEnum(IntEnum):
    SELECT = 0x00
    UP = 0x01
    DOWN = 0x02
    LEFT = 0x03
    RIGHT = 0x04
    RIGHT_UP = 0x05
    RIGHT_DOWN = 0x06
    LEFT_UP = 0x07
    LEFT_DOWN = 0x08
    ROOT_MENU = 0x09
    SETUP_MENU = 0x0A
    CONTENTS_MENU = 0x0B
    FAVORITE_MENU = 0x0C
    EXIT = 0x0D
    MEDIA_TOP_MENU = 0x10
    MEDIA_CONTEXT_SENSITIVE_MENU = 0x11
    NUMBER_ENTRY_MODE = 0x1D
    NUMBER_11 = 0x1E
    NUMBER_12 = 0x1F
    NUMBER_0_OR_NUMBER_10 = 0x20
    NUMBERS_1 = 0x21
    NUMBERS_2 = 0x22
    NUMBERS_3 = 0x23
    NUMBERS_4 = 0x24
    NUMBERS_5 = 0x25
    NUMBERS_6 = 0x26
    NUMBERS_7 = 0x27
    NUMBERS_8 = 0x28
    NUMBERS_9 = 0x29
    DOT = 0x2A
    ENTER = 0x2B
    CLEAR = 0x2C
    NEXT_FAVORITE = 0x2F
    CHANNEL_UP = 0x30
    CHANNEL_DOWN = 0x31
    PREVIOUS_CHANNEL = 0x32
    SOUND_SELECT = 0x33
    INPUT_SELECT = 0x34
    DISPLAY_INFORMATION = 0x35
    HELP = 0x36
    PAGE_UP = 0x37
    PAGE_DOWN = 0x38
    POWER = 0x40
    VOLUME_UP = 0x41
    VOLUME_DOWN = 0x42
    MUTE = 0x43
    PLAY = 0x44
    STOP = 0x45
    PAUSE = 0x46
    RECORD = 0x47
    REWIND = 0x48
    FAST_FORWARD = 0x49
    EJECT = 0x4A
    FORWARD = 0x4B
    BACKWARD = 0x4C
    STOP_RECORD = 0x4D
    PAUSE_RECORD = 0x4E
    RESERVED = 0x4F
    ANGLE = 0x50
    SUB_PICTURE = 0x51
    VIDEO_ON_DEMAND = 0x52
    ELECTRONIC_PROGRAM_GUIDE = 0x53
    TIMER_PROGRAMMING = 0x54
    INITIAL_CONFIGURATION = 0x55
    SELECT_BROADCAST_TYPE = 0x56
    SELECT_SOUND_PRESENTATION = 0x57
    PLAY_FUNCTION = 0x60
    PAUSE_PLAY_FUNCTION = 0x61
    RECORD_FUNCTION = 0x62
    PAUSE_RECORD_FUNCTION = 0x63
    STOP_FUNCTION = 0x64
    MUTE_FUNCTION = 0x65
    RESTORE_VOLUME_FUNCTION = 0x66
    TUNE_FUNCTION = 0x67
    SELECT_MEDIA_FUNCTION = 0x68
    SELECT_AV_INPUT_FUNCTION = 0x69
    SELECT_AUDIO_INPUT_FUNCTION = 0x6A
    POWER_TOGGLE_FUNCTION = 0x6B
    POWER_OFF_FUNCTION = 0x6C
    POWER_ON_FUNCTION = 0x6D
    F1_BLUE = 0x71
    F2_RED = 0x72
    F3_GREEN = 0x73
    F4_YELLOW = 0x74
    F5 = 0x75
    DATA = 0x76


NAVIGATION_KEYS = {
    CecKeyCodeEnum.SELECT,
    CecKeyCodeEnum.UP,
    CecKeyCodeEnum.DOWN,
    CecKeyCodeEnum.LEFT,
    CecKeyCodeEnum.RIGHT,
    CecKeyCodeEnum.BACKWARD,
    CecKeyCodeEnum.EXIT,
    CecKeyCodeEnum.ROOT_MENU,
}

LOCATION_KEYS = {
    CecKeyCodeEnum.ROOT_MENU,
    CecKeyCodeEnum.SETUP_MENU,
}

NUMBER_KEYS = {
    CecKeyCodeEnum.NUMBER_0_OR_NUMBER_10,
    CecKeyCodeEnum.NUMBERS_1,
    CecKeyCodeEnum.NUMBERS_2,
    CecKeyCodeEnum.NUMBERS_3,
    CecKeyCodeEnum.NUMBERS_4,
    CecKeyCodeEnum.NUMBERS_5,
    CecKeyCodeEnum.NUMBERS_6,
    CecKeyCodeEnum.NUMBERS_7,
    CecKeyCodeEnum.NUMBERS_8,
    CecKeyCodeEnum.NUMBERS_9,
}

DEFAULT_EXTRA_SUPPORTED_KEYS = {
    CecKeyCodeEnum.ENTER,
    CecKeyCodeEnum.CLEAR,
    CecKeyCodeEnum.POWER,
    CecKeyCodeEnum.VOLUME_UP,
    CecKeyCodeEnum.VOLUME_DOWN,
    CecKeyCodeEnum.MUTE,
    CecKeyCodeEnum.PLAY,
    CecKeyCodeEnum.PAUSE,
    CecKeyCodeEnum.STOP,
    CecKeyCodeEnum.REWIND,
    CecKeyCodeEnum.FAST_FORWARD,
    CecKeyCodeEnum.CHANNEL_UP,
    CecKeyCodeEnum.CHANNEL_DOWN,
    CecKeyCodeEnum.PREVIOUS_CHANNEL,
}


class KeypadInputCluster(Cluster):
    FEATURE_NAVIGATION_KEY_CODES: int = 0x01
    FEATURE_LOCATION_KEYS: int = 0x02
    FEATURE_NUMBER_KEYS: int = 0x04

    def __init__(self, device: _DeviceLike | None = None, feature_map: int | None = None):
        super().__init__(cluster_id="KeypadInput")

        self.device = device
        self.feature_map = (
            feature_map
            if feature_map is not None
            else (
                self.FEATURE_NAVIGATION_KEY_CODES
                | self.FEATURE_LOCATION_KEYS
                | self.FEATURE_NUMBER_KEYS
            )
        )

        self.attributes = {
            "FeatureMap": self.feature_map,
            "ClusterRevision": 1,
        }
        self.readonly_attributes = {"FeatureMap", "ClusterRevision"}
        self.commands = {"SendKey": self._send_key}

        self.supported_keys = self._build_supported_keys_from_feature_map(self.feature_map)
        self._last_key_code: CecKeyCodeEnum | None = None
        self._last_key_ts: float | None = None

    def _build_supported_keys_from_feature_map(
        self, feature_map: int
    ) -> set[CecKeyCodeEnum]:
        supported: set[CecKeyCodeEnum] = set(DEFAULT_EXTRA_SUPPORTED_KEYS)

        if feature_map & self.FEATURE_NAVIGATION_KEY_CODES:
            supported.update(NAVIGATION_KEYS)
        if feature_map & self.FEATURE_LOCATION_KEYS:
            supported.update(LOCATION_KEYS)
        if feature_map & self.FEATURE_NUMBER_KEYS:
            supported.update(NUMBER_KEYS)

        return supported

    def _sync_feature_map_from_supported_keys(self) -> None:
        feature_map = 0
        if NAVIGATION_KEYS.issubset(self.supported_keys):
            feature_map |= self.FEATURE_NAVIGATION_KEY_CODES
        if LOCATION_KEYS.issubset(self.supported_keys):
            feature_map |= self.FEATURE_LOCATION_KEYS
        if NUMBER_KEYS.issubset(self.supported_keys):
            feature_map |= self.FEATURE_NUMBER_KEYS

        self.feature_map = feature_map
        self.attributes["FeatureMap"] = feature_map

    def _update_repeat_state(self, key_code: CecKeyCodeEnum) -> None:
        now = time.monotonic()
        self._last_key_code = key_code
        self._last_key_ts = now

    def _send_key(self, KeyCode: int | CecKeyCodeEnum) -> Result:
        if not isinstance(KeyCode, (int, CecKeyCodeEnum)):
            return Result.fail(
                ErrorCode.COMMAND_INVALID_ARGS,
                "Invalid KeyCode argument",
                f"KeyCode must be int, got {type(KeyCode).__name__}",
            )

        try:
            key_code = CecKeyCodeEnum(int(KeyCode))
        except ValueError:
            return Result.fail(
                ErrorCode.COMMAND_INVALID_ARGS,
                f"Invalid key code: {KeyCode}",
                "KeyCode must be a valid CecKeyCodeEnum value",
            )

        self._update_repeat_state(key_code)

        if key_code not in self.supported_keys:
            return Result.ok({"Status": StatusEnum.UNSUPPORTED_KEY})

        if not self._is_key_valid_in_current_state(key_code):
            return Result.ok({"Status": StatusEnum.INVALID_KEY_IN_CURRENT_STATE})

        try:
            processed = self._process_key_press(key_code)
        except Exception as error:
            return ResultBuilder.internal_error(error)

        if not processed:
            return Result.ok({"Status": StatusEnum.INVALID_KEY_IN_CURRENT_STATE})

        return Result.ok({"Status": StatusEnum.SUCCESS})

    def _is_device_on(self) -> bool:
        if self.device is None:
            return True

        power = self.device.get_attribute(1, "OnOff", "OnOff")
        if isinstance(power, bool):
            return power
        return True

    def _get_playback_state(self) -> PlaybackStateEnum | None:
        if self.device is None:
            return None

        current_state = self.device.get_attribute(1, "MediaPlayback", "CurrentState")
        if isinstance(current_state, PlaybackStateEnum):
            return current_state
        if isinstance(current_state, int):
            try:
                return PlaybackStateEnum(current_state)
            except ValueError:
                return None
        return None

    def _is_key_valid_in_current_state(self, key: CecKeyCodeEnum) -> bool:
        power_keys = {
            CecKeyCodeEnum.POWER,
            CecKeyCodeEnum.POWER_TOGGLE_FUNCTION,
            CecKeyCodeEnum.POWER_ON_FUNCTION,
            CecKeyCodeEnum.POWER_OFF_FUNCTION,
        }

        if not self._is_device_on():
            return key in power_keys

        if key in power_keys:
            return True

        playback_state = self._get_playback_state()
        if playback_state is None:
            return True

        if key == CecKeyCodeEnum.PLAY:
            return playback_state != PlaybackStateEnum.PLAYING

        if key == CecKeyCodeEnum.PAUSE:
            return playback_state == PlaybackStateEnum.PLAYING

        if key in {
            CecKeyCodeEnum.STOP,
            CecKeyCodeEnum.REWIND,
            CecKeyCodeEnum.FAST_FORWARD,
        }:
            return playback_state in {
                PlaybackStateEnum.PLAYING,
                PlaybackStateEnum.PAUSED,
            }

        return True

    def _process_key_press(self, key: CecKeyCodeEnum) -> bool:
        if key in {
            CecKeyCodeEnum.POWER,
            CecKeyCodeEnum.POWER_TOGGLE_FUNCTION,
            CecKeyCodeEnum.POWER_ON_FUNCTION,
            CecKeyCodeEnum.POWER_OFF_FUNCTION,
        }:
            return self._handle_power_control(key)

        if key in {
            CecKeyCodeEnum.CHANNEL_UP,
            CecKeyCodeEnum.CHANNEL_DOWN,
            CecKeyCodeEnum.PREVIOUS_CHANNEL,
        }:
            channel_cluster = self._get_channel_cluster()
            if channel_cluster is None:
                return False
            if key == CecKeyCodeEnum.CHANNEL_UP:
                return self._handle_channel_up(channel_cluster)
            if key == CecKeyCodeEnum.CHANNEL_DOWN:
                return self._handle_channel_down(channel_cluster)
            return self._handle_previous_channel(channel_cluster)

        if key in {
            CecKeyCodeEnum.VOLUME_UP,
            CecKeyCodeEnum.VOLUME_DOWN,
            CecKeyCodeEnum.MUTE,
        }:
            return self._handle_volume_control(key)

        if key in {
            CecKeyCodeEnum.PLAY,
            CecKeyCodeEnum.PAUSE,
            CecKeyCodeEnum.STOP,
            CecKeyCodeEnum.REWIND,
            CecKeyCodeEnum.FAST_FORWARD,
        }:
            return self._handle_media_playback_control(key)

        return True

    def _handle_power_control(self, key: CecKeyCodeEnum) -> bool:
        if self.device is None:
            return False

        if key == CecKeyCodeEnum.POWER_ON_FUNCTION:
            command = "On"
        elif key == CecKeyCodeEnum.POWER_OFF_FUNCTION:
            command = "Off"
        else:
            command = "Toggle"

        result = self.device.execute_command(1, "OnOff", command)
        return result.success

    def _get_channel_cluster(self) -> ChannelCluster | None:
        if self.device is None:
            return None
        endpoint = self.device.endpoints.get(1, {})
        cluster = endpoint.get("Channel")
        if isinstance(cluster, ChannelCluster):
            return cluster
        return None

    def _get_media_playback_cluster(self) -> MediaPlaybackCluster | None:
        if self.device is None:
            return None
        endpoint = self.device.endpoints.get(1, {})
        cluster = endpoint.get("MediaPlayback")
        if isinstance(cluster, MediaPlaybackCluster):
            return cluster
        return None

    def _get_level_control_cluster(self) -> LevelControlCluster | None:
        if self.device is None:
            return None
        endpoint = self.device.endpoints.get(1, {})
        cluster = endpoint.get("LevelControl")
        if isinstance(cluster, LevelControlCluster):
            return cluster
        return None

    def _handle_media_playback_control(self, key: CecKeyCodeEnum) -> bool:
        media_playback_cluster = self._get_media_playback_cluster()
        if media_playback_cluster is None:
            return False

        handler_name = {
            CecKeyCodeEnum.PLAY: "_play",
            CecKeyCodeEnum.PAUSE: "_pause",
            CecKeyCodeEnum.STOP: "_stop",
            CecKeyCodeEnum.REWIND: "_rewind",
            CecKeyCodeEnum.FAST_FORWARD: "_fast_forward",
        }.get(key)

        if handler_name is None:
            return False

        handler = getattr(media_playback_cluster, handler_name, None)
        if not callable(handler):
            return False

        try:
            result = handler()
        except Exception:
            return False

        if isinstance(result, Result):
            return result.success
        return bool(result)

    def _handle_channel_up(self, channel_cluster: ChannelCluster) -> bool:
        try:
            result = channel_cluster._skip_channel(1)
        except Exception:
            return False
        return result.success

    def _handle_channel_down(self, channel_cluster: ChannelCluster) -> bool:
        try:
            result = channel_cluster._skip_channel(-1)
        except Exception:
            return False
        return result.success

    def _handle_previous_channel(self, channel_cluster: ChannelCluster) -> bool:
        previous_channel = getattr(channel_cluster, "_previous_channel", None)
        current_channel = channel_cluster.attributes.get("CurrentChannel")
        if previous_channel is None or current_channel is None:
            return False

        channel_cluster.attributes["CurrentChannel"] = previous_channel
        channel_cluster._previous_channel = current_channel
        return True

    def _handle_volume_control(self, key: CecKeyCodeEnum) -> bool:
        level_control_cluster = self._get_level_control_cluster()
        if level_control_cluster is None:
            return False

        try:
            if key == CecKeyCodeEnum.VOLUME_UP:
                result = level_control_cluster._step(
                    StepMode=0,
                    StepSize=10,
                    TransitionTime=0,
                )
                return result.success

            if key == CecKeyCodeEnum.VOLUME_DOWN:
                result = level_control_cluster._step(
                    StepMode=1,
                    StepSize=10,
                    TransitionTime=0,
                )
                return result.success

            if key == CecKeyCodeEnum.MUTE:
                min_level = level_control_cluster.attributes.get("MinLevel")
                if not isinstance(min_level, int):
                    return False
                result = level_control_cluster._move_to_level(
                    Level=min_level,
                    TransitionTime=0,
                )
                return result.success
        except Exception:
            return False

        return False

    def set_supported_keys(self, keys: set[CecKeyCodeEnum]) -> None:
        self.supported_keys = set(keys)
        self._sync_feature_map_from_supported_keys()

    def get_supported_keys(self) -> set[CecKeyCodeEnum]:
        return self.supported_keys.copy()

    def __str__(self) -> str:
        return f"KeypadInputCluster(supported_keys={len(self.supported_keys)})"
