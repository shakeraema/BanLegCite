import os
import json
import time
from dotenv import load_dotenv
from openai import OpenAI
import pandas as pd

load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

if not api_key:
    print("Error: OPENROUTER_API_KEY not found in .env")
    exit(1)

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

# 1. Load existing 45 fabricated cases
df = pd.read_csv("data/release/banlegit_cite_dataset.csv")
fab_df = df[df["label"] == "FABRICATED"].copy()

existing_count = len(fab_df)
print(f"Existing fabricated cases count: {existing_count}")

# 2. We need 30 new fabricated cases (15 Statutory S1-S5, 15 Precedent P1-P5)
prompt = """
You are a legal dataset generator for Bangladesh law. Please generate 30 FABRICATED legal citation benchmarks.
Each task must be a JSON object with:
- "citation_id": String (e.g. "FAB_NEW_1" to "FAB_NEW_30")
- "citation": String (e.g. "Section 999, Penal Code, 1860" or "99 DLR (AD) 500")
- "context": String (A 2-3 sentence context describing the fabricated legal holding or section)
- "source": String (e.g. "Penal Code, 1860", "CrPC, 1898", "Dhaka Law Reports (AD)", "Nari O Shishu Nirjatan Daman Act, 2000")
- "fabrication_type": String (Must be one of: "S1: Non-Existent Section", "S2: Wrong Act Attribution", "S3: Misstated Content", "S4: Cross-Jurisdictional Bleed", "S5: Repealed Section", "P1: Non-Existent Case", "P2: Wrong Citation Locator", "P3: Misattributed Holding", "P4: Wrong Court Level", "P5: Cross-Jurisdictional Bleed")
- "extracted_url": String (Provide a generic URL like "http://bdlaws.minlaw.gov.bd/" or "http://www.supremecourt.gov.bd/")
- "label": "FABRICATED"

Generate exactly 30 JSON objects in a JSON array `[...]`. Return ONLY valid JSON, no markdown code blocks.
"""

print("Requesting 30 new fabricated cases from GLM 5.2...")

max_retries = 5
response_text = ""
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
        response_text = response.choices[0].message.content.strip()
        break
    except Exception as e:
        print(f"API error: {e}. Retrying in 5s...")
        time.sleep(5)

# Clean json codeblocks if any
if response_text.startswith("```"):
    response_text = response_text.split("```")[1]
    if response_text.startswith("json"):
        response_text = response_text[4:]
response_text = response_text.strip()

new_fab_list = json.loads(response_text)
print(f"Successfully generated {len(new_fab_list)} new fabricated cases!")

# Create new DataFrame
new_fab_df = pd.DataFrame(new_fab_list)

# Combine existing 45 + new 30
combined_fab_df = pd.concat([fab_df, new_fab_df], ignore_index=True)
print(f"Total combined fabricated cases: {len(combined_fab_df)}")

# Write to markdown file fabricated_cases_75.md
md_content = f"# All 75 Fabricated Cases (45 Gemini + 30 GLM 5.2)\n\nTotal Count: **{len(combined_fab_df)}**\n\n"

for idx, row in combined_fab_df.iterrows():
    md_content += f"### Task {idx+1}: {row['citation_id']}\n"
    md_content += f"- **Citation:** {row['citation']}\n"
    md_content += f"- **Context:** {row['context']}\n"
    md_content += f"- **Source:** {row.get('source', 'N/A')}\n"
    md_content += f"- **Fabrication Type:** {row['fabrication_type']}\n"
    md_content += f"- **Extracted URL:** {row.get('extracted_url', 'N/A')}\n"
    md_content += f"- **Label:** FABRICATED\n\n"

out_md = "fabricated_cases_75.md"
with open(out_md, "w", encoding="utf-8") as f:
    f.write(md_content)

# Also save to JSONL
combined_fab_df.to_json("tasks_fabricated_75.jsonl", orient="records", lines=True)

print(f"Saved to {out_md} and tasks_fabricated_75.jsonl!")
