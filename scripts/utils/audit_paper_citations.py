import re

with open("paper.tex", "r", encoding="utf-8") as f:
    tex_text = f.read()

# Extract all cite keys
cite_keys = set(re.findall(r'\\cite\{([^}]+)\}', tex_text))
# Handle comma-separated citations if any
all_cites = set()
for c in cite_keys:
    for k in c.split(','):
        all_cites.add(k.strip())

# Extract all bibitem keys
bibitem_keys = set(re.findall(r'\\bibitem\{([^}]+)\}', tex_text))

print("="*60)
print("PAPER CITATION AUDIT REPORT")
print("="*60)

print(f"Total Unique Cited Keys in Text: {len(all_cites)}")
print(f"Total Unique Bibitem Keys in Bibliography: {len(bibitem_keys)}")

missing_in_bib = all_cites - bibitem_keys
uncited_in_text = bibitem_keys - all_cites

if not missing_in_bib and not uncited_in_text:
    print("\n✅ PERFECT MATCH! All cited keys have corresponding bibliography entries, and all bibliography entries are cited in text.")
else:
    if missing_in_bib:
        print(f"\n❌ Missing in Bibliography: {missing_in_bib}")
    if uncited_in_text:
        print(f"\n⚠️ Uncited in Text: {uncited_in_text}")

print("\nDetail Breakdown of Bibliography Keys:")
for key in sorted(list(bibitem_keys)):
    is_cited = "CITED" if key in all_cites else "UNCITED"
    print(f"- {key}: {is_cited}")
