import pandas as pd
import json

def audit():
    print("=== RUNNING PROGRAMMATIC DATASET AUDIT ===")
    
    # 1. Dataset Balance
    df_dataset = pd.read_csv("data/release/banlegit_cite_dataset.csv")
    total_rows = len(df_dataset)
    labels = df_dataset["label"].value_counts()
    
    print(f"Total Rows: {total_rows}")
    print("Labels counts:")
    print(labels)
    
    # Count by reporter series
    # Extract reporter series from citation_id (DLR, BLC, ALR)
    df_dataset["reporter"] = df_dataset["citation_id"].apply(lambda x: x.split("_")[0])
    balance_by_rep = df_dataset.groupby(["reporter", "label"]).size().unstack(fill_value=0)
    print("\nReporter Balance:")
    print(balance_by_rep)
    
    # 2. Annotators' verdicts
    df_responses = pd.read_csv("data/annotation_raw/blind_round_2/project_responses.csv")
    
    # Check annotator names
    names = df_responses["Student Name"].tolist()
    print(f"\nAnnotators found: {names}")
    
    # Let's count agreement on Verification Status
    a1_row = df_responses.iloc[0]
    a2_row = df_responses.iloc[1]
    
    status_agreements = 0
    cat_agreements = 0
    status_disagreements = []
    cat_disagreements = []
    
    for i in range(1, 91):
        status_col = f"Task {i} - Step 1: Verification Status"
        cat_col = f"Task {i} - Step 2: Citation Fabrication Category"
        
        s1 = a1_row[status_col]
        s2 = a2_row[status_col]
        
        c1 = a1_row[cat_col]
        c2 = a2_row[cat_col]
        
        # Clean categories
        if "Not Applicable" in str(c1):
            c1 = "Correct"
        if "Not Applicable" in str(c2):
            c2 = "Correct"
            
        if s1 == s2:
            status_agreements += 1
        else:
            status_disagreements.append((i, s1, s2))
            
        if c1 == c2:
            cat_agreements += 1
        else:
            cat_disagreements.append((i, c1, c2))
            
    print(f"\nStatus Agreement: {status_agreements}/90 ({status_agreements/90:.2%})")
    print(f"Category Agreement: {cat_agreements}/90 ({cat_agreements/90:.2%})")
    
    if status_disagreements:
        print(f"Status Disagreements: {status_disagreements}")
    else:
        print("No status disagreements between annotators.")
        
    if cat_disagreements:
        print(f"Category Disagreements: {cat_disagreements}")
    else:
        print("No category disagreements between annotators.")

if __name__ == "__main__":
    audit()
