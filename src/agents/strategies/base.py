from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Protocol

from src.agents.types import ChatMessage


class AgentExecutionError(RuntimeError):
    pass


@dataclass(slots=True)
class AgentStep:
    step: int
    thought: Optional[str]
    action: Optional[str]
    action_input: Optional[Dict[str, Any]]
    observation: Optional[Any]

    def to_dict(self) -> Dict[str, Any]:
        return {
            "step": self.step,
            "thought": self.thought,
            "action": self.action,
            "action_input": self.action_input,
            "observation": self.observation,
        }


@dataclass(slots=True)
class ToolInvocation:
    tool: str
    params: Dict[str, Any]
    observation: Any

    def to_dict(self) -> Dict[str, Any]:
        return {
            "tool": self.tool,
            "params": self.params,
            "observation": self.observation,
        }


@dataclass(slots=True)
class AgentResult:
    steps: List[AgentStep]
    tool_calls: List[ToolInvocation]
    final_answer: str
    raw_responses: List[str]
    events: List[Dict[str, Any]] = field(default_factory=list)


class AgentStrategy(Protocol):
    def run(
        self,
        user_query: str,
        *,
        user_location: Optional[str] = None,
        current_time: Optional[str] = None,
    ) -> AgentResult: ...


__all__ = [
    "AgentStrategy",
    "AgentResult",
    "AgentStep",
    "ToolInvocation",
    "ChatMessage",
    "AgentExecutionError",
]
