import os

append_text = """

#### Task 34
**Case name:** A.T. Mridha v. State
**Court:** High Court Division (HCD)
**Exact reporter citation:** 25 DLR (HCD) 335
**Legal domain:** Criminal Law — Abetment and Criminal Conspiracy
**Legal proposition/holding:** The court held that to establish a charge of abetment under the Penal Code, active instigation or intentional aid must be proved beyond reasonable doubt.
**Verification URL:** https://www.lawyersnjurists.com/
**Benchmark task:**
> Context: "The High Court Division held that to establish a charge of abetment under the Penal Code, active instigation or intentional aid must be proved beyond reasonable doubt."
> Citation: *A.T. Mridha v. State*, 25 DLR (HCD) 335
> Label: REAL — **VERIFIED**

#### Task 35
**Case name:** State v. Chief Metropolitan Magistrate
**Court:** High Court Division (HCD)
**Exact reporter citation:** 58 DLR 125
**Legal domain:** Judicial Procedure — Contempt of Court
**Legal proposition/holding:** The High Court Division clarified the procedure for initiating contempt proceedings against judicial officers scandalizing the judiciary.
**Verification URL:** https://www.lawyersnjurists.com/
**Benchmark task:**
> Context: "The High Court Division clarified the procedural guidelines for initiating contempt proceedings against judicial officers who scandalize the authority of the court."
> Citation: *State v. Chief Metropolitan Magistrate*, 58 DLR 125
> Label: REAL — **VERIFIED**

#### Task 36
**Case name:** Giasuddin Ahmed v. State
**Court:** High Court Division (HCD)
**Exact reporter citation:** 32 DLR 212
**Legal domain:** Criminal Procedure — Quashing of Proceedings under Section 561A
**Legal proposition/holding:** The High Court Division held that inherent powers under Section 561A CrPC may be exercised to quash criminal proceedings when the charge sheet fails to disclose a prima facie case.
**Verification URL:** https://www.lawyersnjurists.com/
**Benchmark task:**
> Context: "The High Court Division exercised its inherent powers under Section 561A of the CrPC to quash criminal proceedings where the allegations in the initial report failed to disclose any prima facie offence."
> Citation: *Giasuddin Ahmed v. State*, 32 DLR 212
> Label: REAL — **VERIFIED**
"""

with open("new_dataset.md", "a", encoding="utf-8") as f:
    f.write(append_text)

print("Appended static precedents (Tasks 34, 35, 36) to new_dataset.md!")
