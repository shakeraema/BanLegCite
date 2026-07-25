import os
import glob
import json
from datetime import datetime

def format_for_label_studio(input_dir: str = "data/annotated"):
    print("=== Generating Label Studio Import Files ===")
    
    annotated_files = glob.glob(os.path.join(input_dir, "*_annotated.json"))
    tasks = []
    
    for file_path in annotated_files:
        print(f"Reading {os.path.basename(file_path)}...")
        with open(file_path, "r", encoding="utf-8") as f:
            file_data = json.load(f)
            
        data = file_data.get("data", [])
        for item in data:
            # Reformat to flat task format (no 'data' wrapper, source_doc key)
            tasks.append({
                "context": item["context"],
                "citation": item["citation"],
                "source_doc": item["source"],
                "helper_notes": f"Source URL: {item['extracted_url']} | Org ID: {item['citation_id']}"
            })
            
    # Save to both fixed and flat paths
    for output_file in ["annotation/label_studio_import_fixed.json", "annotation/label_studio_import_flat.json"]:
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(tasks, f, indent=2, ensure_ascii=False)
        print(f"Formatted and saved {len(tasks)} tasks to {output_file}")

if __name__ == "__main__":
    format_for_label_studio()
