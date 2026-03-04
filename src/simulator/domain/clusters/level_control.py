import math
from typing import Optional
from src.simulator.domain.result import Result, ErrorCode
from src.simulator.domain.clusters.base import Cluster


class LevelControlCluster(Cluster):

    _EXECUTE_IF_OFF_BIT = 0
    _COUPLE_COLOR_TEMP_TO_LEVEL_BIT = 1

    def __init__(self, *, time_aware: bool = False, enable_onoff_coupling: bool = True):
        super().__init__("LevelControl")


        self.attributes = {
            "CurrentLevel": None,
            "RemainingTime": 0,
            "MinLevel": 1,
            "MaxLevel": 254,
            "CurrentFrequency": 0,
            "MinFrequency": 0,
            "MaxFrequency": 0,
            "OnOffTransitionTime": 0,
            "OnLevel": None,
            "OnTransitionTime": None,
            "OffTransitionTime": None,
            "DefaultMoveRate": None,
            "Options": 0,
            "StartUpCurrentLevel": None,
        }

        self.readonly_attributes = {
            "CurrentLevel",
            "RemainingTime",
            "MinLevel",
            "MaxLevel",
            "CurrentFrequency",
            "MinFrequency",
            "MaxFrequency",
        }

        self.commands = {
            "MoveToLevel": self._move_to_level,
            "Move": self._move,
            "Step": self._step,
            "Stop": self._stop,
            "MoveToLevelWithOnOff": self._move_to_level_with_onoff,
            "MoveWithOnOff": self._move_with_onoff,
            "StepWithOnOff": self._step_with_onoff,
            "StopWithOnOff": self._stop_with_onoff,
            "MoveToClosestFrequency": self._move_to_closest_frequency,
        }

        self._transition_state = {
            "active": False,
            "start_level": None,
            "target_level": None,
            "total_time": 0,
            "ticks_required": 0,
            "processed_ticks": 0,
            "delta_per_tick": 0.0,
            "tick_interval": 0.1,
            "with_onoff": False,
        }
        self._move_state = {
            "active": False,
            "direction": None,
            "rate": 0,
            "with_onoff": False,
        }

        self._move_accumulator: float = 0.0

        self._device = None
        self._time_aware = time_aware

        self._enable_onoff_coupling = enable_onoff_coupling

        self._stored_level: Optional[int] = None
        self._default_tick_interval = 0.1

        if self._time_aware:
            self.on_time_tick = self._handle_time_tick  # type: ignore[attr-defined]

    def _effective_current_level(self) -> int:
        level = self.attributes["CurrentLevel"]
        if level is not None:
            return int(level)
        return int(self.attributes["MinLevel"])


    def _get_onoff_cluster(self):
        if self._device is None:
            return None
        for endpoint_id, clusters in getattr(self._device, "endpoints", {}).items():
            if endpoint_id == 0:
                continue
            onoff = clusters.get("OnOff")
            if onoff is not None:
                return onoff
        return None

    def _get_device_onoff_state(self) -> Optional[bool]:
        onoff_cluster = self._get_onoff_cluster()
        if onoff_cluster is None:
            return None
        return onoff_cluster.attributes.get("OnOff")

    def _set_device_onoff_state(self, on: bool) -> None:
        onoff_cluster = self._get_onoff_cluster()
        if onoff_cluster is None:
            return
        onoff_cluster.attributes["OnOff"] = on

    def _apply_onoff_from_level(self, level: int) -> None:
        if not self._enable_onoff_coupling:
            return
        min_level = self.attributes["MinLevel"]
        if level > min_level:
            self._set_device_onoff_state(True)
        else:
            self._set_device_onoff_state(False)


    def _should_execute(self, temp_options: int) -> bool:
        onoff_state = self._get_device_onoff_state()
        if onoff_state is None or onoff_state is True:
            return True
        execute_if_off = (temp_options >> self._EXECUTE_IF_OFF_BIT) & 1
        return bool(execute_if_off)


    def _move_to_level(
        self,
        Level: int,
        TransitionTime: Optional[int] = None,
        OptionsMask: int = 0,
        OptionsOverride: int = 0,
    ) -> Result:
        return self._move_to_level_impl(
            Level=Level,
            TransitionTime=TransitionTime,
            OptionsMask=OptionsMask,
            OptionsOverride=OptionsOverride,
            with_onoff=False,
        )

    def _move(
        self,
        MoveMode: int,
        Rate: Optional[int] = None,
        OptionsMask: int = 0,
        OptionsOverride: int = 0,
    ) -> Result:
        return self._move_impl(
            MoveMode=MoveMode,
            Rate=Rate,
            OptionsMask=OptionsMask,
            OptionsOverride=OptionsOverride,
            with_onoff=False,
        )

    def _step(
        self,
        StepMode: int,
        StepSize: int,
        TransitionTime: Optional[int] = None,
        OptionsMask: int = 0,
        OptionsOverride: int = 0,
    ) -> Result:
        return self._step_impl(
            StepMode=StepMode,
            StepSize=StepSize,
            TransitionTime=TransitionTime,
            OptionsMask=OptionsMask,
            OptionsOverride=OptionsOverride,
            with_onoff=False,
        )

    def _stop(self, OptionsMask: int = 0, OptionsOverride: int = 0) -> Result:
        return self._stop_impl(
            OptionsMask=OptionsMask,
            OptionsOverride=OptionsOverride,
            with_onoff=False,
        )


    def _move_to_level_with_onoff(
        self,
        Level: int,
        TransitionTime: Optional[int] = None,
        OptionsMask: int = 0,
        OptionsOverride: int = 0,
    ) -> Result:
        return self._move_to_level_impl(
            Level=Level,
            TransitionTime=TransitionTime,
            OptionsMask=OptionsMask,
            OptionsOverride=OptionsOverride,
            with_onoff=True,
        )

    def _move_with_onoff(
        self,
        MoveMode: int,
        Rate: Optional[int] = None,
        OptionsMask: int = 0,
        OptionsOverride: int = 0,
    ) -> Result:
        return self._move_impl(
            MoveMode=MoveMode,
            Rate=Rate,
            OptionsMask=OptionsMask,
            OptionsOverride=OptionsOverride,
            with_onoff=True,
        )

    def _step_with_onoff(
        self,
        StepMode: int,
        StepSize: int,
        TransitionTime: Optional[int] = None,
        OptionsMask: int = 0,
        OptionsOverride: int = 0,
    ) -> Result:
        return self._step_impl(
            StepMode=StepMode,
            StepSize=StepSize,
            TransitionTime=TransitionTime,
            OptionsMask=OptionsMask,
            OptionsOverride=OptionsOverride,
            with_onoff=True,
        )

    def _stop_with_onoff(
        self, OptionsMask: int = 0, OptionsOverride: int = 0
    ) -> Result:
        return self._stop_impl(
            OptionsMask=OptionsMask,
            OptionsOverride=OptionsOverride,
            with_onoff=True,
        )


    def _move_to_level_impl(
        self,
        *,
        Level: int,
        TransitionTime: Optional[int],
        OptionsMask: int,
        OptionsOverride: int,
        with_onoff: bool,
    ) -> Result:
        if self._transition_state["active"]:
            return Result.fail(
                ErrorCode.INVALID_STATE,
                "Cannot start new transition while another is active",
            )

        if not (1 <= Level <= 254):
            return Result.fail(
                ErrorCode.COMMAND_INVALID_ARGS,
                "Level must be between 1 and 254",
            )

        temp_options = self._process_options_bitmap(OptionsMask, OptionsOverride)

        if not with_onoff and not self._should_execute(temp_options):
            return Result.ok(
                {
                    "cluster": "LevelControl",
                    "command": "MoveToLevel",
                    "suppressed": True,
                    "reason": "ExecuteIfOff=0 and device is Off",
                }
            )

        level = max(self.attributes["MinLevel"], min(Level, self.attributes["MaxLevel"]))
        command_name = "MoveToLevelWithOnOff" if with_onoff else "MoveToLevel"


        if TransitionTime is None:
            resolved_time = self.attributes["OnOffTransitionTime"] or 0
        else:
            resolved_time = TransitionTime

        if resolved_time == 0 or not self._time_aware:
            self.attributes["CurrentLevel"] = level
            self.attributes["RemainingTime"] = 0
            if with_onoff:
                self._apply_onoff_from_level(level)
            return Result.ok(
                {
                    "cluster": "LevelControl",
                    "command": command_name,
                    "target_level": level,
                    "duration": 0,
                }
            )
        else:
            self._start_transition(level, resolved_time, with_onoff=with_onoff)


            if with_onoff and level > self.attributes["MinLevel"]:
                self._set_device_onoff_state(True)
            return Result.ok(
                {
                    "cluster": "LevelControl",
                    "command": command_name,
                    "target_level": level,
                    "duration": resolved_time,
                }
            )

    def _move_impl(
        self,
        *,
        MoveMode: int,
        Rate: Optional[int],
        OptionsMask: int,
        OptionsOverride: int,
        with_onoff: bool,
    ) -> Result:
        if self._transition_state["active"]:
            return Result.fail(
                ErrorCode.INVALID_STATE,
                "Cannot execute Move command during transition",
            )

        if MoveMode not in [0, 1]:
            return Result.fail(
                ErrorCode.COMMAND_INVALID_ARGS,
                "MoveMode must be 0 (Up) or 1 (Down)",
            )

        if Rate is not None and Rate == 0:
            return Result.fail(
                ErrorCode.COMMAND_INVALID_ARGS, "Rate cannot be 0"
            )

        temp_options = self._process_options_bitmap(OptionsMask, OptionsOverride)

        if not with_onoff and not self._should_execute(temp_options):
            return Result.ok(
                {
                    "cluster": "LevelControl",
                    "command": "Move",
                    "suppressed": True,
                    "reason": "ExecuteIfOff=0 and device is Off",
                }
            )

        command_name = "MoveWithOnOff" if with_onoff else "Move"
        move_rate = Rate or self.attributes["DefaultMoveRate"] or 1
        direction = "up" if MoveMode == 0 else "down"
        self._move_state = {
            "active": True,
            "direction": direction,
            "rate": move_rate,
            "with_onoff": with_onoff,
        }
        self._move_accumulator = 0.0

        if with_onoff and MoveMode == 0:
            self._set_device_onoff_state(True)

        return Result.ok(
            {
                "cluster": "LevelControl",
                "command": command_name,
                "direction": direction,
                "rate": move_rate,
            }
        )

    def _step_impl(
        self,
        *,
        StepMode: int,
        StepSize: int,
        TransitionTime: Optional[int],
        OptionsMask: int,
        OptionsOverride: int,
        with_onoff: bool,
    ) -> Result:
        if self._transition_state["active"]:
            return Result.fail(
                ErrorCode.INVALID_STATE,
                "Cannot start new transition while another is active",
            )

        if StepMode not in [0, 1]:
            return Result.fail(
                ErrorCode.COMMAND_INVALID_ARGS,
                "StepMode must be 0 (Up) or 1 (Down)",
            )

        if StepSize == 0:
            return Result.fail(
                ErrorCode.COMMAND_INVALID_ARGS, "StepSize cannot be 0"
            )

        temp_options = self._process_options_bitmap(OptionsMask, OptionsOverride)

        if not with_onoff and not self._should_execute(temp_options):
            return Result.ok(
                {
                    "cluster": "LevelControl",
                    "command": "Step",
                    "suppressed": True,
                    "reason": "ExecuteIfOff=0 and device is Off",
                }
            )

        command_name = "StepWithOnOff" if with_onoff else "Step"

        current_level = self._effective_current_level()
        if StepMode == 0:
            new_level = min(current_level + StepSize, self.attributes["MaxLevel"])
        else:
            new_level = max(current_level - StepSize, self.attributes["MinLevel"])


        if TransitionTime is None:
            resolved_time = 0
        else:
            resolved_time = TransitionTime


        actual_step = abs(new_level - current_level)
        if actual_step < StepSize and resolved_time > 0 and actual_step > 0:
            resolved_time = max(1, int(resolved_time * actual_step / StepSize))
        elif actual_step == 0:
            resolved_time = 0

        if resolved_time == 0 or not self._time_aware:
            self.attributes["CurrentLevel"] = new_level
            self.attributes["RemainingTime"] = 0
            if with_onoff:
                self._apply_onoff_from_level(new_level)
        else:
            self._start_transition(new_level, resolved_time, with_onoff=with_onoff)

            if with_onoff and new_level > self.attributes["MinLevel"]:
                self._set_device_onoff_state(True)

        return Result.ok(
            {
                "cluster": "LevelControl",
                "command": command_name,
                "direction": "up" if StepMode == 0 else "down",
                "step_size": StepSize,
                "new_level": new_level,
                "duration": resolved_time,
            }
        )

    def _stop_impl(
        self, *, OptionsMask: int, OptionsOverride: int, with_onoff: bool
    ) -> Result:
        temp_options = self._process_options_bitmap(OptionsMask, OptionsOverride)


        if not with_onoff and not self._should_execute(temp_options):
            return Result.ok(
                {
                    "cluster": "LevelControl",
                    "command": "Stop",
                    "suppressed": True,
                    "reason": "ExecuteIfOff=0 and device is Off",
                }
            )

        was_with_onoff = (
            self._transition_state.get("with_onoff", False)
            or self._move_state.get("with_onoff", False)
        )
        self._transition_state["active"] = False
        self._move_state["active"] = False
        self._move_accumulator = 0.0
        self.attributes["RemainingTime"] = 0

        if was_with_onoff:
            self._apply_onoff_from_level(self._effective_current_level())

        return Result.ok(
            {
                "cluster": "LevelControl",
                "command": "StopWithOnOff" if with_onoff else "Stop",
                "stopped": True,
            }
        )


    def on_onoff_change(self, is_on: bool) -> None:

        self._transition_state["active"] = False
        self._move_state["active"] = False
        self._move_accumulator = 0.0
        self.attributes["RemainingTime"] = 0

        if is_on:
            on_level = self.attributes["OnLevel"]
            if on_level is not None:
                target = on_level
            else:

                stored = self._stored_level
                if stored is not None and stored > self.attributes["MinLevel"]:
                    target = stored
                else:
                    current = self.attributes["CurrentLevel"]
                    if current is not None and current > self.attributes["MinLevel"]:
                        target = current
                    else:
                        target = self.attributes["MaxLevel"]

            on_time = self.attributes["OnTransitionTime"]
            transition_time = (
                on_time
                if on_time is not None
                else (self.attributes["OnOffTransitionTime"] or 0)
            )

            if transition_time == 0 or not self._time_aware:
                self.attributes["CurrentLevel"] = target
                self.attributes["RemainingTime"] = 0
            else:
                self._start_transition(target, transition_time, with_onoff=False)
        else:

            current = self.attributes["CurrentLevel"]
            if current is not None and current > self.attributes["MinLevel"]:
                self._stored_level = current

            target = self.attributes["MinLevel"]

            off_time = self.attributes["OffTransitionTime"]
            transition_time = (
                off_time
                if off_time is not None
                else (self.attributes["OnOffTransitionTime"] or 0)
            )

            if transition_time == 0 or not self._time_aware:
                self.attributes["CurrentLevel"] = target
                self.attributes["RemainingTime"] = 0
            else:
                self._start_transition(target, transition_time, with_onoff=False)


    def _move_to_closest_frequency(self, Frequency: int) -> Result:
        min_freq = self.attributes["MinFrequency"]
        max_freq = self.attributes["MaxFrequency"]

        if min_freq > 0 and max_freq > 0:
            if not (min_freq <= Frequency <= max_freq):
                return Result.fail(
                    ErrorCode.CONSTRAINT_ERROR,
                    "Frequency out of supported range",
                )

        self.attributes["CurrentFrequency"] = Frequency

        return Result.ok(
            {
                "cluster": "LevelControl",
                "command": "MoveToClosestFrequency",
                "frequency": Frequency,
            }
        )


    def _process_options_bitmap(self, OptionsMask: int, OptionsOverride: int) -> int:
        temp_options = self.attributes["Options"]
        if temp_options is None:
            temp_options = 0

        for bit in range(8):
            if (OptionsMask >> bit) & 1:
                if (OptionsOverride >> bit) & 1:
                    temp_options |= 1 << bit
                else:
                    temp_options &= ~(1 << bit)

        return temp_options


    def update(self, delta_time: float):
        if delta_time <= 0:
            return
        self._process_transition(delta_time)
        self._process_move(delta_time)

    def set_device_reference(self, device):
        self._device = device

    def _handle_time_tick(self):
        delta = self._get_tick_interval()
        self.update(delta)

    def _get_tick_interval(self) -> float:
        if self._device and hasattr(self._device, "tick_interval"):
            try:
                interval = float(self._device.tick_interval)
                return interval if interval > 0 else self._default_tick_interval
            except (TypeError, ValueError):
                return self._default_tick_interval
        return self._default_tick_interval

    def _start_transition(
        self, target_level: int, transition_time: int, *, with_onoff: bool = False
    ):
        transition_time = max(0, transition_time)
        current_level = self._effective_current_level()
        if transition_time == 0:
            self.attributes["CurrentLevel"] = target_level
            self.attributes["RemainingTime"] = 0
            self._transition_state["active"] = False
            return

        tick_interval = self._get_tick_interval()
        total_seconds = transition_time / 10.0
        ticks_required = max(
            1, math.ceil(total_seconds / max(tick_interval, 1e-6))
        )
        delta_per_tick = (target_level - current_level) / ticks_required

        self._transition_state = {
            "active": True,
            "start_level": current_level,
            "target_level": target_level,
            "total_time": transition_time,
            "ticks_required": ticks_required,
            "processed_ticks": 0,
            "delta_per_tick": delta_per_tick,
            "tick_interval": tick_interval,
            "with_onoff": with_onoff,
        }
        self.attributes["RemainingTime"] = transition_time

    def _process_transition(self, delta_seconds: float):
        if not self._transition_state["active"]:
            return

        state = self._transition_state
        tick_interval = state["tick_interval"] or self._default_tick_interval
        if tick_interval <= 0:
            tick_interval = self._default_tick_interval

        tentative_ticks = max(1, int(round(delta_seconds / tick_interval)))
        remaining_ticks = state["ticks_required"] - state["processed_ticks"]
        ticks_to_process = min(remaining_ticks, tentative_ticks)
        state["processed_ticks"] += ticks_to_process

        new_level = state["start_level"] + state["delta_per_tick"] * state["processed_ticks"]

        if state["delta_per_tick"] >= 0:
            new_level = min(new_level, state["target_level"])
        else:
            new_level = max(new_level, state["target_level"])

        self.attributes["CurrentLevel"] = int(round(new_level))

        remaining_ticks = state["ticks_required"] - state["processed_ticks"]
        remaining_seconds = remaining_ticks * tick_interval
        self.attributes["RemainingTime"] = int(round(max(0.0, remaining_seconds) * 10))

        if remaining_ticks <= 0:
            self.attributes["CurrentLevel"] = state["target_level"]
            self.attributes["RemainingTime"] = 0
            state["active"] = False


            if state.get("with_onoff", False):
                self._apply_onoff_from_level(state["target_level"])

    def _process_move(self, delta_seconds: float):
        if not self._move_state["active"]:
            return

        current_level = self._effective_current_level()
        rate = self._move_state["rate"]


        self._move_accumulator += rate * delta_seconds
        delta_amount = int(self._move_accumulator)
        self._move_accumulator -= delta_amount
        if delta_amount == 0:
            return

        if self._move_state["direction"] == "up":
            new_level = min(current_level + delta_amount, self.attributes["MaxLevel"])
        else:
            new_level = max(current_level - delta_amount, self.attributes["MinLevel"])

        self.attributes["CurrentLevel"] = new_level

        if self._move_state.get("with_onoff", False):
            self._apply_onoff_from_level(new_level)

        if (
            self._move_state["direction"] == "up"
            and new_level >= self.attributes["MaxLevel"]
        ) or (
            self._move_state["direction"] == "down"
            and new_level <= self.attributes["MinLevel"]
        ):
            self._move_state["active"] = False
            self._move_accumulator = 0.0
            self.attributes["RemainingTime"] = 0
