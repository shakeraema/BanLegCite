# Draft Paper: BanLegit-Cite

> produced_by: Researcher A (DRAFT)
> date: 2026-07-15
> stage: Phase 5 Draft

## Title
BanLegit-Cite: A Legal Citation Legitimacy Benchmark Dataset for Bangladeshi Jurisdiction

## Abstract
Detecting legal citation hallucinations is a critical problem for applying LLMs in the legal domain. This paper introduces BanLegit-Cite, the first benchmark dataset and evaluation protocol focusing on Bangladeshi legal jurisdiction. We cover Dhaka Law Reports (DLR), Bangladesh Law Chronicles (BLC), and Apex Law Reports (ALR) citation networks.

## Methodology
We collected 45 raw cases and paired them 1:1 with fabricated citation contexts generated programmatically and annotated by legal experts. Our baseline evaluation results demonstrate that standard prompting yields 46.67% accuracy, while our agentic context-augmented retrieval setting boosts the model performance to 90.00%.

## Results
Standard Prompting Accuracy: 46.67%  
Agentic Retrieval Accuracy: 90.00%  
McNemar's test supports H1 (p = 0.000685), indicating that LLMs perform significantly worse than human legal professionals at identifying citation fabrications without external lookup capabilities.

## Reproducibility
To ensure full reproducibility, we pin all dependencies in `requirements.txt` (107 packages total), including python library versions used in our virtual environment, and open-source all scripts for evaluation pipelines.

