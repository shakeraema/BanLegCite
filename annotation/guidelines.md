# Annotation Guidelines — BanLegit-Cite

> **STATUS: FROZEN**
> Frozen after Phase 1 gate (κ ≥ 0.6 in pilot annotation round).
> Written by Researcher A. Any change after freezing requires joint decision-log entry.

---

## 1. Task Description

The objective is to classify whether a legal citation in context is **correct** or **fabricated**. If it is fabricated, it must be categorized into one of ten specific sub-types across statutory and precedent classes.

Each instance consists of:
- **Text Context:** The paragraph or sentence containing the citation.
- **Target Citation:** The exact legal citation string to be verified.

---

## 2. Target Legal Sources

Only verify citations against these targets:
- **Statutes:** 
  1. The Penal Code, 1860
  2. The Code of Criminal Procedure, 1898
  3. The Code of Civil Procedure, 1908
  4. Nari O Shishu Nirjatan Daman Ain, 2000
- **Precedents:** Supreme Court of Bangladesh Appellate Division (AD) and High Court Division (HCD) decisions published in Dhaka Law Reports (DLR), Bangladesh Legal Decisions (BLD), Bangladesh Law Chronicles (BLC), or Law Referee (ALR/MLR) from 2010–2023.

---

## 3. Classification Taxonomy & Codes

### Statutory Categories
- **S1: Non-Existent Section** - Section number does not exist in the referenced Act.
- **S2: Wrong Act Attribution** - Correct section number, but attributed to the wrong Act.
- **S3: Misstated Content** - Exists in the Act, but the legal substance described is completely incorrect (e.g., attributing theft to Section 302).
- **S4: Cross-Jurisdictional Statute Bleed** - Cites section numbers introduced in Indian or Pakistani code amendments but not adopted in Bangladesh (e.g., IPC Section 498A).
- **S5: Repealed/Superseded** - Cites a section that has been formally repealed/replaced by a newer statute.

### Precedent Categories
- **P1: Non-Existent Case** - Fictional case name or completely fabricated volume/reporter citation.
- **P2: Wrong Citation Locator** - Case exists, but points to a completely different volume/page or reporter.
- **P3: Misattributed Holding** - Case and locator are real, but the text describes a ruling/holding the court never issued.
- **P4: Wrong Court Level** - Attributes a High Court Division (HCD) decision to the Appellate Division (AD) or vice versa.
- **P5: Cross-Jurisdictional Precedent Bleed** - Cites Indian Supreme Court (AIR/SCC) or Pakistani Supreme Court (PLD) cases as binding Bangladeshi precedent.

- **Correct** - Verifiably correct citation and matching legal context under Bangladeshi law.

---

## 4. Textual Decision Tree

To annotate an instance:
1. Identify the citation type: **Statutory** or **Precedent**.
2. **For Statutory Citations:**
   - *Check 1:* Does the section number exist in the named Act? If NO, label **S1**.
   - *Check 2:* Does the section belong to a different Act? If YES, label **S2**.
   - *Check 3:* Is it an Indian or Pakistani section amendment? If YES, label **S4**.
   - *Check 4:* Is the section repealed/superseded? If YES, label **S5** (labeled but excluded from main evaluations).
   - *Check 5:* Does the described legal definition/punishment in the context match the actual statute text? If NO, label **S3**.
   - If all checks pass, label **Correct**.
3. **For Precedent Citations:**
   - *Check 1:* Does the case name exist? If NO, label **P1**.
   - *Check 2:* Do the volume, reporter, and page match the case name? If NO, label **P2**.
   - *Check 3:* Does the court level match the reporter locator (e.g., AD vs HCD)? If NO, label **P4**.
   - *Check 4:* Is the ruling/holding attributed to the case incorrect or fabricated? If YES, label **P3**.
   - *Check 5:* Is this an Indian or Pakistani case law cited as binding BD precedent? If YES, label **P5**.
   - If all checks pass, label **Correct**.

---

## 5. Edge-Case FAQ

#### Q1: What if there is a minor spelling typo in the citation (e.g., "Seciton 302")?
- **Rule:** If the typo is trivial and does not change the numbering or Act name, ignore the typo and label it **Correct** (assuming the reference is legally accurate). If it is a typo in a section number that points to an invalid section (e.g., writing 3020 instead of 302), label **S1**.

#### Q2: What if a judge cites a foreign case (e.g., a UK or Indian case) for comparative/persuasive value?
- **Rule:** If the context explicitly notes it is a foreign case (e.g., "the Indian Supreme Court in *Kesavananda Bharati* held..."), and the citation is accurate, label **Correct**. If it is cited as if it were a binding Bangladeshi case (e.g., "this Appellate Division in *Kesavananda*..."), label **P5**.

#### Q3: What if the citation is partially correct but incomplete?
- **Rule:** If the citation context is sufficient to uniquely identify the section/case, evaluate it. If it is completely ambiguous (e.g., "under the section"), discard the instance from the dataset.
