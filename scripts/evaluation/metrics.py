# metrics.py
# stage: Phase 3 Shadow Work — Evaluation Harness

import os
import json
from collections import defaultdict

def compute_metrics(results: list) -> dict:
    """
    Computes Accuracy, Precision, Recall, F1-score, and per-class breakdown.
    Returns a summary dict.
    """
    labels = ["REAL", "FABRICATED"]
    tp = defaultdict(int)
    fp = defaultdict(int)
    fn = defaultdict(int)
    tn = defaultdict(int)

    for r in results:
        gt = r["ground_truth"]
        pred = r["predicted_verdict"]
        for label in labels:
            if gt == label and pred == label:
                tp[label] += 1
            elif gt != label and pred == label:
                fp[label] += 1
            elif gt == label and pred != label:
                fn[label] += 1
            else:
                tn[label] += 1

    metrics = {}
    for label in labels:
        precision = tp[label] / (tp[label] + fp[label]) if (tp[label] + fp[label]) > 0 else 0.0
        recall    = tp[label] / (tp[label] + fn[label]) if (tp[label] + fn[label]) > 0 else 0.0
        f1        = (2 * precision * recall) / (precision + recall) if (precision + recall) > 0 else 0.0
        metrics[label] = {
            "precision": round(precision, 4),
            "recall":    round(recall,    4),
            "f1":        round(f1,        4),
            "tp": tp[label], "fp": fp[label],
            "fn": fn[label], "tn": tn[label],
        }

    total = len(results)
    correct = sum(1 for r in results if r["ground_truth"] == r["predicted_verdict"])
    metrics["overall"] = {
        "accuracy": round(correct / total, 4) if total > 0 else 0.0,
        "total":    total,
        "correct":  correct,
    }
    return metrics


def print_metrics(metrics: dict):
    print("\n=== Evaluation Metrics ===")
    overall = metrics.get("overall", {})
    print(f"Overall Accuracy : {overall.get('accuracy', 0):.2%}  ({overall.get('correct')}/{overall.get('total')})")
    for cls in ["REAL", "FABRICATED"]:
        m = metrics.get(cls, {})
        print(f"  [{cls}]  P={m.get('precision', 0):.4f}  R={m.get('recall', 0):.4f}  F1={m.get('f1', 0):.4f}")
    print("==========================\n")


def log_to_wandb(run, metrics: dict, setting: str):
    """Logs all metrics to an active W&B run."""
    flat = {"setting": setting}
    flat["accuracy"] = metrics["overall"]["accuracy"]
    for cls in ["REAL", "FABRICATED"]:
        for k, v in metrics.get(cls, {}).items():
            flat[f"{cls.lower()}_{k}"] = v
    run.log(flat)
    print("Metrics logged to W&B.")


def save_metrics(metrics: dict, output_dir: str = "experiments/results", tag: str = "eval"):
    """Persists metric JSON alongside the results file."""
    os.makedirs(output_dir, exist_ok=True)
    from datetime import datetime
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = os.path.join(output_dir, f"{tag}_metrics_{ts}.json")
    output = {
        "metadata": {
            "produced_by": "metrics.py",
            "date": datetime.now().strftime("%Y-%m-%d"),
            "reviewed_by": "pending",
            "stage": "Phase 4 — Experimentation & Statistical Validation",
        },
        "metrics": metrics
    }
    with open(path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    print(f"Metrics saved to {path}")
    return path
