from __future__ import annotations

import os
from urllib.parse import urlparse


def resolve_secret_value(raw: object, key_name: str, required: bool) -> str | None:
    if raw is None:
        if required:
            raise ValueError(f"{key_name} is required")
        return None

    if not isinstance(raw, str):
        raise ValueError(f"{key_name} must be a string")

    if raw.startswith("env:"):
        env_name = raw[4:].strip()
        if not env_name:
            raise ValueError(f"{key_name} env reference is empty")
        env_value = os.getenv(env_name)
        if env_value is None or env_value == "":
            raise ValueError(f"{key_name} env '{env_name}' is empty or missing")
        return env_value

    if raw == "" and required:
        raise ValueError(f"{key_name} cannot be empty")

    return raw


def is_local_api_base(api_base: str) -> bool:
    parsed = urlparse(api_base)
    host = (parsed.hostname or "").strip().lower()
    return host in {"127.0.0.1", "localhost", "0.0.0.0", "::1"}


def resolve_api_key_for_base(raw: object, api_base: str, key_name: str) -> str:
    resolved = resolve_secret_value(raw, key_name, required=False)
    if isinstance(resolved, str) and resolved.strip():
        return resolved.strip()

    if is_local_api_base(api_base):
        return "dummy"

    raise ValueError(f"{key_name} is required for non-local api_base: {api_base}")


__all__ = [
    "resolve_secret_value",
    "is_local_api_base",
    "resolve_api_key_for_base",
]
