from __future__ import annotations

from typing import Any, Dict

from src.pipelines.episode_generation.shared.conflicts import (
    wrap_temporal_conflict_payload,
)


def build_infeasible_conflict_payload(
    *,
    feasible_payload: Dict[str, Any],
    conflict_data: Dict[str, Any],
    keep_only_first_goal: bool = False,
) -> Dict[str, Any]:
    payload = wrap_temporal_conflict_payload(
        feasible_payload=feasible_payload,
        conflict_data=conflict_data,
    )

    payload_meta = payload.get("meta")
    if not isinstance(payload_meta, dict):
        raise ValueError("conflict payload meta must be a dict")
    payload_meta["case"] = "infeasible"
    payload_meta["conflict_type"] = conflict_data["type"]

    if keep_only_first_goal:
        goals = payload.get("eval", {}).get("goals") or []
        if goals:
            payload["eval"]["goals"] = [goals[0]]
    return payload


__all__ = ["build_infeasible_conflict_payload"]
