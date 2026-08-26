# BanLegit-Cite: Phase 1 Pilot Annotation Results & IAA
### Owner: Ema (Researcher A)

This report documents the results of the 20-instance pilot annotation round designed to validate the citation taxonomy (v1) and guidelines (v1).

---

## 1. Agreement Metrics

- **Total Instances:** 20
- **Observed Agreement:** 90.00%
- **Cohen's Kappa (κ):** 0.8765
- **Interpretation:** Substantial Agreement (κ ≥ 0.6 threshold met). The taxonomy and guidelines are formally **frozen** for Phase 1.

---

## 2. Disagreement Analysis

Two disagreements occurred during the 20-instance pilot:

1. **Instance 8 (Section 100 of Penal Code regarding search warrant):**
   - **Annotator 1 (Ema):** `S2_wrong_act_attribution`
   - **Annotator 2:** `S1_non_existent_section`
   - **Adjudication:** Section 100 *does* exist in the Penal Code (right of private defence), but its description here refers to a search warrant (which is CrPC Section 100). Therefore, Section 100 exists but is attributed to the wrong Act. Ema's classification `S2` is correct. The guidelines have been updated to clarify that if a section number exists in both Acts but the context refers to the wrong Act, it is `S2`.

2. **Instance 18 (BLAST v. Bangladesh 55 DLR 313 court level):**
   - **Annotator 1 (Ema):** `P4_wrong_court_level`
   - **Annotator 2:** `correct`
   - **Adjudication:** The text states "The Appellate Division in BLAST v. Bangladesh...". However, 55 DLR 313 was decided by the High Court Division. Therefore, it is indeed a wrong court level (`P4`). Annotator 2 missed the reporter court level division. The guidelines have been updated to instruct annotators to always check the reporter division (e.g., AD vs. HCD).

---

## 3. Exit Status
- **κ = 0.8765** (Passed the exit bar of κ ≥ 0.6)
- **Status:** Taxonomy and Guidelines approved.
