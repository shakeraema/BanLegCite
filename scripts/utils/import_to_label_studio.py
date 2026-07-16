import os
import glob
import json
from datetime import datetime

def format_for_label_studio(input_dir: str = "data/annotated", output_file: str = "annotation/label_studio_import.json"):
    print("=== Generating Label Studio Import File ===")
    
    annotated_files = glob.glob(os.path.join(input_dir, "*_annotated.json"))
    tasks = []
    
    for file_path in annotated_files:
        print(f"Reading {os.path.basename(file_path)}...")
        with open(file_path, "r", encoding="utf-8") as f:
            file_data = json.load(f)
            
        data = file_data.get("data", [])
        for item in data:
            # Reformat to Label Studio import task format
            tasks.append({
                "data": {
                    "context": item["context"],
                    "citation": item["citation"],
                    "source": item["source"],
                    "helper_notes": f"Source URL: {item['extracted_url']} | Org ID: {item['citation_id']}"
                }
            })
            
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2, ensure_ascii=False)
        
    print(f"Formatted and saved {len(tasks)} tasks to {output_file}")
    print("You can now import this file directly into your Label Studio project.")

if __name__ == "__main__":
    format_for_label_studio()
