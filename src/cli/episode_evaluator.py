from __future__ import annotations

import re
import os
import argparse
import json
from pathlib import Path
from typing import List, Dict, Any, Callable, TypedDict
from datetime import datetime

from src.cli.arg_utils import parse_integer_spec
from src.agents.providers.base import (
    EmptyLLMResponseError,
    LLMRetryExhaustedError,
    NonRetryableLLMError,
)
from src.pipelines.episode_evaluation.runner import run_single_config
from src.agents.providers import LLMProvider, OpenAIChatProvider


class ProgressEvent(TypedDict, total=False):
    kind: str
    model: str
    safe_model: str
    run_id: str
    attempt: int
    total: int
    initial_completed: int
    pending: int
    processed: int
    success: int
    failed: int
    episode: str
    message: str


class EvaluationStats(TypedDict):
    total: int
    initial_completed: int
    pending: int
    processed: int
    success: int
    failed: int


ProgressEmitter = Callable[[ProgressEvent], None]


_MODEL_OUTPUT_FORMAT_MARKERS = (
    "invalid structured output",
    "action_input string is not valid json",
    "structured output must be a json object",
    "action must be a non-empty string",
    "invalid action_input type",
)

_CONTEXT_OVERFLOW_MARKERS = (
    "context window exceeded",
    "maximum context length",
    "parameter=input_tokens",
    "input_tokens",
    "reduce the length of the input messages",
)

_NETWORK_ERROR_MARKERS = (
    "network",
    "connection refused",
    "connection reset",
    "failed to establish a new connection",
    "temporary failure in name resolution",
    "name or service not known",
    "timed out",
    "timeout",
    "readtimeout",
    "connecterror",
)


def _contains_any_marker(text: str, markers: tuple[str, ...]) -> bool:
    return any(marker in text for marker in markers)


def _classify_runtime_failure(
    exc: Exception,
) -> tuple[int, str, str, bool]:
    message = str(exc).strip()
    lowered = message.lower()

    if _contains_any_marker(lowered, _CONTEXT_OVERFLOW_MARKERS):
        return -1, "Context Overflow", "infra", False

    if isinstance(exc, EmptyLLMResponseError):
        return -1, "LLM Empty Response", "infra", False

    if isinstance(exc, LLMRetryExhaustedError):
        return -1, "LLM Retry Exhausted", "infra", False

    if _contains_any_marker(lowered, _MODEL_OUTPUT_FORMAT_MARKERS):
        return 0, "Model Output Format Error", "model", True

    if "empty model response" in lowered:
        return -1, "LLM Empty Response", "infra", False

    if _contains_any_marker(lowered, _NETWORK_ERROR_MARKERS):
        return -1, "Network Error", "infra", False

    if "server health check failed" in lowered:
        return -1, "Simulator Unavailable", "infra", False

    if isinstance(exc, NonRetryableLLMError):
        return -1, "LLM Request Rejected", "infra", False

    return -1, "Evaluation Runtime Error", "infra", False


def get_safe_model_name(original_model: str) -> str:
    """Remove filesystem-unsafe characters from model names"""
    return original_model.replace("/", "_").replace(":", "_")


def _run_output_root(output_root: str, run_id: str, model: str) -> Path:
    safe_model_name = get_safe_model_name(str(model))
    return Path(output_root) / run_id / safe_model_name


def _output_path_for_config(
    cfg_path: Path, output_root: str, run_id: str, model: str
) -> Path:
    return _run_output_root(output_root, run_id, model) / cfg_path.name


def _is_valid_existing_result(path: Path) -> bool:
    if not path.exists() or not path.is_file():
        return False

    try:
        with path.open("r", encoding="utf-8") as f:
            payload = json.load(f)
    except Exception:
        return False

    if not isinstance(payload, dict):
        return False

    evaluation_result = payload.get("evaluation_result")
    if not isinstance(evaluation_result, dict):
        return False

    error_type = evaluation_result.get("error_type")
    if isinstance(error_type, str) and error_type.strip():
        return False

    score = evaluation_result.get("score")
    if not isinstance(score, (int, float)):
        return False
    if float(score) < 0:
        return False

    return True


def _write_json_atomic(path: Path, payload: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temp_path = path.with_suffix(path.suffix + ".tmp")
    with temp_path.open("w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
        f.flush()
        os.fsync(f.fileno())
    temp_path.replace(path)


def _filter_pending_configs(
    config_paths: List[Path], output_root: str, run_id: str, model: str
) -> tuple[List[Path], int]:
    pending: List[Path] = []
    skipped = 0

    for cfg_path in config_paths:
        out_path = _output_path_for_config(cfg_path, output_root, run_id, model)
        if _is_valid_existing_result(out_path):
            skipped += 1
            continue
        pending.append(cfg_path)

    return pending, skipped


def _discover_all_query_configs(root: Path) -> List[Path]:
    """Discover all JSON config files in the root directory."""

    def natural_sort_key(path: Path) -> tuple[Any, ...]:
        """Natural sort key for filenames with numbers."""
        parts = re.split(r"(\d+)", path.name)
        return tuple(int(part) if part.isdigit() else part for part in parts)

    return sorted(root.glob("*.json"), key=natural_sort_key)


def _discover_config_by_pattern(root: Path, qt: str, case: str, seed: int) -> Path:
    """Discover single config file matching specific qt, case, and seed pattern."""
    filename = f"{qt}_{case}_seed_{seed}.json"
    cfg_path = root / filename
    if not cfg_path.exists():
        raise FileNotFoundError(f"Config file not found: {cfg_path}")
    return cfg_path


def _build_error_record(
    *,
    cfg_path: Path,
    model: str,
    strategy: str,
    error_type: str,
    message: str,
    score: int,
    error_category: str,
    attempted: bool,
) -> Dict[str, Any]:
    with cfg_path.open("r", encoding="utf-8") as f:
        episode = json.load(f)

    meta = episode.get("meta") if isinstance(episode, dict) else {}
    if not isinstance(meta, dict):
        meta = {}

    return {
        "seed": meta.get("seed"),
        "query_type": str(meta.get("query_type") or ""),
        "case": str(meta.get("case") or ""),
        "model": model,
        "strategy": strategy,
        "config_path": str(cfg_path),
        "query": str(episode.get("query") or ""),
        "duration": 0.0,
        "evaluation_result": {
            "score": score,
            "error_type": error_type,
            "error_category": error_category,
            "attempted": attempted,
            "required_actions": [],
            "judge": [],
            "detail": message,
        },
        "tools_invoked": [],
        "steps": [],
        "trace_type": strategy,
    }


def _get_valid_cases_for_qt(qt: str) -> List[str]:
    """Get valid cases for a given query type."""
    qt_cases = {
        "qt1": ["feasible", "infeasible"],
        "qt2": ["feasible", "infeasible"],
        "qt3": ["feasible", "infeasible"],
        "qt4-1": ["feasible", "infeasible"],
        "qt4-2": ["feasible", "infeasible"],
        "qt4-3": ["feasible", "infeasible"],
    }
    return qt_cases.get(qt, [])


def create_argument_parser() -> argparse.ArgumentParser:
    """Create and configure argument parser."""
    parser = argparse.ArgumentParser(description="Virtual SmartHome - Agent Evaluator")

    parser.add_argument(
        "--model", type=str, required=True, help="Model name for LLM API calls"
    )
    parser.add_argument(
        "--api-base",
        type=str,
        required=True,
        help="Override provider API base (OpenAI-compatible endpoint)",
    )
    parser.add_argument(
        "--api-key",
        type=str,
        required=True,
        help="Override provider API key/token",
    )
    parser.add_argument(
        "--judge-model",
        type=str,
        required=True,
        help="Judge model used for evaluation",
    )
    parser.add_argument(
        "--judge-api-base",
        type=str,
        required=True,
        help="Judge API base endpoint",
    )
    parser.add_argument(
        "--judge-api-key",
        type=str,
        required=True,
        help="Judge API key/token",
    )
    parser.add_argument(
        "--agent",
        type=str,
        default="react",
        choices=["react", "hi_agent"],
        help="Agent strategy to run",
    )
    parser.add_argument(
        "--output-model",
        type=str,
        help="Model name for output directory (defaults to --model)",
    )
    parser.add_argument(
        "--qt",
        type=str,
        choices=["qt1", "qt2", "qt3", "qt4-1", "qt4-2", "qt4-3"],
        help="Query type for single run",
    )
    parser.add_argument("--case", type=str, help="Case type for single run")
    parser.add_argument(
        "--seed",
        type=str,
        help="Seed(s) for single/batch run: '1', '1,2,3', '1-5', '1,3,5-10'",
    )

    parser.add_argument(
        "--base_url",
        type=str,
        default="http://127.0.0.1:8000/api",
        help="Server API base URL",
    )
    parser.add_argument(
        "--timeout", type=float, default=30.0, help="HTTP timeout (seconds)"
    )
    parser.add_argument(
        "--temperature", type=float, default=0.5, help="LLM temperature"
    )
    parser.add_argument(
        "--max_steps",
        type=int,
        default=20,
        help="Max reasoning steps / LLM turns",
    )

    parser.add_argument(
        "--episode_dir",
        type=str,
        default="data/benchmark",
        help="Episode directory containing config files",
    )
    parser.add_argument(
        "--judge-count",
        type=int,
        default=3,
        help="Number of judge LLM instances to use (strict policy: exactly 3)",
    )
    parser.add_argument(
        "--skip-existing",
        action="store_true",
        help="Skip episodes that already have a valid output JSON",
    )
    parser.add_argument(
        "--output-root",
        type=str,
        default="experiments",
        help="Root directory for evaluation outputs",
    )

    return parser


def validate_arguments(args: argparse.Namespace) -> None:
    """Validate command line arguments."""
    if args.judge_count != 3:
        raise ValueError("--judge-count must be exactly 3 for majority voting")

    single_mode_args = [args.qt, args.case, args.seed]
    single_mode = any(single_mode_args)

    if single_mode:
        if not all(single_mode_args):
            raise ValueError(
                "When using specific evaluation, --qt, --case, and --seed must all be provided"
            )

        valid_cases = _get_valid_cases_for_qt(args.qt)
        if args.case not in valid_cases:
            raise ValueError(
                f"Invalid case '{args.case}' for query type '{args.qt}'. Valid cases: {valid_cases}"
            )

        try:
            parse_integer_spec(args.seed)
        except ValueError as e:
            raise ValueError(
                f"Invalid seed format: {args.seed}. Expected format: '1', '1,2,3', '1-5', etc."
            ) from e


def _emit_progress(emit: ProgressEmitter | None, event: ProgressEvent) -> None:
    if emit is None:
        return
    emit(event)


def evaluate_episodes(
    *,
    model: str,
    output_model: str,
    agent: str,
    base_url: str,
    timeout: float,
    temperature: float,
    max_steps: int,
    episode_dir: str,
    qt: str | None,
    case: str | None,
    seed: str | None,
    judge_count: int,
    skip_existing: bool,
    output_root: str,
    run_id: str,
    api_key: str,
    api_base: str,
    judge_model: str,
    judge_api_base: str,
    judge_api_key: str,
    emit: ProgressEmitter | None = None,
) -> EvaluationStats:
    episode_dir_path = Path(episode_dir)
    if not episode_dir_path.exists():
        raise FileNotFoundError(f"Episode directory does not exist: {episode_dir_path}")

    config_paths: List[Path]
    if qt and case and seed:
        seeds = parse_integer_spec(seed)
        config_paths = []
        for seed_value in seeds:
            try:
                config_path = _discover_config_by_pattern(
                    episode_dir_path,
                    qt,
                    case,
                    seed_value,
                )
                config_paths.append(config_path)
            except FileNotFoundError:
                _emit_progress(
                    emit,
                    {
                        "kind": "log",
                        "message": f"Config file not found for seed {seed_value}, skipping.",
                    },
                )
                continue
    else:
        config_paths = _discover_all_query_configs(episode_dir_path)
        if not config_paths:
            raise FileNotFoundError(
                f"No config JSON files found in '{episode_dir_path}'"
            )

    total_episode_count = len(config_paths)
    initial_completed = 0
    if skip_existing:
        config_paths, skipped_count = _filter_pending_configs(
            config_paths,
            output_root,
            run_id,
            output_model,
        )
        initial_completed = skipped_count

    pending_count = len(config_paths)
    _emit_progress(
        emit,
        {
            "kind": "init",
            "total": total_episode_count,
            "initial_completed": initial_completed,
            "pending": pending_count,
        },
    )

    if pending_count == 0:
        return {
            "total": total_episode_count,
            "initial_completed": initial_completed,
            "pending": 0,
            "processed": 0,
            "success": 0,
            "failed": 0,
        }

    main_llm = OpenAIChatProvider(
        model=model,
        temperature=temperature,
        seed=42,
        api_key=api_key,
        api_base=api_base,
        timeout=timeout,
    )

    judge_llms: List[LLMProvider] = []
    for index in range(judge_count):
        judge_llms.append(
            OpenAIChatProvider(
                model=judge_model,
                temperature=temperature,
                seed=42 + index,
                api_key=judge_api_key,
                api_base=judge_api_base,
                timeout=timeout,
            )
        )

    processed = 0
    success_count = 0
    failed_count = 0

    for cfg_path in config_paths:
        out_path = _output_path_for_config(cfg_path, output_root, run_id, output_model)
        try:
            record = run_single_config(
                cfg_path=str(cfg_path),
                base_url=base_url,
                timeout=float(timeout),
                max_steps=int(max_steps),
                agent_strategy=agent,
                main_llm=main_llm,
                judge_llms=judge_llms,
            )
            _write_json_atomic(out_path, record)
            success_count += 1
        except Exception as exc:
            score, error_type, error_category, attempted = _classify_runtime_failure(
                exc
            )
            error_record = _build_error_record(
                cfg_path=cfg_path,
                model=model,
                strategy=str(agent),
                error_type=error_type,
                message=str(exc),
                score=score,
                error_category=error_category,
                attempted=attempted,
            )
            _write_json_atomic(out_path, error_record)
            failed_count += 1
            _emit_progress(
                emit,
                {
                    "kind": "error",
                    "episode": cfg_path.name,
                    "message": f"Failed to evaluate {cfg_path.name}: {exc}",
                },
            )
        finally:
            processed += 1
            _emit_progress(
                emit,
                {
                    "kind": "advance",
                    "episode": cfg_path.name,
                    "processed": processed,
                    "success": success_count,
                    "failed": failed_count,
                    "total": total_episode_count,
                    "initial_completed": initial_completed,
                },
            )

    return {
        "total": total_episode_count,
        "initial_completed": initial_completed,
        "pending": pending_count,
        "processed": processed,
        "success": success_count,
        "failed": failed_count,
    }


def _cli_progress_emitter(event: ProgressEvent) -> None:
    kind = str(event.get("kind", "")).strip()
    if kind == "init":
        total = int(event.get("total", 0))
        initial_completed = int(event.get("initial_completed", 0))
        pending = int(event.get("pending", 0))
        print(
            f"[EpisodeEvaluator] Progress: {initial_completed}/{total} completed, {pending} remaining"
        )
        return

    if kind in {"log", "error"}:
        message = event.get("message")
        if isinstance(message, str) and message.strip():
            print(message)


def main() -> None:
    parser = create_argument_parser()
    args = parser.parse_args()

    if not args.output_model:
        args.output_model = args.model

    run_id = os.getenv("EVAL_TIMESTAMP")
    if not run_id:
        run_id = datetime.now().strftime("%Y%m%d%H%M%S")

    validate_arguments(args)

    stats = evaluate_episodes(
        model=str(args.model),
        output_model=str(args.output_model),
        agent=str(args.agent),
        base_url=str(args.base_url),
        timeout=float(args.timeout),
        temperature=float(args.temperature),
        max_steps=int(args.max_steps),
        episode_dir=str(args.episode_dir),
        qt=str(args.qt) if args.qt else None,
        case=str(args.case) if args.case else None,
        seed=str(args.seed) if args.seed else None,
        judge_count=int(args.judge_count),
        skip_existing=bool(args.skip_existing),
        output_root=str(args.output_root),
        run_id=run_id,
        api_key=str(args.api_key),
        api_base=str(args.api_base),
        judge_model=str(args.judge_model),
        judge_api_base=str(args.judge_api_base),
        judge_api_key=str(args.judge_api_key),
        emit=_cli_progress_emitter,
    )

    print(
        "[EpisodeEvaluator] Done: "
        f"processed={stats['processed']} success={stats['success']} failed={stats['failed']} "
        f"(initial_completed={stats['initial_completed']}, total={stats['total']})"
    )


if __name__ == "__main__":
    main()
