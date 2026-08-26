# Archived Leaked Annotations (v1)

This directory contains the raw and processed annotations from the first (leaked) round of dataset collection for the BanLegit-Cite project.

## Reason for Archival

During internal audit and review, it was discovered that the task generation script (`generate_google_form.js` / `generate_form.gs`) and Label Studio import files inadvertently leaked ground-truth information to the annotators. Specifically:
- The "Verification Helper" / "helper_notes" field exposed the `Org ID` directly (e.g., `DLR_REAL_3` or `ALR_FABRICATED_7`), which explicitly encoded whether a citation was genuine or fabricated.
- The legal context descriptions of mutated citations systematically contained structural markers such as "Applying the fabricated rule from" and "contrary to the actual ruling".

Because this leakage compromised the double-blind nature of the annotation process and inflated the inter-annotator agreement metrics, all data in this directory has been **discarded in full** and archived here for transparency and scientific disclosure purposes. A new blinded re-annotation round has been prepared using a cleaned instrument (Issue 1 of the Remediation Plan).
