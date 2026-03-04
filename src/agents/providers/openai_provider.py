from __future__ import annotations

import os
import time
import importlib
from typing import Any, Dict, Optional, Sequence


_openai_module = importlib.import_module("openai")
APIStatusError = _openai_module.APIStatusError
OpenAI = _openai_module.OpenAI

from src.agents.providers.base import (
    EmptyLLMResponseError,
    LLMProvider,
    LLMRetryExhaustedError,
    NonRetryableLLMError,
    _normalize_messages,
)
from src.agents.types import ChatMessage


def _env_bool(name: str, default: bool) -> bool:
    raw = os.getenv(name)
    if raw is None:
        return default
    return raw.strip().lower() not in {"", "0", "false", "no", "off"}


def _extract_error_message(exc: BaseException) -> str:
    pieces: list[str] = []

    raw = str(exc).strip()
    if raw:
        pieces.append(raw)

    body = getattr(exc, "body", None)
    if isinstance(body, dict):
        nested = body.get("error")
        if isinstance(nested, dict):
            nested_message = nested.get("message")
            if isinstance(nested_message, str) and nested_message.strip():
                pieces.append(nested_message.strip())
        top_message = body.get("message")
        if isinstance(top_message, str) and top_message.strip():
            pieces.append(top_message.strip())
    elif isinstance(body, str) and body.strip():
        pieces.append(body.strip())

    deduped: list[str] = []
    for piece in pieces:
        if piece not in deduped:
            deduped.append(piece)

    return " | ".join(deduped)


def _is_context_overflow_error(message: str) -> bool:
    text = message.lower()
    markers = (
        "maximum context length",
        "reduce the length of the input messages",
        "parameter=input_tokens",
        "input_tokens",
    )
    return any(marker in text for marker in markers)


class OpenAIChatProvider(LLMProvider):
    """
    Unified OpenAI-compatible provider.
    Requires explicit API base/key values from caller-side resolution.
    """

    def __init__(
        self,
        *,
        model: str,
        temperature: float = 1.0,
        seed: int = 42,
        api_key: str,
        api_base: str,
        timeout: Optional[float] = None,
        max_retries: int = 10,
    ):
        self.model = model
        self.temperature = temperature
        self.seed = seed
        self.max_retries = max_retries

        resolved_base = api_base.strip()
        resolved_key = api_key.strip()
        if not resolved_base:
            raise ValueError("api_base must be provided explicitly")
        if not resolved_key:
            raise ValueError("api_key must be provided explicitly")

        self._is_openrouter = "openrouter.ai" in (resolved_base or "").lower()
        self._openrouter_require_parameters = _env_bool(
            "OPENROUTER_REQUIRE_PARAMETERS", False
        )
        self._openrouter_response_healing = _env_bool(
            "OPENROUTER_ENABLE_RESPONSE_HEALING", True
        )

        self._client = OpenAI(
            api_key=resolved_key,
            base_url=resolved_base,
            timeout=timeout,
        )

    def generate(
        self,
        messages: Sequence[ChatMessage],
        response_format: Optional[Dict[str, Any]] = None,
    ) -> str:
        oa_msgs = _normalize_messages(messages)
        kwargs: Dict[str, Any] = {
            "model": self.model,
            "temperature": self.temperature,
            "seed": self.seed,
            "messages": oa_msgs,
        }
        if response_format:
            kwargs["response_format"] = response_format

        if self._is_openrouter:
            extra_body: Dict[str, Any] = {}
            if self._openrouter_require_parameters:
                extra_body["provider"] = {"require_parameters": True}
            if self._openrouter_response_healing:
                extra_body["plugins"] = [{"id": "response-healing"}]
            if extra_body:
                kwargs["extra_body"] = extra_body

        last_error: BaseException | None = None
        retries = 0
        max_attempts = self.max_retries + 1

        while retries < max_attempts:
            try:
                resp = self._client.chat.completions.create(**kwargs)
                content = resp.choices[0].message.content
                if not content:
                    raise EmptyLLMResponseError("LLM response content was empty")
                return content
            except EmptyLLMResponseError as e:
                raise
            except APIStatusError as e:
                last_error = e
                message = _extract_error_message(e)
                status_code = getattr(e, "status_code", None)
                if (
                    isinstance(status_code, int)
                    and 400 <= status_code < 500
                    and status_code not in (408, 429)
                ):
                    if _is_context_overflow_error(message):
                        raise NonRetryableLLMError(
                            f"LLM context window exceeded: {message}"
                        ) from e
                    raise NonRetryableLLMError(
                        f"LLM request rejected with HTTP {status_code}: {message}"
                    ) from e

                retries += 1
                if retries >= max_attempts:
                    break

                time.sleep(min(5 * retries, 30))
            except Exception as e:
                last_error = e
                message = _extract_error_message(e)
                if _is_context_overflow_error(message):
                    raise NonRetryableLLMError(
                        f"LLM context window exceeded: {message}"
                    ) from e

                retries += 1
                if retries >= max_attempts:
                    break

                time.sleep(min(5 * retries, 30))

        if last_error is None:
            raise LLMRetryExhaustedError("LLM request failed with no response")

        raise LLMRetryExhaustedError(
            f"LLM request exhausted {max_attempts} attempts: {_extract_error_message(last_error)}"
        ) from last_error


__all__ = ["OpenAIChatProvider"]
