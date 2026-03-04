from dataclasses import dataclass
from enum import IntEnum
from typing import List, Optional
from src.simulator.domain.clusters.base import Cluster
from src.simulator.domain.result import Result, ErrorCode


class PlaybackStateEnum(IntEnum):
    

    PLAYING = 0
    PAUSED = 1
    NOT_PLAYING = 2
    BUFFERING = 3


class CharacteristicEnum(IntEnum):
    

    FORCED_SUBTITLES = 0
    DESCRIBES_VIDEO = 1
    EASY_TO_READ = 2
    FRAME_BASED = 3
    MAIN_PROGRAM = 4
    ORIGINAL_CONTENT = 5
    VOICE_OVER_TRANSLATION = 6
    CAPTION = 7
    SUBTITLE = 8
    ALTERNATE = 9
    SUPPLEMENTARY = 10
    COMMENTARY = 11
    DUBBED_TRANSLATION = 12
    DESCRIPTION = 13
    METADATA = 14
    ENHANCED_AUDIO_INTELLIGIBILITY = 15
    EMERGENCY = 16
    KARAOKE = 17


@dataclass
class PlaybackPositionStruct:
    

    UpdatedAt: int
    Position: Optional[
        int
    ]


@dataclass
class TrackAttributesStruct:
    

    LanguageCode: str
    Characteristics: Optional[List[CharacteristicEnum]] = None
    DisplayName: Optional[str] = None


@dataclass
class TrackStruct:
    

    ID: str
    TrackAttributes: TrackAttributesStruct


class MediaPlaybackCluster(Cluster):
    

    def __init__(self):
        super().__init__(cluster_id="MediaPlayback")


        self.attributes = {
            "CurrentState": PlaybackStateEnum.NOT_PLAYING,
        }


        self.readonly_attributes = {"CurrentState"}


        self.commands = {
            "Play": self._play,
            "Pause": self._pause,
            "Stop": self._stop,
            "StartOver": self._start_over,
            "Previous": self._previous,
            "Next": self._next,
            "Rewind": self._rewind,
            "FastForward": self._fast_forward,
        }

    def _play(self) -> Result:
        
        try:
            current_state = self.attributes["CurrentState"]

            if current_state == PlaybackStateEnum.PLAYING:
                return Result.fail(
                    ErrorCode.COMMAND_INVALID_ARGS,
                    "Already playing",
                    "Media is already in playing state",
                )

            self.attributes["CurrentState"] = PlaybackStateEnum.PLAYING
            return Result.ok("Playback started")

        except Exception as e:
            return Result.fail(
                ErrorCode.INTERNAL_ERROR, "Failed to start playback", str(e)
            )

    def _pause(self) -> Result:
        
        try:
            current_state = self.attributes["CurrentState"]

            if current_state != PlaybackStateEnum.PLAYING:
                return Result.fail(
                    ErrorCode.COMMAND_INVALID_ARGS,
                    "Not currently playing",
                    "Cannot pause when media is not in playing state",
                )

            self.attributes["CurrentState"] = PlaybackStateEnum.PAUSED
            return Result.ok("Playback paused")

        except Exception as e:
            return Result.fail(
                ErrorCode.INTERNAL_ERROR, "Failed to pause playback", str(e)
            )

    def _stop(self) -> Result:
        
        try:
            current_state = self.attributes["CurrentState"]

            if current_state == PlaybackStateEnum.NOT_PLAYING:
                return Result.fail(
                    ErrorCode.COMMAND_INVALID_ARGS,
                    "Already stopped",
                    "Media is already in stopped state",
                )

            self.attributes["CurrentState"] = PlaybackStateEnum.NOT_PLAYING
            return Result.ok("Playback stopped")

        except Exception as e:
            return Result.fail(
                ErrorCode.INTERNAL_ERROR, "Failed to stop playback", str(e)
            )

    def _start_over(self) -> Result:
        
        try:

            self.attributes["CurrentState"] = PlaybackStateEnum.PLAYING
            return Result.ok("Playback restarted from beginning")

        except Exception as e:
            return Result.fail(
                ErrorCode.INTERNAL_ERROR, "Failed to restart playback", str(e)
            )

    def _previous(self) -> Result:
        
        try:

            return Result.ok("Moved to previous content")

        except Exception as e:
            return Result.fail(
                ErrorCode.INTERNAL_ERROR, "Failed to move to previous", str(e)
            )

    def _next(self) -> Result:
        
        try:

            return Result.ok("Moved to next content")

        except Exception as e:
            return Result.fail(
                ErrorCode.INTERNAL_ERROR, "Failed to move to next", str(e)
            )

    def _rewind(self, playback_speed: float = 1.0) -> Result:
        
        try:
            current_state = self.attributes["CurrentState"]

            if current_state == PlaybackStateEnum.NOT_PLAYING:
                return Result.fail(
                    ErrorCode.COMMAND_INVALID_ARGS,
                    "Cannot rewind when not playing",
                    "Media must be in playing state to rewind",
                )

            self.attributes["CurrentState"] = PlaybackStateEnum.PLAYING
            return Result.ok(f"Rewinding at {playback_speed}x speed")

        except Exception as e:
            return Result.fail(ErrorCode.INTERNAL_ERROR, "Failed to rewind", str(e))

    def _fast_forward(self, playback_speed: float = 1.0) -> Result:
        
        try:
            current_state = self.attributes["CurrentState"]

            if current_state == PlaybackStateEnum.NOT_PLAYING:
                return Result.fail(
                    ErrorCode.COMMAND_INVALID_ARGS,
                    "Cannot fast forward when not playing",
                    "Media must be in playing state to fast forward",
                )

            self.attributes["CurrentState"] = PlaybackStateEnum.PLAYING
            return Result.ok(f"Fast forwarding at {playback_speed}x speed")

        except Exception as e:
            return Result.fail(
                ErrorCode.INTERNAL_ERROR, "Failed to fast forward", str(e)
            )

    def __str__(self):
        
        current_state = self.attributes.get("CurrentState")
        state_name = current_state.name if current_state else "Unknown"

        return f"MediaPlaybackCluster(CurrentState={state_name})"
