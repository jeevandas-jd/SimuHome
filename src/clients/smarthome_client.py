from __future__ import annotations

from typing import Any, Dict, Optional, List

import os
import requests

SIM_BASE_ENV_VAR = "SIMULATOR_API_BASE_URL"
DEFAULT_SIM_BASE_URL = "http://127.0.0.1:8000/api"


def resolve_simulator_base_url(base_url: Optional[str] = None) -> str:
    """Resolve simulator API base URL with environment fallback."""
    resolved = base_url or os.getenv(SIM_BASE_ENV_VAR) or DEFAULT_SIM_BASE_URL
    return resolved[:-1] if resolved.endswith("/") else resolved


class SmartHomeClient:
    def __init__(self, base_url: Optional[str] = None, timeout: float = 10.0):
        resolved_base = resolve_simulator_base_url(base_url)
        self.base_url = resolved_base
        self.timeout = timeout

    def health(self) -> Optional[Dict[str, Any]]:
        try:
            r = requests.get(f"{self.base_url}/__health__", timeout=self.timeout)
            r.raise_for_status()
            return r.json()
        except Exception:
            return None

    def reset_simulation(self, cfg: Dict[str, Any]) -> Dict[str, Any]:
        r = requests.post(
            f"{self.base_url}/simulation/reset", json=cfg, timeout=self.timeout
        )
        r.raise_for_status()
        return r.json()

    def execute_command(
        self,
        device_id: str,
        endpoint_id: int,
        cluster_id: str,
        command_id: str,
        args: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        payload = {
            "endpoint_id": endpoint_id,
            "cluster_id": cluster_id,
            "command_id": command_id,
            "args": args or {},
        }
        r = requests.post(
            f"{self.base_url}/devices/{device_id}/commands",
            json=payload,
            timeout=self.timeout,
        )
        r.raise_for_status()
        return r.json()

    def write_attribute(
        self,
        device_id: str,
        endpoint_id: int,
        cluster_id: str,
        attribute_id: str,
        value: Any,
    ) -> Dict[str, Any]:
        payload = {
            "endpoint_id": endpoint_id,
            "cluster_id": cluster_id,
            "attribute_id": attribute_id,
            "value": value,
        }
        r = requests.post(
            f"{self.base_url}/devices/{device_id}/attributes/write",
            json=payload,
            timeout=self.timeout,
        )
        r.raise_for_status()
        return r.json()

    def get_home_state(self) -> Dict[str, Any]:
        r = requests.get(f"{self.base_url}/home/state", timeout=self.timeout)
        r.raise_for_status()
        return r.json()

    def get_rooms(self) -> Dict[str, Any]:
        r = requests.get(f"{self.base_url}/rooms", timeout=self.timeout)
        r.raise_for_status()
        return r.json()

    def get_room_states(self, room_id: str) -> Dict[str, Any]:
        r = requests.get(
            f"{self.base_url}/rooms/{room_id}/states", timeout=self.timeout
        )
        r.raise_for_status()
        return r.json()

    def get_device_attributes(self, device_id: str) -> Dict[str, Any]:
        r = requests.get(
            f"{self.base_url}/devices/{device_id}/attributes", timeout=self.timeout
        )
        r.raise_for_status()
        return r.json().get("data", {})

    def get_structure(self, device_id: str) -> Dict[str, Any]:
        r = requests.get(
            f"{self.base_url}/devices/{device_id}/structure", timeout=self.timeout
        )
        r.raise_for_status()
        return r.json().get("data", {})

    def get_room_devices(self, room_id: str) -> Dict[str, Any]:
        r = requests.get(
            f"{self.base_url}/rooms/{room_id}/devices", timeout=self.timeout
        )
        r.raise_for_status()
        return r.json()

    def fast_forward_to(
        self, to_tick: int, room_ids: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        payload = {"to_tick": int(to_tick)}
        if room_ids is not None:
            payload["room_ids"] = room_ids
        r = requests.post(
            f"{self.base_url}/simulation/fast_forward_to",
            json=payload,
            timeout=self.timeout,
        )
        r.raise_for_status()
        return r.json()

    def get_environment_control_rules(self, state: str) -> Dict[str, Any]:
        """Get control rules for a specific environmental state."""
        r = requests.get(
            f"{self.base_url}/environment/control_rules/{state}", timeout=self.timeout
        )
        r.raise_for_status()
        return r.json()

    # ---- Generic helpers ----
    def get(self, path: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        if not path.startswith("/"):
            path = "/" + path
        r = requests.get(
            f"{self.base_url}{path}", params=params or {}, timeout=self.timeout
        )
        r.raise_for_status()
        return r.json()

    def post(self, path: str, json: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        if not path.startswith("/"):
            path = "/" + path
        r = requests.post(
            f"{self.base_url}{path}", json=json or {}, timeout=self.timeout
        )
        r.raise_for_status()
        return r.json()

    def delete(self, path: str) -> Dict[str, Any]:
        if not path.startswith("/"):
            path = "/" + path
        r = requests.delete(f"{self.base_url}{path}", timeout=self.timeout)
        r.raise_for_status()
        return r.json()

    def schedule_workflow(
        self,
        start_time: str,
        steps: List[Dict[str, Any]],
    ) -> Dict[str, Any]:
        """Schedule a sequential workflow of steps at a virtual absolute time."""
        payload = {
            "start_time": start_time,
            "steps": steps,
        }
        r = requests.post(
            f"{self.base_url}/schedule/workflow", json=payload, timeout=self.timeout
        )
        r.raise_for_status()
        return r.json()

    def get_workflow_status(self, workflow_id: str) -> Dict[str, Any]:
        """Get workflow status by id."""
        r = requests.get(
            f"{self.base_url}/schedule/workflow/{workflow_id}/status",
            timeout=self.timeout,
        )
        r.raise_for_status()
        return r.json()

    def get_current_time(self) -> Dict[str, Any]:
        """Get current virtual time."""
        r = requests.get(f"{self.base_url}/time", timeout=self.timeout)
        r.raise_for_status()
        return r.json()

    # ---- Batch: run workflow now ----
    def run_workflow_now(
        self,
        steps: List[Dict[str, Any]],
        *,
        continue_on_error: bool = True,
        record: bool = False,
        tag: Optional[str] = None,
    ) -> Dict[str, Any]:
        payload: Dict[str, Any] = {
            "steps": steps,
            "continue_on_error": bool(continue_on_error),
            "record": bool(record),
        }
        if tag is not None:
            payload["tag"] = tag
        return self.post("/workflow/run_now", json=payload)


__all__ = ["SmartHomeClient", "resolve_simulator_base_url", "DEFAULT_SIM_BASE_URL"]
