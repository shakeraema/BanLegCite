# Implementation Plan - Phase 5: Synthesis, Reporting, and Final Release Packaging

This plan outlines the final steps to complete the BanLegit-Cite project, transitioning from simulated pilot data to real-world deployment, double-annotation adjudication, model re-evaluation, and packaging the final research artifact for publication.

---

## User Review Required

> [!IMPORTANT]
> **Adjudication Lock:** Before finalizing the dataset, the 15 Medium/Low confidence tasks identified in the Senior Review Adjudication Log must be resolved by a third annotator with physical DLR print or primary Chancery Law Chronicles access.
> **Google Form Launch:** The compiled Google Apps Script `generate_google_form.js` needs to be run in script.google.com to collect real student annotator responses.

---

## Open Questions

There are no remaining open questions at this stage. All taxonomies, verification rules, and script pipelines are fully aligned and tested.

---

## Proposed Tasks

### 1. Pilot Adjudication & Gold Set Locking
* Run double-annotator validation passes using `convert_google_sheet_to_label_studio.py` and `calculate_iaa.py` on the collected responses CSV.
* Manually adjudicate disagreements in `adjudication_sheet.md` and generate the final ground-truth labels (`annotation/project_export.json`).

### 2. Model Baseline Re-Evaluation
* Run the evaluation script `run_phase4.py` using the verified human gold standard.
* Log accuracy, precision, recall, and F1 metrics for both standard prompting and agentic settings.
* Verify performance gain in agentic settings (reproducing the target metrics in `RESULTS.md`).

### 3. Release Packaging & Verification
* Run `release_package.py` to generate the finalized `data/release/banlegit_cite_dataset.json` and `.csv` files along with their SHA256 checksums.
* Execute `repro_check.py` to check all pinned dependencies, frozen documentation files, and metrics directories.
* Execute `reviewer_sim.py` to confirm that no fatal flaws or copyright leaks exist.

---

## Verification Plan

### Automated Tests
* Run downstream pipelines to ensure zero failures:
  ```bash
  venv/bin/python3 scripts/utils/repro_check.py
  venv/bin/python3 scripts/utils/release_package.py
  venv/bin/python3 scripts/evaluation/reviewer_sim.py
  ```

### Manual Verification
* Review `logs/reviewer_simulation_report.md` to confirm there are no missing metadata annotations or licensing issues.
