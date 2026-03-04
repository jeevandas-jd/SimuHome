from __future__ import annotations

from hashlib import blake2b
from typing import Any, Optional


def ensure_seed(seed: Optional[int], *, context: str) -> int:
    if seed is None:
        raise ValueError(f"{context} requires an integer seed")
    return int(seed)


def derive_subseed(seed: int, *parts: Any) -> int:
    material = "|".join([str(seed), *[str(part) for part in parts]])
    digest = blake2b(material.encode("utf-8"), digest_size=8).digest()
    return int.from_bytes(digest, "big") % (2**31 - 1)


__all__ = ["ensure_seed", "derive_subseed"]
