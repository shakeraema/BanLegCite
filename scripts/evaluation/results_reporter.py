# results_reporter.py
# stage: Phase 4 — Experimentation & Statistical Validation
# Generates formatted results tables for RESULTS.md and experiment summary JSON.

import os
import json
from datetime import datetime
from scripts.evaluation.metrics import compute_metrics, print_metrics
from scripts.evaluation.stats import run_all_tests


def build_results_table(std_metrics: dict, agt_metrics: dict) -> str:
    """Renders a markdown results table for paper/RESULTS.md."""
    header = (
        "| Setting  | Accuracy | REAL P | REAL R | REAL F1 | FAB P | FAB R | FAB F1 |\n"
        "|----------|----------|--------|--------|---------|-------|-------|--------|\n"
    )

    def row(name, m):
        o  = m["overall"]
        r  = m["REAL"]
        f  = m["FABRICATED"]
        return (
            f"| {name:<8} | {o['accuracy']:.4f}   | "
            f"{r['precision']:.4f} | {r['recall']:.4f} | {r['f1']:.4f}   | "
            f"{f['precision']:.4f} | {f['recall']:.4f} | {f['f1']:.4f}   |"
        )

    return header + row("Standard", std_metrics) + "\n" + row("Agentic", agt_metrics) + "\n"


def build_stats_table(stat_results: dict) -> str:
    """Renders a markdown statistical tests table."""
    rows = []
    for h, res in stat_results.items():
        sig = "✅ Yes" if res["significant"] else "❌ No"
        rows.append(
            f"| {h} | {res['test']} | "
            f"{res.get('chi2', res.get('statistic', 'N/A')):.4f} | "
            f"{res['p_value']:.6f} | {sig} |"
        )
    header = (
        "| Hypothesis | Test | Statistic | p-value | Significant (α=0.05) |\n"
        "|------------|------|-----------|---------|----------------------|\n"
    )
    return header + "\n".join(rows) + "\n"


def update_results_md(std_metrics: dict, agt_metrics: dict,
                      stat_results: dict, results_path: str = "RESULTS.md"):
    """Appends a dated results block to RESULTS.md."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    block = f"""
---

## Phase 4 Results — {timestamp}

> produced_by: results_reporter.py  
> stage: Phase 4 — Experimentation & Statistical Validation  
> reviewed_by: pending  

### Performance Metrics

{build_results_table(std_metrics, agt_metrics)}

### Pre-registered Statistical Tests

{build_stats_table(stat_results)}

### Interpretations

"""
    for h, res in stat_results.items():
        block += f"- **{h}:** {res['interpretation']}\n"

    with open(results_path, "a", encoding="utf-8") as f:
        f.write(block)

    print(f"RESULTS.md updated at {results_path}")


def save_summary_json(std_metrics: dict, agt_metrics: dict,
                      stat_results: dict, output_dir: str = "experiments/results") -> str:
    """Saves a combined summary JSON with metadata headers."""
    os.makedirs(output_dir, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = os.path.join(output_dir, f"stage4_summary_{ts}.json")

    summary = {
        "metadata": {
            "produced_by": "results_reporter.py",
            "date": datetime.now().strftime("%Y-%m-%d"),
            "stage": "Phase 4 — Experimentation & Statistical Validation",
            "reviewed_by": "pending",
            "commit": "pending"
        },
        "performance": {
            "standard": std_metrics,
            "agentic":  agt_metrics
        },
        "statistical_tests": stat_results
    }

    with open(path, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)
    print(f"Summary JSON saved to {path}")
    return path
