import re

with open("verified bushra's report.md", "r", encoding="utf-8") as f:
    text = f.read()

# Parse tasks from Bushra's report
tasks = re.split(r'TASK_\d+', text)

disagreements = []
all_parsed = []

blocks = re.findall(r'(TASK_\d+)[\s\S]*?(?=(TASK_\d+|$))', text)

for block_tuple in blocks:
    t_id = block_tuple[0]
    block_text = block_tuple[1]
    
    # Check for DISAGREE
    is_disagree = "DISAGREE" in block_text and ("[x] DISAGREE" in block_text or "[x]DISAGREE" in block_text or "DISAGREE" in block_text.split("Audit Verdict:")[1].split("\n")[0] if "Audit Verdict:" in block_text else False)
    
    # Extract AI Verdict
    ai_verdict = "UNKNOWN"
    if "AI Verdict:" in block_text:
        ai_verdict = block_text.split("AI Verdict:")[1].split("\n")[0].strip()
        
    # Extract Citation
    citation = "UNKNOWN"
    if "Citation:" in block_text:
        citation = block_text.split("Citation:")[1].split("\n")[0].strip()

    # Extract Context
    context = "UNKNOWN"
    if "Context:" in block_text:
        context = block_text.split("Context:")[1].split("\n")[0].strip()

    # Extract Verification URL
    url = "UNKNOWN"
    if "Verification URL:" in block_text:
        url = block_text.split("Verification URL:")[1].split("\n")[0].strip()

    # Extract Bushra's Audit Verdict
    bushra_verdict = "AGREE"
    if "Audit Verdict:" in block_text:
        v_line = block_text.split("Audit Verdict:")[1].split("\n")[0]
        if "[x] DISAGREE" in v_line or "[x]DISAGREE" in v_line or "DISAGREE" in v_line:
            bushra_verdict = "DISAGREE"
            
    # Extract Bushra's Notes
    notes = ""
    if "Bushra's Notes:" in block_text:
        notes = block_text.split("Bushra's Notes:")[1].split("\n")[0].strip()

    all_parsed.append({
        "task_id": t_id,
        "citation": citation,
        "context": context,
        "url": url,
        "ai_verdict": ai_verdict,
        "bushra_verdict": bushra_verdict,
        "notes": notes
    })

print(f"Total parsed tasks in Bushra's report: {len(all_parsed)}")

disagreed_tasks = [t for t in all_parsed if t["bushra_verdict"] == "DISAGREE"]
print(f"Total DISAGREE tasks found in Bushra's report: {len(disagreed_tasks)}")

for t in disagreed_tasks:
    print(f"{t['task_id']} | AI: {t['ai_verdict']} | Citation: {t['citation']} | Notes: {t['notes']}")
