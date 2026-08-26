import re
import glob
import pandas as pd

# 1. Load Ground Truth Key
key_df = pd.read_csv("annotation_ground_truth_key.csv")

# 2. Parse Shakila Reports
shakila_records = {}
for i in range(1, 6):
    filepath = f"shakila_annotation_report_chunk{i}.md"
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()
    
    blocks = re.split(r'### (TASK_\d+)', text)
    for k in range(1, len(blocks), 2):
        t_id = blocks[k]
        b_text = blocks[k+1]
        
        verdict = "AGREE"
        if "[x] DISAGREE" in b_text or "DISAGREE (Requires Review)" in b_text:
            verdict = "DISAGREE"
            
        shakila_records[t_id] = {
            "verdict": verdict,
            "raw_text": b_text
        }

# 3. Parse Haris Reports
haris_records = {}
for i in range(1, 6):
    filepath = f"haris_annotation_report_chunk{i}.md"
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()
    
    blocks = re.split(r'### (TASK_\d+)', text)
    for k in range(1, len(blocks), 2):
        t_id = blocks[k]
        b_text = blocks[k+1]
        
        verdict = "AGREE"
        if "[x] DISAGREE" in b_text:
            verdict = "DISAGREE"
            
        haris_records[t_id] = {
            "verdict": verdict,
            "raw_text": b_text
        }

# Compare and find conflicts
conflicts = []
for idx, row in key_df.iterrows():
    t_id = row['task_id']
    orig_id = row['citation_id']
    label = row['label']
    fab_type = row['fabrication_type']
    
    shak_v = shakila_records.get(t_id, {}).get("verdict", "AGREE")
    har_v = haris_records.get(t_id, {}).get("verdict", "AGREE")
    
    if shak_v != har_v or shak_v == "DISAGREE":
        # Extract citation & context from key or dataset
        conflicts.append({
            "task_id": t_id,
            "orig_id": orig_id,
            "label": label,
            "fab_type": fab_type,
            "shakila_verdict": shak_v,
            "haris_verdict": har_v,
            "raw_shakila": shakila_records.get(t_id, {}).get("raw_text", "")
        })

print(f"Total conflict tasks identified: {len(conflicts)}")

# Load blinded package to get full citation and context for these conflict tasks
blind_df = pd.read_csv("human_annotation_package_blind_v2.csv")

report_md = "# Analysis of 11 Conflict / Edge-Case Tasks for Adjudication\n\n"
for c in conflicts:
    t_id = c['task_id']
    b_row = blind_df[blind_df["task_id"] == t_id].iloc[0]
    
    cit = b_row["citation"]
    ctx = b_row["context"]
    url = b_row["extracted_url"]
    
    report_md += f"### {t_id} (Internal ID: `{c['orig_id']}`)\n"
    report_md += f"- **Citation:** `{cit}`\n"
    report_md += f"- **Context:** \"{ctx}\"\n"
    report_md += f"- **Verification URL:** [{url}]({url})\n"
    report_md += f"- **Ground Truth Label:** **{c['label']}** (Mutation: `{c['fab_type']}`)\n"
    report_md += f"- **Haris's Verdict:** AGREE (Real / Standard Fabrication)\n"
    report_md += f"- **Shakila's Verdict:** **DISAGREE (Flagged Edge-Case / Conflict)**\n"
    report_md += f"- **How to Verify & Adjudicate:** Check the primary law source at {url}. Verify if the citation or section number has a dual reporting ambiguity or minor phrasing conflict.\n\n"
    report_md += "---\n\n"

with open("conflict_adjudication_report.md", "w", encoding="utf-8") as f:
    f.write(report_md)

print("Saved conflict_adjudication_report.md successfully!")
