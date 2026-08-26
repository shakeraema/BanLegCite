# BanLegit-Cite: Annotator Training Guide & Self-Test Module
### Owner: Ema (Researcher A)

Welcome to the BanLegit-Cite annotation team! This guide will train you on using the Label Studio interface, applying our 10-category citation taxonomy, and completing your self-test certification.

---

## 1. Using the Label Studio Interface

1. **Accessing the Portal:** Open the URL provided by the team (e.g., `http://[IP-Address]:8080`) and log in with your assigned credentials.
2. **Reviewing Tasks:** You will see a list of tasks. Each task contains:
   - **Text Context:** The paragraph or sentence extracted from a brief or judgment.
   - **Target Citation:** The specific citation string highlighted in blue/bold that you must verify.
3. **Labeling Panels:**
   - **Binary Status:** Select whether the target citation is `Correct` or `Fabricated`.
   - **Fabrication Category:** If fabricated, select exactly one sub-type (S1-S5 for Statutes, P1-P5 for Precedents).
   - **Confidence Level:** Move the slider to rate your confidence (`Low`, `Medium`, `High`).
   - **Reviewer Notes:** Add a brief sentence explaining your decision (especially for fabrications, e.g., "Penal Code Sec 512 does not exist, code ends at 511").
4. **Submission:** Click the **Submit** button to save your annotation and load the next instance.

---

## 2. Taxonomy Reference Cheat Sheet

Refer to this quick-table during annotation:

| Category Code | Meaning | Key Question to Ask Yourself |
|---|---|---|
| **S1** | Non-Existent Section | Does this section number exist in the named Act? |
| **S2** | Wrong Act Attribution | Does this section number belong to a *different* Act instead? |
| **S3** | Misstated Content | Are the Act and Section real, but the context describes completely wrong crimes/punishments? |
| **S4** | Cross-Jurisdictional Statute Bleed | Is this an Indian or Pakistani section amendment not active in Bangladesh? |
| **P1** | Non-Existent Case | Is this case name or citation volume/reporter completely fictional? |
| **P2** | Wrong Citation Locator | Does this case exist, but at a different volume/reporter/page? |
| **P3** | Misattributed Holding | Did this case rule on a completely different subject than stated? |
| **P4** | Wrong Court Level | Did the High Court decide this instead of the Appellate Division (or vice versa)? |
| **P5** | Cross-Jurisdictional Precedent Bleed | Is this a foreign case cited as if it were a binding Bangladeshi case? |

---

## 3. Onboarding Self-Test & Review

To certify for the full dataset, you must complete the 20-instance **Self-Test Project** in Label Studio and achieve a score of **≥ 80% (16/20 correct classifications)** compared to Ema's gold standard.

Study these pilot examples to understand the decision boundaries:

### Example 1: Section 100 of Penal Code vs Section 100 of CrPC
- **Context:** "A search warrant was issued under Section 100 of the Penal Code 1860 to find the missing child."
- **Gold Label:** `S2_wrong_act_attribution`
- **Explanation:** Search warrants are issued under **Section 100 of the Code of Criminal Procedure 1898 (CrPC)**. While Section 100 *does* exist in the Penal Code 1860, it defines the right of private defence of the body. Since the section number exists in both but the text attributes search warrant powers to the Penal Code, it is a wrong Act attribution (`S2`).

### Example 2: BLAST v. Bangladesh Court Levels
- **Context:** "The Appellate Division in BLAST v. Bangladesh, 55 DLR 313 held that Section 54 of CrPC requires guidelines."
- **Gold Label:** `P4_wrong_court_level`
- **Explanation:** The landmark judgment *BLAST v. Bangladesh* published at *55 DLR 313* was decided by the **High Court Division (HCD)**. The Appellate Division later heard the appeal (published in *DLR (AD)*). Citing the *55 DLR 313* version as an Appellate Division decision is a court level mismatch (`P4`).

### Example 3: Section 498A Penal Code
- **Context:** "The charge sheet was submitted under Section 498A of the Penal Code 1860 regarding husband's cruelty."
- **Gold Label:** `S4_cross_jurisdictional_bleed`
- **Explanation:** Section 498A of the Penal Code is an extremely famous provision in India regarding dowry and husband cruelty. However, the Bangladesh Penal Code has *never* been amended to include Section 498A (cruelty cases in BD are prosecuted under the Nari O Shishu Nirjatan Daman Ain). This is a cross-jurisdictional statutory bleed (`S4`).

### Example 4: Citing Indian Landmark Precedents
- **Context:** "The Appellate Division in Kesavananda Bharati v. State of Kerala, AIR 1973 SC 1461 laid down the basic structure doctrine."
- **Gold Label:** `P5_cross_jurisdictional_precedent_bleed`
- **Explanation:** *Kesavananda Bharati* is the foundational basic structure case of the **Supreme Court of India**. Citing it as a decision of the "Appellate Division" (implying the Appellate Division of Bangladesh) is a cross-jurisdictional precedent bleed (`P5`).
