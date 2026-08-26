import re
import json
import pandas as pd

# Load statutory anchors
with open("statutory_anchors.md", "r", encoding="utf-8") as f:
    stat_text = f.read()

stat_tasks = []
stat_blocks = re.split(r'\*\*Task S\d+\*\*', stat_text)

for idx, block in enumerate(stat_blocks[1:], 1):
    ctx_match = re.search(r'\*\*Context:\*\* "(.*?)"', block, re.DOTALL)
    cit_match = re.search(r'\*\*Citation:\*\* (.*)', block)
    url_match = re.search(r'(https?://[^\s]+)', block)
    
    if ctx_match and cit_match:
        stat_tasks.append({
            "citation_id": f"STAT_REAL_{idx}",
            "citation": cit_match.group(1).strip(),
            "context": ctx_match.group(1).strip(),
            "source": "Statute",
            "extracted_url": url_match.group(1).strip() if url_match else "http://bdlaws.minlaw.gov.bd/",
            "fabrication_type": "N/A",
            "label": "REAL"
        })

print(f"Parsed {len(stat_tasks)} statutory real tasks.")

# Load precedent anchors from new_dataset.md
with open("new_dataset.md", "r", encoding="utf-8") as f:
    prec_text = f.read()

prec_tasks = []
prec_blocks = re.split(r'#+\s*Task\s*\d+', prec_text)

for idx, block in enumerate(prec_blocks[1:], 1):
    ctx_match = re.search(r'> Context: "(.*?)"', block, re.DOTALL)
    cit_match = re.search(r'> Citation: (.*)', block)
    url_match = re.search(r'(https?://[^\s]+)', block)
    
    if ctx_match and cit_match:
        prec_tasks.append({
            "citation_id": f"PREC_REAL_{idx}",
            "citation": cit_match.group(1).strip(),
            "context": ctx_match.group(1).strip(),
            "source": "Precedent",
            "extracted_url": url_match.group(1).strip() if url_match else "http://www.supremecourt.gov.bd/",
            "fabrication_type": "N/A",
            "label": "REAL"
        })

print(f"Parsed {len(prec_tasks)} precedent real tasks.")

all_real = stat_tasks + prec_tasks
print(f"Total REAL tasks count: {len(all_real)}")

# Save to tasks_real_75.jsonl
with open("tasks_real_75.jsonl", "w", encoding="utf-8") as f:
    for task in all_real:
        f.write(json.dumps(task, ensure_ascii=False) + "\n")

# Combine 75 REAL + 75 FABRICATED into tasks_150_v2.jsonl
with open("tasks_fabricated_75.jsonl", "r", encoding="utf-8") as f:
    fab_tasks = [json.loads(line) for line in f if line.strip()]

all_150 = all_real + fab_tasks
print(f"Total Combined v2.0 Dataset size: {len(all_150)} tasks")

with open("tasks_150_v2.jsonl", "w", encoding="utf-8") as f:
    for task in all_150:
        f.write(json.dumps(task, ensure_ascii=False) + "\n")

# Save as CSV as well
df_150 = pd.DataFrame(all_150)
df_150.to_csv("banlegit_cite_v2_dataset.csv", index=False)

print("Saved tasks_real_75.jsonl, tasks_150_v2.jsonl, and banlegit_cite_v2_dataset.csv!")
