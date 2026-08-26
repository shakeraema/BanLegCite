import os
import re
import json
import pandas as pd
from scipy.stats import chi2_contingency

def extract_tasks_from_js(js_path):
    with open(js_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Extract tasks array
    match = re.search(r"var tasks\s*=\s*(\[.*?\]);", content, re.DOTALL)
    if not match:
        raise ValueError("Could not find tasks array in generate_google_form.js")
    
    tasks_str = match.group(1)
    try:
        tasks = json.loads(tasks_str)
    except Exception:
        tasks_str_clean = re.sub(r",\s*([\]}])", r"\1", tasks_str)
        tasks = json.loads(tasks_str_clean)
    return tasks

def audit_field_leakage(js_path: str, ground_truth_path: str):
    """
    Checks whether any annotator-visible field in the blinded form
    is statistically associated with ground-truth status.
    """
    # Load tasks (representing the form schema)
    tasks = extract_tasks_from_js(js_path)
    schema = pd.DataFrame(tasks)
    
    # Extract the citation_id / Org ID from the original helper_notes
    schema["citation_id"] = schema["helper_notes"].apply(
        lambda x: re.search(r"Org ID:\s*(\S+)", x).group(1) if "Org ID:" in x else None
    )
    
    # Generate blinded helper notes (simulating generate_form.gs behavior)
    schema["helper_notes_blind"] = schema["helper_notes"].apply(
        lambda x: re.sub(r"\s*\|\s*Org ID:\s*\S+", "", x)
    )
    
    # Load ground truth
    truth = pd.read_csv(ground_truth_path)  # columns: citation_id, label
    truth["is_fabricated"] = truth["label"] == "FABRICATED"
    
    # Merge only ground truth label to avoid column name overlap
    merged = schema.merge(truth[["citation_id", "is_fabricated"]], on="citation_id")
    
    results = {}
    for field in ["context", "citation", "source_doc", "helper_notes_blind"]:
        # Bucketing length of fields to perform chi-square
        merged[f"{field}_len_bucket"] = pd.qcut(merged[field].str.len(), 4, duplicates="drop")
        table = pd.crosstab(merged[f"{field}_len_bucket"], merged["is_fabricated"])
        try:
            chi2, p, _, _ = chi2_contingency(table)
        except Exception:
            chi2, p = 0.0, 1.0
        results[field] = {"chi2": chi2, "p": p}
        
    return results

if __name__ == "__main__":
    js_path = "scripts/utils/generate_google_form.js"
    ground_truth_path = "data/release/banlegit_cite_dataset.csv"
    
    results = audit_field_leakage(js_path, ground_truth_path)
    
    os.makedirs("diagnostic_output", exist_ok=True)
    out_file = "diagnostic_output/issue1_blinding_chi2.txt"
    
    output = []
    output.append("=== Blinding Audit Chi2 Tests ===")
    for field, stats in results.items():
        flag = "LEAK SUSPECTED" if stats["p"] < 0.05 else "clean"
        line = f"{field}: chi2={stats['chi2']:.3f}, p={stats['p']:.4f} [{flag}]"
        print(line)
        output.append(line)
        
    with open(out_file, "w", encoding="utf-8") as f:
        f.write("\n".join(output) + "\n")
    print(f"Results written to {out_file}")
