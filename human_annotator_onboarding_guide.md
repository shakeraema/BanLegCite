# Legal Annotator Onboarding & Review Instructions

Welcome to the **BanLegit-Cite** legal research project! 

Your contribution as a qualified law graduate is essential to establishing high-precision ground truth for legal citation verification under Bangladeshi law. Your expert role will be formally credited and acknowledged in the published research paper.

---

## 🎯 Overview of Your Role

You are acting as an **Expert Legal Auditor**. 

Our research team has generated candidate verification records for Bangladeshi legal citations (covering both Acts of Parliament and Supreme Court precedents). 

Your job is to **review each draft verification record**, check it against authoritative legal sources, and confirm whether the draft evaluation is **CORRECT** or needs **CORRECTION**.

---

## 📋 What Each Task Contains

For every item, you will be given:
1. **Legal Context**: A sentence describing a legal provision or case holding.
2. **Target Citation**: The exact legal citation string being audited (e.g., *41 DLR (AD) 165* or *Section 302 of the Penal Code, 1860*).
3. **Draft Status**: The proposed classification (**Legitimate/Correct** vs. **Fabricated**).
4. **Draft Category**: The proposed error category (if fabricated).
5. **Draft Reasoning & Notes**: The preliminary explanation of the legal check.

---

## 🔍 How to Perform Your Review (Step-by-Step)

For each entry, follow these 5 simple steps:

### Step 1: Read the Context & Citation
Read the context statement and note the target citation, reporter, and court division.

### Step 2: Cross-Check Against Legal Sources
Verify the citation using your legal knowledge and reputable Bangladeshi legal databases, including:
* **Dhaka Law Reports (DLR)**, **Bangladesh Legal Decisions (BLD)**, **Bangladesh Law Chronicles (BLC)**
* **Chancery Law Chronicles** ([clcbd.org](https://www.clcbd.org))
* **The Lawyers & Jurists Case Index** ([lawyersnjurists.com](https://www.lawyersnjurists.com))
* **Supreme Court of Bangladesh Search Register** ([supremecourt.gov.bd](http://www.supremecourt.gov.bd))
* **BD Laws Portal** ([bdlaws.minlaw.gov.bd](http://bdlaws.minlaw.gov.bd))

### Step 3: Audit the Verification Status
* Is the citation **Legitimate (Correct)**? (Does the case/section exist with the exact volume, page, court, and holding described?)
* Is the citation **Fabricated**? (Does it contain an incorrect page, wrong reporter, fictional section, or wrong holding?)

### Step 4: Audit the Fabrication Category (If Fabricated)
If the entry is fabricated, check if the assigned category code matches the cheat-sheet below.

### Step 5: Record Your Verdict
In the response sheet, record:
* **Do you Agree with the draft verdict?** (`Agree` / `Disagree`)
* **Your Final Verdict**: (`Legitimate` or `Fabricated`)
* **Your Confidence Level**: (`High`, `Medium`, or `Low`)
* **Your Auditor Notes**: A brief 1-2 sentence note explaining your decision (e.g., *"Confirmed page 165 in 41 DLR (AD)"* or *"Page number is actually 44, not 196; category P2 is correct"*).

---

## 📚 Simple Guide to Fabrication Categories

If a citation is **Fabricated**, classify the error using these standard codes:

### 🏛️ Statutory Fabrications (Acts & Laws)
* **S1: Non-Existent Section** — The section number does not exist in the Act (e.g., *Section 600 of the Penal Code*).
* **S2: Wrong Act Attribution** — The section number exists, but is assigned to the wrong Act.
* **S3: Misstated Content** — The section exists, but the legal description is completely wrong.
* **S4: Foreign Statute Bleed** — Cites a section from Indian or Pakistani legal amendments not adopted in Bangladesh (e.g., *IPC Section 498A*).
* **S5: Repealed Section** — Cites a section that has been repealed or superseded.

### ⚖️ Precedent Fabrications (Case Law)
* **P1: Non-Existent Case** — Fictional case name or completely made-up reporter volume.
* **P2: Wrong Citation Locator** — Real case name, but the volume, page number, or reporter is wrong.
* **P3: Misattributed Holding** — Real case and citation locator, but the court never issued the holding described.
* **P4: Wrong Court Level** — Attributes a High Court Division (HCD) ruling to the Appellate Division (AD), or vice versa.
* **P5: Foreign Case Bleed** — Cites Indian (AIR/SCC) or Pakistani (PLD) case law as binding Bangladeshi precedent.

---

## 💡 Important Rules for Annotators

1. **Be Objective**: Base every decision on verifiable legal sources.
2. **Focus on Detail**: Small details matter (e.g., checking whether a ruling was from the High Court Division vs. Appellate Division, or checking exact page numbers).
3. **Flag Ambiguities**: If a historical volume has conflicting page references across secondary sources, select `Medium` confidence and note the ambiguity.
4. **Independent Judgment**: Trust your legal research. If you spot an error in the draft reasoning, mark `Disagree` and write the correct details.

Thank you for your rigorous work in advancing legal NLP research in Bangladesh!
