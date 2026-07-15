# Annotation Guidelines — BanLegit-Cite

> **STATUS: DRAFT — NOT YET FROZEN**
> Frozen after Phase 1 gate (κ ≥ 0.6 in pilot annotation round).
> Written by Researcher A. Any change after freezing requires joint decision-log entry.

---

## Task Definition

Annotators are presented with a legal document excerpt containing one or more citations. For each citation, annotators must decide:

1. **Citation Type** — from the frozen taxonomy (`taxonomy/citation_taxonomy.md`)
2. **Legitimacy Label** — `REAL` or `FABRICATED`
3. **Confidence** — `High` / `Medium` / `Low`
4. **Evidence** — brief note on what source was checked (mandatory for `REAL` labels)

---

## Legitimacy Labeling Rules

### REAL
A citation is REAL if:
- The referenced case/statute/section **exists** in DLR, BLC, or ALR
- The **volume, page, year, and court** match the actual published report
- The **legal proposition** attributed to the citation is accurately represented

### FABRICATED
A citation is FABRICATED if **any** of the following are true:
- The case/statute does not exist
- Volume/page/year/court combination does not match records
- The legal proposition is materially misrepresented

### Edge Cases (to be expanded during Phase 1)
- Partially correct citations (e.g., right case, wrong page): → FABRICATED
- Ambiguous citations (insufficient detail to verify): → flag for adjudication, do not guess

---

## Adjudication Protocol

- Disagreements between annotators go to the human legal adjudicator (law-faculty member)
- High-disagreement cases (both annotators uncertain) go to joint researcher review first
- All adjudication decisions are logged with the adjudicator's reasoning

---

## Freeze Checklist

- [ ] Guidelines drafted by Researcher A
- [ ] Pilot annotation round completed with real annotators
- [ ] IAA κ ≥ 0.6 achieved
- [ ] Both researchers sign decision_log.md: "Annotation guidelines frozen"
