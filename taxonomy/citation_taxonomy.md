# Citation Taxonomy — BanLegit-Cite

> **STATUS: FROZEN**
> Frozen after Phase 1 gate (κ ≥ 0.6 in pilot annotation round).
> Any change after freezing requires a joint decision-log entry.

---

## 1. Taxonomy Structure

The dataset contains two super-categories, each divided into five distinct sub-categories.

```
BanLegit-Cite Taxonomy
 ├── Statutory Fabrications
 │    ├── S1: Non-Existent Section
 │    ├── S2: Wrong Act Attribution
 │    ├── S3: Misstated Content
 │    ├── S4: Cross-Jurisdictional Statute Bleed
 │    └── S5: Repealed/Superseded (Labeled & Excluded from v1.0 Evals)
 └── Precedent Fabrications
      ├── P1: Non-Existent Case
      ├── P2: Wrong Citation Locator
      ├── P3: Misattributed Holding
      ├── P4: Wrong Court Level
      └── P5: Cross-Jurisdictional Precedent Bleed
```

---

## 2. Category Definitions & Examples

### A. Statutory-Fabrication Super-Category

#### S1: Non-Existent Section
- **Definition:** The citation references a section number that does not exist at all in the named Act.
- **Bangla Example:** "দণ্ডবিধি ১৮৬০ এর ৫০৯ক ধারা অনুযায়ী..." (Penal Code 1860 does not have a Section 509A—it ends at 511).
- **English Example:** "Under Section 376B of the Penal Code 1860..." (No Section 376B exists).

#### S2: Wrong Act Attribution
- **Definition:** The section number is valid, but it is attributed to the wrong Act.
- **Bangla Example:** "নারী ও শিশু নির্যাতন দমন আইন ২০০০ এর ধারা ৩২৬ অনুযায়ী..." (Section 326 is from the Penal Code, not Nari O Shishu).
- **English Example:** "Pursuant to Section 54 of the Nari O Shishu Nirjatan Daman Ain 2000..." (Section 54 is a famous arrest section in the CrPC, not Nari O Shishu).

#### S3: Misstated Content
- **Definition:** The Act and Section are both real, but the text describes a law/crime that is completely different from what that Section actually says.
- **Bangla Example:** "দণ্ডবিধি ১৮৬০ এর ধারা ৩০২ অনুযায়ী চুরির শাস্তি..." (Section 302 governs murder, not theft).
- **English Example:** "Section 307 of the Penal Code 1860 prescribes punishment for defamation..." (Section 307 is attempt to murder, not defamation).

#### S4: Cross-Jurisdictional Statute Bleed
- **Definition:** Cites statutory sections that exist in Indian or Pakistani penal/procedural codes but are not part of the Bangladeshi statutes (or have different numbering).
- **English Example:** "According to Section 498A of the Penal Code 1860..." (Section 498A regarding husband/relatives cruelty was introduced in India but does not exist in the Bangladesh Penal Code).

#### S5: Repealed/Superseded Citation
- **Definition:** Cites a section that has been repealed or replaced by a newer Act. (Flagged in annotation, but excluded from active baseline testing in v1.0).

---

### B. Precedent-Fabrication Super-Category

#### P1: Non-Existent Case
- **Definition:** The case name or entire citation refers to a fictitious case that was never decided or published.
- **English Example:** *Kalam v. The State, 75 DLR (AD) 405* (No such case exists).

#### P2: Wrong Citation Locator
- **Definition:** The case exists, but the volume, reporter abbreviation, or page number is fabricated or points to a different case.
- **English Example:** Citing *State v. Oli, 73 DLR 12* when *State v. Oli* is actually published at *74 DLR 212*, and page 12 contains a case about land dispute.

#### P3: Misattributed Holding
- **Definition:** The case and locator are real, but the judgment describes a ruling/holding that the court did not make.
- **English Example:** Citing the famous *Blast v. Bangladesh* case on guidelines for arrest as authority for "commercial bank liquidation rules."

#### P4: Wrong Court Level
- **Definition:** Attributes a High Court Division (HCD) decision to the Appellate Division (AD) or vice versa.
- **English Example:** Stating that the Appellate Division decided *X v. Y, 65 DLR 112* when it was actually a High Court Division ruling (meaning it holds persuasive rather than binding authority).

#### P5: Cross-Jurisdictional Precedent Bleed
- **Definition:** Cites Indian Supreme Court (SCC/AIR) or Pakistani Supreme Court (PLD) case law as if it were binding Bangladeshi precedent.
- **English Example:** "As held by the Appellate Division in *Kesavananda Bharati v. State of Kerala, AIR 1973 SC 1461*..." (This is a famous Indian case, not a BD Appellate Division case).

---

## 3. Annotator Decision Tree (Textual)

To evaluate a citation, annotators must follow these steps in order:

```
1. Is it a Statutory or Precedent Citation?
   ├── Statutory:
   │    ├── Check: Does the named Act exist? (If no, S2/S4)
   │    ├── Check: Does the Section exist in the named Act? (If no, S1)
   │    ├── Check: Does the text match the section's legal substance? (If no, S3)
   │    └── Check: Is the section active in BD law? (If no, S4/S5)
   └── Precedent:
        ├── Check: Does the case name exist? (If no, P1)
        ├── Check: Does the volume/page/reporter match the case? (If no, P2)
        ├── Check: Does the court level match the locator? (If no, P4)
        └── Check: Does the cited holding match the judgment's ruling? (If no, P3)
```

---

## 4. Sign-off
- **Owner A (Ema) Signature:** `EMA [2026-07-15]`
- **Status:** Frozen.
