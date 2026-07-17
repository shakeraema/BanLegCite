import os
import json
import argparse
from datetime import datetime

def calculate_cohen_kappa(annotator1, annotator2):
    """Calculates Cohen's Kappa for two list of labels."""
    if len(annotator1) != len(annotator2):
        raise ValueError("Label lists must have the same length.")
        
    n = len(annotator1)
    if n == 0:
        return 0.0, 0.0
        
    categories = list(set(annotator1 + annotator2))
    cat_to_idx = {cat: idx for idx, cat in enumerate(categories)}
    num_cats = len(categories)
    
    conf_matrix = [[0] * num_cats for _ in range(num_cats)]
    for a1, a2 in zip(annotator1, annotator2):
        conf_matrix[cat_to_idx[a1]][cat_to_idx[a2]] += 1
        
    observed_agreement = sum(conf_matrix[i][i] for i in range(num_cats)) / n
    
    sum_rows = [sum(conf_matrix[i]) for i in range(num_cats)]
    sum_cols = [sum(conf_matrix[j][i] for j in range(num_cats)) for i in range(num_cats)]
    
    chance_agreement = sum((r * c) for r, c in zip(sum_rows, sum_cols)) / (n * n)
    
    if chance_agreement == 1.0:
        return 1.0, 1.0
        
    kappa = (observed_agreement - chance_agreement) / (1.0 - chance_agreement)
    return kappa, observed_agreement

def parse_label_studio_export(export_path: str):
    """Parses Label Studio JSON export to extract labels for two annotators."""
    with open(export_path, "r", encoding="utf-8") as f:
        tasks = json.load(f)
        
    binary_a1, binary_a2 = [], []
    cat_a1, cat_a2 = [], []
    disagreements = []
    
    for task in tasks:
        context = task["data"]["context"]
        citation = task["data"]["citation"]
        source = task["data"]["source"]
        helper_notes = task["data"].get("helper_notes", "")
        
        annotations = task.get("annotations", [])
        if len(annotations) < 2:
            # Skip tasks that don't have at least two annotations yet
            continue
            
        # Sort annotations by completed_by or ID to keep consistent roles
        annotations = sorted(annotations, key=lambda x: x.get("completed_by", 0))
        ann1, ann2 = annotations[0], annotations[1]
        
        def extract_labels(ann):
            status = "Correct"
            category = "Correct"
            
            for result in ann.get("result", []):
                from_name = result.get("from_name")
                value = result.get("value", {})
                choices = value.get("choices", [])
                
                if not choices:
                    continue
                    
                if from_name == "status":
                    status = choices[0]
                elif from_name == "fabrication_category":
                    category = choices[0]
                    
            if status == "Correct":
                category = "Correct"
                
            return status, category
            
        status1, cat1 = extract_labels(ann1)
        status2, cat2 = extract_labels(ann2)
        
        binary_a1.append(status1)
        binary_a2.append(status2)
        
        cat_a1.append(cat1)
        cat_a2.append(cat2)
        
        # Log disagreements
        if status1 != status2 or cat1 != cat2:
            disagreements.append({
                "citation": citation,
                "context": context,
                "source": source,
                "helper_notes": helper_notes,
                "ann1_user": ann1.get("completed_by", "User 1"),
                "ann1_status": status1,
                "ann1_category": cat1,
                "ann2_user": ann2.get("completed_by", "User 2"),
                "ann2_status": status2,
                "ann2_category": cat2
            })
            
    return binary_a1, binary_a2, cat_a1, cat_a2, disagreements

def main():
    parser = argparse.ArgumentParser(description="Calculate Cohen's Kappa score on Label Studio double-annotated export.")
    parser.add_argument("--export", type=str, default="annotation/project_export.json",
                        help="Path to Label Studio JSON export file")
    args = parser.parse_args()
    
    if not os.path.exists(args.export):
        print(f"Error: Label Studio export file not found at: {args.export}")
        print("Please export your annotations in JSON format from Label Studio and save them there.")
        return
        
    try:
        bin_a1, bin_a2, cat_a1, cat_a2, disagreements = parse_label_studio_export(args.export)
        
        if not bin_a1:
            print("No tasks found with at least two annotations to evaluate.")
            return
            
        binary_kappa, binary_obs = calculate_cohen_kappa(bin_a1, bin_a2)
        cat_kappa, cat_obs = calculate_cohen_kappa(cat_a1, cat_a2)
        
        print("\n" + "="*50)
        print("  Inter-Annotator Agreement (IAA) Report")
        print("="*50)
        print(f"Total Double-Annotated Tasks: {len(bin_a1)}")
        print(f"Disagreements Found: {len(disagreements)}")
        print("\n1. Binary Verification Status (Correct vs Fabricated):")
        print(f"   Observed Agreement: {binary_obs:.2%}")
        print(f"   Cohen's Kappa (κ): {binary_kappa:.4f}")
        print("\n2. Detailed Fabrication Categories (11-class):")
        print(f"   Observed Agreement: {cat_obs:.2%}")
        print(f"   Cohen's Kappa (κ): {cat_kappa:.4f}")
        print("="*50 + "\n")
        
        # Write adjudication sheet
        report_path = "logs/adjudication_sheet.md"
        report = []
        report.append("# Adjudication Sheet & Disagreement Log")
        report.append(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append(f"Total Double-Annotated Tasks: {len(bin_a1)}")
        report.append(f"Disagreements: {len(disagreements)}")
        report.append(f"Overall Binary Kappa: {binary_kappa:.4f} | Category Kappa: {cat_kappa:.4f}\n")
        report.append("---")
        report.append("\n## Disagreement Records for Adjudicator Review\n")
        
        for idx, item in enumerate(disagreements):
            report.append(f"### {idx+1}. Citation: `{item['citation']}`")
            report.append(f"- **Source:** {item['source']}")
            report.append(f"- **Context:** {item['context']}")
            report.append(f"- **Metadata:** {item['helper_notes']}")
            report.append(f"- **Annotator 1 ({item['ann1_user']}):** Status: `{item['ann1_status']}` | Category: `{item['ann1_category']}`")
            report.append(f"- **Annotator 2 ({item['ann2_user']}):** Status: `{item['ann2_status']}` | Category: `{item['ann2_category']}`")
            report.append("- **Adjudicator Verdict:** [ ] Annotator 1  [ ] Annotator 2  [ ] Other")
            report.append("- **Adjudicated Category:** ")
            report.append("- **Adjudicator Reasoning:** \n")
            report.append("---")
            
        with open(report_path, "w", encoding="utf-8") as f:
            f.write("\n".join(report))
            
        print(f"Adjudication sheet saved to: {report_path}")
        
    except Exception as e:
        print(f"Failed calculating agreement: {e}")

if __name__ == "__main__":
    main()
