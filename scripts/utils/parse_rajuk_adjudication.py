import pandas as pd

# Load ground truth key
key_df = pd.read_csv("annotation_ground_truth_key.csv")

# Adjudicated tasks provided by RAJUK Law Officer
rajuk_verdicts = {
    "TASK_013": {"verdict": "REAL", "notes": "Section 32Ka provides for DNA testing where IO considers necessary. Citation is genuine."},
    "TASK_055": {"verdict": "FABRICATED", "notes": "Section 7A life imprisonment for workplace digital surveillance is non-existent/mutated."},
    "TASK_057": {"verdict": "FABRICATED", "notes": "Section 9(g) is inaccurate. Section 9(4)(c) prescribes rape with grievous hurt. Inaccurate section reference makes it fabricated."},
    "TASK_092": {"verdict": "FABRICATED", "notes": "Penal Code has no Section 312A. Motor vehicle offence is statutory mutation."},
    "TASK_120": {"verdict": "REAL", "notes": "71 DLR (2019) 598 Asif Imran v. State HCD Goutam Das murder case supports core context."},
    "TASK_125": {"verdict": "REAL", "notes": "69 DLR (AD) 2017 Rangamati Food Products CHT Regulation 1900 upheld as valid law."},
    "TASK_129": {"verdict": "REAL", "notes": "Section 115 CPC 1908 revisional jurisdiction is authentic."},
    "TASK_139": {"verdict": "FABRICATED", "notes": "Badiul Alam Majumdar v. Bangladesh caretaker case struck down caretaker system (64 DLR (AD) 169), claiming 16 BLC (AD) 290 declined to strike down is fabricated."}
}

print("="*80)
print("RAJUK LAW OFFICER ADJUDICATION ANALYSIS")
print("="*80)

results = []
for t_id, data in rajuk_verdicts.items():
    sub = key_df[key_df["task_id"] == t_id]
    if not sub.empty:
        gt_label = sub.iloc[0]["label"]
        gt_type = sub.iloc[0]["fabrication_type"]
        is_match = "MATCH ✅" if data["verdict"] == gt_label else "MISMATCH ⚠️"
        results.append({
            "task_id": t_id,
            "ground_truth": gt_label,
            "lawyer_verdict": data["verdict"],
            "match": is_match,
            "lawyer_reasoning": data["notes"]
        })

df_res = pd.DataFrame(results)
print(df_res.to_string(index=False))
