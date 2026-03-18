# /home/jd/SimuHome/src/scripts/generate_trajectories_ollama.py

import json
import jsonlines
import time
import ollama
from pathlib import Path
from tqdm import tqdm
from collections import defaultdict

# ── Config ───────────────────────────────────────────────────────
EPISODES_DIR  = Path("/home/jd/SimuHome/data/benchmark")
OUTPUT_DIR    = Path("/home/jd/SimuHome/data/gold_trajectories")
MODEL         = "llama3.2:3b"     # or "llama3.2:3b" or "qwen2.5:7b"
DELAY_SECONDS = 0.1           # local = no rate limits, tiny delay

# ── System Prompt ─────────────────────────────────────────────────
SYSTEM_PROMPT = """You are a Smart Home Assistant using the ReAct framework.
Generate ONLY a ReAct trajectory in this EXACT format:

Thought: <your reasoning>
Action: <tool_name>
Action Input: {"param": "value"}
Observation: <simulated tool response based on home config>
Thought: <next reasoning>
Action: <next tool>
Action Input: {"param": "value"}
Observation: <simulated response>
Thought: I have all the information needed.
Action: finish
Action Input: {"answer": "<friendly natural language answer>"}

UNIT CONVERSION RULES:
- Humidity raw ÷ 100 = % (5261 = 52.61%)
- Temperature raw ÷ 100 = °C (2202 = 22.02°C)
- Illuminance = direct lux (964.39 = 964.39 lux)
- PM10 = direct µg/m³

STRICT RULES:
- ALWAYS call every tool listed in required_actions
- Use EXACT values from room states in observations
- Never fabricate values
- For infeasible: detect contradiction, explain, finish
- For QT4: call get_current_time first"""

QT_HINTS = {
    "qt1":   "QT1: get_room_states(room) → read values → finish with units.",
    "qt2":   "QT2: get_room_devices(room) → get_room_states(room) → control device → finish.",
    "qt3":   "QT3: get_room_devices(room) → verify exists → turn on → set attribute → finish.",
    "qt4-1": "QT4-1: get_current_time → get_room_devices → calc absolute time → schedule_workflow → finish.",
    "qt4-2": "QT4-2: get_current_time → get_room_devices → check CountdownTime → schedule_workflow → finish.",
    "qt4-3": "QT4-3: get_current_time → check CountdownTime BOTH devices → schedule_workflow → finish.",
}

def get_hint(qt: str) -> str:
    norm = qt.replace("_", "-").lower()
    for key, hint in QT_HINTS.items():
        if norm.startswith(key):
            return hint
    return ""

def extract_room_states(home_config: dict) -> dict:
    states = {}
    for room, data in home_config["rooms"].items():
        raw = data["state"]
        states[room] = {
            "humidity_pct":    round(raw["humidity"] / 100, 2),
            "temperature_c":   round(raw["temperature"] / 100, 2),
            "illuminance_lux": round(raw["illuminance"], 2),
            "pm10_ugm3":       round(raw["pm10"], 2)
        }
    return states

def extract_device_ops(home_config: dict) -> dict:
    ops = {}
    for room, data in home_config["rooms"].items():
        for device in data["devices"]:
            attrs     = device["attributes"]
            countdown = attrs.get("1.OperationalState.CountdownTime")
            if countdown is not None:
                ops[device["device_id"]] = {
                    "room":          room,
                    "type":          device["device_type"],
                    "countdown_sec": countdown,
                    "op_state":      attrs.get(
                        "1.OperationalState.OperationalState"
                    ),
                    "on": attrs.get("1.OnOff.OnOff")
                }
    return ops

def build_prompt(episode: dict) -> str:
    home   = episode["initial_home_config"]
    qt     = episode["meta"]["query_type"]
    states = extract_room_states(home)

    prompt = f"""{get_hint(qt)}

Time: {home['base_time']}
Rooms: {list(home['rooms'].keys())}
User location: {episode['user_location']}
Query: "{episode['query']}"

Room States (use EXACT values in Observations):
{json.dumps(states, indent=2)}
"""
    if "qt4" in qt.lower():
        ops = extract_device_ops(home)
        if ops:
            prompt += f"\nDevice Operational States:\n"
            prompt += json.dumps(ops, indent=2) + "\n"

    prompt += f"""
Required Actions (ALL must appear in trajectory):
{json.dumps(episode['eval']['required_actions'], indent=2)}

Goals:
{json.dumps(episode['eval']['goals'], indent=2)}

Generate the complete ReAct trajectory now:"""
    return prompt

def validate(traj: str, episode: dict) -> tuple[bool, list]:
    missing = [
        r["tool"] for r in episode["eval"]["required_actions"]
        if r["tool"] not in traj
    ]
    if "finish" not in traj.lower():
        missing.append("finish")
    return len(missing) == 0, missing

def generate(episode: dict, max_retries: int = 3) -> str | None:
    full_prompt = (
        f"{SYSTEM_PROMPT}\n\n"
        f"{build_prompt(episode)}"
    )

    for attempt in range(max_retries):
        try:
            response = ollama.generate(
                model=MODEL,
                prompt=full_prompt,
                options={
                    "temperature": 0.1,
                    "num_predict": 1500,
                    "stop": ["</s>", "Human:", "User:"]
                }
            )
            traj = response["response"].strip()

            # Strip markdown
            if "```" in traj:
                traj = "\n".join(
                    l for l in traj.split("\n")
                    if not l.startswith("```")
                ).strip()

            ok, missing = validate(traj, episode)
            if ok:
                return traj
            else:
                print(f"\n  Attempt {attempt+1} missing: {missing}")

        except Exception as e:
            print(f"\n  Error: {e}")
            time.sleep(2)

    return None

def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # ── Test Ollama connection ─────────────────────────────────────
    print(f"Testing Ollama with {MODEL}...")
    try:
        r = ollama.generate(
            model=MODEL,
            prompt="Say: ready",
            options={"num_predict": 5}
        )
        print(f"✅ Ollama working — model: {MODEL}")
    except Exception as e:
        print(f"❌ Ollama error: {e}")
        print("Make sure ollama is running: ollama serve")
        return

    # ── Load episodes ──────────────────────────────────────────────
    episodes_by_qt = defaultdict(list)
    all_files = list(EPISODES_DIR.rglob("*.json"))
    print(f"Loading {len(all_files)} episodes...")

    for fpath in all_files:
        with open(fpath) as f:
            ep = json.load(f)
        key = f"{ep['meta']['query_type']}_{ep['meta']['case']}"
        episodes_by_qt[key].append(ep)

    # ── Estimate time ─────────────────────────────────────────────
    print(f"\n⏳ Estimated time:")
    print(f"   mistral 7B  on CPU : ~2-3 min/episode → ~20-30 hrs total")
    print(f"   llama3.2:3b on CPU : ~30s/episode     → ~5 hrs total")
    print(f"   any model   on GPU : ~5-10s/episode   → ~1-2 hrs total")
    print(f"\nPress Ctrl+C to stop anytime — resume is supported\n")

    total_success = 0
    total_failed  = 0
    failed_list   = []

    for qt_key in sorted(episodes_by_qt.keys()):
        episodes    = episodes_by_qt[qt_key]
        output_file = OUTPUT_DIR / f"{qt_key}.jsonl"

        # Resume support
        done_seeds = set()
        if output_file.exists():
            with jsonlines.open(output_file) as r:
                for item in r:
                    done_seeds.add(item["seed"])

        remaining = [e for e in episodes
                     if e["meta"]["seed"] not in done_seeds]
        total_success += len(done_seeds)

        if not remaining:
            print(f"✅ {qt_key}: complete")
            continue

        print(f"\n{'='*55}")
        print(f"  {qt_key}")
        print(f"  Done: {len(done_seeds)} | Remaining: {len(remaining)}")
        print(f"{'='*55}")

        with jsonlines.open(output_file, "a") as writer:
            for ep in tqdm(remaining, desc=qt_key):
                traj = generate(ep)

                if traj:
                    writer.write({
                        "seed":             ep["meta"]["seed"],
                        "query_type":       qt_key,
                        "query":            ep["query"],
                        "user_location":    ep["user_location"],
                        "base_time":        ep["initial_home_config"]["base_time"],
                        "rooms":            list(
                            ep["initial_home_config"]["rooms"].keys()
                        ),
                        "trajectory":       traj,
                        "goals":            ep["eval"]["goals"],
                        "required_actions": ep["eval"]["required_actions"]
                    })
                    total_success += 1
                else:
                    total_failed += 1
                    failed_list.append({
                        "qt":   qt_key,
                        "seed": ep["meta"]["seed"]
                    })

                time.sleep(DELAY_SECONDS)

    # ── Summary ───────────────────────────────────────────────────
    print(f"\n{'='*55}")
    print(f"✅ Success : {total_success} / 600")
    print(f"❌ Failed  : {total_failed}")
    print(f"📁 Saved   : {OUTPUT_DIR}")

    if failed_list:
        with open(OUTPUT_DIR / "failed.json", "w") as f:
            json.dump(failed_list, f, indent=2)

    print("\n=== Trajectory Counts ===")
    for f in sorted(OUTPUT_DIR.glob("*.jsonl")):
        count = sum(1 for _ in open(f))
        mark  = "✅" if count >= 45 else "⚠️ "
        print(f"  {mark} {f.stem:<30}: {count}")

if __name__ == "__main__":
    main()