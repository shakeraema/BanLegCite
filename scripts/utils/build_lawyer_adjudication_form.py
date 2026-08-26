import re
import pandas as pd

# Load blind dataset + ground truth key
blind_df = pd.read_csv("human_annotation_package_blind_v2.csv")
key_df = pd.read_csv("annotation_ground_truth_key.csv")

# Merge
df = pd.merge(blind_df, key_df, on="task_id")

# Read conflict tasks list
with open("conflict_adjudication_report.md", "r", encoding="utf-8") as f:
    text = f.read()

conflict_ids = re.findall(r'### (TASK_\d+)', text)

lawyer_md = "# Senior Lawyer Final Adjudication & Binding Verdict Report\n\n"
lawyer_md += "**Project:** BanLegit-Cite v2.0 Dataset Validation\n"
lawyer_md += "**Purpose:** Senior Legal Expert Adjudication on 11 Disputed / Edge-Case Benchmark Items\n"
lawyer_md += "**Instructions for Senior Lawyer / Adjudicator:**\n"
lawyer_md += "1. Review the Task ID, Citation, and Context for each of the 11 disputed items.\n"
lawyer_md += "2. Click the primary source link to verify against Bangladesh statutory and case law.\n"
lawyer_md += "3. Check the AI Ground Truth and Annotator Audit findings.\n"
lawyer_md += "4. Mark your **FINAL BINDING VERDICT** (`REAL` or `FABRICATED`) and sign with your notes.\n\n"
lawyer_md += "="*80 + "\n\n"

for t_id in conflict_ids:
    sub = df[df["task_id"] == t_id]
    if sub.empty:
        continue
    row = sub.iloc[0]
    
    cit = row["citation"]
    ctx = row["context"]
    url = row["extracted_url"]
    label = row["label"]
    fab_type = row["fabrication_type"]
    orig_id = row["citation_id"]
    
    lawyer_md += f"## ADJUDICATION TASK: {t_id} (Ref: `{orig_id}`)\n\n"
    lawyer_md += f"- **Citation Under Audit:** `{cit}`\n"
    lawyer_md += f"- **Context Paragraph:** \"{ctx}\"\n"
    lawyer_md += f"- **Primary Verification Link:** [{url}]({url})\n\n"
    
    lawyer_md += "### Discrepancy & Evidence Overview:\n"
    lawyer_md += f"- **AI Baseline / Ground Truth:** **{label}**"
    if label == "FABRICATED":
        lawyer_md += f" (Mutation Category: `{fab_type}`)"
    lawyer_md += "\n"
    lawyer_md += f"- **Annotator Conflict Summary:** Annotator 1 (Haris) marked `REAL/STANDARD`, while Annotator 2 (Shakila) flagged `DISAGREE` due to reporting volume or statutory amendment ambiguity.\n\n"
    
    lawyer_md += "### Senior Lawyer's Final Binding Decision:\n"
    lawyer_md += "- [ ] **CONFIRM REAL** (Citation and context are authentic under BD law)\n"
    lawyer_md += "- [ ] **CONFIRM FABRICATED** (Citation or context contains genuine legal mutation)\n"
    lawyer_md += "- [ ] **DROP FROM DATASET** (Item is irreconcilably ambiguous)\n\n"
    lawyer_md += "**Lawyer's Legal Reasoning & Notes:**\n"
    lawyer_md += "_________________________________________________________________________________\n"
    lawyer_md += "_________________________________________________________________________________\n\n"
    lawyer_md += "-"*80 + "\n\n"

lawyer_md += "\n## Senior Lawyer Certification\n\n"
lawyer_md += "I hereby certify that I have independently reviewed the 11 disputed legal items against primary Bangladesh legal authorities (Dhaka Law Reports, Supreme Court Bulletins, and Bangladesh Code) and issued my final binding verdicts above.\n\n"
lawyer_md += "**Senior Lawyer Name:** _________________________\n"
lawyer_md += "**Designation / Bar Roll:** _________________________\n"
lawyer_md += "**Date:** ____ / ____ / 2026\n"

output_path = "senior_lawyer_adjudication_report.md"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(lawyer_md)

print(f"Saved senior lawyer adjudication report to {output_path}!")
