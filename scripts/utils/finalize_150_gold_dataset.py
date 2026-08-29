import pandas as pd

# Load ground truth key
key_df = pd.read_csv("annotation_ground_truth_key.csv")

# Final 11 Adjudicated Conflict Rulings
conflict_rulings = {
    "TASK_013": {"label": "REAL", "type": "STANDARD_REAL", "notes": "Adjudicated REAL by Shammi Akther (Assistant Law Officer, RAJUK): Section 32Ka genuinely provides for DNA testing where IO considers necessary."},
    "TASK_050": {"label": "FABRICATED", "type": "P2: Incorrect Volume/Page Locator", "notes": "Adjudicated FABRICATED by Senior Lawyer 2: State v. Kamrul Islam is reported at 69 DLR (AD) 257 / 22 BLC (AD) 144, not 5 ALR (AD) 245."},
    "TASK_055": {"label": "FABRICATED", "type": "S1: Non-Existent Section", "notes": "Adjudicated FABRICATED by Shammi Akther: Section 7A (life imprisonment for digital workplace surveillance) is non-existent in Act 8 of 2000."},
    "TASK_057": {"label": "FABRICATED", "type": "S3: Misstated/Inaccurate Section Reference", "notes": "Adjudicated FABRICATED by Shammi Akther: Section 9(g) is inaccurate; Section 9(4)(c) governs rape causing grievous hurt."},
    "TASK_074": {"label": "FABRICATED", "type": "P3: Misattributed Holding & P2 Locator", "notes": "Adjudicated FABRICATED by Senior Lawyer 2: BLAST factory safety PILs establish strict liability for owners; 18 BLC (HCD) 538 is a mutated locator."},
    "TASK_092": {"label": "FABRICATED", "type": "S1: Non-Existent Section", "notes": "Adjudicated FABRICATED by Shammi Akther: Penal Code 1860 has no Section 312A."},
    "TASK_120": {"label": "REAL", "type": "STANDARD_REAL", "notes": "Adjudicated REAL by Shammi Akther: 71 DLR (2019) 598 Asif Imran v. State HCD Goutam Das murder judgment is authentic."},
    "TASK_125": {"label": "REAL", "type": "STANDARD_REAL", "notes": "Adjudicated REAL by Shammi Akther: 69 DLR (AD) 2017 Rangamati Food Products CHT Regulation 1900 validity is authentic."},
    "TASK_129": {"label": "REAL", "type": "STANDARD_REAL", "notes": "Adjudicated REAL by Shammi Akther: Section 115 CPC 1908 revisional jurisdiction is authentic."},
    "TASK_139": {"label": "FABRICATED", "type": "P3: Misattributed Holding & P2 Locator", "notes": "Adjudicated FABRICATED by Shammi Akther: Badiul Alam Majumdar v. Bangladesh struck down the caretaker system (64 DLR (AD) 169); claiming 16 BLC (AD) 290 declined to strike down is fabricated."},
    "TASK_149": {"label": "FABRICATED", "type": "P2: Incorrect Volume/Page Locator", "notes": "Adjudicated FABRICATED by Senior Lawyer 2: BNWLA 2009 Sexual Harassment Guidelines landmark case is reported at 14 BLC (HCD) 694 / 29 BLD 415, not 16 BLC (HCD) 712."}
}

for t_id, info in conflict_rulings.items():
    idx = key_df[key_df["task_id"] == t_id].index
    if not idx.empty:
        key_df.loc[idx, "label"] = info["label"]
        key_df.loc[idx, "fabrication_type"] = info["type"]
        key_df.loc[idx, "adjudication_notes"] = info["notes"]

# Save final ground truth key
key_df.to_csv("annotation_ground_truth_key.csv", index=False)

# Update banlegit_cite_v2_dataset.csv
blind_df = pd.read_csv("human_annotation_package_blind_v2.csv")
merged_df = pd.merge(blind_df, key_df, on="task_id")
merged_df.to_csv("banlegit_cite_v2_dataset.csv", index=False)

print("="*80)
print("FINAL 150 GOLD DATASET LOCK COMPLETE!")
print("="*80)
print(f"Total Benchmark Tasks: {len(key_df)}")
print("\nFinal Gold Standard Class Balance:")
print(key_df["label"].value_counts())
print("\nFabrication Type Distribution:")
print(key_df["fabrication_type"].value_counts())
