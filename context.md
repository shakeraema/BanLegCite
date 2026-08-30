# BanLegit-Cite: Project Context & Research Master Specifications

> **Target Venue:** IEEE International Conference on Computer and Information Technology (ICCIT 2026)  
> **Status:** Submission-Ready (IEEEtran Two-Column Format, $N=150$ Gold Benchmark)  
> **Repository:** [`https://github.com/ZahidHasan7/BanLegit-Cite`](https://github.com/ZahidHasan7/BanLegit-Cite) (Mirror: [`https://github.com/shakeraema/BanLegCite`](https://github.com/shakeraema/BanLegCite))  

---

## 1. Project Overview & Research Objectives

**BanLegit-Cite** is the first benchmark dataset and evaluation protocol for legal citation legitimacy verification and post-generation hallucination auditing in the Bangladeshi jurisdiction.

While Large Language Models (LLMs) and Retrieval-Augmented Generation (RAG) systems have improved legal question answering, post-generation citation auditing remains an open challenge. In low-resource common law jurisdictions like Bangladesh, transitional court naming conventions (e.g., Appellate Division vs. High Court Division splits), dual reporter locators, and statutory amendment cutoffs create lexical inconsistencies that confuse LLMs, causing them to hallucinate fictitious citations or misattribute real holdings.

### Core Research Questions (RQs)
- **RQ1 (Taxonomy & Benchmark Curation):** Can a structured 10-category fabrication taxonomy effectively categorize statutory and precedent citation anomalies in Bangladeshi legal text with high human agreement?
- **RQ2 (Model Compliance Bias & RAG Impact):** How reliably do SOTA language models detect citation fabrications under closed-book standard prompting versus open-book Agentic RAG verification?
- **RQ3 (Sub-Corpus & Category Robustness):** Does citation verification accuracy vary significantly across different case law reporters (DLR, BLC, ALR) and statutory codes?

---

## 2. Authorship, Annotators & Legal Adjudication

### 🎓 Authors & Research Leads
* **Shakera Jannat Ema** — Department of Software Engineering, Shahjalal University of Science and Technology (SUST), Sylhet, Bangladesh (`shakeraema@gmail.com`)
* **M. M. Zahid Hasan** — Department of Software Engineering, Shahjalal University of Science and Technology (SUST), Sylhet, Bangladesh (`zahidhasan7@gmail.com`)

### 🖋️ Double-Blind Human Law Annotators
* **Bushra Hakim ($A_1$)** — Undergraduate Student, Department of Law, Leading University, Sylhet, Bangladesh
* **Haris Rahman Antor ($A_2$)** — Law Graduate, Department of Law, Leading University, Sylhet, Bangladesh

### ⚖️ Senior Legal Adjudicator
* **Shammi Akther** — Assistant Law Officer, Rajdhani Unnayan Kartripakkha (RAJUK), Dhaka, Bangladesh

---

## 3. Gold Benchmark Dataset Specifications ($N=150$)

- **Total Gold Benchmark Tasks ($N$):** 150 Tasks
- **Ground Truth Class Balance:** 74 REAL (Genuine Citations), 76 FABRICATED (Fabricated Citations)
- **Inter-Annotator Agreement (IAA):** Binary Cohen's Kappa $\kappa = 0.9733$ between independent law annotators ($A_1, A_2$).
- **Senior Adjudication Reliability:** 100.00% consensus following adjudication by Assistant Law Officer Shammi Akther.

### Corpus Breakdown
| Corpus Source | Category Type | Sample Size ($N$) | Description |
| :--- | :---: | :---: | :--- |
| **Dhaka Law Reports (DLR)** | Case Reporter | 47 | Primary Appellate Division & High Court Division precedent reporter |
| **Bangladesh Law Chronicles (BLC)** | Case Reporter | 16 | High Court Division commercial & constitutional case reporter |
| **Apex Law Reports (ALR)** | Case Reporter | 15 | Specialized appellate judicial decisions reporter |
| **Statutory Codes** | Statute | 72 | *Penal Code 1860*, *CrPC*, *CPC*, & *Nari O Shishu Nirjatan Daman Amendment Act 2026* |

---

## 4. Citation Fabrication Taxonomy

Our structured taxonomy divides legal citation anomalies into two distinct super-categories:

### A. Statutory Fabrications (S1–S5)
| Code | Category Name | Description | Example (Statute) |
| :---: | :--- | :--- | :--- |
| **S1** | Non-Existent Section | Section number does not exist in named Act | Section 515 of the *Penal Code 1860* |
| **S2** | Wrong Act Attribution | Real section attributed to wrong Act | Attributing Sec. 326 to *Nari O Shishu Ain* |
| **S3** | Misstated Content | Section is real, but legal text is mutated | Claiming Sec. 302 governs theft |
| **S4** | Cross-Jurisdictional Statute Bleed | Foreign statutory section cited as local law | Citing Indian CrPC Sec. 438 in BD court |
| **S5** | Repealed / Superseded Law | Cites repealed law without amendment context | Citing repealed *DSA 2018* for 2026 offense |

### B. Precedent Fabrications (P1–P5)
| Code | Category Name | Description | Example (Reporter) |
| :---: | :--- | :--- | :--- |
| **P1** | Completely Non-Existent Case | Case title and volume locator are fictitious | *Kalam v. The State*, 75 DLR (AD) 405 |
| **P2** | Wrong Citation Locator | Real case, but volume or page number is mutated | *Masdar Hossain* cited as 55 DLR (AD) 99 |
| **P3** | Misattributed Holding | Real citation locator, but holding is fabricated | Claiming *Anwar Hossain* legalized 8th Amend. |
| **P4** | Wrong Court Level / Division | Real case attributed to wrong division/level | Attributing HCD ruling to Appellate Division |
| **P5** | Cross-Jurisdictional Precedent Bleed | Foreign case law cited as binding local precedent | Citing Indian *Kesavananda Bharati* as BD AD case |

---

## 5. Experimental Methodology & Model Suite Architecture

### Strict Generator vs. Verifier Separation
- **Fabrication-Generator Models (Construction Only):** Gemini 3.5 Flash (Phase 1, 45 tasks) & GLM-5.2 (`z-ai/glm-5.2:free`, Phase 2, 31 tasks). To prevent evaluation collusion, these models are strictly barred from acting as verifiers.
- **Primary Verifier Suite ($N=5$):** `google/gemini-2.5-flash-lite`, `openai/gpt-4o-mini`, `deepseek/deepseek-chat`, `meta-llama/llama-3.3-70b-instruct`, `qwen/qwen-2.5-72b-instruct`.
- **Diagnostic Models ($N=2$):** `deepseek-v4-flash` (RAG collapse $85.33\% \rightarrow 56.00\%$, $\chi^2 = 35.56$) & `glm-5.3` (constant FABRICATED prediction prior, $50.67\%$).

### Local Retrieval Indexing (BM25 Parameters)
- **Retriever Package:** `RankBM25` (`BM25Okapi`) over raw indexed Bangladeshi statutes and case reporters.
- **Hyperparameters:** $k_1 = 1.5$, $b = 0.75$, word-level lowercased tokenization, top-$k = 1$ passage chunk retrieved.
- **Retrieval Coverage:** $100.00\%$ (returned correct primary passage for all 150 tasks).

---

## 6. Canonical Empirical Results ($N=150$)

### Primary 5-Verifier Suite Performance (Table II)
| Model Name | Setting | Accuracy | REAL P | REAL R | REAL F1 | FAB P | FAB R | FAB F1 | McNemar $p$-value |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Gemini 2.5 Flash Lite** | Standard | 76.67% | 0.7097 | 0.8919 | 0.7904 | 0.8596 | 0.6447 | 0.7368 | — |
| **Gemini 2.5 Flash Lite** | Agentic RAG | **81.33%** | 0.7614 | 0.9054 | 0.8272 | 0.8871 | 0.7237 | 0.7971 | $p = 0.2109$ |
| **GPT-4o-mini** | Standard | 78.67% | 0.7386 | 0.8784 | 0.8025 | 0.8548 | 0.6974 | 0.7681 | — |
| **GPT-4o-mini** | Agentic RAG | 69.33% | 0.6228 | 0.9595 | 0.7553 | 0.9167 | 0.4342 | 0.5893 | **$p = 0.0140$** |
| **DeepSeek-Chat** | Standard | 76.00% | 0.6863 | 0.9459 | 0.7955 | 0.9167 | 0.5789 | 0.7097 | — |
| **DeepSeek-Chat** | Agentic RAG | **84.00%** | 0.7907 | 0.9189 | 0.8500 | 0.9063 | 0.7632 | 0.8286 | **$p = 0.0139$** |
| **Llama 3.3 70B** | Standard | 76.67% | 0.7010 | 0.9189 | 0.7953 | 0.8868 | 0.6184 | 0.7287 | — |
| **Llama 3.3 70B** | Agentic RAG | 76.00% | 0.6792 | 0.9730 | 0.8000 | 0.9545 | 0.5526 | 0.7000 | $p = 1.0000$ |
| **Qwen 2.5 72B** | Standard | 74.67% | 0.7000 | 0.8514 | 0.7683 | 0.8167 | 0.6447 | 0.7206 | — |
| **Qwen 2.5 72B** | Agentic RAG | 71.33% | 0.6742 | 0.8108 | 0.7362 | 0.7705 | 0.6184 | 0.6861 | $p = 0.2673$ |

### Full 7-Candidate Model Suite Comparison (Table V)
| Model Name | Suite Tier | Standard Acc. | Agentic Acc. | $\Delta$ RAG Impact | McNemar $p$-val |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Gemini 2.5 Flash Lite** | Primary | 76.67% (115/150) | **81.33% (122/150)** | +4.66% | $p = 0.2109$ |
| **GPT-4o-mini** | Primary | 78.67% (118/150) | 69.33% (104/150) | -9.34% | **$p = 0.0140$** |
| **DeepSeek-Chat** | Primary | 76.00% (114/150) | **84.00% (126/150)** | +8.00% | **$p = 0.0139$** |
| **Llama 3.3 70B** | Primary | 76.67% (115/150) | 76.00% (114/150) | -0.67% | $p = 1.0000$ |
| **Qwen 2.5 72B** | Primary | 74.67% (112/150) | 71.33% (107/150) | -3.34% | $p = 0.2673$ |
| **DeepSeek-V4-Flash** | Diagnostic | **85.33% (128/150)** | 56.00% (84/150) | -29.33% | **$p < 0.0001$** |
| **GLM-5.3** | Diagnostic | 50.67% (76/150) | 50.67% (76/150) | 0.00% | $p = 1.0000$ |

### Category-Level Accuracy & Raw Count Breakdown (Table IV)
| Model | DLR ($N=47$) Std / Agt | BLC ($N=16$) Std / Agt | ALR ($N=15$) Std / Agt | Statute ($N=72$) Std / Agt |
| :--- | :---: | :---: | :---: | :---: |
| **Gemini 2.5 Flash Lite** | 76.60% (36/47) / 68.09% (32/47) | 31.25% (5/16) / 81.25% (13/16) | 93.33% (14/15) / 100.00% (15/15) | 83.33% (60/72) / 86.11% (62/72) |
| **GPT-4o-mini** | 78.72% (37/47) / 70.21% (33/47) | 37.50% (6/16) / 18.75% (3/16) | 93.33% (14/15) / 46.67% (7/15) | 84.72% (61/72) / 84.72% (61/72) |
| **DeepSeek-Chat** | 76.60% (36/47) / 76.60% (36/47) | 31.25% (5/16) / 75.00% (12/16) | 66.67% (10/15) / 86.67% (13/15) | 87.50% (63/72) / 90.28% (65/72) |
| **Llama 3.3 70B** | 76.60% (36/47) / 68.09% (32/47) | 37.50% (6/16) / 37.50% (6/16) | 80.00% (12/15) / 80.00% (12/15) | 84.72% (61/72) / 88.89% (64/72) |
| **Qwen 2.5 72B** | 76.60% (36/47) / 65.96% (31/47) | 50.00% (8/16) / 43.75% (7/16) | 66.67% (10/15) / 73.33% (11/15) | 80.56% (58/72) / 80.56% (58/72) |

---

## 7. Pre-Registered Hypotheses Summary

- **H1 (McNemar Test for Standard vs Agentic RAG):** Statistically significant for **`openai/gpt-4o-mini`** ($p = 0.0140$) and **`deepseek/deepseek-chat`** ($p = 0.0139$).
- **H2 (Wilcoxon Confidence Test):** Paired confidence scores (1–5) were not requested during zero-temperature deterministic binary verification prompts; noted explicitly per model as unrated.
- **H3 (Category Contingency Test):** Under Agentic RAG, category-level accuracy variation is not statistically significant for **`DeepSeek-Chat`** ($\chi^2 = 5.0721, p = 0.1666$, Monte Carlo Exact $p = 0.1631$), but remains significant for the other four models, establishing that category consistency is itself model-dependent.

---

## 8. Main File Artifacts in Repository

- `paper.tex`: Compilable IEEEtran LaTeX source code of the manuscript.
- `banlegit_cite_v2_dataset.csv`: Canonical gold benchmark dataset ($N=150$).
- `tasks_150_v2.jsonl`, `tasks_real_75.jsonl`, `tasks_fabricated_75.jsonl`: Full task specifications with extracted URLs.
- `results_summary.json`: Canonical statistical JSON summary diffed against `paper.tex`.
- `RESULTS.md`: Detailed results documentation.
- `README.md`: Public-facing GitHub repository documentation.
- `scripts/evaluation/run_full_raw_verifier_suite.py`: Master benchmark execution script.
- `scripts/utils/audit_paper_citations.py` & `scripts/utils/verify_paper_stats.py`: Automated verification scripts.
- `annotation/`: Double-blind human law annotator reports and senior law officer adjudication records.
