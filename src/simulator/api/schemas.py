"""Pydantic request/response schemas for the simulator API."""

from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field

class AddDeviceRequest(BaseModel):
    room_id: str = Field(..., description="Room name")
    device_type: str = Field(
        ..., description="on_off_light, dimmable_light, air_conditioner, air_purifier etc."
    )
    device_id: str = Field(..., description="Unique device id")
    attributes: Optional[Dict[str, Any]] = Field(
        None, description="Initial device attributes (e.g., {'1.OnOff.OnOff': True})"
    )


class SetTickIntervalRequest(BaseModel):
    tick_interval: float = Field(..., gt=0, description="Tick interval in seconds")


class FastForwardRequest(BaseModel):
    to_tick: int = Field(
        ..., ge=0, description="Target tick to fast-forward to (inclusive)"
    )
    room_ids: Optional[List[str]] = Field(
        None,
        description="Optional list of room IDs to process. If None, processes all rooms.",
    )


class ExecuteCommandRequest(BaseModel):
    endpoint_id: int
    cluster_id: str
    command_id: str
    args: Optional[Dict[str, Any]] = None


class WriteAttributeRequest(BaseModel):
    endpoint_id: int
    cluster_id: str
    attribute_id: str
    value: Any


class ScheduleWorkflowStep(BaseModel):
    tool: str = Field(..., description="execute_command | write_attribute")
    args: Dict[str, Any] = Field(..., description="Tool arguments")


class ScheduleWorkflowRequest(BaseModel):
    start_time: str = Field(..., description="YYYY-MM-DD HH:MM:SS (virtual time)")
    description: Optional[str] = Field(None, description="Optional description")
    steps: List[ScheduleWorkflowStep] = Field(
        ..., min_length=1, description="Sequential steps"
    )


class RunWorkflowNowStep(BaseModel):
    tool: str = Field(..., description="execute_command | write_attribute")
    args: Dict[str, Any] = Field(..., description="Tool arguments")


class RunWorkflowNowRequest(BaseModel):
    steps: List[RunWorkflowNowStep] = Field(
        ..., min_length=1, description="Sequential steps to run now"
    )
    continue_on_error: bool = Field(True, description="Continue when a step fails")
    record: bool = Field(False, description="Record summary internally")
    tag: Optional[str] = Field(None, description="Opaque tag for tracing")