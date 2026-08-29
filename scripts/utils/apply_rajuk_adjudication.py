import pandas as pd

# Load ground truth key
key_df = pd.read_csv("annotation_ground_truth_key.csv")

# Apply RAJUK Law Officer ruling on TASK_057
# TASK_057: Section 9(g) -> Should be Section 9(4)(c) for rape causing grievous hurt
idx_key = key_df[key_df["task_id"] == "TASK_057"].index
if not idx_key.empty:
    key_df.loc[idx_key, "label"] = "FABRICATED"
    key_df.loc[idx_key, "fabrication_type"] = "S3: Misstated/Inaccurate Section Reference"

# Add adjudication notes column if not present
key_df.loc[idx_key, "adjudication_notes"] = "Adjudicated FABRICATED by RAJUK Law Officer: Section 9(g) is inaccurate; Section 9(4)(c) governs rape causing grievous hurt."

# Save updated ground truth key
key_df.to_csv("annotation_ground_truth_key.csv", index=False)

print("Updated annotation_ground_truth_key.csv with RAJUK Law Officer rulings!")
print("\nUpdated Dataset Label Distribution:")
print(key_df["label"].value_counts())

