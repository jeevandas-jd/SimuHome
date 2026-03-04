from typing import Optional

from src.agents.strategies.base import AgentResult, AgentStep, AgentStrategy, ToolInvocation
from src.agents.strategies.react_agent import ReActAgent, ReActConfig
from src.agents.strategies.hi_agent import HiAgent, HiAgentConfig


def create_agent_strategy(
    name: Optional[str],
    *,
    llm,
    **kwargs,
) -> AgentStrategy:
    key = (name or "react").lower()
    if key in ("react", "react-agent"):
        return ReActAgent(llm=llm, **kwargs)
    if key in ("hi_agent", "hiagent", "hi-agent"):
        return HiAgent(llm=llm, **kwargs)

    raise ValueError(f"Unknown agent strategy '{name}'. Supported strategies: react, hi_agent")


__all__ = [
    "AgentResult",
    "AgentStep",
    "AgentStrategy",
    "ToolInvocation",
    "ReActAgent",
    "ReActConfig",
    "create_agent_strategy",
    "HiAgent",
    "HiAgentConfig",
]
