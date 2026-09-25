# Human submission checklist — IRexp Sci Data

Agent-addressable TV / licence / remirror / overview work is complete on this branch.  
**Only the author can finish the items below.** Do not invent values.

## Critical (submit blockers)

| # | Action | Status | Notes / stub |
|---|---|---|---|
| 1 | Mint **data-only** Zenodo DOI | ☑ | Done — version DOI https://doi.org/10.5281/zenodo.22822285 (concept 10.5281/zenodo.22822284). See `ZENODO_DATA_ONLY_CHECKLIST.md`. |
| 2 | Confirm ORCID — **I. Yabbarov** | ☐ | Paste into TeX author block / eJP. MD still has `[TODO: confirm]`. |
| 3 | Confirm ORCID — **R. A. Vargas-Hernández** | ☐ | Known candidate: `0000-0002-5559-6521` (confirm before submit). |
| 4 | Replace Acknowledgements / funding placeholder | ☑ | NSERC 596133-2025 (CREATE AccelD via Acceleration Consortium) + McMaster Chemistry. Text-only (no sponsor logo in the Descriptor). |

## Optional (strengthen TV vs NMRexp)

| # | Action | Status |
|---|---|---|
| 5 | Expert human structure spot-check n≥100 | ☐ deferred |
| 6 | Human extraction-recall mark-up (paper-level) | ☐ deferred |
| 7 | Commercial-DoR human audit is complete at n=161; do not discuss the unscored NC*/SA queue in the manuscript | ☑ |

## Already done (agent) — do not redo unless counts drift

- Crossref empty-licence recovery → commercial **88,545**
- HF remirror (`scripts/publish_hf.py`, 2026-08-27)
- Overview figure `figures/fig_irexp_overview.pdf`
- Dual-publication fence + honest Data/Code Availability placeholders
- Automated TV pack (transcription n=200, recall n=120, chemist-proxy n=280, quarantine)
- Stratified expert human band-list audit: commercial-DoR human audit is complete at **n=161**. Do not discuss the unscored NC*/SA queue in the manuscript.

## Contacts for placeholders

- Corresponding: `yabbaroi@mcmaster.ca`, `vargashr@mcmaster.ca`
- HF mirror: https://huggingface.co/datasets/ilkhamfy/IRexp
- Working TeX: `scientific_data.tex` (repo root)
