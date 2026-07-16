# BanLegit-Cite

A Bangladeshi legal citation benchmark dataset for detecting legitimate vs. fabricated (hallucinated) legal citations in LLM outputs.

**Target venue:** ICCIT  
**Jurisdiction:** Bangladesh (DLR, BLC, ALR)  
**Status:** Phase 5 — Reproducibility Prep

---

## Project Structure

See `CLAUDE.md` for full file layout, agent rules, and frozen-decision policy.

## Researchers

- **Researcher A** — Data & Legal Content Lead
- **Researcher B** — Engineering & Experiments Lead

## Quick Links

- [Research Questions & Hypotheses](docs/rq_hypotheses.md)
- [Citation Taxonomy](taxonomy/citation_taxonomy.md)
- [Annotation Guidelines](annotation/guidelines.md)
- [Evaluation Protocol](docs/eval_protocol.md)
- [Model Configuration](docs/model_config.md)
- [Novelty Report](literature/novelty_report.md)
- [Decision Log](logs/decision_log.md)
- [Results](RESULTS.md)

## Setup & Reproducibility

```bash
# 1. Clone and enter the repo
git clone <repo-url>
cd BanLegitCite

# 2. Create virtual environment and install pinned dependencies
uv venv
uv pip install -r requirements.txt

# 3. Pull DVC-tracked data
dvc pull   # requires DVC remote credentials

# 4. Run scraping pipeline (generates data/raw/)
python -m scripts.scraper.main --limit 50

# 5. Run fabrication pipeline (generates data/annotated/)
python -m scripts.fabrication.fabricator

# 6. Run full Phase 4 evaluation + statistical tests
python -m scripts.evaluation.run_phase4 --limit 30

# 7. Verify reproducibility
python -m scripts.utils.repro_check
```

## Python Environment

- **Python:** CPython 3.14.6 (via `uv`)
- **Dependencies:** pinned in `requirements.txt`
- **Virtual env:** `.venv/` (created by `uv venv`)
