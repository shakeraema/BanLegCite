# Implementation Plan: Phase 3 Shadow Work (Baseline Evaluation Harness)

This plan details the construction of the **Baseline Evaluation Harness** during Phase 3. B operates independently of the human annotation process, writing and testing the evaluation harness against synthetic data so it is ready to execute immediately when Phase 4 begins.

## User Review Required

> [!IMPORTANT]
> - **Evaluation Settings:** We will implement two core prompting configurations for the baseline models:
>   1. **Standard Setting:** Zero-shot/Few-shot direct verification prompt containing context and citation.
>   2. **Agentic Setting:** Retrieval-augmented prompting, incorporating facts fetched from a simulated local document index over the scraped corpus.
> - **W&B Mock/Real Runs:** We will verify that runs are logged to W&B. Ensure you have the `WANDB_API_KEY` set if you wish to run a live test; otherwise, the harness will fallback to local file logging.

## Proposed Changes

We will create the evaluation framework under `scripts/evaluation/` and `tests/`:

### Component: Evaluation Runner & Prompts

#### [NEW] [prompts.py](file:///c:/Users/user/Desktop/BanLegitCite/scripts/evaluation/prompts.py)
- Defines prompt templates for standard direct prompts and agentic retrieval-augmented prompts.
#### [NEW] [runner.py](file:///c:/Users/user/Desktop/BanLegitCite/scripts/evaluation/runner.py)
- Main baseline model execution class. Connects to the LLM (Gemini or placeholder mock client), queries prompts, parses predictions (REAL/FABRICATED), and logs outputs.

### Component: Retrieval (Agentic Setting)

#### [NEW] [retriever.py](file:///c:/Users/user/Desktop/BanLegitCite/scripts/evaluation/retriever.py)
- Keyword/BM25 local index retriever matching citations to the scraped document corpus to construct agentic context.

### Component: Pipeline Logging & Metrics

#### [NEW] [metrics.py](file:///c:/Users/user/Desktop/BanLegitCite/scripts/evaluation/metrics.py)
- Metrics calculator (Accuracy, F1, Precision, Recall, Confusion Matrix) and integration with `wb_config.py` for logging directly to Weights & Biases.

### Component: Scaffolding Tests

#### [NEW] [test_harness.py](file:///c:/Users/user/Desktop/BanLegitCite/tests/test_harness.py)
- Pytest script testing mock inference, retriever lookups, metric computation, and logging functions.

---

## Verification Plan

### Automated Tests
- Run unit tests with `pytest tests/test_harness.py`.
- Run baseline harness on 5 sample inputs using:
  ```bash
  .venv\Scripts\python -m scripts.evaluation.runner --limit 5 --setting standard
  .venv\Scripts\python -m scripts.evaluation.runner --limit 5 --setting agentic
  ```

### Manual Verification
- Confirm local prediction results are saved in `experiments/results/` and metadata is properly formatted.
