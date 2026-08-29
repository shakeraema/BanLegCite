# BanLegit-Cite: A Legal Citation Legitimacy Benchmark Dataset for the Bangladeshi Jurisdiction

Official open-source repository for **BanLegit-Cite**, an academic legal NLP benchmark dataset and post-generation hallucination auditing framework for the Bangladeshi legal jurisdiction.

[![LaTeX Paper](https://img.shields.to/badge/Paper-IEEEtran%20LaTeX-blue.svg)](paper.tex)
[![Dataset](https://img.shields.to/badge/Dataset-N%3D150%20Gold%20Tasks-green.svg)](banlegit_cite_v2_dataset.csv)
[![License](https://img.shields.to/badge/License-MIT-yellow.svg)](LICENSE)

---

## 👥 Authors & Collaborators

### 🎓 Authors & Research Leads
* **Shakera Jannat Ema** — Department of Software Engineering, Shahjalal University of Science and Technology (SUST), Sylhet, Bangladesh (`shakeraema@gmail.com`)
* **M. M. Zahid Hasan** — Department of Software Engineering, Shahjalal University of Science and Technology (SUST), Sylhet, Bangladesh (`zahidhasan7@gmail.com`)

### 🖋️ Double-Blind Human Law Annotators
* **Bushra Hakim** — Undergraduate Student, Department of Law, Leading University, Sylhet, Bangladesh
* **Haris Rahman Antor** — Law Graduate, Department of Law, Leading University, Sylhet, Bangladesh

### ⚖️ Senior Legal Adjudicator
* **Shammi Akther** — Assistant Law Officer, Rajdhani Unnayan Kartripakkha (RAJUK), Dhaka, Bangladesh

---

## 📖 Executive Summary & Overview

Large Language Models (LLMs) applied in the legal domain frequently hallucinate statutory sections and judicial precedents with high linguistic fluency. In low-resource common law jurisdictions like Bangladesh, post-generation citation auditing is hampered by transitional court naming variations (e.g., Appellate Division vs. High Court Division splits), dual reporter locators, and unindexed physical volume archives.

**BanLegit-Cite** introduces the first gold-standard benchmark ($N=150$ tasks: 74 genuine, 76 fabricated) and evaluation protocol specifically designed to audit legal citation legitimacy in Bangladesh.

### 📐 Double-Blind Annotation Reliability
- **Inter-Annotator Agreement (IAA):** Binary Cohen's Kappa $\kappa = 0.9733$ between independent law graduate annotators ($A_1, A_2$).
- **Senior Legal Adjudication:** 100.00% consensus following adjudication by Assistant Law Officer Shammi Akther.

---

## 🏷️ Citation Fabrication Taxonomy

Our structured taxonomy categorizes legal citation anomalies into two distinct super-categories:

### 1. Statutory Fabrications (S1–S5)
| Code | Category Name | Description | Example (Statute) |
| :---: | :--- | :--- | :--- |
| **S1** | Non-Existent Section | Section number does not exist in named Act | Section 515, *Penal Code 1860* |
| **S2** | Wrong Act Attribution | Real section attributed to wrong Act | Attributing Sec. 326 to *Nari O Shishu Ain* |
| **S3** | Misstated Statutory Content | Section is real, but legal text is mutated | Claiming Sec. 302 governs theft |
| **S4** | Cross-Jurisdictional Statute Bleed | Foreign statutory section cited as local law | Citing Indian CrPC Sec. 438 in BD court |
| **S5** | Repealed / Superseded Law | Cites repealed law without amendment context | Citing repealed *DSA 2018* for 2026 offense |

### 2. Precedent Fabrications (P1–P5)
| Code | Category Name | Description | Example (Reporter) |
| :---: | :--- | :--- | :--- |
| **P1** | Completely Non-Existent Case | Case title and volume locator are fictitious | *Rahman v. State*, 99 DLR (AD) 888 |
| **P2** | Wrong Citation Locator | Real case, but volume or page number is mutated | *Masdar Hossain* cited as 55 DLR (AD) 99 |
| **P3** | Misattributed Holding | Real citation locator, but holding is fabricated | Claiming *Anwar Hossain* legalized 8th Amend. |
| **P4** | Wrong Court Level / Division | Real case attributed to wrong division/level | Attributing HCD ruling to Appellate Division |
| **P5** | Cross-Jurisdictional Precedent Bleed | Foreign case law cited as binding local precedent | Citing Indian *Kesavananda Bharati* as BD AD case |

---

## 📊 Empirical Verification Results

Evaluations across our primary 5-verifier suite ($N=150$ gold tasks) demonstrate that standard closed-book prompting suffers from compliance bias, while open-book retrieval verification produces model-dependent effects:

### Primary Verifier Suite ($N=150$)
| Model Name | Verification Setting | Accuracy | REAL Precision | REAL Recall | REAL F1 | FAB Precision | FAB Recall | FAB F1 | McNemar $p$-value |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Google Gemini 2.5 Flash Lite** | Standard | 76.67% | 0.7097 | 0.8919 | 0.7904 | 0.8596 | 0.6447 | 0.7368 | — |
| **Google Gemini 2.5 Flash Lite** | Agentic RAG | **81.33%** | 0.7614 | 0.9054 | 0.8272 | 0.8871 | 0.7237 | 0.7971 | $p = 0.2109$ |
| **OpenAI GPT-4o-mini** | Standard | 78.67% | 0.7386 | 0.8784 | 0.8025 | 0.8548 | 0.6974 | 0.7681 | — |
| **OpenAI GPT-4o-mini** | Agentic RAG | 69.33% | 0.6228 | 0.9595 | 0.7553 | 0.9167 | 0.4342 | 0.5893 | **$p = 0.0140$** |
| **DeepSeek-Chat** | Standard | 76.00% | 0.6863 | 0.9459 | 0.7955 | 0.9167 | 0.5789 | 0.7097 | — |
| **DeepSeek-Chat** | Agentic RAG | **84.00%** | 0.7907 | 0.9189 | 0.8500 | 0.9063 | 0.7632 | 0.8286 | **$p = 0.0139$** |
| **Llama 3.3 70B** | Standard | 76.67% | 0.7010 | 0.9189 | 0.7953 | 0.8868 | 0.6184 | 0.7287 | — |
| **Llama 3.3 70B** | Agentic RAG | 76.00% | 0.6792 | 0.9730 | 0.8000 | 0.9545 | 0.5526 | 0.7000 | $p = 1.0000$ |
| **Qwen 2.5 72B** | Standard | 74.67% | 0.7000 | 0.8514 | 0.7683 | 0.8167 | 0.6447 | 0.7206 | — |
| **Qwen 2.5 72B** | Agentic RAG | 71.33% | 0.6742 | 0.8108 | 0.7362 | 0.7705 | 0.6184 | 0.6861 | $p = 0.2673$ |

### Category-Level Accuracy Breakdown
| Model | DLR ($N=47$) Std / Agt | BLC ($N=16$) Std / Agt | ALR ($N=15$) Std / Agt | Statute ($N=72$) Std / Agt |
| :--- | :---: | :---: | :---: | :---: |
| **Gemini 2.5 Flash Lite** | 76.60% / 68.09% | 31.25% / 81.25% | 93.33% / 100.00% | 83.33% / 86.11% |
| **GPT-4o-mini** | 78.72% / 70.21% | 37.50% / 18.75% | 93.33% / 46.67% | 84.72% / 84.72% |
| **DeepSeek-Chat** | 76.60% / 76.60% | 31.25% / 75.00% | 66.67% / 86.67% | 87.50% / 90.28% |
| **Llama 3.3 70B** | 76.60% / 68.09% | 37.50% / 37.50% | 80.00% / 80.00% | 84.72% / 88.89% |
| **Qwen 2.5 72B** | 76.60% / 65.96% | 50.00% / 43.75% | 66.67% / 73.33% | 80.56% / 80.56% |

---

## 🛠️ Quickstart & Reproduction Guide

### 1. Prerequisites
- **Python**: CPython `3.10` or higher
- **OpenRouter API Key**: Set `OPENROUTER_API_KEY` in environment

### 2. Environment Setup
```bash
# Clone repository
git clone https://github.com/ZahidHasan7/BanLegit-Cite.git
cd BanLegit-Cite

# Install dependencies
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Run Benchmark Verification Suite
```bash
# Execute master 5-verifier benchmark across all N=150 tasks
OPENROUTER_API_KEY="your_api_key_here" python scripts/evaluation/run_full_raw_verifier_suite.py
```

### 4. Run Paper Consistency Audits
```bash
# Verify 100% citation matching and paper-codebase consistency
python scripts/utils/audit_paper_citations.py
python scripts/utils/verify_paper_stats.py
```

---

## 📂 Repository Structure

```
├── banlegit_cite_v2_dataset.csv  # Canonical Gold Benchmark Dataset (N=150)
├── tasks_150_v2.jsonl            # Full JSONL Task Specifications with Extracted URLs
├── tasks_real_75.jsonl           # Verified Real Citations Sub-dataset (N=74)
├── tasks_fabricated_75.jsonl     # Verified Fabricated Citations Sub-dataset (N=76)
├── paper.tex                     # Compilable IEEEtran LaTeX Source Code of the Paper
├── results_summary.json          # Synchronized Statistical Results & Metrics JSON
├── annotation/                   # Raw Annotator Reports & Adjudication Registers
│   ├── senior_lawyer_adjudication_report.md
│   ├── bushra_annotaion_report.md
│   └── haris_annotation_report.md
├── scripts/
│   ├── evaluation/               # Master Benchmark Execution Scripts
│   └── utils/                    # Paper Citation Audit & Consistency Verification Scripts
├── experiments/results/          # Raw Per-Item Itemized Model Prediction JSON Logs
└── requirements.txt              # Pinned Dependencies
```

---

## 📜 Citation

If you use BanLegit-Cite in your research, please cite our IEEEtran paper:

```bibtex
@inproceedings{ema2026banlegitcite,
  title={BanLegit-Cite: A Legal Citation Legitimacy Benchmark Dataset for the Bangladeshi Jurisdiction},
  author={Ema, Shakera Jannat and Hasan, M. M. Zahid},
  booktitle={Proceedings of the International Conference on Computer and Information Technology (ICCIT)},
  year={2026}
}
```
