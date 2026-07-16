# repro_check.py
# stage: Phase 5 — Reproducibility Prep
# produced_by: Researcher B
# Verifies that all experiment results in RESULTS.md have corresponding files
# in experiments/results/ and that metadata headers are complete.

import os
import re
import json
import glob
from datetime import datetime


def check_results_md_entries(results_md: str = "RESULTS.md") -> list:
    """Parses RESULTS.md and extracts all stage-tagged result blocks."""
    with open(results_md, "r", encoding="utf-8") as f:
        content = f.read()

    # Find all Phase 4 results blocks
    blocks = re.findall(r"## Phase 4 Results — (.+?)(?=\n##|\Z)", content, re.DOTALL)
    print(f"Found {len(blocks)} result block(s) in RESULTS.md.")
    return blocks


def check_experiment_files(results_dir: str = "experiments/results") -> list:
    """Scans results directory and validates metadata headers in each JSON."""
    required_keys = ["produced_by", "date", "stage", "reviewed_by"]
    issues = []

    json_files = glob.glob(os.path.join(results_dir, "*.json"))
    print(f"\nScanning {len(json_files)} file(s) in {results_dir}/")

    for fp in sorted(json_files):
        try:
            with open(fp, "r", encoding="utf-8") as f:
                data = json.load(f)
            meta = data.get("metadata", {})
            missing = [k for k in required_keys if not meta.get(k)]
            if missing:
                issues.append(f"MISSING KEYS {missing} in {os.path.basename(fp)}")
                print(f"  [WARN] {os.path.basename(fp)} — missing: {missing}")
            else:
                print(f"  [OK]   {os.path.basename(fp)}")
        except Exception as e:
            issues.append(f"PARSE ERROR in {os.path.basename(fp)}: {e}")
            print(f"  [ERR]  {os.path.basename(fp)} — {e}")

    return issues


def check_requirements_pinned(req_file: str = "requirements.txt") -> bool:
    """Verifies requirements.txt exists and all entries are version-pinned."""
    if not os.path.exists(req_file):
        print(f"\n[FAIL] {req_file} not found — run `uv pip freeze > requirements.txt`")
        return False

    with open(req_file, "r", encoding="utf-8") as f:
        lines = [l.strip() for l in f if l.strip() and not l.startswith("#")]

    unpinned = [l for l in lines if "==" not in l]
    if unpinned:
        print(f"\n[WARN] Unpinned packages in {req_file}: {unpinned}")
        return False

    print(f"\n[OK]   {req_file} — {len(lines)} packages pinned.")
    return True


def check_frozen_docs() -> list:
    """Checks that all key docs have STATUS: FROZEN."""
    docs_to_check = {
        "docs/rq_hypotheses.md":         "Research Questions",
        "taxonomy/citation_taxonomy.md": "Citation Taxonomy",
        "annotation/guidelines.md":      "Annotation Guidelines",
        "docs/eval_protocol.md":         "Evaluation Protocol",
        "docs/model_config.md":          "Model Configuration",
    }
    issues = []
    print("\nChecking frozen document statuses:")
    for path, label in docs_to_check.items():
        if not os.path.exists(path):
            issues.append(f"MISSING: {path}")
            print(f"  [MISS] {label} ({path})")
            continue
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        if "STATUS: FROZEN" in content:
            print(f"  [OK]   {label}")
        else:
            issues.append(f"NOT FROZEN: {path}")
            print(f"  [WARN] {label} — STATUS not FROZEN")
    return issues


def run_full_check():
    print("=" * 60)
    print("  BanLegit-Cite Reproducibility Check")
    print(f"  Run at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)

    all_issues = []

    # 1. RESULTS.md entries
    blocks = check_results_md_entries()
    if not blocks:
        all_issues.append("No Phase 4 result blocks found in RESULTS.md")

    # 2. Experiment files metadata
    file_issues = check_experiment_files()
    all_issues.extend(file_issues)

    # 3. requirements.txt pinning
    if not check_requirements_pinned():
        all_issues.append("requirements.txt missing or has unpinned packages")

    # 4. Frozen docs
    doc_issues = check_frozen_docs()
    all_issues.extend(doc_issues)

    # Summary
    print("\n" + "=" * 60)
    if all_issues:
        print(f"  [FAIL] {len(all_issues)} issue(s) found:")
        for iss in all_issues:
            print(f"    - {iss}")
    else:
        print("  [PASS] All reproducibility checks passed.")
    print("=" * 60)
    return all_issues


if __name__ == "__main__":
    issues = run_full_check()
    exit(1 if issues else 0)
