from __future__ import annotations

import re
from typing import List


def parse_integer_spec(spec: str) -> List[int]:
    spec_clean = re.sub(r"\s+", "", spec or "")
    tokens = [t for t in spec_clean.split(",") if t]
    out: List[int] = []
    seen = set()
    for tok in tokens:
        if "-" in tok:
            a, b = tok.split("-", 1)
            start, end = int(a), int(b)
            if start > end:
                start, end = end, start
            for s in range(start, end + 1):
                if s not in seen:
                    out.append(s)
                    seen.add(s)
        else:
            s = int(tok)
            if s not in seen:
                out.append(s)
                seen.add(s)
    return out


__all__ = ["parse_integer_spec"]
