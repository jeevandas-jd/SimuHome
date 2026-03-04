from __future__ import annotations

import argparse
import json
import math
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Tuple


_INFRA_ERROR_TYPES = {
    "Judge Error",
    "Judge Configuration Error",
    "Evaluation Runtime Error",
    "Context Overflow",
    "Network Error",
    "Simulator Unavailable",
    "LLM Request Rejected",
    "LLM Empty Response",
}

_MODEL_ERROR_TYPES = {
    "Model Output Format Error",
}


def _is_infra_error(evaluation_result: Dict[str, Any], score: int) -> bool:
    error_category_raw = evaluation_result.get("error_category")
    error_category = str(error_category_raw or "").strip().lower()
    if error_category == "infra":
        return True
    if error_category == "model":
        return False

    attempted_raw = evaluation_result.get("attempted")
    if isinstance(attempted_raw, bool) and not attempted_raw:
        return True

    error_type = str(evaluation_result.get("error_type") or "").strip()
    if error_type in _MODEL_ERROR_TYPES:
        return False
    if error_type in _INFRA_ERROR_TYPES:
        return True

    return score == -1


@dataclass
class _Bucket:
    total: int = 0
    evaluated_total: int = 0
    correct: int = 0
    infra_errors: int = 0
    schema_errors: int = 0
    scores: List[int] = field(default_factory=list)
    binary_scores: List[int] = field(default_factory=list)
    durations: List[float] = field(default_factory=list)
    actions: List[int] = field(default_factory=list)

    def add(
        self,
        score: int,
        duration: float,
        actions: int,
        *,
        is_infra_error: bool = False,
        is_schema_error: bool = False,
    ) -> None:
        self.total += 1
        score_int = int(score)
        self.scores.append(score_int)
        self.durations.append(float(duration))
        self.actions.append(int(actions))

        if is_schema_error:
            self.schema_errors += 1
            return

        if is_infra_error:
            self.infra_errors += 1
            return

        self.evaluated_total += 1
        binary_score = 1 if score_int == 1 else 0
        if binary_score == 1:
            self.correct += 1
        self.binary_scores.append(binary_score)

    def _calculate_std(self, values: List[float]) -> float:
        if len(values) <= 1:
            return 0.0
        mean = sum(values) / len(values)
        variance = sum((x - mean) ** 2 for x in values) / len(values)
        return math.sqrt(variance)

    def to_summary(self) -> Dict[str, Any]:
        if self.total <= 0:
            return {
                "total": 0,
                "evaluated_total": 0,
                "infra_errors": 0,
                "schema_errors": 0,
                "infra_error_rate": 0.00,
                "schema_error_rate": 0.00,
                "correct": 0,
                "accuracy": 0.00,
                "accuracy_denominator": "evaluated_total",
                "accuracy_std": 0.00,
                "avg_duration_sec": 0.00,
                "duration_std": 0.00,
                "avg_actions": 0.00,
                "actions_std": 0.00,
            }

        accuracy = (
            self.correct / self.evaluated_total if self.evaluated_total > 0 else 0.0
        )
        avg_duration = sum(self.durations) / self.total
        avg_actions = sum(self.actions) / self.total
        infra_error_rate = self.infra_errors / self.total
        schema_error_rate = self.schema_errors / self.total

        accuracy_std = self._calculate_std([float(s) for s in self.binary_scores])
        duration_std = self._calculate_std(self.durations)
        actions_std = self._calculate_std([float(a) for a in self.actions])

        return {
            "total": int(self.total),
            "evaluated_total": int(self.evaluated_total),
            "infra_errors": int(self.infra_errors),
            "schema_errors": int(self.schema_errors),
            "infra_error_rate": round(infra_error_rate, 4),
            "schema_error_rate": round(schema_error_rate, 4),
            "correct": int(self.correct),
            "accuracy": round(accuracy, 4),
            "accuracy_denominator": "evaluated_total",
            "accuracy_std": round(accuracy_std, 4),
            "avg_duration_sec": round(avg_duration, 2),
            "duration_std": round(duration_std, 2),
            "avg_actions": round(avg_actions, 2),
            "actions_std": round(actions_std, 2),
        }


def _read_json(path: Path) -> Tuple[Dict[str, Any] | None, str | None]:
    try:
        with path.open("r", encoding="utf-8") as f:
            return json.load(f), None
    except Exception as e:
        return None, str(e)


def _infer_from_filename(path: Path) -> Tuple[str | None, str | None]:
    name = path.stem
    try:
        if not name.startswith("qt"):
            return None, None
        parts = name.split("_")
        if len(parts) < 4:
            return None, None
        qt = parts[0]
        case = parts[1]
        return qt, case
    except Exception:
        return None, None


def _count_actions(steps: List[Dict[str, Any]] | None) -> int:
    if not isinstance(steps, list):
        return 0
    cnt = 0
    for s in steps:
        a = (s or {}).get("action")
        if a and str(a).lower() != "finish":
            cnt += 1
    return cnt


def _extract_steps(data: Dict[str, Any]) -> List[Dict[str, Any]]:
    steps = data.get("steps")
    if not isinstance(steps, list):
        raise ValueError("result JSON must contain steps list in current format")
    return steps


def aggregate_results_for_dir(result_dir: str) -> Dict[str, Any]:
    root = Path(result_dir)
    if not root.exists():
        raise FileNotFoundError(f"Directory not found: {root}")

    files = sorted(
        [p for p in root.glob("*.json") if p.name != "aggregate_summary.json"]
    )

    buckets: Dict[str, Dict[str, _Bucket]] = {}
    overall = _Bucket()
    skipped: List[Dict[str, str]] = []

    for path in files:
        data, err = _read_json(path)
        if data is None:
            skipped.append({"path": str(path), "reason": f"invalid json: {err}"})
            continue

        qt = str(data.get("query_type") or "").strip().lower()
        case = str(data.get("case") or "").strip().lower()
        if not qt or not case:
            fname_qt, fname_case = _infer_from_filename(path)
            qt = qt or (fname_qt or "")
            case = case or (fname_case or "")
        if not qt or not case:
            skipped.append({"path": str(path), "reason": "missing query_type/case"})
            continue

        evaluation_result = data.get("evaluation_result") or {}
        if not isinstance(evaluation_result, dict):
            skipped.append(
                {
                    "path": str(path),
                    "reason": "invalid evaluation_result schema: expected dict",
                }
            )
            continue

        score = 0
        try:
            score = int((evaluation_result.get("score") or 0))
        except Exception:
            score = 0
        is_infra_error = _is_infra_error(evaluation_result, score)

        try:
            duration = float(data.get("duration") or 0.0)
        except Exception:
            duration = 0.0

        is_schema_error = False
        try:
            actions = _count_actions(_extract_steps(data))
        except Exception:
            actions = 0
            is_schema_error = True

        if qt not in buckets:
            buckets[qt] = {}
        if case not in buckets[qt]:
            buckets[qt][case] = _Bucket()

        buckets[qt][case].add(
            score,
            duration,
            actions,
            is_infra_error=is_infra_error,
            is_schema_error=is_schema_error,
        )
        overall.add(
            score,
            duration,
            actions,
            is_infra_error=is_infra_error,
            is_schema_error=is_schema_error,
        )

    by_qt: Dict[str, Any] = {}
    for qt, cases in buckets.items():
        qt_total = _Bucket()
        qt_entry: Dict[str, Any] = {}

        case_names = sorted(cases.keys())

        for case_name in case_names:
            b = cases[case_name]
            qt_entry[case_name] = b.to_summary()
            qt_total.total += b.total
            qt_total.evaluated_total += b.evaluated_total
            qt_total.infra_errors += b.infra_errors
            qt_total.schema_errors += b.schema_errors
            qt_total.correct += b.correct
            qt_total.scores.extend(b.scores)
            qt_total.binary_scores.extend(b.binary_scores)
            qt_total.durations.extend(b.durations)
            qt_total.actions.extend(b.actions)
        qt_entry["total"] = qt_total.to_summary()
        by_qt[qt] = qt_entry

    out: Dict[str, Any] = {
        "aggregated_at": datetime.now().isoformat(timespec="seconds"),
        "result_dir": str(result_dir),
        "overall": overall.to_summary(),
        "by_query_type": by_qt,
        "skipped_files": skipped,
    }
    return out


def main() -> None:
    p = argparse.ArgumentParser(
        description="Aggregate evaluation results from a directory"
    )
    p.add_argument(
        "--result_dir",
        type=str,
        required=True,
        help="Path to directory containing evaluation result JSON files",
    )
    args = p.parse_args()

    summary = aggregate_results_for_dir(args.result_dir)

    out_path = Path(args.result_dir) / "aggregate_summary.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)

    print(f"Aggregation completed: {out_path}")


if __name__ == "__main__":
    main()
