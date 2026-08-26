import pandas as pd
import json

# Load blind package and ground truth key
blind_df = pd.read_csv("human_annotation_package_blind_v2.csv")
key_df = pd.read_csv("annotation_ground_truth_key.csv")

# Merge key with blind_df to get ground truth
df = pd.merge(blind_df, key_df, on="task_id")

# Create report chunks (30 tasks per chunk)
chunk_size = 30
num_chunks = len(df) // chunk_size

for c in range(num_chunks):
    start_idx = c * chunk_size
    end_idx = (c + 1) * chunk_size
    sub_df = df.iloc[start_idx:end_idx]
    
    report_md = f"# Human Annotation Audit Report for Haris (Chunk {c+1}: Tasks {start_idx+1} to {end_idx})\n\n"
    report_md += "Instructions for Haris (Law Graduate Annotator):\n"
    report_md += "1. Review the Task ID, Citation, and Context.\n"
    report_md += "2. Check the AI Verdict (REAL vs FABRICATED) and the provided Rationale.\n"
    report_md += "3. Verify using the provided Primary Legal Link.\n"
    report_md += "4. Indicate whether you **AGREE** or **DISAGREE** with the verdict.\n\n"
    report_md += "---\n\n"
    
    for idx, row in sub_df.iterrows():
        t_id = row['task_id']
        cit = row['citation']
        ctx = row['context']
        url = row['extracted_url']
        label = row['label']
        fab_type = row['fabrication_type']
        
        report_md += f"### {t_id}\n"
        report_md += f"- **Citation:** `{cit}`\n"
        report_md += f"- **Context:** \"{ctx}\"\n"
        report_md += f"- **Verification URL:** [{url}]({url})\n"
        report_md += f"- **AI Verdict:** **{label}**\n"
        
        if label == "FABRICATED":
            report_md += f"- **Mutation Type:** `{fab_type}`\n"
            report_md += f"- **Legal Rationale for Haris:** This citation/context contains a deliberate mutation (`{fab_type}`). Haris should verify why it is invalid.\n"
        else:
            report_md += f"- **Legal Rationale for Haris:** This is a genuine, verified Bangladeshi legal provision/precedent.\n"
            
        report_md += f"- **Haris's Audit Verdict:** [ ] AGREE  [ ] DISAGREE\n"
        report_md += f"- **Haris's Notes:** _________________________\n\n"
        report_md += "---\n\n"
        
    out_file = f"haris_annotation_report_chunk{c+1}.md"
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(report_md)
        
    print(f"Generated {out_file} with {len(sub_df)} tasks.")

print("All 5 annotation report chunks generated successfully!")
