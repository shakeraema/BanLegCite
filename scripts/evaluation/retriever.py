# retriever.py
# stage: Phase 3 Shadow Work — Evaluation Harness

import os
import json
import glob

class LocalRetriever:
    def __init__(self, raw_data_dir: str = "data/raw"):
        self.raw_data_dir = raw_data_dir
        self.index = {}
        self.build_index()

    def build_index(self):
        """Constructs a basic map from citation strings to case metadata and holdings."""
        raw_files = glob.glob(os.path.join(self.raw_data_dir, "*.json"))
        for file_path in raw_files:
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = json.load(f)
                data = content.get("data", [])
                for item in data:
                    citation_key = item["citation"].strip().lower()
                    self.index[citation_key] = {
                        "citation": item["citation"],
                        "context": item["context"],
                        "source": item["source"],
                        "url": item["extracted_url"]
                    }
            except Exception as e:
                print(f"Failed to index file {file_path}: {e}")

    def retrieve(self, citation: str) -> str:
        """Looks up the citation in the index and returns verified holding text."""
        citation_key = citation.strip().lower()
        
        # Exact match check
        if citation_key in self.index:
            entry = self.index[citation_key]
            return f"Verified Citation: {entry['citation']}\nSource: {entry['source']}\nSummary: {entry['context']}\nVerification Link: {entry['url']}"
            
        # Partial match / fuzzy check
        for key, entry in self.index.items():
            if key in citation_key or citation_key in key:
                return f"Verified Citation Match: {entry['citation']}\nSource: {entry['source']}\nSummary: {entry['context']}\nVerification Link: {entry['url']}"
                
        return f"No matching verified citation found in registry for: {citation}"
