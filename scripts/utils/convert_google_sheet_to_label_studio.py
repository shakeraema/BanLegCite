import csv
import json
import argparse
import sys

def convert_csv_to_label_studio(csv_path, original_json_path, output_json_path):
    # Load original tasks to get contexts, citations, source docs, and helper notes
    with open(original_json_path, "r", encoding="utf-8") as f:
        original_tasks = json.load(f)
    
    # Read the CSV file containing Google Form responses
    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        responses = list(reader)
        
    if len(responses) < 2:
        print(f"Error: Google Form responses CSV must contain at least 2 responses (found {len(responses)}).")
        sys.exit(1)
        
    # We expect each row in CSV to represent one annotator's responses for all tasks.
    # Group responses by Student Name
    annotators = list(set(r.get("Student Name", "").strip() for r in responses if r.get("Student Name")))
    
    if len(annotators) < 2:
        print(f"Error: Could not find at least 2 distinct annotator names in CSV. Found: {annotators}")
        sys.exit(1)
        
    print(f"Processing annotations for: {annotators[:2]}")
    
    # Map the first two annotators
    ann1_name = annotators[0]
    ann2_name = annotators[1]
    
    ann1_row = next(r for r in responses if r.get("Student Name", "").strip() == ann1_name)
    ann2_row = next(r for r in responses if r.get("Student Name", "").strip() == ann2_name)
    
    converted_tasks = []
    
    for idx, orig_task in enumerate(original_tasks):
        task_num = idx + 1
        
        # Build annotations array in Label Studio structure
        annotations = []
        
        for name, row, completed_by in [(ann1_name, ann1_row, 1), (ann2_name, ann2_row, 2)]:
            # Construct keys as defined in generate_google_form.js
            status_key = f"Task {task_num} - Step 1: Verification Status"
            category_key = f"Task {task_num} - Step 2: Citation Fabrication Category"
            confidence_key = f"Task {task_num} - Step 3: Confidence Level"
            notes_key = f"Task {task_num} - Step 4: Annotation Notes"
            
            status_val = row.get(status_key, "Correct")
            category_val = row.get(category_key, "Correct")
            confidence_val = row.get(confidence_key, "Low")
            notes_val = row.get(notes_key, "")
            
            # Clean category value (remove helper text if it's the "Not Applicable" choice)
            if "Not Applicable" in category_val or status_val == "Correct":
                category_val = "Correct"
            
            # Construct the result format expected by calculate_iaa.py
            results = [
                {
                    "from_name": "status",
                    "to_name": "text_context",
                    "type": "choices",
                    "value": {"choices": [status_val]}
                },
                {
                    "from_name": "fabrication_category",
                    "to_name": "text_context",
                    "type": "choices",
                    "value": {"choices": [category_val]}
                },
                {
                    "from_name": "confidence",
                    "to_name": "text_context",
                    "type": "choices",
                    "value": {"choices": [confidence_val]}
                }
            ]
            
            annotations.append({
                "completed_by": completed_by,
                "student_name": name,
                "result": results
            })
            
        converted_tasks.append({
            "id": idx + 1,
            "data": {
                "context": orig_task.get("context", ""),
                "citation": orig_task.get("citation", ""),
                "source": orig_task.get("source_doc", ""),
                "helper_notes": orig_task.get("helper_notes", "")
            },
            "annotations": annotations
        })
        
    with open(output_json_path, "w", encoding="utf-8") as f:
        json.dump(converted_tasks, f, indent=2)
        
    print(f"Successfully converted CSV to Label Studio JSON format: {output_json_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert Google Form Responses CSV to Label Studio JSON format.")
    parser.add_argument("--csv", required=True, help="Path to the Google Form responses CSV.")
    parser.add_argument("--original", default="annotation/label_studio_import_fixed.json", help="Path to the original tasks JSON.")
    parser.add_argument("--output", default="annotation/project_export.json", help="Output path for the parsed JSON.")
    
    args = parser.parse_args()
    convert_csv_to_label_studio(args.csv, args.original, args.output)
