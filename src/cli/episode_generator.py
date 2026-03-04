from __future__ import annotations

import argparse
import hashlib
import json
import os
import random
from collections.abc import Iterable, Mapping
from datetime import datetime, timezone
from pathlib import Path
from typing import Protocol, TypedDict, TypeVar, cast

import yaml
from dotenv import load_dotenv
from tqdm import tqdm

from src.cli.config_resolver import resolve_secret_value
from src.agents.providers import LLMProvider, OpenAIChatProvider
from src.agents.types import ChatMessage
from src.pipelines.episode_generation.core import constants as QGP_CONST
from src.pipelines.episode_generation.qt1.feasible_builder import (
    build_qt1_feasible_payload,
)
from src.pipelines.episode_generation.qt1.infeasible_builder import (
    build_qt1_infeasible_payload,
)
from src.pipelines.episode_generation.qt1.prompt_builder import build_qt1_messages
from src.pipelines.episode_generation.qt2.feasible_builder import (
    build_qt2_feasible_payload,
)
from src.pipelines.episode_generation.qt2.infeasible_builder import (
    build_qt2_infeasible_payload,
)
from src.pipelines.episode_generation.qt2.prompt_builder import build_qt2_messages
from src.pipelines.episode_generation.qt3.feasible_builder import (
    build_qt3_feasible_payload,
)
from src.pipelines.episode_generation.qt3.infeasible_builder import (
    build_qt3_infeasible_payload,
)
from src.pipelines.episode_generation.qt3.prompt_builder import build_qt3_messages
from src.pipelines.episode_generation.qt4_1.feasible_builder import (
    build_qt4_1_feasible_payload,
)
from src.pipelines.episode_generation.qt4_1.feasible_prompt_builder import (
    build_qt4_1_feasible_messages,
)
from src.pipelines.episode_generation.qt4_1.infeasible_builder import (
    build_qt4_1_infeasible_payload,
)
from src.pipelines.episode_generation.qt4_1.infeasible_prompt_builder import (
    build_qt4_1_infeasible_messages,
)
from src.pipelines.episode_generation.qt4_2.feasible_builder import (
    build_qt4_2_feasible_payload,
)
from src.pipelines.episode_generation.qt4_2.feasible_prompt_builder import (
    build_qt4_2_feasible_messages,
)
from src.pipelines.episode_generation.qt4_2.infeasible_builder import (
    build_qt4_2_infeasible_payload,
)
from src.pipelines.episode_generation.qt4_2.infeasible_prompt_builder import (
    build_qt4_2_infeasible_messages,
)
from src.pipelines.episode_generation.qt4_3.feasible_builder import (
    build_qt4_3_feasible_payload,
)
from src.pipelines.episode_generation.qt4_3.feasible_prompt_builder import (
    build_qt4_3_feasible_messages,
)
from src.pipelines.episode_generation.qt4_3.infeasible_builder import (
    build_qt4_3_infeasible_payload,
)
from src.pipelines.episode_generation.qt4_3.infeasible_prompt_builder import (
    build_qt4_3_infeasible_messages,
)
from src.pipelines.episode_generation.shared.messages import Message


DEFAULT_START_HOUR = 9
DEFAULT_END_HOUR = 18
MIN_ITEMS_FOR_PROGRESS_BAR = 2
SPEC_SCHEMA_VERSION = "simuhome-gen-spec-v1"
MANIFEST_FILE = "manifest.json"
STATE_FILE = "run_state.json"
SUMMARY_FILE = "run_summary.json"
EPISODES_DIRNAME = "episodes"
SPEC_COPY_FILE = "generation_spec.yaml"
LOCK_FILE = ".generation.lock"
QT_CHOICES = ["qt1", "qt2", "qt3", "qt4-1", "qt4-2", "qt4-3"]
T = TypeVar("T")


JsonDict = dict[str, object]


class EpisodeGenerationError(Exception):
    pass


class QueryGenerationError(EpisodeGenerationError):
    pass


class ConfigurationError(EpisodeGenerationError):
    pass


class ConfigBuilder(Protocol):
    def __call__(
        self,
        *,
        seed: int,
        home_schema: dict[str, object],
        base_time: str = ...,
    ) -> JsonDict: ...


class MessageBuilder(Protocol):
    def __call__(self, payload: JsonDict) -> list[Message]: ...


class QueryTypeConfig(TypedDict):
    valid_cases: list[str]
    config_builders: dict[str, ConfigBuilder]
    message_builder: MessageBuilder | None
    message_builders: dict[str, MessageBuilder] | None


class ResolvedGenerationSpec(TypedDict):
    run_id: str
    output_root: str
    spec_path: str
    qt: str
    case: str
    seeds: list[int]
    base_date: str
    home_schema: dict[str, object]
    llm_model: str
    llm_api_base: str
    llm_api_key: str
    llm_temperature: float


class QueryTypeHandler:
    _QT_CONFIG: dict[str, QueryTypeConfig] = {
        "qt1": {
            "valid_cases": ["feasible", "infeasible"],
            "config_builders": {
                "feasible": build_qt1_feasible_payload,
                "infeasible": build_qt1_infeasible_payload,
            },
            "message_builder": build_qt1_messages,
            "message_builders": None,
        },
        "qt2": {
            "valid_cases": ["feasible", "infeasible"],
            "config_builders": {
                "feasible": build_qt2_feasible_payload,
                "infeasible": build_qt2_infeasible_payload,
            },
            "message_builder": build_qt2_messages,
            "message_builders": None,
        },
        "qt3": {
            "valid_cases": ["feasible", "infeasible"],
            "config_builders": {
                "feasible": build_qt3_feasible_payload,
                "infeasible": build_qt3_infeasible_payload,
            },
            "message_builder": build_qt3_messages,
            "message_builders": None,
        },
        "qt4-1": {
            "valid_cases": ["feasible", "infeasible"],
            "config_builders": {
                "feasible": build_qt4_1_feasible_payload,
                "infeasible": build_qt4_1_infeasible_payload,
            },
            "message_builder": None,
            "message_builders": {
                "feasible": build_qt4_1_feasible_messages,
                "infeasible": build_qt4_1_infeasible_messages,
            },
        },
        "qt4-2": {
            "valid_cases": ["feasible", "infeasible"],
            "config_builders": {
                "feasible": build_qt4_2_feasible_payload,
                "infeasible": build_qt4_2_infeasible_payload,
            },
            "message_builder": None,
            "message_builders": {
                "feasible": build_qt4_2_feasible_messages,
                "infeasible": build_qt4_2_infeasible_messages,
            },
        },
        "qt4-3": {
            "valid_cases": ["feasible", "infeasible"],
            "config_builders": {
                "feasible": build_qt4_3_feasible_payload,
                "infeasible": build_qt4_3_infeasible_payload,
            },
            "message_builder": None,
            "message_builders": {
                "feasible": build_qt4_3_feasible_messages,
                "infeasible": build_qt4_3_infeasible_messages,
            },
        },
    }

    @staticmethod
    def get_valid_cases(qt: str) -> list[str]:
        config = QueryTypeHandler._QT_CONFIG.get(qt)
        if not config:
            return []
        return config["valid_cases"]

    @staticmethod
    def build_config(
        qt: str,
        case: str,
        seed: int,
        home_schema: dict[str, object],
        base_time: str,
    ) -> JsonDict:
        config = QueryTypeHandler._QT_CONFIG.get(qt)
        if not config:
            raise ConfigurationError(f"Invalid query type: {qt}")

        builder = config["config_builders"].get(case)
        if not builder:
            raise ConfigurationError(
                f"Invalid case '{case}' for query type '{qt}'. Valid cases: {config['valid_cases']}"
            )

        return builder(seed=seed, home_schema=home_schema, base_time=base_time)

    @staticmethod
    def build_messages(qt: str, case: str, data: JsonDict) -> list[Message]:
        config = QueryTypeHandler._QT_CONFIG.get(qt)
        if not config:
            raise ConfigurationError(f"Invalid query type: {qt}")

        if case not in config["valid_cases"]:
            raise ConfigurationError(
                f"Invalid case '{case}' for query type '{qt}'. Valid cases: {config['valid_cases']}"
            )

        builder = config.get("message_builder")
        if builder is not None:
            return builder(data)

        case_builders = config.get("message_builders")
        if case_builders is None:
            raise ConfigurationError(
                f"No message builders configured for query type '{qt}'"
            )

        case_builder = case_builders.get(case)
        if case_builder is None:
            raise ConfigurationError(
                f"No message builder found for case '{case}' in query type '{qt}'"
            )

        return case_builder(data)


def _dict_from_object(value: object) -> JsonDict:
    if isinstance(value, dict):
        return cast(JsonDict, value)
    return {}


def _to_chat_messages(messages: list[Message]) -> list[ChatMessage]:
    return [cast(ChatMessage, cast(object, msg)) for msg in messages]


def _utc_iso() -> str:
    return (
        datetime.now(timezone.utc)
        .replace(microsecond=0)
        .isoformat()
        .replace("+00:00", "Z")
    )


def _json_write(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2, sort_keys=True)


def _json_read(path: Path) -> object:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while True:
            chunk = handle.read(8192)
            if not chunk:
                break
            digest.update(chunk)
    return digest.hexdigest()


def _sanitize_error(exc: Exception) -> str:
    text = str(exc).replace("\n", " ").strip()
    if not text:
        text = exc.__class__.__name__
    if len(text) > 300:
        return text[:300]
    return text


def _require_mapping(raw: object, key_name: str) -> dict[str, object]:
    if not isinstance(raw, dict):
        raise ConfigurationError(f"{key_name} must be a mapping")
    return cast(dict[str, object], raw)


def _require_string(raw: object, key_name: str) -> str:
    if not isinstance(raw, str):
        raise ConfigurationError(f"{key_name} must be a string")
    value = raw.strip()
    if not value:
        raise ConfigurationError(f"{key_name} cannot be empty")
    return value


def _to_float(raw: object, key_name: str) -> float:
    if isinstance(raw, (int, float)):
        return float(raw)
    raise ConfigurationError(f"{key_name} must be a number")


def _to_int(raw: object, key_name: str) -> int:
    if isinstance(raw, bool) or not isinstance(raw, int):
        raise ConfigurationError(f"{key_name} must be an integer")
    return raw


def _require_exact_keys(
    mapping: Mapping[str, object],
    *,
    key_name: str,
    expected: tuple[str, ...],
) -> None:
    actual_keys = set(mapping.keys())
    expected_keys = set(expected)
    missing = sorted(expected_keys - actual_keys)
    unknown = sorted(actual_keys - expected_keys)
    if missing or unknown:
        parts: list[str] = []
        if missing:
            parts.append(f"missing keys: {', '.join(missing)}")
        if unknown:
            parts.append(f"unknown keys: {', '.join(unknown)}")
        raise ConfigurationError(f"{key_name} has invalid shape ({'; '.join(parts)})")


def _parse_numeric_range(
    raw: object,
    *,
    key_name: str,
    lower: float,
    upper: float,
) -> dict[str, float]:
    payload = _require_mapping(raw, key_name)
    _require_exact_keys(payload, key_name=key_name, expected=("min", "max"))

    minimum = _to_float(payload.get("min"), f"{key_name}.min")
    maximum = _to_float(payload.get("max"), f"{key_name}.max")
    if minimum > maximum:
        raise ConfigurationError(f"{key_name}.min cannot exceed max")
    if minimum < lower or maximum > upper:
        raise ConfigurationError(f"{key_name} must be within [{lower}, {upper}]")

    return {
        "min": minimum,
        "max": maximum,
    }


def _parse_home_schema(raw: object) -> dict[str, object]:
    home = _require_mapping(raw, "episode.home")
    _require_exact_keys(
        home,
        key_name="episode.home",
        expected=("room_count", "devices_per_room", "environment"),
    )

    room_count = _to_int(home.get("room_count"), "episode.home.room_count")
    min_room_count = 4
    max_room_count = min(QGP_CONST.MAX_ROOMS, 9)
    if room_count < min_room_count or room_count > max_room_count:
        raise ConfigurationError(
            f"episode.home.room_count must be between {min_room_count} and {max_room_count}"
        )

    devices_per_room = _require_mapping(
        home.get("devices_per_room"),
        "episode.home.devices_per_room",
    )
    _require_exact_keys(
        devices_per_room,
        key_name="episode.home.devices_per_room",
        expected=("min", "max"),
    )
    devices_min = _to_int(
        devices_per_room.get("min"),
        "episode.home.devices_per_room.min",
    )
    devices_max = _to_int(
        devices_per_room.get("max"),
        "episode.home.devices_per_room.max",
    )
    if devices_min < 1:
        raise ConfigurationError("episode.home.devices_per_room.min must be >= 1")
    if devices_min > devices_max:
        raise ConfigurationError("episode.home.devices_per_room.min cannot exceed max")
    if devices_max > QGP_CONST.MAX_DEVICES_PER_ROOM:
        raise ConfigurationError(
            f"episode.home.devices_per_room.max must be <= {QGP_CONST.MAX_DEVICES_PER_ROOM}"
        )
    if devices_max < 4:
        raise ConfigurationError(
            "episode.home.devices_per_room.max must be >= 4 to satisfy required room devices"
        )

    environment = _require_mapping(home.get("environment"), "episode.home.environment")
    _require_exact_keys(
        environment,
        key_name="episode.home.environment",
        expected=(
            "temperature_c",
            "humidity_pct",
            "illuminance_lux",
            "pm10_ugm3",
        ),
    )

    temperature_range = _parse_numeric_range(
        environment.get("temperature_c"),
        key_name="episode.home.environment.temperature_c",
        lower=QGP_CONST.TEMPERATURE_RANGE_CENTI[0] / 100.0,
        upper=QGP_CONST.TEMPERATURE_RANGE_CENTI[1] / 100.0,
    )
    humidity_range = _parse_numeric_range(
        environment.get("humidity_pct"),
        key_name="episode.home.environment.humidity_pct",
        lower=QGP_CONST.HUMIDITY_RANGE_CENTI[0] / 100.0,
        upper=QGP_CONST.HUMIDITY_RANGE_CENTI[1] / 100.0,
    )
    illuminance_range = _parse_numeric_range(
        environment.get("illuminance_lux"),
        key_name="episode.home.environment.illuminance_lux",
        lower=QGP_CONST.ILLUMINANCE_RANGE[0],
        upper=QGP_CONST.ILLUMINANCE_RANGE[1],
    )
    pm10_range = _parse_numeric_range(
        environment.get("pm10_ugm3"),
        key_name="episode.home.environment.pm10_ugm3",
        lower=QGP_CONST.PM10_RANGE[0],
        upper=QGP_CONST.PM10_RANGE[1],
    )

    return {
        "room_count": room_count,
        "devices_per_room": {
            "min": devices_min,
            "max": devices_max,
        },
        "environment": {
            "temperature_c": temperature_range,
            "humidity_pct": humidity_range,
            "illuminance_lux": illuminance_range,
            "pm10_ugm3": pm10_range,
        },
    }


def _requires_temperature_one(model: str) -> bool:
    normalized = model.strip().lower()
    return normalized == "gpt-5-mini" or normalized.endswith("/gpt-5-mini")


def _parse_integer_spec(spec: str) -> list[int]:
    tokens = [t.strip() for t in (spec or "").split(",") if t.strip()]
    out: list[int] = []
    seen: set[int] = set()
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


def _parse_seed_spec(raw: object) -> list[int]:
    if isinstance(raw, int):
        return [raw]

    if isinstance(raw, str):
        parsed = _parse_integer_spec(raw)
        if not parsed:
            raise ConfigurationError("episode.seed parsed to empty list")
        return parsed

    if isinstance(raw, list):
        out: list[int] = []
        seen: set[int] = set()
        for idx, item in enumerate(raw):
            if isinstance(item, int):
                if item not in seen:
                    out.append(item)
                    seen.add(item)
                continue

            if isinstance(item, str):
                parsed = _parse_integer_spec(item)
                if not parsed:
                    raise ConfigurationError(
                        f"episode.seed[{idx}] parsed to empty list"
                    )
                for seed_value in parsed:
                    if seed_value not in seen:
                        out.append(seed_value)
                        seen.add(seed_value)
                continue

            raise ConfigurationError(
                f"episode.seed[{idx}] must be an int or integer-spec string"
            )

        if not out:
            raise ConfigurationError("episode.seed parsed to empty list")
        return out

    raise ConfigurationError(
        "episode.seed must be an int, integer-spec string, or a list of those"
    )


def _parse_base_date(raw: object) -> str:
    base_date = _require_string(raw, "episode.base_date")
    try:
        datetime.strptime(base_date, "%Y-%m-%d")
    except ValueError as exc:
        raise ConfigurationError(
            "episode.base_date must be a valid date in YYYY-MM-DD format"
        ) from exc
    return base_date


def _generate_random_base_time(seed: int, *, base_date: str) -> str:
    rng = random.Random(seed)
    hour = rng.randint(DEFAULT_START_HOUR, DEFAULT_END_HOUR)
    minute = rng.randint(0, 59)
    second = rng.randint(0, 59)
    return f"{base_date} {hour:02d}:{minute:02d}:{second:02d}"


def _resolve_generation_spec(
    spec_path: Path,
    *,
    forced_run_id: str | None = None,
    forced_output_root: str | None = None,
) -> ResolvedGenerationSpec:
    if not spec_path.exists():
        raise FileNotFoundError(f"spec file not found: {spec_path}")

    with spec_path.open("r", encoding="utf-8") as handle:
        raw_spec = yaml.safe_load(handle)

    spec = _require_mapping(raw_spec, "spec")
    schema = _require_string(spec.get("schema"), "schema")
    if schema != SPEC_SCHEMA_VERSION:
        raise ConfigurationError(
            f"schema must be '{SPEC_SCHEMA_VERSION}', got '{schema}'"
        )
    _require_exact_keys(
        spec,
        key_name="spec",
        expected=("schema", "run", "episode", "llm"),
    )

    run = _require_mapping(spec.get("run"), "run")
    run_id = forced_run_id or _require_string(run.get("id"), "run.id")
    output_root = forced_output_root or _require_string(
        run.get("output_root"), "run.output_root"
    )

    episode = _require_mapping(spec.get("episode"), "episode")
    qt = _require_string(episode.get("qt"), "episode.qt")
    if qt not in QT_CHOICES:
        raise ConfigurationError(f"episode.qt must be one of: {', '.join(QT_CHOICES)}")

    case = _require_string(episode.get("case"), "episode.case")
    home_schema = _parse_home_schema(episode.get("home"))

    valid_cases = QueryTypeHandler.get_valid_cases(qt)
    if case not in valid_cases:
        raise ConfigurationError(
            f"episode.case '{case}' is invalid for {qt}. Valid cases: {valid_cases}"
        )

    seeds = _parse_seed_spec(episode.get("seed"))
    base_date = _parse_base_date(episode.get("base_date"))

    llm = _require_mapping(spec.get("llm"), "llm")
    llm_model = _require_string(llm.get("model"), "llm.model")

    llm_api_base = resolve_secret_value(llm.get("api_base"), "llm.api_base", True)
    if not isinstance(llm_api_base, str) or not llm_api_base.strip():
        raise ConfigurationError("llm.api_base must resolve to a non-empty string")

    llm_api_key = resolve_secret_value(llm.get("api_key"), "llm.api_key", True)
    if not isinstance(llm_api_key, str) or not llm_api_key.strip():
        raise ConfigurationError("llm.api_key must resolve to a non-empty string")

    llm_temperature = _to_float(llm.get("temperature", 0.5), "llm.temperature")
    if _requires_temperature_one(llm_model) and abs(llm_temperature - 1.0) > 1e-9:
        raise ConfigurationError("llm.temperature must be 1 for gpt-5-mini generation")

    return {
        "run_id": run_id,
        "output_root": output_root,
        "spec_path": str(spec_path.resolve()),
        "qt": qt,
        "case": case,
        "seeds": seeds,
        "base_date": base_date,
        "home_schema": home_schema,
        "llm_model": llm_model,
        "llm_api_base": llm_api_base.strip(),
        "llm_api_key": llm_api_key.strip(),
        "llm_temperature": llm_temperature,
    }


def _run_dir(resolved: ResolvedGenerationSpec) -> Path:
    return Path(resolved["output_root"]) / resolved["run_id"]


def _episodes_dir(run_dir: Path) -> Path:
    return run_dir / EPISODES_DIRNAME


def _acquire_run_lock(run_dir: Path) -> Path:
    lock_path = run_dir / LOCK_FILE
    try:
        fd = os.open(str(lock_path), os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    except FileExistsError as exc:
        raise ConfigurationError(
            f"run lock exists: {lock_path}. another generation process may be active"
        ) from exc
    with os.fdopen(fd, "w", encoding="utf-8") as handle:
        handle.write(f"pid={os.getpid()}\n")
        handle.write(f"created_at={_utc_iso()}\n")
    return lock_path


def _release_run_lock(lock_path: Path) -> None:
    try:
        lock_path.unlink()
    except FileNotFoundError:
        return


def _manifest_payload(
    resolved: ResolvedGenerationSpec,
    *,
    spec_path: str,
    spec_source_path: str,
    spec_sha256: str,
) -> dict[str, object]:
    return {
        "schema": SPEC_SCHEMA_VERSION,
        "run_id": resolved["run_id"],
        "spec_path": spec_path,
        "spec_source_path": spec_source_path,
        "spec_sha256": spec_sha256,
        "created_at": _utc_iso(),
        "resolved": {
            "run": {
                "id": resolved["run_id"],
                "output_root": resolved["output_root"],
            },
            "episode": {
                "qt": resolved["qt"],
                "case": resolved["case"],
                "seed": [str(seed) for seed in resolved["seeds"]],
                "base_date": resolved["base_date"],
                "home": resolved["home_schema"],
            },
            "llm": {
                "model": resolved["llm_model"],
                "api_base": resolved["llm_api_base"],
                "api_key": "<redacted>",
                "temperature": resolved["llm_temperature"],
            },
        },
    }


def _initial_state(resolved: ResolvedGenerationSpec) -> dict[str, object]:
    now = _utc_iso()
    seeds: dict[str, object] = {}
    for seed in resolved["seeds"]:
        seeds[str(seed)] = {
            "status": "pending",
            "file": None,
            "error": None,
            "updated_at": now,
        }

    state: dict[str, object] = {
        "run_id": resolved["run_id"],
        "created_at": now,
        "updated_at": now,
        "generation": {
            "qt": resolved["qt"],
            "case": resolved["case"],
            "total": len(resolved["seeds"]),
            "completed": 0,
            "failed": 0,
            "pending": len(resolved["seeds"]),
        },
        "seeds": seeds,
    }
    return state


def _normalize_seed_entry(entry: object, now: str) -> dict[str, object]:
    if not isinstance(entry, Mapping):
        return {
            "status": "pending",
            "file": None,
            "error": None,
            "updated_at": now,
        }

    status_raw = entry.get("status")
    status = status_raw if isinstance(status_raw, str) else "pending"
    if status not in {"pending", "success", "failed"}:
        status = "pending"

    file_raw = entry.get("file")
    file_path = file_raw if isinstance(file_raw, str) and file_raw.strip() else None

    error_raw = entry.get("error")
    error = error_raw if isinstance(error_raw, str) and error_raw.strip() else None

    updated_raw = entry.get("updated_at")
    updated_at = (
        updated_raw if isinstance(updated_raw, str) and updated_raw.strip() else now
    )

    return {
        "status": status,
        "file": file_path,
        "error": error,
        "updated_at": updated_at,
    }


def _is_valid_episode_output(path: Path) -> bool:
    if not path.exists() or not path.is_file():
        return False
    try:
        payload = _json_read(path)
    except Exception:
        return False
    if not isinstance(payload, dict):
        return False
    query = payload.get("query")
    return isinstance(query, str) and bool(query.strip())


def _candidate_episode_filenames(
    resolved: ResolvedGenerationSpec, seed: int
) -> list[str]:
    if resolved["qt"] == "qt2" and resolved["case"] == "feasible":
        return [
            f"qt2_feasible_seed_{seed}.json",
            f"qt2_infeasible_seed_{seed}.json",
        ]
    return [f"{resolved['qt']}_{resolved['case']}_seed_{seed}.json"]


def _discover_existing_episode_file(
    run_dir: Path, resolved: ResolvedGenerationSpec, seed: int
) -> str | None:
    episodes_dir = _episodes_dir(run_dir)
    for file_name in _candidate_episode_filenames(resolved, seed):
        candidate = episodes_dir / file_name
        if _is_valid_episode_output(candidate):
            return f"{EPISODES_DIRNAME}/{file_name}"
    return None


def _seed_success(seed_entry: Mapping[str, object], run_dir: Path) -> bool:
    status = seed_entry.get("status")
    file_rel = seed_entry.get("file")
    if status != "success":
        return False
    if not isinstance(file_rel, str) or not file_rel.strip():
        return False
    return _is_valid_episode_output(run_dir / file_rel)


def _refresh_generation_counts(
    resolved: ResolvedGenerationSpec, state: dict[str, object], run_dir: Path
) -> None:
    seeds_raw = state.get("seeds")
    seeds = seeds_raw if isinstance(seeds_raw, dict) else {}

    completed = 0
    failed = 0
    for seed in resolved["seeds"]:
        entry_raw = seeds.get(str(seed))
        entry = entry_raw if isinstance(entry_raw, Mapping) else {}
        if _seed_success(entry, run_dir):
            completed += 1
            continue

        status = entry.get("status") if isinstance(entry, Mapping) else None
        if status == "failed":
            failed += 1

    total = len(resolved["seeds"])
    pending = total - completed - failed
    state["generation"] = {
        "qt": resolved["qt"],
        "case": resolved["case"],
        "total": total,
        "completed": completed,
        "failed": failed,
        "pending": pending,
    }
    state["updated_at"] = _utc_iso()


def _reconcile_state_for_resume(
    resolved: ResolvedGenerationSpec, state: dict[str, object], run_dir: Path
) -> dict[str, object]:
    now = _utc_iso()
    seed_map_raw = state.get("seeds")
    existing_seed_map = seed_map_raw if isinstance(seed_map_raw, dict) else {}

    reconciled_seeds: dict[str, object] = {}
    for seed in resolved["seeds"]:
        key = str(seed)
        normalized = _normalize_seed_entry(existing_seed_map.get(key), now)
        if _seed_success(normalized, run_dir):
            normalized["error"] = None
        else:
            recovered_file = _discover_existing_episode_file(run_dir, resolved, seed)
            if recovered_file:
                normalized["status"] = "success"
                normalized["file"] = recovered_file
                normalized["error"] = None
                normalized["updated_at"] = now
            else:
                normalized["status"] = "pending"

        reconciled_seeds[key] = normalized

    state["run_id"] = resolved["run_id"]
    created_at = state.get("created_at")
    state["created_at"] = created_at if isinstance(created_at, str) else now
    state["seeds"] = reconciled_seeds
    _refresh_generation_counts(resolved, state, run_dir)
    return state


def _pending_seeds(
    resolved: ResolvedGenerationSpec, state: Mapping[str, object], run_dir: Path
) -> list[int]:
    seeds_raw = state.get("seeds")
    seed_map = seeds_raw if isinstance(seeds_raw, Mapping) else {}
    pending: list[int] = []
    for seed in resolved["seeds"]:
        entry_raw = seed_map.get(str(seed))
        entry = entry_raw if isinstance(entry_raw, Mapping) else {}
        if not _seed_success(entry, run_dir):
            pending.append(seed)
    return pending


def _set_seed_state(
    state: dict[str, object],
    seed: int,
    *,
    status: str,
    file_rel: str | None,
    error: str | None,
) -> None:
    seed_map_raw = state.get("seeds")
    if not isinstance(seed_map_raw, dict):
        seed_map_raw = {}
        state["seeds"] = seed_map_raw

    seed_map_raw[str(seed)] = {
        "status": status,
        "file": file_rel,
        "error": error,
        "updated_at": _utc_iso(),
    }


def _load_state_or_init(
    resolved: ResolvedGenerationSpec, run_dir: Path
) -> dict[str, object]:
    state_path = run_dir / STATE_FILE
    if not state_path.exists():
        return _initial_state(resolved)

    raw_state = _json_read(state_path)
    if not isinstance(raw_state, dict):
        return _initial_state(resolved)

    return _reconcile_state_for_resume(
        resolved, cast(dict[str, object], raw_state), run_dir
    )


def _load_resolved_for_resume(run_dir: Path) -> ResolvedGenerationSpec:
    manifest_path = run_dir / MANIFEST_FILE
    if not manifest_path.exists():
        raise FileNotFoundError(f"manifest not found: {manifest_path}")

    manifest_raw = _json_read(manifest_path)
    manifest = _require_mapping(manifest_raw, "manifest")
    manifest_schema = _require_string(manifest.get("schema"), "manifest.schema")
    if manifest_schema != SPEC_SCHEMA_VERSION:
        raise ConfigurationError(
            f"manifest.schema must be '{SPEC_SCHEMA_VERSION}', got '{manifest_schema}'"
        )

    run_id = _require_string(manifest.get("run_id"), "manifest.run_id")
    spec_path_raw = _require_string(manifest.get("spec_path"), "manifest.spec_path")
    spec_sha256 = _require_string(manifest.get("spec_sha256"), "manifest.spec_sha256")

    spec_path = Path(spec_path_raw)
    if not spec_path.is_absolute():
        spec_path = run_dir / spec_path
    spec_path = spec_path.resolve()
    if not spec_path.exists():
        raise FileNotFoundError(f"resume spec not found: {spec_path}")

    if _sha256_file(spec_path) != spec_sha256:
        raise ConfigurationError("resume spec hash mismatch; run spec appears modified")

    return _resolve_generation_spec(
        spec_path,
        forced_run_id=run_id,
        forced_output_root=str(run_dir.parent),
    )


def _create_progress_iterator(items: list[T], description: str) -> Iterable[T]:
    return (
        tqdm(items, desc=description, dynamic_ncols=True)
        if len(items) >= MIN_ITEMS_FOR_PROGRESS_BAR
        else items
    )


def _progress_print(message: str, use_tqdm: bool) -> None:
    if use_tqdm:
        tqdm.write(message)
    else:
        print(message)


def _generate_single_episode(
    resolved: ResolvedGenerationSpec,
    provider: LLMProvider,
    seed_value: int,
    episodes_dir: Path,
    *,
    use_tqdm: bool,
) -> str:
    random_base_time = _generate_random_base_time(
        seed_value,
        base_date=resolved["base_date"],
    )
    payload = QueryTypeHandler.build_config(
        resolved["qt"],
        resolved["case"],
        seed=seed_value,
        home_schema=resolved["home_schema"],
        base_time=random_base_time,
    )

    if hasattr(provider, "seed"):
        try:
            setattr(provider, "seed", int(seed_value))
        except Exception:
            pass

    try:
        messages = QueryTypeHandler.build_messages(
            resolved["qt"], resolved["case"], payload
        )
        text = provider.generate(_to_chat_messages(messages)) or ""
    except Exception as exc:
        raise QueryGenerationError(str(exc)) from exc

    payload["query"] = text.strip()
    if not payload["query"]:
        raise QueryGenerationError("empty query generated")

    final_case = resolved["case"]
    if resolved["qt"] == "qt2" and resolved["case"] == "feasible":
        meta_feasibility = _dict_from_object(payload.get("meta")).get(
            "feasibility", True
        )
        if not meta_feasibility:
            final_case = "infeasible"

    file_name = f"{resolved['qt']}_{final_case}_seed_{seed_value}.json"
    output_path = episodes_dir / file_name
    temp_path = output_path.with_suffix(output_path.suffix + ".tmp")
    with temp_path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2)
    temp_path.replace(output_path)

    _progress_print(f"OK seed={seed_value}: {file_name}", use_tqdm)

    return f"{EPISODES_DIRNAME}/{file_name}"


def _run_generation(
    resolved: ResolvedGenerationSpec,
    state: dict[str, object],
    run_dir: Path,
) -> None:
    provider = OpenAIChatProvider(
        model=resolved["llm_model"],
        temperature=resolved["llm_temperature"],
        seed=42,
        api_key=resolved["llm_api_key"],
        api_base=resolved["llm_api_base"],
    )

    episodes_dir = _episodes_dir(run_dir)
    episodes_dir.mkdir(parents=True, exist_ok=True)

    pending = _pending_seeds(resolved, state, run_dir)
    if not pending:
        print("[generation] no pending seeds")
        return

    use_tqdm = len(pending) >= MIN_ITEMS_FOR_PROGRESS_BAR
    iterator = _create_progress_iterator(
        pending, f"qt={resolved['qt']} case={resolved['case']}"
    )

    for seed_value in iterator:
        try:
            file_rel = _generate_single_episode(
                resolved, provider, seed_value, episodes_dir, use_tqdm=use_tqdm
            )
            _set_seed_state(
                state,
                seed_value,
                status="success",
                file_rel=file_rel,
                error=None,
            )
        except Exception as exc:
            _set_seed_state(
                state,
                seed_value,
                status="failed",
                file_rel=None,
                error=_sanitize_error(exc),
            )
            _progress_print(f"ERROR seed={seed_value}: {exc}", use_tqdm)

        _refresh_generation_counts(resolved, state, run_dir)
        _json_write(run_dir / STATE_FILE, state)


def _build_summary(
    resolved: ResolvedGenerationSpec,
    state: Mapping[str, object],
    run_dir: Path,
) -> dict[str, object]:
    generation_raw = state.get("generation")
    generation = generation_raw if isinstance(generation_raw, Mapping) else {}

    seeds_raw = state.get("seeds")
    seeds = seeds_raw if isinstance(seeds_raw, Mapping) else {}

    success_files: list[str] = []
    failed_items: list[dict[str, object]] = []
    pending_items: list[int] = []

    for seed in resolved["seeds"]:
        entry_raw = seeds.get(str(seed))
        entry = entry_raw if isinstance(entry_raw, Mapping) else {}
        status = entry.get("status")
        file_rel = entry.get("file")
        error = entry.get("error")

        if status == "success" and isinstance(file_rel, str) and file_rel.strip():
            if _is_valid_episode_output(run_dir / file_rel):
                success_files.append(file_rel)
            else:
                pending_items.append(seed)
            continue

        if status == "failed":
            failed_items.append(
                {
                    "seed": seed,
                    "error": error if isinstance(error, str) else "unknown",
                }
            )
            continue

        pending_items.append(seed)

    return {
        "schema": SPEC_SCHEMA_VERSION,
        "run_id": resolved["run_id"],
        "generated_at": _utc_iso(),
        "spec_path": resolved["spec_path"],
        "output_dir": str(_episodes_dir(run_dir)),
        "total": generation.get("total", len(resolved["seeds"])),
        "success": generation.get("completed", len(success_files)),
        "failed": generation.get("failed", len(failed_items)),
        "pending": generation.get("pending", len(pending_items)),
        "files": sorted(success_files),
        "failed_items": failed_items,
        "pending_seeds": pending_items,
    }


def create_argument_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Spec-driven smart home episode generation"
    )
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--spec", type=str, help="Path to generation spec YAML")
    mode.add_argument("--resume", type=str, help="Path to generation run directory")
    return parser


def _main() -> int:
    load_dotenv()
    parser = create_argument_parser()
    args = parser.parse_args()

    if args.spec:
        resolved = _resolve_generation_spec(Path(args.spec))
        run_dir = _run_dir(resolved)
        if run_dir.exists():
            raise FileExistsError(
                "run directory already exists: "
                f'{run_dir}. Resume with: uv run simuhome episode-resume --resume "{run_dir}"'
            )
        run_dir.mkdir(parents=True, exist_ok=False)
        _episodes_dir(run_dir).mkdir(parents=True, exist_ok=False)
        source_spec_path = Path(resolved["spec_path"])
        copied_spec_path = run_dir / SPEC_COPY_FILE
        copied_spec_path.write_text(
            source_spec_path.read_text(encoding="utf-8"), encoding="utf-8"
        )
        copied_spec_sha = _sha256_file(copied_spec_path)
        _json_write(
            run_dir / MANIFEST_FILE,
            _manifest_payload(
                resolved,
                spec_path=SPEC_COPY_FILE,
                spec_source_path=resolved["spec_path"],
                spec_sha256=copied_spec_sha,
            ),
        )
        state = _initial_state(resolved)
    else:
        run_dir = Path(args.resume).expanduser().resolve()
        if not run_dir.exists() or not run_dir.is_dir():
            raise FileNotFoundError(f"resume directory not found: {run_dir}")
        resolved = _load_resolved_for_resume(run_dir)
        _episodes_dir(run_dir).mkdir(parents=True, exist_ok=True)
        state = _load_state_or_init(resolved, run_dir)

    lock_path = _acquire_run_lock(run_dir)
    try:
        _refresh_generation_counts(resolved, state, run_dir)
        _json_write(run_dir / STATE_FILE, state)

        _run_generation(resolved, state, run_dir)

        _refresh_generation_counts(resolved, state, run_dir)
        _json_write(run_dir / STATE_FILE, state)

        summary = _build_summary(resolved, state, run_dir)
        _json_write(run_dir / SUMMARY_FILE, summary)

        failed = summary.get("failed")
        pending = summary.get("pending")
        if isinstance(failed, int) and isinstance(pending, int):
            if failed == 0 and pending == 0:
                return 0
        return 1
    finally:
        _release_run_lock(lock_path)


def main() -> None:
    try:
        raise SystemExit(_main())
    except (
        EpisodeGenerationError,
        FileNotFoundError,
        ValueError,
        OSError,
        yaml.YAMLError,
    ) as exc:
        print(f"[episode-generator] ERROR: {exc}")
        raise SystemExit(1) from exc


if __name__ == "__main__":
    main()
