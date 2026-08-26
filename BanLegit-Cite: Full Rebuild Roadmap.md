# BanLegit-Cite: Full Rebuild Roadmap
### Rebuild, not patch — see decision rationale in chat. Chunk 1 and Chunk 2 are completed; remaining chunks are planned.

**Rule for every chunk:** no case, citation, holding, or locator is used unless it is independently confirmed against a real source or explicitly tagged `NEEDS VERIFICATION`. No chunk after this one modifies any task — this document only plans the order of work.

---

## CHUNK 1 — Full Audit & Triage of the Existing 90 Tasks [COMPLETED]

- **Objective:** Produce a definitive, row-by-row inventory of the current dataset: what's verified, what's fabricated-on-purpose, what's unannotated, what's mismatched between annotation and release, what's simply wrong.
- **What was changed:** Generated row-by-row triage in `Chunk 1 audit inventory of all 90 existing BanLegit-Cite tasks.md`.
- **Files/tasks involved:** Reconciled `banlegit_cite_dataset.csv`, `project_responses.csv`, `adjudication_sheet.md`, and `senior_review.md`.
- **Expected output:** Complete audit inventory log.

---

## CHUNK 2 — Target Dataset Structure & Taxonomy Coverage Matrix [COMPLETED]

- **Objective:** Decide the rebuilt dataset's shape before sourcing any new content: target N, real/fabricated balance, statutory/precedent split, per-category minimums for all 10 taxonomy codes (S1–S5, P1–P5).
- **What was changed:** Locked N = 150 unique tasks (Option B) in `dataset_spec.md`.
- **Files/tasks involved:** Created `dataset_spec.md` defining: N = 150, 1:1 real/fabricated split, 1:1 statutory/precedent split, strictly no verbatim duplicates, and ~7–8 instances per taxonomy category.

---

## CHUNK 3 — Statutory Scope Decision (Which Acts, Which Sections)

- **Objective:** Decide definitively whether Nari O Shishu Nirjatan Daman Ain 2000 is included, and lock the full statutory scope (Acts + specific sections) with sourcing plan.
- **What will be changed:** No tasks — this produces the statutory sourcing target list.
- **Files/tasks involved:** New `statutory_scope.md`. Cross-referenced directly against `bdlaws.minlaw.gov.bd` Act pages for each candidate Act.
- **Verification needed:** Confirm current section numbering for each Act directly on bdlaws.minlaw.gov.bd (numbering has shifted historically via amendment — must use the live consolidated text, not memory).
- **Expected output:** Locked Act list with specific sections earmarked for S1 (non-existent section — requires picking a section number just past the Act's actual last section), S2 (wrong Act — requires two Acts with genuinely confusable section-number overlaps), S3 (misstated content — requires a section whose real content is unambiguous and checkable), S4 (cross-jurisdictional — requires a genuine Indian/Pakistani-only provision, e.g. IPC 498A, with confirmation it was never adopted in BD law), S5 (repealed — requires a genuinely repealed/superseded provision with a confirmable repeal date).
- **Dependencies:** Chunk 2 (need the statutory:precedent ratio target first).

---

## CHUNK 4 — Precedent Candidate Shortlist Across Legal Domains

- **Objective:** Build a broad candidate list of landmark, frequently-cited, publicly-verifiable Bangladeshi cases, spread across distinct legal domains, before doing deep verification on any single one.
- **What will be changed:** No tasks — this is a sourcing candidate list, over-generated so weak candidates can be dropped later without shrinking the pool below target.
- **Files/tasks involved:** New `case_candidate_list.md`, organized by domain: constitutional law, criminal law/sentencing, anti-corruption, environmental/PIL, labor/industrial safety, women's rights/family law, administrative law, media/regulatory law, juvenile justice, land/Adivasi rights. Aim for 3–5 candidates per domain, over-generating ~50–60 candidates against a target of exactly 38 unique precedent cases.
- **Verification needed:** None yet at this stage — candidate generation only, verification happens in Chunk 5.
- **Expected output:** A domain-balanced long-list, explicitly avoiding the earlier dataset's heavy skew toward constitutional/BLAST-adjacent cases.
- **Dependencies:** Chunk 2 (need the target unique-case count of 38 to know how large a long-list to generate).

---

## CHUNK 5 — Source Verification Pass on the Candidate List

- **Objective:** Independently verify each candidate case's citation (case name, reporter, volume, page, court level, actual holding) against real sources.
- **What will be changed:** No tasks — this produces the verification status per candidate.
- **Files/tasks involved:** `case_candidate_list.md` → annotated with verification status. Primary sources checked in this order: `supremecourt.gov.bd` case search, `bdpil.org` (Bangladesh Public Interest Litigation resource — particularly valuable for the environmental/PIL domain), `clcbd.org` (Chancery Law Chronicles), cross-checked against independent academic/legal-commentary sources the way earlier verification in this project was done (never relying on a single source).
- **Verification needed:** This chunk *is* the verification step. Every candidate gets one of: `VERIFIED` (locator + holding independently confirmed by ≥2 sources), `PARTIALLY VERIFIED` (case confirmed real, locator or holding detail uncertain), `NEEDS VERIFICATION` (insufficient evidence either way — dropped from the pool, not force-fit), `REJECTED` (evidence contradicts the candidate, e.g. wrong court level or non-existent).
- **Expected output:** A filtered, evidence-tagged case pool ready for final selection.
- **Dependencies:** Chunk 4.

---

## CHUNK 6 — Finalize the Verified Case & Statute Pool

- **Objective:** Lock the final list of real, verified anchors — both statutory sections and precedent cases — that the whole dataset will be built from. No more sourcing after this point.
- **What will be changed:** No tasks yet — this is the frozen "ground truth anchor list."
- **Files/tasks involved:** New `verified_anchor_pool.csv` — one row per anchor, with case/section name, citation, court level, holding summary, source citations (URLs/document references), verification tier (per Chunk 5's tags).
- **Verification needed:** Final cross-check that the pool meets Chunk 2's structural targets (exactly 75 final real anchors: 37 statutory and 38 precedent, no duplicates).
- **Expected output:** A frozen, versioned anchor list of 75 anchors — this is the single source of truth for everything downstream.
- **Dependencies:** Chunks 3 and 5 (needs both the statutory scope and the verified precedent pool).

---

## CHUNK 7 — Construct Real Statutory Task Instances

- **Objective:** Turn the statutory anchors from Chunk 6 into actual dataset task rows (context text + citation, all genuinely correct).
- **What will be changed:** New task rows created (not yet fabricated variants — real instances only).
- **Files/tasks involved:** New `tasks_statutory_real.jsonl`.
- **Verification needed:** Each generated context sentence must be checked against the actual Act text on bdlaws.minlaw.gov.bd to confirm the description of the section's content is accurate — this is where S3-adjacent errors could accidentally get introduced into a "real" row if care isn't taken.
- **Expected output:** The real half of the statutory portion of the dataset.
- **Dependencies:** Chunk 6.

---

## CHUNK 8 — Construct Real Precedent Task Instances

- **Objective:** Turn the precedent anchors from Chunk 6 into actual dataset task rows.
- **What will be changed:** New task rows created (real instances only).
- **Files/tasks involved:** New `tasks_precedent_real.jsonl`.
- **Verification needed:** Same standard as Chunk 7 — each context sentence's holding description must be checked against the verified source, not paraphrased from memory.
- **Expected output:** The real half of the precedent portion of the dataset.
- **Dependencies:** Chunk 6 (can run in parallel with Chunk 7).

---

## CHUNK 9 — Fabrication Construction Methodology (Design, No Generation Yet)

- **Objective:** Design the exact mutation rules per taxonomy category before generating a single fabricated instance, including the batch-and-gate human-review workflow from the earlier Operating Manual.
- **What will be changed:** No tasks — this is a methodology document.
- **Files/tasks involved:** New `fabrication_methodology.md`, specifying per-category construction rules (e.g., P2's page-offset range should be large enough to be unambiguous — this project's own senior review confirmed 150+ page deltas are cleanly diagnostic, so offsets should be deliberately calibrated, including some intentionally *harder* near-miss offsets for a subset, rather than only easy ones), and the review-batch size/approval threshold per category.
- **Verification needed:** None — design only.
- **Expected output:** A locked fabrication protocol.
- **Dependencies:** Chunks 7 and 8 (need real instances to mutate from).

---

## CHUNK 10 — Generate Fabricated Variants (Batch-and-Gate)

- **Objective:** Execute Chunk 9's methodology to produce the fabricated half of the dataset, reviewed in batches, not in one bulk pass.
- **What will be changed:** New fabricated task rows created.
- **Files/tasks involved:** New `tasks_fabricated.jsonl`, plus a `batch_approval_log.md` tracking each review batch's pass/reject status.
- **Verification needed:** Each batch spot-checked before the next is generated, per the earlier project's established batch-and-gate discipline — this is the step most likely to silently reintroduce quality problems if rushed.
- **Expected output:** Complete fabricated-instance set, matched to the real instances from Chunks 7–8.
- **Dependencies:** Chunk 9.

---

## CHUNK 11 — Deduplication, Balance & Structural QA

- **Objective:** Confirm the assembled dataset actually meets Chunk 2's spec — no duplicate real citations, correct balance, category minimums met — before it goes anywhere near annotators.
- **What will be changed:** No new content — this is a QA gate that may bounce work back to earlier chunks if it fails.
- **Files/tasks involved:** `analysis/structural_qa.py` run against the combined `tasks_statutory_real.jsonl` + `tasks_precedent_real.jsonl` + `tasks_fabricated.jsonl`.
- **Verification needed:** Automated checks (exact-duplicate detection, category-count tally) plus a manual spot-check that no context sentence was accidentally copy-pasted between rows.
- **Expected output:** A pass/fail QA report; only a pass unlocks Chunk 12.
- **Dependencies:** Chunk 10.

---

## CHUNK 12 — Blind Annotation Package Preparation

- **Objective:** Build the actual annotator-facing form/interface, applying the Org ID leak lesson directly this time — no field visible to annotators may encode ground truth, and this is verified *before* the form goes out, not after.
- **What will be changed:** New form/interface artifact; no dataset content changes.
- **Files/tasks involved:** Form-generation script (rebuilt from scratch given the prior leak), `annotation/blinding_audit.py` run against it, updated `annotation/guidelines_v2.md` incorporating the earlier taxonomy edge-case amendments (P2/P4 ordering rule, historical-convention Medium-confidence rule).
- **Verification needed:** Blinding audit must pass before the form is sent to anyone — this is a hard gate, mirroring the earlier remediation plan's Issue 1 protocol.
- **Expected output:** A verified-blind annotation instrument, ready to deploy.
- **Dependencies:** Chunk 11.

---

## CHUNK 13 — Annotation Execution (Human Round)

- **Objective:** Run the actual blind double-annotation with Shakila and Haris (or their successors) on the full rebuilt dataset (N = 150 tasks).
- **What will be changed:** Raw annotation data collected — no gold labels finalized yet.
- **Files/tasks involved:** New `project_responses_v2.csv` (covering 150 tasks), collected under the verified-blind instrument from Chunk 12.
- **Verification needed:** Confirm both annotators worked fully independently (no shared-answer coordination), per the original project's own ground rules.
- **Expected output:** Complete raw double-annotation covering 100% of the rebuilt task set (150 tasks).
- **Dependencies:** Chunk 12.

---

## CHUNK 14 — Inter-Annotator Agreement Computation

- **Objective:** Compute binary and category-level Cohen's Kappa on the actual, complete annotation round.
- **What will be changed:** No dataset content — produces the IAA report.
- **Files/tasks involved:** `analysis/iaa.py`, run against `project_responses_v2.csv` in full (not a partial subset).
- **Verification needed:** Cross-check that every one of the rebuilt dataset's rows has exactly two annotation entries before computing kappa — this is the specific reconciliation failure from the audit, worth a hard automated check this time rather than a manual claim.
- **Expected output:** A verified, complete IAA figure that actually corresponds 1:1 to the released dataset.
- **Dependencies:** Chunk 13.

---

## CHUNK 15 — Adjudication Protocol Redesign & Execution

- **Objective:** Resolve annotator disagreements using primary-source evidence only — explicitly banning any reference to internal Org IDs or construction metadata in adjudication reasoning, per the audit's core finding.
- **What will be changed:** No dataset content changes beyond finalizing disputed labels.
- **Files/tasks involved:** New `adjudication_sheet_v2.md`, with a mandatory field per disagreement: "primary source(s) consulted" — an adjudication entry without this field is treated as incomplete, not accepted.
- **Verification needed:** Each adjudicated disagreement must cite a specific, checkable source for its reasoning — matching the standard `senior_review.md` set (not `adjudication_sheet.md`'s Org-ID-based reasoning) in the earlier audit.
- **Expected output:** Fully adjudicated gold labels, with a reasoning trail an outside auditor could actually follow and check.
- **Dependencies:** Chunk 14.

---

## CHUNK 16 — Gold Dataset Packaging & Release

- **Objective:** Assemble the final, versioned, checksummed release file — this time with a verifiable chain from raw annotation through adjudication to release, so the Chunk-1-style audit gap can't recur silently.
- **What will be changed:** New `banlegit_cite_dataset_v2.csv` (containing the final 150 unique tasks), plus a `provenance_map.csv` explicitly linking every released row back to its annotation and adjudication record by ID.
- **Verification needed:** Automated check that every released row has a traceable provenance chain — this becomes a release gate, not an afterthought.
- **Expected output:** The actual final dataset of 150 unique tasks, with reproducibility built in rather than reconstructed after the fact.
- **Dependencies:** Chunk 15.

---

## CHUNK 17 — Paper Synchronization

- **Objective:** Rewrite the paper's Dataset, Methodology, and Results sections to match the rebuilt dataset exactly — numbers, structure, taxonomy coverage, IAA, all pulled from Chunk 16's artifacts, not from memory of the old numbers.
- **What will be changed:** `paper.tex` Sections 3–5, Limitations, and all corresponding tables.
- **Files/tasks involved:** `paper.tex`, cross-checked line-by-line against `provenance_map.csv` and the final IAA report.
- **Verification needed:** Every number in the paper must trace to a specific file/script output, per the earlier project's reproducibility convention (RESULTS.md-style mapping).
- **Expected output:** A paper that is finally describing the dataset that actually ships with it.
- **Dependencies:** Chunk 16 (and, if you're also addressing the earlier retrieval-leakage/model-baseline findings, those remain separate work streams layered on top of this once the dataset itself is trustworthy).

---

## Recommended Starting Point

**Start with Chunk 3 (Statutory Scope Decision).**

Chunks 1 and 2 are fully completed, locking the specifications at exactly N=150 unique, non-repeating tasks. Proceeding to Chunk 3 allows us to establish the statutory Acts and provisions (including the Nari O Shishu 2026 amendments) that will serve as our 37 statutory anchors.