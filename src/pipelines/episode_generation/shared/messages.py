from __future__ import annotations


class Message:
    def __init__(self, role: str, content: str):
        self.role = role
        self.content = content


__all__ = ["Message"]
