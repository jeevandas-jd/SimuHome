from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path
from typing import List


RELEVANT_PATH_PREFIXES = (
    "src/simulator/domain/aggregators/",
    "src/simulator/domain/devices/",
    "src/simulator/domain/clusters/",
    "src/simulator/domain/home.py",
    "src/simulator/application/home_initializer.py",
    "src/simulator/api/routes.py",
    "src/clients/smarthome_client.py",
)


def _run_git(cwd: Path, args: List[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        cwd=cwd,
        capture_output=True,
        text=True,
        check=False,
    )


def _is_git_repo(cwd: Path) -> bool:
    result = _run_git(cwd, ["rev-parse", "--is-inside-work-tree"])
    return result.returncode == 0 and result.stdout.strip() == "true"


def _collect_changed_files(
    cwd: Path,
    *,
    staged_only: bool,
    base_ref: str | None,
) -> List[str]:
    changed: set[str] = set()

    if staged_only:
        staged = _run_git(cwd, ["diff", "--cached", "--name-only"])
        if staged.returncode == 0:
            changed.update(line.strip() for line in staged.stdout.splitlines() if line)
    else:
        unstaged = _run_git(cwd, ["diff", "--name-only"])
        staged = _run_git(cwd, ["diff", "--cached", "--name-only"])
        if unstaged.returncode == 0:
            changed.update(
                line.strip() for line in unstaged.stdout.splitlines() if line
            )
        if staged.returncode == 0:
            changed.update(line.strip() for line in staged.stdout.splitlines() if line)

    if base_ref:
        base_diff = _run_git(cwd, ["diff", "--name-only", f"{base_ref}...HEAD"])
        if base_diff.returncode == 0:
            changed.update(
                line.strip() for line in base_diff.stdout.splitlines() if line
            )

    return sorted(changed)


def _is_relevant_change(path: str) -> bool:
    return any(
        path == prefix or path.startswith(prefix) for prefix in RELEVANT_PATH_PREFIXES
    )


def _run_guard_suite(cwd: Path) -> int:
    command = [
        sys.executable,
        "-m",
        "unittest",
        "src.cli.sim_parity_guard_tests",
        "-v",
    ]
    result = subprocess.run(command, cwd=cwd, check=False)
    return int(result.returncode)


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Run simulator parity guard automatically when simulator/runtime core files change."
        )
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Run parity guard regardless of changed files.",
    )
    parser.add_argument(
        "--staged-only",
        action="store_true",
        help="Consider only staged changes (useful for pre-commit hooks).",
    )
    parser.add_argument(
        "--base-ref",
        default=None,
        help="Optional git base reference to include in changed-file detection.",
    )

    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parents[2]
    in_git_repo = _is_git_repo(repo_root)

    if not args.force and in_git_repo:
        changed_files = _collect_changed_files(
            repo_root,
            staged_only=bool(args.staged_only),
            base_ref=args.base_ref,
        )
        relevant = [path for path in changed_files if _is_relevant_change(path)]
        if not relevant:
            print("[sim-parity-guard] SKIP: no simulator/runtime core changes detected")
            return 0

        print("[sim-parity-guard] Relevant changes detected:")
        for path in relevant:
            print(f"  - {path}")
    elif not in_git_repo:
        print("[sim-parity-guard] Git metadata unavailable; running guard suite")
    else:
        print("[sim-parity-guard] Forced run")

    code = _run_guard_suite(repo_root)
    if code == 0:
        print("[sim-parity-guard] PASS")
    else:
        print("[sim-parity-guard] FAIL")
    return code


if __name__ == "__main__":
    raise SystemExit(main())
