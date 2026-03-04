from __future__ import annotations

from typing import Any, Dict, List, Optional
import time

from src.clients.smarthome_client import SmartHomeClient
from src.pipelines.episode_generation.core.candidate_sampler import sample_candidate


def _call_api(
    client: SmartHomeClient, device_id: str, api: Dict[str, Any]
) -> Dict[str, Any]:
    api_type = api.get("api_type")
    endpoint_id = int(api.get("endpoint_id", 1))
    cluster_id = api.get("cluster_id")

    if api_type == "execute_command":
        return client.execute_command(
            device_id=device_id,
            endpoint_id=endpoint_id,
            cluster_id=cluster_id,
            command_id=api.get("command_id"),
            args=api.get("args") or {},
        )
    elif api_type == "write_attribute":
        return client.write_attribute(
            device_id=device_id,
            endpoint_id=endpoint_id,
            cluster_id=cluster_id,
            attribute_id=api.get("attribute_id"),
            value=api.get("value"),
        )
    else:
        return {
            "status": {"code": 400, "message": "INVALID_API"},
            "error": {"type": "VALIDATION_ERROR", "detail": "Unsupported api_type"},
        }


def _is_success(resp: Dict[str, Any]) -> bool:
    try:
        return int(resp.get("status", {}).get("code", 0)) == 200
    except Exception:
        return False


def _get_error_type(resp: Dict[str, Any]) -> Optional[str]:
    try:
        err = resp.get("error") or {}
        return err.get("type")
    except Exception:
        return None


def execute_device_step(
    *,
    client: SmartHomeClient,
    device_id: str,
    device_type: str,
    seed: Optional[int] = None,
) -> Dict[str, Any]:
    state_flat = client.get_device_attributes(device_id)

    if state_flat is None:
        return {
            "status": "skipped",
            "executed": [],
            "response": None,
            "candidate": None,
            "error": "Failed to get device state",
        }

    candidate = sample_candidate(
        device_type=device_type,
        device_id=device_id,
        state_flat=state_flat,
        seed=seed,
    )
    if not candidate:
        return {
            "status": "skipped",
            "executed": [],
            "response": None,
            "candidate": None,
        }

    executed: List[Dict[str, Any]] = []

    api = candidate.get("api", {})
    resp = _call_api(client, device_id, api)
    executed.append({"api": api, "resp": resp})
    if not _is_success(resp):
        err_type = _get_error_type(resp)
        return {
            "status": "skipped",
            "executed": executed,
            "response": resp,
            "candidate": candidate,
            "error_type": err_type,
        }

    return {
        "status": "ok",
        "executed": executed,
        "response": resp,
        "candidate": candidate,
    }


__all__ = ["execute_device_step"]
