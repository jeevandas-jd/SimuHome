from __future__ import annotations

from typing import Any, Dict


def wrap_temporal_conflict_payload(
    *, feasible_payload: Dict[str, Any], conflict_data: Dict[str, Any]
) -> Dict[str, Any]:
    
    return {
        "meta": dict(feasible_payload.get("meta", {})),
        "query": feasible_payload.get("query", ""),
        "user_location": feasible_payload.get("user_location"),
        "temporal_conflict": dict(conflict_data or {}),
        "eval": {
            "required_actions": [],
            "goals": list(feasible_payload.get("eval", {}).get("goals", [])),
        },
        "initial_home_config": feasible_payload.get("initial_home_config"),
    }


__all__ = ["wrap_temporal_conflict_payload"]


