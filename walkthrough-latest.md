# Walkthrough: BanLegit-Cite v2.0 Dataset Rebuild Complete! 🎉

## Dataset Summary ($N = 150$)

We have officially constructed and verified the complete **BanLegit-Cite v2.0 Dataset**, perfectly adhering to all academic specifications for ICCIT 2026!

| Metric | Target | Actual Result | Status |
| :--- | :--- | :--- | :--- |
| **Total Benchmark Size ($N$)** | 150 tasks | **150 tasks** | ✅ Completed |
| **Real : Fabricated Ratio** | 1:1 (75 / 75) | **75 Real / 75 Fabricated** | ✅ Completed |
| **Statute : Precedent Split** | ~1:1 Split | **37 Statutory / 38 Precedent** | ✅ Completed |
| **Verification URLs** | 100% verified | **100% backed by primary sources/URLs** | ✅ Completed |
| **2026 Statutory Amendments** | Included | **10 sections from 2026 Nari O Shishu Act** | ✅ Completed |
| **10-Class Taxonomy** | S1–S5, P1–P5 | **Balanced across all 10 mutation types** | ✅ Completed |

---

## Output Files Created

1. [`tasks_real_75.jsonl`](file:///Users/shakera/Downloads/Study/Researches/ICCIT/BanLegit-Cite/tasks_real_75.jsonl)
   * Contains the 75 verified real tasks (38 judicial precedents + 37 statutory provisions).
2. [`tasks_fabricated_75.jsonl`](file:///Users/shakera/Downloads/Study/Researches/ICCIT/BanLegit-Cite/tasks_fabricated_75.jsonl)
   * Contains the 75 fabricated tasks (45 from Gemini + 30 from GLM 5.2).
3. [`tasks_150_v2.jsonl`](file:///Users/shakera/Downloads/Study/Researches/ICCIT/BanLegit-Cite/tasks_150_v2.jsonl)
   * The complete, unified machine-readable JSONL dataset.
4. [`banlegit_cite_v2_dataset.csv`](file:///Users/shakera/Downloads/Study/Researches/ICCIT/BanLegit-Cite/banlegit_cite_v2_dataset.csv)
   * CSV format ready for model evaluation runs and human annotation export.

---

## Next Steps
We are now ready for **Chunk 12**: Preparing the Double-Blind Human Annotation Package for Shakila and Haris to compute Cohen's Kappa ($\kappa$)!
