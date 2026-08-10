# BanLegit-Cite: A Legal Citation Legitimacy Benchmark Dataset for the Bangladeshi Jurisdiction

Official repository for **BanLegit-Cite**, an academic legal NLP research project targeting citation legitimacy verification and hallucination auditing in the Bangladeshi jurisdiction. 

---

## 👥 Authors & Affiliations

*   **Shakera Jannat Ema** (Dept. of Software Engineering, Shahjalal University of Science and Technology, Sylhet, Bangladesh)
*   **M. M. Zahid Hasan** (Dept. of Software Engineering, Shahjalal University of Science and Technology, Sylhet, Bangladesh)

### 🖋️ Student Annotators
*   **Shakila Sharmin** (Islamic University, Kushtia, Bangladesh)
*   **Haris Rahman Antor** (Leading University, Sylhet, Bangladesh)

---

## 📖 Overview

Large Language Models (LLMs) frequently hallucinate legal authorities, statutory sections, and case precedents, posing severe risks for automated advisory systems. While Retrieval-Augmented Generation (RAG) improves output quality, post-generation citation auditing remains an open challenge, especially in low-resource common law jurisdictions like Bangladesh where transitional naming conventions (e.g., Appellate Division vs. High Court Division splits) introduce lexical naming inconsistencies.

**BanLegit-Cite** is the first gold-standard benchmark and evaluation protocol designed to audit legal citation legitimacy in Bangladesh. It includes a structured fabrication taxonomy consisting of:
*   **Statutory Fabrications (S1–S5):** Non-existent sections, wrong Act attributions, misstated content, cross-jurisdictional statute bleed, and repealed/superseded laws.
*   **Precedent Fabrications (P1–P5):** Non-existent cases, wrong citation locators, misattributed holdings, wrong court levels, and cross-jurisdictional precedent bleed.

---

## 📊 Experimental Results

We benchmarked **Gemini 3.5 Flash** on the final gold-standard dataset of **90 unique tasks** (45 real, 45 fabricated cases) spanning major reporters (Dhaka Law Reports [DLR], Bangladesh Law Chronicles [BLC], and Apex Law Reports [ALR]).

### Primary Performance Metrics
| Verification Setting | Accuracy | REAL Precision | REAL Recall | REAL F1 | FAB Precision | FAB Recall | FAB F1 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Standard (Zero-Shot)** | **78.89%** | 0.7955 | 0.7778 | 0.7865 | 0.7826 | 0.8000 | 0.7912 |
| **Agentic (RAG-Augmented)** | **100.00%** | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |

### Pre-Registered Statistical Hypotheses
*   **H1 (LLM vs. Human Expert Baseline):** **Supported** ($p = 0.008829$, $\alpha = 0.05$). Standard prompting performs statistically significantly worse than human legal annotators due to compliance bias (defaulting to accepting fabricated references).
*   **H2 (Agentic vs. Standard Confidence):** **Supported** ($W = 0.0, p = 0.000019$, $\alpha = 0.05$). The agentic setting produces statistically significantly higher confidence scores on correct predictions compared to standard prompting.
*   **H3 (Reporter Category Bias):** **Not Supported** ($p = 0.229680$, $\alpha = 0.05$). The model's verification accuracy is robust and does not vary significantly across different citation reporter sub-corpora.

---

## 🛠️ Installation & Setup

### Prerequisites
*   **Python:** CPython `3.10.8` (or compatible 3.10+ runtime)
*   **Gemini API Key:** Required for live model queries (set as `GEMINI_API_KEY` in environment)

### Environment Initialization
```bash
# 1. Clone the repository
git clone https://github.com/ZahidHasan7/BanLegit-Cite.git
cd BanLegit-Cite

# 2. Set up virtual environment and install pinned dependencies
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

---

## 🚀 Running Pipelines & Checks

### 1. Programmatic Citation Fabrication
Mutate raw verified precedents into realistic fabricated cases:
```bash
GEMINI_API_KEY="your-api-key" python3 scripts/fabrication/fabricator.py
```

### 2. Live Model Baseline Evaluation
Evaluate both standard and agentic settings across all 90 benchmark items:
```bash
GEMINI_API_KEY="your-api-key" PYTHONPATH=. python3 scripts/evaluation/run_phase4.py --limit 90
```

### 3. Reproducibility Verification
Run the automated reproducibility test suite to verify requirements and results integrity:
```bash
python3 scripts/utils/repro_check.py
```

### 4. Code Packaging Release
Build clean CSV/JSON dataset releases under `data/release/` and calculate SHA256 checksums:
```bash
python3 scripts/utils/release_package.py
```

---

## 📂 Project Structure

```
├── data/
│   ├── raw/         # Raw citation source files (DLR, BLC, ALR)
│   └── release/     # Unified clean datasets (CSV, JSON, SHA256 checksums)
├── scripts/
│   ├── evaluation/  # Baseline evaluation, statistical testing, and simulation scripts
│   ├── fabrication/ # LLM-based precedent fabrication scripts
│   └── utils/       # Release packager and reproducibility checks
├── tests/           # Pytest unit tests for prompts, retrievers, and metrics
├── paper.tex        # Full compilable LaTeX source code of the manuscript
└── requirements.txt # Pinned python package dependencies
```
