# RESULTS.md — BanLegit-Cite Final Canonical Benchmark Results

> **Status:** Canonical Gold Benchmark Evaluation Results ($N=150$)  
> **Last Synchronized:** 2026-08-30 01:08:00  
> **Paper Source:** `paper.tex` (IEEEtran Conference Standard)  

---

## 📊 Summary of Final Gold Benchmark ($N=150$)

- **Total Gold Tasks ($N$):** 150 (74 Real, 76 Fabricated)
- **Inter-Annotator Agreement (IAA):** Cohen's Kappa $\kappa = 0.9733$ (double-blind legal graduate annotators $A_1, A_2$)
- **Senior Legal Adjudication:** 100.00% consensus following adjudication by Assistant Law Officer Shammi Akther

---

## 1. Primary 5-Verifier Model Suite Results

| Model Name | Setting | Accuracy | REAL P | REAL R | REAL F1 | FAB P | FAB R | FAB F1 | McNemar $\chi^2$ | $p$-value |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Gemini 2.5 Flash Lite** | Standard | 0.7667 | 0.7097 | 0.8919 | 0.7904 | 0.8596 | 0.6447 | 0.7368 | — | — |
| **Gemini 2.5 Flash Lite** | Agentic RAG | **0.8133** | 0.7614 | 0.9054 | 0.8272 | 0.8871 | 0.7237 | 0.7971 | 1.5652 | 0.2109 |
| **GPT-4o-mini** | Standard | 0.7867 | 0.7386 | 0.8784 | 0.8025 | 0.8548 | 0.6974 | 0.7681 | — | — |
| **GPT-4o-mini** | Agentic RAG | 0.6933 | 0.6228 | 0.9595 | 0.7553 | 0.9167 | 0.4342 | 0.5893 | 6.0357 | **0.0140** |
| **DeepSeek-Chat** | Standard | 0.7600 | 0.6863 | 0.9459 | 0.7955 | 0.9167 | 0.5789 | 0.7097 | — | — |
| **DeepSeek-Chat** | Agentic RAG | **0.8400** | 0.7907 | 0.9189 | 0.8500 | 0.9063 | 0.7632 | 0.8286 | 6.0500 | **0.0139** |
| **Llama 3.3 70B** | Standard | 0.7667 | 0.7010 | 0.9189 | 0.7953 | 0.8868 | 0.6184 | 0.7287 | — | — |
| **Llama 3.3 70B** | Agentic RAG | 0.7600 | 0.6792 | 0.9730 | 0.8000 | 0.9545 | 0.5526 | 0.7000 | 0.0000 | 1.0000 |
| **Qwen 2.5 72B** | Standard | 0.7467 | 0.7000 | 0.8514 | 0.7683 | 0.8167 | 0.6447 | 0.7206 | — | — |
| **Qwen 2.5 72B** | Agentic RAG | 0.7133 | 0.6742 | 0.8108 | 0.7362 | 0.7705 | 0.6184 | 0.6861 | 1.2308 | 0.2673 |

---

## 2. Category-Level Accuracy Breakdown (Table IV)

| Model Name | DLR ($N=47$) (Std / Agt) | BLC ($N=16$) (Std / Agt) | ALR ($N=15$) (Std / Agt) | Statute ($N=72$) (Std / Agt) |
| :--- | :---: | :---: | :---: | :---: |
| **Gemini 2.5 Flash Lite** | 76.60% / 68.09% | 31.25% / 81.25% | 93.33% / 100.00% | 83.33% / 86.11% |
| **GPT-4o-mini** | 78.72% / 70.21% | 37.50% / 18.75% | 93.33% / 46.67% | 84.72% / 84.72% |
| **DeepSeek-Chat** | 76.60% / 76.60% | 31.25% / 75.00% | 66.67% / 86.67% | 87.50% / 90.28% |
| **Llama 3.3 70B** | 76.60% / 68.09% | 37.50% / 37.50% | 80.00% / 80.00% | 84.72% / 88.89% |
| **Qwen 2.5 72B** | 76.60% / 65.96% | 50.00% / 43.75% | 66.67% / 73.33% | 80.56% / 80.56% |

---

## 3. Diagnostic Models Analysis (Section VI-D)

| Diagnostic Model | Standard Acc. | Agentic Acc. | Diagnostic Failure Mode Observed |
| :--- | :---: | :---: | :--- |
| **DeepSeek-V4-Flash** | 85.33% | 56.00% | Severe RAG context sensitivity ($\chi^2 = 35.56, p < 0.0001$) |
| **GLM-5.3** | 50.67% | 50.67% | Degenerate constant FABRICATED prediction prior ($\chi^2 = 0.0, p = 1.0$) |

---

## 4. Pre-Registered Statistical Hypotheses Summary

- **H1 (McNemar Test for Standard vs Agentic RAG):** Statistically significant for **`openai/gpt-4o-mini`** ($p = 0.0140$) and **`deepseek/deepseek-chat`** ($p = 0.0139$).
- **H2 (Wilcoxon Confidence Test):** Paired confidence scores (1-5) were not requested or logged during zero-temperature deterministic binary predictions; noted explicitly per model.
- **H3 (Chi-Squared Category Contingency Test):** Evaluates variation across DLR, BLC, ALR, and Statute categories. Demonstrates that **`deepseek/deepseek-chat`** achieves robust category generalization in Agentic RAG ($\chi^2 = 5.0721, p = 0.1666$).
