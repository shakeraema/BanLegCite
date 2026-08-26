import os

# Comprehensive AI Verification & Adjudication Guide for the 11 Conflict Tasks
guide_content = """# Detailed Verification & Adjudication Guide for the 11 Conflict Tasks

This guide provides step-by-step verification instructions for the **11 conflict / edge-case tasks** identified between the human annotators. A senior legal adjudicator (or human auditor) can follow these exact steps to verify each task against Bangladesh primary legal sources.

---

### 1. TASK_013 (Internal ID: `STAT_REAL_37`)
- **Citation:** `Section 32Ka, Nari O Shishu Nirjatan Daman Act, 2000 (As amended 2026)`
- **Context:** "Under the newly added provisions, which section specifically requires mandatory DNA testing (Deoxyribonucleic Acid test) for accused and victims in rape cases?"
- **Ground Truth:** **REAL**
- **Verification Link:** [http://bdlaws.minlaw.gov.bd/act-335.html](http://bdlaws.minlaw.gov.bd/act-335.html)
- **AI Legal Analysis:** REAL. Section 32Ka (*ধারা ৩২ক*) was enacted under the 2026 Statutory Amendments to mandate DNA testing in sexual assault proceedings.
- **Verification Steps for Lawyer:**
  1. Open the [2026 Nari O Shishu Gazette PDF](file:///Users/shakera/Downloads/Study/Researches/ICCIT/BanLegit-Cite/নারী%20ও%20শিশু%20নির্যাতন%20দমন%20(সংশোধন)%20আইন,%20২০২৬.pdf) page 10.
  2. Confirm Section 32Ka (*ডিএনএ পরীক্ষা*) is a newly added section.

---

### 2. TASK_050 (Internal ID: `ALR_FABRICATED_5`)
- **Citation:** `5 ALR (AD) 245` (*State v. Kamrul Islam*)
- **Context:** "In the case of State v. Kamrul Islam, the Appellate Division mitigated the lower court's death sentence to life imprisonment, holding that public lynching cases... do not automatically qualify for fast-track processing..."
- **Ground Truth:** **FABRICATED** (Mutation: `Incorrect Volume/Page`)
- **Verification Link:** [http://www.supremecourt.gov.bd/](http://www.supremecourt.gov.bd/)
- **AI Legal Analysis:** FABRICATED. The volume and page number `5 ALR (AD) 245` is mutated; the case citation is fictionalized.
- **Verification Steps for Lawyer:**
  1. Search the Appellate Division law reports for *State v. Kamrul Islam*.
  2. Confirm that 5 ALR (AD) 245 is not the actual reporter locator for this ruling.

---

### 3. TASK_055 (Internal ID: `FAB_NEW_3`)
- **Citation:** `Section 7A, Nari O Shishu Nirjatan Daman Act, 2000`
- **Context:** "This section criminalizes the unauthorized digital surveillance of women in workplaces, prescribing a punishment of life imprisonment."
- **Ground Truth:** **FABRICATED** (Mutation: `S1: Non-Existent Section`)
- **Verification Link:** [http://bdlaws.minlaw.gov.bd/](http://bdlaws.minlaw.gov.bd/)
- **AI Legal Analysis:** FABRICATED. Section 7A does not exist in the Nari O Shishu Nirjatan Daman Act, 2000. Digital surveillance is governed by the Cyber Security Act 2023.
- **Verification Steps for Lawyer:**
  1. Open `bdlaws.minlaw.gov.bd` for Act No. 8 of 2000.
  2. Verify that there is no Section 7A in the Act.

---

### 4. TASK_057 (Internal ID: `STAT_REAL_29`)
- **Citation:** `Section 9(g), Nari O Shishu Nirjatan Daman Act, 2000 (As amended)`
- **Context:** "Which specific clause under the Act prescribes the punishment for a person who commits rape resulting in grievous hurt?"
- **Ground Truth:** **REAL**
- **Verification Link:** [http://bdlaws.minlaw.gov.bd/act-429.html](http://bdlaws.minlaw.gov.bd/act-429.html)
- **AI Legal Analysis:** REAL. Section 9(g) [Section 9(4)(g) / Section 9(গ)] prescribes death or life imprisonment for rape causing grievous hurt.
- **Verification Steps for Lawyer:**
  1. Open page 3, clause (গ) of the 2026 Gazette PDF.
  2. Confirm the punishment for rape causing grievous hurt (*মারাত্মক জখম*).

---

### 5. TASK_074 (Internal ID: `BLC_FABRICATED_12`)
- **Citation:** `18 BLC (HCD) 538` (*BLAST v. Bangladesh*)
- **Context:** "In the decision reported at 18 BLC (HCD) 538, the High Court Division held that private textile factory owners bear no statutory liability for structural failures..."
- **Ground Truth:** **FABRICATED** (Mutation: `Incorrect Volume/Page` & `P3: Misattributed Holding`)
- **Verification Link:** [http://www.supremecourt.gov.bd/](http://www.supremecourt.gov.bd/)
- **AI Legal Analysis:** FABRICATED. The citation 18 BLC (HCD) 538 is fake, and the context claims factory owners bear no liability, which contradicts established labor safety precedents.
- **Verification Steps for Lawyer:**
  1. Check BLAST factory safety PILs.
  2. Confirm court held owners strictly liable, proving the context is fabricated.

---

### 6. TASK_092 (Internal ID: `FAB_NEW_1`)
- **Citation:** `Section 312A, Penal Code, 1860`
- **Context:** "This section provides punishment for the unauthorized use of a motor vehicle without the owner's consent..."
- **Ground Truth:** **FABRICATED** (Mutation: `S1: Non-Existent Section`)
- **Verification Link:** [http://bdlaws.minlaw.gov.bd/](http://bdlaws.minlaw.gov.bd/)
- **AI Legal Analysis:** FABRICATED. Section 312A does not exist in the Penal Code 1860 (Sections 312-318 deal with miscarriage/abortion). Motor vehicle theft is under Section 379/392 or Road Transport Act.
- **Verification Steps for Lawyer:**
  1. Open Penal Code 1860 on `bdlaws`.
  2. Confirm Section 312A does not exist.

---

### 7. TASK_120 (Internal ID: `PREC_REAL_24`)
- **Citation:** `*Asif Imran and others v. State*, 71 DLR (2019) 598`
- **Context:** "The High Court Division upheld the conviction of five of nine accused in the murder of a journalist who was killed for reporting on corruption in a local road-renovation project..."
- **Ground Truth:** **REAL**
- **Verification Link:** [https://globalfreedomofexpression.columbia.edu/cases/asif-imran-v-state/](https://globalfreedomofexpression.columbia.edu/cases/asif-imran-v-state/)
- **AI Legal Analysis:** REAL. Genuine High Court Division judgment reported in 71 DLR (2019) 598.
- **Verification Steps for Lawyer:**
  1. Click the Columbia Global Freedom of Expression link.
  2. Confirm case facts and 71 DLR 598 reporter citation.

---

### 8. TASK_125 (Internal ID: `PREC_REAL_12`)
- **Citation:** `*Government of Bangladesh v. Rangamati Food Products*, 69 DLR (AD) (2017)`
- **Context:** "The Appellate Division overturned the lower court's characterization of the Chittagong Hill Tracts Regulation, 1900 as a 'dead law'..."
- **Ground Truth:** **REAL**
- **Verification Link:** [https://minorityrights.org/](https://minorityrights.org/)
- **AI Legal Analysis:** REAL. Landmark Appellate Division judgment upholding CHT Regulation 1900.
- **Verification Steps for Lawyer:**
  1. Search 69 DLR (AD) 2017 Rangamati Food Products case.
  2. Confirm AD ruling on validity of CHT Regulation.

---

### 9. TASK_129 (Internal ID: `STAT_REAL_22`)
- **Citation:** `Section 115, Code of Civil Procedure, 1908`
- **Context:** "What section grants revisional jurisdiction to the High Court Division over decisions of subordinate courts where no appeal lies?"
- **Ground Truth:** **REAL**
- **Verification Link:** [https://www.lawyersnjurists.com/article/civil-law/code-of-civil-procedure/revisional-jurisdiction-under-section-115-of-the-code-of-civil-procedure/](https://www.lawyersnjurists.com/article/civil-law/code-of-civil-procedure/revisional-jurisdiction-under-section-115-of-the-code-of-civil-procedure/)
- **AI Legal Analysis:** REAL. Codifies Civil Revision (*রিভিশন*) under Section 115 CPC.
- **Verification Steps for Lawyer:**
  1. Open Section 115 of CPC on `bdlaws`.
  2. Confirm revisional power of High Court Division.

---

### 10. TASK_139 (Internal ID: `BLC_FABRICATED_10`)
- **Citation:** `16 BLC (AD) 290` (*Badiul Alam Majumdar v. Bangladesh*)
- **Context:** "In Badiul Alam Majumdar v. Bangladesh, the Appellate Division declined to strike down the caretaker government system..."
- **Ground Truth:** **FABRICATED** (Mutation: `P3: Misattributed Holding`)
- **Verification Link:** [http://www.supremecourt.gov.bd/](http://www.supremecourt.gov.bd/)
- **AI Legal Analysis:** FABRICATED. The 13th Amendment Caretaker Government decision (*Abdul Mannan Khan v. Bangladesh*, 64 DLR (AD) 169) *struck down* the caretaker system. The context claims it declined to strike it down, making it fabricated.
- **Verification Steps for Lawyer:**
  1. Search Appellate Division 13th Amendment case.
  2. Confirm court declared 13th Amendment unconstitutional.

---

### 11. TASK_149 (Internal ID: `BLC_FABRICATED_3`)
- **Citation:** `16 BLC (HCD) 712` (*BNWLA v. Bangladesh*)
- **Context:** "In the case of BNWLA v. Bangladesh, the High Court Division expanded the scope of labor welfare, establishing that the 2009 sexual harassment guidelines apply retroactively..."
- **Ground Truth:** **FABRICATED** (Mutation: `Incorrect Volume/Page`)
- **Verification Link:** [http://www.supremecourt.gov.bd/](http://www.supremecourt.gov.bd/)
- **AI Legal Analysis:** FABRICATED. The 2009 BNWLA Sexual Harassment Guidelines case is reported at 14 BLC 687 / 29 BLD 415, NOT 16 BLC (HCD) 712.
- **Verification Steps for Lawyer:**
  1. Search 2009 BNWLA judgment.
  2. Confirm volume `16 BLC 712` is a fake citation locator.
"""

with open("gemini_conflict_verification_guide.md", "w", encoding="utf-8") as f:
    f.write(guide_content)

print("Saved gemini_conflict_verification_guide.md successfully!")
