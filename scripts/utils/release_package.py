# release_package.py
# stage: Phase 6 — Reproducibility, Release & Reviewer Simulation
# Packages final clean dataset, runs copyright safety checks, and builds sha256 checksums.

import os
import glob
import json
import csv
import hashlib
from datetime import datetime

class ReleasePackager:
    def __init__(self, annotated_dir: str = "data/annotated", release_dir: str = "data/release"):
        self.annotated_dir = annotated_dir
        self.release_dir = release_dir
        os.makedirs(self.release_dir, exist_ok=True)

    def load_combined_data(self) -> list:
        annotated_files = glob.glob(os.path.join(self.annotated_dir, "*.json"))
        combined = []
        for fp in annotated_files:
            with open(fp, "r", encoding="utf-8") as f:
                payload = json.load(f)
            combined.extend(payload.get("data", []))
        return combined

    def check_copyright_compliance(self, items: list) -> bool:
        """Verifies that no text contains full cases (i.e. length is limited to excerpts)."""
        compliance_passed = True
        print("\nRunning copyright/licensing scan on excerpts...")
        for item in items:
            context_len = len(item.get("context", ""))
            # Flag if an excerpt is excessively long (suggesting full case text leak)
            if context_len > 1500:
                print(f"  [WARN] Large context text detected ({context_len} chars) in ID {item['citation_id']}. Verify copyright.")
                compliance_passed = False
        if compliance_passed:
            print("  [OK] No full text leaks detected. Only metadata + fair-use excerpts included.")
        return compliance_passed

    def compile_release_files(self):
        items = self.load_combined_data()
        if not items:
            print("Error: No annotated data files found to package.")
            return False

        # Run safety scan
        self.check_copyright_compliance(items)

        # Write clean unified JSON
        json_release_path = os.path.join(self.release_dir, "banlegit_cite_dataset.json")
        release_payload = {
            "metadata": {
                "produced_by": "release_package.py",
                "date": datetime.now().strftime("%Y-%m-%d"),
                "reviewed_by": "both",
                "license": "MIT",
                "version": "1.0.0"
            },
            "data": items
        }
        with open(json_release_path, "w", encoding="utf-8") as f:
            json.dump(release_payload, f, indent=2, ensure_ascii=False)
        print(f"Unified JSON dataset saved to {json_release_path}")

        # Write clean unified CSV
        csv_release_path = os.path.join(self.release_dir, "banlegit_cite_dataset.csv")
        headers = ["citation_id", "citation", "context", "source", "extracted_url", "fabrication_type", "label"]
        with open(csv_release_path, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            for item in items:
                # Only write expected schema fields
                row = {k: item.get(k, "N/A") for k in headers}
                writer.writerow(row)
        print(f"Unified CSV dataset saved to {csv_release_path}")

        # Generate sha256 checksums
        self.generate_checksum(json_release_path)
        self.generate_checksum(csv_release_path)
        return True

    def generate_checksum(self, file_path: str):
        sha256 = hashlib.sha256()
        with open(file_path, "rb") as f:
            while chunk := f.read(8192):
                sha256.update(chunk)
        digest = sha256.hexdigest()
        
        checksum_path = file_path + ".sha256"
        with open(checksum_path, "w", encoding="utf-8") as f:
            f.write(digest)
        print(f"  => Checksum: {digest[:16]}... saved to {os.path.basename(checksum_path)}")

if __name__ == "__main__":
    packager = ReleasePackager()
    packager.compile_release_files()
