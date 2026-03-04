from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Sequence

from src.agents.types import ChatMessage


def _normalize_messages(messages: Sequence[ChatMessage]) -> List[Dict[str, str]]:
    """Convert internal ChatMessage objects into OpenAI-compatible dicts."""
    normalized: List[Dict[str, str]] = []
    for msg in messages:
        role = msg.role
        content = msg.content

        if role == "tool":
            role = "user"
        elif role not in ("system", "user", "assistant"):
            role = "user"
            content = f"Observation: {content}"

        normalized.append({"role": role, "content": content})
    return normalized


class LLMProvider(ABC):
    """Abstract provider interface."""

    @abstractmethod
    def generate(
        self,
        messages: Sequence[ChatMessage],
        response_format: Optional[Dict[str, Any]] = None,
    ) -> str:
        """Execute a chat completion request."""


class NonRetryableLLMError(RuntimeError):
    pass


class LLMRetryExhaustedError(NonRetryableLLMError):
    """Raised when the provider exhausts all retry attempts."""


class EmptyLLMResponseError(NonRetryableLLMError):
    """Raised when the LLM returns an empty content payload."""


__all__ = [
    "LLMProvider",
    "NonRetryableLLMError",
    "LLMRetryExhaustedError",
    "EmptyLLMResponseError",
    "_normalize_messages",
]
