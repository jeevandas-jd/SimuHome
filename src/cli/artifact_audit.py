from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections.abc import Mapping
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from src.cli.arg_utils import parse_integer_spec


ARTIFACT_AUDIT_SCHEMA = "simuhome-artifact-audit-v1"
GEN_SPEC_SCHEMA = "simuhome-gen-spec-v1"
EVAL_SPEC_SCHEMA = "simuhome-eval-spec-v1"
MANIFEST_FILE = "manifest.json"
STATE_FILE = "run_state.json"
SUMMARY_FILE = "run_summary.json"
EPISODES_DIRNAME = "episodes"
DEFAULT_REPORT_FILE = "artifact_audit.json"
DEFAULT_RERUN_PLAN_FILE = "artifact_rerun_plan.json"

STATUS_SUCCESS = "success"
STATUS_MISSING = "missing"
STATUS_INVALID = "invalid"
STATUS_RUNTIME_ERROR = "runtime_error"
STATUS_PENDING = "pending"
STATUS_SKIPPED = "skipped"

ARTIFACT_FAILURE_STATUSES = {
    STATUS_MISSING,
    STATUS_INVALID,
    STATUS_RUNTIME_ERROR,
    STATUS_PENDING,
    STATUS_SKIPPED,
}
ARTIFACT_SUCCESS_STATUSES = {STATUS_SUCCESS}
ALL_ARTIFACT_STATUSES = {
    *ARTIFACT_SUCCESS_STATUSES,
    *ARTIFACT_FAILURE_STATUSES,
}


def _utc_now() -> str:
    return (
        datetime.now(timezone.utc)
        .replace(microsecond=0)
        .isoformat()
        .replace("+00:00", "Z")
    )


def _json_read(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def _json_write(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temp_path = path.with_suffix(path.suffix + ".tmp")
    with temp_path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2, sort_keys=True)
    temp_path.replace(path)


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while True:
            chunk = handle.read(8192)
            if not chunk:
                break
            digest.update(chunk)
    return digest.hexdigest()


def _safe_text(raw: object, default: str = "") -> str:
    if isinstance(raw, str):
        return raw.strip()
    return default


def _is_failure_status(status: str) -> bool:
    return status in ARTIFACT_FAILURE_STATUSES


def _require_known_status(status: str) -> None:
    if status not in ALL_ARTIFACT_STATUSES:
        raise ValueError(f"unknown artifact status: {status!r}")


def _require_mapping(raw: object, label: str) -> dict[str, object]:
    if not isinstance(raw, dict):
        raise ValueError(f"{label} must be a mapping")
    return {str(k): v for k, v in raw.items()}


def _natural_sort_key(value: str) -> tuple[Any, ...]:
    return tuple(
        int(part) if part.isdigit() else part for part in re.split(r"(\d+)", value)
    )


def _normalize_seed_value(raw: object) -> list[int]:
    if isinstance(raw, list):
        flat: list[int] = []
        seen: set[int] = set()
        for item in raw:
            if isinstance(item, int):
                if item not in seen:
                    flat.append(item)
                    seen.add(item)
                continue
            if isinstance(item, str):
                parsed = parse_integer_spec(item)
                for seed in parsed:
                    if seed not in seen:
                        flat.append(seed)
                        seen.add(seed)
                continue
            raise ValueError(f"seed value must be int or int range string: {raw!r}")
        return flat
    if isinstance(raw, int):
        return [raw]
    if isinstance(raw, str):
        parsed = parse_integer_spec(raw)
        if not parsed:
            raise ValueError("seed list cannot be empty")
        return parsed
    raise ValueError("seed must be int, int-list, or range string")


def _safe_model_name(original_model: str) -> str:
    return original_model.replace("/", "_").replace(":", "_")


def _resolve_episode_directory(
    run_dir: Path,
    episode_dir_raw: str,
    manifest: Mapping[str, object] | None = None,
) -> Path:
    episode_dir = Path(episode_dir_raw.strip())
    if episode_dir.is_absolute():
        return episode_dir

    candidates = [run_dir / episode_dir, episode_dir]

    if isinstance(manifest, Mapping):
        spec_source_path = manifest.get("spec_source_path")
        if isinstance(spec_source_path, str) and spec_source_path.strip():
            spec_source = Path(spec_source_path.strip())
            if spec_source.is_file():
                candidates.append(spec_source.parent / episode_dir)
            elif spec_source.is_dir():
                candidates.append(spec_source / episode_dir)

    for candidate in candidates:
        if candidate.exists():
            return candidate

    return run_dir / episode_dir


def _classify_generation_output(path: Path) -> tuple[str, str]:
    if not path.exists() or not path.is_file():
        return STATUS_MISSING, "file_not_found"
    try:
        payload = _json_read(path)
    except Exception as exc:  # pragma: no cover - defensive
        return STATUS_INVALID, f"json_error:{type(exc).__name__}"
    if not isinstance(payload, dict):
        return STATUS_INVALID, "payload_not_object"
    query = payload.get("query")
    if not isinstance(query, str) or not query.strip():
        return STATUS_INVALID, "query_missing_or_empty"
    return STATUS_SUCCESS, "ok"


def _classify_evaluation_output(path: Path) -> tuple[str, str, dict[str, Any]]:
    if not path.exists() or not path.is_file():
        return STATUS_MISSING, "file_not_found", {}
    try:
        payload = _json_read(path)
    except Exception as exc:  # pragma: no cover - defensive
        return STATUS_INVALID, f"json_error:{type(exc).__name__}", {}
    if not isinstance(payload, dict):
        return STATUS_INVALID, "payload_not_object", {}

    evaluation_result = payload.get("evaluation_result")
    if not isinstance(evaluation_result, dict):
        return STATUS_INVALID, "evaluation_result_missing_or_invalid", {}

    attempted = evaluation_result.get("attempted")
    if attempted is False:
        return STATUS_SKIPPED, "attempted_false", {"attempted": False}

    error_type = evaluation_result.get("error_type")
    if isinstance(error_type, str) and error_type.strip():
        return (
            STATUS_RUNTIME_ERROR,
            f"error_type:{error_type.strip()}",
            {"error_type": error_type.strip()},
        )

    score = evaluation_result.get("score")
    if not isinstance(score, (int, float)):
        return STATUS_INVALID, "score_missing_or_invalid", {"error_type": error_type}
    if float(score) < 0:
        return STATUS_RUNTIME_ERROR, f"score_negative:{score}", {"score": score}
    return STATUS_SUCCESS, "ok", {"score": score}


def _coerce_manifest_seed_from_string(seed_value: object) -> int | None:
    if isinstance(seed_value, int):
        return seed_value
    if isinstance(seed_value, str):
        text = seed_value.strip()
        if text.isdigit() or (text.startswith("-") and text[1:].isdigit()):
            return int(text)
    return None


def _generation_candidates(qt: str, case: str, seed: int) -> list[str]:
    if qt == "qt2" and case == "feasible":
        return [
            f"qt2_feasible_seed_{seed}.json",
            f"qt2_infeasible_seed_{seed}.json",
        ]
    return [f"{qt}_{case}_seed_{seed}.json"]


def _discover_target_episodes(
    selection: Mapping[str, object],
    *,
    run_dir: Path,
    manifest: Mapping[str, object] | None = None,
) -> list[str]:
    episode_dir_raw = selection.get("episode_dir")
    if not isinstance(episode_dir_raw, str):
        raise ValueError("selection.episode_dir must be a string")
    episode_dir = _resolve_episode_directory(
        run_dir=run_dir,
        episode_dir_raw=episode_dir_raw,
        manifest=manifest,
    )
    if not episode_dir.exists() or not episode_dir.is_dir():
        raise FileNotFoundError(f"episode directory not found: {episode_dir_raw}")

    qt = selection.get("qt")
    case = selection.get("case")
    seed = selection.get("seed")
    qt_value = qt.strip() if isinstance(qt, str) else None
    case_value = case.strip() if isinstance(case, str) else None
    seed_value = str(seed).strip() if seed is not None else None

    if qt_value and case_value and seed_value:
        seed_values = parse_integer_spec(seed_value)
        return sorted(
            (
                f"{qt_value}_{case_value}_seed_{seed_value_item}.json"
                for seed_value_item in seed_values
            ),
            key=_natural_sort_key,
        )

    if qt_value or case_value or seed_value:
        raise ValueError(
            "episode.qt, episode.case, and episode.seed must be set together or all empty for full replay"
        )
    return sorted(
        (path.name for path in episode_dir.glob("*.json") if path.is_file()),
        key=_natural_sort_key,
    )


def _build_rerun_hint(run_dir: Path, run_type: str) -> str:
    if run_type == "generation":
        return f"uv run simuhome episode-resume --resume {run_dir}"
    return f"uv run simuhome eval-resume --resume {run_dir}"


def _initialize_counts() -> dict[str, int]:
    return {status: 0 for status in ALL_ARTIFACT_STATUSES}


def _increment(counts: dict[str, int], status: str) -> None:
    _require_known_status(status)
    counts[status] += 1


def _load_run_directory_manifest(run_dir: Path) -> dict[str, object]:
    manifest_path = run_dir / MANIFEST_FILE
    if not manifest_path.exists():
        raise FileNotFoundError(f"manifest file not found: {manifest_path}")
    payload = _json_read(manifest_path)
    if not isinstance(payload, dict):
        raise ValueError("manifest must be an object")
    return _require_mapping(payload, "manifest")


def _load_run_state(run_dir: Path) -> dict[str, object] | None:
    state_path = run_dir / STATE_FILE
    if not state_path.exists():
        return None
    raw = _json_read(state_path)
    if not isinstance(raw, dict):
        return None
    return {str(k): v for k, v in raw.items()}


def _audit_generation(
    run_dir: Path, manifest: Mapping[str, object], state: Mapping[str, object] | None
) -> tuple[dict[str, Any], dict[str, Any]]:
    resolved = _require_mapping(manifest.get("resolved"), "manifest.resolved")
    run_id = _safe_text(manifest.get("run_id"), "")
    if not run_id:
        raise ValueError("manifest.run_id is missing")

    episode = _require_mapping(resolved.get("episode"), "manifest.resolved.episode")
    qt = _safe_text(episode.get("qt"))
    case = _safe_text(episode.get("case"))
    if not qt or not case:
        raise ValueError("manifest.resolved.episode.qt and .case are required")

    seeds = _normalize_seed_value(episode.get("seed"))
    if not seeds:
        raise ValueError("manifest.resolved.episode.seed is required")

    episodes_dir = run_dir / EPISODES_DIRNAME
    state_seeds: dict[str, object] = {}
    if isinstance(state, dict):
        state_seeds = _require_mapping(state.get("seeds"), "run_state.seeds")

    problems: list[dict[str, Any]] = []
    items: list[dict[str, Any]] = []
    counts = _initialize_counts()
    manifest_seed_set = {seed for seed in seeds}
    state_seed_keys: set[str] = set()

    for seed in seeds:
        state_entry = state_seeds.get(str(seed))
        if isinstance(state_entry, dict):
            state_seed_keys.add(str(seed))
            seed_status = _safe_text(state_entry.get("status"), "pending")
            seed_error = _safe_text(state_entry.get("error"))
            state_file = _safe_text(state_entry.get("file"))
        else:
            seed_status = "pending"
            seed_error = ""
            state_file = ""

        candidates = _generation_candidates(qt, case, seed)
        expected_files = [f"{EPISODES_DIRNAME}/{name}" for name in candidates]
        valid_path: Path | None = None
        reason = ""
        status = STATUS_MISSING

        for filename in candidates:
            candidate = episodes_dir / filename
            candidate_status, candidate_reason = _classify_generation_output(candidate)
            if candidate_status == STATUS_SUCCESS:
                valid_path = candidate
                status = STATUS_SUCCESS
                reason = "ok"
                break
            if candidate_status == STATUS_INVALID:
                status = STATUS_INVALID
                reason = candidate_reason
            elif status == STATUS_MISSING:
                status = candidate_status
                reason = candidate_reason

        if valid_path is None and status in {STATUS_MISSING, STATUS_INVALID}:
            if seed_status == "failed":
                status = STATUS_RUNTIME_ERROR
                reason = seed_error or "state_marked_failed"
            elif seed_status == "success" and status == STATUS_MISSING:
                status = STATUS_INVALID
                reason = "state_marked_success_without_valid_output"
            else:
                status = STATUS_MISSING

        if status == STATUS_SUCCESS:
            _increment(counts, STATUS_SUCCESS)
        else:
            _increment(counts, status)

        item = {
            "scope": {
                "type": "seed",
                "seed": seed,
                "qt": qt,
                "case": case,
            },
            "status": status,
            "expected_files": expected_files,
            "output_file": str(valid_path.relative_to(run_dir))
            if valid_path is not None
            else (state_file or ""),
            "state_status": seed_status,
            "reason": reason,
        }
        if seed_error:
            item["state_error"] = seed_error
        items.append(item)

    # Flag extra seed states that are no longer in manifest
    for seed_key in state_seed_keys:
        seed_int = _coerce_manifest_seed_from_string(seed_key)
        if seed_int is not None and seed_int not in manifest_seed_set:
            problems.append(
                {
                    "severity": "warning",
                    "scope": "run_state",
                    "code": "extra_seed_state",
                    "message": f"state contains seed {seed_key} not requested by manifest",
                    "seed": seed_key,
                }
            )

    report_summary = {
        "generated_at": _utc_now(),
        "run_dir": str(run_dir),
        "run_id": run_id,
        "run_type": "generation",
        "manifest_schema": GEN_SPEC_SCHEMA,
        "counts": counts,
        "total_expected": len(seeds),
        "artifact_checks": {
            "manifest_valid": True,
            "state_exists": state is not None,
            "episodes_dir_exists": episodes_dir.exists() and episodes_dir.is_dir(),
        },
    }

    report = {
        "schema": ARTIFACT_AUDIT_SCHEMA,
        "generated_at": _utc_now(),
        "run_type": "generation",
        "run_id": run_id,
        "run_dir": str(run_dir),
        "manifest_schema": GEN_SPEC_SCHEMA,
        "summary": report_summary,
        "problems": problems,
        "items": items,
    }

    rerun_items: list[dict[str, Any]] = []
    for item in items:
        if _is_failure_status(item["status"]):
            entry = {
                "qt": qt,
                "case": case,
                "seed": item["scope"]["seed"],
                "status": item["status"],
                "reason": item["reason"],
            }
            rerun_items.append(entry)

    rerun_plan = {
        "schema": ARTIFACT_AUDIT_SCHEMA,
        "generated_at": _utc_now(),
        "run_type": "generation",
        "run_id": run_id,
        "run_dir": str(run_dir),
        "rerun_command": _build_rerun_hint(run_dir, "generation"),
        "count": len(rerun_items),
        "items": rerun_items,
    }

    return report, rerun_plan


def _parse_episode_filename(filename: str) -> tuple[str | None, str | None, str | None]:
    match = re.fullmatch(
        r"(qt\d(?:-\d+)?|qt\d)_(feasible|infeasible)_seed_(.+)\.json", filename
    )
    if not match:
        return None, None, None
    qt = match.group(1)
    case = match.group(2)
    seed = match.group(3)
    return qt, case, seed


def _audit_evaluation(
    run_dir: Path, manifest: Mapping[str, object], state: Mapping[str, object] | None
) -> tuple[dict[str, Any], dict[str, Any]]:
    resolved = _require_mapping(manifest.get("resolved"), "manifest.resolved")
    run_id = _safe_text(manifest.get("run_id"), "")
    if not run_id:
        raise ValueError("manifest.run_id is missing")

    selection = _require_mapping(
        resolved.get("selection"), "manifest.resolved.selection"
    )
    models_raw = resolved.get("models")
    if not isinstance(models_raw, list) or not models_raw:
        raise ValueError("manifest.resolved.models must be a non-empty list")

    model_names: list[tuple[str, str]] = []  # (display, safe)
    for idx, model_entry in enumerate(models_raw):
        if not isinstance(model_entry, dict):
            raise ValueError(f"manifest.resolved.models[{idx}] must be a mapping")

        model_raw = model_entry.get("model")
        if not isinstance(model_raw, str) or not model_raw.strip():
            raise ValueError(f"manifest.resolved.models[{idx}].model must be a string")
        model = model_raw.strip()
        model_names.append((model, _safe_model_name(model)))

    try:
        expected_episodes = _discover_target_episodes(
            selection, run_dir=run_dir, manifest=manifest
        )
    except FileNotFoundError:
        raise
    except Exception as exc:
        raise ValueError(f"invalid episode selection: {exc}") from exc

    if not expected_episodes:
        raise FileNotFoundError("no target episode files found from selection")

    state_models: dict[str, object] = {}
    if isinstance(state, dict):
        state_models = _require_mapping(state.get("models"), "run_state.models")

    problems: list[dict[str, Any]] = []
    items: list[dict[str, Any]] = []
    counts = _initialize_counts()

    if len(state_models) < len(model_names):
        problems.append(
            {
                "severity": "warning",
                "scope": "run_state",
                "code": "incomplete_model_state",
                "message": "run_state is missing some model entries",
            }
        )

    for model, safe_model in model_names:
        model_dir = run_dir / safe_model
        model_entry = state_models.get(safe_model)
        model_status = (
            _safe_text(model_entry.get("status"), "missing")
            if isinstance(model_entry, dict)
            else "missing"
        )

        for filename in expected_episodes:
            file_path = model_dir / filename
            status, reason, extra = _classify_evaluation_output(file_path)
            _increment(counts, status)

            qt, case, seed = _parse_episode_filename(filename)
            item = {
                "scope": {
                    "type": "evaluation_file",
                    "model": model,
                    "safe_model": safe_model,
                    "filename": filename,
                    "qt": qt,
                    "case": case,
                    "seed": _coerce_manifest_seed_from_string(seed),
                },
                "status": status,
                "relative_path": str(file_path.relative_to(run_dir)),
                "run_state_status": model_status,
                "reason": reason,
            }
            if extra:
                item["details"] = extra
            if status == STATUS_SUCCESS:
                pass
            items.append(item)

    report_summary = {
        "generated_at": _utc_now(),
        "run_dir": str(run_dir),
        "run_id": run_id,
        "run_type": "evaluation",
        "manifest_schema": EVAL_SPEC_SCHEMA,
        "counts": counts,
        "total_expected": len(expected_episodes) * len(model_names),
        "artifact_checks": {
            "manifest_valid": True,
            "state_exists": state is not None,
            "selection_dir_exists": True,
            "target_episode_count": len(expected_episodes),
            "model_count": len(model_names),
        },
    }

    report = {
        "schema": ARTIFACT_AUDIT_SCHEMA,
        "generated_at": _utc_now(),
        "run_type": "evaluation",
        "run_id": run_id,
        "run_dir": str(run_dir),
        "manifest_schema": EVAL_SPEC_SCHEMA,
        "summary": report_summary,
        "problems": problems,
        "items": items,
    }

    rerun_items: list[dict[str, Any]] = []
    for item in items:
        if _is_failure_status(item["status"]):
            scope = item["scope"]
            rerun_items.append(
                {
                    "model": scope["model"],
                    "filename": scope["filename"],
                    "qt": scope["qt"],
                    "case": scope["case"],
                    "seed": scope["seed"],
                    "status": item["status"],
                    "reason": item["reason"],
                }
            )

    rerun_items.sort(
        key=lambda item: (
            item["model"],
            _natural_sort_key(item["filename"]),
            item["seed"] if item["seed"] is not None else 0,
        )
    )

    rerun_plan = {
        "schema": ARTIFACT_AUDIT_SCHEMA,
        "generated_at": _utc_now(),
        "run_type": "evaluation",
        "run_id": run_id,
        "run_dir": str(run_dir),
        "rerun_command": _build_rerun_hint(run_dir, "evaluation"),
        "count": len(rerun_items),
        "items": rerun_items,
    }

    return report, rerun_plan


def _build_overall_status(report: dict[str, Any]) -> bool:
    counts = _require_mapping(report["summary"].get("counts"), "report.summary.counts")
    unknown_statuses = set(counts) - ALL_ARTIFACT_STATUSES
    if unknown_statuses:
        return False

    failures = 0
    for status in ARTIFACT_FAILURE_STATUSES:
        value = counts.get(status, 0)
        if isinstance(value, int):
            failures += value
    return failures == 0


def _parse_run_type(schema: str) -> str:
    if schema == GEN_SPEC_SCHEMA:
        return "generation"
    if schema == EVAL_SPEC_SCHEMA:
        return "evaluation"
    return "unknown"


def run_audit(
    *,
    run_dir: Path,
    run_type: str,
) -> tuple[dict[str, Any], dict[str, Any]]:
    if run_type not in {"auto", "generation", "evaluation"}:
        raise ValueError("type must be auto, generation, or evaluation")

    manifest = _load_run_directory_manifest(run_dir)
    schema = _safe_text(manifest.get("schema"))
    if not schema:
        raise ValueError("manifest.schema is missing")

    detected_type = _parse_run_type(schema)
    if run_type == "auto":
        if detected_type == "unknown":
            raise ValueError(f"unsupported manifest schema '{schema}'")
        run_type = detected_type
    elif run_type != detected_type:
        raise ValueError(
            f"requested type '{run_type}' but manifest schema is '{schema}', which is not supported for this type"
        )

    state = _load_run_state(run_dir)

    manifest_seed_path = manifest.get("spec_path")
    if isinstance(manifest_seed_path, str):
        spec_path = (
            run_dir / manifest_seed_path
            if not Path(manifest_seed_path).is_absolute()
            else Path(manifest_seed_path)
        )
        if not spec_path.exists():
            raise FileNotFoundError(f"copied spec not found: {spec_path}")
    else:
        raise ValueError("manifest.spec_path is missing or invalid")

    sha = _safe_text(manifest.get("spec_sha256"))
    if sha and _sha256_file(spec_path) != sha:
        raise ValueError(
            "manifest spec hash mismatch: manifest.spec_sha256 does not match copied spec"
        )

    if run_type == "generation":
        report, rerun_plan = _audit_generation(run_dir, manifest, state)
    else:
        report, rerun_plan = _audit_evaluation(run_dir, manifest, state)

    return report, rerun_plan


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Spec-driven run artifact audit")
    parser.add_argument("--run-dir", type=str, required=True)
    parser.add_argument(
        "--type", type=str, choices=["auto", "generation", "evaluation"], default="auto"
    )
    parser.add_argument("--report", type=str, default=DEFAULT_REPORT_FILE)
    parser.add_argument("--rerun-plan", type=str, default=DEFAULT_RERUN_PLAN_FILE)
    parser.add_argument(
        "--strict", action="store_true", help="exit non-zero if any item is not success"
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    run_dir = Path(args.run_dir).expanduser().resolve()
    if not run_dir.exists() or not run_dir.is_dir():
        print(f"[artifact-audit] ERROR: run directory not found: {run_dir}")
        return 1

    try:
        report, rerun_plan = run_audit(
            run_dir=run_dir,
            run_type=args.type,
        )
    except Exception as exc:  # pragma: no cover
        print(f"[artifact-audit] ERROR: {exc}")
        return 1

    report_path = (
        run_dir / args.report
        if not Path(args.report).is_absolute()
        else Path(args.report)
    )
    rerun_plan_path = (
        run_dir / args.rerun_plan
        if not Path(args.rerun_plan).is_absolute()
        else Path(args.rerun_plan)
    )

    _json_write(report_path, report)
    _json_write(rerun_plan_path, rerun_plan)

    failures = not _build_overall_status(report)
    status_word = "PASS" if not failures else "FAIL"
    print(
        f"[artifact-audit] {status_word}: {report['run_dir']} ({report['summary']['counts']})"
    )
    print(f"[artifact-audit] report -> {report_path}")
    print(f"[artifact-audit] rerun_plan -> {rerun_plan_path}")

    if failures and args.strict:
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
