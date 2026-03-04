"""API routes for the simulator service."""

import logging
import threading
from typing import Any, Dict, Optional

from fastapi import APIRouter, HTTPException

from src.simulator.api.responses import ResponseBuilder
from src.simulator.domain.result import Result, ResultBuilder
from src.simulator.application.device_factory import (
    create_device,
    is_valid_device_type,
)
from src.simulator.application.home_initializer import (
    SimulationConfig,
    initialize_home_from_config,
)
from src.simulator.domain.home import Home

from .schemas import (
    AddDeviceRequest,
    ExecuteCommandRequest,
    FastForwardRequest,
    RunWorkflowNowRequest,
    ScheduleWorkflowRequest,
    SetTickIntervalRequest,
    WriteAttributeRequest,
)

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api")
home = Home(base_time="2025-08-23 00:00:00")
home_lock = threading.Lock()


def get_home() -> Home:
    """Return the singleton :class:`Home` instance backing the API."""
    with home_lock:
        return home


def _queue_api(api_type: str, **kwargs: Any) -> Result:
    current_home = get_home()
    return current_home.queue_api(api_type, **kwargs)


def _result_or_raise(result: Result | None) -> Dict[str, Any]:
    if result is None:
        raise HTTPException(
            status_code=500,
            detail="No response from simulator queue",
        )

    payload = ResponseBuilder.from_result(result)

    status = payload.get("status")
    if not isinstance(status, dict):
        raise HTTPException(status_code=500, detail="Simulator response missing status")

    raw_code = status.get("code")
    if raw_code is None:
        raise HTTPException(
            status_code=500, detail="Simulator response missing status code"
        )

    try:
        status_code = int(raw_code)
    except Exception:
        raise HTTPException(
            status_code=500, detail="Simulator response has invalid status code"
        )

    if status_code >= 400:
        error_detail = None
        error_obj = payload.get("error")
        if isinstance(error_obj, dict):
            error_detail = error_obj.get("detail")

        status_message = status.get("message")
        detail = error_detail or status_message or "Simulator request failed"
        raise HTTPException(status_code=status_code, detail=str(detail))

    return payload


@router.post("/simulation/reset")
def reset_simulation(cfg: SimulationConfig):
    """Stop the running simulation, re-create :class:`Home`, and start again."""

    global home

    with home_lock:
        try:
            home.stop_simulation()

            new_home = Home(
                tick_interval=cfg.tick_interval,
                enable_aggregators=cfg.enable_aggregators,
                max_ticks=cfg.max_ticks,
                fast_forward=bool(cfg.fast_forward),
                base_time=cfg.base_time,
            )

            init_result = initialize_home_from_config(new_home, cfg)
            if not init_result.success:
                logger.error(
                    "Home initialization failed: %s", init_result.error_message
                )
                return ResponseBuilder.from_result(init_result)

            if init_result.data is None:
                error_result = ResultBuilder.internal_error(
                    Exception("Initialization result missing data payload")
                )
                return ResponseBuilder.from_result(error_result)

            init_data = init_result.data
            initial_home_config = init_data.get("initial_home_config")
            if not initial_home_config:
                error_result = ResultBuilder.internal_error(
                    Exception("Home state not found in initialization result")
                )
                return ResponseBuilder.from_result(error_result)

            new_home.start_simulation()

            home = new_home

            success_result = Result.ok(
                {
                    "meta": {
                        "max_ticks": cfg.max_ticks,
                        "fast_forward": bool(cfg.fast_forward),
                        "num_rooms": init_data.get("total_rooms", 0),
                        "num_devices": init_data.get("total_devices", 0),
                        "base_time": cfg.base_time,
                    },
                    "initial_home_config": initial_home_config,
                }
            )
            return ResponseBuilder.from_result(success_result)

        except Exception as error:  # pylint: disable=broad-except
            logger.exception("Simulation reset failed")
            error_result = ResultBuilder.internal_error(error)
            return ResponseBuilder.from_result(error_result)


@router.post("/devices/add")
def add_device(req: AddDeviceRequest):
    if not is_valid_device_type(req.device_type):
        raise HTTPException(
            status_code=400, detail=f"Unsupported device_type: {req.device_type}"
        )

    device = create_device(req.device_type, req.device_id)
    resp = _queue_api(
        "add_device", room_id=req.room_id, device=device, attributes=req.attributes
    )
    return _result_or_raise(resp)


@router.delete("/devices/{device_id}")
def remove_device(device_id: str):
    resp = _queue_api("remove_device", device_id=device_id)
    return _result_or_raise(resp)


@router.get("/environment/control_rules/{state}")
def get_environment_control_rules(state: str):
    resp = _queue_api("get_environment_control_rules", state=state)
    return _result_or_raise(resp)


@router.post("/simulation/tick_interval")
def set_tick_interval(req: SetTickIntervalRequest):
    resp = _queue_api("set_tick_interval", tick_interval=req.tick_interval)
    return _result_or_raise(resp)


@router.post("/simulation/fast_forward_to")
def fast_forward_to(req: FastForwardRequest):
    """Advance the simulation to a target tick within the main loop context."""

    current_home = get_home()

    if not current_home.is_running:
        current_home.start_simulation()

    resp = current_home.queue_api(
        "fast_forward_to", to_tick=int(req.to_tick), room_ids=req.room_ids
    )
    return _result_or_raise(resp)


@router.post("/devices/{device_id}/commands")
def execute_command(device_id: str, req: ExecuteCommandRequest):
    resp = _queue_api(
        "execute_command",
        device_id=device_id,
        endpoint_id=req.endpoint_id,
        cluster_id=req.cluster_id,
        command_id=req.command_id,
        args=req.args or {},
    )
    return _result_or_raise(resp)


@router.post("/devices/{device_id}/attributes/write")
def write_attribute(device_id: str, req: WriteAttributeRequest):
    resp = _queue_api(
        "write_attribute",
        device_id=device_id,
        endpoint_id=req.endpoint_id,
        cluster_id=req.cluster_id,
        attribute_id=req.attribute_id,
        value=req.value,
    )
    return _result_or_raise(resp)


@router.get("/devices/{device_id}/attributes")
def get_all_attributes(device_id: str):
    current_home = get_home()
    if current_home.is_running:
        resp = current_home.queue_api("get_all_attributes", device_id=device_id)
        return _result_or_raise(resp)
    result = current_home._get_all_attributes(device_id)  # noqa: SLF001
    return ResponseBuilder.from_result(result)


@router.get("/devices/{device_id}/attributes/{endpoint_id}/{cluster_id}/{attribute_id}")
def get_attribute(device_id: str, endpoint_id: int, cluster_id: str, attribute_id: str):
    current_home = get_home()
    if current_home.is_running:
        resp = current_home.queue_api(
            "get_attribute",
            device_id=device_id,
            endpoint_id=endpoint_id,
            cluster_id=cluster_id,
            attribute_id=attribute_id,
        )
        return _result_or_raise(resp)
    result = current_home._get_attribute(  # noqa: SLF001
        device_id, endpoint_id, cluster_id, attribute_id
    )
    return ResponseBuilder.from_result(result)


@router.get("/devices/{device_id}/structure")
def get_structure(device_id: str):
    current_home = get_home()
    if current_home.is_running:
        resp = current_home.queue_api("get_structure", device_id=device_id)
        return _result_or_raise(resp)
    result = current_home._get_structure(device_id)  # noqa: SLF001
    return ResponseBuilder.from_result(result)


@router.get("/rooms/{room_id}/devices")
def get_room_devices(room_id: str):
    current_home = get_home()
    if current_home.is_running:
        resp = current_home.queue_api("get_room_devices", room_id=room_id)
        return _result_or_raise(resp)
    result = current_home._get_room_devices(room_id)  # noqa: SLF001
    return ResponseBuilder.from_result(result)


@router.get("/rooms/{room_id}/states")
def get_room_states(room_id: str):
    current_home = get_home()
    if current_home.is_running:
        resp = current_home.queue_api("get_room_states", room_id=room_id)
        return _result_or_raise(resp)
    result = current_home._get_room_states(room_id)  # noqa: SLF001
    return ResponseBuilder.from_result(result)


@router.get("/rooms")
def get_rooms():
    current_home = get_home()
    if current_home.is_running:
        resp = current_home.queue_api("get_rooms")
        return _result_or_raise(resp)
    result = current_home._get_rooms()  # noqa: SLF001
    return ResponseBuilder.from_result(result)


@router.get("/home/state")
def get_home_state():
    """Return a full home snapshot in ``home_config`` format."""

    current_home = get_home()
    if current_home.is_running:
        resp = current_home.queue_api("get_home_state")
        return _result_or_raise(resp)
    result = current_home._get_home_state()  # noqa: SLF001
    return ResponseBuilder.from_result(result)


@router.get("/__health__")
def health_check():
    return ResponseBuilder.from_result(Result.ok())


@router.post("/schedule/workflow")
def schedule_workflow(req: ScheduleWorkflowRequest):
    allowed = {"execute_command", "write_attribute"}
    for i, step in enumerate(req.steps):
        if step.tool not in allowed:
            raise HTTPException(
                status_code=400, detail=f"Unsupported tool at steps[{i}]: {step.tool}"
            )

    resp = _queue_api(
        "schedule_workflow",
        start_time=req.start_time,
        steps=[{"tool": step.tool, "args": step.args} for step in req.steps],
        description=req.description,
    )
    return _result_or_raise(resp)


@router.get("/schedule/workflow/{workflow_id}/status")
def get_workflow_status(workflow_id: str):
    resp = _queue_api("get_workflow_status", workflow_id=workflow_id)
    return _result_or_raise(resp)


@router.post("/schedule/workflow/{workflow_id}/cancel")
def cancel_workflow(workflow_id: str):
    resp = _queue_api("cancel_workflow", workflow_id=workflow_id)
    return _result_or_raise(resp)


@router.get("/schedule/workflows")
def get_workflow_list(
    status: Optional[str] = None,
    from_time: Optional[str] = None,
    to_time: Optional[str] = None,
):
    resp = _queue_api(
        "get_workflow_list",
        status=status,
        from_time=from_time,
        to_time=to_time,
    )
    return _result_or_raise(resp)


@router.get("/time")
def get_current_time():
    resp = _queue_api("get_current_time")
    return _result_or_raise(resp)


@router.post("/workflow/run_now")
def run_workflow_now(req: RunWorkflowNowRequest):
    allowed = {"execute_command", "write_attribute"}
    for i, step in enumerate(req.steps):
        if step.tool not in allowed:
            raise HTTPException(
                status_code=400, detail=f"Unsupported tool at steps[{i}]: {step.tool}"
            )

    current_home = get_home()
    if not current_home.is_running:
        current_home.start_simulation()

    try:
        current_home.api_queue.put_nowait(
            {
                "api_type": "run_workflow_now",
                "args": {
                    "steps": [
                        {"tool": step.tool, "args": step.args} for step in req.steps
                    ],
                    "continue_on_error": bool(req.continue_on_error),
                    "record": bool(req.record),
                    "tag": req.tag,
                },
            }
        )
    except Exception as exc:  # pylint: disable=broad-except
        raise HTTPException(
            status_code=503, detail="API queue full or unavailable"
        ) from exc

    return ResponseBuilder.from_result(
        Result.ok(
            {
                "accepted": True,
                "queued": True,
                "steps": len(req.steps),
                "continue_on_error": bool(req.continue_on_error),
                "record": bool(req.record),
                "tag": req.tag,
            }
        )
    )
