# SimuHome-Edge — Data Directory

This directory contains all data assets for the SimuHome-Edge
fine-tuning and evaluation project.

---

## Directory Structure

```
data/
├── benchmark/          ← 600 raw SimuHome episodes (JSON)
├── gold_trajectories/  ← 602 LLM-distilled ReAct trajectories (JSONL)
├── processed/          ← Final training / validation / test splits (JSONL)
└── vector_db/          ← Matter protocol cluster documentation index
```

---

## 1. `benchmark/` — Raw Episodes

**600 JSON files** sourced directly from the SimuHome benchmark
(ICLR 2026 Oral, arXiv:2509.24282).

### Naming Convention

```
{query_type}_{case}_seed_{seed}.json

Examples:
  qt1_feasible_seed_1.json
  qt4-1_infeasible_seed_42.json
```

### Distribution

| Query Type | Feasible | Infeasible | Total |
|------------|----------|------------|-------|
| QT1 — Environment Perception | 50 | 50 | 100 |
| QT2 — Implicit Intent | 50 | 50 | 100 |
| QT3 — Explicit Device Control | 50 | 50 | 100 |
| QT4-1 — Future Scheduling | 50 | 50 | 100 |
| QT4-2 — Dependency Scheduling | 50 | 50 | 100 |
| QT4-3 — Concurrent Scheduling | 50 | 50 | 100 |
| **Total** | **300** | **300** | **600** |

### Episode Schema

Each JSON file contains:

```json
{
  "meta": {
    "seed": 1,
    "query_type": "qt1",
    "case": "feasible",
    "num_rooms": 5,
    "num_devices": 31
  },
  "query": "How bright is the utility room right now?",
  "user_location": "kitchen",
  "eval": {
    "required_actions": [
      {"tool": "get_room_states", "params": {"room_id": "utility_room"}}
    ],
    "goals": [
      {
        "variant": "room_state",
        "room_id": "utility_room",
        "room_state": "illuminance",
        "current_value": 681.81,
        "unit": "lux"
      }
    ]
  },
  "initial_home_config": {
    "tick_interval": 0.1,
    "base_time": "2025-08-23 11:36:54",
    "rooms": {
      "utility_room": {
        "devices": [...],
        "state": {
          "humidity": 3500.0,
          "illuminance": 681.81,
          "pm10": 24.24,
          "temperature": 2852.0
        }
      }
    }
  }
}
```

### Unit Conventions (Matter Protocol)

| Variable | Raw Unit | Conversion | Example |
|----------|----------|------------|---------|
| Temperature | hundredths of °C | ÷ 100 | 2852 → 28.52°C |
| Humidity | hundredths of % | ÷ 100 | 3500 → 35.00% |
| Illuminance | lux (direct) | none | 681.81 lux |
| PM10 | µg/m³ (direct) | none | 24.24 µg/m³ |

### Why Episodes Alone Cannot Be Used for Fine-Tuning

Episodes contain the **question** and **correct answer** but
not the **reasoning process**. Fine-tuning requires complete
input → output pairs where the output is a full step-by-step
ReAct trajectory. The `gold_trajectories/` directory fills
this gap.

---

## 2. `gold_trajectories/` — LLM-Distilled ReAct Trajectories

**12 JSONL files**, one per query type + case combination.
Total: ~602 trajectories (some episodes failed validation).

### Generation Method

Episodes were processed by `llama3.2:3b` running locally via
Ollama. The teacher model was prompted to produce a complete
ReAct trajectory — Thought → Action → Action Input →
Observation → Finish — grounded in the episode's actual room
states and required actions.

**Important caveat:** The 3B teacher model is known to
hallucinate sensor values in QT1 trajectories instead of
correctly calling `get_room_states`. This is the primary
research finding of this project and explains the 0% score
on QT1 environment perception tasks. See research notes below.

### File Schema

```jsonl
{
  "seed": 1,
  "query_type": "qt1_feasible",
  "query": "How bright is the utility room right now?",
  "user_location": "kitchen",
  "base_time": "2025-08-23 11:36:54",
  "rooms": ["bathroom", "utility_room", "kitchen", ...],
  "trajectory": "Thought: I need to check the utility room illuminance.\nAction: get_room_states\nAction Input: {\"room_id\": \"utility_room\"}\nObservation: {\"illuminance_lux\": 681.81, ...}\nThought: Got the value.\nAction: finish\nAction Input: {\"answer\": \"The utility room is at 681.81 lux.\"}",
  "goals": [...],
  "required_actions": [...]
}
```

### Trajectory Counts

| File | Trajectories |
|------|-------------|
| qt1_feasible.jsonl | 50 |
| qt1_infeasible.jsonl | 53 |
| qt2_feasible.jsonl | 50 |
| qt2_infeasible.jsonl | 50 |
| qt3_feasible.jsonl | 50 |
| qt3_infeasible.jsonl | 50 |
| qt4-1_feasible.jsonl | 50 |
| qt4-1_infeasible.jsonl | 50 |
| qt4-2_feasible.jsonl | 50 |
| qt4-2_infeasible.jsonl | 50 |
| qt4-3_feasible.jsonl | 49 |
| qt4-3_infeasible.jsonl | 50 |
| **Total** | **602** |

`failed.json` — contains seeds that failed trajectory
validation after 3 retries (tool name missing from output
or no finish action).

---

## 3. `processed/` — Training Splits

Final formatted data ready for fine-tuning Mistral 7B.

### Files

| File | Samples | Purpose |
|------|---------|---------|
| `train.jsonl` | 481 | Fine-tuning |
| `val.jsonl` | 60 | Validation during training |
| `test.jsonl` | 61 | Held-out evaluation |
| `split_info.json` | — | Split metadata |

### Split Ratio

```
80% train / 10% val / 10% test
Random seed: 42
Shuffled before splitting (balanced across QT types)
```

### Sample Schema

Each line is one training sample formatted in
Mistral instruction template:

```jsonl
{
  "text": "<s>[INST] <<SYS>>\nYou are a Smart Home Assistant...<</SYS>>\n\nTime: 2025-08-23 11:36:54\nRooms: bathroom, utility_room, kitchen\nYour location: kitchen\nQuery: How bright is the utility room? [/INST]\nThought: I need to check...\nAction: get_room_states\n...\nAction: finish\nAction Input: {\"answer\": \"681.81 lux\"}</s>",
  "query_type": "qt1_feasible",
  "seed": 1
}
```

### `split_info.json`

```json
{
  "total": 602,
  "train": 481,
  "val": 60,
  "test": 61,
  "random_seed": 42,
  "model_format": "mistral-instruct"
}
```

---

## 4. `vector_db/` — Matter Protocol Index

FAISS vector index of Matter protocol cluster documentation.
Used by the SimuHome agent's `get_cluster_doc` tool for
semantic search over device specifications.

```
vector_db/
└── matter_index/    ← FAISS index files
```

Not used during fine-tuning. Used at inference time when
the agent needs to look up device cluster documentation.

---

## Data Pipeline Summary

```
benchmark/                     gold_trajectories/
  600 episodes (JSON)    →       602 trajectories (JSONL)
  (SimuHome simulator)           (llama3.2:3b teacher)
         │                               │
         └───────────────┬───────────────┘
                         ▼
                    processed/
                 481 train.jsonl
                  60 val.jsonl
                  61 test.jsonl
                         │
                         ▼
              Fine-tuned Mistral 7B
              (QLoRA, r=16, 3 epochs)
```

---

## Research Notes

### Known Issue — QT1 Teacher Hallucination

The `llama3.2:3b` teacher model used to generate
`gold_trajectories/qt1_feasible.jsonl` frequently
hallucinated sensor values instead of correctly simulating
a `get_room_states` tool call. This caused the fine-tuned
student model to inherit this incorrect behavior, resulting
in 0% on QT1 environment perception tasks during evaluation.

**Planned fix (Plan C ablation study):**
Regenerate QT1 trajectories using progressively larger
teacher models (`llama3.1:8b`, `llama3.3:70b`, `GPT-4o-mini`)
to identify the minimum teacher capability required for
correct tool-calling distillation.

### Evaluation Methodology Note

The test split (61 samples) was evaluated using both:
- **String matching** — checks if tool name appears anywhere in output (inflated, not reliable)
- **Strict ReAct parsing** — checks actual `Action:` call blocks with valid `Action Input:` (in progress)

Results from string matching only should not be directly
compared to the SimuHome paper's simulator-based evaluation.

---

## Reproducing the Data

### Regenerate Trajectories

```bash
# Install dependencies
pip install groq jsonlines tqdm ollama

# Generate using Ollama (local)
python src/scripts/generate_trajectories.py

# OR using Groq API (faster)
python src/scripts/generate_trajectories_groq.py
```

### Rebuild Training Splits

```bash
python src/scripts/build_training_data.py
```

### Audit Episode Distribution

```bash
python src/scripts/audit.py
# Expected: 50 episodes per QT per case = 600 total
```

---

## Citation

If you use this dataset or pipeline, please cite the
original SimuHome paper:

```bibtex
@inproceedings{seo2026simuhome,
  title={SimuHome: A Temporal- and Environment-Aware
         Benchmark for Smart Home LLM Agents},
  author={Gyuhyeon Seo and Jungwoo Yang and Junseong Pyo
          and Nalim Kim and Jonggeun Lee and Yohan Jo},
  booktitle={ICLR 2026},
  year={2026},
  url={https://openreview.net/forum?id=LCS1WsGvha}
}
```

---

## License

The benchmark episodes are derived from SimuHome and are
subject to **CC BY-NC-ND 4.0** (non-commercial,
no derivatives, attribution required).

Gold trajectories and processed splits are project artifacts
for research purposes only.
