# evaluation/groq_benchmark.py
"""
Evaluates model on SimuHome test split using Groq API.
No GPU needed. Runs in ~20 minutes.
Usage: python evaluation/groq_benchmark.py
"""

import json
import time
import jsonlines
from pathlib import Path
from collections import defaultdict
from tqdm import tqdm
from groq import Groq

# ── Config ────────────────────────────────────────────────
GROQ_API_KEY = ""   # ← your key from console.groq.com
MODEL        = "llama-3.1-8b-instant"
TEST_PATH    = "../data/processed/test.jsonl"
OUTPUT_DIR   = Path("outputs/evaluation")
DELAY        = 2.1          # seconds between requests

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
client = Groq(api_key=GROQ_API_KEY)

# ── System prompt (same as fine-tuning) ──────────────────
SYSTEM_PROMPT = """You are a Smart Home Assistant that uses tools
to control devices and provide information based on the Matter
protocol, with the goal of fulfilling the User Query.

You operate under the ReAct framework with structured responses.

[REACT FRAMEWORK]
- LOOP: thought -> action -> action_input -> observation -> repeat
- End with the finish tool when the query is fully satisfied.

[DATA UNITS]
- Temperature: hundredths of Celsius (2792 = 27.92C)
- Humidity: hundredths of percent (5261 = 52.61%)
- Illuminance: direct lux
- PM10: direct ug/m3

[AVAILABLE TOOLS]
- get_room_states(room_id)
- get_room_devices(room_id)
- get_current_time()
- execute_command(device_id, endpoint_id, cluster_id, command_id)
- write_attribute(device_id, cluster_id, attribute_id, value)
- schedule_workflow(start_time, steps)
- finish(answer)

ALWAYS call required tools before answering. Never guess."""

# ── Paper baselines (Table 1 — Gemma3-4B SFT) ────────────
BASELINES = {
    "qt1_feasible":     44.0,
    "qt1_infeasible":   82.0,
    "qt2_feasible":     22.0,
    "qt2_infeasible":   36.0,
    "qt3_feasible":     24.0,
    "qt3_infeasible":   88.0,
    "qt4-1_feasible":    4.0,
    "qt4-1_infeasible": 12.0,
    "qt4-2_feasible":    4.0,
    "qt4-2_infeasible": 34.0,
    "qt4-3_feasible":    0.0,
    "qt4-3_infeasible": 32.0,
}


def build_prompt(sample: dict) -> str:
    rooms    = sample.get("rooms", [])
    location = sample.get("user_location", "unknown")
    time_str = sample.get("base_time", "unknown")
    query    = sample.get("query", "")

    return (
        f"Current time: {time_str}\n"
        f"Available rooms: {', '.join(rooms)}\n"
        f"Your location: {location}\n\n"
        f"User query: {query}\n\n"
        f"Respond with a complete ReAct trajectory "
        f"starting with 'Thought:'"
    )


def evaluate_sample(sample: dict) -> dict:
    """Run one sample through Groq and evaluate."""
    req   = sample.get("required_actions", [])
    qt    = sample.get("query_type", "unknown")

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user",   "content": build_prompt(sample)}
            ],
            temperature=0.1,
            max_tokens=500
        )
        output = response.choices[0].message.content.strip()

    except Exception as e:
        return {
            "query_type":  qt,
            "error":       str(e),
            "strict_pass": False,
            "tools_ok":    False,
            "finish_ok":   False,
        }

    # Evaluation
    tools_ok  = all(r["tool"] in output for r in req)
    finish_ok = "finish" in output.lower()
    thought_ok = "Thought:" in output
    action_ok  = "Action:" in output

    return {
        "query_type":   qt,
        "query":        sample.get("query", "")[:100],
        "required":     [r["tool"] for r in req],
        "tools_ok":     tools_ok,
        "finish_ok":    finish_ok,
        "thought_ok":   thought_ok,
        "action_ok":    action_ok,
        "strict_pass":  tools_ok and finish_ok,
        "partial_pass": thought_ok and action_ok and finish_ok,
        "response":     output[:400],
    }


def main():
    # Load test samples
    samples = []
    with jsonlines.open(TEST_PATH) as r:
        for item in r:
            samples.append(item)
    print(f"Loaded {len(samples)} test samples")
    print(f"sample data {samples[4]}")

    # Test connection
    print("Testing Groq connection...")
    try:
        r = client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "user", "content": "say: ready"}],
            max_tokens=5
        )
        print(f"✅ Connected to Groq — {MODEL}")
    except Exception as e:
        print(f"❌ Groq error: {e}")
        return

    print(f"⏱  Est. time: ~{len(samples)*DELAY/60:.0f} minutes\n")

    # Run evaluation
    qt_results  = defaultdict(lambda: {"total": 0, "passed": 0})
    all_results = []

    for sample in tqdm(samples, desc="Evaluating"):
        result = evaluate_sample(sample)
        qt     = result["query_type"]

        qt_results[qt]["total"]  += 1
        qt_results[qt]["passed"] += int(result["strict_pass"])
        all_results.append(result)

        time.sleep(DELAY)

    # Print results table
    print("\n" + "="*70)
    print(f"  BENCHMARK: {MODEL} (base) vs SimuHome Paper Baselines")
    print("="*70)
    print(f"  {'Query Type':<25} {'Score':>7} "
          f"{'Baseline':>9} {'Delta':>8} {'Pass/Total':>12}")
    print("-"*70)

    total_pass  = 0
    total_count = 0
    beats       = 0

    for qt in sorted(qt_results.keys()):
        r      = qt_results[qt]
        score  = r["passed"] / r["total"] * 100
        base   = BASELINES.get(qt, 0)
        delta  = score - base
        flag   = "✅" if delta >= 0 else "⚠️ "
        if delta >= 0:
            beats += 1

        total_pass  += r["passed"]
        total_count += r["total"]

        print(f"  {flag} {qt:<23} "
              f"{score:>6.1f}%  "
              f"{base:>8.1f}%  "
              f"{delta:>+7.1f}%  "
              f"{r['passed']}/{r['total']}")

    overall = total_pass / total_count * 100
    print("-"*70)
    print(f"  {'OVERALL':<25} {overall:>6.1f}%  "
          f"{'—':>8}   {'—':>7}   "
          f"{total_pass}/{total_count}")
    print(f"\n  Beats baseline: {beats}/{len(qt_results)} query types")
    print("="*70)

    # Save report
    report = {
        "model":      MODEL,
        "type":       "base model (no fine-tuning)",
        "baseline":   "Gemma3-4B SFT (SimuHome paper)",
        "overall":    overall,
        "beats":      f"{beats}/{len(qt_results)}",
        "results": {
            qt: {
                "score":    qt_results[qt]["passed"] /
                            qt_results[qt]["total"] * 100,
                "baseline": BASELINES.get(qt, 0),
                "delta":    qt_results[qt]["passed"] /
                            qt_results[qt]["total"] * 100 -
                            BASELINES.get(qt, 0),
                "passed":   qt_results[qt]["passed"],
                "total":    qt_results[qt]["total"],
            }
            for qt in qt_results
        },
        "samples": all_results
    }

    out_path = OUTPUT_DIR / f"groq_{MODEL}_benchmark.json"
    with open(out_path, "w") as f:
        json.dump(report, f, indent=2)

    print(f"\n✅ Saved: {out_path}")
    print("\nNext steps:")
    print("  1. Run fine-tuned model eval when Colab GPU resets")
    print("  2. Compare: base vs fine-tuned vs paper baselines")
    print("  3. Build edge deployment system")


if __name__ == "__main__":
    main()
