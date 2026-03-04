from __future__ import annotations
import importlib
import json
import time

from typing import Any, Dict, List, Optional

from src.clients.smarthome_client import SmartHomeClient
from src.agents.providers import LLMProvider
from src.agents.strategies import (
    ReActConfig,
    create_agent_strategy,
)
from src.agents.strategies.hi_agent import HiAgentConfig
from src.agents.tools import ToolConfig, get_tool_config, set_tool_config
from src.pipelines.episode_evaluation.strategy_adapters import (
    EpisodeContext,
    get_strategy_adapter,
)

_EVALUATOR_REGISTRY = {
    ("qt1", "feasible"): "src.pipelines.episode_evaluation.qt1.feasible",
    ("qt1", "infeasible"): "src.pipelines.episode_evaluation.qt1.infeasible",
    ("qt2", "feasible"): "src.pipelines.episode_evaluation.qt2.feasible",
    ("qt2", "infeasible"): "src.pipelines.episode_evaluation.qt2.infeasible",
    ("qt3", "feasible"): "src.pipelines.episode_evaluation.qt3.feasible",
    ("qt3", "infeasible"): "src.pipelines.episode_evaluation.qt3.infeasible",
    ("qt4-1", "feasible"): "src.pipelines.episode_evaluation.qt4.feasible",
    ("qt4-1", "infeasible"): "src.pipelines.episode_evaluation.qt4.infeasible_1",
    ("qt4-2", "feasible"): "src.pipelines.episode_evaluation.qt4.feasible",
    ("qt4-2", "infeasible"): "src.pipelines.episode_evaluation.qt4.infeasible_2",
    ("qt4-3", "feasible"): "src.pipelines.episode_evaluation.qt4.feasible",
    ("qt4-3", "infeasible"): "src.pipelines.episode_evaluation.qt4.infeasible_3",
}

_RESERVED_EVALUATION_KEYS = {
    "episode",
    "final_home_state",
    "client",
    "tools_invoked",
}


def _canonical_strategy_name(strategy: str | None) -> str:
    key = (strategy or "react").lower()
    if key in ("react", "react-agent"):
        return "react"
    if key in ("hi_agent", "hiagent", "hi-agent"):
        return "hi_agent"
    return key


def _build_agent(
    llm: LLMProvider,
    *,
    max_steps: int,
    strategy: str = "react",
):
    strategy_key = _canonical_strategy_name(strategy)

    if strategy_key == "react":
        cfg = ReActConfig(max_steps=max_steps, show_assistant_raw=True)
        return create_agent_strategy(strategy_key, llm=llm, config=cfg)

    elif strategy_key == "hi_agent":
        cfg = HiAgentConfig()
        cfg.max_steps = max_steps

        return create_agent_strategy(strategy_key, llm=llm, config=cfg)

    return create_agent_strategy(strategy_key, llm=llm, max_steps=max_steps)


def _serialize_tool_calls(tool_calls: List[Any]) -> List[Dict[str, Any]]:
    serialized: List[Dict[str, Any]] = []
    for call in tool_calls or []:
        tool = getattr(call, "tool", None)
        if not isinstance(tool, str) or not tool:
            raise ValueError("ToolInvocation.tool must be a non-empty string")

        params = getattr(call, "params", None)
        if not isinstance(params, dict):
            raise ValueError("ToolInvocation.params must be a dict")

        observation = getattr(call, "observation", None)
        status_code: Optional[int] = None
        error_type: Optional[str] = None
        ok: Optional[bool] = None

        if isinstance(observation, dict):
            status = observation.get("status")
            if isinstance(status, dict):
                raw_code = status.get("code")
                if isinstance(raw_code, int):
                    status_code = raw_code

            error = observation.get("error")
            if isinstance(error, dict):
                raw_error_type = error.get("type")
                if isinstance(raw_error_type, str) and raw_error_type:
                    error_type = raw_error_type
            elif isinstance(error, str) and error:
                error_type = error

            if status_code is not None:
                ok = status_code == 200 and error_type is None

        serialized.append(
            {
                "tool": tool,
                "params": params,
                "outcome": {
                    "ok": ok,
                    "status_code": status_code,
                    "error_type": error_type,
                },
            }
        )
    return serialized


def _require_ok_response(resp: Any, *, context: str) -> Dict[str, Any]:
    if not isinstance(resp, dict):
        raise RuntimeError(f"{context}: response must be a dict")

    status = resp.get("status")
    if not isinstance(status, dict):
        raise RuntimeError(f"{context}: missing status dict")

    code = status.get("code")
    if not isinstance(code, int):
        raise RuntimeError(f"{context}: status.code must be int")

    if code != 200:
        raise RuntimeError(f"{context}: non-OK status code {code}")

    if resp.get("error") is not None:
        raise RuntimeError(f"{context}: response.error must be null on success")

    data = resp.get("data")
    if not isinstance(data, dict):
        raise RuntimeError(f"{context}: response.data must be a dict")

    return data


def _merge_evaluation_payload(
    base_payload: Dict[str, Any], evaluation_payload: Dict[str, Any]
) -> Dict[str, Any]:
    if not isinstance(evaluation_payload, dict):
        raise RuntimeError("evaluation payload must be a dict")

    conflicting = sorted(
        key for key in evaluation_payload.keys() if key in _RESERVED_EVALUATION_KEYS
    )
    if conflicting:
        raise RuntimeError(
            "evaluation payload contains reserved keys: " + ", ".join(conflicting)
        )

    merged = dict(base_payload)
    merged.update(evaluation_payload)
    return merged


def run_single_config(
    *,
    cfg_path: str,
    base_url: str,
    timeout: float,
    max_steps: int,
    agent_strategy: str = "react",
    main_llm: LLMProvider,
    judge_llms: List[LLMProvider],
) -> Dict[str, Any]:
    with open(cfg_path, "r", encoding="utf-8") as f:
        episode = json.load(f)

    qt = episode["meta"]["query_type"]
    case = episode["meta"]["case"]
    conflict_type = episode["meta"].get("conflict_type")

    canonical_strategy = _canonical_strategy_name(agent_strategy)

    agent = _build_agent(main_llm, max_steps=max_steps, strategy=agent_strategy)
    adapter = get_strategy_adapter(canonical_strategy)

    client = SmartHomeClient(base_url=base_url, timeout=timeout)
    if not client.health():
        raise RuntimeError(
            "Server health check failed. Ensure 'python server.py' is running."
        )

    reset_resp = client.reset_simulation(episode["initial_home_config"])
    _require_ok_response(reset_resp, context="reset_simulation")
    current_tool_config = get_tool_config()
    set_tool_config(
        ToolConfig(
            base_url=base_url,
            timeout=int(timeout),
            db=current_tool_config.db,
        )
    )

    started_at = time.perf_counter()
    artifacts = adapter.run(
        agent,
        EpisodeContext(
            query=episode["query"],
            user_location=episode.get("user_location"),
            current_time=episode["initial_home_config"].get("base_time"),
        ),
    )
    ended_at = time.perf_counter()
    duration_sec = float(ended_at - started_at)

    tools_invoked = _serialize_tool_calls(artifacts.agent_result.tool_calls)

    time.sleep(0.5)
    final_home_state_resp = client.get_home_state()
    final_home_state = _require_ok_response(
        final_home_state_resp, context="get_home_state"
    )

    payload_for_eval: Dict[str, Any] = {
        "episode": episode,
        "final_home_state": final_home_state,
        "client": client,
        "tools_invoked": tools_invoked,
    }
    payload_for_eval = _merge_evaluation_payload(
        payload_for_eval, artifacts.evaluation_payload
    )

    module_name = _EVALUATOR_REGISTRY.get((qt, case))
    if module_name is None:
        supported = sorted({f"{q}:{c}" for (q, c) in _EVALUATOR_REGISTRY})
        raise RuntimeError(
            f"Unsupported evaluator dispatch key query_type='{qt}', case='{case}'. "
            f"Supported keys: {supported}"
        )

    try:
        evaluator_module = importlib.import_module(module_name)
    except ModuleNotFoundError as e:
        raise RuntimeError(f"Evaluator module not found: {module_name}") from e

    if not hasattr(evaluator_module, "evaluate"):
        raise RuntimeError(
            f"Evaluator module '{module_name}' must expose function "
            "'evaluate(payload: dict, judge_llms: List[LLMProvider]) -> dict'"
        )

    evaluation_result = evaluator_module.evaluate(payload_for_eval, judge_llms)
    out: Dict[str, Any] = {}
    out["seed"] = episode["meta"]["seed"]
    out["query_type"] = qt
    out["case"] = case
    if conflict_type:
        out["conflict_type"] = conflict_type
    out["model"] = str(getattr(main_llm, "model", ""))
    out["strategy"] = canonical_strategy
    out["config_path"] = cfg_path
    out["query"] = episode["query"]
    out["duration"] = duration_sec
    out["evaluation_result"] = evaluation_result
    out["tools_invoked"] = tools_invoked
    out.update(artifacts.storage_payload)

    steps = artifacts.evaluation_payload.get("steps")
    if not isinstance(steps, list):
        raise RuntimeError("evaluation payload must include steps list")
    out["steps"] = steps

    trace_type = artifacts.evaluation_payload.get("trace_type")
    if not isinstance(trace_type, str) or not trace_type:
        raise RuntimeError("evaluation payload must include trace_type string")
    out["trace_type"] = trace_type

    return out
