from __future__ import annotations

import sys
import types


def _ensure_langchain_pydantic_v1() -> None:
    """Shim for langgraph packages expecting langchain_core.pydantic_v1."""
    try:
        import langchain_core.pydantic_v1  # type: ignore
        return
    except ModuleNotFoundError:
        pass

    from pydantic import BaseModel, Field, ValidationError, root_validator

    shim = types.ModuleType("langchain_core.pydantic_v1")
    shim.BaseModel = BaseModel
    shim.Field = Field
    shim.ValidationError = ValidationError
    shim.root_validator = root_validator
    sys.modules["langchain_core.pydantic_v1"] = shim


_ensure_langchain_pydantic_v1()

from src.agents.providers import (
    LLMProvider,
    OpenAIChatProvider,
)
from src.agents.strategies import (
    AgentResult,
    AgentStrategy,
    ReActAgent,
    ReActConfig,
    create_agent_strategy,
    HiAgent,
    HiAgentConfig,
)
from src.agents.types import ChatMessage

__all__ = [
    "ChatMessage",
    "LLMProvider",
    "OpenAIChatProvider",
    "AgentResult",
    "AgentStrategy",
    "ReActAgent",
    "ReActConfig",
    "create_agent_strategy",
    "HiAgent",
    "HiAgentConfig",
]
