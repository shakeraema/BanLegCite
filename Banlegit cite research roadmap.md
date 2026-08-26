# BanLegit-Cite: Complete Research Supervision Roadmap
### From Idea to ICCIT Submission to Journal Extension

---

## PART 0 — CRITICAL EVALUATION (Go / No-Go Decision)

### 0.1 Is this genuinely novel?

**Verdict: YES, conditionally novel — proceed, but narrow the claim.**

The novelty is **jurisdictional + linguistic**, not methodological. This must be stated explicitly in your paper's contribution section, or reviewers with NLP-benchmark background will correctly flag it as "LePhantomCite applied to a new country."

| Competing work | What it actually does | Why it does NOT cover your gap |
|---|---|---|
| **LePhantomCite** (2026) | 1,300 US federal appellate brief excerpts, 4,499 citation instances, 5 hallucination categories, agentic vs. standard verification (GPT-5 agentic: 82.8% recall) | English-only, US common law, no statutory-code duality, no diglossia |
| **LegalCiteBench** (2026) | ~24K instances from 1,000 US judicial opinions (Case Law Access Project), 5 tasks: retrieval/completion/error-detection/matching/correction | English-only, closed-book, no South Asian jurisdiction |
| **SG-LegalCite** (2026) | 100,890 case-principle pairs, Singapore Supreme Court, principle-augmented **retrieval** | Different task family (retrieval ranking, not fabrication detection) |
| **LeCNet** | Indian legal citation network for link prediction | Different task (graph/network), not hallucination |
| **BenHalluEval** (2026) | 12,000 hallucinated candidates, 4 general NLP tasks, Bengali | Zero legal content |
| **Mina** | BD Bar Council exam-passing agent | Exam correctness, not citation fabrication |

**Confirmed gap:** No existing benchmark tests citation fabrication in Bangladeshi law, in Bangla, across the statute+precedent duality that defines the BD legal system. This is real and defensible.

### 0.2 Weaknesses of the idea as currently stated

1. **"Just a translated LePhantomCite" risk** — if you don't add at least one structural dimension beyond "same method, new country," ICCIT reviewers (and any later journal reviewers) will read it as low-effort geographic transfer.
2. **No baseline novelty** — running GPT/Llama on your data is expected, not a contribution by itself.
3. **Expert annotation bottleneck** — BD legal expert availability is your single biggest execution risk, not the NLP.
4. **Source data scarcity** — DLR/BLC/ALR digitized coverage is inconsistent; underestimate this and your timeline breaks.
5. **No stated hypothesis** — "we built a dataset" is a resource paper; ICCIT wants a research question with a measurable answer.

### 0.3 Required modification before proceeding

**Do not submit a pure dataset paper.** Reframe as:

> **RQ:** Does the statute-vs-precedent duality of a mixed civil/common-law system (Bangladesh) produce a *different* citation-fabrication error profile than pure common-law systems (US), and does this transfer to multilingual (Bangla/English) legal queries?

This converts BanLegit-Cite from "a dataset" into "a dataset + an empirical finding," which is what gets accepted. Keep the **Cross-Script Verification Test** as your headline second contribution (highest novelty per prior analysis) — it is what elevates this from a resource paper to a research paper.

**Final locked scope for ICCIT:** BanLegit-Cite dataset (statutory + precedent fabrication) + dual-taxonomy + cross-script robustness test + baseline evaluation (standard + agentic). Temporal/amendment-aware verification is explicitly OUT of scope — defer to journal extension (Part 22).

---

## PART 1 — STAGE-BY-STAGE RESEARCH PLAN

---

### STAGE 1 — Problem Formulation

- **Objective:** Convert the general idea into one falsifiable research question and 2–3 sub-hypotheses.
- **Why necessary:** Every subsequent stage (annotation, metrics, paper structure) depends on a fixed RQ. Changing scope mid-project is the #1 cause of missed deadlines.
- **Expected outputs:** 1-page problem statement; 1 primary RQ; 2–3 hypotheses (H1–H3).
- **Prerequisites:** None — do this first.
- **Recommended reading:** Dahl et al. 2024 ("Large Legal Fictions"); LePhantomCite paper (arXiv 2606.21155); LegalCiteBench (arXiv 2605.10186).
- **Datasets/resources:** None yet.
- **Implementation:** Write the RQ from Part 0.3 verbatim; derive:
  - H1: Fabrication detection recall is lower on statutory citations than precedent citations (novel duality claim).
  - H2: Detection recall drops when the query language is Bangla vs. English, for the same underlying fact (diglossia claim).
  - H3: Agentic verification narrows H1/H2 gaps more than it narrows overall error rate (replicates + extends LePhantomCite's agentic finding).
- **Tools:** None — plain writing.
- **Common mistakes:** Writing a vague RQ ("can LLMs detect fake citations in Bangla legal text") that isn't falsifiable.
- **Risks:** Scope creep if RQ isn't locked before Stage 6.
- **Evaluation criteria:** RQ must be answerable with a yes/no or a measured effect size from the planned experiments.
- **Timeline:** 2–3 days.
- **Exit criteria:** RQ + H1–H3 written, reviewed by your advisor/co-author, frozen (no further edits without a formal reason).

---

### STAGE 2 — Novelty Validation

- **Objective:** Formally document the gap table from Part 0.1 as a defensible related-work section skeleton.
- **Why necessary:** ICCIT reviewers reject papers most often for "insufficient positioning against prior work," not weak method.
- **Expected outputs:** Related-work comparison table (already drafted above) + 1-paragraph novelty statement.
- **Prerequisites:** Stage 1 complete.
- **Recommended reading:** All 6 competing papers listed in Part 0.1, read in full (not abstract only) — especially their limitations sections, since your paper must cite what *they* admit they don't cover.
- **Datasets/resources:** arXiv, ACL Anthology, Google Scholar alerts for "legal citation hallucination," "Bangla legal NLP," set up now and monitored monthly until submission.
- **Implementation:** For each competitor, extract: task definition, dataset size, language, jurisdiction, category taxonomy, best-model score. Build the table now — reuse it directly in your paper's Related Work.
- **Tools:** Zotero or Notion for reference management; Connected Papers for citation graph exploration.
- **Common mistakes:** Only checking arXiv, missing ACL/EMNLP/NAACL system-demo tracks and workshop papers (e.g., justNLP, AI4Law workshops) where adjacent legal-NLP-for-South-Asia work often appears first.
- **Risks:** A directly competing Bangla legal benchmark could appear before your submission — this is why Stage 2 is repeated as a check immediately before submission (Stage 14).
- **Evaluation criteria:** Every cell in the gap table must be traceable to a specific sentence/claim in the source paper, not paraphrased assumption.
- **Timeline:** 1 week.
- **Exit criteria:** Gap table complete and citation-verified; no unresolved "does X paper already do this?" questions remain.

---

### STAGE 3 — Literature Review (Full)

- **Objective:** Build complete theoretical grounding across four areas: legal NLP, hallucination detection, RAG/retrieval, benchmark construction methodology.
- **Why necessary:** Prevents reinventing evaluation metrics/annotation schemes that already have established best practice.
- **Expected outputs:** Annotated bibliography (25–40 papers); a literature map grouped by theme.
- **Prerequisites:** Stage 2.
- **Recommended reading (four clusters):**
  - *Legal hallucination:* Dahl et al. 2024; LePhantomCite; LegalCiteBench; "Hallucinating Law" (Stanford RegLab line of work).
  - *Legal NLP for South Asia:* LeCaRD/LeCaRDv2 (Chinese, for methodology transfer); IL-PCR (Indian precedent retrieval); AILA.
  - *Hallucination benchmarking methodology:* BenHalluEval; PerHalluEval (Persian — same construction pattern for a low-resource language, directly useful as a template).
  - *RAG/agentic verification:* ReAct-style agentic search papers; the agentic evaluation section of LePhantomCite specifically.
- **Datasets/resources:** ACL Anthology bulk search, arXiv legal-NLP category, Semantic Scholar API for citation-graph expansion from your six core papers.
- **Implementation:** Maintain a shared spreadsheet: paper | task | dataset size | language | key metric | relevance-to-you (1–5).
- **Tools:** Zotero, Semantic Scholar API, Connected Papers.
- **Common mistakes:** Reading only abstracts; missing that PerHalluEval's construction pipeline (LLM-generation + human validation, dynamic refresh to prevent leakage) is your best methodological template for low-resource-language benchmark construction.
- **Risks:** Literature review scope creep — cap at 40 papers, prioritize the 4 clusters above.
- **Evaluation criteria:** You should be able to explain, without notes, how your taxonomy differs from LePhantomCite's five categories and why.
- **Timeline:** 1.5–2 weeks (runs partially parallel with Stage 4).
- **Exit criteria:** Annotated bibliography complete; literature map ready to become paper's Related Work section.

---

### STAGE 4 — Research Gap Identification (Formal)

- **Objective:** State the gap as a single sentence usable in your abstract/intro.
- **Why necessary:** This sentence is the first thing a reviewer reads to decide if the paper is worth continuing.
- **Expected outputs:** One gap sentence, reviewed against Stage 2's table.
- **Prerequisites:** Stages 2–3.
- **Recommended reading:** N/A — synthesis task.
- **Datasets/resources:** N/A.
- **Implementation:** Draft: *"While recent work has introduced citation-hallucination benchmarks for U.S. common-law systems (LePhantomCite, LegalCiteBench) and general-domain Bengali hallucination (BenHalluEval), no existing resource evaluates citation fabrication in Bangladeshi legal text, where models must simultaneously verify codified statutory citations and common-law precedent citations across a Bangla/English diglossic environment."*
- **Tools:** N/A.
- **Common mistakes:** Overclaiming ("no work exists on legal hallucination in South Asia" — false, LeCNet exists for India, just for a different task). Be precise about task, not just geography.
- **Risks:** None significant at this stage.
- **Evaluation criteria:** Sentence must survive a devil's-advocate read: "could a reviewer name a paper that already does this?" If yes, revise.
- **Timeline:** 2 days.
- **Exit criteria:** Gap sentence frozen and inserted into paper draft skeleton (create the skeleton now, even if empty).

---

### STAGE 5 — Research Questions and Hypotheses (Final Form)

- **Objective:** Lock RQ + H1–H3 into their testable, metric-linked final form.
- **Why necessary:** Metrics (Stage 13) must be chosen to directly answer these, not the reverse.
- **Expected outputs:** RQ/H1–H3 table, each row mapped to a specific planned experiment.
- **Prerequisites:** Stage 1 draft, refined using Stage 3 methodology knowledge.
- **Recommended reading:** Statistical hypothesis-testing conventions in NLP (e.g., how LePhantomCite reports recall deltas with significance).
- **Datasets/resources:** N/A.
- **Implementation table:**

| Hypothesis | Metric | Test |
|---|---|---|
| H1: statutory vs. precedent recall gap | Detection recall, per category | Paired bootstrap significance test |
| H2: Bangla vs. English recall gap | Detection recall, per script, same fact-pairs | Paired test (matched pairs by construction) |
| H3: agentic narrows the gap more than it narrows overall error | Δrecall (agentic − standard), per subgroup | Interaction effect test |

- **Tools:** scipy.stats, statsmodels for paired bootstrap/permutation tests.
- **Common mistakes:** Choosing metrics after running experiments (post-hoc rationalization) instead of before.
- **Risks:** If H2's matched-pair design isn't clean (Stage 6), the test becomes invalid — flag this dependency now.
- **Evaluation criteria:** Every hypothesis has exactly one pre-registered statistical test.
- **Timeline:** 2–3 days.
- **Exit criteria:** RQ/H/metric table complete and will not change without formal justification logged in a decision log (start this log now — a simple dated markdown file).

---

### STAGE 6 — Dataset Scope and Design

- **Objective:** Define exact corpus boundaries: which statutes, which courts, which time range, target size.
- **Why necessary:** Undefined scope is the single largest cause of 8–12 week overruns in dataset papers.
- **Expected outputs:** A locked data-scope document.
- **Prerequisites:** Stages 1–5.
- **Recommended reading:** LePhantomCite's data-construction section (source selection criteria, why pre-AI-era briefs were chosen to ensure clean ground truth).
- **Datasets/resources & exact scope decision:**
  - **Statutes:** Penal Code 1860, Code of Criminal Procedure 1898, Code of Civil Procedure 1908, Nari O Shishu Nirjatan Daman Ain 2000 — four acts only, not "all BD law." This bounds Stage 8 effort.
  - **Case law:** Appellate Division + High Court Division judgments, sourced from Bangladesh Supreme Court Online Digest — target a fixed date range (e.g., 2010–2023) to avoid picking up cases the annotators themselves are unsure about.
  - **Target size:** 1,000–1,300 total citation instances (matches LePhantomCite's scale — defensible comparison point in your paper).
- **Implementation:** Write a formal data-scope PDF/markdown: inclusion criteria, exclusion criteria, exact source URLs, snapshot date (legal sites change — record access date for reproducibility).
- **Tools:** Simple spreadsheet or SQLite table to track source-document provenance from day one.
- **Common mistakes:** Starting collection before finalizing scope, leading to inconsistent source formatting later.
- **Risks:** Digitized coverage gaps for older BD judgments — mitigate by picking a recent date range (post-2010) where digital records are denser.
- **Evaluation criteria:** Scope document reviewed and signed off before any scraping begins.
- **Timeline:** 3–4 days.
- **Exit criteria:** Scope document frozen; any change after this point requires updating the decision log with a reason.

---

### STAGE 7 — Citation Taxonomy (Fabricated / Incorrect / Outdated / Hallucinated / Misleading)

- **Objective:** Define a precise, non-overlapping category scheme combining statutory and precedent fabrication types.
- **Why necessary:** This taxonomy is your paper's core conceptual contribution (Part 0.3) — it must be tighter and more defensible than LePhantomCite's.
- **Expected outputs:** Final taxonomy document with 1 canonical example per category.
- **Prerequisites:** Stage 6.
- **Recommended reading:** LePhantomCite's Table 1 (five-category taxonomy) as the direct template to extend, not replace.
- **Datasets/resources:** None new.
- **Implementation — locked taxonomy (two super-categories, five sub-types each):**

  **Statutory-fabrication super-category:**
  1. *Non-existent section* — cites a section number that does not exist in the named Act.
  2. *Wrong Act attribution* — correct section number, wrong Act name (e.g., confusing Penal Code §376 with Nari O Shishu equivalent).
  3. *Misstated content* — real section, fabricated/incorrect description of what it says.
  4. *Cross-jurisdictional bleed* — cites Indian/Pakistani statutory equivalents as if binding in BD.
  5. *Repealed/superseded citation* (flagged but NOT deeply evaluated in ICCIT version — reserved for journal extension's temporal work; include only as a labeled-but-excluded category here to avoid scope creep).

  **Precedent-fabrication super-category:**
  1. *Non-existent case* — case does not exist at all.
  2. *Wrong citation locator* — real case, fabricated volume/page/reporter.
  3. *Misattributed holding* — real case, fabricated ruling/outcome.
  4. *Wrong court level* — attributes a High Court decision to the Appellate Division or vice versa.
  5. *Cross-jurisdictional precedent bleed* — cites Indian/Pakistani case law as binding BD precedent.

- **Tools:** N/A — conceptual design, documented in markdown with 2–3 real examples per category collected during Stage 6 scoping.
- **Common mistakes:** Category overlap (e.g., "wrong Act" and "cross-jurisdictional bleed" can collide) — resolve with a decision-tree diagram, not prose rules alone.
- **Risks:** If categories are ambiguous, inter-annotator agreement (Stage 10) will be low and unfixable late.
- **Evaluation criteria:** Every one of the ~15 pilot examples from Stage 6 must classify unambiguously into exactly one category by two independent readers.
- **Timeline:** 1 week, includes 1 pilot round with a second person.
- **Exit criteria:** Taxonomy frozen; annotation guideline document (Stage 9) can now be written against it.

---

### STAGE 8 — Dataset Collection Strategy

- **Objective:** Execute source-text collection per Stage 6 scope.
- **Why necessary:** Real, verified source text is the ground-truth anchor — the entire benchmark's validity rests on this being unambiguously correct.
- **Expected outputs:** Raw corpus of 1,200–1,500 real citation instances (buffer above the 1,000–1,300 target to survive later filtering).
- **Prerequisites:** Stage 6 scope frozen.
- **Recommended reading:** N/A — execution stage.
- **Datasets/resources:** bdlaws.minlaw.gov.bd (statutes); Bangladesh Supreme Court website/digest; DLR/BLC/ALR volumes accessible via your institution's library or law-school partnership — **secure this access explicitly at this stage, it is a common bottleneck.**
- **Implementation:**
  1. Scrape/manually extract statute text with section-level granularity, store with exact source URL + retrieval date.
  2. Extract case citations from real judgments — do NOT invent example citations even for testing; every "real" instance must be independently verifiable.
  3. Store everything in a structured schema from day one (see GitHub repo structure, Part 3).
- **Tools:** Python (`requests`/`BeautifulSoup` or `Scrapy` for statute pages; manual PDF extraction with `pdfplumber` for scanned judgment PDFs); OCR (`Tesseract`) if judgments are scanned images, common for older BD records.
- **Common mistakes:** Scraping without recording provenance metadata — you will need this for reproducibility (Stage 19) and cannot reconstruct it later.
- **Risks:** Scanned/low-quality PDFs requiring OCR will have transcription errors — budget extra review time for OCR'd sources specifically; flag OCR-sourced instances as a metadata field so you can report a data-quality caveat honestly.
- **Evaluation criteria:** Every raw instance has: source type, source URL, retrieval date, OCR-flag (yes/no), initial format-validity check passed.
- **Timeline:** 2.5–3 weeks (largest single time block in the project).
- **Exit criteria:** Raw corpus assembled, deduplicated, and passes an automated format-validity check (e.g., citation string matches expected structural pattern) before annotation begins.

---

### STAGE 9 — Annotation Guidelines

- **Objective:** Write a guideline document detailed enough that two independent annotators reach consistent labels without consulting you.
- **Why necessary:** Directly determines Stage 11's inter-annotator agreement — the paper's core quality signal.
- **Expected outputs:** Annotation guideline PDF (8–15 pages), with decision-tree diagram from Stage 7.
- **Prerequisites:** Stage 7 taxonomy frozen, Stage 8 raw corpus available for real examples.
- **Recommended reading:** Any annotation-guideline appendix from LePhantomCite/LegalCiteBench/BenHalluEval — copy their structural format (task description → decision tree → worked examples → edge-case FAQ).
- **Datasets/resources:** 20–30 hand-picked ambiguous examples from your raw corpus for the "edge case FAQ" section.
- **Implementation:** Sections required: (1) task overview, (2) taxonomy with decision tree, (3) 3 worked examples per category (15 categories worth), (4) edge-case FAQ, (5) fabrication-generation instructions (separate sub-guideline for the LLM-assisted generation step in Stage 8B below).
- **Tools:** Plain document, but pilot it using a shared annotation tool (see Stage 10 tools).
- **Common mistakes:** Writing guidelines in isolation without a pilot round — always pilot-test on 20 examples with a second annotator before finalizing.
- **Risks:** Guidelines that work for you (the designer) but fail for an independent annotator — this is exactly what the pilot round catches.
- **Evaluation criteria:** Pilot round (20 examples, 2 annotators) reaches Cohen's κ ≥ 0.6 before guidelines are considered final; below that, revise and re-pilot.
- **Timeline:** 1 week writing + 3–4 days piloting = ~1.5 weeks.
- **Exit criteria:** Pilot κ ≥ 0.6 achieved; guideline document frozen and version-numbered.

---

### STAGE 8B — Fabrication Generation (sits between Stage 8 and Stage 9 in practice)

- **Objective:** Produce the fabricated half of the dataset using LLM-assisted generation, per taxonomy category.
- **Why necessary:** Manual fabrication writing does not scale to 1,000+ instances; LLM generation + human review is the established pattern (BenHalluEval, PerHalluEval).
- **Expected outputs:** ~1,000–1,300 fabricated instances, category-labeled, batch-tracked.
- **Prerequisites:** Stage 7 taxonomy, Stage 8 real corpus (fabrication is generated *conditioned on* real citations, not from scratch).
- **Recommended reading:** BenHalluEval's generation-prompt design (explicit hallucination-type conditioning); PerHalluEval's dynamic refresh methodology (relevant for your reproducibility/leakage-prevention plan, Stage 19).
- **Datasets/resources:** GPT-5-class model via API, or Claude via API — pick one and document the exact model version used (critical for reproducibility).
- **Implementation:** Batch generation (50–100 instances/batch) per category → human spot-check per batch (this is the "Agentic AI supervised, repeated review" workflow discussed earlier) → reject/regenerate batches failing plausibility or implausibility checks → advance only after a batch passes.
- **Tools:** Anthropic/OpenAI API, structured-output JSON prompting for consistent metadata per instance.
- **Common mistakes:** Generating all instances in one unsupervised pass — always batch-and-gate (established in earlier discussion of agentic supervision).
- **Risks:** LLM-generated fabrications that are either too obviously fake (trivial task) or too subtly wrong (unverifiable even by experts) — calibrate difficulty in the pilot round.
- **Evaluation criteria:** Spot-checked batches must show <10% rejection rate before the category is considered stable.
- **Timeline:** 2 weeks, runs partially parallel with Stage 9 guideline-writing.
- **Exit criteria:** Full fabricated set generated and batch-approved.

---

### STAGE 10 — Annotation Workflow

- **Objective:** Execute full-scale annotation: verify real instances, verify/label fabricated instances, apply taxonomy.
- **Why necessary:** This produces the actual gold-standard labels the benchmark is built on.
- **Expected outputs:** Fully annotated dataset with category labels + annotator IDs + confidence flags.
- **Prerequisites:** Stage 9 guidelines frozen at κ ≥ 0.6; Stage 8B fabricated set ready.
- **Recommended reading:** N/A — execution stage.
- **Datasets/resources:** Recruit 2–3 BD law students/junior lawyers (not just senior faculty — senior faculty for adjudication only, see Stage 11) for primary annotation; 1 senior legal expert for disagreement adjudication.
- **Implementation:** Double-annotate 100% of instances (not a sample) given the stakes of legal-domain ground truth; route disagreements to the adjudicator.
- **Tools:** Label Studio or Doccano (open-source annotation platforms, support custom taxonomy schemas and multi-annotator tracking) — do not use spreadsheets at this scale, you lose annotator-agreement tracking.
- **Common mistakes:** Single-annotation to save time — this invalidates your IAA metric entirely and will be flagged by reviewers as unrigorous for a legal dataset.
- **Risks:** Annotator fatigue/inconsistency over long sessions — cap sessions at 60–90 minutes, rotate categories.
- **Evaluation criteria:** 100% double-annotation coverage; disagreement log maintained per instance.
- **Timeline:** 3–4 weeks (largest single human-effort block).
- **Exit criteria:** All instances annotated by 2 annotators; disagreement set identified and routed to Stage 11.

---

### STAGE 11 — Quality Control and Inter-Annotator Agreement

- **Objective:** Compute formal IAA, adjudicate disagreements, finalize gold labels.
- **Why necessary:** IAA score is a mandatory reported statistic for any annotated benchmark — its absence is an automatic reviewer red flag.
- **Expected outputs:** Final gold-label dataset; reported Cohen's κ / Fleiss' κ per category and overall.
- **Prerequisites:** Stage 10 complete.
- **Recommended reading:** Standard IAA reporting conventions in NLP annotation papers (Artstein & Poesio survey on agreement metrics).
- **Datasets/resources:** Disagreement log from Stage 10.
- **Implementation:** Compute Cohen's κ (2 annotators) or Fleiss' κ (if 3+) per taxonomy category and overall; senior adjudicator makes final call on all disagreements; report both pre- and post-adjudication numbers.
- **Tools:** `scikit-learn` (`cohen_kappa_score`), `statsmodels`, or `nltk.metrics.agreement`.
- **Common mistakes:** Reporting only overall κ and hiding that specific categories (e.g., "cross-jurisdictional bleed") have much lower agreement — report per-category, it's more honest and often more interesting.
- **Risks:** Low κ (<0.6) on any category signals a Stage 7/9 problem — be willing to revise the taxonomy even at this late stage rather than ship weak ground truth.
- **Evaluation criteria:** Target overall κ ≥ 0.7 (substantial agreement); minimum acceptable ≥ 0.6 with explicit discussion of harder categories.
- **Timeline:** 1–1.5 weeks.
- **Exit criteria:** Gold dataset finalized and frozen — no further label changes after this point without a documented, versioned reason.

---

### STAGE 12 — Benchmark Construction

- **Objective:** Package the gold dataset into a formal benchmark: splits, task definitions, format.
- **Why necessary:** A benchmark is not just labeled data — it needs fixed splits and clear task framing for others to reuse it (this is what makes it citable infrastructure, not just a paper artifact).
- **Expected outputs:** Train/dev/test splits (or dev/test-only if train isn't meaningful for a fine-tuning-free eval); JSON/JSONL formatted release.
- **Prerequisites:** Stage 11 gold dataset frozen.
- **Recommended reading:** LegalCiteBench's task-family definition (5 distinct tasks from one dataset) as a structural template.
- **Datasets/resources:** N/A — packaging stage.
- **Implementation:** Define your locked task set now (see Stage 14 for full task list); split by category proportionally, not randomly, to guarantee each split has balanced category representation; hold out a blind test set you do not touch during baseline development.
- **Tools:** `pandas`/`datasets` (HuggingFace) library for standardized formatting; publish to HuggingFace Datasets Hub for visibility.
- **Common mistakes:** Random splitting without stratifying by category — can leave rare categories entirely out of test set.
- **Risks:** If your total N (~1,000–1,300) is small, splits may be too small for stable per-category metrics — consider k-fold cross-validation evaluation instead of a single fixed split if category counts are below ~30 per split.
- **Evaluation criteria:** Every category represented in both dev and test with a minimum count (e.g., ≥15 instances) to support meaningful per-category metrics.
- **Timeline:** 3–4 days.
- **Exit criteria:** Splits frozen, uploaded to a version-controlled location, checksummed.

---

### STAGE 13 — Baseline Systems

- **Objective:** Implement and run baseline models: standard (non-agentic) LLM verification and agentic (search-augmented) verification.
- **Why necessary:** Baselines establish the difficulty of your benchmark and directly test H1–H3.
- **Expected outputs:** Results table across ≥4 models (mix of open + closed), standard vs. agentic setting.
- **Prerequisites:** Stage 12 splits ready.
- **Recommended reading:** LePhantomCite's agentic-setting methodology (models can iteratively search legal databases/web before verdict) — replicate this design directly.
- **Datasets/resources:** Model access: GPT-5-class, Claude Sonnet/Opus-class, one open-weight model (Llama-3.x or Qwen2.5, for reproducibility since open weights don't require ongoing API cost for replication), one Bangla-centric model if available (BanglaBERT-derived or a Bangla-tuned LLM).
- **Implementation:** Standard setting: model sees the citation in context, must classify real/fabricated + category. Agentic setting: model can issue search queries against a provided legal-database index (build a minimal retrieval index over your Stage 8 source corpus + general web search tool) before answering.
- **Tools:** Anthropic/OpenAI APIs, `vllm` or `transformers` for open-weight models, a lightweight retrieval index (`elasticsearch` or `FAISS`) over your statute/case corpus for the agentic setting's search tool.
- **Common mistakes:** Only testing closed models — reviewers value open-weight baselines for reproducibility; don't skip them even if scores are lower.
- **Risks:** Agentic setting cost/complexity — budget API costs explicitly; agentic runs are far more expensive than standard classification.
- **Evaluation criteria:** All 4+ models run under identical prompts/settings except the standard-vs-agentic variable; results logged with exact model version/date (models change).
- **Timeline:** 2 weeks.
- **Exit criteria:** Full results matrix (model × setting × category) computed and sanity-checked (no impossible scores, no crashed runs silently excluded).

---

### STAGE 14 — Benchmark Tasks (Formal Definitions)

Lock exactly three tasks — do not add more for the ICCIT version:

1. **Binary fabrication detection** — real vs. fabricated, given citation + context.
2. **Category classification** — given a confirmed fabrication, classify into one of the 10 sub-types (Stage 7).
3. **Cross-script robustness** — Task 1, repeated on matched Bangla/English pairs, reporting the recall delta (this is your H2 test and your headline novelty result).

- **Objective/Why/Outputs/etc. follow Stage 13's implementation directly** — this stage is really the formal write-up of what Stage 13 already executed. Timeline: folded into Stage 13's 2 weeks, add 2–3 days for formal task documentation.

---

### STAGE 15 — Evaluation Metrics

- **Objective:** Define exact metrics per task, matched to H1–H3.
- **Why necessary:** Ambiguous metrics ("accuracy") undersell nuanced findings; legal-domain stakes justify precision/recall separation.
- **Expected outputs:** Metrics specification document.
- **Implementation:**
  - Task 1: Precision, Recall, F1 on the fabricated class specifically (not just accuracy — class imbalance and asymmetric cost of missing a fabrication matter, following BenHalluEval's dual-track logic of scoring false-positive and false-negative separately).
  - Task 2: Macro-F1 across 10 categories (macro, not micro, so rare categories aren't drowned out).
  - Task 3: Recall delta (Bangla − English) per matched pair, with paired significance test (Stage 5).
- **Tools:** `scikit-learn.metrics`.
- **Common mistakes:** Reporting only accuracy on an imbalanced real/fabricated split.
- **Timeline:** 2–3 days (definition), executed within Stage 13's runs.
- **Exit criteria:** Metrics computed for all model/setting/category combinations, no missing cells.

---

### STAGE 16 — Experimental Protocol

- **Objective:** Formalize reproducible experiment settings: temperature, prompts, seeds, number of runs.
- **Why necessary:** LLM outputs are stochastic; single-run results are not publishable without variance reporting.
- **Implementation:** Temperature = 0 for primary results (deterministic, matches BenHalluEval's protocol) + 3 repeated runs at temperature 0.7 to report variance as a robustness check; fix and document exact prompt templates in an appendix; fix random seeds for any sampling steps.
- **Tools:** Prompt-version-controlled in the GitHub repo (Part 3), not just pasted in the paper.
- **Common mistakes:** Not fixing/reporting prompt wording — irreproducible without it.
- **Timeline:** Folded into Stage 13; formalize protocol doc in 2 days before running.
- **Exit criteria:** Protocol document exists before Stage 13 execution begins (not after).

---

### STAGE 17 — Error Analysis

- **Objective:** Qualitatively examine failure patterns beyond aggregate metrics.
- **Why necessary:** This is where your H1/H2 findings get explained, not just reported — reviewers and future readers value this most.
- **Expected outputs:** Error-analysis section with 8–12 concrete examples, categorized failure patterns (e.g., "models over-trust real-sounding Act names," "diglossic queries fail more on precedent than statutory citations").
- **Implementation:** Manually review a stratified sample (~50 errors) from your best and worst-performing models; look specifically for the H1 (statute vs. precedent) and H2 (script) patterns predicted.
- **Tools:** Manual review, supported by a simple filtering script over the results JSON.
- **Common mistakes:** Cherry-picking only errors that support your hypothesis — review a genuinely random stratified sample first, then select illustrative examples from it.
- **Timeline:** 1 week.
- **Exit criteria:** Error patterns documented and linked back explicitly to H1–H3.

---

### STAGE 18 — Statistical Significance Testing

- **Objective:** Confirm H1–H3 findings are not noise.
- **Implementation:** Paired bootstrap resampling (10,000 iterations) for recall deltas; report 95% CI, not just p-values (CIs are more informative and increasingly expected).
- **Tools:** `scipy.stats`, custom bootstrap script (simple, ~30 lines).
- **Common mistakes:** Using unpaired tests on paired data (your cross-script pairs are matched — must use paired tests).
- **Timeline:** 3–4 days.
- **Exit criteria:** All three hypotheses have a reported effect size + CI/p-value.

---

### STAGE 19 — Reproducibility

- **Objective:** Ensure every number in the paper can be regenerated by a stranger.
- **Implementation:** Freeze exact model versions/dates used (models silently update); pin all library versions (`requirements.txt`/`environment.yml`); include exact prompts, seeds, splits as files, not just described in prose; add a `RESULTS.md` mapping every paper table/figure to the exact script that produced it.
- **Tools:** `git`, Docker (optional but strong for full-environment reproducibility), `DVC` for dataset versioning if the dataset evolves.
- **Common mistakes:** Describing methodology only in prose without shipping the actual code/config.
- **Timeline:** Ongoing from Stage 8 onward, formalized as a dedicated 3–4 day pass before submission.
- **Exit criteria:** A colleague not involved in the project can clone the repo and regenerate at least the main results table.

---

### STAGE 20 — Open-Source Release

- **Objective:** Publish dataset + code publicly, with a clear license and data statement.
- **Implementation:** HuggingFace Datasets Hub release; GitHub code release; explicit license (check BD legal-text copyright status — statutes are typically public domain/government works, but confirm before release, especially for DLR/BLC/ALR reporter text which may carry publisher copyright — you may need to release only citation metadata, not full reporter text, for those).
- **Common mistakes:** Overlooking reporter copyright — LDR/BLC/ALR are commercial law reports; releasing full text may violate copyright even though the citations themselves (facts) are not copyrightable. Release structured metadata + short excerpts under fair-use-length quotation, not full judgment text.
- **Timeline:** 3–5 days, before submission (ICCIT increasingly expects data/code availability statements).
- **Exit criteria:** Public repo + dataset live, linked in the paper, DOI obtained (Zenodo) for citability.

---

### STAGE 21 — ICCIT Paper Structure

Standard structure, mapped directly to your stages:

1. **Abstract** — RQ + headline finding (H2 result likely most striking).
2. **Introduction** — gap sentence (Stage 4), contributions bullet list (3 items: dataset, taxonomy, cross-script finding).
3. **Related Work** — Stage 2/3 table, condensed to prose + 1 table.
4. **BanLegit-Cite Dataset** — Stages 6–8, 8B (scope, sources, construction).
5. **Taxonomy** — Stage 7 (with decision-tree figure).
6. **Annotation & Quality Control** — Stages 9–11 (guidelines summary + IAA table).
7. **Benchmark Tasks & Metrics** — Stages 12, 14–15.
8. **Experiments** — Stage 13, 16.
9. **Results** — main tables, H1/H2/H3 answered explicitly.
10. **Error Analysis** — Stage 17.
11. **Limitations** — be explicit: dataset size, 4-Act scope, temporal validity excluded (sets up journal extension).
12. **Conclusion**.
13. **Reproducibility/Data Statement** — Stage 19–20 links.

- **Timeline:** 2 weeks writing (can start earlier, drafting sections as their stages complete — do NOT wait until all experiments finish to start writing Sections 1–7).
- **Exit criteria:** Full draft, internal review by 1–2 colleagues, revised, submitted before deadline with buffer.

---

## PART 2 — MINIMUM PUBLISHABLE VERSION (MVP) FOR ICCIT

If timeline pressure forces cuts, cut in this order (do not cut earlier items to save later ones):

1. **Keep:** BanLegit-Cite core dataset (statute + precedent fabrication), full taxonomy, standard-setting baselines, IAA-verified gold labels.
2. **Keep:** Cross-script test (this is your differentiator — cutting it reduces the paper to "LePhantomCite for Bangladesh," a much weaker accept).
3. **Cut first if needed:** Agentic baseline — report standard-setting results only, mention agentic as future work.
4. **Cut second if needed:** Reduce from 4 statutes to 2 (Penal Code + Nari O Shishu Ain) and reduce dataset target from 1,300 to 700–800 instances — still comparable in scale to credible benchmark papers, still supports IAA and significance testing.
5. **Never cut:** Double-annotation/IAA — a legal dataset without agreement statistics will not survive review regardless of other strengths.

---

## PART 3 — GITHUB REPOSITORY STRUCTURE

```
banlegit-cite/
├── README.md                        # dataset card, quick start, citation
├── LICENSE                          # data license (see Stage 20 copyright note)
├── CITATION.cff
├── requirements.txt / environment.yml
├── decision_log.md                  # dated log of every scope change (Stage 1 onward)
│
├── data/
│   ├── raw/                         # scraped, provenance-tagged, untouched
│   │   ├── statutes/
│   │   └── case_law/
│   ├── fabricated/                  # Stage 8B outputs, batch-tracked
│   ├── annotated/                   # Stage 10 double-annotations + adjudication
│   ├── gold/                        # Stage 11 final frozen labels
│   └── splits/                      # Stage 12 dev/test JSONL
│
├── annotation/
│   ├── guidelines_v{N}.pdf          # versioned, Stage 9
│   ├── taxonomy_decision_tree.svg
│   └── label_studio_config.xml
│
├── generation/
│   ├── prompts/                     # Stage 8B fabrication-generation prompts
│   └── batch_logs/                  # per-batch approval/rejection records
│
├── src/
│   ├── data_collection/             # scrapers, OCR pipeline
│   ├── fabrication_generation/
│   ├── evaluation/
│   │   ├── run_baseline.py          # standard setting
│   │   ├── run_agentic.py           # agentic setting
│   │   └── metrics.py
│   ├── analysis/
│   │   ├── iaa.py
│   │   ├── significance_tests.py
│   │   └── error_analysis.py
│   └── utils/
│
├── experiments/
│   ├── configs/                     # exact prompt/temperature/seed configs, Stage 16
│   └── results/                     # raw model outputs, versioned by date+model version
│
├── notebooks/                       # exploratory only, not source of truth
│
├── paper/
│   ├── iccit_submission.tex
│   ├── figures/
│   └── tables/
│
└── RESULTS.md                       # maps every paper table/figure → exact script + config
```

---

## PART 4 — MILESTONE PLAN AND WEEKLY TIMELINE

Total: ~16 weeks to ICCIT-ready draft (adjust start date to your actual deadline, work backward).

| Week | Stage(s) | Milestone |
|---|---|---|
| 1 | Stage 1–2 | RQ/H frozen, novelty table done |
| 2–3 | Stage 3–4 | Lit review + gap sentence frozen |
| 3 | Stage 5 | Metrics/hypothesis table locked |
| 4 | Stage 6 | Data scope frozen, source access secured |
| 5 | Stage 7 | Taxonomy frozen (pilot-tested) |
| 6–8 | Stage 8 | Raw corpus collection (largest block) |
| 8–9 | Stage 8B | Fabrication generation, batch-approved |
| 9–10 | Stage 9 | Guidelines written + piloted (κ ≥ 0.6) |
| 10–13 | Stage 10 | Full double-annotation |
| 13–14 | Stage 11 | IAA computed, adjudication, gold frozen |
| 14 | Stage 12 | Splits finalized |
| 14–15 | Stage 13–16 | Baselines run (standard + agentic) |
| 15 | Stage 17–18 | Error analysis + significance tests |
| 15–16 | Stage 19–20 | Reproducibility pass + open-source release |
| 13–16 | Stage 21 | Paper writing (parallel, starting week 13) |
| 16 | — | Internal review, submission |

**Critical path:** Stages 6→7→8→8B→9→10→11 are strictly sequential and consume weeks 4–14 — this is 10 of your 16 weeks. Everything else can compress; this cannot.

---

## PART 5 — RISK ASSESSMENT

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Expert annotator unavailability | High | High | Recruit 2 law students + 1 senior adjudicator in week 1, not week 9; have a backup adjudicator identified |
| Low IAA (κ < 0.6) | Medium | High | Pilot round at Stage 9 catches this before full annotation; budget 1 revision cycle |
| DLR/BLC/ALR access/copyright issues | Medium | Medium | Confirm access + copyright status by end of Stage 6, not during Stage 8 |
| OCR errors in scanned judgments | Medium | Medium | Flag OCR-sourced instances; prioritize digitally-native sources first |
| Competing paper published before submission | Low-Medium | High | Repeat Stage 2 novelty check monthly; if a direct competitor appears, pivot to emphasize cross-script contribution (least likely to be scooped) |
| API cost overrun (agentic baselines) | Medium | Low-Medium | Budget explicitly; cut agentic scope per MVP plan if needed |
| Scope creep (adding temporal/amendment task mid-project) | Medium | High | Decision log + Stage 1 freeze; explicitly deferred to journal extension |
| Dataset too small for stable per-category stats | Medium | Medium | Use k-fold rather than fixed split if category counts are low (Stage 12) |

---

## PART 6 — ROADMAP TO IEEE/ACL JOURNAL EXTENSION

The ICCIT paper is intentionally scoped narrow (Part 0.3). The journal version adds exactly the pieces deferred above, in this order of impact:

1. **Temporal/Amendment-Aware Verification** (deferred from Stage 7's category 5) — requires sourcing gazette/amendment records; highest novelty add, highest sourcing cost. Position as "BanLegit-Cite v2."
2. **Scale expansion** — from 4 Acts to full Bangladesh Code coverage; from ~1,000 to 5,000+ instances, enabling fine-tuning experiments (not just zero-shot evaluation), which ICCIT's timeline didn't allow.
3. **Fine-tuned detector model** — train a citation-verification classifier on BanLegit-Cite itself and show it outperforms zero-shot LLM baselines; this is the kind of methodological contribution (not just resource contribution) that ACL/journal venues weight heavily.
4. **Cross-jurisdiction comparison study** — directly compare fabrication error profiles across BanLegit-Cite (BD), LePhantomCite (US), LegalCiteBench (US) under a unified evaluation protocol — turns your resource into a comparative-legal-NLP study, which is a distinct and higher-impact paper.
5. **Human study** — have practicing BD lawyers use an AI citation-checking tool built on your benchmark and measure real task-time reduction, moving from benchmark-only evaluation to human-in-the-loop validation (mirrors LePhantomCite's framing around reducing court burden).

**Sequencing recommendation:** ICCIT paper (Parts 0–21 above) → 6–9 months → journal submission incorporating items 1–3 above as the primary new contributions, with item 4 as a strong secondary result if time permits, item 5 reserved for a follow-up empirical/HCI-adjacent paper.