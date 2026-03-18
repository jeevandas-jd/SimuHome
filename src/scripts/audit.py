# scripts/audit_episodes.py
import json
from pathlib import Path
from collections import Counter

# ── Fix: use the correct directory ──────────────────────────
episodes_dir = Path("/home/jd/SimuHome/data/benchmark")

qt_counter = Counter()
issues = []

# ── Fix: search recursively in the correct directory ────────
all_files = list(episodes_dir.rglob("*.json"))

print(f"Found {len(all_files)} JSON files in {episodes_dir}")

if len(all_files) == 0:
    print("\n⚠️  No files found! Checking directory structure...")
    if episodes_dir.exists():
        print(f"Directory exists. Contents:")
        for item in episodes_dir.iterdir():
            print(f"  {item}")
    else:
        print(f"❌ Directory does not exist: {episodes_dir}")
        print("Available directories:")
        for item in Path("/home/jd/SimuHome/data").iterdir():
            print(f"  {item}")
else:
    for fpath in all_files:
        try:
            with open(fpath) as f:
                ep = json.load(f)

            qt   = ep["meta"]["query_type"]
            case = ep["meta"]["case"]
            key  = f"{qt}_{case}"
            qt_counter[key] += 1

            if "query" not in ep:
                issues.append(f"{fpath}: missing query")
            if "eval" not in ep:
                issues.append(f"{fpath}: missing eval")
            if "initial_home_config" not in ep:
                issues.append(f"{fpath}: missing home_config")

        except Exception as e:
            issues.append(f"{fpath}: parse error — {e}")

    print("\n=== Episode Distribution ===")
    for qt, count in sorted(qt_counter.items()):
        print(f"  {qt:<25} : {count}")

    print(f"\nTotal: {sum(qt_counter.values())}")
    print(f"Issues found: {len(issues)}")
    for issue in issues[:5]:
        print(f"  ⚠️  {issue}")