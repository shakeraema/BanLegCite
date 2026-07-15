import os
import glob
import json
import random

def run_spot_check(input_dir: str = "data/raw", sample_percentage: float = 0.05):
    """Samples percentage of raw extractions for human verification."""
    print(f"=== Starting Spot Check Verification (Sample: {sample_percentage*100}%) ===")
    
    raw_files = glob.glob(os.path.join(input_dir, "*_raw.json"))
    all_citations = []
    
    for file_path in raw_files:
        with open(file_path, "r", encoding="utf-8") as f:
            raw_data = json.load(f)
            all_citations.extend(raw_data.get("data", []))
            
    if not all_citations:
        print("No citations found to spot check.")
        return
        
    sample_size = max(1, int(len(all_citations) * sample_percentage))
    sampled_items = random.sample(all_citations, sample_size)
    
    print(f"Sampled {sample_size} of {len(all_citations)} total citations:")
    
    report = []
    report.append(f"# Spot-Check Quality Report - {sample_percentage*100}% sample size")
    report.append(f"Total Raw Citations: {len(all_citations)}")
    report.append(f"Sample Size: {sample_size}\n")
    report.append("## Sampled Items for Human Verification\n")
    
    for idx, item in enumerate(sampled_items):
        print(f"[{idx+1}] ID: {item['citation_id']} | Cit: {item['citation']}")
        report.append(f"### {idx+1}. Citation: `{item['citation']}`")
        report.append(f"- **ID:** {item['citation_id']}")
        report.append(f"- **Source:** {item['source']}")
        report.append(f"- **Context:** {item['context']}")
        report.append(f"- **Extracted URL:** [{item['extracted_url']}]({item['extracted_url']})")
        report.append("- **Verification Verdict:** [ ] Pass  [ ] Fail")
        report.append("- **Notes:** \n")
        
    report_path = "logs/spot_check_report.md"
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("\n".join(report))
        
    print(f"\nQuality verification spot check saved to {report_path}")

if __name__ == "__main__":
    run_spot_check()
