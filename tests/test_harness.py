# test_harness.py
# stage: Phase 3 Shadow Work — Scaffolding Tests

import sys
import os
import json
import pytest

# Make sure project root is on the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from scripts.evaluation.prompts import STANDARD_PROMPT, AGENTIC_PROMPT
from scripts.evaluation.retriever import LocalRetriever
from scripts.evaluation.metrics import compute_metrics, print_metrics
from scripts.evaluation.runner import BaselineRunner


# --------------------------------------------------------------------------
# 1.  Prompt template tests
# --------------------------------------------------------------------------
class TestPrompts:
    def test_standard_prompt_fills_placeholders(self):
        filled = STANDARD_PROMPT.format(
            context="The court applied…",
            citation="52 DLR (AD) 12",
            source="Dhaka Law Reports"
        )
        assert "52 DLR (AD) 12" in filled
        assert "REAL or FABRICATED" in filled

    def test_agentic_prompt_fills_placeholders(self):
        filled = AGENTIC_PROMPT.format(
            retrieved_info="Verified: 52 DLR (AD) 12 — Anwar Hossain case",
            context="The court applied…",
            citation="52 DLR (AD) 12",
            source="Dhaka Law Reports"
        )
        assert "52 DLR (AD) 12" in filled
        assert "retrieved" in filled.lower()


# --------------------------------------------------------------------------
# 2.  Retriever tests
# --------------------------------------------------------------------------
class TestRetriever:
    def test_index_builds_without_error(self):
        r = LocalRetriever(raw_data_dir="data/raw")
        assert isinstance(r.index, dict)

    def test_retrieve_known_citation_returns_info(self):
        r = LocalRetriever(raw_data_dir="data/raw")
        # At least one DLR citation must be indexable
        result = r.retrieve("41 DLR (AD) 165")
        assert isinstance(result, str)
        assert len(result) > 0

    def test_retrieve_unknown_returns_fallback_message(self):
        r = LocalRetriever(raw_data_dir="data/raw")
        result = r.retrieve("999 XYZ (UK) 9999")
        assert "No matching verified citation" in result


# --------------------------------------------------------------------------
# 3.  Metrics tests
# --------------------------------------------------------------------------
class TestMetrics:
    SAMPLE_RESULTS = [
        {"ground_truth": "REAL",       "predicted_verdict": "REAL"},
        {"ground_truth": "REAL",       "predicted_verdict": "FABRICATED"},  # FN
        {"ground_truth": "FABRICATED", "predicted_verdict": "FABRICATED"},
        {"ground_truth": "FABRICATED", "predicted_verdict": "REAL"},         # FP
        {"ground_truth": "REAL",       "predicted_verdict": "REAL"},
    ]

    def test_overall_accuracy(self):
        m = compute_metrics(self.SAMPLE_RESULTS)
        assert m["overall"]["total"] == 5
        assert m["overall"]["correct"] == 3
        assert abs(m["overall"]["accuracy"] - 0.6) < 1e-4

    def test_precision_recall_f1_computed(self):
        m = compute_metrics(self.SAMPLE_RESULTS)
        for cls in ["REAL", "FABRICATED"]:
            assert "precision" in m[cls]
            assert "recall"    in m[cls]
            assert "f1"        in m[cls]

    def test_perfect_predictions(self):
        perfect = [
            {"ground_truth": "REAL",       "predicted_verdict": "REAL"},
            {"ground_truth": "FABRICATED", "predicted_verdict": "FABRICATED"},
        ]
        m = compute_metrics(perfect)
        assert m["overall"]["accuracy"] == 1.0
        assert m["REAL"]["f1"] == 1.0
        assert m["FABRICATED"]["f1"] == 1.0


# --------------------------------------------------------------------------
# 4.  Runner tests (mock mode)
# --------------------------------------------------------------------------
class TestRunner:
    SAMPLE_ITEM = {
        "citation_id": "DLR_REAL_1",
        "citation": "52 DLR (AD) 12",
        "context": "The Appellate Division held the basic structure doctrine applies.",
        "source": "Dhaka Law Reports (AD)",
        "extracted_url": "http://example.com",
        "label": "REAL"
    }

    def test_standard_runner_returns_verdict(self):
        runner = BaselineRunner(setting="standard")
        result = runner.evaluate_instance(self.SAMPLE_ITEM)
        assert "predicted_verdict" in result
        assert result["predicted_verdict"] in ("REAL", "FABRICATED")

    def test_agentic_runner_returns_verdict(self):
        runner = BaselineRunner(setting="agentic")
        result = runner.evaluate_instance(self.SAMPLE_ITEM)
        assert "predicted_verdict" in result
        assert result["predicted_verdict"] in ("REAL", "FABRICATED")

    def test_result_contains_all_required_keys(self):
        runner = BaselineRunner(setting="standard")
        result = runner.evaluate_instance(self.SAMPLE_ITEM)
        for key in ("citation_id", "citation", "ground_truth", "predicted_verdict", "confidence", "reasoning"):
            assert key in result, f"Missing key: {key}"
