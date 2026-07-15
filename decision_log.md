# BanLegit-Cite: Decision Log

This log tracks all high-stakes scientific, architectural, and scoping decisions with research consequence.

---

### [2026-07-15] DECISION 1: Adoption of Sequential Single-Owner Execution Plan
- **Context:** Minimizing coordination overhead and preventing idle-blocking between the two researchers.
- **Options Considered:** 
  1. Shared Track-based parallel execution (traditional track splits).
  2. Sequential Single-Owner alternating phase execution.
- **Rationale:** Sequential Single-Owner alternating structure matches skillsets (Ema = Judgment/Narrative, Zahid = Systems/Execution) and limits sync points to fixed handoff gates, allowing higher-focus execution.
- **Reversible:** No (High-stakes)

---

### [2026-07-15] DECISION 2: Annotation Strategy Constraint (Lack of External Law Students)
- **Context:** The team currently does not have external law students recruited for the primary double-annotation phase.
- **Options Considered:**
  1. Pause research to recruit external law students (high risk of timeline slip).
  2. Adapt annotation responsibilities: Researcher A (Ema), who holds the legal-content judgment, acts as the primary validator and legal-content driver. Zahid handles system-level fabrications. 
  3. Recruit annotators asynchronously during Phase 2 shadow-work, aiming for a smaller, highly focused legal expert group (e.g. junior colleagues/students) and using Ema as the main adjudicator.
- **Rationale:** We will target option 3. Ema will prioritize recruiting a small target annotator pool (2 junior lawyers or advanced law students) during her Phase 2 shadow-work window. If recruitment fails, Ema will act as Annotator 1, a recruited peer will act as Annotator 2, and the senior advisor/adjudicator will act as the final arbiter to ensure we maintain the mandatory double-annotation/IAA requirement (`κ ≥ 0.6` target).
- **Reversible:** Yes (Medium-stakes)
