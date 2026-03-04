import time
import math
import queue
import threading
import logging
import uuid
from datetime import datetime, timedelta
from typing import List, Dict, Any, Optional
from src.simulator.domain.result import Result, ResultBuilder, ErrorCode
from src.simulator.domain.aggregators.registry import AGGREGATOR_REGISTRY
from src.simulator.domain.aggregators.base import Aggregator
from src.simulator.domain.devices.base import Device
import json


logger = logging.getLogger(__name__)


class Home:
    

    def __init__(
        self,
        tick_interval=0.1,
        enable_aggregators: bool = True,
        *,
        max_ticks: Optional[int] = None,
        fast_forward: bool = False,
        base_time: str = "2025-08-23 00:00:00",
    ):  
        
        self.tick_interval = tick_interval
        self.enable_aggregators = enable_aggregators
        self.current_tick = 0
        self.max_ticks: Optional[int] = max_ticks
        self.fast_forward: bool = bool(fast_forward)
        self.is_running = False
        self.simulation_thread = None

        
        self.virtual_epoch_seconds = datetime.strptime(
            base_time, "%Y-%m-%d %H:%M:%S"
        ).timestamp()
        self.virtual_offset_seconds: float = 0.0

        
        self.schedular_queue: queue.PriorityQueue[tuple[int, int, str, Any]] = (
            queue.PriorityQueue(maxsize=1000)
        )
        self.task_seq_counter: int = 0

        
        self.workflows_by_id: Dict[str, dict[str, Any]] = {}

        
        self.api_queue = queue.Queue(maxsize=100)
        self.response_lock = threading.Lock()  
        self.response_events: Dict[
            int, threading.Event
        ] = {}  
        self.response_results: Dict[
            int, Result
        ] = {}  
        self.request_states: Dict[int, str] = {}
        self.request_id_counter = 0

        self.max_apis_per_tick = 10

        
        self._skip_increment_once: bool = False
        self._skip_sleep_once: bool = False
        self._fatal_error: Optional[Exception] = None

        
        self.devices_by_room: dict[
            str, dict[str, Device]
        ] = {}  
        self.time_aware_devices_by_room: dict[str, dict[str, Device]] = {}
        self.devices_by_id: dict[
            str, tuple[str, Device]
        ] = {}  
        self.aggregators_by_room: dict[
            str, dict[str, Aggregator]
        ] = {}  

    def queue_api(
        self, api_type: str, *, wait_timeout: float = 60.0, **kwargs
    ) -> Result:
        

        if self._fatal_error is not None:
            return ResultBuilder.internal_error(self._fatal_error)

        thread_alive = bool(
            self.simulation_thread and self.simulation_thread.is_alive()
        )
        if not self.is_running and not thread_alive:
            return Result.fail(
                ErrorCode.CONNECTION_ERROR,
                "Simulation unavailable",
                "Simulation loop is not running",
            )

        event = threading.Event()

        with self.response_lock:
            self.request_id_counter += 1
            request_id = self.request_id_counter
            self.response_events[request_id] = event
            self.request_states[request_id] = "queued"

        api = {"request_id": request_id, "api_type": api_type, "args": kwargs}

        try:
            self.api_queue.put_nowait(api)
        except queue.Full:
            with self.response_lock:
                self.response_events.pop(request_id, None)
                self.response_results.pop(request_id, None)
                self.request_states.pop(request_id, None)
            return ResultBuilder.internal_error(Exception("API queue full"))

        timeout_s = max(0.0, float(wait_timeout))
        poll_interval_s = 0.05
        deadline = time.monotonic() + timeout_s

        while True:
            if event.wait(timeout=poll_interval_s):
                break

            with self.response_lock:
                state = self.request_states.get(request_id)

            if state == "processing":
                event.wait()
                break

            if state == "completed":
                break

            if time.monotonic() >= deadline:
                with self.response_lock:
                    state = self.request_states.get(request_id)
                    if state == "queued":
                        self.request_states[request_id] = "cancelled"
                        self.response_events.pop(request_id, None)
                        self.response_results.pop(request_id, None)
                        return ResultBuilder.internal_error(
                            Exception("API response timeout")
                        )

        with self.response_lock:
            result = self.response_results.pop(request_id, None)
            self.response_events.pop(request_id, None)
            self.request_states.pop(request_id, None)

        if result is None:
            return ResultBuilder.internal_error(Exception("API response missing"))

        return result

    def start_simulation(self):
        if not self.is_running:
            self._fatal_error = None
            self.is_running = True
            self.simulation_thread = threading.Thread(
                target=self.__simulation_loop, daemon=True
            )
            self.simulation_thread.start()

    def __simulation_loop(self):
        
        try:
            while self.is_running:
                tick_start = time.perf_counter()

                self.__process_time_aware_devices()
                self.__process_aggregators()
                self.__process_schedular_queue()
                self.__process_api_queue()

                elapsed = time.perf_counter() - tick_start
                
                if (
                    not self.fast_forward
                    and elapsed < self.tick_interval
                    and not self._skip_sleep_once
                ):
                    time.sleep(self.tick_interval - elapsed)
                if self._skip_sleep_once:
                    self._skip_sleep_once = False
                if self._skip_increment_once:
                    
                    self._skip_increment_once = False
                else:
                    self.current_tick += 1

                if self.max_ticks is not None and self.current_tick >= self.max_ticks:
                    self.is_running = False
                    break
        except Exception as error:
            self._fatal_error = RuntimeError(
                f"Simulation loop terminated at tick {self.current_tick}: {error}"
            )
            self.is_running = False
            logger.exception("Simulation loop terminated unexpectedly")
        finally:
            self.__cleanup_simulation_resources()

    def stop_simulation(self):
        
        if self.is_running:
            self.is_running = False

            if self.simulation_thread and self.simulation_thread.is_alive():
                self.simulation_thread.join(timeout=1.0)
                if self.simulation_thread.is_alive():
                    logger.warning("Simulation thread did not stop within timeout")

            self.__cleanup_simulation_resources()

    def __cleanup_simulation_resources(self):
        
        terminal_error = self._fatal_error or Exception("Simulation stopped")
        with self.response_lock:
            events_copy = dict(self.response_events)
            for request_id, event in events_copy.items():
                if request_id not in self.response_results:
                    self.response_results[request_id] = ResultBuilder.internal_error(
                        terminal_error
                    )
                self.request_states[request_id] = "completed"
                event.set()
            while not self.api_queue.empty():
                try:
                    self.api_queue.get_nowait()
                except queue.Empty:
                    break
            self.request_states.clear()

        
        for wf in self.workflows_by_id.values():
            if wf.get("status") in ("pending", "running"):
                wf["status"] = "cancelled"

        while True:
            try:
                self.schedular_queue.get_nowait()
            except queue.Empty:
                break

    def __process_time_aware_devices(self, room_ids: Optional[List[str]] = None):
        
        rooms_to_process = (
            room_ids if room_ids is not None else self.time_aware_devices_by_room.keys()
        )
        for room_id in rooms_to_process:
            devices = self.time_aware_devices_by_room.get(room_id)
            if not devices:
                continue
            for device in devices.values():
                device.on_time_tick()

    def __process_aggregators(self, room_ids: Optional[List[str]] = None):
        
        rooms_to_process = (
            room_ids if room_ids is not None else self.aggregators_by_room.keys()
        )
        for room_id in rooms_to_process:
            if room_id in self.aggregators_by_room:
                room_aggs = self.aggregators_by_room[room_id]
                for agg_type, agg in room_aggs.items():
                    try:
                        agg.on_time_tick()
                    except Exception as error:
                        raise RuntimeError(
                            f"Aggregator '{agg_type}' failed in room '{room_id}'"
                        ) from error

    def __process_schedular_queue(self, *, start_workflow_inline: bool = False):
        while not self.schedular_queue.empty():
            try:
                due_tick, seq, task_type, task_data = self.schedular_queue.get_nowait()
            except queue.Empty:
                break

            if due_tick <= self.current_tick and task_type == "workflow":
                if start_workflow_inline:
                    self.__start_workflow(task_data)
                else:
                    try:
                        self.api_queue.put_nowait(
                            {
                                "api_type": "start_workflow",
                                "args": {"workflow_id": task_data},
                            }
                        )
                    except queue.Full:
                        self.schedular_queue.put_nowait(
                            (due_tick, seq, task_type, task_data)
                        )
                        break
            else:
                self.schedular_queue.put_nowait((due_tick, seq, task_type, task_data))
                break

    def __start_workflow(self, workflow_id: str) -> Result:
        
        wf = self.workflows_by_id.get(workflow_id)
        if not wf:
            return Result.fail(
                ErrorCode.VALIDATION_ERROR,
                "Not found",
                f"workflow_id '{workflow_id}' not found",
            )
        if wf.get("status") != "pending":
            return Result.ok(
                {
                    "workflow_id": workflow_id,
                    "status": wf.get("status"),
                    "started": False,
                }
            )

        wf["status"] = "running"
        wf["current_step"] = 0

        self.__execute_workflow_step(wf, 0)
        return Result.ok(
            {
                "workflow_id": workflow_id,
                "status": wf.get("status"),
                "started": True,
            }
        )

    def __execute_workflow_step(self, wf: dict[str, Any], step_idx: int):
        
        if step_idx >= len(wf["steps"]):
            wf["status"] = "completed"
            return

        step = wf["steps"][step_idx]
        tool = step.get("tool")
        args = step.get("args", {})

        if tool == "execute_command":
            exec_result = self._execute_command(**args)
        elif tool == "write_attribute":
            exec_result = self._write_attribute(**args)
        else:
            exec_result = Result.fail(
                ErrorCode.VALIDATION_ERROR,
                "Unsupported tool",
                f"tool '{tool}' is not allowed",
            )

        if not exec_result.success:
            wf["status"] = "failed"
            wf["error"] = exec_result.error_message
            return

        next_idx = step_idx + 1
        if next_idx >= len(wf["steps"]):
            wf["status"] = "completed"
            wf["current_step"] = step_idx
            return
        else:
            wf["current_step"] = step_idx

            self.__execute_workflow_step(wf, next_idx)

    def __process_api_queue(self):
        
        for _ in range(self.max_apis_per_tick):
            try:
                api = self.api_queue.get_nowait()
            except queue.Empty:
                break

            request_id = api.get("request_id")
            response = ResultBuilder.internal_error(
                Exception("API handler returned invalid result")
            )

            if request_id is not None:
                with self.response_lock:
                    state = self.request_states.get(request_id)
                    if state == "cancelled":
                        self.request_states.pop(request_id, None)
                        self.response_events.pop(request_id, None)
                        self.response_results.pop(request_id, None)
                        continue
                    if state == "queued":
                        self.request_states[request_id] = "processing"

            try:
                raw_response = self.__process_api(api)

                if isinstance(raw_response, Result):
                    response = raw_response
                else:
                    response = ResultBuilder.internal_error(
                        Exception("API handler returned invalid result")
                    )
            except Exception as e:
                logger.exception(
                    "API processing failed for api_type='%s'", api.get("api_type")
                )
                response = ResultBuilder.internal_error(e)

            if request_id is not None:
                with self.response_lock:
                    if self.request_states.get(request_id) == "cancelled":
                        self.request_states.pop(request_id, None)
                        self.response_events.pop(request_id, None)
                        self.response_results.pop(request_id, None)
                        continue

                    if request_id in self.response_events:
                        self.response_results[request_id] = response
                        self.request_states[request_id] = "completed"
                        event = self.response_events.get(request_id)
                        if event:
                            event.set()

            
            if api.get("api_type") == "run_workflow_now":
                self._skip_sleep_once = True
                return

    def __process_api(self, api):
        
        api_type = api["api_type"]
        args = api["args"]

        if api_type == "schedule_workflow":
            return self.schedule_workflow(**args)
        elif api_type == "get_workflow_status":
            return self.get_workflow_status(**args)
        elif api_type == "get_workflow_list":
            return self.get_workflow_list(**args)
        elif api_type == "get_current_time":
            return Result.ok({"now": self.get_virtual_now_str()})
        elif api_type == "start_workflow":
            return self.__start_workflow(**args)
        elif api_type == "cancel_workflow":
            return self.cancel_workflow(**args)

        if api_type == "add_device":
            response = self._add_device(**args)
        elif api_type == "remove_device":
            response = self._remove_device(**args)
        elif api_type == "set_tick_interval":
            response = self._set_tick_interval(**args)
        elif api_type == "fast_forward_to":
            response = self._fast_forward_to(**args)
        
        elif api_type == "execute_command":
            response = self._execute_command(**args)
        elif api_type == "write_attribute":
            response = self._write_attribute(**args)
        elif api_type == "get_all_attributes":
            response = self._get_all_attributes(**args)
        elif api_type == "get_attribute":
            response = self._get_attribute(**args)
        elif api_type == "get_structure":
            response = self._get_structure(**args)
        elif api_type == "get_room_devices":
            response = self._get_room_devices(**args)
        elif api_type == "get_room_states":
            response = self._get_room_states(**args)
        elif api_type == "get_home_state":
            response = self._get_home_state()
        elif api_type == "get_rooms":
            response = self._get_rooms()
        elif api_type == "run_workflow_now":
            response = self._run_workflow_now(**args)
        elif api_type == "get_environment_control_rules":
            response = self._get_environment_control_rules(**args)
        else:
            response = Result.fail(
                ErrorCode.VALIDATION_ERROR,
                "Unknown API type",
                f"api_type '{api_type}' is not supported",
            )
        return response

    def __resolve_rooms(
        self, room_ids: Optional[List[str]], source: Dict[str, Any]
    ) -> List[str]:
        selected = room_ids if room_ids is not None else list(source.keys())
        resolved: List[str] = []
        seen = set()
        for room_id in selected:
            if room_id in source and room_id not in seen:
                resolved.append(room_id)
                seen.add(room_id)
        return resolved

    def __has_batch_blocking_tick_work_in_rooms(
        self, room_ids: Optional[List[str]]
    ) -> bool:
        rooms = self.__resolve_rooms(room_ids, self.time_aware_devices_by_room)
        for room_id in rooms:
            devices = self.time_aware_devices_by_room.get(room_id)
            if not devices:
                continue
            for device in devices.values():
                if device.has_batch_blocking_tick_work():
                    return True
        return False

    def __can_exact_batch_advance(self, room_ids: Optional[List[str]]) -> bool:
        rooms = self.__resolve_rooms(room_ids, self.aggregators_by_room)
        for room_id in rooms:
            for aggregator in self.aggregators_by_room.get(room_id, {}).values():
                if not aggregator.can_exact_batch_advance():
                    return False
        return True

    def __advance_exact_batch(self, ticks: int, room_ids: Optional[List[str]]) -> None:
        if ticks <= 0:
            return

        rooms = self.__resolve_rooms(room_ids, self.aggregators_by_room)
        for room_id in rooms:
            for aggregator in self.aggregators_by_room.get(room_id, {}).values():
                if not aggregator.exact_batch_advance(ticks):
                    raise RuntimeError(
                        f"Aggregator '{aggregator.agg_type}' cannot exact-batch advance"
                    )

        self.current_tick += ticks

    def __peek_next_due_tick(self) -> Optional[int]:
        with self.schedular_queue.mutex:
            if not self.schedular_queue.queue:
                return None
            head = self.schedular_queue.queue[0]

        try:
            return int(head[0])
        except (IndexError, TypeError, ValueError) as error:
            raise RuntimeError(
                "Scheduler queue head is malformed; expected (due_tick, seq, task_type, task_data)"
            ) from error

    def __steps_until_next_scheduler_event(self) -> Optional[int]:
        next_due_tick = self.__peek_next_due_tick()
        if next_due_tick is None:
            return None

        current_tick = int(self.current_tick)
        if next_due_tick <= current_tick:
            return 1
        return next_due_tick - current_tick

    def __advance_one_tick(
        self, room_ids: Optional[List[str]], *, start_workflow_inline: bool
    ) -> None:
        self.__process_time_aware_devices(room_ids)
        self.__process_aggregators(room_ids)
        self.__process_schedular_queue(start_workflow_inline=start_workflow_inline)
        self.current_tick += 1

    def _fast_forward_to(
        self, to_tick: int, room_ids: Optional[List[str]] = None
    ) -> Result:
        try:
            target = int(max(0, to_tick))
        except Exception:
            return Result.fail(
                ErrorCode.VALIDATION_ERROR,
                "Invalid to_tick",
                "to_tick must be an integer >= 0",
            )

        current_tick = int(self.current_tick)
        if target <= current_tick:
            return self._get_home_state()

        if self.max_ticks is not None:
            target = min(target, int(self.max_ticks))

        try:
            while int(self.current_tick) < target:
                remaining = target - int(self.current_tick)
                if remaining <= 0:
                    break

                steps_until_event = self.__steps_until_next_scheduler_event()
                if steps_until_event is None:
                    chunk_steps = remaining
                    due_now = False
                else:
                    chunk_steps = min(remaining, max(1, int(steps_until_event)))
                    due_now = int(steps_until_event) == 1

                can_batch = (
                    chunk_steps > 0
                    and not due_now
                    and not self.__has_batch_blocking_tick_work_in_rooms(room_ids)
                    and self.__can_exact_batch_advance(room_ids)
                )

                if can_batch:
                    self.__advance_exact_batch(chunk_steps, room_ids)
                    continue

                for _ in range(chunk_steps):
                    self.__advance_one_tick(room_ids, start_workflow_inline=True)
                    if int(self.current_tick) >= target:
                        break
        except Exception as e:
            return ResultBuilder.internal_error(e)

        
        self._skip_increment_once = True

        
        return self._get_home_state()

    def get_virtual_now_seconds(self) -> float:
        return self.virtual_offset_seconds + (
            float(self.current_tick) * float(self.tick_interval)
        )

    def get_virtual_now_str(self) -> str:
        now_s = self.get_virtual_now_seconds()
        base_dt = datetime.fromtimestamp(self.virtual_epoch_seconds)
        now_dt = base_dt + timedelta(seconds=now_s)
        return now_dt.strftime("%Y-%m-%d %H:%M:%S")

    def schedule_workflow(
        self,
        start_time: str,
        steps: List[dict[str, Any]],
        description: Optional[str] = None,
    ) -> Result:
        
        if not steps:
            return Result.fail(
                ErrorCode.VALIDATION_ERROR, "Empty steps", "'steps' must not be empty"
            )

        allowed_tools = {"execute_command", "write_attribute"}
        for idx, st in enumerate(steps):
            tool = st.get("tool")
            if tool not in allowed_tools:
                return Result.fail(
                    ErrorCode.VALIDATION_ERROR,
                    "Unsupported tool",
                    f"steps[{idx}].tool '{tool}' is not allowed",
                )
            if not isinstance(st.get("args"), dict):
                return Result.fail(
                    ErrorCode.VALIDATION_ERROR,
                    "Invalid args",
                    f"steps[{idx}].args must be an object",
                )

        try:
            base_dt = datetime.fromtimestamp(self.virtual_epoch_seconds)
            start_dt = datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
            start_s = (start_dt - base_dt).total_seconds()
        except Exception:
            return Result.fail(
                ErrorCode.VALIDATION_ERROR,
                "Invalid start_time",
                "expected 'YYYY-MM-DD HH:MM:SS'",
            )

        if start_s <= self.get_virtual_now_seconds():
            return Result.fail(
                ErrorCode.VALIDATION_ERROR,
                "Start time in the past",
                "start_time must be in the future",
            )

        due_tick = int(
            math.ceil(
                (start_s - self.virtual_offset_seconds) / float(self.tick_interval)
            )
        )

        wf_id = str(uuid.uuid4())
        workflow = {
            "workflow_id": wf_id,
            "description": description,
            "start_time": start_time,
            "start_seconds": float(start_s),
            "due_tick": int(due_tick),
            "status": "pending",
            "current_step": 0,
            "total_steps": len(steps),
            "steps": steps,
            "error": None,
        }

        self.workflows_by_id[wf_id] = workflow
        self.task_seq_counter += 1
        try:
            self.schedular_queue.put_nowait(
                (int(due_tick), self.task_seq_counter, "workflow", wf_id)
            )
        except queue.Full:
            self.workflows_by_id.pop(wf_id, None)
            return Result.fail(
                ErrorCode.INTERNAL_ERROR,
                "Scheduler queue full",
                "Cannot schedule workflow",
            )

        return Result.ok({"workflow_id": wf_id})

    def _run_workflow_now(
        self,
        steps: List[dict[str, Any]],
        continue_on_error: bool = True,
        record: bool = False,
        tag: Optional[str] = None,
    ) -> Result:
        
        if not isinstance(steps, list) or not steps:
            return Result.fail(
                ErrorCode.VALIDATION_ERROR,
                "Empty steps",
                "'steps' must be a non-empty list",
            )

        allowed_tools = {"execute_command", "write_attribute"}
        step_results: List[dict[str, Any]] = []
        for idx, step in enumerate(steps):
            tool = step.get("tool")
            args = step.get("args", {})
            if tool not in allowed_tools:
                err = Result.fail(
                    ErrorCode.VALIDATION_ERROR,
                    "Unsupported tool",
                    f"steps[{idx}].tool '{tool}' is not allowed",
                )
                step_results.append(
                    {"index": idx, "success": False, "error": err.error_message}
                )
                if not continue_on_error:
                    return Result.ok(
                        {
                            "tag": tag,
                            "completed": False,
                            "continue_on_error": bool(continue_on_error),
                            "steps_total": len(steps),
                            "steps_done": idx,
                            "results": step_results,
                        }
                    )
                continue

            try:
                if tool == "execute_command":
                    exec_result = self._execute_command(**args)
                else:  
                    exec_result = self._write_attribute(**args)
            except Exception as e:
                exec_result = ResultBuilder.internal_error(e)

            step_results.append(
                {
                    "index": idx,
                    "success": bool(exec_result.success),
                    "error": None if exec_result.success else exec_result.error_message,
                }
            )

            if not exec_result.success and not continue_on_error:
                return Result.ok(
                    {
                        "tag": tag,
                        "completed": False,
                        "continue_on_error": bool(continue_on_error),
                        "steps_total": len(steps),
                        "steps_done": idx + 1,
                        "results": step_results,
                    }
                )

        return Result.ok(
            {
                "tag": tag,
                "completed": True,
                "continue_on_error": bool(continue_on_error),
                "steps_total": len(steps),
                "steps_done": len(steps),
                "results": step_results,
                "recorded": bool(record),
            }
        )

    def get_workflow_status(self, workflow_id: str) -> Result:
        
        wf = self.workflows_by_id.get(workflow_id)
        if not wf:
            return Result.fail(
                ErrorCode.VALIDATION_ERROR,
                "Not found",
                f"workflow_id '{workflow_id}' not found",
            )

        safe = {
            "workflow_id": wf["workflow_id"],
            "description": wf["description"],
            "start_time": wf["start_time"],
            "status": wf["status"],
            "current_step": wf["current_step"],
            "total_steps": wf["total_steps"],
            "error": wf.get("error"),
        }
        return Result.ok(safe)

    def get_workflow_list(
        self,
        status: Optional[str] = None,
        from_time: Optional[str] = None,
        to_time: Optional[str] = None,
    ) -> Result:
        
        workflows = list(self.workflows_by_id.values())

        if status:
            allowed_statuses = {
                "pending",
                "running",
                "completed",
                "failed",
                "cancelled",
            }
            if status not in allowed_statuses:
                return Result.fail(
                    ErrorCode.VALIDATION_ERROR,
                    "Invalid status",
                    f"status must be one of {allowed_statuses}",
                )
            workflows = [wf for wf in workflows if wf["status"] == status]

        if from_time or to_time:
            try:
                base_dt = datetime.fromtimestamp(self.virtual_epoch_seconds)

                if from_time:
                    from_dt = datetime.strptime(from_time, "%Y-%m-%d %H:%M:%S")
                    from_s = (from_dt - base_dt).total_seconds()
                    workflows = [
                        wf for wf in workflows if wf["start_seconds"] >= from_s
                    ]

                if to_time:
                    to_dt = datetime.strptime(to_time, "%Y-%m-%d %H:%M:%S")
                    to_s = (to_dt - base_dt).total_seconds()
                    workflows = [wf for wf in workflows if wf["start_seconds"] <= to_s]

            except Exception:
                return Result.fail(
                    ErrorCode.VALIDATION_ERROR,
                    "Invalid time format",
                    "expected 'YYYY-MM-DD HH:MM:SS'",
                )

        if from_time and to_time:
            from_dt = datetime.strptime(from_time, "%Y-%m-%d %H:%M:%S")
            to_dt = datetime.strptime(to_time, "%Y-%m-%d %H:%M:%S")
            if from_dt > to_dt:
                return Result.fail(
                    ErrorCode.VALIDATION_ERROR,
                    "Invalid time range",
                    "from_time must be before to_time",
                )

        safe_workflows = []
        for wf in workflows:
            safe_workflows.append(
                {
                    "workflow_id": wf["workflow_id"],
                    "description": wf["description"],
                    "start_time": wf["start_time"],
                    "status": wf["status"],
                    "current_step": wf["current_step"],
                    "total_steps": wf["total_steps"],
                }
            )

        return Result.ok(safe_workflows)

    def cancel_workflow(self, workflow_id: str) -> Result:
        
        wf = self.workflows_by_id.get(workflow_id)
        if not wf:
            return Result.fail(
                ErrorCode.VALIDATION_ERROR,
                "Not found",
                f"workflow_id '{workflow_id}' not found",
            )

        if wf["status"] == "pending":
            wf["status"] = "cancelled"
            return Result.ok({"workflow_id": workflow_id, "status": "cancelled"})
        elif wf["status"] == "cancelled":
            return Result.ok(
                {
                    "workflow_id": workflow_id,
                    "status": "cancelled",
                    "message": "Already cancelled",
                }
            )
        else:
            return Result.fail(
                ErrorCode.VALIDATION_ERROR,
                "Cannot cancel",
                f"Workflow '{workflow_id}' is in '{wf['status']}' state and cannot be cancelled",
            )

    def _add_device(
        self, room_id: str, device: Device, attributes: Optional[Dict[str, Any]] = None
    ) -> Result:
        
        if device.device_id in self.devices_by_id:
            return Result.fail(
                ErrorCode.DEVICE_ALREADY_EXISTS,
                "Device already exists",
                f"Device '{device.device_id}' already exists in room '{self.devices_by_id[device.device_id][0]}'",
            )

        if attributes:
            attr_result = device.initialize_attributes(attributes)
            if not attr_result.success:
                return attr_result
        device.set_tick_interval(self.tick_interval)

        self.__ensure_room_initialized(room_id)
        self.devices_by_room[room_id][device.device_id] = device
        self.devices_by_id[device.device_id] = (room_id, device)
        if device.is_time_aware:
            self.time_aware_devices_by_room[room_id][device.device_id] = device

        for agg in self.aggregators_by_room[room_id].values():
            if device.device_type in agg.interested_device_types:
                agg.monitored_devices[device.device_id] = device

        return Result.ok({"room_id": room_id, "device_id": device.device_id})

    def __ensure_room_initialized(self, room_id: str) -> None:
        
        if room_id in self.devices_by_room:
            return
        self.devices_by_room.setdefault(room_id, {})
        self.time_aware_devices_by_room.setdefault(room_id, {})
        self.aggregators_by_room.setdefault(room_id, {})

        if not self.enable_aggregators:
            return

        for agg_type, (agg_class, init_args) in AGGREGATOR_REGISTRY.items():
            agg = agg_class(
                agg_id=agg_type,
                current_value=init_args["current_value"],
                baseline_value=init_args["baseline_value"],
                interested_device_types=init_args["interested_device_types"],
                unit=init_args["unit"],
                tick_interval=self.tick_interval,
            )
            self.aggregators_by_room[room_id][agg.agg_type] = agg

    def ensure_room_initialized(self, room_id: str) -> None:
        self.__ensure_room_initialized(room_id)

    def _remove_device(self, device_id: str) -> Result:
        
        if device_id not in self.devices_by_id:
            return ResultBuilder.device_not_found(device_id)
        self.__remove_device_from_aggregators(device_id)
        self.__remove_device_from_room(device_id)
        self.devices_by_id.pop(device_id, None)
        return Result.ok({"device_id": device_id})

    def __remove_device_from_aggregators(self, device_id: str) -> None:
        
        if device_id not in self.devices_by_id:
            return
        room_id, _ = self.devices_by_id[device_id]
        if room_id in self.aggregators_by_room:
            for agg in self.aggregators_by_room[room_id].values():
                agg.monitored_devices.pop(device_id, None)

    def __remove_device_from_room(self, device_id: str) -> None:
        
        room_id, device = self.devices_by_id.get(device_id, (None, None))
        if room_id:
            self.devices_by_room[room_id].pop(device_id, None)
            if device and device.is_time_aware:
                self.time_aware_devices_by_room.get(room_id, {}).pop(device_id, None)

    def _set_tick_interval(self, tick_interval: float) -> Result:
        
        try:
            new_interval = float(tick_interval)
        except Exception:
            return Result.fail(
                ErrorCode.VALIDATION_ERROR,
                "Invalid tick_interval",
                "tick_interval must be a positive number",
            )

        if new_interval <= 0.0:
            return Result.fail(
                ErrorCode.VALIDATION_ERROR,
                "Invalid tick_interval",
                "tick_interval must be > 0",
            )

        previous_virtual_now = self.get_virtual_now_seconds()
        self.tick_interval = new_interval
        self.virtual_offset_seconds = previous_virtual_now - (
            float(self.current_tick) * float(self.tick_interval)
        )

        for _, device in self.devices_by_id.values():
            device.set_tick_interval(self.tick_interval)

        aggregator_count = 0
        for room_aggs in self.aggregators_by_room.values():
            for agg in room_aggs.values():
                agg.tick_interval = self.tick_interval
                aggregator_count += 1

        return Result.ok(
            {
                "tick_interval": self.tick_interval,
                "device_count": len(self.devices_by_id),
                "aggregator_count": aggregator_count,
            }
        )

    def _execute_command(
        self,
        device_id: str,
        endpoint_id: int,
        cluster_id: str,
        command_id: str,
        args: Optional[dict[str, Any]] = None,
    ):
        
        if args is None:
            args = {}
        if not device_id in self.devices_by_id:
            return ResultBuilder.device_not_found(device_id)

        device = self.devices_by_id[device_id][1]
        return device.execute_command(endpoint_id, cluster_id, command_id, **args)

    def _write_attribute(
        self,
        device_id: str,
        endpoint_id: int,
        cluster_id: str,
        attribute_id: str,
        value: Any,
    ):
        
        if not device_id in self.devices_by_id:
            return ResultBuilder.device_not_found(device_id)
        device = self.devices_by_id[device_id][1]
        return device.write_attribute(endpoint_id, cluster_id, attribute_id, value)

    def _get_all_attributes(self, device_id: str) -> Result:
        
        if device_id not in self.devices_by_id:
            return ResultBuilder.device_not_found(device_id)
        device = self.devices_by_id[device_id][1]
        return Result.ok(device.get_all_attributes())

    def _get_attribute(
        self, device_id: str, endpoint_id: int, cluster_id: str, attribute_id: str
    ) -> Result:
        
        if device_id not in self.devices_by_id:
            return ResultBuilder.device_not_found(device_id)
        device = self.devices_by_id[device_id][1]
        return Result.ok(device.get_attribute(endpoint_id, cluster_id, attribute_id))

    def _get_structure(self, device_id: str) -> Result:
        
        if device_id not in self.devices_by_id:
            return ResultBuilder.device_not_found(device_id)
        device = self.devices_by_id[device_id][1]
        return Result.ok(device.get_structure())

    def _get_room_devices(self, room_id: str) -> Result:
        
        devices = self.devices_by_room.get(room_id)
        if devices is None:
            return Result.fail(
                ErrorCode.ROOM_NOT_FOUND,
                "Room not found",
                f"Room '{room_id}' does not exist",
            )
        serialized = {
            did: {"device_type": dev.device_type} for did, dev in devices.items()
        }
        return Result.ok(serialized)

    def _get_rooms(self) -> Result:
        
        rooms = []
        for room_id in sorted(
            set(self.devices_by_room.keys()) | set(self.aggregators_by_room.keys())
        ):
            display_name = room_id.replace("_", " ").title()
            rooms.append({"room_id": room_id, "display_name": display_name})
        return Result.ok({"rooms": rooms})

    def _get_room_states(self, room_id: str) -> Result:
        
        result: Dict[str, Any] = {}
        room_aggs = self.aggregators_by_room.get(room_id)
        if room_aggs is None:
            return Result.fail(
                ErrorCode.ROOM_NOT_FOUND,
                "Room not found",
                f"Room '{room_id}' does not exist",
            )
        for agg_id, agg in room_aggs.items():
            result[agg.agg_type] = agg.get_current_value()
        return Result.ok(result)

    def _get_home_state(self) -> Result:
        
        snapshot: Dict[str, Any] = {
            "tick_interval": float(self.tick_interval),
            "current_tick": int(self.current_tick),
            "current_time": self.get_virtual_now_str(),
            "base_time": datetime.fromtimestamp(self.virtual_epoch_seconds).strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
            "rooms": {},
        }

        room_ids = set(self.devices_by_room.keys()) | set(
            self.aggregators_by_room.keys()
        )

        for room_id in room_ids:
            room_entry: Dict[str, Any] = {}

            room_aggs = self.aggregators_by_room.get(room_id, {})
            if room_aggs:
                state: Dict[str, Any] = {}
                for _, agg in room_aggs.items():
                    state[agg.agg_type] = agg.get_current_value()
                if state:
                    room_entry["state"] = state

            devices_in_room = self.devices_by_room.get(room_id, {})
            if devices_in_room:
                devices_list = []
                for device_id, device in devices_in_room.items():
                    attrs_by_cluster = device.get_all_attributes()
                    devices_list.append(
                        {
                            "device_id": device_id,
                            "device_type": device.device_type,
                            "attributes": attrs_by_cluster,
                        }
                    )
                if devices_list:
                    room_entry["devices"] = devices_list

            snapshot["rooms"][room_id] = room_entry

        return Result.ok(snapshot)

    def _get_environment_control_rules(self, state: str) -> Result:
        
        allowed_states = ["temperature", "humidity", "air_quality", "illuminance"]
        if state not in allowed_states:
            return Result.fail(
                ErrorCode.VALIDATION_ERROR,
                "Invalid state",
                f"State '{state}' is not valid, must be one of {allowed_states}",
            )

        environment_control_rules = {
            "temperature": [
                {
                    "device_type": "air_conditioner",
                    "actions": {
                        "required": [
                            {
                                "type": "execute_command",
                                "cluster_id": "OnOff",
                                "command_id": "On",
                                "args": {},
                            },
                            {
                                "type": "write_attribute",
                                "cluster_id": "Thermostat",
                                "attribute_id": "SystemMode",
                                "value": 3,
                            },  
                            {
                                "type": "write_attribute",
                                "cluster_id": "Thermostat",
                                "attribute_id": "OccupiedCoolingSetpoint",
                                "value": "<current",
                            },
                        ],
                        "optional": [
                            {
                                "type": "write_attribute",
                                "cluster_id": "FanControl",
                                "attribute_id": "PercentSetting",
                                "value": "nonzero",
                            },
                            {
                                "type": "write_attribute",
                                "cluster_id": "FanControl",
                                "attribute_id": "FanMode",
                                "value": "nonzero",
                            },
                            {
                                "type": "execute_command",
                                "cluster_id": "FanControl",
                                "command_id": "Step",
                                "args": {"Direction": 0},
                            },
                        ],
                    },
                    "note": "To lower temperature, the air conditioner must be powered ON and set to cooling mode. In addition, at least one action from the optional list must also be executed",
                },
                {
                    "device_type": "heat_pump",
                    "actions": {
                        "required": [
                            {
                                "type": "write_attribute",
                                "cluster_id": "Thermostat",
                                "attribute_id": "SystemMode",
                                "value": 4,
                            },  
                            {
                                "type": "write_attribute",
                                "cluster_id": "Thermostat",
                                "attribute_id": "OccupiedHeatingSetpoint",
                                "value": ">current",
                            },
                        ],
                        "optional": [],
                    },
                    "note": "The heat pump has no On/Off command. To raise temperature, set heating mode and a heating setpoint above the current temperature.",
                },
            ],
            "humidity": [
                {
                    "device_type": "humidifier",
                    "actions": {
                        "required": [
                            {
                                "type": "execute_command",
                                "cluster_id": "OnOff",
                                "command_id": "On",
                                "args": {},
                            }
                        ],
                        "optional": [
                            {
                                "type": "write_attribute",
                                "cluster_id": "FanControl",
                                "attribute_id": "PercentSetting",
                                "value": "nonzero",
                            },
                            {
                                "type": "write_attribute",
                                "cluster_id": "FanControl",
                                "attribute_id": "FanMode",
                                "value": "nonzero",
                            },
                            {
                                "type": "execute_command",
                                "cluster_id": "FanControl",
                                "command_id": "Step",
                                "args": {"Direction": 0},
                            },
                        ],
                    },
                    "note": "To increase humidity, the humidifier must be powered ON. In addition, at least one action from the optional list must also be executed",
                },
                {
                    "device_type": "dehumidifier",
                    "actions": {
                        "required": [
                            {
                                "type": "execute_command",
                                "cluster_id": "OnOff",
                                "command_id": "On",
                                "args": {},
                            }
                        ],
                        "optional": [
                            {
                                "type": "write_attribute",
                                "cluster_id": "FanControl",
                                "attribute_id": "PercentSetting",
                                "value": "nonzero",
                            },
                            {
                                "type": "write_attribute",
                                "cluster_id": "FanControl",
                                "attribute_id": "FanMode",
                                "value": "nonzero",
                            },
                            {
                                "type": "execute_command",
                                "cluster_id": "FanControl",
                                "command_id": "Step",
                                "args": {"Direction": 0},
                            },
                        ],
                    },
                    "note": "To decrease humidity, the dehumidifier must be powered ON. In addition, at least one action from the optional list must also be executed",
                },
            ],
            "illuminance": [
                {
                    "device_type": "on_off_light",
                    "actions": {
                        "required": [
                            {
                                "type": "execute_command",
                                "cluster_id": "OnOff",
                                "command_id": "On",
                                "args": {},
                            },
                            {
                                "type": "execute_command",
                                "cluster_id": "OnOff",
                                "command_id": "Off",
                                "args": {},
                            },
                        ],
                        "optional": [],
                    },
                    "note": "Turning the light ON increases illuminance, turning it OFF decreases it.",
                },
                {
                    "device_type": "dimmable_light",
                    "actions": {
                        "required": [
                            {
                                "type": "execute_command",
                                "cluster_id": "OnOff",
                                "command_id": "On",
                                "args": {},
                            }
                        ],
                        "optional": [
                            {
                                "type": "execute_command",
                                "cluster_id": "OnOff",
                                "command_id": "Off",
                                "args": {},
                            },
                            {
                                "type": "execute_command",
                                "cluster_id": "LevelControl",
                                "command_id": "MoveToLevel",
                                "args": {"Level": "(1-254)"},
                            },
                        ],
                    },
                    "note": "Brightness control requires the light to be ON. The LevelControl command allows fine-grained illuminance adjustment.",
                },
            ],
            "air_quality": [
                {
                    "device_type": "air_purifier",
                    "actions": {
                        "required": [
                            {
                                "type": "execute_command",
                                "cluster_id": "OnOff",
                                "command_id": "On",
                                "args": {},
                            }
                        ],
                        "optional": [
                            {
                                "type": "write_attribute",
                                "cluster_id": "FanControl",
                                "attribute_id": "PercentSetting",
                                "value": "nonzero",
                            },
                            {
                                "type": "write_attribute",
                                "cluster_id": "FanControl",
                                "attribute_id": "FanMode",
                                "value": "nonzero",
                            },
                            {
                                "type": "execute_command",
                                "cluster_id": "FanControl",
                                "command_id": "Step",
                                "args": {"Direction": 0},
                            },
                        ],
                    },
                    "note": "To improve air quality, the air purifier must be powered ON. In addition, at least one action from the optional list must also be executed",
                }
            ],
        }

        return Result.ok(
            {
                "state": state,
                "control_rules": json.dumps(environment_control_rules[state]),
            }
        )
