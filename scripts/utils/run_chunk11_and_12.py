import pandas as pd
import json
import numpy as np

# Load the dataset
df = pd.read_csv("banlegit_cite_v2_dataset.csv")

print("="*50)
print("CHUNK 11: PROGRAMMATIC QA & BALANCE AUDIT")
print("="*50)

total_count = len(df)
real_count = len(df[df["label"] == "REAL"])
fab_count = len(df[df["label"] == "FABRICATED"])

print(f"Total Dataset Size: {total_count}")
print(f"Real Count: {real_count}")
print(f"Fabricated Count: {fab_count}")

# 1. Null Value Check
nulls = df.isnull().sum()
print("\nNull Value Audit:")
print(nulls)

# 2. Uniqueness & Deduplication Check
unique_contexts = df["context"].nunique()
unique_citations = df["citation"].nunique()
print(f"\nUnique Contexts: {unique_contexts} / {total_count}")
print(f"Unique Citations: {unique_citations} / {total_count}")

# 3. Taxonomy Breakdown
print("\nTaxonomy Breakdown:")
print(df["fabrication_type"].value_counts())

print("\n" + "="*50)
print("CHUNK 12: BLIND ANNOTATION PACKAGE PREPARATION")
print("="*50)

# Create blinded copy
blind_df = df.copy()

# Shuffle deterministically using fixed random state so it's reproducible
np.random.seed(42)
blind_df = blind_df.sample(frac=1).reset_index(drop=True)

# Replace provenance IDs (STAT_REAL_1, DLR_FAB_1) with blind Task IDs (TASK_001 to TASK_150)
blind_df["task_id"] = [f"TASK_{i+1:03d}" for i in range(len(blind_df))]

# Keep original ground truth mapping separately for adjudication
ground_truth_key = blind_df[["task_id", "citation_id", "label", "fabrication_type"]].copy()
ground_truth_key.to_csv("annotation_ground_truth_key.csv", index=False)

# Strip out ground truth columns for human annotator package
annotator_package = blind_df[["task_id", "citation", "context", "extracted_url"]].copy()
annotator_package["human_verdict"] = ""  # Blank column for Shakila & Haris
annotator_package["notes"] = ""          # Blank column for notes

annotator_package.to_csv("human_annotation_package_blind_v2.csv", index=False)
annotator_package.to_json("human_annotation_package_blind_v2.json", orient="records", indent=2)

print("Saved human_annotation_package_blind_v2.csv (Blind package for Shakila & Haris)")
print("Saved annotation_ground_truth_key.csv (Secret key for adjudication)")
print("Chunk 11 & Chunk 12 Execution Complete!")
