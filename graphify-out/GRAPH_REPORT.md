# Graph Report - BanLegitCite  (2026-07-16)

## Corpus Check
- 42 files · ~11,496 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 265 nodes · 336 edges · 26 communities (19 shown, 7 thin omitted)
- Extraction: 96% EXTRACTED · 4% INFERRED · 0% AMBIGUOUS · INFERRED: 12 edges (avg confidence: 0.5)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- README.md
- BanLegit-Cite — Project Instructions for AI Agents
- Annotation Guidelines — BanLegit-Cite
- Citation Taxonomy — BanLegit-Cite
- Evaluation Protocol — BanLegit-Cite
- Novelty Report — BanLegit-Cite
- Research Log — BanLegit-Cite
- BanLegit-Cite
- Fabrication Review Log — BanLegit-Cite
- RESULTS.md — BanLegit-Cite
- graphify.md
- graphify.md
- Phase Roadmap for Researcher B
- Decision Log — BanLegit-Cite
- wb_config.py
- dvc_setup.py
- setup_label_studio.sh
- run_spot_check
- compute_metrics
- repro_check.py
- run_all_tests
- ReviewerSim
- E2 Reviewer Simulation Report

## God Nodes (most connected - your core abstractions)
1. `BaselineRunner` - 17 edges
2. `LocalRetriever` - 15 edges
3. `BaseScraper` - 12 edges
4. `main()` - 10 edges
5. `compute_metrics()` - 9 edges
6. `BanLegit-Cite — Project Instructions for AI Agents` - 9 edges
7. `run_all_tests()` - 8 edges
8. `update_results_md()` - 6 edges
9. `ALRScraper` - 6 edges
10. `BLCScraper` - 6 edges

## Surprising Connections (you probably didn't know these)
- `TestMetrics` --uses--> `LocalRetriever`  [INFERRED]
  tests/test_harness.py → scripts/evaluation/retriever.py
- `TestMetrics` --uses--> `BaselineRunner`  [INFERRED]
  tests/test_harness.py → scripts/evaluation/runner.py
- `TestPrompts` --uses--> `LocalRetriever`  [INFERRED]
  tests/test_harness.py → scripts/evaluation/retriever.py
- `TestRetriever` --uses--> `LocalRetriever`  [INFERRED]
  tests/test_harness.py → scripts/evaluation/retriever.py
- `TestRunner` --uses--> `LocalRetriever`  [INFERRED]
  tests/test_harness.py → scripts/evaluation/retriever.py

## Import Cycles
- None detected.

## Communities (26 total, 7 thin omitted)

### Community 0 - "README.md"
Cohesion: 0.06
Nodes (29): Evaluation Protocol — BanLegit-Cite, Freeze Checklist, Pre-registered Statistical Tests, Primary Metrics, Freeze Checklist, Hypotheses, Research Question (RQ), Research Questions & Hypotheses — BanLegit-Cite (+21 more)

### Community 1 - "BanLegit-Cite — Project Instructions for AI Agents"
Cohesion: 0.20
Nodes (9): 1. WHAT THIS PROJECT IS, 2. EVIDENCE-LOGGING RULES (mandatory for all agent outputs), 3. BATCH-AND-GATE RULES (for fabrication generation & annotation), 4. PROVENANCE-METADATA REQUIREMENTS, 5. FROZEN DECISIONS — DO NOT MODIFY WITHOUT JOINT SIGN-OFF, 6. GIT CONVENTIONS, 7. FILE STRUCTURE (do not reorganize without updating this file), 8. RESEARCHER TRACK ASSIGNMENTS (+1 more)

### Community 2 - "Annotation Guidelines — BanLegit-Cite"
Cohesion: 0.22
Nodes (8): Adjudication Protocol, Annotation Guidelines — BanLegit-Cite, Edge Cases (to be expanded during Phase 1), FABRICATED, Freeze Checklist, Legitimacy Labeling Rules, REAL, Task Definition

### Community 4 - "Evaluation Protocol — BanLegit-Cite"
Cohesion: 0.12
Nodes (14): Agentic Prompt, date: 2026-07-15, DO NOT MODIFY after Phase 4 results are logged. Any change requires a, Evaluation Settings, Inference Parameters, joint decision-log entry per CLAUDE.md Section 5., Model & Prompt Configuration — BanLegit-Cite, Model Registry (+6 more)

### Community 5 - "Novelty Report — BanLegit-Cite"
Cohesion: 0.14
Nodes (9): ABC, ALRScraper, BaseScraper, Fetch URL with rate-limiting delay and safety error handling., Perform scraping logic. To be implemented by sub-classes., Save scraped results with the mandatory metadata header., BLCScraper, DLRScraper (+1 more)

### Community 6 - "Research Log — BanLegit-Cite"
Cohesion: 0.40
Nodes (4): [2026-07-15] Joint, Entries, Log Format, Research Log — BanLegit-Cite

### Community 7 - "BanLegit-Cite"
Cohesion: 0.47
Nodes (5): process_fabrications(), query_gemini_fabrication(), Uses Gemini API to fabricate a citation and rewrite the legal proposition contex, Fallback function to perform programmatic high-fidelity citation fabrication., rule_based_fabrication()

### Community 8 - "Fabrication Review Log — BanLegit-Cite"
Cohesion: 0.50
Nodes (3): Entries, Fabrication Review Log — BanLegit-Cite, Log Format

### Community 9 - "RESULTS.md — BanLegit-Cite"
Cohesion: 0.29
Nodes (6): Dataset Card for BanLegit-Cite, Dataset Description, Dataset Licensing & Copyright, Dataset Structure, Dataset Summary, Supported Tasks

### Community 12 - "Phase Roadmap for Researcher B"
Cohesion: 0.17
Nodes (11): Automated Tests, Component: Git Workflow, Component: Packaging & Release Preparation, Component: Reviewer Simulation (E2 Agent), Implementation Plan: Phase 6 (Reproducibility, Release & Reviewer Simulation), [NEW] [dataset_card.md](file:///c:/Users/user/Desktop/BanLegitCite/data/dataset_card.md), [NEW] [release_package.py](file:///c:/Users/user/Desktop/BanLegitCite/scripts/utils/release_package.py), [NEW] [reviewer_sim.py](file:///c:/Users/user/Desktop/BanLegitCite/scripts/evaluation/reviewer_sim.py) (+3 more)

### Community 13 - "Decision Log — BanLegit-Cite"
Cohesion: 0.17
Nodes (11): Interpretations, Interpretations, Paper Table → Result Mapping, Performance Metrics, Performance Metrics, Phase 4 Results — 2026-07-15 23:19:50, Phase 4 Results — 2026-07-15 23:42:48, Pre-registered Statistical Tests (+3 more)

### Community 14 - "wb_config.py"
Cohesion: 0.10
Nodes (15): LocalRetriever, Constructs a basic map from citation strings to case metadata and holdings., Looks up the citation in the index and returns verified holding text., BaselineRunner, Queries model or falls back to high-fidelity simulated response., Parses standard formatting from model text output., Evaluates a single citation record., run_evaluation() (+7 more)

### Community 19 - "compute_metrics"
Cohesion: 0.09
Nodes (31): compute_metrics(), log_to_wandb(), print_metrics(), Logs all metrics to an active W&B run., Persists metric JSON alongside the results file., Computes Accuracy, Precision, Recall, F1-score, and per-class breakdown.     Re, save_metrics(), build_results_table() (+23 more)

### Community 22 - "repro_check.py"
Cohesion: 0.29
Nodes (9): check_experiment_files(), check_frozen_docs(), check_requirements_pinned(), check_results_md_entries(), Parses RESULTS.md and extracts all stage-tagged result blocks., Scans results directory and validates metadata headers in each JSON., Verifies requirements.txt exists and all entries are version-pinned., Checks that all key docs have STATUS: FROZEN. (+1 more)

### Community 23 - "run_all_tests"
Cohesion: 0.29
Nodes (6): Abstract, Draft Paper: BanLegit-Cite, Methodology, Reproducibility, Results, Title

### Community 25 - "E2 Reviewer Simulation Report"
Cohesion: 0.40
Nodes (4): Actionable Action Items / Fatal Flaw Flags, E2 Reviewer Simulation Report, Numerical Scores (Scale 1-5), Summary Evaluation

## Knowledge Gaps
- **80 isolated node(s):** `setup_label_studio.sh script`, `graphify`, `Workflow: graphify`, `1. WHAT THIS PROJECT IS`, `2. EVIDENCE-LOGGING RULES (mandatory for all agent outputs)` (+75 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **7 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `BaselineRunner` connect `wb_config.py` to `compute_metrics`?**
  _High betweenness centrality (0.028) - this node is a cross-community bridge._
- **Why does `LocalRetriever` connect `wb_config.py` to `compute_metrics`?**
  _High betweenness centrality (0.015) - this node is a cross-community bridge._
- **Are the 5 inferred relationships involving `BaselineRunner` (e.g. with `LocalRetriever` and `TestMetrics`) actually correct?**
  _`BaselineRunner` has 5 INFERRED edges - model-reasoned connections that need verification._
- **Are the 5 inferred relationships involving `LocalRetriever` (e.g. with `BaselineRunner` and `TestMetrics`) actually correct?**
  _`LocalRetriever` has 5 INFERRED edges - model-reasoned connections that need verification._
- **Are the 3 inferred relationships involving `BaseScraper` (e.g. with `ALRScraper` and `BLCScraper`) actually correct?**
  _`BaseScraper` has 3 INFERRED edges - model-reasoned connections that need verification._
- **What connects `setup_label_studio.sh script`, `graphify`, `Workflow: graphify` to the rest of the system?**
  _80 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `README.md` be split into smaller, more focused modules?**
  _Cohesion score 0.05714285714285714 - nodes in this community are weakly interconnected._