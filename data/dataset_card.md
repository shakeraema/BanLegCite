# Dataset Card for BanLegit-Cite

> produced_by: Researcher B
> date: 2026-07-15
> stage: Phase 6 Release

## Dataset Description

BanLegit-Cite is a Bangladeshi legal citation benchmark dataset designed to detect legitimate vs. fabricated (hallucinated) legal citations in LLM outputs. It covers Supreme Court judgments from Dhaka Law Reports (DLR), Bangladesh Law Chronicles (BLC), and Apex Law Reports (ALR).

### Dataset Summary

- **Total Citations:** 90 records (paired 1:1 between real and fabricated classes)
- **Languages:** Bengali, English
- **Jurisdiction:** Bangladesh

### Supported Tasks

- **Citation Verification:** Binary classification task to evaluate if a legal citation is `REAL` (exists and accurately references the matching court report) or `FABRICATED` (hallucinated, incorrect volume/page, or false legal propositions).

---

## Dataset Structure

Each instance in the dataset contains:

| Feature | Type | Description |
|---------|------|-------------|
| `citation_id` | `string` | Unique identifier (e.g. `DLR_REAL_1` or `DLR_FABRICATED_1`) |
| `citation` | `string` | The legal citation text (e.g. `52 DLR (AD) 12`) |
| `context` | `string` | Surrounding context paragraph containing the citation and legal proposition |
| `source` | `string` | The publication reporter name (e.g. `Dhaka Law Reports (AD)`) |
| `extracted_url` | `string` | Search URL reference for manual validation lookup |
| `fabrication_type` | `string` | Error taxonomy classification (e.g. `Incorrect Volume/Page` or `N/A` for real) |
| `label` | `string` | Ground truth target: `REAL` or `FABRICATED` |

---

## Dataset Licensing & Copyright

- **Licensing:** MIT License
- **Copyright Policy:** Standard metadata lookup context and fair-use excerpts only. No full text of copyright-protected law reports is released, ensuring compliance with legal domain copyrights.
