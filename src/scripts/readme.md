# Data Distillation Pipeline Scripts

This directory contains the complete data distillation and dataset
construction pipeline used for the SimuHome-Edge project.

The pipeline converts raw SimuHome benchmark episodes into
high-quality ReAct-style trajectories using LLMs, then formats
them into training-ready instruction datasets for fine-tuning
smart-home agents.

---

# Pipeline Overview

```text
benchmark/ (raw episodes)
        │
        ▼
generate_trajectories_*.py
        │
        ▼
gold_trajectories/ (ReAct trajectories)
        │
        ▼
build_training_data.py
        │
        ▼
processed/ (train / val / test splits)
        │
        ▼
Fine-tuning (QLoRA / SFT)
```

---

# Directory Structure

```text
src/scripts/
├── generate_trajectories_ollama.py
├── generate_trajectories_groq.py
├── build_training_data.py
└── README.md
```

---
# Environment Variables

Never hardcode API keys inside scripts.

Export API keys from your terminal instead.

## Groq API

Temporary session:

```bash
export GROQ_API_KEY="your_api_key_here"
```

Permanent setup:

```bash
echo 'export GROQ_API_KEY="your_api_key_here"' >> ~/.bashrc
source ~/.bashrc
```

Verify:

```bash
echo $GROQ_API_KEY
```

---
# Scripts

---

## 1. `generate_trajectories_ollama.py`

Generate ReAct trajectories locally using Ollama models.

### Features

- Uses local LLMs through Ollama
- Supports:
  - `llama3.2:3b`
  - `qwen`
  - other Ollama-compatible models
- Resume support
- Automatic validation
- Retry mechanism
- QT-specific prompting
- Structured ReAct trajectory generation

### Input

```text
data/benchmark/*.json
```

### Output

```text
data/gold_trajectories/*.jsonl
```

### Run

```bash
ollama serve

python src/scripts/generate_trajectories_ollama.py
```

### Example Generated Trajectory

```text
Thought: I need to check the utility room illuminance.
Action: get_room_states
Action Input: {"room_id": "utility_room"}
Observation: {"illuminance_lux": 681.81}

Thought: I now know the brightness level.
Action: finish
Action Input: {"answer": "The utility room is currently 681.81 lux."}
```

---

## 2. `generate_trajectories_groq.py`

Generate trajectories using the Groq API.

This is significantly faster than local CPU inference.

### Features

- Fast cloud inference
- Rate-limit handling
- Automatic retries
- Resume support
- Validation checks
- Same output format as Ollama version

### Supported Models

- `llama-3.1-8b-instant`
- Other Groq-supported models

### Setup

Install dependencies:

```bash
pip install groq jsonlines tqdm
```

Add your API key:

```python
GROQ_API_KEY = "your_api_key"
```

### Run

```bash
python src/scripts/generate_trajectories_groq.py
```

---

## 3. `build_training_data.py`

Build final train/validation/test splits for supervised fine-tuning.

This script converts distilled trajectories into the
Mistral instruction-tuning format.

### Features

- Merges trajectories with original benchmark episodes
- Formats samples into Mistral chat template
- Creates:
  - train split
  - validation split
  - test split
- Random shuffling
- Reproducible splitting

### Split Ratio

```text
Train : 80%
Val   : 10%
Test  : 10%
```

### Output

```text
data/processed/
├── train.jsonl
├── val.jsonl
├── test.jsonl
└── split_info.json
```

### Run

```bash
python src/scripts/build_training_data.py
```

---


# Reusing the Pipeline With Different Models

The pipeline is model-agnostic and can be reused with
different teacher models for trajectory distillation.

---

## Local Models (Ollama)

Inside:

```python
MODEL = "llama3.2:3b"
```

You can replace with:

```python
MODEL = "qwen2.5:7b"
MODEL = "mistral:7b"
MODEL = "llama3.1:8b"
```

Pull models using:

```bash
ollama pull llama3.1:8b
ollama pull qwen2.5:7b
```

Run:

```bash
python src/scripts/generate_trajectories_ollama.py
```

---

## Groq Models

Inside:

```python
MODEL = "llama-3.1-8b-instant"
```

You can swap to any Groq-supported model.

Example:

```python
MODEL = "llama-3.3-70b-versatile"
MODEL = "mixtral-8x7b-32768"
```

Run:

```bash
python src/scripts/generate_trajectories_groq.py
```

---

# Recommended Teacher Models

| Model | Quality | Speed | Cost |
|---|---|---|---|
| llama3.2:3b | Low-Medium | Fast | Free |
| qwen2.5:7b | Medium | Medium | Free |
| llama3.1:8b | Good | Medium | Free |
| llama3.3:70b | Very Good | Fast (API) | Paid/API |
| GPT-4o-mini | Excellent | Fast | Paid |

---

# Important Research Insight

Teacher model quality strongly affects distilled trajectories.

Smaller models may:
- hallucinate observations
- skip tool calls
- ignore required actions

Larger models generally produce:
- cleaner ReAct traces
- more reliable tool usage
- better downstream fine-tuning performance
# Dataset Flow

## Step 1 — Raw Benchmark Episodes

Located in:

```text
data/benchmark/
```

Each episode contains:

- smart-home configuration
- room states
- devices
- user query
- evaluation goals
- required actions

---

## Step 2 — Trajectory Distillation

The generation scripts:

- read benchmark episodes
- construct prompts
- ask the teacher model to generate ReAct trajectories
- validate outputs
- save trajectories

Generated trajectories are stored in:

```text
data/gold_trajectories/
```

---

## Step 3 — Training Dataset Construction

`build_training_data.py`:

- loads trajectories
- matches them with original episodes
- formats them into instruction-tuning samples
- creates train/val/test splits

Final processed dataset:

```text
data/processed/
```

---

# ReAct Format

All trajectories follow the ReAct framework:

```text
Thought:
Action:
Action Input:
Observation:
```

and terminate with:

```text
Action: finish
```

---

# Supported Query Types

| Query Type | Description |
|---|---|
| QT1 | Environment perception |
| QT2 | Implicit intent understanding |
| QT3 | Explicit device control |
| QT4-1 | Future scheduling |
| QT4-2 | Dependency scheduling |
| QT4-3 | Concurrent scheduling |

Each type contains:
- feasible cases
- infeasible cases

---

# Validation Rules

Generated trajectories are validated to ensure:

- all required tools are called
- `finish` action exists
- formatting is correct
- required actions appear in output

Failed generations are retried automatically.

---

# Dependencies

Install required packages:

```bash
pip install:
pip install jsonlines tqdm ollama groq
```

---

# Recommended Workflow

## Option A — Local Generation

```bash
ollama serve

python src/scripts/generate_trajectories_ollama.py
python src/scripts/build_training_data.py
```

---

## Option B — Groq API (Faster)

```bash
python src/scripts/generate_trajectories_groq.py
python src/scripts/build_training_data.py
```

---

# Research Notes

This pipeline was designed for studying:

- LLM tool-calling behavior
- ReAct trajectory distillation
- smart-home agents
- temporal reasoning
- environment-aware assistants
- teacher → student fine-tuning

One key finding observed during experimentation:

> Small teacher models (e.g., 3B) may hallucinate sensor values
> instead of correctly invoking tools, especially in QT1 tasks.

This directly impacts downstream fine-tuning quality.

---

# Future Improvements

Planned upgrades include:

- larger teacher models
- simulator-based validation
- strict trajectory parsing
- trajectory repair pipelines
- multi-agent distillation
- synthetic augmentation
- preference optimization (DPO)

---

# License

This pipeline is intended for research and educational use.

Original benchmark:
SimuHome (ICLR 2026)

Generated trajectories and processed datasets are research artifacts.
