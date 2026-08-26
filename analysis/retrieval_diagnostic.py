import os
import glob
import json
import pandas as pd
from scripts.evaluation.retriever import LocalRetriever

def run_diagnostic():
    # Instantiate the same retriever used in evaluation
    retriever = LocalRetriever()
    
    # Find the latest agentic run result file in experiments/results/
    agentic_files = glob.glob("experiments/results/stage4_gemini_agentic_*.json")
    if not agentic_files:
        print("No existing agentic result logs found.")
        return
        
    latest_file = max(agentic_files, key=os.path.getmtime)
    print(f"Reading latest agentic run log: {latest_file}")
    
    with open(latest_file, "r", encoding="utf-8") as f:
        log_data = json.load(f)
        
    results = log_data.get("results", [])
    records = []
    
    for r in results:
        citation = r["citation"]
        gt = r["ground_truth"]
        
        # Determine if it is a hit in the retriever
        citation_key = citation.strip().lower()
        hit = (citation_key in retriever.index) or any(
            key in citation_key or citation_key in key for key in retriever.index
        )
        
        records.append({
            "citation_id": r.get("citation_id", "UNKNOWN"),
            "citation": citation,
            "ground_truth": gt,
            "hit": hit
        })
        
    df = pd.DataFrame(records)
    
    # Compute hit rate by ground truth
    hit_rates = df.groupby("ground_truth")["hit"].mean().reset_index()
    hit_rates.columns = ["ground_truth", "hit_rate"]
    
    print("\n=== Retrieval Hit Rate by Ground Truth ===")
    print(hit_rates.to_string(index=False))
    
    # Write to diagnostic_output/issue2_hitrate.csv
    os.makedirs("diagnostic_output", exist_ok=True)
    out_csv = "diagnostic_output/issue2_hitrate.csv"
    hit_rates.to_csv(out_csv, index=False)
    print(f"\nSaved hit rate table to {out_csv}")
    
    # Write a quick text summary as well
    out_txt = "diagnostic_output/issue2_hitrate.txt"
    with open(out_txt, "w") as f:
        f.write("=== Retrieval Hit Rate by Ground Truth ===\n")
        f.write(hit_rates.to_string(index=False) + "\n")

if __name__ == "__main__":
    run_diagnostic()
