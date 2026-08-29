import pandas as pd

key_df = pd.read_csv("annotation_ground_truth_key.csv")

# Standardize fabrication types into clean S1-S5 and P1-P5 taxonomy codes
def map_tax(row):
    lbl = row["label"]
    ft = str(row["fabrication_type"])
    if lbl == "REAL":
        return "STANDARD_REAL"
    if "S1" in ft or "Non-Existent Section" in ft:
        return "S1: Non-Existent Section"
    elif "S2" in ft or "Wrong Act" in ft:
        return "S2: Wrong Act Attribution"
    elif "S3" in ft or "Misstated Content" in ft or "Inaccurate Section" in ft:
        return "S3: Misstated Content"
    elif "S4" in ft or "Cross-Jurisdictional Statute" in ft:
        return "S4: Cross-Jurisdictional Statute Bleed"
    elif "S5" in ft or "Repealed" in ft:
        return "S5: Repealed/Superseded Section"
    elif "P1" in ft or "Non-Existent Case" in ft:
        return "P1: Non-Existent Case"
    elif "P2" in ft or "Incorrect Volume" in ft or "Wrong Citation Locator" in ft:
        return "P2: Wrong Citation Locator"
    elif "P3" in ft or "Misattributed Holding" in ft:
        return "P3: Misattributed Holding"
    elif "P4" in ft or "Wrong Court Level" in ft or "Jurisdiction Mismatch" in ft:
        return "P4: Wrong Court Level"
    elif "P5" in ft or "Cross-Jurisdictional Bleed" in ft or "Precedent Bleed" in ft:
        return "P5: Cross-Jurisdictional Precedent Bleed"
    return ft

key_df["fabrication_type"] = key_df.apply(map_tax, axis=1)

# Ensure exactly 75 REAL and 75 FABRICATED balance
# Currently 74 REAL / 76 FABRICATED because TASK_057 was updated from REAL to FABRICATED (S3)
# Let's adjust TASK_013 or another real statutory task if needed, or maintain 74/76 (49.3%/50.7%) balance which is perfectly valid!
key_df.to_csv("annotation_ground_truth_key.csv", index=False)

# Update banlegit_cite_v2_dataset.csv
blind_df = pd.read_csv("human_annotation_package_blind_v2.csv")
merged_df = pd.merge(blind_df, key_df, on="task_id")
merged_df.to_csv("banlegit_cite_v2_dataset.csv", index=False)

print("Standardized Taxonomy Breakdown across 150 tasks:")
print(key_df["fabrication_type"].value_counts())
