import os
import json
import requests

def run_chunk2_with_claude():
    # Load env vars
    env_vars = {}
    if os.path.exists(".env"):
        with open(".env", "r") as f:
            for line in f:
                if "=" in line:
                    key, val = line.strip().split("=", 1)
                    env_vars[key] = val
                    
    api_key = env_vars.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("Error: ANTHROPIC_API_KEY not found in .env")
        return
        
    # Read context files
    with open("BanLegit-Cite: Full Rebuild Roadmap.md", "r", encoding="utf-8") as f:
        roadmap = f.read()
        
    with open("audits_first.md", "r", encoding="utf-8") as f:
        audits_first = f.read()
        
    with open("Chunk 1 audit inventory of all 90 existing BanLegit-Cite tasks.md", "r", encoding="utf-8") as f:
        audit_inventory = f.read()
        
    # Construct the prompt
    prompt = f"""
You are the Lead Legal NLP Research Architect. We are executing Chunk 2 of the "BanLegit-Cite: Full Rebuild Roadmap".

Here is the context of what we have completed in Chunk 1:
### 1. audits_first.md
{audits_first}

### 2. Chunk 1 Audit Inventory
{audit_inventory}

### 3. Rebuild Roadmap
{roadmap}

---

### Your Task (CHUNK 2 — Target Dataset Structure & Taxonomy Coverage Matrix):
Generate the contents of `dataset_spec.md` as specified in Chunk 2 of the roadmap. 

The specification must define:
1.  **Target Size (N = 150 unique instances)**: Frame this as the locked target size.
2.  **Statutory vs. Precedent Split**: Design a balanced split (e.g. 75 statutory, 75 precedent).
3.  **Real vs. Fabricated Balance**: 1:1 ratio (75 Real, 75 Fabricated).
4.  **Per-Category Minimums**: Define a minimum of exactly 15 instances for each of the 10 taxonomy categories (S1-S5, P1-P5).
    - statutory fabrications: S1 (15), S2 (15), S3 (15), S4 (15), S5 (15) -> Total = 75 tasks.
    - precedent fabrications: P1 (15), P2 (15), P3 (15), P4 (15), P5 (15) -> Total = 75 tasks.
    - statutory real: 37 or 38 tasks.
    - precedent real: 37 or 38 tasks.
5.  **No Verbatim Duplication Rule**: Outline the strict constraint that no real citation is repeated verbatim (retiring the old triplication pattern).
6.  **Taxonomy Definitions**: Document the S1-S5 and P1-P5 category definitions.

Please return only the markdown contents of `dataset_spec.md` to be written directly to a file.
"""

    url = "https://api.anthropic.com/v1/messages"
    headers = {
        "x-api-key": api_key,
        "anthropic-version": "2023-06-01",
        "content-type": "application/json"
    }
    
    payload = {
        "model": "claude-3-5-sonnet-20241022",
        "max_tokens": 4000,
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }
    
    print("Calling Anthropic Claude API for Chunk 2...")
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code != 200:
        print(f"API Error ({response.status_code}): {response.text}")
        return
        
    res_data = response.json()
    content = res_data["content"][0]["text"]
    
    # Strip any markdown code block wrappers if Claude returned them
    spec_content = content
    if spec_content.startswith("```markdown"):
        spec_content = spec_content[11:]
    elif spec_content.startswith("```"):
        spec_content = spec_content[3:]
    if spec_content.endswith("```"):
        spec_content = spec_content[:-3]
        
    spec_content = spec_content.strip()
    
    # Write to dataset_spec.md
    with open("dataset_spec.md", "w", encoding="utf-8") as f:
        f.write(spec_content + "\n")
        
    print("\nSuccessfully executed Chunk 2 and wrote output to dataset_spec.md")
    print("=== dataset_spec.md Contents ===")
    print(spec_content[:1000] + "\n...")

if __name__ == "__main__":
    run_chunk2_with_claude()
