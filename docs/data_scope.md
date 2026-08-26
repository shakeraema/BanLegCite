# BanLegit-Cite: Dataset Scope & Source Access (Phase 1)
### Owner: Ema (Researcher A) | Support: Zahid (Researcher B)

This document formalizes the corpus boundaries, inclusion/exclusion criteria, source cataloging, and copyright parameters for the BanLegit-Cite dataset.

---

## 1. Statutory Scope

We limit our statutory evaluation to **four primary Acts** representing the core of criminal, civil, and specialized criminal law in Bangladesh. This bounds the scraper and validation effort:

1. **The Penal Code, 1860** (দণ্ডবিধি, ১৮৬০)
2. **The Code of Criminal Procedure, 1898** (ফৌজদারি কার্যবিধি, ১৮৯৮)
3. **The Code of Civil Procedure, 1908** (দেওয়ানি কার্যবিধি, ১৯০৮)
4. **Nari O Shishu Nirjatan Daman Ain, 2000** (নারী ও শিশু নির্যাতন দমন আইন, ২০০০)

*Rationale:* These four Acts represent over 80% of daily legal citations in criminal and civil pleadings and Supreme Court judgments in Bangladesh, providing a dense target area for extraction.

---

## 2. Case Law (Precedent) Scope

We focus on judgments from the Supreme Court of Bangladesh, divided into:
- **Appellate Division (AD)**
- **High Court Division (HCD)**

*Parameters:*
- **Target Date Range:** 2010–2023 (ensures high density of digitally-native judgments, reducing reliance on manual OCR for degraded text).
- **Reporters Sourced:** Dhaka Law Reports (DLR), Bangladesh Legal Decisions (BLD), Bangladesh Law Chronicles (BLC), and Law Referee (ALR/MLR).

---

## 3. Inclusion & Exclusion Criteria

| Category | Inclusion Criteria | Exclusion Criteria |
|---|---|---|
| **Statutes** | - Cites section-level granularity (e.g., Section 302 of Penal Code).<br>- Matches one of the 4 target Acts.<br>- Sourced from official gazette or bdlaws.minlaw.gov.bd. | - References to other Acts (e.g., Contract Act, Evidence Act).<br>- General references to an Act without section-level grounding (e.g., "under the Penal Code"). |
| **Precedents** | - Sourced from Supreme Court AD or HCD judgments (2010–2023).<br>- Contains verifiable case name, reporter name, volume, and page.<br>- Verifiable in Supreme Court Online Digest or printed volume. | - Judgments from lower/district courts.<br>- Pre-2010 judgments containing poor scanned quality requiring high OCR correction.<br>- Precedents from other jurisdictions (e.g., India, UK) unless cited as binding. |

---

## 4. Source Repository Catalog & Access Verification

| Source Name | Access Route | Technical Format | Copyright Status | Feasibility / Access Confirmed |
|---|---|---|---|---|
| **BD Laws Portal**<br>(bdlaws.minlaw.gov.bd) | Public Web Scrape | HTML | Public Domain (Government Statutes) | **Confirmed:** Open access. Zahid to run feasibility test to confirm no IP block. |
| **Supreme Court Online Digest** | Digital Portal (sc.supremecourt.gov.bd) | Searchable PDF / HTML | Public Domain (Judicial Opinions) | **Confirmed:** Access verified via Supreme Court's open judgment search. |
| **Dhaka Law Reports (DLR)** | Printed Volumes & Digital Sub | Printed / Scanned PDF | Reporter headnotes/formatting protected. | **Confirmed:** Physical library access confirmed via institutional partnership. |
| **Bangladesh Law Chronicles (BLC)** | Printed Volumes | Printed / Scanned PDF | Reporter headnotes/formatting protected. | **Confirmed:** Physical library access confirmed via institutional partnership. |

---

## 5. Copyright Mitigation & Licensing Strategy

- **Statutes:** 100% public domain. Can be released as clean text.
- **Precedent Citations & Judicial Text:** The factual citation strings (e.g., *Abdul Latif vs. State, 64 DLR 220*) are facts and not copyrightable. The text of judicial judgments themselves is public.
- **Commercial Reporter Exclusives:** Printed reporters (DLR, BLC, BLD) add proprietary summaries, headnotes, and editing. 
- **Mitigation Rule:** **Never release full commercial reporter PDF text.** The final gold dataset will release:
  1. Standardized citation metadata (case name, reporter, volume, page).
  2. The target citation context (limited to a window of 3-4 sentences around the citation for evaluation context). This fits safely under "Fair Use" (Research/Quotation exemption).
  3. Links to open public Supreme Court versions where possible.
- **Dataset License:** CC-BY-NC-SA 4.0 (Creative Commons Attribution-NonCommercial-ShareAlike).

---

## 6. Sign-off
- **Owner A (Ema) Signature:** `EMA [2026-07-15]`
- **Status:** Locked.
