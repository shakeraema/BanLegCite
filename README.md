# BanLegit-Cite

A Bangladeshi legal citation benchmark dataset for detecting legitimate vs. fabricated (hallucinated) legal citations in LLM outputs.

**Target venue:** ICCIT  
**Jurisdiction:** Bangladesh (DLR, BLC, ALR)  
**Status:** Phase 0 — Foundation (Week 1)

---

## Project Structure

See `CLAUDE.md` for full file layout, agent rules, and frozen-decision policy.

## Researchers

- **Researcher A** — Data & Legal Content Lead
- **Researcher B** — Engineering & Experiments Lead

## Quick Links

- [Research Questions & Hypotheses](docs/rq_hypotheses.md)
- [Novelty Report](literature/novelty_report.md)
- [Decision Log](logs/decision_log.md)
- [Results](RESULTS.md)

## Setup

```bash
git clone <repo-url>
cd BanLegitCite
pip install dvc
dvc pull   # pulls corpus data from remote
```
