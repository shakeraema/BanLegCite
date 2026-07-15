# run_phase4.py
# stage: Phase 4 — Experimentation & Statistical Validation
# Full pipeline orchestrator: load dataset → evaluate both settings →
# compute metrics → run statistical tests → update RESULTS.md

import os
import json
import argparse
import glob
from datetime import datetime

from scripts.evaluation.runner import BaselineRunner
from scripts.evaluation.metrics import compute_metrics, print_metrics, save_metrics
from scripts.evaluation.stats import run_all_tests
from scripts.evaluation.results_reporter import (
    update_results_md, save_summary_json, build_results_table, build_stats_table
)


def load_dataset(dataset_path: str) -> list:
    """Loads and returns the data list from an annotated JSON file."""
    with open(dataset_path, "r", encoding="utf-8") as f:
        payload = json.load(f)
    return payload.get("data", [])


def evaluate_setting(items: list, setting: str, limit: int) -> list:
    """Runs the BaselineRunner over items for a given setting."""
    print(f"\n{'='*60}")
    print(f"  Evaluating — Setting: {setting.upper()} | Samples: {limit}")
    print(f"{'='*60}")
    runner = BaselineRunner(setting=setting)
    results = []
    for item in items[:limit]:
        print(f"  [{setting}] {item['citation']} ...", end=" ")
        res = runner.evaluate_instance(item)
        label = "PASS" if res["ground_truth"] == res["predicted_verdict"] else "FAIL"
        print(f"{label}  pred={res['predicted_verdict']}  gt={res['ground_truth']}")
        results.append(res)
    return results


def save_results_json(results: list, setting: str, output_dir: str = "experiments/results") -> str:
    """Persists per-setting results with CLAUDE.md-compliant metadata header."""
    os.makedirs(output_dir, exist_ok=True)
    ts  = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = os.path.join(output_dir, f"stage4_gemini_{setting}_{ts}.json")
    payload = {
        "metadata": {
            "produced_by": "run_phase4.py",
            "date": datetime.now().strftime("%Y-%m-%d"),
            "reviewed_by": "pending",
            "stage": "Phase 4 — Experimentation",
            "setting": setting,
            "commit": "pending"
        },
        "results": results
    }
    with open(path, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)
    print(f"  => Saved to {path}")
    return path


def main():
    parser = argparse.ArgumentParser(description="Phase 4 full evaluation pipeline.")
    parser.add_argument("--dataset", type=str, default=None,
                        help="Path to annotated JSON (default: merge all data/annotated/*.json)")
    parser.add_argument("--limit", type=int, default=30,
                        help="Max samples to evaluate per setting (default: 30)")
    args = parser.parse_args()

    # ── 1. Load dataset ──────────────────────────────────────────────
    if args.dataset:
        all_items = load_dataset(args.dataset)
    else:
        all_items = []
        for fp in sorted(glob.glob("data/annotated/*.json")):
            all_items.extend(load_dataset(fp))
    print(f"\nLoaded {len(all_items)} items from annotated dataset.")

    # ── 2. Evaluate both settings ────────────────────────────────────
    std_results = evaluate_setting(all_items, "standard", args.limit)
    agt_results = evaluate_setting(all_items, "agentic",  args.limit)

    save_results_json(std_results, "standard")
    save_results_json(agt_results, "agentic")

    # ── 3. Compute metrics ───────────────────────────────────────────
    print("\n--- Standard Setting Metrics ---")
    std_metrics = compute_metrics(std_results)
    print_metrics(std_metrics)

    print("--- Agentic Setting Metrics ---")
    agt_metrics = compute_metrics(agt_results)
    print_metrics(agt_metrics)

    save_metrics(std_metrics, tag="stage4_standard")
    save_metrics(agt_metrics, tag="stage4_agentic")

    # ── 4. Run pre-registered statistical tests ──────────────────────
    print("\n--- Pre-registered Statistical Tests ---")
    stat_results = run_all_tests(std_results, agt_results)
    for h, res in stat_results.items():
        print(f"  {res['interpretation']}")

    # ── 5. Save summary & update RESULTS.md ─────────────────────────
    save_summary_json(std_metrics, agt_metrics, stat_results)
    update_results_md(std_metrics, agt_metrics, stat_results)

    print("\n[DONE] Phase 4 pipeline complete. See experiments/results/ and RESULTS.md.")


if __name__ == "__main__":
    main()
