# BanLegit-Cite: Agentic AI Research Operating Manual
### Human-in-the-Loop Multi-Agent System for a Publication-Grade Benchmark

**Governing principle:** AI agents accelerate execution. The PI (you) makes every decision with research consequence. No agent output is trusted without evidence; no agent claim of "novel" or "gap" is trusted without a citation trail you can independently check.

---

## PART 0 — OPERATING PHILOSOPHY: THE DECISION MATRIX

This is the constitution every agent below is bound by. Read this before anything else — it resolves ambiguity in every stage that follows.

| Category | Rule |
|---|---|
| **AI may decide autonomously** | Formatting of data files, code style, batch sizes for generation, which library to use for a computational step, draft wording of non-claim sentences (e.g., methods-section prose describing a completed step). |
| **AI may recommend, PI decides** | Taxonomy category boundaries, dataset scope (which Acts/courts/date range), which baseline models to run, statistical test selection, paper framing/contribution claims, what to cut under time pressure. |
| **PI decides alone, AI does not recommend** | The core research question and hypotheses (agents may help *articulate* them, never *originate* them — see Novelty Verification Agent limitations below), whether a novelty claim is strong enough to submit, final taxonomy freeze, final gold-label disputes after adjudication, submission go/no-go. |
| **Requires manual verification (PI or human expert), never agent-only** | Every "this citation is real/fake" ground-truth label at the point it enters the gold set; every claim that "no prior work covers X" before it appears in the paper; IAA computation inputs (agent can compute the statistic, PI/adjudicator must confirm the underlying labels are correct); copyright/licensing status of any scraped legal text. |
| **Requires reading the original paper, not an agent summary** | Any paper whose finding directly supports a novelty claim, a metric choice, or a taxonomy design decision (LePhantomCite, LegalCiteBench, BenHalluEval, SG-LegalCite, LeCNet, Dahl et al. 2024, PerHalluEval, Mina). Agent summaries are a triage tool to decide *what* to read, never a substitute for reading it. |
| **Must never be trusted without evidence** | Any agent statement containing "no existing work does X," "this is the first," "this is novel" — these require a citation search transcript attached, not just the claim. Any agent-reported metric without the underlying results file linked. Any agent claim about annotator agreement without the raw annotation data available for spot-check. |

**Standing rule for every agent:** every deliverable must be traceable to either (a) a cited external source, (b) a data artifact in the repo, or (c) an explicit "PI decision, logged on [date]" entry. Anything that fails this test is flagged `UNVERIFIED` and cannot move to the next stage.

---

## PART 1 — THE AGENT TEAM

18 agents, organized into 5 functional clusters. Each spec follows: objective → responsibilities → inputs → outputs → dependencies → limitations → verification method → required evidence → stop-and-escalate condition.

### Cluster A — Planning & Positioning

#### A1. Principal Research Planner (Orchestrator)
- **Objective:** Maintain the master research plan, sequence agent invocations, track stage-gate status.
- **Responsibilities:** Own the dependency graph (Part 6); route outputs between agents; flag when a downstream agent's input prerequisites aren't met; maintain the decision log.
- **Inputs:** Outputs of all other agents; PI decisions.
- **Outputs:** Live project-status dashboard (markdown or lightweight tracker); weekly status summary for PI review.
- **Dependencies:** None — this is the top-level coordinator.
- **Limitations:** Cannot resolve scientific disagreements between agents (e.g., Novelty Agent vs. Gap Agent disagreeing on framing) — must escalate to PI, not adjudicate itself.
- **Verification method:** PI reviews weekly status summary against actual repo state (spot-check that claimed progress matches committed artifacts).
- **Required evidence:** Every "stage complete" flag must link to the actual exit-criteria artifact.
- **Stop-and-escalate:** Any time two agents produce contradictory outputs; any time a stage's exit criteria (Part 4) aren't met but the plan pressures moving forward anyway.

#### A2. Literature Review Agent
- **Objective:** Build and maintain the annotated bibliography and literature map.
- **Responsibilities:** Search arXiv/ACL Anthology/Semantic Scholar for relevant papers across the four clusters (legal hallucination, South Asian legal NLP, hallucination-benchmark methodology, RAG/agentic verification); extract structured metadata (task, dataset size, language, jurisdiction, metric, key finding) per paper; flag papers the PI must read in full vs. those adequately covered by abstract.
- **Inputs:** Search keywords from PI/Planner; existing bibliography.
- **Outputs:** Structured literature spreadsheet; monthly "new papers since last check" digest (mandatory recurring task through submission, per Stage 2's repeat-check requirement).
- **Dependencies:** None to start; refined by Novelty Verification Agent's findings.
- **Limitations:** Cannot judge which papers are "close enough to be a competing gap" — that's the Novelty Agent's job, using this agent's raw output as input. Search coverage is only as good as keyword design — PI must review and expand keyword lists periodically.
- **Verification method:** PI spot-checks 10% of entries against the actual paper (not just the agent's extracted summary) each month.
- **Required evidence:** Every spreadsheet row must include the source URL and the exact sentence(s) supporting each extracted field.
- **Stop-and-escalate:** If a paper appears that plausibly overlaps with your specific gap (Bangladeshi legal citation fabrication) — immediately flag to PI, do not wait for the monthly digest.

#### A3. Novelty Verification Agent
- **Objective:** Formally test whether the stated contribution is not already covered by existing work.
- **Responsibilities:** Given the PI's draft gap statement, actively search for counter-evidence (papers that might already do this); build the competing-work comparison table (task/dataset/language/jurisdiction/taxonomy/best-score per competitor); explicitly attempt to falsify the novelty claim rather than confirm it.
- **Inputs:** Literature Review Agent's bibliography; PI's draft RQ/gap statement.
- **Outputs:** Novelty Validation Report — a table plus a written adversarial case ("here is the strongest argument this is NOT novel, and here is why it doesn't hold").
- **Dependencies:** A2 must be reasonably mature first.
- **Limitations:** **This agent must never itself declare something "novel."** It only reports "no counter-evidence found in the following N sources, searched with the following queries, on [date]." The PI makes the novelty judgment. This is a hard constraint — an agent asserting novelty is exactly the failure mode this manual exists to prevent.
- **Verification method:** PI reads the top 3–5 flagged "closest competitor" papers in full before accepting the report.
- **Required evidence:** Full search query log; every competitor entry cited to the specific claim/table/sentence in the source paper (as done in the comparison table built earlier in this project).
- **Stop-and-escalate:** Any time a paper is found with >70% task/scope overlap — halt, do not let the Planner proceed to Stage 4 until PI reviews.

#### A4. Research Gap Agent
- **Objective:** Convert the Novelty Verification Report into a precise, defensible one-sentence gap statement.
- **Responsibilities:** Draft candidate gap sentences; stress-test each against the competitor table (does any competitor already satisfy this exact sentence?); flag overclaiming language ("no work exists on X" when a narrower true claim is safer).
- **Inputs:** A3's report.
- **Outputs:** 2–3 candidate gap-sentence drafts with a devil's-advocate rebuttal attached to each.
- **Dependencies:** A3 complete.
- **Limitations:** Cannot originate the underlying research direction — only sharpens phrasing of a direction the PI has already chosen.
- **Verification method:** PI selects/edits final sentence; logs the decision.
- **Required evidence:** Each candidate sentence traceable to specific rows of A3's table.
- **Stop-and-escalate:** If no candidate survives the devil's-advocate test without modification — return to A3/PI rather than shipping a weak sentence.

### Cluster B — Design

#### B1. Benchmark Design Agent
- **Objective:** Translate the RQ/hypotheses into formal task definitions, splits strategy, and metric choices.
- **Responsibilities:** Propose task set (binary detection / category classification / cross-script robustness); propose split strategy (stratified vs. k-fold given expected corpus size); propose metrics mapped to each hypothesis (as in the H1–H3 → metric table established earlier).
- **Inputs:** Locked RQ/H1–H3 (PI-owned); structural templates from competitor benchmarks (via A2).
- **Outputs:** Draft benchmark specification document.
- **Dependencies:** A4 gap statement finalized; RQ/H frozen by PI.
- **Limitations:** Cannot decide the actual RQ; can only design the measurement apparatus around it.
- **Verification method:** PI checks each task/metric traces back to a specific hypothesis — no orphan tasks that don't answer anything.
- **Required evidence:** Mapping table: hypothesis → task → metric → statistical test.
- **Stop-and-escalate:** If any hypothesis has no clean corresponding metric — flag before dataset collection begins, not after.

#### B2. Citation Taxonomy Agent
- **Objective:** Draft the fabrication-category taxonomy (statutory + precedent super-categories).
- **Responsibilities:** Propose category definitions extending LePhantomCite's five-category scheme to the statute/precedent duality; draft the decision tree; surface likely category-overlap edge cases for PI review; propose 2–3 worked examples per category once real source text exists (coordinates with Data Collection Agent).
- **Inputs:** A2/A3 competitor taxonomies (as direct structural templates); Data Collection Agent's raw corpus for real examples.
- **Outputs:** Draft taxonomy document + decision tree diagram.
- **Dependencies:** Benchmark scope frozen (B1); raw corpus at least partially available for realistic examples.
- **Limitations:** Cannot resolve category-overlap ambiguity alone — that requires the pilot annotation round (human judgment), not agent judgment.
- **Verification method:** Pilot annotation round with two independent human annotators; Cohen's κ ≥ 0.6 required before taxonomy is accepted (agent cannot self-certify its own taxonomy).
- **Required evidence:** Pilot round results (raw annotations, computed κ) attached to the taxonomy-freeze decision.
- **Stop-and-escalate:** Pilot κ < 0.6 → returns to this agent for revision, does not proceed to full annotation.

#### B3. Dataset Discovery Agent
- **Objective:** Identify and catalog exact source repositories for statutes and case law before collection begins.
- **Responsibilities:** Locate bdlaws.minlaw.gov.bd structure, Bangladesh Supreme Court digest access points, DLR/BLC/ALR access routes (library/institutional); document access method, format (HTML/PDF/scanned), estimated coverage density by year; flag copyright status per source type.
- **Inputs:** Locked scope (Acts, courts, date range) from PI.
- **Outputs:** Source catalog with access instructions, format notes, copyright flags per source.
- **Dependencies:** Scope frozen (Stage 6 equivalent).
- **Limitations:** Cannot secure institutional access itself (e.g., a law-library DLR subscription) — that is a PI action item, flagged explicitly by this agent as a blocker.
- **Verification method:** PI or a delegated team member manually confirms access to each flagged source before Data Collection Agent begins scraping.
- **Required evidence:** Screenshot/log confirming successful access per source; explicit copyright-status note per source (public domain vs. commercial reporter).
- **Stop-and-escalate:** Any source with unclear or restrictive copyright status — escalate before any scraping of that source occurs, not after.

### Cluster C — Data Construction

#### C1. Data Collection Agent
- **Objective:** Execute scraping/extraction of source text per B3's catalog and B1/scope constraints.
- **Responsibilities:** Run scrapers/PDF extractors/OCR pipelines; attach provenance metadata (source URL, retrieval date, OCR-flag) to every instance; deduplicate; run automated format-validity checks.
- **Inputs:** B3's source catalog.
- **Outputs:** Raw corpus (target 1,200–1,500 instances, per earlier buffer plan) with full provenance metadata.
- **Dependencies:** B3 complete, access confirmed by PI.
- **Limitations:** Cannot judge whether an extracted citation is *substantively correct* (that's a legal-content judgment) — only whether it's *structurally well-formed* and *correctly attributed to its stated source*.
- **Verification method:** PI/team spot-checks a random 5% sample of raw extractions against the original source document directly.
- **Required evidence:** Provenance metadata complete for 100% of instances; spot-check pass rate ≥95% before corpus is accepted.
- **Stop-and-escalate:** Spot-check failure rate >5% — halt collection, diagnose the extraction pipeline before continuing (likely an OCR or parsing bug, not a one-off error).

#### C2. Fabrication Generation Agent
- **Objective:** Generate the fabricated half of the dataset, conditioned on real citations, per taxonomy category.
- **Responsibilities:** Batch-generate fabricated instances (50–100/batch) using explicit category-conditioned prompts (following the BenHalluEval-style generation-prompt pattern); attach category label + generation metadata (model version, prompt version, batch ID) to every instance.
- **Inputs:** C1's raw corpus; B2's taxonomy; PI-approved generation prompts.
- **Outputs:** Fabricated instance batches, submitted for review before advancing to the next batch.
- **Dependencies:** C1 and B2 complete.
- **Limitations:** **Cannot self-approve its own output.** Every batch requires human spot-check before the next batch is generated (the batch-and-gate workflow established earlier in this project) — this is a hard architectural constraint, not a suggestion.
- **Verification method:** PI or trained reviewer checks a fixed percentage of each batch (recommend ≥20% for the first 5 batches per category, reducible to 10% once a category shows consistent quality) for: (a) plausibility — is it a realistic fabrication a model might actually produce? (b) non-triviality — is it not so obviously fake it trivializes the task? (c) accidental-truth check — did generation accidentally produce a real citation?
- **Required evidence:** Batch approval log with reviewer ID, date, sample reviewed, pass/fail, and specific rejection reasons for failed batches.
- **Stop-and-escalate:** Batch rejection rate >10% for a category — stop generating that category, escalate to PI/B2 to revise the category definition or generation prompt before resuming.

#### C3. Annotation Guideline Agent
- **Objective:** Draft the full annotation guideline document.
- **Responsibilities:** Structure the guideline (task overview → decision tree → worked examples → edge-case FAQ); draft worked examples using real C1/C2 instances; maintain version numbers across revisions.
- **Inputs:** B2 taxonomy; C1/C2 sample instances.
- **Outputs:** Versioned guideline document.
- **Dependencies:** B2 taxonomy pilot-passed.
- **Limitations:** Cannot itself annotate the full dataset — guideline authorship and gold-label production must stay separated to avoid circular validation (an agent that wrote the rules shouldn't also be the sole judge of applying them).
- **Verification method:** Same pilot-round requirement as B2 (κ ≥ 0.6) — guideline and taxonomy are validated together in practice.
- **Required evidence:** Pilot annotation results per guideline version.
- **Stop-and-escalate:** Same as B2.

#### C4. Legal Citation Validator
- **Objective:** Cross-check individual citation instances against authoritative sources at annotation time — a fact-checking assistant to human annotators, not a replacement for them.
- **Responsibilities:** Given a citation string, attempt to verify it against the indexed raw corpus / known statute structure (e.g., "does Penal Code have a §XXX?"); surface a confidence flag and supporting/contradicting evidence to the human annotator; never issue a final real/fake label itself.
- **Inputs:** Individual citation instances during annotation; indexed statute/case corpus from C1.
- **Outputs:** Per-instance evidence summary (e.g., "Section 376 found in Penal Code source text, retrieved [date], link: [x]" or "no matching section found in indexed corpus").
- **Dependencies:** C1 corpus indexed and searchable.
- **Limitations:** Can only check against what's in the indexed corpus — a true positive it can't find (e.g., a real citation from a source outside your Stage-6 scope) will incorrectly read as "unverified," not "fake." Annotators must be explicitly trained on this failure mode.
- **Verification method:** This agent's flags are advisory inputs to human annotation, cross-checked during Stage 11 adjudication whenever the agent's flag and the human label disagree.
- **Required evidence:** Every flag includes the exact source passage it matched or failed to match against.
- **Stop-and-escalate:** High disagreement rate between this agent's flags and final human labels (>15%) on any category — signals either indexing gaps or a taxonomy ambiguity; escalate to PI.

#### C5. Quality Assurance / IAA Agent
- **Objective:** Compute inter-annotator agreement and manage the disagreement-adjudication queue.
- **Responsibilities:** Compute Cohen's/Fleiss' κ overall and per-category from the double-annotation data; generate the disagreement queue for the senior adjudicator; track adjudication decisions; produce the final QA report.
- **Inputs:** C1/C2 instances with two independent human annotation passes.
- **Outputs:** IAA report (overall + per-category κ); disagreement queue; post-adjudication gold-label file.
- **Dependencies:** Full double-annotation pass complete (human effort, Stage 10 equivalent).
- **Limitations:** Purely computational — cannot adjudicate disagreements itself; that is reserved for the human senior legal expert exclusively (Part 0 rule: ground-truth labels always require manual verification).
- **Verification method:** PI reviews the IAA report; confirms adjudicator's decisions are logged with reasoning, not just a final label.
- **Required evidence:** Raw annotation data underlying every κ score must remain accessible for audit, not just the summary statistic.
- **Stop-and-escalate:** Overall κ < 0.6, or any single category's κ < 0.5 — halt progression to Stage 12 (benchmark construction) until re-guideline/re-pilot cycle resolves it.

### Cluster D — Experimentation

#### D1. Experiment Design Agent
- **Objective:** Formalize the experimental protocol (Stage 16 equivalent): prompts, temperature, seeds, run counts, exact model versions.
- **Responsibilities:** Draft prompt templates for standard and agentic settings; specify determinism settings (temp=0 primary + repeated-run variance check); lock model version/date documentation requirements.
- **Inputs:** B1 benchmark spec; C-cluster gold dataset.
- **Outputs:** Experimental protocol document + versioned prompt files.
- **Dependencies:** Gold dataset frozen (C5 exit criteria met), benchmark splits finalized.
- **Limitations:** Cannot decide which models are "worth" testing under budget constraints — that's a PI resourcing decision.
- **Verification method:** PI approves prompt wording before any baseline run begins (prompt wording materially affects results and must be a deliberate, reviewed choice, not agent-improvised).
- **Required evidence:** Protocol document exists and is version-controlled *before* Baseline Research Agent executes anything.
- **Stop-and-escalate:** If protocol changes are proposed mid-experiment — must restart the affected runs under the new protocol, never silently mix protocol versions within one results table.

#### D2. Baseline Research Agent
- **Objective:** Execute baseline model runs (standard + agentic settings) per D1's locked protocol.
- **Responsibilities:** Run ≥4 models (mix of closed/open/Bangla-centric) under both settings; log raw outputs, costs, failures; assemble the results matrix (model × setting × category).
- **Inputs:** D1 protocol, C-cluster splits.
- **Outputs:** Raw results files (one per run, timestamped, config-linked) + assembled results matrix.
- **Dependencies:** D1 complete.
- **Limitations:** Cannot interpret results (that's D3/D4's job) — only executes and reports raw numbers; cannot silently drop failed/crashed runs from the matrix without flagging them.
- **Verification method:** PI/Planner spot-checks that reported scores are computed from the actual logged raw outputs, not agent-summarized numbers with no backing file.
- **Required evidence:** Every cell in the results matrix links to a specific raw-output file and exact config.
- **Stop-and-escalate:** Any model producing implausible results (e.g., 0% or 100% on a non-trivial task) — flag for manual inspection of the run before including it in the paper.

#### D3. Statistical Analysis Agent
- **Objective:** Run the pre-registered significance tests (Stage 18) against H1–H3.
- **Responsibilities:** Execute paired bootstrap/permutation tests per the metrics table locked in Stage 5/B1; compute effect sizes and 95% CIs; verify test assumptions (e.g., pairing validity for the cross-script matched design) before running.
- **Inputs:** D2's results matrix; Stage 5's pre-registered hypothesis→test mapping.
- **Outputs:** Statistical results report (effect size, CI, p-value per hypothesis).
- **Dependencies:** D2 complete.
- **Limitations:** Must use only the pre-registered tests from Stage 5 — cannot select a different test post-hoc because it produces a more favorable result (this is a hard-coded constraint, not a judgment call left to the agent).
- **Verification method:** PI confirms the test used matches the Stage 5 pre-registration exactly; any deviation requires a logged justification, not silent substitution.
- **Required evidence:** Test code + raw inputs + outputs all linked in the repo.
- **Stop-and-escalate:** If a pre-registered test's assumptions are violated by the actual data (e.g., matched pairs turn out incomplete) — escalate rather than substitute a different test silently.

#### D4. Result Interpretation Agent
- **Objective:** Translate statistical outputs into plain-language findings tied explicitly to H1–H3, and conduct structured error analysis.
- **Responsibilities:** Draft the Results and Error Analysis sections' factual content (not the polished prose — that's the Scientific Writing Agent); pull a stratified random sample of errors (not cherry-picked) for qualitative review; propose 8–12 illustrative examples per the earlier error-analysis plan.
- **Inputs:** D3's statistical report, D2's raw outputs.
- **Outputs:** Draft findings summary + candidate error examples with categorized failure patterns.
- **Dependencies:** D3 complete.
- **Limitations:** Cannot cherry-pick examples that only support hypotheses — must show the full stratified sample to the PI, not a pre-filtered "best evidence" set.
- **Verification method:** PI reviews the full stratified sample (not just the selected illustrative examples) to confirm the selected examples are representative, not cherry-picked.
- **Required evidence:** The complete stratified sample (all ~50 reviewed errors, per the earlier plan), not only the ones that made it into the paper.
- **Stop-and-escalate:** If findings contradict a hypothesis — report this plainly, do not reframe the hypothesis after the fact to fit the data (classic p-hacking risk flagged for PI attention).

### Cluster E — Writing & Review

#### E1. Scientific Writing Agent
- **Objective:** Draft the paper following the locked structure (Stage 21).
- **Responsibilities:** Draft each section from the corresponding stage's verified artifacts (Related Work from A2/A3/A4 outputs, Methods from B/C-cluster docs, Results from D-cluster reports); maintain citation accuracy; flag any claim it cannot trace to an artifact.
- **Inputs:** All prior agent outputs + PI decisions/decision log.
- **Outputs:** Full paper draft, section by section, ideally started early and updated incrementally (per the earlier "don't wait until all experiments finish" guidance).
- **Dependencies:** Rolling — each section depends on its corresponding stage being complete.
- **Limitations:** **Cannot invent a claim not backed by an artifact.** Every sentence containing a number, a comparison to prior work, or a novelty assertion must have a traceable source; if none exists, the agent must output a placeholder flag (e.g., `[CLAIM NEEDS SOURCE — PI REVIEW]`) rather than write plausible-sounding unsupported prose.
- **Verification method:** PI (and ideally a co-author) reads the full draft against the artifact trail before any submission-track review.
- **Required evidence:** A claim-to-artifact mapping for the full paper, not just for contested sections.
- **Stop-and-escalate:** Any section where more than ~10% of claims lack a traceable artifact — do not proceed to Reviewer Simulation until resolved.

#### E2. Reviewer Simulation Agent
- **Objective:** Adversarially review the draft as an ICCIT PC member would, at every milestone (not just at the end).
- **Responsibilities:** At each milestone (Part 5 below), answer the five standing reviewer questions; specifically hunt for unsupported novelty claims, weak IAA reporting, missing baselines, insufficient statistical rigor, and reproducibility gaps.
- **Inputs:** Current state of the paper draft + underlying artifacts.
- **Outputs:** A structured review report per milestone, formatted like an actual reviewer's comments (strengths / weaknesses / questions / recommendation).
- **Dependencies:** Runs recurrently, triggered at every milestone in Part 5, not just once before submission.
- **Limitations:** Cannot guarantee it catches everything a real reviewer would — it is a risk-reduction tool, not a substitute for actual pre-submission peer feedback from colleagues, which the PI must still separately arrange.
- **Verification method:** PI treats every "would reject because..." flag as mandatory to address or explicitly accept as a known limitation before submission (logged, not silently ignored).
- **Required evidence:** Each critique must reference the specific section/claim/table it applies to.
- **Stop-and-escalate:** Any critique in the "fatal flaw" category (fabricated/unverifiable novelty claim, missing IAA, no significance testing) blocks submission until resolved — this agent has veto power over the submit action, exercised by informing the PI, who then acts on it.

---

## PART 2 — EVIDENCE-BASED RESEARCH PROTOCOL (Cross-Cutting Rule Set)

Applies to every agent above, at every stage:

1. **Citation requirement:** Any comparative or novelty claim must cite the specific paper + specific sentence/table/finding, not just "prior work suggests."
2. **Comparison requirement:** When two methods/papers could both apply, the agent must present both and note the tradeoff — never silently pick one and hide the alternative.
3. **Contradiction surfacing:** If two sources disagree (e.g., one paper claims agentic verification helps, another shows marginal gains), the agent must flag the contradiction explicitly, not average it away.
4. **Fact vs. assumption labeling:** Every agent output distinguishes `[VERIFIED FACT — source: X]`, `[AGENT INFERENCE — not directly sourced]`, and `[PI DECISION REQUIRED]`. This labeling is mandatory in all deliverables, not optional formatting.
5. **No invented gaps:** Per Part 0, an agent may report "I found no counter-evidence in N searched sources" — it may never report "this is a research gap" as a conclusion. Only the PI concludes that.
6. **No invented citations:** Any agent-generated bibliography entry must resolve to a real, checkable URL/DOI. An agent that cannot find a source for a claim must flag the claim as unsupported, not fabricate a plausible-looking citation.

---

## PART 3 — STAGE-BY-STAGE AGENTIC WORKFLOW

Compact form — full implementation detail (papers, tools, timelines) is in the companion document `BanLegit-Cite_Research_Roadmap.md`; this table adds the agent/approval/evidence layer on top of that plan.

| Stage | Objective | Primary Agents | PI Role / Approval Checkpoint | Evidence Required Before Proceeding | Exit Criteria | Key Risk |
|---|---|---|---|---|---|---|
| 1. Problem Formulation | Lock RQ + H1–H3 | A1 (facilitates), PI originates | PI writes/owns RQ; agents only help phrase it | None — this is PI-original | RQ/H frozen in decision log | Agent-suggested RQ mistaken for PI-original (must avoid) |
| 2. Novelty Validation | Confirm gap is real | A2, A3 | PI reads top 3–5 flagged competitor papers in full | Full search-query log + competitor table | PI signs off novelty table | Overclaiming ("first ever") without full search coverage |
| 3. Literature Review | Build full bibliography | A2 | PI spot-checks 10%/month | Source-linked spreadsheet | ≥25–40 papers catalogued across 4 clusters | Shallow abstract-only reading |
| 4. Research Gap | One-sentence gap statement | A4 | PI selects/edits final wording | Devil's-advocate rebuttal per candidate | Gap sentence frozen | Vague/unfalsifiable phrasing |
| 5. RQ/Hypotheses (final) | Metric-linked H1–H3 | B1 (formalizes) | PI approves metric-to-hypothesis mapping | Mapping table complete | Pre-registered before any data collection | Metrics chosen post-hoc |
| 6. Dataset Scope | Lock Acts/courts/date range | B1, B3 | PI approves scope doc; confirms institutional access | Access-confirmation evidence per source | Scope doc frozen | Starting collection before scope locked |
| 7. Citation Taxonomy | Category scheme | B2, C3 | PI reviews pilot κ | Pilot round data (κ ≥ 0.6) | Taxonomy + guideline frozen together | Category overlap undetected until full annotation |
| 8. Data Collection | Raw corpus assembly | C1 | PI/team spot-checks 5% sample | Provenance metadata 100% complete | ≥95% spot-check pass rate | Silent OCR/parsing errors |
| 8B. Fabrication Generation | Generate fake half | C2 | PI/reviewer approves each batch (≥20% sampled) | Batch approval log | All categories batch-approved, <10% rejection | Ungated bulk generation |
| 9. Annotation Guidelines | Guideline doc | C3 | Same pilot-κ gate as Stage 7 | Pilot annotation data | κ ≥ 0.6 on pilot | Guidelines untested on independent annotator |
| 10. Annotation Workflow | Full double-annotation | C4 (advisory), human annotators | PI ensures 100% double-annotation coverage (non-negotiable for legal ground truth) | Two independent passes per instance | All instances annotated | Single-annotation shortcut |
| 11. QA / IAA | Compute agreement, adjudicate | C5 | PI reviews adjudicator's logged reasoning, not just final labels | Raw annotation data + adjudication log | κ ≥ 0.6 overall, ≥0.5 per category | Hiding low per-category κ behind good overall κ |
| 12. Benchmark Construction | Splits, packaging | B1 | PI approves split strategy | Per-category counts per split | Splits frozen, checksummed | Random (non-stratified) splitting |
| 13. Baseline Systems | Run models | D1, D2 | PI approves prompt wording before runs | Protocol doc pre-dated before runs | Full results matrix, no silently dropped runs | Prompt changed mid-experiment |
| 14. Tasks (formal) | Lock 3 task definitions | B1 | PI confirms each task maps to a hypothesis | Hypothesis-task-metric table | No orphan tasks | Adding tasks that don't answer anything |
| 15. Evaluation Metrics | Precision/Recall/F1/macro-F1/paired delta | B1, D3 | PI approves metric choices pre-registered | Metric spec doc | Metrics computed for all cells | Reporting accuracy only on imbalanced classes |
| 16. Experimental Protocol | Fix temp/seed/prompts | D1 | PI approves before D2 executes | Version-controlled protocol file | Protocol frozen pre-execution | Undocumented ad hoc prompt tweaks |
| 17. Error Analysis | Qualitative failure review | D4 | PI reviews full stratified sample, not just picks | Full ~50-error sample available | Patterns linked explicitly to H1–H3 | Cherry-picked confirming examples |
| 18. Statistical Testing | Pre-registered tests | D3 | PI confirms test matches Stage 5 registration | Test code + raw I/O | Effect size + CI per hypothesis | Post-hoc test switching |
| 19. Reproducibility | Full artifact trail | A1 (coordinates), all agents | PI/colleague dry-run reproduction of main table | Pinned versions, seeds, prompts, configs | Independent reproduction succeeds | Prose-only methodology description |
| 20. Open-Source Release | Publish data + code | A1 (coordinates) | PI confirms copyright/licensing status per source | Per-source copyright determination | Public repo + DOI live | Releasing copyrighted reporter text |
| 21. Paper Writing | Full draft | E1 | PI/co-author full read against artifact trail | Claim-to-artifact map | <10% unsupported claims, resolved | Plausible-sounding unsupported prose |
| 22. Reviewer Simulation | Adversarial pre-review | E2 | PI resolves/logs every "fatal flaw" flag | Structured review report | No unresolved fatal-flaw flags | Ignoring simulated rejection reasons |
| 23. Final Submission | Go/no-go | PI alone | **PI decision, not delegable** | Full checklist below (Part 5) passed | Submitted | Submitting with open fatal-flaw flags |

---

## PART 4 — HUMAN-IN-THE-LOOP WORKFLOW SUMMARY

Restating Part 0 as an operational checklist, organized by *when* in the pipeline it applies:

**Before data collection starts:** PI has personally verified — not delegated — the Stage 6 scope document, institutional access to DLR/BLC/ALR, and copyright status of every source (B3 flags, PI confirms).

**Before annotation starts:** PI has personally reviewed the pilot round's raw disagreement cases (not just the κ number) for Stage 7/9.

**Before any label enters the gold set:** Confirmed by a human (annotator + adjudicator), never accepted from C4 (Legal Citation Validator) alone — C4 is advisory only.

**Before any baseline run:** PI has approved the exact prompt text in D1's protocol document.

**Before any claim enters the paper:** E1 has produced a claim-to-artifact trace; PI has spot-checked it.

**Before submission:** PI has personally read the full draft, resolved every E2 fatal-flaw flag, and made the final go/no-go call alone.

---

## PART 5 — REVIEWER SIMULATION PROTOCOL (Recurring, Not One-Time)

Trigger the Reviewer Simulation Agent (E2) at **five checkpoints**, not just before submission:

| Checkpoint | Trigger | Standard Questions Asked |
|---|---|---|
| After Stage 4 (gap frozen) | Gap sentence finalized | Is this gap real or a reframing of existing work? What's the strongest counter-paper? |
| After Stage 11 (gold set frozen) | IAA computed | Is IAA high enough to trust the ground truth? Are rare categories underrepresented? |
| After Stage 13 (baselines run) | Results matrix complete | Are the baselines strong enough (SOTA models included)? Is any result suspiciously trivial (near 0% or 100%)? |
| After Stage 18 (stats done) | Hypotheses tested | Is the statistical test appropriate for the pairing structure? Are effect sizes reported, not just p-values? |
| Before Stage 23 (submission) | Full draft complete | The full five-question battery below, on the complete paper. |

**Standard five-question battery (run in full at the final checkpoint, run partially at earlier ones):**
1. What evidence is still missing?
2. What assumptions remain unvalidated?
3. What experiments are still required?
4. What could cause rejection?
5. What should be improved before proceeding?

**Non-negotiable fatal-flaw categories** (any one of these blocks Stage 23 go/no-go until resolved):
- A novelty claim with no attached search-evidence trail.
- Missing or unreported IAA for any gold-label category.
- No statistical significance testing behind a headline empirical claim (H1/H2/H3).
- No open-weight baseline included (reproducibility concern reviewers routinely raise).
- Any claim traceable to "agent inference" rather than "verified fact" appearing in the paper without a `[PI DECISION REQUIRED]` resolution logged.

---

## PART 6 — RESEARCH MANAGEMENT INFRASTRUCTURE

### 6.1 Dependency Graph (text form)

```
Stage 1 (RQ/H) 
  └─> Stage 2 (Novelty) ──> Stage 3 (Lit Review) ──> Stage 4 (Gap)
        └─> Stage 5 (Final RQ/H, metric-linked)
              └─> Stage 6 (Scope) ──> Stage 7 (Taxonomy) ──> Stage 8 (Collection)
                                                                └─> Stage 8B (Fabrication)
                                                                      └─> Stage 9 (Guidelines)
                                                                            └─> Stage 10 (Annotation)
                                                                                  └─> Stage 11 (QA/IAA)
                                                                                        └─> Stage 12 (Benchmark)
                                                                                              └─> Stage 13 (Baselines) ──┬─> Stage 14 (Tasks, formal)
                                                                                                                          ├─> Stage 15 (Metrics)
                                                                                                                          └─> Stage 16 (Protocol)
                                                                                                                                └─> Stage 17 (Error Analysis)
                                                                                                                                      └─> Stage 18 (Stats)
                                                                                                                                            └─> Stage 19 (Reproducibility)
                                                                                                                                                  └─> Stage 20 (Open-Source)
                                                                                                                                                        └─> Stage 21 (Writing, starts earlier in parallel)
                                                                                                                                                              └─> Stage 22 (Reviewer Sim)
                                                                                                                                                                    └─> Stage 23 (Submission)
```

Critical path: Stage 6 → 11 is strictly sequential (matches the earlier roadmap's 10-week critical block). Stage 21 (writing) should start as early as Stage 4/7, running in parallel — not sequenced at the end.

### 6.2 GitHub Repository Structure (extends the prior structure with agent infrastructure)

```
banlegit-cite/
├── README.md
├── LICENSE
├── decision_log.md                    # every PI decision, dated, with rationale
├── operating_manual.md                # this document
│
├── agents/
│   ├── configs/                       # per-agent prompt/config files, versioned
│   │   ├── A2_literature_review.yaml
│   │   ├── B2_taxonomy.yaml
│   │   ├── C2_fabrication_generation.yaml
│   │   └── ...
│   ├── logs/                          # every agent invocation logged: input, output, timestamp
│   └── approval_records/              # PI approval checkpoints, one file per checkpoint
│
├── data/  (as previously specified: raw/ fabricated/ annotated/ gold/ splits/)
├── annotation/  (guidelines, decision tree, pilot round results + κ)
├── generation/  (prompts/ batch_logs/ with approval status per batch)
├── src/  (data_collection/ fabrication_generation/ evaluation/ analysis/ utils/)
├── experiments/  (configs/ results/, D1/D2 outputs)
│
├── literature/
│   ├── bibliography.csv               # A2's structured output
│   ├── novelty_report.md              # A3's adversarial report
│   └── monthly_digests/               # recurring competitor-check logs
│
├── reviews/
│   ├── milestone_1_gap_review.md      # E2 outputs per Part 5 checkpoint
│   ├── milestone_2_iaa_review.md
│   ├── milestone_3_baseline_review.md
│   ├── milestone_4_stats_review.md
│   └── final_submission_review.md
│
├── paper/  (tex, figures, tables)
└── RESULTS.md
```

### 6.3 Research Log Structure

One entry per work session, appended (never edited retroactively — corrections are new entries referencing the original):
```
[DATE] [STAGE] [AGENT(S) INVOLVED] 
Action taken:
Output produced (link):
PI review status: [approved / rejected / pending]
Notes/deviations from plan:
```

### 6.4 Decision Log Structure

Separate from the research log — only PI-level decisions with research consequence:
```
[DATE] DECISION: [what was decided]
CONTEXT: [why this came up]
OPTIONS CONSIDERED: [what alternatives existed, per agent recommendations]
RATIONALE: [why this option]
REVERSIBLE: [yes/no — if no, flag as high-stakes]
```

### 6.5 Literature Database Structure

CSV/table schema (A2's primary output):
```
paper_id | title | authors | year | venue | url | task | dataset_size | language | jurisdiction | 
taxonomy_categories | best_model_score | relevance_score(1-5) | full_read_status(abstract/full) | 
key_quote | key_quote_location
```

### 6.6 Benchmark Versioning Strategy

Semantic versioning applied to the dataset itself, not just code:
- **v0.x** — pilot/internal versions during taxonomy and guideline development, never released externally.
- **v1.0** — ICCIT submission version, frozen at Stage 11 exit, immutable once submitted (create a new version rather than editing v1.0 post-submission).
- **v1.x** — minor corrections (e.g., a confirmed mislabeled instance found post-publication) documented in a CHANGELOG, original version preserved for reproducibility of the published paper's exact numbers.
- **v2.0** — journal-extension version incorporating temporal/amendment-aware data (Part 6 of the companion roadmap document) — a materially larger scope, justifying a major version bump.

Each version gets a Zenodo DOI; the paper cites the exact DOI'd version, not a moving "latest" link.

---

## PART 7 — RESEARCH GOVERNANCE PROTOCOL

| Governance Area | Protocol |
|---|---|
| **Reproducibility** | Every result traces to a config file + pinned model version/date + seed. No result enters the paper without this trail (enforced by D2/D3 evidence requirements above). |
| **Transparency** | Agent vs. human authorship is labeled throughout (`[AGENT DRAFT]` vs `[PI VERIFIED]`) internally; the paper itself should include a brief methodology note on AI-assisted workflow use, per increasingly standard venue disclosure norms — check ICCIT's current author-guidelines for AI-use disclosure requirements before submission. |
| **Version Control** | All code, prompts, configs, and taxonomy/guideline documents in git, with meaningful commit messages tied to stage/agent. Data versioned separately per 6.6. |
| **Experiment Traceability** | RESULTS.md maps every paper table/figure to its exact generating script + config + data version — maintained continuously, not reconstructed at the end. |
| **Benchmark Integrity** | Test set never used for prompt-tuning or model selection during baseline development (a held-out blind test set, touched only for final reported numbers, per Stage 12). |
| **Annotation Consistency** | 100% double-annotation, formal IAA reporting per category, adjudication log preserved — never summarized away. |
| **Ethical Data Usage** | Copyright status confirmed per source before release (Stage 20); no PII beyond what's already in public judicial records; no release of full commercial-reporter text, only citation metadata + fair-use-length excerpts. |
| **Scientific Rigor** | Pre-registered hypotheses and tests (Stage 5/18) — no post-hoc metric or test switching; stratified, non-cherry-picked error analysis (Stage 17); adversarial novelty checking (A3) rather than confirmatory. |

---

## PART 8 — QUICK-REFERENCE SUBMISSION CHECKLIST

Before Stage 23 go/no-go, PI confirms all of the following are true:

- [ ] Novelty claim has a full search-evidence trail (A3), and PI has read the top competing papers directly.
- [ ] Gap sentence survives devil's-advocate rebuttal (A4).
- [ ] Taxonomy and guidelines passed pilot at κ ≥ 0.6 (B2/C3).
- [ ] 100% double-annotation completed; IAA ≥ 0.6 overall, ≥ 0.5 per category (C5).
- [ ] Gold labels adjudicated by a human legal expert, with reasoning logged.
- [ ] Splits stratified, blind test set untouched during development (Stage 12).
- [ ] ≥4 baseline models including at least one open-weight model, both standard and agentic settings (D2).
- [ ] Pre-registered statistical tests run exactly as specified in Stage 5 (D3).
- [ ] Error analysis based on a full stratified sample, not cherry-picked (D4).
- [ ] Every paper claim traced to an artifact; no unresolved `[CLAIM NEEDS SOURCE]` flags (E1).
- [ ] All five Reviewer Simulation checkpoints run; no unresolved fatal-flaw flags (E2).
- [ ] Reproducibility dry-run completed by someone other than the primary author.
- [ ] Copyright/licensing confirmed for every released data source.
- [ ] Decision log and research log complete and internally consistent with the actual repo state.

**This checklist is the actual final gate. If any box is unchecked, the submission decision is not ready — regardless of deadline pressure.**