import os
import json
import numpy as np
from sklearn.metrics import cohen_kappa_score

def extract_labels_from_export(export_path):
    with open(export_path, "r", encoding="utf-8") as f:
        tasks = json.load(f)
        
    binary_labels = []
    category_labels = []
    
    # We will extract labels for Annotator 1 and Annotator 2
    a1_binary, a2_binary = [], []
    a1_category, a2_category = [], []
    
    for task in tasks:
        annotations = task.get("annotations", [])
        if len(annotations) < 2:
            continue
        # Sort annotations by completed_by to ensure consistent order
        annotations = sorted(annotations, key=lambda x: x.get("completed_by", 0))
        ann1, ann2 = annotations[0], annotations[1]
        
        def get_status_and_cat(ann):
            status = "Correct"
            category = "Correct"
            for result in ann.get("result", []):
                from_name = result.get("from_name")
                value = result.get("value", {})
                choices = value.get("choices", [])
                if choices:
                    if from_name == "status":
                        status = choices[0]
                    elif from_name == "fabrication_category":
                        category = choices[0]
            if status == "Correct":
                category = "Correct"
            return status, category
            
        s1, c1 = get_status_and_cat(ann1)
        s2, c2 = get_status_and_cat(ann2)
        
        a1_binary.append(s1)
        a2_binary.append(s2)
        a1_category.append(c1)
        a2_category.append(c2)
        
    return a1_binary, a2_binary, a1_category, a2_category

def run_iaa_analysis():
    old_export = "data/archive/leaked_annotations_v1/project_export.json"
    new_export = "data/annotation_raw/blind_round_2/project_export.json"
    
    # Parse labels
    old_a1_bin, old_a2_bin, old_a1_cat, old_a2_cat = extract_labels_from_export(old_export)
    new_a1_bin, new_a2_bin, new_a1_cat, new_a2_cat = extract_labels_from_export(new_export)
    
    # Compute Kappas
    old_bin_kappa = cohen_kappa_score(old_a1_bin, old_a2_bin)
    old_cat_kappa = cohen_kappa_score(old_a1_cat, old_a2_cat)
    
    new_bin_kappa = cohen_kappa_score(new_a1_bin, new_a2_bin)
    new_cat_kappa = cohen_kappa_score(new_a1_cat, new_a2_cat)
    
    # Compute agreement between old and new labels (to see if stripping Org ID changed decisions)
    # Since the annotator identity might have changed (from Maksudul to Haris), we check Shakila (A1) specifically
    # and also check the cross-round overall label stability.
    a1_bin_agreement = np.mean([o == n for o, n in zip(old_a1_bin, new_a1_bin)])
    a1_cat_agreement = np.mean([o == n for o, n in zip(old_a1_cat, new_a1_cat)])
    
    a2_bin_agreement = np.mean([o == n for o, n in zip(old_a2_bin, new_a2_bin)])
    a2_cat_agreement = np.mean([o == n for o, n in zip(old_a2_cat, new_a2_cat)])
    
    os.makedirs("diagnostic_output", exist_ok=True)
    report_file = "diagnostic_output/issue1_leaked_vs_blind_agreement.txt"
    
    report = []
    report.append("============================================================")
    report.append("  BanLegit-Cite Inter-Annotator Agreement (IAA) Comparison")
    report.append("============================================================")
    report.append(f"Old Leaked Binary Kappa:   {old_bin_kappa:.4f}")
    report.append(f"Old Leaked Category Kappa: {old_cat_kappa:.4f}")
    report.append("")
    report.append(f"New Blinded Binary Kappa:   {new_bin_kappa:.4f}")
    report.append(f"New Blinded Category Kappa: {new_cat_kappa:.4f}")
    report.append("")
    report.append("--- Agreement Between Leaked and Blind Labels ---")
    report.append(f"Annotator 1 (Shakila) Binary Agreement:   {a1_bin_agreement:.2%}")
    report.append(f"Annotator 1 (Shakila) Category Agreement: {a1_cat_agreement:.2%}")
    report.append(f"Annotator 2 (Maksudul vs Haris) Binary Agreement:   {a2_bin_agreement:.2%}")
    report.append(f"Annotator 2 (Maksudul vs Haris) Category Agreement: {a2_cat_agreement:.2%}")
    report.append("")
    
    # Find list of changes in Shakila's labels
    changes = []
    for i in range(len(old_a1_bin)):
        if old_a1_bin[i] != new_a1_bin[i] or old_a1_cat[i] != new_a1_cat[i]:
            changes.append(f"Task {i+1}: Old ({old_a1_bin[i]}, {old_a1_cat[i]}) -> New ({new_a1_bin[i]}, {new_a1_cat[i]})")
            
    if changes:
        report.append("--- Changes in Annotator 1 (Shakila) Labels ---")
        report.extend(changes)
    else:
        report.append("No changes in Annotator 1's labels between leaked and blind rounds.")
    report.append("============================================================")
    
    report_text = "\n".join(report)
    print(report_text)
    
    with open(report_file, "w", encoding="utf-8") as f:
        f.write(report_text + "\n")
        
if __name__ == "__main__":
    run_iaa_analysis()
