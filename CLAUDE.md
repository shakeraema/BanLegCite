# BanLegit-Cite — Project Instructions for AI Agents

> Every Claude Code session in this repo inherits these constraints automatically.
> Do NOT override, ignore, or relax any rule below without a joint decision-log entry signed by both researchers.

---

## 1. WHAT THIS PROJECT IS

BanLegit-Cite is a Bangladeshi legal citation benchmark dataset and evaluation framework, targeting ICCIT submission.
The project detects **legitimate vs. fabricated (hallucinated)** legal citations in LLM outputs, scoped to Bangladeshi jurisdiction (DLR, BLC, ALR).

---

## 2. EVIDENCE-LOGGING RULES (mandatory for all agent outputs)

- **Every factual claim** about a competitor paper must cite a specific passage (page/section) in the source PDF stored in Zotero.
- **No novelty claim** may be made based solely on an LLM's recollection — all novelty statements must trace to `literature/novelty_report.md`.
- **Any finding** that goes into the paper must have a corresponding entry in `RESULTS.md` (updated same day).
- When in doubt, log it. Missing provenance is a fatal flaw at submission.

---

## 3. BATCH-AND-GATE RULES (for fabrication generation & annotation)

- Fabrication batches are generated in units of **≤50 examples** at a time.
- **No next batch** is generated until Researcher A has reviewed ≥20% of the current batch and approved it.
- Approval is recorded as a dated entry in `logs/decision_log.md`.
- Rejected examples are logged with a reason in `logs/fabrication_review_log.md` — never silently deleted.

---

## 4. PROVENANCE-METADATA REQUIREMENTS

Every data file produced by an agent must include a header block:
```
# produced_by: <agent-name or script name>
# date: YYYY-MM-DD
# reviewed_by: <Researcher A / B / both / pending>
# stage: <Operating Manual stage number>
# commit: <git commit hash if applicable>
```

Every experiment output file must include in its filename:
`<stage>_<model>_<setting>_<YYYYMMDD>_<config-hash>.json`

---

## 5. FROZEN DECISIONS — DO NOT MODIFY WITHOUT JOINT SIGN-OFF

The following are locked after Phase 0 gate. Any agent asked to change these must refuse and escalate:
- Research questions (RQ) and hypotheses H1–H3 → `docs/rq_hypotheses.md`
- Citation taxonomy categories → `taxonomy/citation_taxonomy.md`
- Gold-label annotation guidelines → `annotation/guidelines.md`
- Evaluation metrics and pre-registered statistical tests → `docs/eval_protocol.md`

---

## 6. GIT CONVENTIONS

- Branch naming: `stage<N>-<short-description>` (e.g., `stage7-taxonomy`, `stage13-baselines`)
- Commit messages: `[stage<N>] <description>, <agent>-generated, <researcher>-reviewed, <N> rejected`
- Never commit raw corpus/annotation files — use DVC pointer files only.
- Never push directly to `main` — all merges require the other researcher's PR review.

---

## 7. FILE STRUCTURE (do not reorganize without updating this file)

```
BanLegitCite/
├── CLAUDE.md                  ← this file
├── RESULTS.md                 ← updated same-day for every result
├── README.md
├── docs/
│   ├── rq_hypotheses.md       ← frozen after Phase 0 gate
│   └── eval_protocol.md       ← frozen after Phase 1 gate
├── literature/
│   ├── bibliography.csv       ← single source of truth (A2 agent feeds this)
│   └── novelty_report.md      ← A3 agent adversarial findings
├── taxonomy/
│   └── citation_taxonomy.md   ← frozen after Phase 1 gate
├── annotation/
│   └── guidelines.md          ← frozen after Phase 1 gate
├── data/
│   ├── raw/                   ← DVC-tracked, never git-committed
│   ├── annotated/             ← DVC-tracked
│   └── gold/                  ← DVC-tracked, frozen after Phase 2 gate
├── experiments/
│   └── results/               ← timestamped output files, DVC-tracked
├── scripts/
│   └── ...                    ← all pipeline code
├── logs/
│   ├── decision_log.md        ← append-only, both researchers
│   ├── research_log.md        ← daily 3-line updates
│   └── fabrication_review_log.md
└── .dvc/                      ← DVC config
```

---

## 8. RESEARCHER TRACK ASSIGNMENTS

| Track | Owner | Scope |
|-------|-------|-------|
| Data & Legal Content | Researcher A | Corpus, taxonomy, annotation, legal correctness |
| Engineering & Experiments | Researcher B | Pipeline, baselines, stats, infra |

Agents must tag outputs with which track they belong to.
