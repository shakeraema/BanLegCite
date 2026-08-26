import os
import re

files_to_scan = [
    "statutory_anchors.md",
    "new_dataset.md",
    "new 1-23 cases with url.md",
    "banlegit_cite_v2_dataset.csv",
    "tasks_150_v2.jsonl",
    "tasks_real_75.jsonl",
    "tasks_fabricated_75.jsonl"
]

all_urls = set()

url_pattern = re.compile(r'https?://[^\s,\"\'>\)]+')

for filepath in files_to_scan:
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            text = f.read()
            found = url_pattern.findall(text)
            for u in found:
                # Clean trailing punctuation
                cleaned = u.rstrip(".,;)")
                if cleaned:
                    all_urls.add(cleaned)

sorted_urls = sorted(list(all_urls))

# Separate PDF URLs and HTML/Web URLs
pdf_urls = [u for u in sorted_urls if u.lower().endswith(".pdf") or ".pdf" in u.lower()]
web_urls = [u for u in sorted_urls if u not in pdf_urls]

md_content = "# BanLegit-Cite Project Sources & Verification URLs\n\n"
md_content += f"Total Unique Sources Collected: **{len(sorted_urls)}**\n\n"

md_content += "## 1. Official PDF & Code Documentation Sources\n\n"
for u in pdf_urls:
    md_content += f"- [{u}]({u})\n"

md_content += "\n## 2. Primary Law & Case Verification Web Sources\n\n"
for u in web_urls:
    md_content += f"- [{u}]({u})\n"

output_file = "sources.md"
with open(output_file, "w", encoding="utf-8") as f:
    f.write(md_content)

print(f"Extracted {len(sorted_urls)} unique URLs ({len(pdf_urls)} PDFs) into {output_file}!")
