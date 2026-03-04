from __future__ import annotations

from typing import Any, Dict, List, Optional

from src.pipelines.episode_generation.shared.goals import count_rooms_and_devices


def assemble_payload(
    *,
    seed: int,
    query_type: str,
    case: str,
    snapshot: Dict[str, Any],
    user_location: str,
    required_actions: List[Dict[str, Any]],
    goals: List[Dict[str, Any]],
    meta_extras: Optional[Dict[str, Any]] = None,
    query: str = "",
) -> Dict[str, Any]:
    num_rooms, num_devices = count_rooms_and_devices(snapshot)
    meta = {
        "seed": seed,
        "query_type": query_type,
        "case": case,
        "num_rooms": num_rooms,
        "num_devices": num_devices,
    }
    if meta_extras:
        meta.update(meta_extras)

    return {
        "meta": meta,
        "query": query,
        "user_location": user_location,
        "eval": {
            "required_actions": required_actions,
            "goals": goals,
        },
        "initial_home_config": snapshot,
    }


__all__ = ["assemble_payload"]
