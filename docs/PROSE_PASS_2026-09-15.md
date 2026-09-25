# Prose pass — 2026-09-15 (release v0.34)

Point-fixes in `scientific_data.tex` (no figure redesign).

## Human audit clarification (critical)

- Abstract / Technical Validation / Limitations: **161 scored** from rows available on the commercial Hugging Face dataset of record; **39** stratified NC*/ShareAlike queue rows (9 non-commercial/empty-unknown + 30 Chemotion ShareAlike, stratum E) are **absent from that HF publish and were intentionally left unscored**.
- Removed “39 pending” / “under way” / “stratum E untouched” wording that implied unfinished auditor work.
- `docs/HUMAN_AUDIT_RUDRA_SUMMARY_2026-09-15.md` status / manuscript-wording lines aligned.

## Background & flow

- Kept IRexp-first open; no `\paragraph` in Background.
- Smoothed peer situating (“likewise illustrate…”) and closing complementarity vs SDBS (less defensive “does not claim”).
- Softened substrate / companion-manuscript scope sentence; tightened intended-reuse lead-in.
- Reduced redundant NMR-resource stacking in Limitations Object bullet.

## Methods / captions / DAS

- Subject–verb agreement (`code live`); Methods opener and F1 “relative to” wording.
- Fig.~2 caption: normalized Unicode em dash to LaTeX `---`; **Cleaning rules** / **350–4000** / **HF+Zenodo** with archival-DOI-not-claimed caveat (matches shipped H figure).
- Dropped redundant DAS archival-DOI bullet (lead sentence already states it); Access bullet shortened.
- Usage Notes attribution tightened.

## Technical Validation

- Single NMRexp expert-audit disclaimer retained (line-break only).
- Recall-proxy close: “automatic proxy does not replace…”.
- QC status human-audit item rewritten for commercial-DoR honesty + intentional unscored 39.

## Authorship / consistency left intact

- HF revision SHA `8db58466e3ddfd2fbe09bd47fdd5eb4cfc3e1975` unchanged.
- F2/F3 fields + rates unchanged in Data Records / TV.
- Zenodo / archival DOI still not claimed.
- AccelD / NSERC funding reference **596133-2025** unchanged.
- R.S. Author contributions: added validation (human band-list audit).

## Remaining soft blockers (unchanged)

- ORCID confirmation for authors was still open on this pass (later confirmed in `scientific_data.tex`; see `HUMAN_SUBMISSION_CHECKLIST.md`).
- Zenodo archival DOI mint (commercial pool).
- Optional: stage NC*/SA rows if a full *n*=200 multi-pool human audit is desired later (not required for commercial DoR honesty).
