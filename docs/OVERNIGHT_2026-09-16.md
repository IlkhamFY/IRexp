# Overnight pass — 2026-09-16 (release v0.37–v0.38)

Point-fixes only. No figure redesign. No invented ORCID, Zenodo DOI, or Rudra scores.

Started from `origin/main` at **v0.36** (`bd11755`).

## Locked facts re-checked (do not regress)

| Fact | Status in TeX / cover letter |
|------|------------------------------|
| Sci Data primary; JCIM App Notes backup only | Unchanged (no JCIM targeting in manuscript) |
| Fig.~2 = locked H (`fig_pipe.png` / HF+Zenodo, Cleaning rules, 350–4000, Automated QC) | Caption already 350–4000 / HF~+~Zenodo; **binaries untouched** |
| Human audit 161/200 scored on commercial DoR; 39 NC/SA intentionally unscored | Abstract, TV, Limitations, cover letter agree |
| Construction *n* = 121,233; commercial DoR 88,545 on HF `ilkhamfy/IRexp` | Abstract, Background, Data Records, DAS, cover letter agree |
| AccelD Grant #596133-2025 | `\section*{Funding}` + cover letter |
| Cover letter: McMaster letterhead, Rodrigo / `vargashr@mcmaster.ca` | Unchanged sign-off |
| Archival / Zenodo DOI | Data-only version DOI https://doi.org/10.5281/zenodo.22822285 (commercial CC-BY/CC0 pool). No software DOI claimed. |
| ORCID | Still absent from TeX author block (not invented) |

Rudra sheet re-counted (not re-scored): 161 scored / 39 unscored; 160/161 source Y; bands exact 143, subset_ok 13, mismatch 4, cannot_tell 1. Unscored pools: 7 NC + 2 empty_unknown + 30 ShareAlike.

## What changed

### `scientific_data.tex`

- **Band window consistency:** Data Records + Technical Validation “IR physical window” restored to **350–4000 cm⁻¹** (had drifted to 400–4000). Matches locked Fig.~2 Cleaning rules and frozen `data/qc_structure_nmr.json` (`out_of_range_outside_350_4000 = 0`). Did **not** claim a tighter [400, 4000] cut without a matching QC field.
- Grammar/clarity: “and as the literature substrate” → “and serving as…”; “rawer rows” → “raw rows”; “IE toolkits” → “information-extraction toolkits”; “Human mark-up” → “human mark-up”; “Productized reuse” → “Reuse”; DAS “artifact” → “artefact” (British consistency).
- Headline counts, HF revision SHA `8db58466…`, F2/F3 rates, 161/39 wording, AccelD funding: **untouched**.

### Cover letter

- Still Rodrigo template (McMaster letterhead PNG, sign-off Rodrigo A. Vargas-Hernández / `vargashr@mcmaster.ca`).
- TV now two sentences: **161 scored** on the commercial HF DoR; **39** NC*/SA rows absent from that publish and **intentionally unscored**.
- 121,233 / 88,545 / AccelD were left as they stood that night. The data-only archival DOI is https://doi.org/10.5281/zenodo.22822285.

### Compile (local, not committed)

- `scientific_data.tex`: tectonic + `sn-jnl` search path → PDF; BibTeX `sn-nature.bst` clean (no undefined citations). Remaining overfull boxes are pre-existing table/URL lines.
- Cover letter: compiles with letterhead; a ~5.6 pt overfull is the pre-existing “stores numeric band lists…” sentence, not a new citation problem.

### Docs (hygiene, not new science)

- `docs/SCIENTIFIC_DATA.md` working notes: abstract / QC / Limitations / R.S. contributions aligned to 161/39 (was still “chemist-proxy only”).
- `docs/HUMAN_AUDIT_RUDRA_SUMMARY_2026-09-15.md`: tab-corrupted field names; “pending/untouched” wording that implied unfinished auditor work.
- `docs/HUMAN_SUBMISSION_CHECKLIST.md`: 161/39 marked done; ORCID + Zenodo remain blockers; optional NC/SA scoring listed as optional.
- `docs/REFEREE_RESPONSE_CHECKLIST_2026-09-10.md`: band-window row updated for the 350–4000 realignment.
- `references.bib`: missing blank line after the companion-manuscript entry (no citation invented).

## What still blocks submit (human only)

1. **ORCID — I. Yabbarov** — still `[TODO: confirm]` in MD notes; do not invent; paste into TeX / eJP when confirmed.
2. **ORCID — R. A. Vargas-Hernández** — known candidate `0000-0002-5559-6521`; confirm before paste (do not assume).
3. **Zenodo data-only DOI** — minted: https://doi.org/10.5281/zenodo.22822285 (commercial CC-BY/CC0 pool). No software DOI.
4. Optional, not required for commercial-DoR honesty: stage NC*/SA rows and finish the 39-row queue if a full *n*=200 multi-pool audit is desired later.

## Morning actions

1. Overleaf: **Pull from GitHub** (no force) → `scientific_data.tex` is main.
2. Compile pdfLaTeX + BibTeX; skim Fig.~2 caption vs the locked H figure (350–4000 / HF+Zenodo / Cleaning rules / Automated QC) — binaries were not regenerated.
3. Confirm ORCIDs; only then add `\orcid` (or eJP metadata).
4. Data-only archival DOI is https://doi.org/10.5281/zenodo.22822285; do not revert Data Availability to an unminted claim.
5. Cover letter: confirm letterhead PNG still sits beside `cover_letter.tex` on Overleaf; date is `\today`.
6. Do **not** run figure redesign sweeps; do **not** fill Rudra’s 39 unscored rows from memory.

## Explicitly not done

- No figure PDF/PNG/SVG edits.
- No new Rudra scores.
- No ORCID / Zenodo DOI strings invented.
- No JCIM App Notes conversion.
- No paper-wide 121,233 rebuild.
