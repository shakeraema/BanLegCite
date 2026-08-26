import os
import json
import re
import time
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

if not api_key:
    print("Error: OPENROUTER_API_KEY not found in .env")
    exit(1)

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

# Read conflict tasks
with open("conflict_adjudication_report.md", "r", encoding="utf-8") as f:
    text = f.read()

tasks = re.split(r'### (TASK_\d+)', text)

print("Starting AI Legal Verification on the 11 Conflict Tasks...\n")

results = []

for k in range(1, len(tasks), 2):
    t_id = tasks[k]
    body = tasks[k+1]
    
    cit_match = re.search(r'\*\*Citation:\*\* `(.*?)`', body)
    ctx_match = re.search(r'\*\*Context:\*\* "(.*?)"', body)
    url_match = re.search(r'\[(https?://.*?)\]', body)
    
    cit = cit_match.group(1) if cit_match else ""
    ctx = ctx_match.group(1) if ctx_match else ""
    url = url_match.group(1) if url_match else ""
    
    prompt = f"""
    You are a Bangladesh Senior Legal Scholar evaluating a benchmark dataset item.
    
    Task ID: {t_id}
    Citation: "{cit}"
    Context: "{ctx}"
    Reference URL: {url}
    
    Please evaluate:
    1. Is this citation and context REAL or FABRICATED in Bangladeshi Law?
    2. If FABRICATED, state the exact reason (e.g. non-existent section, wrong reporter volume, misstated legal holding).
    3. If REAL, confirm its statutory/judicial validity.
    4. Provide clear instructions on how a human lawyer can verify it.
    
    Format output cleanly as:
    - **Verdict**: [REAL / FABRICATED]
    - **Legal Reason**: <Reason>
    - **Verification Procedure**: <Instructions>
    """
    
    print(f"Processing {t_id}...")
    
    max_retries = 5
    res_text = ""
    for attempt in range(max_retries):
        try:
            response = client.chat.completions.create(
                model="z-ai/glm-5.2:free",
                messages=[{"role": "user", "content": prompt}],
                extra_headers={
                    "HTTP-Referer": "https://github.com/ZahidHasan7/BanLegit-Cite",
                    "X-Title": "BanLegit-Cite Research"
                }
            )
            res_text = response.choices[0].message.content.strip()
            break
        except Exception as e:
            print(f"Error: {e}. Retrying in 5s...")
            time.sleep(5)
            
    results.append({
        "task_id": t_id,
        "citation": cit,
        "context": ctx,
        "url": url,
        "ai_eval": res_text
    })
    time.sleep(1)

# Write to markdown
out_md = "# Detailed AI Adjudication & Verification Guide for the 11 Conflict Tasks\n\n"
for r in results:
    out_md += f"### {r['task_id']}\n"
    out_md += f"- **Citation:** `{r['citation']}`\n"
    out_md += f"- **Context:** \"{r['context']}\"\n"
    out_md += f"- **Verification URL:** [{r['url']}]({r['url']})\n\n"
    out_md += f"#### AI Verification Analysis:\n{r['ai_eval']}\n\n---\n\n"

with open("gemini_conflict_verification_guide.md", "w", encoding="utf-8") as f:
    f.write(out_md)

print("Saved gemini_conflict_verification_guide.md successfully!")
