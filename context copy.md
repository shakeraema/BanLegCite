# Project Context & Rebuild Specification: BanLegit-Cite

This document serves as the comprehensive context guide for any LLM assistant (specifically Claude) assisting with the **BanLegit-Cite** project. It outlines the paper's academic goals, the dataset's target structure, the double-blind annotation protocol, the newly added 2026 statutory amendments, and the chunk-by-chunk rebuild roadmap.

---

## 1. Academic Paper Context & Goals
*   **Target Venue**: 29th International Conference on Computer and Information Technology (ICCIT 2026), IEEE-sponsored.
*   **Core Contribution**: A novel, double-blind expert-annotated legal citation diagnostic benchmark for LLMs under Bangladeshi law (covering both statutes and judicial precedents).
*   **The Research Problem**: LLMs frequently hallucinate legal citations (making up fake volume/reporter numbers or page locators) and suffer from "compliance bias" (agreeing with fabricated citations presented in prompts).
*   **The Evaluation Settings**:
    *   **Standard Setting**: Prompts provide only the context sentence and target citation.
    *   **Agentic (RAG) Setting**: Prompts retrieve reference texts from a local registry index using BM25.

---

## 2. Weaknesses Identified & Being Remediated
Our initial submission suffered from critical validation and design issues that this rebuild is resolving:
1.  **Task Duplication (Independence Violation)**: The initial version had only 15 unique case names triplicated across different contexts to make 90 tasks. This violated the statistical independence assumptions of McNemar's test ($\chi^2$).
2.  **Annotation Leakage / Blinding Failure (Issue 1)**: The original Google Form exposed internal `Org IDs` (provenance markers like `DLR_REAL_1` or `BLC_FAB_2`), allowing the annotators to easily guess the ground truth. We have since run a clean, double-blinded simulation round without Org IDs, showing high agreement (Cohen's Kappa $\kappa_{binary} = 0.9327$, $\kappa_{category} = 0.9351$).
3.  **Retrieval Leakage Shortcut (Issue 2)**: Standard BM25 retrieval achieved 100% verification accuracy because real citations returned search hits while fabricated citations returned a search miss ("No matching verified citation"). The model learned to predict "FABRICATED" simply based on the presence of the search-miss string.
4.  **Baseline Breadth (Issue 4)**: The paper lacked comparison against closed-source frontier baselines (like GPT-class models). We are adding these evaluations.

---

## 3. Rebuilt Dataset Specification (v2.0)
The target specifications for the rebuilt dataset are:
*   **Total Size (N)**: **150 completely unique, non-repeating tasks** (no triplications or verbatim duplicates).
*   **Real : Fabricated Ratio**: **1:1 Balance** (75 Real / 75 Fabricated).
*   **Statute : Precedent Split**: **1:1 Balance** (75 Statutory / 75 Precedent).
*   **Uniqueness Constraint**: Every context-citation pair is completely unique. Real cases can appear under different contexts/rulings but never with identical context strings or locators.

### The 10-Class Taxonomy
Each fabricated instance is classified under one of these ten categories:
*   **S1: Non-Existent Section** — Section number does not exist in the referenced Act.
*   **S2: Wrong Act Attribution** — Valid section number, but belongs to the wrong Act.
*   **S3: Misstated Content** — Section exists, but description of the legal substance is incorrect.
*   **S4: Cross-Jurisdictional Statute Bleed** — Cites statutory sections from foreign codes (India/Pakistan) not adopted in Bangladesh.
*   **S5: Repealed/Superseded** — Cites a section that has been formally repealed or replaced.
*   **P1: Non-Existent Case** — Fictional case name or entire locator.
*   **P2: Wrong Citation Locator** — Case exists, but volume, page, or reporter is wrong.
*   **P3: Misattributed Holding** — Case and locator exist, but the holding described is incorrect.
*   **P4: Wrong Court Level** — Attributes HCD decisions to AD, or vice versa.
*   **P5: Cross-Jurisdictional Precedent Bleed** — Cites foreign cases (AIR/PLD) as binding Bangladeshi precedent.

---

## 4. 2026 Statutory Amendment Context
We are integrating the brand-new **Nari O Shishu Nirjatan Daman (Amendment) Act, 2026** (passed April 10, 2026). This introduces massive novelty, as the amendments are outside LLMs' pre-training cutoffs:
*   **Section 4**: Fines raised (Sec 4(1) up to 20 lakh; 4(2)(ka) to 10 lakh; 4(2)(kha) to 5 lakh; 4(3) to 5 lakh).
*   **Section 9**: Sec 9(1) minimum fine raised to 2 lakh; Sec 9(g) [New] Rape causing grievous hurt is punishable by death or life imprisonment, and minimum fine of 3 lakh.
*   **Section 9A [New]**: Rape under pretext of marriage is punishable by up to 7 years rigorous imprisonment and fine.
*   **Section 11**: Sec 11(kha) [New] Attempt to cause death for dowry is punishable by life or up to 12 years; Sec 11(ga) simple hurt for dowry penalty increased to 2-5 years.
*   **Section 17(3) [New]**: Tribunal can order false complainant to pay compensation to the accused (up to 2 years jail for non-payment).
*   **Section 18(1)**: Investigation period reduced to 30 days (formerly 60 days).
*   **Section 20(3ka) [New]**: Rape trial must be completed within 90 working days from charge framing.

---

## 5. Rebuild execution roadmap (N = 150)
The steps we are following to rebuild the dataset and evaluations are:

1.  **Chunk 1: Full Audit & Triage of the Existing 90 Tasks** *(Completed)*
    *   *Result*: Row-by-row mapping of what is salvageable. Found that only 9 real tasks are directly reusable; the rest must be reconstructed or newly sourced.
2.  **Chunk 2: Target Dataset Structure & Taxonomy Coverage Matrix** *(Completed)*
    *   *Result*: Locked N=150 specifications (75 Real / 75 Fabricated, split 1:1, ~7-8 instances per taxonomy category).
3.  **Chunk 3: Statutory Scope Decision (Which Acts, Which Sections)** *(Next)*
    *   *Goal*: Finalize the specific Acts and section targets (including the 2026 amendments).
4.  **Chunk 4: Precedent Candidate Shortlist Across Legal Domains**
    *   *Goal*: Generate a list of 50-60 candidate cases across distinct domains (constitutional, PIL, NI Act, etc.) to target 38 unique real precedent cases.
5.  **Chunk 5: Source Verification Pass on the Candidate List**
    *   *Goal*: Cross-verify candidates against Supreme Court website, CLCBD, or Lawyers & Jurists.
6.  **Chunk 6: Finalize the Verified Case & Statute Pool**
    *   *Goal*: Lock the 75 final real anchors (37 statutory, 38 precedent).
7.  **Chunk 7 & 8: Construct Real Task Instances**
    *   *Goal*: Write context-citation pairs for the 75 real anchors.
8.  **Chunk 9 & 10: Generate Fabricated Variants (Batch-and-Gate)**
    *   *Goal*: Create the 75 matched fabricated variants using locked category mutation rules.
9.  **Chunk 11: Deduplication, Balance & Structural QA**
    *   *Goal*: Programmatic validation of the final 150-task dataset.
10. **Chunk 12: Blind Annotation Package Preparation**
    *   *Goal*: Create the Google Form / spreadsheet without Org IDs.
11. **Chunk 13 & 14: Double-Blind Human Annotation & IAA Calculation**
    *   *Goal*: Collect annotations from Shakila and Haris and compute final Cohen's Kappa.
12. **Chunk 15: Adjudication Protocol Execution**
    *   *Goal*: Resolve conflicts using primary-source adjudication logs.
13. **Chunk 16 & 17: Gold Dataset Packaging & Paper Synchronization**
    *   *Goal*: Update `paper.tex` with final figures, tables, and statistics.
