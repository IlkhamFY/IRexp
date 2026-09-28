# Zenodo data-only mint checklist (human)

**Minted (data-only commercial pool).** Prefer the version DOI
`https://doi.org/10.5281/zenodo.22822285` (`10.5281/zenodo.22822285`).
Concept DOI: `10.5281/zenodo.22822284`. Record:
https://zenodo.org/records/22822285.
This record mirrors the earlier Hugging Face `ilkhamfy/IRexp` revision
`8db58466e3ddfd2fbe09bd47fdd5eb4cfc3e1975` (commercial n=88,545).
It is not the live Hub dataset of record. That file is revision
`fc238e3b600f556045bc9a3f7a37738734620cd8` (commercial n=88,519).
88,545 remains the research-corpus commercial stamp and this Zenodo snapshot.

## Why a separate deposit

Repo-root `.zenodo.json` describes a **combined** research archive (IRexp **+** IRSpectra-Bench + model artefacts). Scientific Data archival must be a **data-only** IRexp deposit. Do **not** reuse that combined metadata as the Sci Data record.

## Files to upload

| Priority | File | Licence metadata | Notes |
|---|---|---|---|
| Primary | `data/irexp/licence_pools/irexp_commercial.jsonl.gz` (88,545) | `cc-by-4.0` (deposit metadata) | Earlier Zenodo snapshot (research-corpus commercial stamp). Live Sci Data Hub DoR is 88,519 (rev `fc238e3`) |
| Companion | `data/irexp/licence_pools/irexp_sharealike.jsonl.gz` (1,897) | CC-BY-SA-4.0 | Chemotion + rare PMC SA; description must say ShareAlike |
| Optional / labelled | `irexp_non_commercial.jsonl.gz` (21,823) | NC* — not commercial | Hold aside; clear label |
| Optional / labelled | `irexp_empty_unknown.jsonl.gz` (8,963) | unresolved | Excluded from commercial primary |
| Optional / labelled | `irexp_other.jsonl.gz` (5) | CC-BY-ND | Held aside |
| Docs | `data/NOTICE`, `docs/scientific_data/LICENCE_REMEDIATION.md`, `pmc_licence_summary.json` | — | Provenance |

Do **not** upload IRSpectra-Bench predictions, leaderboards, or model-result tables into this Sci Data deposit.

## Suggested title / description stubs

- **Title:** `IRexp: experimental infrared band lists from open literature (data release)`
- **Creators:** Ilkham Yabbarov (https://orcid.org/0009-0004-9393-9822); Rodrigo A. Vargas-Hernández (https://orcid.org/0000-0002-5559-6521)
- **Description (skeleton):** Redistributable experimental IR **band lists** (cm⁻¹), not absorbance traces. Full research corpus is multi-licence; this deposit’s primary file is the earlier commercial CC-BY/CC0 snapshot (88,545), not the live Hub dataset of record (88,519, revision `fc238e3`). ShareAlike companion is separate. NC* and empty/unknown are excluded from the commercial artifact (optional labelled files only). See LICENCE_REMEDIATION.md. Companion ICLR/IRSpectra-Bench results are **out of scope**.
- **Related identifiers:** GitHub paper/manifests `IlkhamFY/IRexp`; code `IlkhamFY/spectro-agent`; HF `ilkhamfy/IRexp`; forthcoming Sci Data Data Descriptor; companion research manuscript (cross-cite, no results).

## After mint

1. Paste DOI into TeX Access + Data Availability and MD TODOs. **Done**
   (`scientific_data.tex` cites `https://doi.org/10.5281/zenodo.22822285`).
2. Tag the Git commit that matches the uploaded files.
3. Update HF card Zenodo line if desired.
4. Tick the matching row in `HUMAN_SUBMISSION_CHECKLIST.md`.
