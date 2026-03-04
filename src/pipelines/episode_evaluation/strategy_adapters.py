from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, Optional, Protocol

from src.agents.strategies import AgentResult, AgentStrategy


@dataclass(slots=True)
class EpisodeContext:
    query: str
    user_location: Optional[str]
    current_time: Optional[str]
    queries: Optional[list[str]] = None


@dataclass(slots=True)
class StrategyArtifacts:
    agent_result: AgentResult
    storage_payload: Dict[str, Any]
    evaluation_payload: Dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        self.evaluation_payload.setdefault("strategy_output", self.storage_payload)

        steps = self.evaluation_payload.get("steps")
        if not isinstance(steps, list):
            raise ValueError(
                "StrategyArtifacts.evaluation_payload.steps must be a list"
            )

        trace_type = self.evaluation_payload.get("trace_type")
        if not isinstance(trace_type, str) or not trace_type:
            raise ValueError(
                "StrategyArtifacts.evaluation_payload.trace_type must be a non-empty string"
            )

        final_answer = self.storage_payload.get("final_answer")
        if isinstance(final_answer, str):
            self.evaluation_payload.setdefault("final_answer", final_answer)


class StrategyAdapter(Protocol):
    def run(self, agent: AgentStrategy, ctx: EpisodeContext) -> StrategyArtifacts: ...


class ReActStrategyAdapter:
    def run(self, agent: AgentStrategy, ctx: EpisodeContext) -> StrategyArtifacts:
        result = agent.run(
            ctx.query,
            user_location=ctx.user_location,
            current_time=ctx.current_time,
        )

        steps = [step.to_dict() for step in result.steps]
        storage_payload = {
            "steps": steps,
            "trace_type": "react",
            "raw_responses": list(result.raw_responses),
            "final_answer": result.final_answer,
        }
        evaluation_payload = {
            "steps": steps,
            "trace_type": "react",
        }

        return StrategyArtifacts(
            agent_result=result,
            storage_payload=storage_payload,
            evaluation_payload=evaluation_payload,
        )


class HiAgentAdapter:
    def run(self, agent: AgentStrategy, ctx: EpisodeContext) -> StrategyArtifacts:
        result = agent.run(
            ctx.query,
            user_location=ctx.user_location,
            current_time=ctx.current_time,
        )

        steps = [step.to_dict() for step in result.steps]
        logs = list(result.events)

        storage_payload = {
            "steps": steps,
            "trace_type": "hi_agent",
            "hi_agent_logs": logs,
            "hi_agent_raw_responses": list(result.raw_responses),
            "final_answer": result.final_answer,
        }
        evaluation_payload = {
            "hi_agent_logs": logs,
            "steps": steps,
            "trace_type": "hi_agent",
        }

        return StrategyArtifacts(
            agent_result=result,
            storage_payload=storage_payload,
            evaluation_payload=evaluation_payload,
        )


def get_strategy_adapter(strategy: Optional[str]) -> StrategyAdapter:
    key = (strategy or "react").lower()
    if key in ("react", "react-agent"):
        return ReActStrategyAdapter()
    if key in ("hi_agent", "hiagent", "hi-agent"):
        return HiAgentAdapter()

    raise ValueError(f"Unsupported strategy adapter for '{strategy}'.")
