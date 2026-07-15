# Implementation Plan: Phase 6 (Reproducibility, Release & Reviewer Simulation)

This plan details the implementation of **Phase 6** tasks, which include setting up the reviewer simulation runner, completing end-to-end reproducibility dry-runs, and preparing configuration catalogs for release packaging.

## User Review Required

> [!IMPORTANT]
> - **Paper Draft Location:** The Reviewer Simulation (E2) runs against the final paper draft. Since the draft is not yet fully written, we will configure the simulation to scan a placeholder file (`docs/draft_placeholder.md`) so the harness is verified and ready.
> - **Zenodo & HF Releases:** The actual dataset upload will be simulated using script endpoints that check schema alignment and catalog metadata.

## Proposed Changes

We will create the release and simulation infrastructure:

### Component: Reviewer Simulation (E2 Agent)

#### [NEW] [reviewer_sim.py](file:///c:/Users/user/Desktop/BanLegitCite/scripts/evaluation/reviewer_sim.py)
- Evaluates the draft against the pre-registered 5 standard review criteria (Clarity, Novelty, Methodology correctness, Citation integrity, and Reproducibility details).

### Component: Packaging & Release Preparation

#### [NEW] [dataset_card.md](file:///c:/Users/user/Desktop/BanLegitCite/data/dataset_card.md)
- Dataset documentation card for HuggingFace Datasets Hub including licensing, language, features, and source attribution.
#### [NEW] [release_package.py](file:///c:/Users/user/Desktop/BanLegitCite/scripts/utils/release_package.py)
- Final script to package clean CSV files, build checksums (`sha256`), and verify licensing/copyright policies before push.

### Component: Git Workflow
- Checkout git branch `stage6-release`.

---

## Verification Plan

### Automated Tests
- Run reviewer simulation on draft placeholder using:
  ```bash
  .venv\Scripts\python -m scripts.evaluation.reviewer_sim
  ```
- Run final release packaging verification:
  ```bash
  .venv\Scripts\python -m scripts.utils.release_package
  ```
