from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class ChatMessage:
    """Unified chat message model shared by providers and agent strategies."""

    role: str
    content: str


__all__ = ["ChatMessage"]

