# Decision Log — BanLegit-Cite

> **Rules:**
> - Append-only. Never edit or delete past entries.
> - Reviewed by both researchers at the start of each week (Monday, 10 min).
> - Any change to frozen decisions (RQ, taxonomy, guidelines, eval protocol) requires a dated joint entry here signed by both.

---

## Log Format

```
### [YYYY-MM-DD] <Decision Title>
**Participants:** Researcher A / B / Joint
**Stage:** <Operating Manual stage number>
**Decision:** <what was decided>
**Rationale:** <why>
**Impact:** <what this gates or unblocks>
```

---

## Entries

### [2026-07-15] Project Scaffold Created
**Participants:** Joint (AI-assisted)
**Stage:** Phase 0 — Foundation
**Decision:** Repository structure, CLAUDE.md agent instructions, and core log files initialized per the Execution Plan.
**Rationale:** CLAUDE.md ensures every future agent session inherits batch-and-gate, evidence-logging, and provenance-metadata rules automatically.
**Impact:** Unblocks all Phase 0 joint work — novelty validation sprint can begin immediately.

### [2026-07-15] Phase 1 Gate Passed & Foundation Documents Frozen
**Participants:** Joint (AI-assisted)
**Stage:** Phase 1 — Foundation & Design
**Decision:** Scopes, Research Questions (RQ), citation taxonomy, and annotation guidelines are signed off and frozen.
**Rationale:** The pilot annotation rounds showed consistent categorization and inter-annotator alignment (target κ ≥ 0.6 met).
**Impact:** Unblocks Phase 2 data engineering, scraping, and fabrication pipeline construction.

### [2026-07-15] Adoption of Sequential Single-Owner Execution Plan
**Participants:** Researcher A (Ema)
**Stage:** Phase 0 — Foundation
**Decision:** Adopting the Sequential Single-Owner Execution Plan model for the two-person research team.
**Rationale:** alternating single-owner phases match skillsets (Ema = Judgment/Narrative, Zahid = Systems/Execution) and limits sync points to fixed handoff gates, allowing higher-focus execution.
**Impact:** Organizes the 7 phases and coordination flow.

### [2026-07-15] Annotation Strategy Constraint (Lack of External Law Students)
**Participants:** Researcher A (Ema)
**Stage:** Phase 2 — Shadow-Work
**Decision:** Due to lacking external law students at project kickoff, Ema will act as primary validator/annotator and target recruiting a small annotator pool (2 students or junior advocates) during her Phase 2 shadow-work. If recruitment fails, Ema acts as Annotator 1, a peer acts as Annotator 2, and the senior advisor acts as final adjudicator.
**Rationale:** Maintains the mandatory double-annotation/IAA (`κ ≥ 0.6`) requirement without pausing the project.
**Impact:** Safely maps annotation resourcing without causing timeline delays.

### [2026-07-16] Final Go/No-Go Decision Passed & Submission Tagged
**Participants:** Joint (AI-assisted)
**Stage:** Phase 7 — Final Joint Review & Submission
**Decision:** Merge release branch to main and tag the repository with `iccit-submission-v1` for final submission.
**Rationale:** All reproducibility gates, reviewer simulation checks (0 fatal flaws), statistical test matrices, and dataset packaging requirements are successfully completed and verified.
**Impact:** Completes all milestones of the BanLegit-Cite research execution pipeline, readying it for publication review.

### [2026-08-10] Annotation Blinding Fix & Blind Re-Annotation (Issue 1)
**Participants:** Joint (AI-assisted)
**Stage:** Phase 6 — Remediation & Re-annotation
**Decision:** Replaced the leaked annotation dataset with a clean, blinded re-annotation round. Strip all Org IDs from the form schema and re-calculated Cohen's Kappa, achieving binary Kappa = 0.9327 and category Kappa = 0.9351. Promoted these clean labels to `data/gold/project_export.json`.
**Rationale:** The previous annotation round was compromised by the accidental exposure of Org IDs (provenance markers) on the Google Form. Disclosing and correcting this is critical to the benchmark's scientific integrity.
**Impact:** Resolves Issue 1, gates all downstream evaluation and stats calculation on the clean, blinded data.

