import os
import glob
import json
import random
from datetime import datetime

# Optional GenAI library import
try:
    import google.generativeai as genai
    HAS_GENAI = True
except ImportError:
    HAS_GENAI = False

def query_gemini_fabrication(citation_text: str, context: str) -> dict:
    """Uses Gemini API to fabricate a citation and rewrite the legal proposition context."""
    api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
    if not api_key or not HAS_GENAI:
        return None
        
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-3.5-flash")
        
        prompt = f"""
You are a legal citation fabrication bot. Your job is to take a real Bangladeshi court citation and its context, and produce a fabricated citation record that looks extremely realistic but is factually incorrect.

Real Citation: "{citation_text}"
Real Context: "{context}"

Generate a JSON response with the following keys:
1. "fabricated_citation": A realistic but incorrect citation string (e.g., change page/volume numbers slightly, e.g. from "52 DLR (AD) 12" to "52 DLR (AD) 255" or "50 DLR (HCD) 12").
2. "fabricated_context": A context paragraph that quotes the fabricated citation and states a slightly modified, incorrect, or completely fabricated legal holding or case facts.
3. "fabrication_type": Choose from ["Incorrect Volume/Page", "Non-Existent Case", "Misattributed Text", "Jurisdiction Mismatch"]

Return ONLY the raw JSON object, without markdown formatting blocks.
"""
        response = model.generate_content(prompt)
        # Parse the JSON response
        text = response.text.strip()
        # Clean markdown code block wraps if any
        if text.startswith("```"):
            text = "\n".join(text.split("\n")[1:-1])
        return json.loads(text)
    except Exception as e:
        print(f"Gemini fabrication call failed: {e}. Falling back to rule-based fabrication.")
        return None

def rule_based_fabrication(citation: dict) -> dict:
    """Fallback function to perform programmatic high-fidelity citation fabrication."""
    citation_text = citation["citation"]
    context = citation["context"]
    
    # Parse out citation numbers
    nums = re.findall(r'\d+', citation_text)
    fabricated_citation = citation_text
    
    if len(nums) >= 2:
        # Alter volume or page number randomly
        vol, page = nums[0], nums[-1]
        new_page = str(int(page) + random.randint(100, 300))
        fabricated_citation = citation_text.replace(page, new_page)
        fabrication_type = "Incorrect Volume/Page"
    else:
        fabricated_citation = f"99 {citation['source'][:3]} (AD) 999"
        fabrication_type = "Non-Existent Case"
        
    # Introduce legal holding distortion in context
    fabricated_context = context.replace("held:", "held (contrary to the actual ruling):")
    fabricated_context = fabricated_context.replace("observed:", "incorrectly observed:")
    fabricated_context = fabricated_context.replace("clarified that", "incorrectly stated that")
    
    return {
        "fabricated_citation": fabricated_citation,
        "fabricated_context": f"Applying the fabricated rule from {fabricated_citation}, the court supposedly held a modified legal principle: {fabricated_context}",
        "fabrication_type": fabrication_type
    }

import re

def process_fabrications(input_dir: str = "data/raw", output_dir: str = "data/annotated"):
    os.makedirs(output_dir, exist_ok=True)
    raw_files = glob.glob(os.path.join(input_dir, "*_raw.json"))
    
    for file_path in raw_files:
        print(f"Processing fabrication batch for {os.path.basename(file_path)}...")
        with open(file_path, "r", encoding="utf-8") as f:
            raw_data = json.load(f)
            
        metadata = raw_data.get("metadata", {})
        data = raw_data.get("data", [])
        
        fabricated_batch = []
        
        # Batch and gate rule: ≤50 examples in units
        for item in data[:50]:
            print(f"Fabricating citation: {item['citation']}...")
            fab_result = query_gemini_fabrication(item["citation"], item["context"])
            if not fab_result:
                fab_result = rule_based_fabrication(item)
                
            fabricated_batch.append({
                "citation_id": item["citation_id"].replace("REAL", "FABRICATED"),
                "citation": fab_result["fabricated_citation"],
                "context": fab_result["fabricated_context"],
                "source": item["source"],
                "extracted_url": item["extracted_url"],
                "fabrication_type": fab_result["fabrication_type"],
                "label": "FABRICATED"
            })
            
        # Add labels to real citations
        real_labeled = []
        for item in data:
            real_labeled.append({
                "citation_id": item["citation_id"],
                "citation": item["citation"],
                "context": item["context"],
                "source": item["source"],
                "extracted_url": item["extracted_url"],
                "fabrication_type": "N/A",
                "label": "REAL"
            })
            
        # Combine matching 1:1 distribution
        combined_dataset = real_labeled + fabricated_batch
        
        output_metadata = {
            "produced_by": "fabricator.py",
            "date": datetime.now().strftime("%Y-%m-%d"),
            "reviewed_by": "pending",
            "stage": "Phase 2 — Fabrication Pipeline",
            "commit": "pending"
        }
        
        output_file = os.path.join(output_dir, os.path.basename(file_path).replace("_raw.json", "_annotated.json"))
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump({"metadata": output_metadata, "data": combined_dataset}, f, indent=2, ensure_ascii=False)
            
        print(f"Saved {len(combined_dataset)} items (REAL + FABRICATED) to {output_file}")

if __name__ == "__main__":
    process_fabrications()
