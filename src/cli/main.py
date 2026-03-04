from __future__ import annotations

import argparse
import os
import shutil
import stat
import subprocess
import sys
import time
from pathlib import Path
from urllib.error import URLError
from urllib.request import urlopen

from src.cli import artifact_audit


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def _default_port() -> int:
    raw = os.getenv("PORT", "8000")
    return int(raw)


def _health_endpoint(host: str, port: int, endpoint: str | None) -> str:
    if endpoint:
        return endpoint
    return f"http://{host}:{port}/api/__health__"


def _run_module(
    module: str, args: list[str], env_overrides: dict[str, str] | None = None
) -> int:
    env = os.environ.copy()
    if env_overrides:
        env.update(env_overrides)
    command = [sys.executable, "-m", module, *args]
    completed = subprocess.run(command, cwd=_repo_root(), check=False, env=env)
    return int(completed.returncode)


def _check_health(url: str, timeout: float = 2.0) -> bool:
    try:
        with urlopen(url, timeout=timeout) as response:
            status = getattr(response, "status", 200)
            return 200 <= int(status) < 300
    except URLError:
        return False
    except TimeoutError:
        return False


def _handle_health(args: argparse.Namespace) -> int:
    endpoint = _health_endpoint(args.host, args.port, args.endpoint)
    if _check_health(endpoint, timeout=2.0):
        print("[health] OK")
        return 0
    print("[health] FAIL")
    return 1


def _handle_server_stop(args: argparse.Namespace) -> int:
    print("[server] Stopping servers...")
    return _run_module("src.cli.stop_servers", [], {"PORT": str(args.port)})


def _handle_server_start(args: argparse.Namespace) -> int:
    server_out = _repo_root() / "server.out"
    endpoint = _health_endpoint(args.host, args.port, args.endpoint)
    command = [sys.executable, "-m", "src.simulator.api.app"]
    print(f"[server] Starting: {' '.join(command)} (port {args.port})")
    with server_out.open("w", encoding="utf-8") as out_file:
        subprocess.Popen(
            command,
            cwd=_repo_root(),
            stdout=out_file,
            stderr=subprocess.STDOUT,
            env={**os.environ, "SERVER_PORT": str(args.port)},
            start_new_session=True,
        )
    time.sleep(1)
    if _check_health(endpoint, timeout=2.0):
        print("[server] Started")
        return 0
    print(
        "[server] Failed to start. "
        f"Check logs at {server_out} and retry with: uv run simuhome server-start --port {args.port}"
    )
    return 1


def _handle_server_restart(args: argparse.Namespace) -> int:
    stop_code = _handle_server_stop(args)
    if stop_code != 0:
        return stop_code
    return _handle_server_start(args)


def _handle_server_ensure(args: argparse.Namespace) -> int:
    endpoint = _health_endpoint(args.host, args.port, args.endpoint)
    if _check_health(endpoint, timeout=2.0):
        print("[server] Already running")
        return 0
    return _handle_server_start(args)


def _handle_logs(args: argparse.Namespace) -> int:
    server_out = _repo_root() / "server.out"
    print(f"[logs] tail -n {args.lines} {server_out.name}")
    if not server_out.exists():
        return 0
    lines = server_out.read_text(encoding="utf-8", errors="replace").splitlines()
    for line in lines[-args.lines :]:
        print(line)
    return 0


def _handle_episode(args: argparse.Namespace) -> int:
    return _run_module("src.cli.episode_generator", ["--spec", args.spec])


def _handle_episode_resume(args: argparse.Namespace) -> int:
    return _run_module("src.cli.episode_generator", ["--resume", args.resume])


def _handle_eval_start(args: argparse.Namespace) -> int:
    return _run_module("src.cli.parallel_model_evaluation", ["--spec", args.spec])


def _handle_eval_resume(args: argparse.Namespace) -> int:
    return _run_module("src.cli.parallel_model_evaluation", ["--resume", args.resume])


def _handle_aggregate(args: argparse.Namespace) -> int:
    return _run_module(
        "src.pipelines.episode_evaluation.aggregate_results",
        ["--result_dir", args.dir],
    )


def _handle_aggregate_all(args: argparse.Namespace) -> int:
    return _run_module(
        "src.pipelines.episode_evaluation.aggregate_all_results",
        ["--experiment_dir", args.dir],
    )


def _handle_verify_sim_parity(args: argparse.Namespace) -> int:
    command_args: list[str] = []
    if args.force:
        command_args.append("--force")
    return _run_module("src.cli.sim_parity_guard", command_args)


def _handle_install_local_hooks(_args: argparse.Namespace) -> int:
    repo_root = _repo_root()
    hooks_dir = repo_root / ".git" / "hooks"
    src_hook = repo_root / ".githooks" / "pre-commit"
    dst_hook = hooks_dir / "pre-commit"
    if not hooks_dir.exists():
        print("[install-local-hooks] .git/hooks not found")
        return 1
    shutil.copy2(src_hook, dst_hook)
    mode = dst_hook.stat().st_mode
    dst_hook.chmod(mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
    print("[install-local-hooks] Installed .git/hooks/pre-commit")
    return 0


def _handle_artifact_audit(args: argparse.Namespace) -> int:
    cli_args = [
        "--run-dir",
        args.run_dir,
        "--type",
        args.type,
        "--report",
        args.report,
        "--rerun-plan",
        args.rerun_plan,
    ]
    if args.strict:
        cli_args.append("--strict")
    return artifact_audit.main(cli_args)


def _add_server_shared(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--host", type=str, default="127.0.0.1")
    parser.add_argument("--port", type=int, default=_default_port())
    parser.add_argument("--endpoint", type=str, default=None)


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="simuhome", description="SimuHome unified command-line interface"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    health = subparsers.add_parser("health", help="Check server health")
    _add_server_shared(health)
    health.set_defaults(handler=_handle_health)

    server_start = subparsers.add_parser("server-start", help="Start server")
    _add_server_shared(server_start)
    server_start.set_defaults(handler=_handle_server_start)

    server_stop = subparsers.add_parser("server-stop", help="Stop server")
    server_stop.add_argument("--port", type=int, default=_default_port())
    server_stop.set_defaults(handler=_handle_server_stop)

    server_restart = subparsers.add_parser("server-restart", help="Restart server")
    _add_server_shared(server_restart)
    server_restart.set_defaults(handler=_handle_server_restart)

    server_ensure = subparsers.add_parser(
        "server-ensure", help="Ensure server is running"
    )
    _add_server_shared(server_ensure)
    server_ensure.set_defaults(handler=_handle_server_ensure)

    logs = subparsers.add_parser("logs", help="Show server logs")
    logs.add_argument("--lines", type=int, default=100)
    logs.set_defaults(handler=_handle_logs)

    episode = subparsers.add_parser(
        "episode", help="Start spec-driven episode generation"
    )
    episode.add_argument("--spec", type=str, required=True)
    episode.set_defaults(handler=_handle_episode)

    episode_resume = subparsers.add_parser(
        "episode-resume", help="Resume spec-driven episode generation run"
    )
    episode_resume.add_argument("--resume", type=str, required=True)
    episode_resume.set_defaults(handler=_handle_episode_resume)

    eval_start = subparsers.add_parser(
        "eval-start", help="Start spec-driven evaluation"
    )
    eval_start.add_argument("--spec", type=str, required=True)
    eval_start.set_defaults(handler=_handle_eval_start)

    eval_resume = subparsers.add_parser("eval-resume", help="Resume evaluation run")
    eval_resume.add_argument("--resume", type=str, required=True)
    eval_resume.set_defaults(handler=_handle_eval_resume)

    artifact_audit_cmd = subparsers.add_parser(
        "artifact-audit", help="Audit generated/evaluated artifacts and emit rerun plan"
    )
    artifact_audit_cmd.add_argument("--run-dir", type=str, required=True)
    artifact_audit_cmd.add_argument(
        "--type", type=str, choices=["auto", "generation", "evaluation"], default="auto"
    )
    artifact_audit_cmd.add_argument("--report", type=str, default="artifact_audit.json")
    artifact_audit_cmd.add_argument(
        "--rerun-plan", type=str, default="artifact_rerun_plan.json"
    )
    artifact_audit_cmd.add_argument(
        "--strict",
        action="store_true",
        help="Exit non-zero if any item is not successful",
    )
    artifact_audit_cmd.set_defaults(handler=_handle_artifact_audit)

    aggregate = subparsers.add_parser(
        "aggregate", help="Aggregate single model results"
    )
    aggregate.add_argument("--dir", type=str, required=True)
    aggregate.set_defaults(handler=_handle_aggregate)

    aggregate_all = subparsers.add_parser(
        "aggregate-all", help="Aggregate all model results in experiment"
    )
    aggregate_all.add_argument("--dir", type=str, required=True)
    aggregate_all.set_defaults(handler=_handle_aggregate_all)

    verify = subparsers.add_parser(
        "verify-sim-parity", help="Run simulator parity verification"
    )
    verify.add_argument("--force", action="store_true")
    verify.set_defaults(handler=_handle_verify_sim_parity)

    install_hooks = subparsers.add_parser(
        "install-local-hooks", help="Install local pre-commit hook"
    )
    install_hooks.set_defaults(handler=_handle_install_local_hooks)

    return parser


def main() -> int:
    parser = create_parser()
    args = parser.parse_args()
    handler = getattr(args, "handler")
    return int(handler(args))


if __name__ == "__main__":
    raise SystemExit(main())
