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
from src.agents.memory.hi_memory import HiMemory
from prompts.agents.hi_agent import (
    SYSTEM_PROMPT,
    PLANNING_PROMPT,
    ACTION_PROMPT,
    SUMMARIZATION_PROMPT,
)


@dataclass(slots=True)
class HiAgentConfig:
    max_steps: int = 50  # Default, overridden by config
    max_subgoals: int = 10
    observation_prefix: str = "observation:"
    show_assistant_raw: bool = False
    max_context_tokens: Optional[int] = None  # None means no limit
    strict_mode: bool = True
    max_consecutive_failures: int = 3
    require_explicit_finish: bool = True
    max_workflow_polls: int = 8
    workflow_poll_base_delay_seconds: float = 1.0
    workflow_poll_max_delay_seconds: float = 8.0


class HiAgent(AgentStrategy):
    """
    HiAgent Strategy: Planning -> Subgoal Execution -> Summarization -> Next Subgoal
    """

    def __init__(
        self,
        llm: Callable[[Sequence[ChatMessage]], str] | Any,
        *,
        max_steps: Optional[int] = None,
        config: Optional[HiAgentConfig] = None,
    ):
        self.llm = llm
        self.config = config or HiAgentConfig()
        if max_steps is not None:
            self.config.max_steps = max_steps
        self.memory = HiMemory()
        self._events: List[Dict[str, Any]] = []
        self._consecutive_failures = 0
        self._workflow_poll_counts: Dict[str, int] = {}

    def _record_event(self, event: str, payload: str) -> None:
        self._events.append({"event": event, "payload": payload})

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

    def _normalize_action_input(self, raw_action_input: Any) -> Dict[str, Any]:
        if raw_action_input is None:
            return {}

        action_input = raw_action_input
        if isinstance(action_input, str):
            if not action_input.strip():
                return {}
            try:
                action_input = json.loads(action_input)
            except json.JSONDecodeError as exc:
                raise ValueError("action_input string is not valid JSON") from exc

        if not isinstance(action_input, dict):
            raise ValueError(
                f"Invalid action_input type '{type(action_input).__name__}', expected object"
            )

        return action_input

    def _get_planning_schema(self) -> dict[str, Any]:
        return {
            "type": "json_schema",
            "json_schema": {
                "name": "planning_response",
                "strict": True,
                "schema": {
                    "type": "object",
                    "properties": {
                        "subgoals": {"type": "array", "items": {"type": "string"}}
                    },
                    "required": ["subgoals"],
                    "additionalProperties": False,
                },
            },
        }

    def _get_action_schema(self) -> dict[str, Any]:
        return {
            "type": "json_schema",
            "json_schema": {
                "name": "action_response",
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

    def _call_llm(
        self,
        messages: List[ChatMessage],
        schema: Optional[dict[str, Any]] = None,
    ) -> str:
        kwargs: dict[str, Any] = {}
        if schema:
            kwargs["response_format"] = schema

        generate_fn = getattr(self.llm, "generate", None)
        if callable(generate_fn):
            return str(generate_fn(messages, **kwargs))

        if callable(self.llm):
            return str(self.llm(messages, **kwargs))

        raise RuntimeError("Configured LLM is not callable")

    def _estimate_tokens(self, text: str) -> int:
        """Simple token estimation: ~4 characters per token for English."""
        return len(text) // 4

    def _should_use_sampling(self, system_prompt: str, context_prompt: str) -> bool:
        """Check if we should use memory sampling based on estimated tokens."""
        if self.config.max_context_tokens is None:
            return False

        combined_text = system_prompt + context_prompt
        estimated_tokens = self._estimate_tokens(combined_text)
        # Use sampling if we're approaching 80% of the limit
        return estimated_tokens > (self.config.max_context_tokens * 0.8)

    def _plan_subgoals(
        self,
        user_query: str,
        user_location: Optional[str],
        current_time: Optional[str],
    ) -> List[str]:
        prompt = PLANNING_PROMPT.format(
            user_query=user_query,
            user_location=user_location,
            current_time=current_time,
        )
        messages = [
            ChatMessage(
                role="system",
                content=SYSTEM_PROMPT.format(tools=render_tool_markdown_table()),
            ),
            ChatMessage(role="user", content=prompt),
        ]

        try:
            response = self._call_llm(messages, schema=self._get_planning_schema())
            self._record_event("planning_response", response)
        except (EmptyLLMResponseError, LLMRetryExhaustedError, NonRetryableLLMError):
            raise
        except Exception as e:
            self._record_event("planning_error", str(e))
            raise AgentExecutionError(f"Episode failed: planning invocation failed: {e}") from e

        try:
            # Clean up markdown code blocks if present
            cleaned_response = response.strip()
            if cleaned_response.startswith("```"):
                parts = cleaned_response.split("```", 2)
                if len(parts) >= 3:
                    cleaned_response = (
                        parts[1].lstrip("json").strip() or parts[2].strip()
                    )
                else:
                    cleaned_response = cleaned_response.strip("`")

            data = json.loads(cleaned_response)
            if isinstance(data, dict) and "subgoals" in data:
                return [str(s) for s in data["subgoals"]]
            raise ValueError("planning response missing required 'subgoals' field")

        except Exception as e:
            self._record_event("planning_error", str(e))
            raise AgentExecutionError(f"Episode failed: invalid planning response: {e}") from e

    def _summarize_subgoal(self, subgoal: str) -> None:
        history = self.memory.get_short_term_memory_str()
        prompt = SUMMARIZATION_PROMPT.format(subgoal=subgoal, history=history)
        messages = [
            ChatMessage(
                role="system",
                content="You are a helpful assistant that summarizes execution history.",
            ),
            ChatMessage(role="user", content=prompt),
        ]
        try:
            summary = self._call_llm(messages)
        except (EmptyLLMResponseError, LLMRetryExhaustedError, NonRetryableLLMError):
            raise
        except Exception as e:
            self._record_event("summarization_error", str(e))
            raise AgentExecutionError(f"Episode failed: summarization failed: {e}") from e

        self.memory.summarize_current_subgoal(summary)
        self._record_event("summarization", summary)

    def run(
        self,
        user_query: str,
        *,
        user_location: Optional[str] = None,
        current_time: Optional[str] = None,
    ) -> AgentResult:
        self._events = []
        self.memory = HiMemory()  # Reset memory for new run
        self._consecutive_failures = 0
        self._workflow_poll_counts = {}

        # 1. Planning Phase
        subgoals = self._plan_subgoals(user_query, user_location, current_time)
        self.memory.set_subgoals(subgoals)
        self._record_event("plan", str(subgoals))

        steps: List[AgentStep] = []
        tool_calls: List[ToolInvocation] = []
        raw_responses: List[str] = []
        final_answer = ""
        step_idx = 0

        # 2. Execution Loop
        while self.memory.current_subgoal:
            current_subgoal = self.memory.current_subgoal
            self._record_event("current_subgoal", current_subgoal)

            # Subgoal Loop
            subgoal_finished = False
            for _ in range(self.config.max_steps):
                # Build Context with potential sampling
                system_prompt_text = SYSTEM_PROMPT.format(
                    tools=render_tool_markdown_table()
                )

                # Try without sampling first
                short_term_str = self.memory.get_short_term_memory_str(
                    use_sampling=False
                )
                context_prompt = ACTION_PROMPT.format(
                    current_subgoal=current_subgoal,
                    global_context=json.dumps(self.memory.global_context, indent=2)
                    if self.memory.global_context
                    else "None",
                    long_term_memory=self.memory.get_long_term_memory_str(),
                    short_term_memory=short_term_str,
                )

                # Check if we need sampling
                if self._should_use_sampling(system_prompt_text, context_prompt):
                    # Use boundary-preserved sampling
                    short_term_str = self.memory.get_short_term_memory_str(
                        use_sampling=True, max_size=self.memory.max_short_term_size
                    )
                    context_prompt = ACTION_PROMPT.format(
                        current_subgoal=current_subgoal,
                        global_context=json.dumps(self.memory.global_context, indent=2)
                        if self.memory.global_context
                        else "None",
                        long_term_memory=self.memory.get_long_term_memory_str(),
                        short_term_memory=short_term_str,
                    )
                    self._record_event(
                        "memory_sampling",
                        f"Sampled to {len(self.memory.get_sampled_short_term_memory())} observations",
                    )

                messages = [
                    ChatMessage(role="system", content=system_prompt_text),
                    ChatMessage(role="user", content=context_prompt),
                ]

                # Get Action
                try:
                    assistant_text = self._call_llm(
                        messages, schema=self._get_action_schema()
                    )
                except (EmptyLLMResponseError, LLMRetryExhaustedError, NonRetryableLLMError):
                    raise
                except Exception as e:
                    raise AgentExecutionError(
                        f"Episode failed: LLM invocation failed: {e}"
                    ) from e

                if not assistant_text.strip():
                    error_msg = "LLM returned an empty response"
                    self._register_turn_failure("empty model response")
                    self._record_event("error", error_msg)
                    self.memory.add_observation("unknown", "{}", error_msg)
                    continue

                raw_responses.append(assistant_text)
                if self.config.show_assistant_raw:
                    self._record_event("assistant", assistant_text)

                # Parse Action
                try:
                    # Basic cleaning
                    text = assistant_text.strip()
                    if text.startswith("```"):
                        parts = text.split("```", 2)
                        if len(parts) >= 3:
                            text = parts[1].lstrip("json").strip() or parts[2].strip()
                        else:
                            text = text.strip("`")

                    response_dict = json.loads(text)
                    if not isinstance(response_dict, dict):
                        raise ValueError("structured output must be a JSON object")

                    thought = response_dict.get("thought", "")
                    action = response_dict.get("action")
                    if not isinstance(action, str) or not action.strip():
                        raise ValueError("action must be a non-empty string")

                    action_input = self._normalize_action_input(
                        response_dict.get("action_input", {})
                    )

                except Exception as e:
                    # Handle parse error
                    error_msg = f"Error parsing response: {str(e)}"
                    self._register_turn_failure("invalid structured output")
                    self._record_event("error", error_msg)
                    # Add error to memory to inform agent
                    self.memory.add_observation("unknown", "{}", error_msg)
                    continue

                self._reset_consecutive_failures()
                step_idx += 1

                # Handle Virtual Tools
                if action == "retrieve_trajectory":
                    subgoal_idx = action_input.get("subgoal_index")
                    if subgoal_idx is not None:
                        try:
                            idx = int(subgoal_idx)
                            trajectory = self.memory.get_trajectory(idx)
                            if trajectory:
                                observation = json.dumps(trajectory, ensure_ascii=False)
                            else:
                                observation = json.dumps(
                                    {
                                        "error": f"No trajectory found for subgoal index {idx}"
                                    },
                                    ensure_ascii=False,
                                )
                        except ValueError:
                            observation = json.dumps(
                                {"error": "Invalid subgoal_index format"},
                                ensure_ascii=False,
                            )
                    else:
                        observation = json.dumps(
                            {"error": "Missing subgoal_index argument"},
                            ensure_ascii=False,
                        )

                    self._record_event("observation", observation)
                    self.memory.add_observation(
                        action, json.dumps(action_input), observation
                    )
                    steps.append(
                        AgentStep(step_idx, thought, action, action_input, observation)
                    )
                    continue

                if action == "finish_subgoal":
                    steps.append(
                        AgentStep(
                            step_idx, thought, "finish_subgoal", action_input, None
                        )
                    )
                    # Fix: Record finish_subgoal in memory so it's included in the summary
                    self.memory.add_observation(
                        action,
                        json.dumps(action_input),
                        "Subgoal finished successfully",
                    )
                    self._summarize_subgoal(current_subgoal)
                    subgoal_finished = True
                    self._reset_consecutive_failures()
                    break  # Break subgoal loop, proceed to next subgoal

                if action == "finish":
                    # GUARDRAIL: Check if there are remaining subgoals
                    remaining_subgoals = self.memory.subgoals[
                        self.memory.current_subgoal_index + 1 :
                    ]
                    if remaining_subgoals:
                        # Reject finish
                        error_msg = (
                            f"CRITICAL ERROR: You cannot finish the task yet. "
                            f"You have {len(remaining_subgoals)} remaining subgoals to complete: {remaining_subgoals}. "
                            f"Please complete the current subgoal '{current_subgoal}' and use 'finish_subgoal' to proceed."
                        )
                        observation = json.dumps(
                            {"error": error_msg}, ensure_ascii=False
                        )
                        self._register_turn_failure("premature finish action")
                        self._record_event("error", error_msg)
                        # Add to memory so agent sees the error
                        self.memory.add_observation(
                            action, json.dumps(action_input), observation
                        )
                        steps.append(
                            AgentStep(
                                step_idx, thought, action, action_input, observation
                            )
                        )
                        continue

                    # If no remaining subgoals, proceed to finish
                    if "answer" not in action_input:
                        error_msg = "finish tool requires 'answer' parameter"
                        observation = json.dumps(
                            {"error": error_msg}, ensure_ascii=False
                        )
                        self._register_turn_failure("invalid finish payload")
                        self._record_event("error", error_msg)
                        self.memory.add_observation(
                            action, json.dumps(action_input), observation
                        )
                        steps.append(
                            AgentStep(
                                step_idx, thought, action, action_input, observation
                            )
                        )
                        continue

                    final_answer = str(action_input.get("answer", ""))
                    steps.append(
                        AgentStep(step_idx, thought, "finish", action_input, None)
                    )
                    self._reset_consecutive_failures()
                    self._record_event("finish", final_answer)
                    return AgentResult(
                        steps, tool_calls, final_answer, raw_responses, self._events
                    )

                # Execute Real Tool
                self._record_event("action", action)
                observation = ""
                if action in TOOL_REGISTRY:
                    try:
                        if action == "get_workflow_status":
                            self._enforce_workflow_polling_budget(action_input)
                        result = run_tool(action, action_input)
                        observation = json.dumps(result, ensure_ascii=False)
                    except AgentExecutionError:
                        raise
                    except Exception as e:
                        observation = json.dumps({"error": str(e)}, ensure_ascii=False)
                else:
                    self._register_turn_failure("unknown tool")
                    observation = json.dumps(
                        {"error": f"Unknown tool '{action}'"}, ensure_ascii=False
                    )

                if action in TOOL_REGISTRY:
                    self._reset_consecutive_failures()

                self._record_event("observation", observation)

                # Update Global Context for Time
                if (
                    action == "get_current_time"
                    and "reference_time" not in self.memory.global_context
                ):
                    # Try to parse observation if it's a JSON string, otherwise use raw
                    try:
                        # If observation is just a string like "2025...", use it directly
                        # If it's JSON like "{\"current_time\": ...}", parse it
                        if observation.strip().startswith("{"):
                            obs_data = json.loads(observation)
                            self.memory.global_context["reference_time"] = obs_data
                        else:
                            self.memory.global_context["reference_time"] = (
                                observation.strip('"')
                            )
                    except json.JSONDecodeError as error:
                        raise AgentExecutionError(
                            f"Episode failed: invalid get_current_time payload: {error}"
                        ) from error

                # Update Memory
                self.memory.add_observation(
                    action, json.dumps(action_input), observation
                )

                steps.append(
                    AgentStep(step_idx, thought, action, action_input, observation)
                )
                tool_calls.append(ToolInvocation(action, action_input, observation))

            if not subgoal_finished:
                raise AgentExecutionError(
                    f"Episode failed: subgoal '{current_subgoal}' was not finished explicitly within step budget."
                )

        if self.config.require_explicit_finish:
            raise AgentExecutionError(
                "Episode failed: explicit finish action is required."
            )

        return AgentResult(
            steps,
            tool_calls,
            final_answer or "Task completed without explicit finish.",
            raw_responses,
            self._events,
        )
