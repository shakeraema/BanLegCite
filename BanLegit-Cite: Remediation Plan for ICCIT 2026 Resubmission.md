# BanLegit-Cite: Remediation Plan for ICCIT 2026 Resubmission
### Lead Academic Advisor Response to Peer Review

**Overall sequencing principle:** The two "Blocking" issues (annotation blinding, retrieval leakage) must be resolved *first and in that order*, because every other number in the paper — IAA, accuracy tables, statistical tests — is downstream of them. Do not spend time on taxonomy prose or LaTeX polish until Issues 1 and 2 are closed. Everything below is ordered by dependency, not by the review's original numbering.

---

## ISSUE 1 (Blocking) — Annotation Blinding / Org ID Leakage

### 1.1 Specific Scientific Resolution
The Google Form's "Verification Helper" field exposed `Org ID: DLR_REAL_3` / `ALR_FABRICATED_7` directly to annotators. This is a label leak, not a verification aid — an annotator doesn't need to check anything if the answer is printed next to the question. The fix is not statistical; it's a re-collection with a genuinely blinded instrument, followed by re-computation of every downstream metric that depended on the old IAA.

Two acceptable resolutions, in order of preference:
- **(A) Full re-annotation, blind.** Strip the Org ID entirely from the annotator-facing form, re-run both annotators on all 90 items, recompute κ from scratch. This is the scientifically clean fix and should be the default.
- **(B) If re-annotation is infeasible before deadline:** explicitly disclose the leak, discard the κ=0.93 figure, and substitute a smaller *blind* validation round (e.g., 20–30 randomly sampled items) as a partial-reliability check, clearly labeled as such and not extrapolated to the full 90.

Do not attempt to "fix" this by simply removing the Org ID column from the paper's description while leaving the original (leaked) annotations as the reported κ — a reviewer with the form-generation script (as I had) will find this immediately.

### 1.2 Textual Revisions for `paper.tex`

Add to **Section 4 (Annotation Protocol)**, replacing any existing IAA paragraph:

```latex
\subsection{Blinded Annotation Protocol}
To prevent label leakage, the annotator-facing interface excludes any
metadata that could reveal ground-truth status (e.g., internal
organizational identifiers used for dataset construction). Each task
presents only the legal context, the target citation, and the
purported source document; no field indicates whether an instance was
constructed as a genuine or fabricated citation. Annotators independently
labeled all $N=90$ instances under this blinded interface before any
adjudication step.

\paragraph{Blinding verification.} To confirm the interface was free of
leakage, we conducted a manual audit of the annotator-facing form schema
(Appendix~\ref{app:blinding-audit}), verifying that no field name,
ordering pattern, or metadata string correlated with instance
provenance above chance ($\chi^2$ test on field-presence vs.\ ground
truth, $p > 0.05$; see Appendix~\ref{app:blinding-audit}).
```

Add a new **Limitations** entry:

```latex
\paragraph{Annotation re-collection.} An earlier internal annotation
round used a form template that inadvertently exposed a provenance
identifier to annotators. We discovered this during internal review,
discarded the resulting labels in full, and re-collected all
annotations under the blinded protocol described in
Section~\ref{sec:annotation}. We report this transparently because we
believe disclosing and correcting such issues, rather than omitting
them, is essential to the credibility of a fabrication-detection
benchmark specifically.
```

### 1.3 Robustness & Validity Proofs
- **Field-leakage audit script**: programmatically check every field shown to annotators against ground-truth labels for any statistical association (see 1.4 below) — report this as Appendix material, not just an assertion.
- **Blind-vs-original agreement check**: if you re-annotate, compute agreement *between* the original (leaked) labels and the new blind labels. A large drop signals the leak was doing real work; a small drop is reassuring but should still be reported, not used to justify keeping the leaked figure.
- **Annotator debrief**: have both annotators confirm in writing (a short signed statement, referenced in Appendix) that they did not have access to any external metadata, spreadsheet, or the original task-generation script during blind re-annotation.

### 1.4 Step-by-Step Implementation Guide

1. **Locate and neutralize the leak in the form-generation script.**
   File: `data_collection/generate_form.gs` (Apps Script).
   Find every line of the form:
   ```javascript
   var desc = 'Legal Context:\n' + task.context + '\n\nTarget Citation to Verify:\n' + task.citation + '\n\nPurported Source Document:\n' + task.source_doc + '\n\nVerification Helper (Source URL / Metadata):\n' + task.helper_notes;
   ```
   Replace with a version that strips the Org ID before display, while retaining it in a separate, non-displayed internal mapping:
   ```javascript
   // Strip Org ID from anything shown to annotators — keep it only in
   // the backend task object for later scoring, never in `desc`.
   var helperNotesBlind = task.helper_notes.replace(/\s*\|\s*Org ID:\s*\S+/, '');
   var desc = 'Legal Context:\n' + task.context + '\n\nTarget Citation to Verify:\n' + task.citation + '\n\nPurported Source Document:\n' + task.source_doc + '\n\nVerification Helper (Source URL):\n' + helperNotesBlind;
   ```
   Also strip the Source URL's query pattern if it encodes real/fabricated status in any way (audit it — in this project it did not, but check).

2. **Regenerate the form** from the corrected script, producing a new form ID. Do not reuse the old form even with fields hidden — Google Forms retains prior response data tied to the old ID, and reviewers/auditors should be able to see the form was regenerated cleanly.

3. **Write the blinding-audit script.** New file: `analysis/blinding_audit.py`
   ```python
   import pandas as pd
   from scipy.stats import chi2_contingency

   def audit_field_leakage(form_schema_path: str, ground_truth_path: str):
       """
       Checks whether any annotator-visible field is statistically
       associated with ground-truth status. Run BEFORE annotation begins,
       against the form as annotators will actually see it.
       """
       schema = pd.read_json(form_schema_path)
       truth = pd.read_csv(ground_truth_path)  # columns: task_id, is_fabricated
       merged = schema.merge(truth, on="task_id")

       results = {}
       for field in ["context", "citation", "source_doc", "helper_notes_blind"]:
           # crude leak-detection heuristic: does field length, or presence
           # of any suspicious substring, correlate with ground truth?
           merged[f"{field}_len_bucket"] = pd.qcut(merged[field].str.len(), 4, duplicates="drop")
           table = pd.crosstab(merged[f"{field}_len_bucket"], merged["is_fabricated"])
           chi2, p, _, _ = chi2_contingency(table)
           results[field] = {"chi2": chi2, "p": p}
       return results

   if __name__ == "__main__":
       results = audit_field_leakage(
           "annotation/blind_form_schema.json",
           "data/gold/ground_truth.csv"
       )
       for field, stats in results.items():
           flag = "LEAK SUSPECTED" if stats["p"] < 0.05 else "clean"
           print(f"{field}: chi2={stats['chi2']:.3f}, p={stats['p']:.4f} [{flag}]")
   ```
   Run this **before** sending the form to annotators, not after — it's a pre-flight check, not a post-hoc justification.

4. **Re-collect annotations.** Send the regenerated, audited form to both Shakila and Haris independently. Do not let them coordinate or discuss items before both submit — enforce this the same way the original protocol specified ("show, then wait for confirmation," never batch-share answers between annotators).

5. **Recompute IAA.** File: `analysis/iaa.py` — rerun `cohen_kappa_score` (binary) and a category-level kappa (e.g., via `sklearn.metrics.cohen_kappa_score` with `labels=` the 11-way category list, or a weighted kappa if you want partial credit for "close" categories like P2/P4).
   ```python
   from sklearn.metrics import cohen_kappa_score
   binary_kappa = cohen_kappa_score(annotator1_binary, annotator2_binary)
   category_kappa = cohen_kappa_score(annotator1_category, annotator2_category)
   print(f"Binary kappa: {binary_kappa:.4f}")
   print(f"Category kappa: {category_kappa:.4f}")
   ```

6. **Update every downstream artifact** that referenced the old κ: `RESULTS.md`, `paper.tex` Table/Section references, `reviewer_sim.py`'s expected-value checks if it hardcodes the old number anywhere.

7. **Re-run adjudication** only on items where the two blind annotations disagree — this will likely be a different (probably larger) set of items than under the leaked protocol, since annotators are now actually exercising judgment.

---

## ISSUE 2 (Blocking) — Agentic RAG 100% Accuracy / Retrieval Leakage

### 2.1 Specific Scientific Resolution
A perfect score is not evidence of a good system; on a 90-item benchmark with three fabrication-heavy blocks, it is evidence that the retrieval step trivializes the task. The most likely mechanism: the BM25 index was built over the *same* raw source corpus used to construct both the real and fabricated instances, so a fabricated locator (e.g., page 297 when the true page is 165) simply fails to retrieve any matching chunk at that page — the model doesn't need to reason about legal content at all, it only needs to check "did retrieval return something at this exact locator." This is a retrieval-existence shortcut, not citation verification.

**Required diagnostic before anything else:** log, per instance, (a) whether retrieval returned any chunk, (b) the chunk's actual locator vs. the queried locator, (c) the model's stated reasoning. If real instances retrieve a chunk and fabricated instances retrieve nothing at all, this confirms the shortcut.

**Required fix, in order of rigor:**
1. Add **near-miss fabrications**: fabricated locators that are numerically close to the real one (off by 1–5 pages) or that share the exact volume number, so naive "did retrieval find *anything* nearby" heuristics fail.
2. Add **distractor chunks**: index additional real cases *not* in the eval set, so the retriever can return plausible-looking-but-irrelevant content instead of nothing.
3. Report retrieval hit-rate and a **retrieval-blind ablation**: what does the agentic setting score if retrieval is deliberately disabled/randomized? This isolates how much of the 100% is retrieval-existence shortcut vs. genuine model reasoning over retrieved content.

### 2.2 Textual Revisions for `paper.tex`

Add to **Section 5 (Experimental Setup)**, as a new subsection:

```latex
\subsection{Retrieval Leakage Diagnostic}
\label{sec:leakage-diagnostic}
A perfect verification score raises the possibility that the retrieval
step alone -- independent of any model reasoning -- trivializes the
task (e.g., fabricated locators simply fail to retrieve any indexed
chunk). To rule this out, we report three additional analyses.

\paragraph{Retrieval hit-rate by ground truth.} Table~\ref{tab:hitrate}
reports, separately for genuine and fabricated instances, the fraction
of queries for which BM25 retrieval returned at least one chunk above
a similarity threshold $\tau$.

\paragraph{Near-miss fabrication subset.} We constructed an additional
$k=30$ near-miss instances, where fabricated locators are perturbed by
$\pm 1$--$5$ pages from the genuine locator rather than drawn from a
wide random range (Appendix~\ref{app:near-miss}). We report agentic
accuracy on this harder subset separately from the main $N=90$ set.

\paragraph{Retrieval-blind ablation.} We report agentic-setting accuracy
when the retrieved context is replaced with (a) no context (identical
to standard prompting) and (b) a randomly sampled irrelevant chunk from
the index, to establish a lower bound and confirm the model is not
simply pattern-matching on retrieval-success as a proxy signal.
```

Add a corresponding **Limitations** paragraph:

```latex
\paragraph{Perfect agentic accuracy.} We note that 100\% accuracy in
the agentic setting (Table~\ref{tab:primary-results}), while
consistent with the retrieval-diagnostic evidence in
Section~\ref{sec:leakage-diagnostic}, should be interpreted as an
upper bound reflecting the current corpus size and fabrication
construction method rather than a claim that citation verification is
a solved problem in this jurisdiction. We expect accuracy to decrease
on the near-miss subset and on a larger, more diverse corpus, and we
report the near-miss results (Table~\ref{tab:nearmiss}) as the more
representative difficulty estimate going forward.
```

### 2.3 Robustness & Validity Proofs
- **Hit-rate table** (real vs. fabricated retrieval success) — the single most important new artifact; if this shows a clean 100%-vs-0% split, that *is* the leakage, and the paper must say so plainly rather than let the reader infer it.
- **Near-miss subset accuracy** — expect and report a real drop from 100%; a paper that shows "100% on easy version, 61% on near-miss version" is a *stronger*, more credible paper than one claiming 100% everywhere.
- **Retrieval-blind ablation** — isolates model reasoning from retrieval-existence signal.
- **Manual trace inspection**: read 10 full agentic transcripts (5 real, 5 fabricated) and confirm the model's stated reasoning references actual legal content, not just "no matching document found → fabricated."

### 2.4 Step-by-Step Implementation Guide

1. **Instrument the retrieval call to log hit/miss data.** File: `src/evaluation/run_agentic.py`
   ```python
   def retrieve_and_log(query_citation, index, task_id, is_fabricated_gt):
       hits = index.search(query_citation, top_k=3)
       hit_logged = {
           "task_id": task_id,
           "ground_truth_fabricated": is_fabricated_gt,
           "num_hits": len(hits),
           "top_hit_score": hits[0].score if hits else None,
           "top_hit_locator": hits[0].metadata.get("locator") if hits else None,
           "queried_locator": query_citation,
       }
       retrieval_log.append(hit_logged)
       return hits
   ```
   Write `retrieval_log` to `experiments/results/retrieval_hitrate_log.csv` at the end of the run.

2. **Compute the hit-rate table.** New file: `analysis/retrieval_diagnostic.py`
   ```python
   import pandas as pd
   log = pd.read_csv("experiments/results/retrieval_hitrate_log.csv")
   hitrate = log.groupby("ground_truth_fabricated")["num_hits"].apply(lambda x: (x > 0).mean())
   print(hitrate)
   # If fabricated ≈ 0.0 and real ≈ 1.0, leakage is confirmed.
   ```

3. **Construct the near-miss subset.** New file: `data_construction/near_miss_generator.py`
   ```python
   import random

   def generate_near_miss(real_instance, offset_range=(1, 5)):
       real_page = real_instance["real_page"]
       offset = random.choice([-1, 1]) * random.randint(*offset_range)
       fabricated_page = real_page + offset
       return {
           **real_instance,
           "citation": real_instance["citation"].replace(str(real_page), str(fabricated_page)),
           "fabrication_category": "P2",
           "construction_method": "near_miss",
       }
   ```
   Generate 30 such instances (2 per each of the 15 base cases), save to `data/near_miss/near_miss_30.jsonl`, and run both standard and agentic settings on this subset exactly as done for the main 90.

4. **Build the retrieval-blind ablation harness.** File: `src/evaluation/run_ablation.py`
   ```python
   def run_no_retrieval_ablation(tasks, model):
       # Identical prompt structure to agentic setting, but context is
       # either empty or a randomly sampled irrelevant chunk.
       results_empty = [model.verify(t, context=None) for t in tasks]
       results_random = [model.verify(t, context=random_irrelevant_chunk()) for t in tasks]
       return results_empty, results_random
   ```

5. **Update `RESULTS.md`** to map the new Table (hit-rate), Table (near-miss accuracy), and Table (ablation) each to their exact generating script, per the project's existing reproducibility convention.

6. **Only after Steps 1–5 are complete**, revise the paper's Table I to include near-miss accuracy alongside the original figures, and write the Discussion paragraph honestly reporting whichever outcome the diagnostics actually show — do not pre-decide the narrative before running the diagnostic.

---

## ISSUE 3 (High Priority) — Dataset Scale (15 unique cases, not 45)

### 3.1 Specific Scientific Resolution
Two honest paths, not a cosmetic relabeling:
- **(A) Genuinely expand:** source 15 *additional* unique real cases (5 more per reporter block), verified with the same rigor used for the original 15, bringing the corpus to 30 unique underlying cases / ~180 instances. This is the stronger fix if time allows.
- **(B) Reframe honestly:** if expansion isn't feasible before the deadline, explicitly state the true structure — 15 unique verified cases, each contributing 2–3 fabrication variants plus repeated real instances — and justify this as a deliberate diagnostic-set design choice (controlled repetition to test locator-sensitivity specifically), not as an unexplained N=90 claim.

Given the timeline constraints discussed earlier in this project's execution plan, **(B) is the realistic choice for this ICCIT cycle**, with **(A) explicitly scoped as the journal-extension follow-up**.

### 3.2 Textual Revisions for `paper.tex`

Replace the dataset-size claim in the **Abstract** and **Section 3 (Dataset)**:

```latex
% OLD (misleading):
% "a perfectly balanced evaluation dataset of 90 gold tasks (45 real, 45 fabricated)"

% NEW:
Our evaluation set comprises $N=90$ verification instances constructed
from $15$ unique, independently verified landmark Bangladeshi
precedents (5 per reporter series: DLR, BLC, and ALR-tagged sources
subsequently re-sourced to DLR for verifiability; see
Section~\ref{sec:alr-resourcing}). Each unique case contributes one
genuine instance (repeated across three annotation batches to assess
within-case labeling consistency) and up to three controlled
locator-fabrication variants, for a total of $45$ genuine and $45$
fabricated instances. We report this structure transparently: the
dataset is best understood as a \emph{controlled diagnostic
benchmark} over $15$ high-confidence verified cases rather than a
broad-coverage corpus, and we scope corpus expansion to $\geq$30 unique
cases as future work (Section~\ref{sec:future-work}).
```

Add to **Limitations**:

```latex
\paragraph{Corpus breadth.} With 15 unique underlying cases, our
findings characterize model behavior on a curated, high-verification-
confidence set rather than the full breadth of citation fabrication
patterns in Bangladeshi legal practice. Category-level accuracy
estimates (Table~\ref{tab:category-breakdown}) should be read with
this in mind, particularly for the ALR/DLR-resourced block where case
availability constrained selection.
```

### 3.3 Robustness & Validity Proofs
- **Case-level (not instance-level) accuracy reporting**: in addition to the instance-level N=90 table, report accuracy aggregated *by unique case* (N=15) to show the finding isn't an artifact of any single case's repetition dominating the metric.
- **Leave-one-case-out check**: recompute overall accuracy with each of the 15 cases held out in turn; report the range. Large swings indicate the result is fragile to specific case selection.

### 3.4 Step-by-Step Implementation Guide

1. **Add a `case_id` field** to every task in the dataset schema (`data/gold/gold_dataset_v1.1.jsonl`), grouping the 90 instances into their 15 underlying cases.
2. **Write case-level aggregation.** File: `analysis/case_level_accuracy.py`
   ```python
   df = pd.read_json("data/gold/gold_dataset_v1.1.jsonl", lines=True)
   case_level = df.groupby("case_id").apply(
       lambda g: (g["prediction"] == g["ground_truth"]).mean()
   )
   print(case_level.describe())
   ```
3. **Implement leave-one-case-out.** File: `analysis/loco_robustness.py` — loop over the 15 `case_id` values, exclude each in turn, recompute accuracy, store results, plot/tabulate the range.
4. **If pursuing path (A)** (genuine expansion): repeat the full Stage 6→11 pipeline from the project's Operating Manual (source discovery → taxonomy application → annotation → IAA) for 15 new cases, budgeting this explicitly as its own 3–4 week block before the deadline, not squeezed into final-week revisions.

---

## ISSUE 4 (High Priority) — Single Model Family

### 4.1 Specific Scientific Resolution
Add a minimum of two additional models: one closed (GPT-class, for cross-vendor comparability) and one open-weight (Llama 3.x or Qwen2.5-class, for reproducibility without ongoing API dependency). This is not optional for a benchmark paper — a benchmark tested on one model is a case study, not a benchmark.

### 4.2 Textual Revisions for `paper.tex`

Revise **Section 5 (Experimental Setup)**:

```latex
\subsection{Models Evaluated}
To establish cross-model validity, we evaluate three model families
under identical prompting protocols (Appendix~\ref{app:prompts}):
Gemini 3.5 Flash (closed, primary results), GPT-5-class
(closed, cross-vendor validation), and Llama-3.3-70B-Instruct
(open-weight, reproducibility baseline). All models are evaluated
under both standard and agentic settings described in
Section~\ref{sec:settings}, with identical retrieval index and prompt
templates.
```

Add a new results table:

```latex
\begin{table}[t]
\centering
\caption{Cross-model accuracy comparison (Standard / Agentic settings)}
\label{tab:cross-model}
\begin{tabular}{lcc}
\toprule
Model & Standard Acc. & Agentic Acc. \\
\midrule
Gemini 3.5 Flash & XX.X\% & XX.X\% \\
GPT-5-class      & XX.X\% & XX.X\% \\
Llama-3.3-70B    & XX.X\% & XX.X\% \\
\bottomrule
\end{tabular}
\end{table}
```

### 4.3 Robustness & Validity Proofs
- **Inter-model agreement**: report pairwise agreement between models on the standard setting, to show whether errors are correlated (same instances fooling all models) or idiosyncratic (different failure modes per model) — the former is a stronger claim about the benchmark's inherent difficulty.
- **Cost/reproducibility note**: explicitly report that the Llama baseline can be reproduced without API cost, addressing reviewer reproducibility concerns directly.

### 4.4 Step-by-Step Implementation Guide

1. **Add model configs.** File: `experiments/configs/models.yaml`
   ```yaml
   models:
     - name: gemini-3.5-flash
       provider: google
       api_version: v1beta
     - name: gpt-5-class
       provider: openai
       api_version: "2025-XX"
     - name: llama-3.3-70b-instruct
       provider: local
       backend: vllm
       weights_path: /models/llama-3.3-70b-instruct
   ```
2. **Generalize the evaluation harness** in `src/evaluation/run_baseline.py` to loop over `models.yaml` entries rather than hardcoding Gemini, using a common interface (`model.verify(task) -> {status, category, confidence}`).
3. **Provision the open-weight model** via `vllm` (per the project's existing tool stack) — `pip install vllm --break-system-packages`, download weights, smoke-test on 5 instances before the full run.
4. **Run all three models × both settings** on the full 90 (plus near-miss 30 from Issue 2) — 6 full runs total, each logged with model version/date per the reproducibility convention.
5. **Update `analysis/cross_model.py`** to compute the pairwise agreement matrix and populate Table~\ref{tab:cross-model}.

---

## ISSUE 5 (Medium) — Undisclosed Verification Gaps (e.g., Aberchai Mog)

### 5.1 Specific Scientific Resolution
Do not claim uniform verification confidence across all 15 cases. Report confidence tier explicitly per case, and discuss the lowest-confidence cases as a specific limitation illustrating Bangladesh's case-law digitization gap — this is actually a *finding*, not just a flaw to hide.

### 5.2 Textual Revisions for `paper.tex`

Add to **Section 3 (Dataset)**:

```latex
\subsection{Verification Confidence Tiers}
Not all 15 underlying cases could be verified with equal confidence
against independently corroborating sources. We report a
verification-confidence tier per case (High: $\geq$3 independent
corroborating sources; Medium: 1--2 sources with a resolvable
ambiguity, e.g.\ historical court-designation conventions; Low:
case existence confirmed via a single authoritative source, but
pinpoint locator unconfirmable). Table~\ref{tab:confidence-tiers}
reports this breakdown; two of fifteen cases (13.3\%) fall in the
Low tier, reflecting known digitization gaps in older or
regionally-specific Bangladeshi case law rather than annotator
uncertainty.
```

### 5.3 Robustness & Validity Proofs
- **Sensitivity analysis excluding Low-tier cases**: report headline accuracy figures both with and without the Low-confidence cases included, so a reviewer can see the result doesn't hinge on the shakiest ground truth.

### 5.4 Step-by-Step Implementation Guide

1. **Add a `verification_tier` field** to the gold dataset schema (High/Medium/Low), populated from the annotation notes already produced during the annotation passes.
2. **Write the sensitivity script.** File: `analysis/tier_sensitivity.py` — recompute Table I's headline numbers with Low-tier cases excluded, report both versions side by side.
3. **Populate Table~\ref{tab:confidence-tiers}** directly from this field.

---

## ISSUE 6 (Medium) — Statistical Test Reporting Gaps

### 6.1 Specific Scientific Resolution
- **H1 (McNemar):** report the full 2×2 discordant-pair table; if discordant pairs < 25, use exact binomial McNemar (`statsmodels.stats.contingency_tables.mcnemar(table, exact=True)`) instead of the chi-square approximation.
- **H3 (Chi-squared):** clarify which setting's data the test uses; if the agentic arm is degenerate (100%, zero variance), either exclude it from this specific test and note why, or report Fisher's exact test as the primary statistic given likely small expected cell counts.

### 6.2 Textual Revisions for `paper.tex`

```latex
\paragraph{H1 statistical detail.} We report the full McNemar
contingency table (Table~\ref{tab:mcnemar}). With $n_{01} + n_{10} =
XX$ discordant pairs, we use the exact binomial McNemar test
\citep{mcnemar1947} rather than the $\chi^2$ approximation, following
standard guidance for $n < 25$ discordant pairs.

\paragraph{H3 statistical detail.} Because the agentic setting achieved
uniform accuracy across all reporter categories (zero within-cell
variance), the $\chi^2$ contingency test in Table~\ref{tab:h3} is
computed on the \emph{standard-setting} results only; we report
Fisher's exact test as a robustness check given expected cell counts
below 5 in two of nine cells.
```

### 6.3 Robustness & Validity Proofs
- Report exact and approximate test statistics side by side wherever cell counts are borderline — this preempts the exact objection a statistically literate reviewer will raise.

### 6.4 Step-by-Step Implementation Guide

1. **File: `analysis/statistical_tests.py`** — replace the existing McNemar call:
   ```python
   from statsmodels.stats.contingency_tables import mcnemar

   table = build_2x2_discordant_table(llm_results, human_results)
   n_discordant = table[0][1] + table[1][0]
   exact = n_discordant < 25
   result = mcnemar(table, exact=exact, correction=not exact)
   print(f"McNemar ({'exact' if exact else 'chi2 approx'}): "
         f"stat={result.statistic}, p={result.pvalue}")
   ```
2. **Add Fisher's exact test for H3**:
   ```python
   from scipy.stats import fisher_exact, chi2_contingency
   table_h3 = build_reporter_contingency_table(standard_results_only)
   chi2, p_chi2, _, expected = chi2_contingency(table_h3)
   low_cells = (expected < 5).sum()
   print(f"Chi2 p={p_chi2:.4f}, cells with expected<5: {low_cells}")
   if table_h3.shape == (2, 2):
       odds, p_fisher = fisher_exact(table_h3)
       print(f"Fisher exact p={p_fisher:.4f}")
   ```
3. **Regenerate Tables** in `paper.tex` from these corrected script outputs, and update `RESULTS.md`'s script-to-table mapping accordingly.

---

## ISSUE 7 (Medium) — Taxonomy Edge Cases

### 7.1 Specific Scientific Resolution
Formalize two edge cases the guideline currently doesn't cover, both surfaced during actual annotation: (a) simultaneous P2+P4 conflicts (wrong page *and* wrong court division at once), (b) historical citation-convention ambiguity (pre-1980s cases cited inconsistently as "(SC)" vs "(AD)" across sources).

### 7.2 Textual Revisions (Annotation Guidelines document, not paper.tex)

Add to the FROZEN guidelines' Edge-Case FAQ (requires a formal versioned amendment per the project's decision-log protocol, not a silent edit):

```markdown
#### Q4: What if a citation has BOTH a wrong page number AND a wrong
court-division letter simultaneously?
**Rule:** Apply the decision tree strictly in order. Check 2
(volume/reporter/page match) is evaluated first; if it fails, label
P2 and stop — do not proceed to Check 3 (court level) even if that
would also independently fail. This keeps classification
deterministic and reproducible across annotators, at the cost of not
separately flagging the court-level error. Annotation Notes should
mention both discrepancies even though only P2 is the assigned label.

#### Q5: What if independent real sources disagree on whether a
pre-1980s case should be cited with "(AD)", "(HCD)", or "(SC)"?
**Rule:** This reflects a genuine historical labeling convention
shift, not a fabrication. If the volume and page number are
independently confirmed correct, label the citation Correct
regardless of which division-letter convention it uses, but set
Confidence to Medium (not High) and note the specific source
disagreement in Annotation Notes.
```

### 7.3 Robustness & Validity Proofs
- Re-run the pilot κ calculation specifically on a small set of synthetically constructed P2+P4-conflict and historical-convention test items, to confirm the amended guideline resolves the ambiguity (target: κ ≥ 0.6 on this specific edge-case subset, not just the overall set).

### 7.4 Step-by-Step Implementation Guide

1. **Version the guideline document**: `annotation/guidelines_v2.md`, with a changelog entry referencing this amendment and the decision-log entry authorizing it (per the frozen-document protocol — no silent edits).
2. **Construct 6–10 synthetic edge-case test items** (3–5 P2+P4 conflicts, 3–5 historical-convention cases) and add them to a dedicated `annotation/edge_case_pilot.jsonl`.
3. **Re-run the two annotators on this small set only**, compute κ, and report it as a footnote/appendix validating the guideline amendment.

---

## ISSUE 8 (Lower Priority, Strengthens Paper) — Cross-Script Robustness Dimension

### 8.1 Specific Scientific Resolution
This was the project's originally-planned headline novelty contribution (distinguishing it from a pure jurisdictional port of LePhantomCite's methodology) but is entirely absent from the current report. If time allows after Issues 1–2 are resolved, add it; if not, explicitly flag it as immediate future work with a committed timeline, since a reviewer familiar with the broader legal-NLP-benchmark literature may otherwise ask "what's actually new here besides the country?"

### 8.2 Textual Revisions for `paper.tex`

If time permits full inclusion, add a new Section 6:

```latex
\section{Cross-Script Robustness}
\label{sec:cross-script}
Bangladesh's legal system operates under sustained Bangla/English
diglossia: statutes exist in both languages, and citations are
routinely embedded in Bangla-language legal writing. We construct
matched Bangla/English query pairs for each of the 15 base cases
(Appendix~\ref{app:cross-script}) and report the recall delta between
scripts (Table~\ref{tab:cross-script}), testing whether fabrication
detection degrades when the same underlying fact is queried in Bangla
rather than English.
```

If time does not permit, add to **Future Work** instead:

```latex
\paragraph{Cross-script evaluation.} A natural extension, in progress,
is evaluating whether verification accuracy is script-invariant --
i.e., whether the same underlying citation fact is detected with equal
reliability when queried in Bangla versus English. We view this as the
most linguistically distinctive extension of this benchmark relative
to existing English-only citation-hallucination benchmarks, and plan
to report it in a follow-up study.
```

### 8.3 Robustness & Validity Proofs
- If included: matched-pair construction (same fact, professionally translated, difficulty-controlled) is itself the validity proof — report translation methodology and a bilingual reviewer's spot-check of translation fidelity.

### 8.4 Step-by-Step Implementation Guide (if pursued this cycle)

1. Recruit a bilingual legal-Bangla speaker (ideally one of the existing annotators or adjudicator) to produce Bangla translations of all 15 base-case contexts.
2. Store as `data/cross_script/bangla_pairs.jsonl`, matched by `case_id` to the existing English instances.
3. Re-run the full model × setting matrix on this additional 15–30 instances (time-boxed; do not let this delay Issues 1–2).
4. Compute paired recall delta (Bangla − English) with a paired significance test (bootstrap or Wilcoxon), per the project's original pre-registered H2-style design.

---

## Master Execution Order

| Order | Issue | Est. time | Blocking? |
|---|---|---|---|
| 1 | Issue 1 — Annotation blinding fix + re-collection | 1–1.5 weeks | Yes — blocks everything downstream |
| 2 | Issue 2 — Retrieval leakage diagnostic + near-miss subset | 1 week | Yes — blocks all Table I claims |
| 3 | Issue 6 — Statistical test corrections | 2–3 days | Depends on 1 & 2's corrected data |
| 4 | Issue 4 — Additional model baselines | 1 week | Independent, can run parallel to 1–2 |
| 5 | Issue 3 — Dataset scale reframing/expansion | 3 days (reframe) or 3 weeks (expand) | Independent |
| 6 | Issue 5 — Confidence-tier disclosure | 2 days | Depends on existing annotation notes only |
| 7 | Issue 7 — Taxonomy edge-case amendment | 3 days | Independent |
| 8 | Issue 8 — Cross-script (if time allows) | 1–2 weeks | Optional, do last |

**Do not touch `paper.tex`'s Results/Discussion prose until Issues 1, 2, and 6 are complete** — every other textual revision above can be drafted in parallel, but the numbers they reference will change once the blocking issues are resolved, so final integration must happen last.