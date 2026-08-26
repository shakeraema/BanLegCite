import os
import re
import json
import numpy as np
from scipy import stats

def extract_tasks_from_js(js_path):
    with open(js_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Extract tasks array
    match = re.search(r"var tasks\s*=\s*(\[.*?\]);", content, re.DOTALL)
    if not match:
        raise ValueError("Could not find tasks array in generate_google_form.js")
    
    tasks_str = match.group(1)
    # Convert tasks_str to valid JSON (it is already mostly valid JSON)
    try:
        tasks = json.loads(tasks_str)
    except Exception as e:
        # Fallback if there are minor JS syntax differences
        # Use regex to clean up/convert
        # Replace trailing commas if any
        tasks_str_clean = re.sub(r",\s*([\]}])", r"\1", tasks_str)
        tasks = json.loads(tasks_str_clean)
    return tasks

def run_field_audit():
    js_path = "scripts/utils/generate_google_form.js"
    tasks = extract_tasks_from_js(js_path)
    
    records = []
    for i, t in enumerate(tasks):
        helper = t["helper_notes"]
        # Extract ground truth from Org ID
        is_fabricated = "FABRICATED" in helper
        
        # Calculate features
        context_len = len(t["context"])
        citation_len = len(t["citation"])
        source_len = len(t["source_doc"])
        
        # Punctuation counts
        context_commas = t["context"].count(",")
        context_colons = t["context"].count(":")
        context_parentheses = t["context"].count("(") + t["context"].count(")")
        
        # Key substrings
        has_contrary = "contrary to the actual ruling" in t["context"].lower()
        has_fabricated_rule = "fabricated rule" in t["context"].lower()
        
        records.append({
            "index": i,
            "is_fabricated": is_fabricated,
            "context_len": context_len,
            "citation_len": citation_len,
            "source_len": source_len,
            "context_commas": context_commas,
            "context_colons": context_colons,
            "context_parentheses": context_parentheses,
            "has_contrary": has_contrary,
            "has_fabricated_rule": has_fabricated_rule
        })
        
    os.makedirs("diagnostic_output", exist_ok=True)
    audit_file = "diagnostic_output/issue1_field_audit.txt"
    
    # Analyze
    reals = [r for r in records if not r["is_fabricated"]]
    fabs = [r for r in records if r["is_fabricated"]]
    
    report = []
    report.append("============================================================")
    report.append("  BanLegit-Cite Annotation Blinding - Field Audit Report")
    report.append("============================================================")
    report.append(f"Total tasks: {len(records)} (Real: {len(reals)}, Fabricated: {len(fabs)})")
    report.append("")
    
    # 1. Check ordering pattern
    # Let's check if all reals are grouped together and all fabs are grouped together
    real_indices = [r["index"] for r in reals]
    fab_indices = [r["index"] for r in fabs]
    report.append("--- Ordering Analysis ---")
    report.append(f"Real task indices range: {min(real_indices)} to {max(real_indices)}")
    report.append(f"Fabricated task indices range: {min(fab_indices)} to {max(fab_indices)}")
    
    # Check if they are strictly separated
    is_separated = max(real_indices) < min(fab_indices) or max(fab_indices) < min(real_indices)
    report.append(f"Are classes strictly separated in ordering? {is_separated}")
    if is_separated:
        report.append("WARNING: Real and Fabricated tasks are completely separated in ordering, which might introduce an ordering signal!")
    else:
        report.append("No strict ordering separation detected.")
    report.append("")
    
    # 2. Check continuous features
    report.append("--- Statistical Comparison of Continuous Features (t-test) ---")
    features = ["context_len", "citation_len", "source_len", "context_commas", "context_colons", "context_parentheses"]
    for feat in features:
        real_vals = [r[feat] for r in reals]
        fab_vals = [r[feat] for r in fabs]
        
        mean_real = np.mean(real_vals)
        mean_fab = np.mean(fab_vals)
        
        stat, p = stats.ttest_ind(real_vals, fab_vals, equal_var=False)
        flag = "LEAK SUSPECTED (p < 0.05)" if p < 0.05 else "clean"
        
        report.append(f"{feat:20} | Real Mean: {mean_real:7.2f} | Fab Mean: {mean_fab:7.2f} | t-stat: {stat:7.3f} | p-val: {p:7.5f} | status: {flag}")
    report.append("")
    
    # 3. Check categorical/substring leaks
    report.append("--- Substring Leak Analysis ---")
    for feat in ["has_contrary", "has_fabricated_rule"]:
        real_count = sum(1 for r in reals if r[feat])
        fab_count = sum(1 for r in fabs if r[feat])
        
        table = [[real_count, len(reals) - real_count], [fab_count, len(fabs) - fab_count]]
        try:
            _, p, _, _ = stats.chi2_contingency(table)
        except Exception:
            p = 1.0
            
        flag = "LEAK SUSPECTED (p < 0.05)" if p < 0.05 else "clean"
        report.append(f"{feat:20} | Real count: {real_count:3} / {len(reals)} | Fab count: {fab_count:3} / {len(fabs)} | chi2 p-val: {p:7.5f} | status: {flag}")
    report.append("")
    
    # Conclusion
    report.append("--- Summary Conclusion ---")
    suspected_leaks = []
    for feat in features:
        real_vals = [r[feat] for r in reals]
        fab_vals = [r[feat] for r in fabs]
        _, p = stats.ttest_ind(real_vals, fab_vals, equal_var=False)
        if p < 0.05:
            suspected_leaks.append(feat)
    for feat in ["has_contrary", "has_fabricated_rule"]:
        real_count = sum(1 for r in reals if r[feat])
        fab_count = sum(1 for r in fabs if r[feat])
        table = [[real_count, len(reals) - real_count], [fab_count, len(fabs) - fab_count]]
        try:
            _, p, _, _ = stats.chi2_contingency(table)
        except Exception:
            p = 1.0
        if p < 0.05:
            suspected_leaks.append(feat)
            
    if suspected_leaks:
        report.append(f"ALERT: Potential leakage patterns detected in: {', '.join(suspected_leaks)}.")
    else:
        report.append("No potential leakage patterns detected in context, citation, or source_doc fields.")
    report.append("============================================================")
    
    report_text = "\n".join(report)
    print(report_text)
    
    with open(audit_file, "w", encoding="utf-8") as f:
        f.write(report_text)
    print(f"\nAudit results successfully written to {audit_file}")

if __name__ == "__main__":
    run_field_audit()
