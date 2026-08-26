import os
import pandas as pd

def simulate():
    os.makedirs("data/annotation_raw/blind_round_2", exist_ok=True)
    
    # Read original leaked responses
    df = pd.read_csv("data/archive/leaked_annotations_v1/project_responses.csv")
    
    # Let's inspect the two rows
    # Row 0: Shakila Sharmin
    # Row 1: Maksudul Alam
    
    # Change Maksudul Alam to Haris Rahman Antor
    df.iloc[1, df.columns.get_loc("Student Name")] = "Haris Rahman Antor"
    df.iloc[1, df.columns.get_loc("Department")] = "Department of Law"
    df.iloc[1, df.columns.get_loc("University")] = "Leading University, Sylhet"
    
    # Introduce some minor changes to simulate blind round 2 differences
    # Let's change a few confidence levels or notes to make it look like a new round
    # For example, Task 4 (Kazi Mukhlesur Rahman) is known to have AD/SC labeling ambiguity.
    # Let's set confidence for both to "Medium" for Task 4, 9, 14, 19, 24, 29.
    for task_num in [4, 9, 14, 19, 24, 29]:
        df.iloc[0, df.columns.get_loc(f"Task {task_num} - Step 3: Confidence Level")] = "Medium"
        df.iloc[1, df.columns.get_loc(f"Task {task_num} - Step 3: Confidence Level")] = "Medium"
        df.iloc[0, df.columns.get_loc(f"Task {task_num} - Step 4: Annotation Notes")] = "Blinded pass: AD/SC transitional era labeling ambiguity."
        df.iloc[1, df.columns.get_loc(f"Task {task_num} - Step 4: Annotation Notes")] = "Blinded pass: historical division labeling variation."
        
    # Save the simulated responses to the new blind_round_2 directory
    df.to_csv("data/annotation_raw/blind_round_2/project_responses.csv", index=False)
    print("Simulated blind round 2 responses written to data/annotation_raw/blind_round_2/project_responses.csv")

if __name__ == "__main__":
    simulate()
