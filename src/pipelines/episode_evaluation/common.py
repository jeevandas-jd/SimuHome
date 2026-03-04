from __future__ import annotations

from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from typing import Any, Dict, List

from src.agents.providers import LLMProvider
from src.agents.types import ChatMessage


def is_subset(expected: Any, actual: Any) -> bool:
    if isinstance(expected, dict) and isinstance(actual, dict):
        for k, v in expected.items():
            if k not in actual or not is_subset(v, actual[k]):
                return False
        return True
    if isinstance(expected, list) and isinstance(actual, list):
        return all(e in actual for e in expected)
    return expected == actual


def evaluate_required_actions(payload: Dict[str, Any]) -> List[Dict[str, Any]]:
    episode = payload.get("episode", {})
    if not isinstance(episode, dict):
        raise ValueError("payload.episode must be a dict")

    eval_section = episode.get("eval") or {}
    if not isinstance(eval_section, dict):
        raise ValueError("payload.episode.eval must be a dict")

    required = eval_section.get("required_actions")
    if not isinstance(required, list):
        raise ValueError("payload.episode.eval.required_actions must be a list")

    invoked = payload.get("tools_invoked")
    if not isinstance(invoked, list):
        raise ValueError("payload.tools_invoked must be a list")

    for req in required:
        if not isinstance(req, dict):
            raise ValueError("each required action must be a dict")
        req_tool = req.get("tool")
        req_params = req.get("params")
        if not isinstance(req_tool, str) or not req_tool:
            raise ValueError("required action tool must be a non-empty string")
        if not isinstance(req_params, dict):
            raise ValueError("required action params must be a dict")

    for inv in invoked:
        if not isinstance(inv, dict):
            raise ValueError("each tools_invoked entry must be a dict")
        inv_tool = inv.get("tool")
        inv_params = inv.get("params")
        inv_outcome = inv.get("outcome")
        if not isinstance(inv_tool, str) or not inv_tool:
            raise ValueError("tools_invoked.tool must be a non-empty string")
        if not isinstance(inv_params, dict):
            raise ValueError("tools_invoked.params must be a dict")
        if not isinstance(inv_outcome, dict):
            raise ValueError("tools_invoked.outcome must be a dict")

        if "ok" not in inv_outcome:
            raise ValueError("tools_invoked.outcome.ok is required")
        if inv_outcome.get("ok") is not None and not isinstance(
            inv_outcome.get("ok"), bool
        ):
            raise ValueError("tools_invoked.outcome.ok must be bool or null")

        status_code = inv_outcome.get("status_code")
        if status_code is not None and not isinstance(status_code, int):
            raise ValueError("tools_invoked.outcome.status_code must be int or null")

        error_type = inv_outcome.get("error_type")
        if error_type is not None and not isinstance(error_type, str):
            raise ValueError("tools_invoked.outcome.error_type must be str or null")

    results = []

    for req in required:
        req_tool = req.get("tool")
        req_params = req.get("params") or {}
        found = False

        for inv in invoked:
            if inv.get("tool") != req_tool:
                continue
            inv_params = inv.get("params") or {}
            if is_subset(req_params, inv_params):
                found = True
                break

        results.append({"tool": req_tool, "params": req_params, "invoked": found})

    return results


def extract_steps(payload: Dict[str, Any]) -> List[Dict[str, Any]]:
    steps = payload.get("steps")
    if not isinstance(steps, list):
        raise ValueError("payload.steps must be a list in current format")
    return steps


def extract_final_answer(react_steps: List[Dict[str, Any]]) -> str:
    final_answer: str = ""
    for s in reversed(react_steps or []):
        if s.get("action") == "finish":
            ai = s.get("action_input")
            if isinstance(ai, dict) and "answer" in ai:
                final_answer = str(ai["answer"])
            break
    return final_answer


def read_device_attr(state: Dict[str, Any], device_id: str, attribute: str) -> Any:
    for rid, rc in (state.get("rooms") or {}).items():
        for d in rc.get("devices") or []:
            if str(d.get("device_id")) == device_id:
                return (d.get("attributes") or {}).get(attribute)
    return None


def single_judge_call(judge_llm: LLMProvider, system: str, user: str) -> str:
    try:
        out = judge_llm.generate(
            [
                ChatMessage(role="system", content=system),
                ChatMessage(role="user", content=user),
            ]
        )
        letter = (out or "").strip().upper()[:1]
        return "A" if letter == "A" else "B"
    except Exception:
        return "Error"


def run_judge_panel(
    judge_llms: List[LLMProvider],
    system: str,
    user: str,
    *,
    failure_error_type: str = "Context Faithfulness Failure",
) -> Dict[str, Any]:
    if len(judge_llms) != 3:
        return {
            "score": -1,
            "error_type": "Judge Configuration Error",
            "judge": ["Error", "Error", "Error"],
        }

    judge_letters: List[str] = []
    try:
        with ThreadPoolExecutor(max_workers=len(judge_llms)) as executor:
            judge_letters = list(
                executor.map(
                    lambda judge: single_judge_call(judge, system, user), judge_llms
                )
            )
    except Exception:
        judge_letters = ["Error"] * len(judge_llms)

    if judge_letters and "Error" in judge_letters:
        return {
            "score": -1,
            "error_type": "Judge Error",
            "judge": judge_letters,
        }

    counter = Counter(judge_letters)
    a_count = counter.get("A", 0)
    b_count = counter.get("B", 0)

    if a_count > b_count:
        return {
            "score": 1,
            "error_type": None,
            "judge": judge_letters,
        }

    return {
        "score": 0,
        "error_type": failure_error_type,
        "judge": judge_letters,
    }


def extract_reasoning_and_answer(react_steps: List[Dict[str, Any]]) -> Dict[str, str]:
    thoughts = []
    final_answer = ""

    for step in react_steps or []:
        
        thought = step.get("thought")
        if thought and str(thought).strip():
            thoughts.append(str(thought).strip())

        
        if step.get("action") == "finish":
            ai = step.get("action_input")
            if isinstance(ai, dict):
                final_answer = str(ai.get("answer"))
            else:
                final_answer = str(ai)

    reasoning_process = "\n\n".join(thoughts) if thoughts else ""

    return {"reasoning_process": reasoning_process, "final_answer": final_answer}
