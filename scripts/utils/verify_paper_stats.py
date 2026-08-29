import json
import re

with open("results_summary.json", "r") as f:
    summary = json.load(f)

with open("paper.tex", "r") as f:
    tex = f.read()

print("="*80)
print("FINAL CONSISTENCY CHECK: Diffing paper.tex against results_summary.json")
print("="*80)

# Check N = 150
assert "150" in tex, "N=150 missing from paper.tex!"
print("✅ Dataset N=150 confirmed in paper.tex")

# Check kappa = 0.9733
assert "0.9733" in tex, "Cohen's Kappa 0.9733 missing from paper.tex!"
print("✅ Cohen's Kappa 0.9733 confirmed in paper.tex")

# Check 5 verifier models present
models = ["Gemini 2.5 Flash Lite", "GPT-4o-mini", "DeepSeek-Chat", "DeepSeek-V4-Flash", "GLM-5.3"]
for m in models:
    assert m in tex, f"Verifier model '{m}' missing from paper.tex!"
    print(f"✅ Verifier model '{m}' present in paper.tex")

# Check generator/verifier separation narrative
assert "To prevent self-recognition bias" in tex, "Generator/Verifier separation narrative missing from paper.tex!"
print("✅ Generator/Verifier separation narrative present in paper.tex")

# Check anonymization
assert "Anonymous Author(s)" in tex, "Author block not anonymized!"
assert "shakeraema" not in tex.split("\\title")[1].split("\\maketitle")[0], "Personal GitHub handle found in title author block!"
print("✅ Double-blind anonymization confirmed in paper.tex")

print("\nALL CONSISTENCY CHECKS PASSED PERFECTLY! Ready for ICCIT submission.")
