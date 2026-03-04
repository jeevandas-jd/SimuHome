from __future__ import annotations

from contextvars import ContextVar
from threading import Lock
from typing import Dict, Any, Callable, Optional
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os
from pathlib import Path
from dataclasses import dataclass
from src.simulator.api.responses import HTTPStatus, ResponseBuilder
from src.simulator.domain.result import Result, ErrorCode
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from dotenv import load_dotenv
from src.clients.smarthome_client import SmartHomeClient, resolve_simulator_base_url

root_dir = Path(__file__).parent.parent  # .../src
project_root = root_dir.parent  # repo root
load_dotenv()


def load_docs():
    docs_path = project_root / "docs" / "clusters"
    docs = []
    if docs_path.exists():
        for md_file in docs_path.glob("*.md"):
            try:
                with open(md_file, "r", encoding="utf-8") as f:
                    content = f.read()
                content = content.encode("ascii", errors="ignore").decode("ascii")
                doc = Document(
                    page_content=content,
                    metadata={"source": str(md_file), "filename": md_file.name},
                )
                docs.append(doc)
            except Exception as e:
                raise ValueError(f"Failed to load {md_file}: {e}")
        return docs
    else:
        raise ValueError("Docs directory does not exist")


def load_faiss():
    index_path = project_root / "data" / "vector_db" / "matter_index"
    faiss_file = index_path / "index.faiss"
    pkl_file = index_path / "index.pkl"

    if faiss_file.exists() and pkl_file.exists():
        embeddings = OpenAIEmbeddings()
        db = FAISS.load_local(
            str(index_path), embeddings, allow_dangerous_deserialization=True
        )
        return db
    else:
        docs = load_docs()

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000, chunk_overlap=200
        )
        split_docs = text_splitter.split_documents(docs)
        embeddings = OpenAIEmbeddings()
        db = FAISS.from_documents(split_docs, embeddings)
        index_path.mkdir(parents=True, exist_ok=True)
        db.save_local(str(index_path))
        return db


@dataclass
class ToolConfig:
    """setup for tools"""

    base_url: str = resolve_simulator_base_url()
    timeout: int = 10
    db: Optional[FAISS] = None


_DEFAULT_TOOL_CONFIG = ToolConfig(
    base_url=resolve_simulator_base_url(),
    timeout=int(os.getenv("SIMULATOR_API_TIMEOUT", "10")),
    db=None,
)
_tool_config_var: ContextVar[ToolConfig] = ContextVar(
    "tool_config", default=_DEFAULT_TOOL_CONFIG
)
_shared_db_lock = Lock()
_shared_db: Optional[FAISS] = None


def get_tool_config() -> ToolConfig:
    return _tool_config_var.get()


def set_tool_config(config: ToolConfig) -> None:
    _tool_config_var.set(config)


def _load_shared_db() -> FAISS:
    global _shared_db
    if _shared_db is not None:
        return _shared_db

    with _shared_db_lock:
        if _shared_db is None:
            _shared_db = load_faiss()
        assert _shared_db is not None
        return _shared_db


def _make_request(
    method: str, path: str, json_body: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    config = get_tool_config()
    url = f"{config.base_url}{path}"

    try:
        client = SmartHomeClient(
            base_url=config.base_url, timeout=float(config.timeout)
        )
        method_upper = method.upper()
        if method_upper == "GET":
            return client.get(path, params=json_body or {})
        elif method_upper == "POST":
            return client.post(path, json=json_body or {})
        elif method_upper == "DELETE":
            return client.delete(path)
        else:
            raise ValueError(f"Unsupported HTTP method: {method}")

    except Exception as e:
        try:
            import requests as _req
        except Exception:
            _req = None

        if _req is not None and isinstance(e, _req.exceptions.Timeout):
            return ResponseBuilder.from_result(
                Result.fail(
                    ErrorCode.TIMEOUT_ERROR,
                    "Request Timeout",
                    f"Request to {url} timed out after {config.timeout}s",
                )
            )
        if _req is not None and isinstance(e, _req.exceptions.ConnectionError):
            return ResponseBuilder.from_result(
                Result.fail(
                    ErrorCode.CONNECTION_ERROR,
                    "Connection Error",
                    f"Cannot connect to {url}",
                )
            )
        if _req is not None and isinstance(e, _req.exceptions.HTTPError):
            status_code = (
                e.response.status_code
                if getattr(e, "response", None) is not None
                else int(HTTPStatus.BAD_REQUEST)
            )
            return ResponseBuilder.from_result(
                Result.fail(
                    ErrorCode.HTTP_ERROR,
                    "HTTP Error",
                    f"{status_code}: {str(e)}",
                )
            )
        return ResponseBuilder.from_result(
            Result.fail(
                ErrorCode.INTERNAL_ERROR,
                "Unknown Error",
                str(e),
            )
        )


def tool_add_device(args: Dict[str, Any]) -> Dict[str, Any]:
    """
    Add a new device to a room.

    Args:
      room_id (str): Target room id (e.g., "living_room") [required]
      device_type (str): Device type identifier (e.g., "light", "ac") [required]
      device_id (str): New device id (e.g., "living_room_on_off_light_1") [required]

    Returns:
      {"status": {"code": int, "message": str}, "data": {"room_id": str, "device_id": str}, "error": {"type": str, "detail": str}}
    """
    return _make_request("POST", "/devices/add", args)


def tool_remove_device(args: Dict[str, Any]) -> Dict[str, Any]:
    """
    Remove a device.

    Args:
      device_id (str): Target device id (e.g., "living_room_on_off_light_1") [required]

    Returns:
      {"status": {"code": int, "message": str}, "data": {...}, "error": {"type": "...", "detail": "..."}}
    """
    device_id = args["device_id"]
    return _make_request("DELETE", f"/devices/{device_id}")


def tool_set_tick_interval(args: Dict[str, Any]) -> Dict[str, Any]:
    """
    Set simulation tick interval in seconds.

    Args:
      tick_interval (float): Seconds between simulator ticks (e.g., 0.5, 1, 2) [required]

    Returns:
      {"status": {"code": int, "message": str}, "data": {...}, "error": {"type": "...", "detail": "..."}}
    """
    return _make_request("POST", "/simulation/tick_interval", args)


def tool_execute_command(args: Dict[str, Any]) -> Dict[str, Any]:
    """
    Execute a command on a device (e.g., turn on light, set level, set setpoint).

    Args:
      device_id (str): Target device id (e.g., "living_room_on_off_light_1") [required]
      endpoint_id (int): Endpoint id (e.g., 1) [required]
      cluster_id (str): Cluster id (e.g., "OnOff", "LevelControl", "Thermostat") [required]
      command_id (str): Command id (e.g., "On", "Off", "MoveToLevel", "SetCoolingSetpoint") [required]
      args (dict): Command arguments. Use {} if no arguments are needed. [required]

    Returns:
      {"status": {"code": int, "message": str}, "data": {...}, "error": {"type": str, "detail": str}}
    """
    device_id = args.pop("device_id")
    return _make_request("POST", f"/devices/{device_id}/commands", args)


def tool_write_attribute(args: Dict[str, Any]) -> Dict[str, Any]:
    """
    Directly set a device attribute value.

    Args:
      device_id (str): Target device id (e.g., "living_room_on_off_light_1") [required]
      endpoint_id (int): Endpoint id (e.g., 1) [required]
      cluster_id (str): Cluster id (e.g., "OnOff", "LevelControl", "Thermostat") [required]
      attribute_id (str): Attribute id (e.g., "OnOff", "CurrentLevel", "LocalTemperature") [required]
      value (any): Value to set (e.g., true, 100, 2400) [required]

    Returns:
      {"status": {"code": int, "message": str}, "data": {...}, "error": {"type": "...", "detail": "..."}}
    """
    device_id = args.pop("device_id")
    return _make_request("POST", f"/devices/{device_id}/attributes/write", args)


def tool_get_device_structure(args: Dict[str, Any]) -> Dict[str, Any]:
    """
    Get device structure (endpoints, clusters, attributes, and commands).

    Args:
      device_id (str): Target device id (e.g., "living_room_on_off_light_1") [required]

    Returns:
      {"status": {"code": int, "message": str}, "data": {...}, "error": {"type": str, "detail": str}}
    """
    device_id = args["device_id"]
    return _make_request("GET", f"/devices/{device_id}/structure")


def tool_get_all_attributes(args: Dict[str, Any]) -> Dict[str, Any]:
    """
    Get all attributes of a device.

    Args:
      device_id (str): Target device id (e.g., "living_room_on_off_light_1") [required]

    Returns:
      {"status": {"code": int, "message": str}, "data": {...}, "error": {"type": str, "detail": str}}
    """
    device_id = args["device_id"]
    return _make_request("GET", f"/devices/{device_id}/attributes")


def tool_get_attribute(args: Dict[str, Any]) -> Dict[str, Any]:
    """
    Get a specific attribute of a device.

    Args:
      device_id (str): Target device id (e.g., "living_room_on_off_light_1") [required]
      endpoint_id (int): Endpoint id [required]
      cluster_id (str): Cluster id (e.g., "OnOff", "LevelControl", "Thermostat") [required]
      attribute_id (str): Attribute id (e.g., "OnOff", "CurrentLevel", "LocalTemperature") [required]

    Returns:
      {"status": {"code": int, "message": str}, "data": {...}, "error": {"type": str, "detail": str}}
    """
    return _make_request(
        "GET",
        f"/devices/{args['device_id']}/attributes/{args['endpoint_id']}/{args['cluster_id']}/{args['attribute_id']}",
    )


def tool_get_room_devices(args: Dict[str, Any]) -> Dict[str, Any]:
    """
    Get all devices in a room.

    Args:
      room_id (str): Room id (e.g., "living_room") [required]

    Returns:
      {"status": {"code": int, "message": str}, "data": {"devices": [...]}, "error": {"type": "...", "detail": "..."}}
    """
    return _make_request("GET", f"/rooms/{args['room_id']}/devices")


def tool_get_room_states(args: Dict[str, Any]) -> Dict[str, Any]:
    """
    Get environmental states of a room (temperature, humidity, illuminance, PM10).

    Args:
      room_id (str): Room id (e.g., "living_room") [required]

    Returns:
      {"status": {"code": int, "message": str}, "data": {"temperature": int, "humidity": int, "illuminance": int, "pm10": int}, "error": {"type": "...", "detail": "..."}}
    """
    return _make_request("GET", f"/rooms/{args['room_id']}/states")


def tool_get_cluster_doc(args: Dict[str, Any]) -> Dict[str, Any]:
    """
    Perform semantic search across Matter cluster documentation (covering specifications for clusters, commands, and attributes)

    Args:
      query (str): Search query (e.g., "Explain the OperationalState attribute.") [required]
      top_k (int): Number of top relevant documentation chunks to return [required]

    Returns:
      {"status": {"code": int, "message": str}, "data": {"text": str}, "error": {"type": str, "detail": str}}
    """
    try:
        config = get_tool_config()
        db = config.db or _load_shared_db()
        hits = db.similarity_search(args["query"], k=int(args["top_k"]))
        if not hits:
            return ResponseBuilder.from_result(Result.ok({"text": ""}))

        text = "\n\n".join(h.page_content for h in hits)
        return ResponseBuilder.from_result(Result.ok({"text": text}))
    except Exception as e:
        return ResponseBuilder.from_result(
            Result.fail(ErrorCode.INTERNAL_ERROR, "DocSearchError", str(e))
        )


def tool_get_home_state(args: Dict[str, Any]) -> Dict[str, Any]:
    """
    Get a full home snapshot in home_config format.

    Args:
      (none)

    Returns:
      {"status": {"code": int, "message": str}, "data": {...}, "error": {"type": str, "detail": str}}
    """
    return _make_request("GET", "/home/state")


def tool_schedule_workflow(args: Dict[str, Any]) -> Dict[str, Any]:
    """
    Schedule a sequential workflow of steps at a virtual absolute time. The scheduled time must be in the future relative to the current time.
    WARNING: A success response indicates that scheduling was successful, but it does not guarantee that all steps will execute successfully.

    Args:
      start_time (str): The scheduled execution time in the format "YYYY-MM-DD HH:MM:SS". [required]
      steps (list): An ordered list of workflow steps, e.g., [{"tool": "execute_command"|"write_attribute", "args": {...}}] [required]

    Returns:
      {"status": {"code": int, "message": str}, "data": {"workflow_id": "..."}, "error": {"type": "...", "detail": "..."}}
    """
    return _make_request("POST", "/schedule/workflow", args)


def tool_get_workflow_status(args: Dict[str, Any]) -> Dict[str, Any]:
    """
    Get workflow status by id.

    Args:
      workflow_id (str): Workflow identifier [required]

    Returns:
      {"status": {"code": int, "message": str}, "data": {"status": "pending|running|completed|failed|cancelled"}, "error": {"type": "...", "detail": "..."}}
    """
    return _make_request("GET", f"/schedule/workflow/{args['workflow_id']}/status")


def tool_cancel_workflow(args: Dict[str, Any]) -> Dict[str, Any]:
    """
    Cancel a scheduled workflow by id.

    Args:
      workflow_id (str): Workflow identifier [required]

    Returns:
      {"status": {"code": int, "message": str}, "data": {"workflow_id": str, "status": "cancelled"}, "error": {"type": "...", "detail": "..."}}
    """
    return _make_request("POST", f"/schedule/workflow/{args['workflow_id']}/cancel")


def tool_get_current_time(args: Dict[str, Any]) -> Dict[str, Any]:
    """
    Get current virtual time as human-friendly string "YYYY-MM-DD HH:MM:SS".

    Args:
      (none)

    Returns:
      {"status": {"code": int, "message": str}, "data": {"now": "YYYY-MM-DD HH:MM:SS"}, "error": {"type": "...", "detail": "..."}}
    """
    return _make_request("GET", "/time")


def tool_get_workflow_list(args: Dict[str, Any]) -> Dict[str, Any]:
    """
    Get list of workflows with optional filtering.

    Args:
      (none)

    Returns:
      {"status": {"code": int, "message": str}, "data": [...], "error": {"type": "...", "detail": "..."}}
    """
    return _make_request("GET", "/schedule/workflows", args)


def tool_finish(args: Dict[str, Any]) -> Dict[str, Any]:
    """
    Complete the task and return the final natural-language answer.

    Args:
      answer (str): Final response text [required]

    Returns:
      {"status": {"code": int, "message": str}, "data": {"answer": str}, "error": {"type": str, "detail": str}}
    """
    answer_text = str(args["answer"])
    return ResponseBuilder.from_result(Result.ok({"answer": answer_text}))


def tool_get_rooms(args: Dict[str, Any]) -> Dict[str, Any]:
    """
    Get all rooms in the home along with their display names.

    Args:
      (none)

    Returns:
      {"status": {"code": int, "message": str}, "data": {"rooms": [{"room_id": str, "display_name": str}, ...]}, "error": {"type": str, "detail": str}}
    """
    return _make_request("GET", "/rooms", args)


def tool_get_environment_control_rules(args: Dict[str, Any]) -> Dict[str, Any]:
    """
    Get control rules for a specific environmental state.

    Args:
      state (str): Environmental state (e.g., "temperature", "humidity", "air_quality", "illuminance") [required]

    Returns:
      {"status": {"code": int, "message": str}, "data": {"state": str, "control_rules": str}, "error": {"type": str, "detail": str}}
    """
    state = args["state"]
    return _make_request("GET", f"/environment/control_rules/{state}", args)


TOOL_REGISTRY: Dict[str, Callable[[Dict[str, Any]], Dict[str, Any]]] = {
    "add_device": tool_add_device,
    "remove_device": tool_remove_device,
    "set_tick_interval": tool_set_tick_interval,
    "finish": tool_finish,
    "execute_command": tool_execute_command,
    "write_attribute": tool_write_attribute,
    "get_all_attributes": tool_get_all_attributes,
    "get_attribute": tool_get_attribute,
    "get_device_structure": tool_get_device_structure,
    "get_home_state": tool_get_home_state,
    "get_rooms": tool_get_rooms,
    "get_room_devices": tool_get_room_devices,
    "get_room_states": tool_get_room_states,
    "get_cluster_doc": tool_get_cluster_doc,
    "schedule_workflow": tool_schedule_workflow,
    "get_workflow_status": tool_get_workflow_status,
    "cancel_workflow": tool_cancel_workflow,
    "get_current_time": tool_get_current_time,
    "get_workflow_list": tool_get_workflow_list,
    "get_environment_control_rules": tool_get_environment_control_rules,
}


def render_tool_markdown_table() -> str:
    """Render TOOL_REGISTRY entries as a Markdown table using tool docstrings.

    Columns: Tool | Description | Args | Returns
    """

    def _escape_pipes(text: str) -> str:
        return text.replace("|", "\\|")

    def _normalize_whitespace(text: str) -> str:
        return " ".join(text.split())

    def _join_lines(lines: list[str]) -> str:
        return "<br>".join(
            [_escape_pipes(_normalize_whitespace(l)) for l in lines if l.strip()]
        )

    header = "| Tool | Description | Args | Returns |\n|---|---|---|---|"
    rows: list[str] = []

    for name in sorted(TOOL_REGISTRY.keys()):
        fn = TOOL_REGISTRY[name]
        description = ""
        args_lines: list[str] = []
        returns_lines: list[str] = []

        if hasattr(fn, "__doc__") and fn.__doc__:
            doc = fn.__doc__.strip()
            doc_lines = [line.rstrip() for line in doc.split("\n")]
            for line in doc_lines:
                if line.strip():
                    description = line.strip()
                    break

            in_args = False
            in_returns = False
            for line in doc_lines:
                stripped = line.strip()
                if stripped.startswith("Args:"):
                    in_args = True
                    in_returns = False
                    continue
                if stripped.startswith("Returns:"):
                    in_args = False
                    in_returns = True
                    continue
                if stripped.startswith("Examples:"):
                    if in_args or in_returns:
                        break
                    continue
                if in_args:
                    args_lines.append(stripped)
                elif in_returns:
                    returns_lines.append(stripped)

        args_text = _join_lines(args_lines) if args_lines else ""
        returns_text = _join_lines(returns_lines) if returns_lines else ""
        if not description:
            description = "(no description)"

        rows.append(
            f"| {name} | {_escape_pipes(description)} | {args_text} | {returns_text} |"
        )
    content = "\n".join([header] + rows)
    return f"```markdown\n{content}\n```"


def render_tool_html_table() -> str:
    """Render TOOL_REGISTRY entries as an HTML table using tool docstrings.

    Columns: Tool | Description | Args | Returns
    """

    def _escape_html(text: str) -> str:
        return (
            text.replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace('"', "&quot;")
            .replace("'", "&#39;")
        )

    def _normalize_whitespace(text: str) -> str:
        return " ".join(text.split())

    def _join_lines(lines: list[str]) -> str:
        safe_lines = [
            _escape_html(_normalize_whitespace(l)) for l in lines if l.strip()
        ]
        return "<br/>".join(safe_lines)

    parts: list[str] = []
    parts.append("<table>")
    parts.append("  <thead>")
    parts.append(
        "    <tr><th>Tool</th><th>Description</th><th>Args</th><th>Returns</th></tr>"
    )
    parts.append("  </thead>")
    parts.append("  <tbody>")

    for name in sorted(TOOL_REGISTRY.keys()):
        fn = TOOL_REGISTRY[name]
        description = ""
        args_lines: list[str] = []
        returns_lines: list[str] = []

        if hasattr(fn, "__doc__") and fn.__doc__:
            doc = fn.__doc__.strip()
            doc_lines = [line.rstrip() for line in doc.split("\n")]
            # Description: first non-empty line
            for line in doc_lines:
                if line.strip():
                    description = line.strip()
                    break

            # Sections
            in_args = False
            in_returns = False
            for line in doc_lines:
                stripped = line.strip()
                if stripped.startswith("Args:"):
                    in_args = True
                    in_returns = False
                    continue
                if stripped.startswith("Returns:"):
                    in_args = False
                    in_returns = True
                    continue
                if stripped.startswith("Examples:"):
                    if in_args or in_returns:
                        break
                    continue
                if in_args:
                    args_lines.append(stripped)
                elif in_returns:
                    returns_lines.append(stripped)

        tool_cell = _escape_html(name)
        desc_cell = _escape_html(description) if description else "(no description)"
        args_cell = _join_lines(args_lines) if args_lines else ""
        returns_cell = _join_lines(returns_lines) if returns_lines else ""

        parts.append(
            f"    <tr><td>{tool_cell}</td><td>{desc_cell}</td><td>{args_cell}</td><td>{returns_cell}</td></tr>"
        )

    parts.append("  </tbody>")
    parts.append("</table>")

    html = "\n".join(parts)
    return f"```html\n{html}\n```"


def render_tool_docstrings_json() -> str:
    """Render tools as JSON: {tool_name: docstring} wrapped in ```json``` block."""
    import json

    tools_dict = {}
    for name in sorted(TOOL_REGISTRY.keys()):
        fn = TOOL_REGISTRY[name]
        doc = (fn.__doc__ or "").strip()
        if not doc:
            doc = "(no docstring)"
        tools_dict[name] = doc

    json_str = json.dumps(tools_dict, indent=2, ensure_ascii=False)
    return f"```json\n{json_str}\n```"


def run_tool(name: str, args: Dict[str, Any]) -> Dict[str, Any]:
    REQUIRED_ARGS = {
        "add_device": ["room_id", "device_type", "device_id"],
        "remove_device": ["device_id"],
        "set_tick_interval": ["tick_interval"],
        "execute_command": [
            "device_id",
            "endpoint_id",
            "cluster_id",
            "command_id",
            "args",
        ],
        "write_attribute": [
            "device_id",
            "endpoint_id",
            "cluster_id",
            "attribute_id",
            "value",
        ],
        "get_all_attributes": ["device_id"],
        "get_attribute": ["device_id", "endpoint_id", "cluster_id", "attribute_id"],
        "get_home_state": [],
        "get_rooms": [],
        "get_room_devices": ["room_id"],
        "get_room_states": ["room_id"],
        "get_cluster_doc": ["query", "top_k"],
        "finish": ["answer"],
        "schedule_workflow": ["start_time", "steps"],
        "get_workflow_status": ["workflow_id"],
        "cancel_workflow": ["workflow_id"],
        "get_current_time": [],
        "get_workflow_list": [],
        "get_environment_control_rules": ["state"],
    }

    missing = [k for k in REQUIRED_ARGS.get(name, []) if k not in (args or {})]
    if missing:
        return {
            "status": {"code": 400, "message": "VALIDATION_ERROR"},
            "data": None,
            "error": {
                "type": "MISSING_PARAMETERS",
                "detail": f"Missing required arguments: {', '.join(missing)}",
            },
        }

    allowed_params = REQUIRED_ARGS.get(name, set())
    if allowed_params:
        extra_params = [k for k in (args or {}) if k not in allowed_params]
        if extra_params:
            return {
                "status": {"code": 400, "message": "VALIDATION_ERROR"},
                "data": None,
                "error": {
                    "type": "INVALID_PARAMETERS",
                    "detail": f"Invalid parameters: {', '.join(extra_params)}. Allowed: {', '.join(sorted(allowed_params))}",
                },
            }

    fn = TOOL_REGISTRY[name]
    return fn(args)
