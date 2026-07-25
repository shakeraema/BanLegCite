# RESULTS.md — BanLegit-Cite

> **Rule:** Updated same day any result is produced. Never batched retrospectively.
> Format: `| Date | Stage | Description | Script | Config | Run ID / Commit |`

---

## Results Table

| Date | Stage | Description | Script | Config | Run ID / Commit |
|------|-------|-------------|--------|--------|-----------------|
| — | — | No results yet — Phase 0 in progress | — | — | — |

---

## Paper Table → Result Mapping

_To be filled as results are produced. Each paper table/figure must map to a specific run ID and git tag._

| Paper Table/Figure | Stage | Script | Config Hash | Git Tag |
|-------------------|-------|--------|-------------|---------|
| — | — | — | — | — |

---

## Phase 4 Results — 2026-07-15 23:19:50

> produced_by: results_reporter.py  
> stage: Phase 4 — Experimentation & Statistical Validation  
> reviewed_by: pending  

### Performance Metrics

| Setting  | Accuracy | REAL P | REAL R | REAL F1 | FAB P | FAB R | FAB F1 |
|----------|----------|--------|--------|---------|-------|-------|--------|
| Standard | 0.5333   | 0.5217 | 0.8000 | 0.6316   | 0.5714 | 0.2667 | 0.3636   |
| Agentic  | 0.9000   | 1.0000 | 0.8000 | 0.8889   | 0.8333 | 1.0000 | 0.9091   |


### Pre-registered Statistical Tests

| Hypothesis | Test | Statistic | p-value | Significant (α=0.05) |
|------------|------|-----------|---------|----------------------|
| H1 | McNemar | 11.0769 | 0.000874 | ✅ Yes |
| H2 | Wilcoxon | 0.0000 | 1.000000 | ❌ No |
| H3 | Chi-squared | 0.0000 | 1.000000 | ❌ No |


### Interpretations

- **H1:** H1 SUPPORTED (Ï‡Â²=11.0769, p=0.000874, Î±=0.05). LLM significantly worse than human annotators.
- **H2:** No differences between settings â€” cannot distinguish.
- **H3:** Insufficient categories for chi-squared test.

---

## Phase 4 Results — 2026-07-15 23:42:48

> produced_by: results_reporter.py  
> stage: Phase 4 — Experimentation & Statistical Validation  
> reviewed_by: pending  

### Performance Metrics

| Setting  | Accuracy | REAL P | REAL R | REAL F1 | FAB P | FAB R | FAB F1 |
|----------|----------|--------|--------|---------|-------|-------|--------|
| Standard | 0.4667   | 0.4737 | 0.6000 | 0.5294   | 0.4545 | 0.3333 | 0.3846   |
| Agentic  | 0.9000   | 1.0000 | 0.8000 | 0.8889   | 0.8333 | 1.0000 | 0.9091   |


### Pre-registered Statistical Tests

| Hypothesis | Test | Statistic | p-value | Significant (α=0.05) |
|------------|------|-----------|---------|----------------------|
| H1 | McNemar | 11.5294 | 0.000685 | ✅ Yes |
| H2 | Wilcoxon | 0.0000 | 1.000000 | ❌ No |
| H3 | Chi-squared | 0.0000 | 1.000000 | ❌ No |


### Interpretations

- **H1:** H1 SUPPORTED (Ï‡Â²=11.5294, p=0.000685, Î±=0.05). LLM significantly worse than human annotators.
- **H2:** No differences between settings â€” cannot distinguish.
- **H3:** Insufficient categories for chi-squared test.

---

## Phase 4 Results — 2026-07-17 01:12:04

> produced_by: results_reporter.py  
> stage: Phase 4 — Experimentation & Statistical Validation  
> reviewed_by: pending  

### Performance Metrics

| Setting  | Accuracy | REAL P | REAL R | REAL F1 | FAB P | FAB R | FAB F1 |
|----------|----------|--------|--------|---------|-------|-------|--------|
| Standard | 0.5333   | 0.7895 | 0.6000 | 0.6818   | 0.0909 | 0.2000 | 0.1250   |
| Agentic  | 0.8333   | 1.0000 | 0.8000 | 0.8889   | 0.5000 | 1.0000 | 0.6667   |


### Pre-registered Statistical Tests

| Hypothesis | Test | Statistic | p-value | Significant (α=0.05) |
|------------|------|-----------|---------|----------------------|
| H1 | McNemar | 11.0769 | 0.003933 | ✅ Yes |
| H2 | Wilcoxon | 0.0000 | 1.000000 | ❌ No |
| H3 | Chi-squared | 0.0000 | 1.000000 | ❌ No |


### Interpretations

- **H1:** H1 SUPPORTED (Ï‡Â²=11.0769, p=0.003933, Î±=0.05). LLM significantly worse than human annotators.
- **H2:** No differences between settings â€” cannot distinguish.
- **H3:** Insufficient categories for chi-squared test.

---

## Phase 4 Results — 2026-07-25 16:48:11

> produced_by: results_reporter.py  
> stage: Phase 4 — Experimentation & Statistical Validation  
> reviewed_by: pending  

### Performance Metrics

| Setting  | Accuracy | REAL P | REAL R | REAL F1 | FAB P | FAB R | FAB F1 |
|----------|----------|--------|--------|---------|-------|-------|--------|
| Standard | 0.3667   | 0.3750 | 0.4000 | 0.3871   | 0.3571 | 0.3333 | 0.3448   |
| Agentic  | 1.0000   | 1.0000 | 1.0000 | 1.0000   | 1.0000 | 1.0000 | 1.0000   |


### Pre-registered Statistical Tests

| Hypothesis | Test | Statistic | p-value | Significant (α=0.05) |
|------------|------|-----------|---------|----------------------|
| H1 | McNemar | 16.0556 | 0.000326 | ✅ Yes |
| H2 | Wilcoxon | 0.0000 | 1.000000 | ❌ No |
| H3 | Chi-squared | 0.0000 | 1.000000 | ❌ No |


### Interpretations

- **H1:** H1 SUPPORTED (Ï‡Â²=16.0556, p=0.000326, Î±=0.05). LLM significantly worse than human annotators.
- **H2:** No differences between settings â€” cannot distinguish.
- **H3:** Insufficient categories for chi-squared test.
