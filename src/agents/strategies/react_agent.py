from __future__ import annotations

import json
import time
from dataclasses import dataclass
from typing import Any, Callable, Dict, List, Optional, Sequence

from src.agents.providers.base import (
    EmptyLLMResponseError,
    LLMRetryExhaustedError,
    NonRetryableLLMError,
)
from src.agents.strategies.base import (
    AgentResult,
    AgentExecutionError,
    AgentStep,
    AgentStrategy,
    ToolInvocation,
)
from src.agents.tools import (
    TOOL_REGISTRY,
    render_tool_markdown_table,
    run_tool,
)
from src.agents.types import ChatMessage
from prompts.agents.react import SYSTEM_PROMPT, USER_PROMPT


@dataclass(slots=True)
class ReActConfig:
    max_steps: int = 20
    observation_prefix: str = "observation:"
    trace_fn: Optional[Callable[[str, str], None]] = None
    show_assistant_raw: bool = False
    strict_mode: bool = True
    max_consecutive_failures: int = 3
    require_explicit_finish: bool = True
    max_workflow_polls: int = 8
    workflow_poll_base_delay_seconds: float = 1.0
    workflow_poll_max_delay_seconds: float = 8.0


class ReActAgent(AgentStrategy):
    """
    ReAct loop that expects JSON structured output on every turn:
    {"thought": str, "action": str, "action_input": "JSON string"}
    The loop terminates when action == "finish".
    """

    def __init__(
        self,
        llm: Any,
        *,
        max_steps: Optional[int] = None,
        config: Optional[ReActConfig] = None,
    ):
        self.llm = llm
        self.config = config or ReActConfig()
        if max_steps is not None:
            self.config.max_steps = max_steps
        self._events: List[Dict[str, Any]] = []
        self._consecutive_failures = 0
        self._workflow_poll_counts: Dict[str, int] = {}

    # Prompt builders
    def _get_react_schema(self) -> dict[str, Any]:
        return {
            "type": "json_schema",
            "json_schema": {
                "name": "react_response",
                "strict": True,
                "schema": {
                    "type": "object",
                    "properties": {
                        "thought": {"type": "string"},
                        "action": {"type": "string"},
                        "action_input": {
                            "type": "string",
                            "default": "{}",
                        },
                    },
                    "required": ["thought", "action", "action_input"],
                    "additionalProperties": False,
                },
            },
        }

    def _format_action_input(self, payload: Optional[Dict[str, Any]] = None) -> str:
        return json.dumps(payload or {}, ensure_ascii=False)

    def _format_one_shot_step(
        self, thought: str, action: str, action_input: Optional[Dict[str, Any]] = None
    ) -> str:
        return json.dumps(
            {
                "thought": thought,
                "action": action,
                "action_input": self._format_action_input(action_input),
            },
            ensure_ascii=False,
        )

    def _build_one_shot_prompt(self) -> List[ChatMessage]:
        turns = [
            {
                "role": "user",
                "content": "In following turns, I’ll show you how to solve a task in the smart home environment.\n [TASK]\n User Query: Set kitchen freezer 2 to -19.0°C in 13 minutes from now, and then turn on the dimmable light 1 in the bathroom.",
            },
            {
                "role": "assistant",
                "content": self._format_one_shot_step(
                    "The user wants to schedule two actions: Set kitchen freezer 2 and turn on the dimmable light 1 in the bathroom. First action is dependent on time. First, get the current time so I can compute the schedule time 13 minutes from now.",
                    "get_current_time",
                ),
            },
            {
                "role": "user",
                "content": '{"status": {"code": 200, "message": "OK"}, "data": {"now": "YYYY-MM-DD 09:05:06"}, "error": null}',
            },
            {
                "role": "assistant",
                "content": self._format_one_shot_step(
                    "Next, I need to find the device ID for 'freezer 2' in the 'kitchen', and 'dimmable light 1' in the 'bathroom'. I'll start by getting the list of rooms.",
                    "get_rooms",
                ),
            },
            {
                "role": "user",
                "content": '{"status": {"code": 200, "message": "OK"}, "data": {"rooms": [{"room_id": "bathroom", "display_name": "Bathroom"}, {"room_id": "kitchen", "display_name": "Kitchen"}, {"room_id": "living_room", "display_name": "Living Room"}, {"room_id": "utility_room", "display_name": "Utility Room"}]}, "error": null}',
            },
            {
                "role": "assistant",
                "content": self._format_one_shot_step(
                    "I have the list of rooms. Now I need to find the devices associated with each action. I will first get the devices in the 'kitchen' to find 'freezer 2'.",
                    "get_room_devices",
                    {"room_id": "kitchen"},
                ),
            },
            {
                "role": "user",
                "content": '{"status": {"code": 200, "message": "OK"}, "data": {"kitchen_on_off_light_1": {"device_type": "on_off_light"}, "kitchen_heat_pump_1": {"device_type": "heat_pump"}, "kitchen_freezer_2": {"device_type": "freezer"}, "kitchen_fan_1": {"device_type": "fan"}}, "error": null}',
            },
            {
                "role": "assistant",
                "content": self._format_one_shot_step(
                    "I have successfully retrieved the devices in the kitchen. The freezer is identified as `kitchen_freezer_2`. Now, I need to determine the relevant cluster and attribute for temperature control. I will use `get_device_structure` to explore the device's structure.",
                    "get_device_structure",
                    {"device_id": "kitchen_freezer_2"},
                ),
            },
            {
                "role": "user",
                "content": '{"status": {"code": 200, "message": "OK"}, "data": {"device_id": "kitchen_freezer_2", "device_type": "freezer", "endpoints": {"0": {"clusters": {"BasicInformation": {"cluster_id": "BasicInformation", "attributes": {"VendorName": {"value": "LG Electronics", "type": "str", "readonly": true}, "VendorID": {"value": 1, "type": "int", "readonly": true}, "ProductName": {"value": "Freezer", "type": "str", "readonly": true}, "ProductID": {"value": 2, "type": "int", "readonly": true}}, "commands": []}}}}}, "error": null}',
            },
            {
                "role": "assistant",
                "content": self._format_one_shot_step(
                    "The current time is YYYY-MM-DD 09:05:06. The user wants to set the temperature of kitchen freezer 2 to -19.0°C at 09:18:06 (13 minutes from now). I will create a workflow to schedule this temperature change using `schedule_tool_call`.",
                    "schedule_tool_call",
                    {
                        "start_time": "YYYY-MM-DD 09:18:06",
                        "tool_call": [
                            {
                                "tool": "write_attribute",
                                "args": {
                                    "device_id": "kitchen_freezer_2",
                                    "endpoint_id": 1,
                                    "cluster_id": "TemperatureControl",
                                    "attribute_id": "TemperatureSetpoint",
                                    "value": -1900,
                                },
                            }
                        ],
                    },
                ),
            },
            {
                "role": "user",
                "content": '{"status": {"code": 200, "message": "OK"}, "data": {"workflow_id": "a54f26cd-a294-495c-a4f4-dfb860e36819"}, "error": null}',
            },
            {
                "role": "assistant",
                "content": self._format_one_shot_step(
                    "Fetch bathroom devices to verify the dimmable light device id (target: bathroom_dimmable_light_1) for confirmation.",
                    "get_room_devices",
                    {"room_id": "bathroom"},
                ),
            },
            {
                "role": "user",
                "content": '{"status": {"code": 200, "message": "OK"}, "data": {"bathroom_on_off_light_1": {"device_type": "on_off_light"}, "bathroom_fan_1": {"device_type": "heat_pump"}, "bathroom_dehumidifier_1": {"device_type": "dehumidifier"}, "bathroom_dimmable_light_2": {"device_type": "dimmable_light"}, "bathroom_humidifier_2": {"device_type": "humidifier"}}, "error": null}',
            },
            {
                "role": "assistant",
                "content": self._format_one_shot_step(
                    "From the previous step, I already checked the bathroom devices using get_room_devices. The user requested dimmable_light_1 in the bathroom, but such a device does not exist there. I will inform the user about this.",
                    "finish",
                    {
                        "answer": "I have scheduled the first request: set kitchen freezer 2 to -19.0°C in 13 minutes from now. However, for the second request, turning on dimmable_light_1 in the bathroom, that device does not exist. Please check the device again.",
                    },
                ),
            },
        ]
        return [ChatMessage(role=t["role"], content=t["content"]) for t in turns]

    # Helpers
    def _parse_structured_output(
        self, text: str
    ) -> tuple[Optional[str], Optional[Dict[str, Any]], Optional[str]]:
        def _strip_code_fence(raw: str) -> str:
            text = raw.strip()
            if text.startswith("```"):
                parts = text.split("```", 2)
                if len(parts) >= 3:
                    return parts[1].lstrip("json").strip() or parts[2].strip()
                return text.strip("`")
            return text

        try:
            # Extract the first valid JSON object from the response
            text = _strip_code_fence(text)

            # Find the first complete JSON object (from first { to matching })
            start_idx = text.find("{")
            if start_idx == -1:
                return None, None, None

            brace_count = 0
            end_idx = start_idx
            for i in range(start_idx, len(text)):
                if text[i] == "{":
                    brace_count += 1
                elif text[i] == "}":
                    brace_count -= 1
                    if brace_count == 0:
                        end_idx = i + 1
                        break

            if brace_count != 0:
                return None, None, None

            json_str = text[start_idx:end_idx]
            response = json.loads(json_str)
            if not isinstance(response, dict):
                return None, None, None

            thought_text = response.get("thought", "")
            tool_name = response.get("action")
            action_input = response.get("action_input") or {}

            if isinstance(action_input, str):
                try:
                    action_input = json.loads(action_input) if action_input else {}
                except json.JSONDecodeError:
                    self._record_event(
                        "error",
                        "action_input string is not valid JSON",
                    )
                    return None, None, thought_text

            if not isinstance(action_input, dict):
                self._record_event(
                    "error",
                    f"Invalid action_input type '{type(action_input).__name__}', expected object",
                )
                return None, None, thought_text

            return tool_name, action_input, thought_text

        except (json.JSONDecodeError, ValueError):
            return None, None, None

    def _record_event(self, event: str, payload: str) -> None:
        self._events.append({"event": event, "payload": payload})
        if self.config.trace_fn:
            self.config.trace_fn(event, payload)

    def _register_turn_failure(self, reason: str) -> None:
        self._consecutive_failures += 1
        self._record_event(
            "consecutive_failure", f"{self._consecutive_failures}:{reason}"
        )
        if (
            self.config.strict_mode
            and self._consecutive_failures >= self.config.max_consecutive_failures
        ):
            raise AgentExecutionError(
                f"Episode failed: reached {self._consecutive_failures} consecutive failures ({reason})."
            )

    def _reset_consecutive_failures(self) -> None:
        self._consecutive_failures = 0

    def _enforce_workflow_polling_budget(self, action_input: Dict[str, Any]) -> None:
        workflow_id_raw = action_input.get("workflow_id")
        if isinstance(workflow_id_raw, str) and workflow_id_raw.strip():
            workflow_key = workflow_id_raw.strip()
        else:
            workflow_key = "__missing_workflow_id__"

        poll_count = self._workflow_poll_counts.get(workflow_key, 0) + 1
        self._workflow_poll_counts[workflow_key] = poll_count

        if poll_count > self.config.max_workflow_polls:
            raise AgentExecutionError(
                f"Episode failed: workflow status polling budget exceeded for '{workflow_key}'"
            )

        if poll_count > 1:
            delay = min(
                self.config.workflow_poll_base_delay_seconds * (2 ** (poll_count - 2)),
                self.config.workflow_poll_max_delay_seconds,
            )
            time.sleep(delay)
            self._record_event("workflow_poll_backoff", f"{workflow_key}:{delay:.2f}s")

    def _call_llm(self, messages: List[ChatMessage], schema: dict[str, Any]) -> str:
        generate_fn = getattr(self.llm, "generate", None)
        if callable(generate_fn):
            return str(generate_fn(messages, response_format=schema))
        if callable(self.llm):
            return str(self.llm(messages, response_format=schema))
        raise RuntimeError("Configured LLM is not callable")

    def _ensure_messages(self, messages: List[ChatMessage]) -> None:
        if not messages:
            raise RuntimeError("Message history cannot be empty.")

    def _final_answer_from_finish(self, tool_args: Optional[Dict[str, Any]]) -> str:
        if tool_args is None:
            raise RuntimeError("finish tool requires parameters.")
        if "answer" not in tool_args:
            raise RuntimeError("finish tool requires 'answer' parameter.")
        return str(tool_args["answer"])

    # Public API
    def run(
        self,
        user_query: str,
        *,
        user_location: Optional[str] = None,
        current_time: Optional[str] = None,
    ) -> AgentResult:
        self._events = []
        self._consecutive_failures = 0
        self._workflow_poll_counts = {}

        system_content = SYSTEM_PROMPT.format(tools=render_tool_markdown_table())
        user_content = USER_PROMPT.format(
            user_query=user_query,
            user_location=user_location or "None",
            current_time=current_time or "None",
        )

        messages: List[ChatMessage] = [
            ChatMessage(role="system", content=system_content)
        ]
        messages.extend(self._build_one_shot_prompt())
        messages.append(ChatMessage(role="user", content=user_content))

        steps: List[AgentStep] = []
        tool_calls: List[ToolInvocation] = []
        raw_responses: List[str] = []
        final_answer = ""
        step_idx = 0

        for _ in range(self.config.max_steps):
            try:
                assistant_text = self._call_llm(messages, self._get_react_schema())
            except EmptyLLMResponseError as e:
                raise AgentExecutionError(f"Episode failed: {e}") from e
            except LLMRetryExhaustedError as e:
                raise AgentExecutionError(f"Episode failed: {e}") from e
            except NonRetryableLLMError as e:
                raise AgentExecutionError(f"Episode failed: {e}") from e
            except Exception as e:
                raise AgentExecutionError(
                    f"Episode failed: LLM invocation failed: {e}"
                ) from e

            if not assistant_text.strip():
                raise AgentExecutionError(
                    "Episode failed: LLM returned an empty response."
                )

            raw_responses.append(assistant_text)
            if self.config.show_assistant_raw:
                self._record_event("assistant", assistant_text)

            messages.append(ChatMessage(role="assistant", content=assistant_text))

            tool_name, tool_args, thought_text = self._parse_structured_output(
                assistant_text
            )

            if thought_text:
                self._record_event("thought", thought_text)

            if tool_name is None:
                err_obs = json.dumps(
                    {"error": "Invalid structured output format"}, ensure_ascii=False
                )
                self._register_turn_failure("invalid structured output")
                self._record_event("observation", err_obs)
                messages.append(
                    ChatMessage(
                        role="user",
                        content=f"{self.config.observation_prefix} {err_obs}",
                    )
                )
                continue

            action_input = tool_args or {}

            if tool_name.lower() == "finish":
                try:
                    final_answer = self._final_answer_from_finish(action_input)
                except RuntimeError as err:
                    err_obs = json.dumps({"error": str(err)}, ensure_ascii=False)
                    self._register_turn_failure("invalid finish payload")
                    self._record_event("observation", err_obs)
                    messages.append(
                        ChatMessage(
                            role="user",
                            content=f"{self.config.observation_prefix} {err_obs}",
                        )
                    )
                    continue

                step_idx += 1
                steps.append(
                    AgentStep(
                        step=step_idx,
                        thought=thought_text,
                        action="finish",
                        action_input=action_input,
                        observation=None,
                    )
                )
                self._reset_consecutive_failures()
                self._record_event("finish", final_answer)
                return AgentResult(
                    steps=steps,
                    tool_calls=tool_calls,
                    final_answer=final_answer,
                    raw_responses=raw_responses,
                    events=list(self._events),
                )

            if tool_name not in TOOL_REGISTRY:
                err_obs = json.dumps(
                    {"error": f"Unknown tool '{tool_name}'"}, ensure_ascii=False
                )
                self._register_turn_failure("unknown tool")
                self._record_event("observation", err_obs)
                messages.append(
                    ChatMessage(
                        role="user",
                        content=f"{self.config.observation_prefix} {err_obs}",
                    )
                )
                continue

            self._reset_consecutive_failures()
            step_idx += 1
            try:
                self._record_event("action", tool_name)
                self._record_event(
                    "action_input", json.dumps(action_input, ensure_ascii=False)
                )
            except Exception:
                self._record_event("action_input", str(action_input))
            self._record_event("waiting", tool_name)

            try:
                if tool_name == "get_workflow_status":
                    self._enforce_workflow_polling_budget(action_input)
                result = run_tool(tool_name, dict(action_input))
                observation_payload = json.dumps(result, ensure_ascii=False)
                observation_obj: Any = result
            except AgentExecutionError:
                raise
            except Exception as e:
                observation_obj = {"error": str(e)}
                observation_payload = json.dumps(observation_obj, ensure_ascii=False)

            self._record_event("observation", observation_payload)
            messages.append(
                ChatMessage(
                    role="user",
                    content=f"{self.config.observation_prefix} {observation_payload}",
                )
            )

            steps.append(
                AgentStep(
                    step=step_idx,
                    thought=thought_text,
                    action=tool_name,
                    action_input=action_input,
                    observation=observation_obj,
                )
            )
            tool_calls.append(
                ToolInvocation(
                    tool=tool_name,
                    params=dict(action_input),
                    observation=observation_obj,
                )
            )

        if not final_answer and self.config.require_explicit_finish:
            raise AgentExecutionError(
                "Episode failed: explicit finish action is required."
            )

        if not final_answer:
            final_answer = "Maximum steps reached. Please call the finish tool with your final answer."

        return AgentResult(
            steps=steps,
            tool_calls=tool_calls,
            final_answer=final_answer,
            raw_responses=raw_responses,
            events=list(self._events),
        )
