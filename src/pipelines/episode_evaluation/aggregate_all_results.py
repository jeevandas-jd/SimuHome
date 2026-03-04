from __future__ import annotations

import argparse
import json
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List

from .aggregate_results import aggregate_results_for_dir


def aggregate_all_results_for_experiment(experiment_dir: str) -> Dict[str, Any]:
    root = Path(experiment_dir)
    if not root.exists():
        raise FileNotFoundError(f"Experiment directory not found: {root}")

    model_dirs: List[Path] = []
    for subdir in root.iterdir():
        if subdir.is_dir():
            json_files = list(subdir.glob("*.json"))
            if json_files:
                model_dirs.append(subdir)

    if not model_dirs:
        raise ValueError(f"No model directories with JSON files found in: {root}")

    print(f"Found {len(model_dirs)} model directories:")
    for model_dir in sorted(model_dirs):
        print(f"  - {model_dir.name}")

    all_models_results: Dict[str, Any] = {}
    overall_stats = {
        "total_models": 0,
        "total_evaluations": 0,
        "total_correct": 0,
        "model_accuracies": [],
    }

    for model_dir in sorted(model_dirs):
        model_name = model_dir.name

        try:
            model_summary = aggregate_results_for_dir(str(model_dir))
            all_models_results[model_name] = model_summary

            overall = model_summary.get("overall", {})
            total = overall.get("total", 0)
            correct = overall.get("correct", 0)
            accuracy = overall.get("accuracy", 0.0)

            overall_stats["total_models"] += 1
            overall_stats["total_evaluations"] += total
            overall_stats["total_correct"] += correct
            overall_stats["model_accuracies"].append(accuracy)

        except Exception as e:
            all_models_results[model_name] = {
                "error": str(e),
                "aggregated_at": datetime.now().isoformat(timespec="seconds"),
            }

    if overall_stats["total_evaluations"] > 0:
        overall_accuracy = (
            overall_stats["total_correct"] / overall_stats["total_evaluations"]
        )
    else:
        overall_accuracy = 0.0

    model_accuracies = overall_stats["model_accuracies"]
    if model_accuracies:
        avg_model_accuracy = sum(model_accuracies) / len(model_accuracies)
        max_model_accuracy = max(model_accuracies)
        min_model_accuracy = min(model_accuracies)
    else:
        avg_model_accuracy = max_model_accuracy = min_model_accuracy = 0.0

    result = {
        "aggregated_at": datetime.now().isoformat(timespec="seconds"),
        "experiment_dir": str(experiment_dir),
        "summary": {
            "total_models": overall_stats["total_models"],
            "total_evaluations": overall_stats["total_evaluations"],
            "total_correct": overall_stats["total_correct"],
            "overall_accuracy": round(overall_accuracy, 4),
            "avg_model_accuracy": round(avg_model_accuracy, 4),
            "max_model_accuracy": round(max_model_accuracy, 4),
            "min_model_accuracy": round(min_model_accuracy, 4),
        },
        "models": all_models_results,
    }

    return result


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Aggregate evaluation results from all model directories in an experiment"
    )
    parser.add_argument(
        "--experiment_dir",
        type=str,
        required=True,
        help="Path to experiment directory containing model subdirectories",
    )
    args = parser.parse_args()

    summary = aggregate_all_results_for_experiment(args.experiment_dir)

    out_path = Path(args.experiment_dir) / "aggregate_all_summary.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)

    with out_path.open("w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()
