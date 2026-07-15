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

### [2026-07-16] Final Go/No-Go Decision Passed & Submission Tagged
**Participants:** Joint (AI-assisted)
**Stage:** Phase 7 — Final Joint Review & Submission
**Decision:** Merge release branch to main and tag the repository with `iccit-submission-v1` for final submission.
**Rationale:** All reproducibility gates, reviewer simulation checks (0 fatal flaws), statistical test matrices, and dataset packaging requirements are successfully completed and verified.
**Impact:** Completes all milestones of the BanLegit-Cite research execution pipeline, readying it for publication review.


