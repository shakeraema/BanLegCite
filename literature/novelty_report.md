# BanLegit-Cite: Novelty Validation Report
### Adversarial Novelty Verification & Gap Statement (Phase 1)

This document contains the adversarial verification of BanLegit-Cite's novelty, positioning it against existing Bangla NLP, South Asian legal NLP, and international legal citation benchmarks.

---

## 1. Stated Research Gap

> **Gap Statement:** While recent work has introduced citation-hallucination benchmarks for U.S. common-law systems (LePhantomCite, LegalCiteBench) and general-domain Bengali hallucination (BenHalluEval), no existing resource evaluates citation fabrication in Bangladeshi legal text, where models must simultaneously verify codified statutory citations and common-law precedent citations across a Bangla/English diglossic environment.

---

## 2. Competitor Comparison Table

Competitor Paper	Year	Task / Focus	Language	Jurisdiction	Dataset Size	Citation Taxonomy	Why it does NOT cover BanLegit-Cite's gap
LePhantomCite :https://arxiv.org/pdf/2606.21155	2026	Citation fabrication detection & agentic verification	English	United States (Common Law)	1,300 brief excerpts (4,499 citation instances)	5 categories (Non-existent, wrong case, wrong opinion, wrong page, wrong quote)	English-only, US common law, lacks statutory-code duality, lacks multilingual/diglossic query evaluation. 
LegalCiteBench:  https://arxiv.org/pdf/2605.10186	2026	Closed-book citation tasks (completion, error detection, matching)	English	United States (Common Law)	~24K instances	N/A (task-based)	English-only, US common law, closed-book focus, no South Asian legal structure.
SG-LegalCite : https://arxiv.org/pdf/2605.21057	2026	Precedent retrieval ranking	English	Singapore (Common Law)	100,890 case-principle pairs	None	Evaluates retrieval ranking, not hallucination or citation fabrication.
LeCNet : https://aclanthology.org/2025.justnlp-main.4/	2024	Citation network link prediction	English	India (Common Law)	N/A (graph)	None	Network/graph link prediction task, not citation fabrication.
BenHalluEval : https://arxiv.org/pdf/2605.31483	2026	General NLP hallucination evaluation	Bangla	General Domain	12,000 candidates	General NLP types	Evaluates general-domain Bengali hallucination, completely lacking legal structure, citation rules, or legal-domain terminology.
MINA (ACL Findings) : https://aclanthology.org/2026.findings-acl.1295.pdf	2026	Bar Council exam assistant (two-stage RAG + citation insertion)	Bangla & English	Bangladesh (Mixed Law)	N/A (applied model)	None	It is a model pipeline/assistant for exam-passing, not an evaluation benchmark. It reports answer accuracy, not citation-level precision/recall/fabrication metrics.
LegalRAG: https://arxiv.org/pdf/2504.16121	2025	Multilingual RAG with relevance checker	Bangla & English	Bangladesh (Mixed Law)	N/A (applied RAG)	None	An applied RAG retrieval system to raise precision, not a benchmark. Lacks citation-level precision/recall metrics or a double-annotated gold set.
JusticeNetBD : 	2025	Women's legal rights RAG assistant	Bangla	Bangladesh (Mixed Law)	N/A (applied RAG)	None	Applied QA assistant, not a benchmark. No evaluation of citation fabrication.
UKIL-DB-EN : https://arxiv.org/html/2410.17210v1	2024	BD legal assistant	English	Bangladesh (Mixed Law)	N/A (applied RAG)	None	First structured BD legal assistant, but lacks citation-level fabrication auditing and Bangla multilingual support.


## 3. Core Research Questions and Hypotheses

### Primary Research Question
*Does the statute-vs-precedent duality of a mixed civil/common-law system (Bangladesh) produce a different citation-fabrication error profile than pure common-law systems (US), and does this transfer to multilingual (Bangla/English) legal queries?*

### Testable Hypotheses
- **H1 (Duality Hypothesis):** LLM citation fabrication detection recall is significantly lower on statutory citations (verifying exact section boundaries across acts) than on precedent citations (verifying case names/reporters).
- **H2 (Diglossia Hypothesis):** LLM detection recall drops significantly when the query and fact context are in Bangla vs. English, for the same underlying legal facts (due to low-resource training representations).
- **H3 (Agentic Hypothesis):** Agentic verification (allowing the model iterative search access to indexed local codes/cases) narrows the statutory-precedent (H1) and script (H2) recall gaps more than it reduces overall error rate.

---

## 4. Adversarial Case (Devil's Advocate Review)

### Objection 1: "This is just LePhantomCite applied to a new country (geographic transfer)."
- **Rebuttal:** U.S. legal citation verification is structurally homogeneous—it relies almost entirely on common-law case precedents (Bluebook format). The Bangladeshi legal system is a mixed system featuring codification (Acts/Sections dating from 1860) alongside common-law Supreme Court precedents (DLR/BLC reporters). Checking statutory section boundaries represents a different cognitive and linguistic task for LLMs than matching case names. Furthermore, our Matched-Pair Cross-Script design explicitly tests diglossia (Bangla/English), introducing a multilingual dimension that does not exist in US-centric benchmarks.

### Objection 2: "MINA (ACL Findings 2026) already inserts citations and uses a two-stage RAG pipeline to prevent statute conflation in Bangladesh."
- **Rebuttal:** MINA is an *agentic system* designed to generate answers. It is evaluated on its overall scores on the Bar Council exam. It is *not* a diagnostic benchmark. BanLegit-Cite is a dedicated evaluation harness that establishes citation-level precision/recall baselines on a double-annotated gold set. We benchmark models specifically on their ability to detect fabrications (which MINA cannot evaluate, since it does not have a dataset of legal fabrications).

---

## 5. PI Sign-off & Freeze
- **Owner A (Ema) Signature:** `EMA [2026-07-15]`
- **Status:** Frozen. (No changes to RQ/H1-H3 without logged entries in `decision_log.md`).
