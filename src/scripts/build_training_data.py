# /home/jd/SimuHome/src/scripts/build_training_data.py

import json
import jsonlines
import random
from pathlib import Path
from collections import defaultdict

# ── Config ───────────────────────────────────────────────────────
abs_path="/home/jeevandas/WinningProjects/SimuHome/data/gold_trajectories"
TRAJECTORIES_DIR = Path("/home/jeevandas/WinningProjects/SimuHome/data/gold_trajectories")
EPISODES_DIR     = Path("/home/jeevandas/WinningProjects/SimuHome/data/benchmark")
OUTPUT_DIR       = Path("/home/jeevandas/WinningProjects/SimuHome/data/processed")

TRAIN_RATIO = 0.80   # 480 samples
VAL_RATIO   = 0.10   #  60 samples
TEST_RATIO  = 0.10   #  60 samples

RANDOM_SEED = 42

# ── Mistral Instruction Format ────────────────────────────────────
SYSTEM_PROMPT = """You are a Smart Home Assistant that uses tools to control devices
and provide information based on the Matter protocol, with the goal of fulfilling the User Query.

You operate under the ReAct framework with structured responses.

[REACT FRAMEWORK]
- LOOP: ('thought' -> 'action' -> 'action_input') -> 'observation' -> repeat until completion.
- End with the 'finish' tool when the query is fully satisfied.

[CRITICAL REQUIREMENTS]
- NEVER fabricate, assume, or guess information - always verify through tools.
- Always include the correct room_id in your tool calls.
- If rooms or devices do not exist, explicitly state this in the final answer.

[DATA UNITS]
- Temperature: hundredths of °C (2792 = 27.92°C)
- Humidity: hundredths of % (5261 = 52.61%)
- Illuminance: direct lux (681.81 = 681.81 lux)
- PM10: direct µg/m³

[AVAILABLE TOOLS]
- get_room_states(room_id): Get temperature, humidity, illuminance, PM10
- get_room_devices(room_id): Get all devices in a room
- get_current_time(): Get current virtual time
- execute_command(device_id, endpoint_id, cluster_id, command_id, args)
- write_attribute(device_id, cluster_id, attribute_id, value)
- schedule_workflow(start_time, steps)
- cancel_workflow(workflow_id)
- get_workflow_status(workflow_id)
- finish(answer): Return final answer to user"""


def format_sample(trajectory_item: dict, episode: dict) -> str:
    """
    Format into Mistral chat template:
    <s>[INST] <<SYS>>system<</SYS>>user [/INST] assistant</s>
    """
    home  = episode["initial_home_config"]
    rooms = list(home["rooms"].keys())

    user_message = (
        f"Current time: {home['base_time']}\n"
        f"Available rooms: {', '.join(rooms)}\n"
        f"Your current location: {episode['user_location']}\n\n"
        f"User query: {episode['query']}"
    )

    assistant_message = trajectory_item["trajectory"]

    return (
        f"<s>[INST] <<SYS>>\n{SYSTEM_PROMPT}\n<</SYS>>\n\n"
        f"{user_message} [/INST]\n"
        f"{assistant_message}</s>"
    )


def load_episodes_by_key() -> dict:
    """Load all episodes indexed by (query_type, case, seed)."""
    episodes = {}
    for fpath in EPISODES_DIR.rglob("*.json"):
        with open(fpath) as f:
            ep = json.load(f)
        qt   = ep["meta"]["query_type"]
        case = ep["meta"]["case"]
        seed = ep["meta"]["seed"]
        episodes[(qt, case, seed)] = ep
    print(f"Loaded {len(episodes)} episodes")
    return episodes


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    random.seed(RANDOM_SEED)

    # Load episodes for matching
    episodes = load_episodes_by_key()

    # Load all trajectories
    all_samples = []
    skipped     = 0

    print("\nProcessing trajectories...")
    for traj_file in sorted(TRAJECTORIES_DIR.glob("*.jsonl")):
        qt_key = traj_file.stem   # e.g. "qt1_feasible"
        count  = 0

        with jsonlines.open(traj_file) as reader:
            for item in reader:
                seed = item["seed"]

                # Parse qt and case from filename
                # Handle both qt1_feasible and qt4-1_feasible
                parts = qt_key.rsplit("_", 1)
                case  = parts[-1]                    # feasible/infeasible
                qt    = parts[0].replace("-", "-")   # qt1, qt4-1 etc

                # Match to original episode
                ep_key = (qt, case, seed)
                if ep_key not in episodes:
                    # Try alternate key formats
                    qt_alt = qt.replace("-", "_")
                    ep_key = (qt_alt, case, seed)

                if ep_key not in episodes:
                    skipped += 1
                    continue

                episode = episodes[ep_key]
                formatted = format_sample(item, episode)

                all_samples.append({
                    "text":       formatted,
                    "query_type": qt_key,
                    "seed":       seed
                })
                count += 1

        print(f"  {qt_key:<30}: {count} samples")

    print(f"\nTotal samples  : {len(all_samples)}")
    print(f"Skipped        : {skipped}")

    # Shuffle
    random.shuffle(all_samples)

    # Split
    n_total = len(all_samples)
    n_train = int(n_total * TRAIN_RATIO)
    n_val   = int(n_total * VAL_RATIO)

    train = all_samples[:n_train]
    val   = all_samples[n_train:n_train + n_val]
    test  = all_samples[n_train + n_val:]

    print(f"\nSplit:")
    print(f"  Train : {len(train)}")
    print(f"  Val   : {len(val)}")
    print(f"  Test  : {len(test)}")

    # Save splits
    for name, split in [("train", train), ("val", val), ("test", test)]:
        out_path = OUTPUT_DIR / f"{name}.jsonl"
        with jsonlines.open(out_path, "w") as writer:
            for item in split:
                writer.write(item)
        print(f"  Saved {len(split)} → {out_path}")

    # Save split info
    info = {
        "total":        n_total,
        "train":        len(train),
        "val":          len(val),
        "test":         len(test),
        "random_seed":  RANDOM_SEED,
        "model_format": "mistral-instruct"
    }
    with open(OUTPUT_DIR / "split_info.json", "w") as f:
        json.dump(info, f, indent=2)

    # Sample check
    print("\n=== Sample Check (first training example) ===")
    print(train[0]["text"][:500])
    print("...")
    print(f"\n✅ Training data ready at: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()