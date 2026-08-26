# BanLegit-Cite: Dataset Specification (Chunk 2)

This document locks the target structure, category coverage, and design rules for the rebuilt **BanLegit-Cite v2.0** dataset.

---

## 1. Core Design Parameters

To resolve the statistical independence flaws and scale limitations of version 1.0, the rebuilt dataset is locked to the following specification:

| Parameter | Specification | Rationale |
| :--- | :--- | :--- |
| **Total Size (N)** | **150 unique tasks** | Avoids the "15 cases in 45 contexts" triplication, ensuring all statistical testing inputs are independent. |
| **Real : Fabricated Ratio** | **1:1 Balance** (75 Real / 75 Fabricated) | Standard binary classification baseline. Prevents majority-class guessing bias. |
| **Statute : Precedent Split** | **1:1 Balance** (75 Statutory / 75 Precedent) | Ensures equal representation of codified law and judicial precedents. |
| **Uniqueness Constraint** | **Strictly No Verbatim Repeats** | Every context-citation pair is unique. Real cases can appear under multiple *different* contexts/rulings but never with duplicate text or identical citations. |

---

## 2. Statistical Split (N = 150)

Because there are **10 taxonomy categories** (5 Statutory, 5 Precedent), the total size (N = 150) results in the following category splits:

### A. Real Tasks (75 Tasks)
*   **Statutory Real**: 37 tasks (Genuinely correct sections and descriptions from the Penal Code, CrPC, CPC, and Nari O Shishu Nirjatan Daman Act).
*   **Precedent Real**: 38 tasks (Genuinely correct court names, locators, and holdings from verified Appellate Division and High Court Division rulings).

### B. Fabricated Tasks (75 Tasks)
The fabricated tasks are distributed as evenly as possible across the 10 taxonomy categories (approx. **7 to 8 instances per category**):
*   **Statutory Fabrications (S1–S5)**: 37 tasks (~7 per category)
*   **Precedent Fabrications (P1–P5)**: 38 tasks (~8 per category)

---

## 3. Taxonomy Definitions & Targets

### Statutory Fabrications (37 Tasks Total)
*   **S1: Non-Existent Section** (~7 tasks): Citations referencing section numbers that do not exist in the Act (e.g., Section 600 of the Penal Code).
*   **S2: Wrong Act Attribution** (~7 tasks): Valid section numbers attributed to the wrong Act.
*   **S3: Misstated Content** (~7 tasks): Section exists, but the legal substance described is completely incorrect.
*   **S4: Cross-Jurisdictional Statute Bleed** (~8 tasks): Citations to Indian/Pakistani-only section amendments (e.g., IPC Section 498A) never adopted in Bangladesh.
*   **S5: Repealed/Superseded** (~8 tasks): Citations to sections that have been repealed or replaced by newer amendments.

### Precedent Fabrications (38 Tasks Total)
*   **P1: Non-Existent Case** (~7 tasks): Completely fictional case names or reporter volumes.
*   **P2: Wrong Citation Locator** (~8 tasks): Case exists, but volume, page, or reporter is wrong.
*   **P3: Misattributed Holding** (~8 tasks): Real case and locator, but the described holding was never issued by the court.
*   **P4: Wrong Court Level** (~7 tasks): Attributes an HCD decision to the AD or vice versa.
*   **P5: Cross-Jurisdictional Precedent Bleed** (~8 tasks): Cites foreign case law (AIR/PLD) as binding Bangladeshi precedent.
