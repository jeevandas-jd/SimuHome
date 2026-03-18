# /home/jd/SimuHome/src/scripts/generate_trajectories_groq.py

import json
import jsonlines
import time
from pathlib import Path
from tqdm import tqdm
from collections import defaultdict
from groq import Groq

# ── Config ───────────────────────────────────────────────────────
EPISODES_DIR  = Path("/home/jd/SimuHome/data/benchmark")
OUTPUT_DIR    = Path("/home/jd/SimuHome/data/gold_trajectories")
GROQ_API_KEY  = ""          # ← paste your key here
MODEL         = "llama-3.1-8b-instant"
DELAY_SECONDS = 4.0                # safe for 30 RPM free tier

client = Groq(api_key=GROQ_API_KEY)

# ── System Prompt ─────────────────────────────────────────────────
SYSTEM_PROMPT = """You are a Smart Home Assistant using the ReAct framework.
Generate ONLY a ReAct trajectory in this EXACT format — no extra text:

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
- ALWAYS call every tool listed in required_actions — no exceptions
- Use EXACT values from room states in observations
- Never fabricate or guess values
- For infeasible cases: detect contradiction, explain clearly, finish
- For QT4: ALWAYS call get_current_time first"""

QT_HINTS = {
    "qt1":   "QT1 (Environment Perception):\nget_room_states(room_id) → read exact values → finish with clear answer including units.",
    "qt2":   "QT2 (Implicit Intent):\nget_room_devices(room_id) → get_room_states(room_id) → infer device action → execute_command → finish.",
    "qt3":   "QT3 (Explicit Intent):\nget_room_devices(room_id) → verify device exists → turn on if needed → set attribute → finish.",
    "qt4-1": "QT4-1 (Future Scheduling):\nget_current_time → get_room_devices → verify devices → absolute_time = now + offset → schedule_workflow → finish.",
    "qt4-2": "QT4-2 (Dependency Scheduling):\nget_current_time → get_room_devices → check device CountdownTime → completion = now + countdown → schedule_workflow → finish.",
    "qt4-3": "QT4-3 (Concurrent Scheduling):\nget_current_time → check CountdownTime of BOTH devices → calculate simultaneous finish → schedule_workflow → finish.",
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
            op_state  = attrs.get("1.OperationalState.OperationalState")
            if countdown is not None:
                ops[device["device_id"]] = {
                    "room":          room,
                    "type":          device["device_type"],
                    "countdown_sec": countdown,
                    "op_state":      op_state,
                    "on":            attrs.get("1.OnOff.OnOff")
                }
    return ops

def build_prompt(episode: dict) -> str:
    home   = episode["initial_home_config"]
    qt     = episode["meta"]["query_type"]
    states = extract_room_states(home)

    prompt = f"""{get_hint(qt)}

TIME: {home['base_time']}
ROOMS: {list(home['rooms'].keys())}
USER LOCATION: {episode['user_location']}
USER QUERY: "{episode['query']}"

ROOM STATES — use these EXACT values in your Observations:
{json.dumps(states, indent=2)}
"""
    if "qt4" in qt.lower():
        ops = extract_device_ops(home)
        if ops:
            prompt += f"\nDEVICE OPERATIONAL STATES:\n{json.dumps(ops, indent=2)}\n"

    prompt += f"""
REQUIRED ACTIONS — ALL of these tools MUST appear in your trajectory:
{json.dumps(episode['eval']['required_actions'], indent=2)}

GOALS:
{json.dumps(episode['eval']['goals'], indent=2)}

Generate the complete ReAct trajectory now. Start with 'Thought:':"""
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
    for attempt in range(max_retries):
        try:
            response = client.chat.completions.create(
                model=MODEL,
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user",   "content": build_prompt(episode)}
                ],
                temperature=0.1,
                max_tokens=1500
            )
            traj = response.choices[0].message.content.strip()

            # Strip markdown fences
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
                time.sleep(DELAY_SECONDS)

        except Exception as e:
            err = str(e)
            if "429" in err or "rate" in err.lower():
                print(f"\n  ⚠️  Rate limit — waiting 30s...")
                time.sleep(30)
            elif "503" in err or "502" in err:
                print(f"\n  Server error — waiting 10s...")
                time.sleep(10)
            else:
                print(f"\n  Error attempt {attempt+1}: {e}")
                time.sleep(3)
    return None

def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # ── Test connection ───────────────────────────────────────────
    print("Testing Groq connection...")
    try:
        r = client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "user", "content": "say: ready"}],
            max_tokens=5
        )
        print(f"✅ Groq connected — {MODEL}")
        print(f"⏱  Delay : {DELAY_SECONDS}s between requests")
        print(f"⏳ Est.   : ~{int(600 * DELAY_SECONDS / 60)} minutes total")
    except Exception as e:
        print(f"❌ Groq connection failed: {e}")
        return

    # ── Load all 600 episodes ─────────────────────────────────────
    episodes_by_qt = defaultdict(list)
    all_files = list(EPISODES_DIR.rglob("*.json"))
    print(f"\nLoading {len(all_files)} episodes...")

    for fpath in all_files:
        with open(fpath) as f:
            ep = json.load(f)
        key = f"{ep['meta']['query_type']}_{ep['meta']['case']}"
        episodes_by_qt[key].append(ep)

    total_success = 0
    total_failed  = 0
    failed_list   = []

    for qt_key in sorted(episodes_by_qt.keys()):
        episodes    = episodes_by_qt[qt_key]
        output_file = OUTPUT_DIR / f"{qt_key}.jsonl"

        # ── Resume support ────────────────────────────────────────
        done_seeds = set()
        if output_file.exists():
            with jsonlines.open(output_file) as r:
                for item in r:
                    done_seeds.add(item["seed"])

        remaining = [e for e in episodes
                     if e["meta"]["seed"] not in done_seeds]
        total_success += len(done_seeds)

        if not remaining:
            print(f"✅ {qt_key}: already complete ({len(done_seeds)})")
            continue

        print(f"\n{'='*55}")
        print(f"  {qt_key}")
        print(f"  Done: {len(done_seeds)} | Remaining: {len(remaining)}")
        print(f"  Est : ~{len(remaining)*DELAY_SECONDS/60:.1f} min")
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
                    print(f"\n  ❌ Failed: seed={ep['meta']['seed']}")

                time.sleep(DELAY_SECONDS)

    # ── Final summary ─────────────────────────────────────────────
    print(f"\n{'='*55}")
    print(f"✅ Success : {total_success} / 600")
    print(f"❌ Failed  : {total_failed}")
    print(f"📁 Saved   : {OUTPUT_DIR}")

    if failed_list:
        with open(OUTPUT_DIR / "failed.json", "w") as f:
            json.dump(failed_list, f, indent=2)
        print(f"⚠️  Failed list: {OUTPUT_DIR}/failed.json")

    print("\n=== Final Trajectory Counts ===")
    for f in sorted(OUTPUT_DIR.glob("*.jsonl")):
        count = sum(1 for _ in open(f))
        mark  = "✅" if count >= 45 else "⚠️ "
        print(f"  {mark} {f.stem:<30}: {count}")

if __name__ == "__main__":
    main()


"""

## Side by Side — Your Two Options Right Now

Option A: Fix Ollama GPU          Option B: Groq API (recommended)
─────────────────────────────     ────────────────────────────────
sudo systemctl stop ollama        1. browser → console.groq.com
sudo OLLAMA_NUM_GPU=99 \          2. signup → create API key
  ollama serve &                  3. pip install groq
→ ~2 hrs if GPU works             4. run groq script
→ ~5 hrs if stays on CPU          → done in ~25 minutes FREE"""