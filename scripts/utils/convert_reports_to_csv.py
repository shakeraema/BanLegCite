import pandas as pd

# Load blind dataset + ground truth key
blind_df = pd.read_csv("human_annotation_package_blind_v2.csv")
key_df = pd.read_csv("annotation_ground_truth_key.csv")

# Merge
df = pd.merge(blind_df, key_df, on="task_id")

# Create 5 CSV chunks (30 items each)
chunk_size = 30
num_chunks = len(df) // chunk_size

for c in range(num_chunks):
    start_idx = c * chunk_size
    end_idx = (c + 1) * chunk_size
    sub_df = df.iloc[start_idx:end_idx].copy()
    
    # Prepare human-friendly CSV columns
    csv_df = pd.DataFrame({
        "Task_ID": sub_df["task_id"],
        "Citation": sub_df["citation"],
        "Context": sub_df["context"],
        "Verification_URL": sub_df["extracted_url"],
        "AI_Verdict": sub_df["label"],
        "Mutation_Type": sub_df["fabrication_type"],
        "Human_Verdict (AGREE / DISAGREE)": "",  # Blank for Haris to fill
        "Human_Notes": ""                          # Blank for Haris notes
    })
    
    out_csv = f"haris_annotation_report_chunk{c+1}.csv"
    csv_df.to_csv(out_csv, index=False)
    print(f"Generated {out_csv}")

print("All 5 CSV chunk files generated successfully!")
