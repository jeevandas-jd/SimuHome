from __future__ import annotations

import argparse
import concurrent.futures as cf
import hashlib
import json
import multiprocessing as mp
import os
import queue
import re
import signal
import socket
import subprocess
import sys
import threading
import time
from datetime import datetime
from pathlib import Path
from typing import Any, TypedDict

import requests
import yaml
from dotenv import load_dotenv
from tqdm import tqdm

from src.cli.arg_utils import parse_integer_spec
from src.cli.config_resolver import (
    resolve_api_key_for_base,
    resolve_secret_value,
)
from src.cli.episode_evaluator import ProgressEvent, evaluate_episodes


MANIFEST_FILE = "manifest.json"
STATE_FILE = "run_state.json"
SUMMARY_FILE = "run_summary.json"
SPEC_SCHEMA_VERSION = "simuhome-eval-spec-v1"
SPEC_COPY_FILE = "evaluation_spec.yaml"

DEFAULT_STRATEGY_PRESETS: dict[str, dict[str, float | int]] = {
    "react": {"timeout": 60.0, "temperature": 0.0, "max_steps": 20},
    "hi_agent": {"timeout": 60.0, "temperature": 0.0, "max_steps": 50},
}

STRATEGY_ALIASES: dict[str, str] = {
    "react-agent": "react",
    "hiagent": "hi_agent",
    "hi-agent": "hi_agent",
}


def _normalize_strategy_name(raw_name: str) -> str:
    key = raw_name.strip().lower()
    return STRATEGY_ALIASES.get(key, key)


class StrategySettings(TypedDict):
    name: str
    timeout: float
    temperature: float
    max_steps: int


class OrchestrationSettings(TypedDict):
    max_workers: int | None
    simulator_start_timeout: int
    simulator_start_retries: int
    evaluation_retries: int
    allow_partial_start: bool


class EpisodeSelection(TypedDict):
    episode_dir: str
    qt: str | None
    case: str | None
    seed: str | None


class ModelConfig(TypedDict):
    model: str
    api_base: str
    api_key: str
    judge_model: str
    judge_api_base: str
    judge_api_key: str


class ModelRuntimeConfig(ModelConfig):
    port: int


class ResolvedRun(TypedDict):
    run_id: str
    output_root: str
    spec_path: str
    strategy: StrategySettings
    orchestration: OrchestrationSettings
    selection: EpisodeSelection
    models: list[ModelConfig]


class SimulatorInfo(TypedDict):
    model: str
    port: int
    process: subprocess.Popen[str]
    pid: int


class StartupResult(TypedDict):
    success: bool
    model_config: ModelRuntimeConfig
    attempts: int
    error: str


class EvaluationResult(TypedDict):
    original_model: str
    safe_model: str
    port: int
    success: bool
    returncode: int
    attempts: int
    phase: str
    error: str


_worker_progress_queue: Any = None
_worker_event_seq = 0
_worker_stdio_devnull: Any = None


def _init_eval_worker(progress_queue: Any) -> None:
    global _worker_progress_queue, _worker_event_seq, _worker_stdio_devnull
    _worker_progress_queue = progress_queue
    _worker_event_seq = 0
    _worker_stdio_devnull = open(os.devnull, "w", encoding="utf-8")
    sys.stdout = _worker_stdio_devnull
    sys.stderr = _worker_stdio_devnull


def _emit_worker_event(event: ProgressEvent) -> None:
    queue_ref = _worker_progress_queue
    if queue_ref is None:
        return

    global _worker_event_seq
    _worker_event_seq += 1
    payload = dict(event)
    payload.setdefault("seq", _worker_event_seq)
    payload.setdefault("ts", datetime.now().isoformat(timespec="seconds"))

    try:
        queue_ref.put_nowait(payload)
    except Exception:
        pass


class PortAllocator:
    def __init__(self) -> None:
        self._lock = threading.Lock()
        self._used_ports: set[int] = set()

    def allocate(self) -> int:
        with self._lock:
            for _ in range(200):
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                    sock.bind(("127.0.0.1", 0))
                    port = int(sock.getsockname()[1])
                if port in self._used_ports:
                    continue
                if self._is_port_available(port):
                    self._used_ports.add(port)
                    return port
            raise RuntimeError("unable to allocate a free local port")

    @staticmethod
    def _is_port_available(port: int) -> bool:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            return sock.connect_ex(("127.0.0.1", port)) != 0


class SimulatorManager:
    def __init__(self) -> None:
        self._lock = threading.Lock()
        self.processes: list[SimulatorInfo] = []

    def start_simulator(self, model: str, port: int) -> SimulatorInfo:
        env = os.environ.copy()
        env.update(
            {
                "LLM_MODEL": model,
                "EVAL_MODEL_NAME": model,
                "SERVER_PORT": str(port),
            }
        )

        process = subprocess.Popen(
            [sys.executable, "-m", "src.simulator.api.app"],
            env=env,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            text=True,
        )

        info: SimulatorInfo = {
            "model": model,
            "port": port,
            "process": process,
            "pid": int(process.pid),
        }
        with self._lock:
            self.processes.append(info)
        return info

    def terminate_process(self, process: subprocess.Popen[str]) -> None:
        if process.poll() is not None:
            return
        process.terminate()
        try:
            process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            process.kill()
            process.wait(timeout=5)

    def cleanup_all(self) -> None:
        with self._lock:
            processes = list(self.processes)
            self.processes.clear()
        if not processes:
            return
        for info in processes:
            process = info["process"]
            try:
                self.terminate_process(process)
            except Exception as exc:
                print(
                    f"[SimulatorManager] WARN: failed to terminate PID {info['pid']} for {info['model']}: {exc}"
                )


def get_safe_model_name(original_model: str) -> str:
    return original_model.replace("/", "_").replace(":", "_")


def _natural_sort_key(name: str) -> tuple[Any, ...]:
    parts = re.split(r"(\d+)", name)
    return tuple(int(part) if part.isdigit() else part for part in parts)


def _discover_target_episode_filenames(selection: EpisodeSelection) -> list[str]:
    episode_dir = Path(selection["episode_dir"])
    if not episode_dir.exists() or not episode_dir.is_dir():
        return []

    qt = selection["qt"]
    case = selection["case"]
    seed = selection["seed"]

    if qt and case and seed:
        try:
            seeds = parse_integer_spec(seed)
        except ValueError:
            return []

        filenames = [
            f"{qt}_{case}_seed_{seed_value}.json"
            for seed_value in seeds
            if (episode_dir / f"{qt}_{case}_seed_{seed_value}.json").exists()
        ]
        return sorted(filenames, key=_natural_sort_key)

    return sorted(
        (path.name for path in episode_dir.glob("*.json")), key=_natural_sort_key
    )


def _classify_episode_result(path: Path) -> str:
    try:
        payload = _json_read(path)
    except Exception:
        return "invalid"

    evaluation_result = payload.get("evaluation_result")
    if not isinstance(evaluation_result, dict):
        return "invalid"

    error_type = evaluation_result.get("error_type")
    if isinstance(error_type, str) and error_type.strip():
        return "runtime_error"

    score = evaluation_result.get("score")
    if isinstance(score, (int, float)) and float(score) < 0:
        return "runtime_error"

    if not isinstance(score, (int, float)):
        return "invalid"

    return "success"


def _collect_episode_progress_for_model(
    resolved: ResolvedRun, run_dir: Path, model: ModelConfig
) -> dict[str, object]:
    safe_name = get_safe_model_name(model["model"])
    target_filenames = _discover_target_episode_filenames(resolved["selection"])
    target_set = set(target_filenames)

    model_dir = run_dir / safe_name
    existing_paths: list[Path] = []
    if model_dir.exists() and model_dir.is_dir():
        existing_paths = sorted(
            (
                path
                for path in model_dir.glob("*.json")
                if path.is_file() and path.name in target_set
            ),
            key=lambda path: _natural_sort_key(path.name),
        )

    observed_files = len(existing_paths)
    total = len(target_filenames)
    file_statuses: list[tuple[Path, str]] = [
        (path, _classify_episode_result(path)) for path in existing_paths
    ]
    successful_paths = [path for path, status in file_statuses if status == "success"]
    completed = len(successful_paths)
    pending = max(total - completed, 0)
    runtime_errors = sum(
        1 for _path, status in file_statuses if status == "runtime_error"
    )
    invalid_files = sum(1 for _path, status in file_statuses if status == "invalid")

    completion_rate = 0.0
    if total > 0:
        completion_rate = round((completed / total) * 100.0, 2)

    payload: dict[str, object] = {
        "total": total,
        "observed_files": observed_files,
        "completed": completed,
        "pending": pending,
        "completed_without_runtime_error": completed,
        "runtime_errors": runtime_errors,
        "invalid_files": invalid_files,
        "completion_rate": completion_rate,
        "updated_at": datetime.now().isoformat(timespec="seconds"),
    }

    if successful_paths:
        payload["last_completed_file"] = successful_paths[-1].name

    return payload


def _reconcile_episode_progress_in_state(
    resolved: ResolvedRun, state: dict[str, object], run_dir: Path
) -> dict[str, object]:
    model_state = _require_mapping(state.get("models", {}), "state.models")

    for model in resolved["models"]:
        safe_name = get_safe_model_name(model["model"])
        existing_entry = model_state.get(safe_name)

        entry: dict[str, object]
        if isinstance(existing_entry, dict):
            entry = {str(k): v for k, v in existing_entry.items()}
        else:
            entry = {
                "model": model["model"],
                "status": "pending",
                "attempts": 0,
                "returncode": None,
                "error": "",
            }

        progress = _collect_episode_progress_for_model(resolved, run_dir, model)
        entry["episode_progress"] = progress

        total = progress.get("total")
        pending = progress.get("pending")
        if isinstance(total, int) and isinstance(pending, int):
            if total > 0 and pending == 0:
                entry["status"] = "success"
                if entry.get("returncode") is None:
                    entry["returncode"] = 0
                if not isinstance(entry.get("error"), str):
                    entry["error"] = ""
            elif str(entry.get("status", "")).lower() == "success" and pending > 0:
                entry["status"] = "pending"

        entry["updated_at"] = datetime.now().isoformat(timespec="seconds")
        model_state[safe_name] = entry

    state["models"] = model_state
    if "run_id" not in state:
        state["run_id"] = resolved["run_id"]
    if "created_at" not in state:
        state["created_at"] = datetime.now().isoformat(timespec="seconds")
    state["updated_at"] = datetime.now().isoformat(timespec="seconds")
    return state


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Virtual SmartHome - Spec-driven Parallel Model Evaluation"
    )
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--spec", type=str, help="Path to evaluation spec file")
    mode.add_argument("--resume", type=str, help="Path to existing run directory")
    return parser.parse_args()


def _require_mapping(value: object, path: str) -> dict[str, object]:
    if not isinstance(value, dict):
        raise ValueError(f"{path} must be a mapping")
    return {str(k): v for k, v in value.items()}


def _read_spec_file(spec_path: Path) -> dict[str, object]:
    if not spec_path.exists():
        raise FileNotFoundError(f"spec file not found: {spec_path}")

    suffix = spec_path.suffix.lower()
    if suffix not in {".yaml", ".yml"}:
        raise ValueError("spec must be .yaml or .yml")

    text = spec_path.read_text(encoding="utf-8")
    loaded = yaml.safe_load(text)

    return _require_mapping(loaded, "spec")


def _to_float(raw: object, key_name: str) -> float:
    if isinstance(raw, (int, float)):
        return float(raw)
    if isinstance(raw, str) and raw.strip():
        return float(raw)
    raise ValueError(f"{key_name} must be numeric")


def _to_int(raw: object, key_name: str) -> int:
    if isinstance(raw, int):
        return raw
    if isinstance(raw, float):
        return int(raw)
    if isinstance(raw, str) and raw.strip():
        return int(raw)
    raise ValueError(f"{key_name} must be an integer")


def _resolve_strategy(spec: dict[str, object]) -> StrategySettings:
    raw_strategy = spec.get("strategy", "react")
    name: str
    overrides: dict[str, object]

    if isinstance(raw_strategy, str):
        name = _normalize_strategy_name(raw_strategy)
        overrides = {}
    else:
        strategy_map = _require_mapping(raw_strategy, "strategy")
        name = _normalize_strategy_name(str(strategy_map.get("name", "react")))
        overrides = strategy_map

    if name not in DEFAULT_STRATEGY_PRESETS:
        raise ValueError(
            f"strategy '{name}' is not supported. Use one of: {sorted(DEFAULT_STRATEGY_PRESETS.keys())}"
        )

    base = DEFAULT_STRATEGY_PRESETS[name]
    timeout = _to_float(overrides.get("timeout", base["timeout"]), "strategy.timeout")
    temperature = _to_float(
        overrides.get("temperature", base["temperature"]), "strategy.temperature"
    )
    max_steps = _to_int(
        overrides.get("max_steps", base["max_steps"]), "strategy.max_steps"
    )

    if timeout <= 0:
        raise ValueError("strategy.timeout must be > 0")
    if max_steps <= 0:
        raise ValueError("strategy.max_steps must be > 0")

    return {
        "name": name,
        "timeout": timeout,
        "temperature": temperature,
        "max_steps": max_steps,
    }


def _resolve_orchestration(spec: dict[str, object]) -> OrchestrationSettings:
    raw = spec.get("orchestration", {})
    orch = _require_mapping(raw, "orchestration")

    raw_max_workers = orch.get("max_workers")
    max_workers: int | None
    if raw_max_workers is None:
        max_workers = None
    else:
        max_workers = _to_int(raw_max_workers, "orchestration.max_workers")
        if max_workers < 1:
            raise ValueError("orchestration.max_workers must be >= 1")

    simulator_start_timeout = _to_int(
        orch.get("simulator_start_timeout", 30),
        "orchestration.simulator_start_timeout",
    )
    simulator_start_retries = _to_int(
        orch.get("simulator_start_retries", 0),
        "orchestration.simulator_start_retries",
    )
    evaluation_retries = _to_int(
        orch.get("evaluation_retries", 0),
        "orchestration.evaluation_retries",
    )
    allow_partial_start = bool(orch.get("allow_partial_start", False))

    if simulator_start_timeout < 1:
        raise ValueError("orchestration.simulator_start_timeout must be >= 1")
    if simulator_start_retries < 0:
        raise ValueError("orchestration.simulator_start_retries must be >= 0")
    if evaluation_retries < 0:
        raise ValueError("orchestration.evaluation_retries must be >= 0")

    return {
        "max_workers": max_workers,
        "simulator_start_timeout": simulator_start_timeout,
        "simulator_start_retries": simulator_start_retries,
        "evaluation_retries": evaluation_retries,
        "allow_partial_start": allow_partial_start,
    }


def _resolve_selection(spec: dict[str, object]) -> EpisodeSelection:
    episode = _require_mapping(spec.get("episode"), "episode")
    episode_dir = episode.get("dir")
    if not isinstance(episode_dir, str) or not episode_dir.strip():
        raise ValueError("episode.dir is required and must be a string")

    qt = episode.get("qt")
    case = episode.get("case")
    seed = episode.get("seed")

    qt_value = str(qt).strip() if qt is not None else None
    case_value = str(case).strip() if case is not None else None
    seed_value = str(seed).strip() if seed is not None else None

    if any(v is not None and v != "" for v in (qt_value, case_value, seed_value)):
        if not qt_value or not case_value or not seed_value:
            raise ValueError(
                "episode.qt, episode.case, and episode.seed must be set together"
            )
    else:
        qt_value = None
        case_value = None
        seed_value = None

    return {
        "episode_dir": episode_dir.strip(),
        "qt": qt_value,
        "case": case_value,
        "seed": seed_value,
    }


def _resolve_model_configs(spec: dict[str, object]) -> list[ModelConfig]:
    global_api = _require_mapping(spec.get("api"), "api")
    global_judge = _require_mapping(spec.get("judge"), "judge")

    global_api_base = resolve_secret_value(global_api.get("base"), "api.base", True)
    if not isinstance(global_api_base, str) or not global_api_base.strip():
        raise ValueError("api.base must resolve to a non-empty string")
    global_api_base = global_api_base.strip()
    global_api_key_raw = global_api.get("key")
    _ = resolve_api_key_for_base(global_api_key_raw, global_api_base, "api.key")

    global_judge_model_raw = global_judge.get("model")
    if (
        not isinstance(global_judge_model_raw, str)
        or not global_judge_model_raw.strip()
    ):
        raise ValueError("judge.model must be a non-empty string")
    global_judge_model = global_judge_model_raw.strip()

    global_judge_api_base = resolve_secret_value(
        global_judge.get("api_base"),
        "judge.api_base",
        True,
    )
    if not isinstance(global_judge_api_base, str) or not global_judge_api_base.strip():
        raise ValueError("judge.api_base must resolve to a non-empty string")
    global_judge_api_base = global_judge_api_base.strip()
    global_judge_api_key_raw = global_judge.get("api_key")
    _ = resolve_api_key_for_base(
        global_judge_api_key_raw,
        global_judge_api_base,
        "judge.api_key",
    )

    raw_models = spec.get("models")
    if not isinstance(raw_models, list) or not raw_models:
        raise ValueError("models must be a non-empty list")

    models: list[ModelConfig] = []
    for idx, entry in enumerate(raw_models):
        model_entry: dict[str, object]
        if isinstance(entry, str):
            model_entry = {"model": entry}
        else:
            model_entry = _require_mapping(entry, f"models[{idx}]")

        model_name_raw = model_entry.get("model")
        if not isinstance(model_name_raw, str) or not model_name_raw.strip():
            raise ValueError(f"models[{idx}].model must be a non-empty string")
        model_name = model_name_raw.strip()

        api_base_raw = model_entry.get("api_base", global_api_base)
        api_key_raw = model_entry.get("api_key", global_api_key_raw)
        judge_model_raw = model_entry.get(
            "judge_model",
            global_judge_model,
        )
        judge_api_base_raw = model_entry.get(
            "judge_api_base",
            global_judge_api_base,
        )
        judge_api_key_raw = model_entry.get("judge_api_key", global_judge_api_key_raw)

        api_base = resolve_secret_value(api_base_raw, f"models[{idx}].api_base", True)
        if not isinstance(api_base, str):
            raise ValueError(f"models[{idx}].api_base must be a string")

        api_key = resolve_api_key_for_base(
            api_key_raw, api_base, f"models[{idx}].api_key"
        )

        if not isinstance(judge_model_raw, str) or not judge_model_raw.strip():
            raise ValueError(f"models[{idx}].judge_model must be a non-empty string")
        judge_model = judge_model_raw.strip()

        judge_api_base = resolve_secret_value(
            judge_api_base_raw, f"models[{idx}].judge_api_base", True
        )
        if not isinstance(judge_api_base, str):
            raise ValueError(f"models[{idx}].judge_api_base must be a string")

        judge_api_key = resolve_api_key_for_base(
            judge_api_key_raw,
            judge_api_base,
            f"models[{idx}].judge_api_key",
        )

        models.append(
            {
                "model": model_name,
                "api_base": api_base or "",
                "api_key": api_key or "",
                "judge_model": judge_model,
                "judge_api_base": judge_api_base or "",
                "judge_api_key": judge_api_key or "",
            }
        )

    return models


def _resolve_run(
    spec: dict[str, object], spec_path: Path, forced_run_id: str | None = None
) -> ResolvedRun:
    schema_raw = spec.get("schema")
    if not isinstance(schema_raw, str) or not schema_raw.strip():
        raise ValueError("schema is required and must be a string")
    schema = schema_raw.strip()
    if schema != SPEC_SCHEMA_VERSION:
        raise ValueError(f"schema must be '{SPEC_SCHEMA_VERSION}', got '{schema}'")

    run_section = _require_mapping(spec.get("run"), "run")
    output_root_raw = run_section.get("output_root")
    if not isinstance(output_root_raw, str) or not output_root_raw.strip():
        raise ValueError("run.output_root must be a non-empty string")
    output_root = output_root_raw.strip()

    if forced_run_id is not None:
        run_id = forced_run_id
    else:
        run_id_raw = run_section.get("id")
        if run_id_raw is None:
            raise ValueError("run.id is required")
        run_id = str(run_id_raw).strip()
        if not run_id:
            raise ValueError("run.id must not be empty")

    return {
        "run_id": run_id,
        "output_root": output_root,
        "spec_path": str(spec_path.resolve()),
        "strategy": _resolve_strategy(spec),
        "orchestration": _resolve_orchestration(spec),
        "selection": _resolve_selection(spec),
        "models": _resolve_model_configs(spec),
    }


def _run_dir(resolved: ResolvedRun) -> Path:
    return Path(resolved["output_root"]) / resolved["run_id"]


def _json_write(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temp_path = path.with_suffix(path.suffix + ".tmp")
    temp_path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    temp_path.replace(path)


def _json_read(path: Path) -> dict[str, object]:
    loaded = json.loads(path.read_text(encoding="utf-8"))
    return _require_mapping(loaded, str(path))


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while True:
            chunk = handle.read(8192)
            if not chunk:
                break
            digest.update(chunk)
    return digest.hexdigest()


def _manifest_payload(
    resolved: ResolvedRun,
    *,
    spec_path: str,
    spec_source_path: str,
    spec_sha256: str,
) -> dict[str, object]:
    models_payload: list[dict[str, object]] = []
    for model in resolved["models"]:
        models_payload.append(
            {
                "model": model["model"],
                "api_base": model["api_base"],
                "api_key": "<redacted>",
                "judge_model": model["judge_model"],
                "judge_api_base": model["judge_api_base"],
                "judge_api_key": "<redacted>",
            }
        )

    return {
        "schema": SPEC_SCHEMA_VERSION,
        "created_at": datetime.now().isoformat(timespec="seconds"),
        "run_id": resolved["run_id"],
        "spec_path": spec_path,
        "spec_source_path": spec_source_path,
        "spec_sha256": spec_sha256,
        "resolved": {
            "run_id": resolved["run_id"],
            "output_root": resolved["output_root"],
            "strategy": resolved["strategy"],
            "orchestration": resolved["orchestration"],
            "selection": resolved["selection"],
            "models": models_payload,
        },
    }


def _initial_state(resolved: ResolvedRun) -> dict[str, object]:
    model_state: dict[str, object] = {}
    for model in resolved["models"]:
        safe_name = get_safe_model_name(model["model"])
        model_state[safe_name] = {
            "model": model["model"],
            "status": "pending",
            "attempts": 0,
            "returncode": None,
            "error": "",
            "updated_at": datetime.now().isoformat(timespec="seconds"),
        }

    return {
        "run_id": resolved["run_id"],
        "created_at": datetime.now().isoformat(timespec="seconds"),
        "updated_at": datetime.now().isoformat(timespec="seconds"),
        "models": model_state,
    }


def _load_resolved_for_resume(run_dir: Path) -> tuple[ResolvedRun, dict[str, object]]:
    manifest_path = run_dir / MANIFEST_FILE
    if not manifest_path.exists():
        raise FileNotFoundError(f"manifest not found: {manifest_path}")

    manifest = _json_read(manifest_path)
    manifest_schema = manifest.get("schema")
    if (
        not isinstance(manifest_schema, str)
        or manifest_schema.strip() != SPEC_SCHEMA_VERSION
    ):
        raise ValueError(f"manifest.schema must be '{SPEC_SCHEMA_VERSION}'")

    run_id = manifest.get("run_id")
    spec_path = manifest.get("spec_path")
    spec_sha256 = manifest.get("spec_sha256")
    if not isinstance(run_id, str) or not run_id:
        raise ValueError("manifest.run_id is missing or invalid")
    if not isinstance(spec_path, str) or not spec_path:
        raise ValueError("manifest.spec_path is missing or invalid")
    if not isinstance(spec_sha256, str) or not spec_sha256:
        raise ValueError("manifest.spec_sha256 is missing or invalid")

    resolved_spec_path = Path(spec_path)
    if not resolved_spec_path.is_absolute():
        resolved_spec_path = run_dir / resolved_spec_path
    resolved_spec_path = resolved_spec_path.resolve()
    if not resolved_spec_path.exists():
        raise FileNotFoundError(f"resume spec not found: {resolved_spec_path}")

    if _sha256_file(resolved_spec_path) != spec_sha256:
        raise ValueError("resume spec hash mismatch; run spec appears modified")

    spec = _read_spec_file(resolved_spec_path)
    resolved = _resolve_run(spec, resolved_spec_path, forced_run_id=run_id)
    resolved["output_root"] = str(run_dir.parent)

    return resolved, manifest


def _wait_for_simulator(simulator: SimulatorInfo, timeout: int) -> bool:
    start_at = time.time()
    health_url = f"http://127.0.0.1:{simulator['port']}/api/__health__"
    process = simulator["process"]

    while (time.time() - start_at) < timeout:
        if process.poll() is not None:
            return False
        try:
            response = requests.get(health_url, timeout=2)
            if response.status_code == 200:
                return True
        except Exception:
            pass
        time.sleep(1)

    return False


def _startup_one_model(
    model: ModelConfig,
    manager: SimulatorManager,
    allocator: PortAllocator,
    startup_timeout: int,
    startup_retries: int,
) -> StartupResult:
    max_attempts = startup_retries + 1
    attempts = 0
    last_error = ""

    for _ in range(max_attempts):
        attempts += 1
        port = allocator.allocate()
        runtime_cfg: ModelRuntimeConfig = {
            "model": model["model"],
            "api_base": model["api_base"],
            "api_key": model["api_key"],
            "judge_model": model["judge_model"],
            "judge_api_base": model["judge_api_base"],
            "judge_api_key": model["judge_api_key"],
            "port": port,
        }

        simulator = manager.start_simulator(runtime_cfg["model"], runtime_cfg["port"])
        if _wait_for_simulator(simulator, startup_timeout):
            return {
                "success": True,
                "model_config": runtime_cfg,
                "attempts": attempts,
                "error": "",
            }

        last_error = "simulator did not become healthy before timeout"
        try:
            manager.terminate_process(simulator["process"])
        except Exception as exc:
            last_error = f"{last_error}; terminate error: {exc}"

    failed_cfg: ModelRuntimeConfig = {
        "model": model["model"],
        "api_base": model["api_base"],
        "api_key": model["api_key"],
        "judge_model": model["judge_model"],
        "judge_api_base": model["judge_api_base"],
        "judge_api_key": model["judge_api_key"],
        "port": -1,
    }
    return {
        "success": False,
        "model_config": failed_cfg,
        "attempts": attempts,
        "error": last_error,
    }


def _startup_models(
    models: list[ModelConfig],
    manager: SimulatorManager,
    settings: OrchestrationSettings,
) -> tuple[list[ModelRuntimeConfig], list[EvaluationResult]]:
    allocator = PortAllocator()
    ready: list[ModelRuntimeConfig] = []
    startup_failures: list[EvaluationResult] = []

    with cf.ThreadPoolExecutor(max_workers=max(1, len(models))) as executor:
        futures = [
            executor.submit(
                _startup_one_model,
                model,
                manager,
                allocator,
                settings["simulator_start_timeout"],
                settings["simulator_start_retries"],
            )
            for model in models
        ]

        for future in cf.as_completed(futures):
            result = future.result()
            model_name = result["model_config"]["model"]
            safe_name = get_safe_model_name(model_name)
            if result["success"]:
                runtime_cfg = result["model_config"]
                ready.append(runtime_cfg)
                continue

            startup_failures.append(
                {
                    "original_model": model_name,
                    "safe_model": safe_name,
                    "port": -1,
                    "success": False,
                    "returncode": -1,
                    "attempts": result["attempts"],
                    "phase": "startup",
                    "error": result["error"],
                }
            )
            print(
                f"[Main] ERROR: Simulator startup failed for {model_name} after {result['attempts']} attempt(s)"
            )

    return ready, startup_failures


def _run_model_evaluation(args: tuple[Any, ...]) -> EvaluationResult:
    (
        model_cfg,
        strategy,
        selection,
        run_id,
        output_root,
        evaluation_retries,
    ) = args

    cfg = model_cfg
    safe_model = get_safe_model_name(cfg["model"])
    max_attempts = int(evaluation_retries) + 1
    attempts = 0
    last_error = ""
    last_returncode = -1
    succeeded = False

    def emit_event(event: ProgressEvent) -> None:
        payload: ProgressEvent = {
            "kind": str(event.get("kind", "")).strip(),
            "model": cfg["model"],
            "safe_model": safe_model,
            "run_id": run_id,
            "attempt": attempts,
        }

        for key in (
            "total",
            "initial_completed",
            "pending",
            "processed",
            "success",
            "failed",
            "episode",
            "message",
        ):
            value = event.get(key)
            if value is not None:
                payload[key] = value

        _emit_worker_event(payload)

    def emit_log(message: str, kind: str = "log") -> None:
        emit_event({"kind": kind, "message": message})

    try:
        while attempts < max_attempts:
            attempts += 1
            emit_log(
                f"Starting evaluation for {cfg['model']} (attempt {attempts}/{max_attempts})."
            )

            try:
                evaluate_episodes(
                    model=cfg["model"],
                    output_model=safe_model,
                    agent=str(strategy["name"]),
                    base_url=f"http://127.0.0.1:{cfg['port']}/api",
                    timeout=float(strategy["timeout"]),
                    temperature=float(strategy["temperature"]),
                    max_steps=int(strategy["max_steps"]),
                    episode_dir=selection["episode_dir"],
                    qt=selection["qt"],
                    case=selection["case"],
                    seed=selection["seed"],
                    judge_count=3,
                    skip_existing=True,
                    output_root=output_root,
                    run_id=run_id,
                    api_key=cfg["api_key"],
                    api_base=cfg["api_base"],
                    judge_model=cfg["judge_model"],
                    judge_api_base=cfg["judge_api_base"],
                    judge_api_key=cfg["judge_api_key"],
                    emit=emit_event,
                )

                last_returncode = 0
                last_error = ""
                succeeded = True
                return {
                    "original_model": cfg["model"],
                    "safe_model": safe_model,
                    "port": int(cfg["port"]),
                    "success": True,
                    "returncode": 0,
                    "attempts": attempts,
                    "phase": "evaluation",
                    "error": "",
                }
            except Exception as exc:
                last_returncode = -1
                last_error = str(exc)
                emit_log(
                    f"Evaluation attempt failed for {cfg['model']}: {exc}",
                    kind="error",
                )

            if attempts < max_attempts:
                emit_log(
                    f"Retrying evaluation for {cfg['model']} ({attempts}/{max_attempts - 1})"
                )

        return {
            "original_model": cfg["model"],
            "safe_model": safe_model,
            "port": int(cfg["port"]),
            "success": False,
            "returncode": last_returncode,
            "attempts": attempts,
            "phase": "evaluation",
            "error": last_error,
        }
    finally:
        emit_event(
            {
                "kind": "done",
                "message": last_error,
                "success": int(succeeded),
            }
        )


def _drain_progress_events(
    progress_queue: Any,
    *,
    progress_bars: dict[str, Any],
    per_model_completed: dict[str, int],
) -> int:
    consumed = 0

    while True:
        try:
            raw_event = progress_queue.get_nowait()
        except queue.Empty:
            break
        except Exception:
            break

        if not isinstance(raw_event, dict):
            continue
        consumed += 1

        kind = str(raw_event.get("kind", "")).strip()
        model_name = str(raw_event.get("model", "")).strip()
        safe_model = str(raw_event.get("safe_model", "")).strip()
        if not safe_model:
            safe_model = get_safe_model_name(model_name) if model_name else ""

        if kind == "init":
            initial_completed = int(raw_event.get("initial_completed", 0) or 0)
            if safe_model:
                known = per_model_completed.get(safe_model, 0)
                if initial_completed > known:
                    per_model_completed[safe_model] = initial_completed
            continue

        if kind == "error":
            continue

        if kind == "advance":
            processed = int(raw_event.get("processed", 0) or 0)
            initial_completed = int(raw_event.get("initial_completed", 0) or 0)
            absolute_completed = max(initial_completed + processed, 0)
            known_completed = per_model_completed.get(safe_model, 0)
            delta = absolute_completed - known_completed
            if delta > 0:
                bar = progress_bars.get(safe_model)
                if bar is not None:
                    bar.update(delta)
            if safe_model and absolute_completed > known_completed:
                per_model_completed[safe_model] = absolute_completed
            continue

        if kind == "log":
            continue

        if kind == "done":
            continue

    return consumed


def _select_models_for_execution(
    resolved: ResolvedRun, state: dict[str, object], resume_mode: bool
) -> list[ModelConfig]:
    if not resume_mode:
        return list(resolved["models"])

    model_status = _require_mapping(state.get("models", {}), "state.models")
    selected: list[ModelConfig] = []
    for model in resolved["models"]:
        safe_name = get_safe_model_name(model["model"])
        status_entry = model_status.get(safe_name)
        if isinstance(status_entry, dict):
            status = str(status_entry.get("status", "pending"))
            if status == "success":
                continue

            progress = status_entry.get("episode_progress")
            if isinstance(progress, dict):
                total = progress.get("total")
                completed = progress.get("completed")
                if (
                    isinstance(total, int)
                    and isinstance(completed, int)
                    and total > 0
                    and completed >= total
                ):
                    continue
        selected.append(model)

    return selected


def _update_state(
    state: dict[str, object], results: list[EvaluationResult]
) -> dict[str, object]:
    model_status = _require_mapping(state.get("models", {}), "state.models")

    for result in results:
        safe_name = result["safe_model"]
        status_value = "success" if result["success"] else f"{result['phase']}_failed"
        model_status[safe_name] = {
            "model": result["original_model"],
            "status": status_value,
            "attempts": result["attempts"],
            "returncode": result["returncode"],
            "error": result["error"],
            "port": result["port"],
            "updated_at": datetime.now().isoformat(timespec="seconds"),
        }

    state["models"] = model_status
    state["updated_at"] = datetime.now().isoformat(timespec="seconds")
    return state


def _build_summary(
    resolved: ResolvedRun, results: list[EvaluationResult]
) -> dict[str, object]:
    success_count = sum(1 for result in results if result["success"])
    failed = [result for result in results if not result["success"]]

    return {
        "run_id": resolved["run_id"],
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "output_dir": str(_run_dir(resolved)),
        "totals": {
            "models": len(results),
            "success": success_count,
            "failed": len(failed),
        },
        "successful_models": [
            result["original_model"] for result in results if result["success"]
        ],
        "failed_models": [result["original_model"] for result in failed],
        "results": results,
    }


def main() -> None:
    args = parse_args()
    load_dotenv()

    resume_mode = args.resume is not None
    if resume_mode:
        run_dir = Path(args.resume).resolve()
        if not run_dir.exists() or not run_dir.is_dir():
            raise FileNotFoundError(f"resume directory not found: {run_dir}")
        resolved, _ = _load_resolved_for_resume(run_dir)
    else:
        spec_path = Path(args.spec).resolve()
        raw_spec = _read_spec_file(spec_path)
        resolved = _resolve_run(raw_spec, spec_path)
        run_dir = _run_dir(resolved).resolve()
        if run_dir.exists():
            raise FileExistsError(
                f"run directory already exists: {run_dir}. Use --resume {run_dir}"
            )
        run_dir.mkdir(parents=True, exist_ok=False)
        copied_spec_path = run_dir / SPEC_COPY_FILE
        copied_spec_path.write_text(
            spec_path.read_text(encoding="utf-8"), encoding="utf-8"
        )
        copied_spec_sha = _sha256_file(copied_spec_path)
        _json_write(
            run_dir / MANIFEST_FILE,
            _manifest_payload(
                resolved,
                spec_path=SPEC_COPY_FILE,
                spec_source_path=str(spec_path),
                spec_sha256=copied_spec_sha,
            ),
        )

    episode_dir_path = Path(resolved["selection"]["episode_dir"])
    if not episode_dir_path.exists() or not episode_dir_path.is_dir():
        raise FileNotFoundError(
            f"episode directory not found: {resolved['selection']['episode_dir']}"
        )

    state_path = run_dir / STATE_FILE
    if state_path.exists():
        state = _json_read(state_path)
    else:
        state = _initial_state(resolved)
    state = _reconcile_episode_progress_in_state(resolved, state, run_dir)
    _json_write(state_path, state)

    target_models = _select_models_for_execution(resolved, state, resume_mode)
    if not target_models:
        print("[Main] Nothing to run. All models are already successful.")
        return

    simulator_manager = SimulatorManager()

    def cleanup_and_exit(
        signum: int | None = None, _frame: object | None = None
    ) -> None:
        simulator_manager.cleanup_all()
        if signum is None:
            sys.exit(0)
        sys.exit(128 + int(signum))

    signal.signal(signal.SIGINT, cleanup_and_exit)
    signal.signal(signal.SIGTERM, cleanup_and_exit)

    final_results: list[EvaluationResult] = []

    try:
        ready_models, startup_failures = _startup_models(
            target_models,
            simulator_manager,
            resolved["orchestration"],
        )
        final_results.extend(startup_failures)

        if startup_failures and not resolved["orchestration"]["allow_partial_start"]:
            print("[Main] Startup failure detected and allow_partial_start is false.")
            state = _update_state(state, final_results)
            _json_write(state_path, state)
            summary = _build_summary(resolved, final_results)
            _json_write(run_dir / SUMMARY_FILE, summary)
            sys.exit(1)

        if not ready_models:
            print("[Main] No simulator reached healthy state.")
            state = _update_state(state, final_results)
            _json_write(state_path, state)
            summary = _build_summary(resolved, final_results)
            _json_write(run_dir / SUMMARY_FILE, summary)
            sys.exit(1)

        seen_safe_names: set[str] = set()
        duplicate_safe_names: set[str] = set()
        for model in ready_models:
            safe_name = get_safe_model_name(model["model"])
            if safe_name in seen_safe_names:
                duplicate_safe_names.add(safe_name)
            else:
                seen_safe_names.add(safe_name)
        if duplicate_safe_names:
            duplicated = ", ".join(sorted(duplicate_safe_names))
            raise ValueError(
                "Duplicate model entries detected in eval spec (safe-name collision): "
                + duplicated
            )

        target_model_order = {
            item["model"]: idx for idx, item in enumerate(target_models)
        }
        ready_models.sort(
            key=lambda item: target_model_order.get(item["model"], len(target_models))
        )

        max_workers_cfg = resolved["orchestration"]["max_workers"]
        worker_count = len(ready_models)
        if max_workers_cfg is not None:
            worker_count = min(worker_count, max_workers_cfg)

        eval_args = [
            (
                model,
                resolved["strategy"],
                resolved["selection"],
                resolved["run_id"],
                resolved["output_root"],
                resolved["orchestration"]["evaluation_retries"],
            )
            for model in ready_models
        ]

        per_model_completed: dict[str, int] = {}
        progress_bars: dict[str, Any] = {}
        max_desc_width = max(
            len(get_safe_model_name(model["model"])) for model in ready_models
        )
        for model in ready_models:
            safe_name = get_safe_model_name(model["model"])
            progress_snapshot = _collect_episode_progress_for_model(
                resolved,
                run_dir,
                model,
            )
            total = _to_int(progress_snapshot.get("total", 0), "episode_progress.total")
            completed = _to_int(
                progress_snapshot.get("completed", 0),
                "episode_progress.completed",
            )
            bounded_completed = max(0, min(completed, total))
            per_model_completed[safe_name] = bounded_completed
            progress_bars[safe_name] = tqdm(
                total=max(total, 0),
                initial=bounded_completed,
                desc=f"{safe_name:<{max_desc_width}}",
                dynamic_ncols=True,
                leave=True,
                position=len(progress_bars),
            )

        progress_queue: Any = mp.Queue()

        try:
            with mp.Pool(
                processes=worker_count,
                initializer=_init_eval_worker,
                initargs=(progress_queue,),
            ) as pool:
                async_result = pool.map_async(_run_model_evaluation, eval_args)

                while not async_result.ready():
                    _drain_progress_events(
                        progress_queue,
                        progress_bars=progress_bars,
                        per_model_completed=per_model_completed,
                    )
                    time.sleep(0.05)

                _drain_progress_events(
                    progress_queue,
                    progress_bars=progress_bars,
                    per_model_completed=per_model_completed,
                )
                eval_results = async_result.get()
        finally:
            while _drain_progress_events(
                progress_queue,
                progress_bars=progress_bars,
                per_model_completed=per_model_completed,
            ):
                continue
            for bar in progress_bars.values():
                bar.close()
            try:
                progress_queue.close()
                progress_queue.join_thread()
            except Exception:
                pass

        final_results.extend(eval_results)

    finally:
        simulator_manager.cleanup_all()

    state = _update_state(state, final_results)
    state = _reconcile_episode_progress_in_state(resolved, state, run_dir)
    _json_write(state_path, state)

    summary = _build_summary(resolved, final_results)
    _json_write(run_dir / SUMMARY_FILE, summary)

    summary_totals = _require_mapping(summary.get("totals", {}), "summary.totals")
    success_count = _to_int(summary_totals.get("success", 0), "summary.totals.success")
    failed_count = _to_int(summary_totals.get("failed", 0), "summary.totals.failed")
    print(f"[Main] Completed: {success_count} succeeded, {failed_count} failed")

    if failed_count > 0:
        sys.exit(1)


if __name__ == "__main__":
    mp.set_start_method("spawn", force=True)
    try:
        main()
    except Exception as exc:
        print(f"Error: {exc}")
        sys.exit(1)
