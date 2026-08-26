import os
import json
import re
from dotenv import load_dotenv

# Try importing google-genai or google.generativeai or openai client for gemini
load_dotenv()
gemini_key = os.getenv("GEMINI_API_KEY")

try:
    import google.generativeai as genai
    genai.configure(api_key=gemini_key)
    # Use gemini-1.5-flash or gemini-1.5-pro
    model = genai.GenerativeModel("gemini-1.5-pro")
    USE_NATIVE_GEMINI = True
except Exception as e:
    print(f"Native Gemini import error: {e}")
    USE_NATIVE_GEMINI = False

# Read the conflict tasks from conflict_adjudication_report.md
with open("conflict_adjudication_report.md", "r", encoding="utf-8") as f:
    text = f.read()

tasks = re.split(r'### (TASK_\d+)', text)

print("Starting Gemini Adjudication on the 11 Conflict Tasks...\n")

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
    You are an expert Bangladeshi Legal Adjudicator.
    Please evaluate the following citation and context string under Bangladesh Law:
    
    Task ID: {t_id}
    Citation: "{cit}"
    Context: "{ctx}"
    
    Is this legal citation and context REAL or FABRICATED under Bangladesh Law?
    If FABRICATED, explain why (e.g. non-existent section, wrong reporter volume, misstated holding).
    If REAL, confirm its validity.
    
    Provide your response strictly in 3 lines:
    1. Verdict: REAL or FABRICATED
    2. Primary Reason: <one sentence reason>
    3. Verification Advice: <how a lawyer should verify it>
    """
    
    print(f"Querying Gemini for {t_id}...")
    
    if USE_NATIVE_GEMINI:
        try:
            res = model.generate_content(prompt)
            verdict_text = res.text.strip()
        except Exception as err:
            verdict_text = f"API Error: {err}"
    else:
        verdict_text = "Gemini SDK not configured properly."
        
    print(f"--- {t_id} Gemini Output ---")
    print(verdict_text)
    print("\n" + "="*40 + "\n")
    
    results.append({
        "task_id": t_id,
        "citation": cit,
        "gemini_adjudication": verdict_text
    })

# Save results
with open("gemini_conflict_adjudication.md", "w", encoding="utf-8") as f:
    f.write("# Gemini Independent Adjudication of the 11 Conflict Tasks\n\n")
    for r in results:
        f.write(f"### {r['task_id']}\n")
        f.write(f"- **Citation:** `{r['citation']}`\n")
        f.write(f"- **Gemini Verdict & Reason:**\n```\n{r['gemini_adjudication']}\n```\n\n---\n\n")

print("Saved gemini_conflict_adjudication.md successfully!")
