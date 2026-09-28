# Overnight pass — 2026-09-16 (release v0.37–v0.38)

Point-fixes only. No figure redesign. No invented ORCID, Zenodo DOI, or Rudra scores.

**Superseded for the live dataset of record:** Hub revision `fc238e3b600f556045bc9a3f7a37738734620cd8` is 88,519, archived at https://doi.org/10.5281/zenodo.23021932. 88,545 in this note is the research-corpus commercial stamp. Version DOI https://doi.org/10.5281/zenodo.22822285 is the earlier pre-clean snapshot, not the dataset of record.

Started from `origin/main` at **v0.36** (`bd11755`).

## Locked facts re-checked (do not regress)

| Fact | Status in TeX / cover letter |
|------|------------------------------|
| Sci Data primary; JCIM App Notes backup only | Unchanged (no JCIM targeting in manuscript) |
| Fig.~2 = locked H (`fig_pipe.png` / HF+Zenodo, Cleaning rules, 350–4000, Automated QC) | Caption already 350–4000 / HF~+~Zenodo; **binaries untouched** |
| Human audit 161/200 scored on commercial DoR; 39 NC/SA intentionally unscored | Abstract, TV, Limitations, cover letter agree |
| Construction *n* = 121,233; that night’s HF commercial file was 88,545 | Agreed in TeX on 2026-09-16. Live Hub DoR is now 88,519 (rev `fc238e3`); 88,545 is the research-corpus stamp / prior Zenodo snapshot |
| AccelD Grant #596133-2025 | `\section*{Funding}` + cover letter |
| Cover letter: McMaster letterhead, Rodrigo / `vargashr@mcmaster.ca` | Unchanged sign-off |
| Archival / Zenodo DOI | Current version DOI https://doi.org/10.5281/zenodo.23021932 (this Hub revision, n=88,519). Earlier version DOI https://doi.org/10.5281/zenodo.22822285 archived the pre-clean snapshot. No software DOI claimed. |
| ORCID | Absent from the TeX author block on this date (not invented). Confirmed later in `scientific_data.tex`; see `HUMAN_SUBMISSION_CHECKLIST.md`. |

Rudra sheet re-counted (not re-scored): 161 scored / 39 unscored; 160/161 source Y; bands exact 143, subset_ok 13, mismatch 4, cannot_tell 1. Unscored pools: 7 NC + 2 empty_unknown + 30 ShareAlike.

## What changed

### `scientific_data.tex`

- **Band window consistency:** Data Records + Technical Validation “IR physical window” restored to **350–4000 cm⁻¹** (had drifted to 400–4000). Matches locked Fig.~2 Cleaning rules and frozen `data/qc_structure_nmr.json` (`out_of_range_outside_350_4000 = 0`). Did **not** claim a tighter [400, 4000] cut without a matching QC field.
- Grammar/clarity: “and as the literature substrate” → “and serving as…”; “rawer rows” → “raw rows”; “IE toolkits” → “information-extraction toolkits”; “Human mark-up” → “human mark-up”; “Productized reuse” → “Reuse”; DAS “artifact” → “artefact” (British consistency).
- Headline counts, HF revision SHA `8db58466…`, F2/F3 rates, 161/39 wording, AccelD funding: **untouched**.

### Cover letter

- Still Rodrigo template (McMaster letterhead PNG, sign-off Rodrigo A. Vargas-Hernández / `vargashr@mcmaster.ca`).
- TV now two sentences: **161 scored** on the commercial HF DoR; **39** NC*/SA rows absent from that publish and **intentionally unscored**.
- 121,233 / 88,545 / AccelD were left as they stood that night. That night’s data-only version DOI was https://doi.org/10.5281/zenodo.22822285; the current archival version is https://doi.org/10.5281/zenodo.23021932.

### Compile (local, not committed)

- `scientific_data.tex`: tectonic + `sn-jnl` search path → PDF; BibTeX `sn-nature.bst` clean (no undefined citations). Remaining overfull boxes are pre-existing table/URL lines.
- Cover letter: compiles with letterhead; a ~5.6 pt overfull is the pre-existing “stores numeric band lists…” sentence, not a new citation problem.

### Docs (hygiene, not new science)

- `docs/SCIENTIFIC_DATA.md` working notes: abstract / QC / Limitations / R.S. contributions aligned to 161/39 (was still “chemist-proxy only”).
- `docs/HUMAN_AUDIT_RUDRA_SUMMARY_2026-09-15.md`: tab-corrupted field names; “pending/untouched” wording that implied unfinished auditor work.
- `docs/HUMAN_SUBMISSION_CHECKLIST.md`: 161/39 marked done; ORCID + Zenodo were still listed as blockers; optional NC/SA scoring listed as optional.
- `docs/REFEREE_RESPONSE_CHECKLIST_2026-09-10.md`: band-window row updated for the 350–4000 realignment.
- `references.bib`: missing blank line after the companion-manuscript entry (no citation invented).

## What still blocks submit (human only)

1. **ORCID — I. Yabbarov** — unconfirmed in the MD notes on this date. Later: https://orcid.org/0009-0004-9393-9822 in `scientific_data.tex`.
2. **ORCID — R. A. Vargas-Hernández** — candidate later confirmed as https://orcid.org/0000-0002-5559-6521 in `scientific_data.tex`.
3. **ORCID — Rudra Sondhi** — not yet recorded on this date. Later: https://orcid.org/0009-0003-3034-7347 in `scientific_data.tex`.
4. **Zenodo data-only DOI** — first mint was https://doi.org/10.5281/zenodo.22822285 (pre-clean commercial snapshot). Current version DOI is https://doi.org/10.5281/zenodo.23021932. No software DOI.
5. Optional, not required for commercial-DoR honesty: stage NC*/SA rows and finish the 39-row queue if a full *n*=200 multi-pool audit is desired later.

## Morning actions

1. Overleaf: **Pull from GitHub** (no force) → `scientific_data.tex` is main.
2. Compile pdfLaTeX + BibTeX; skim Fig.~2 caption vs the locked H figure (350–4000 / HF+Zenodo / Cleaning rules / Automated QC) — binaries were not regenerated.
3. ORCID iDs were added later with `\orcid{https://orcid.org/...}` in `scientific_data.tex` (see `HUMAN_SUBMISSION_CHECKLIST.md`).
4. Data-only archival version DOI is https://doi.org/10.5281/zenodo.23021932; do not revert Data Availability to version DOI https://doi.org/10.5281/zenodo.22822285 or to an unminted claim.
5. Cover letter: confirm letterhead PNG still sits beside `cover_letter.tex` on Overleaf; date is `\today`.
6. Do **not** run figure redesign sweeps; do **not** fill Rudra’s 39 unscored rows from memory.

## Explicitly not done

- No figure PDF/PNG/SVG edits.
- No new Rudra scores.
- No ORCID / Zenodo DOI strings invented.
- No JCIM App Notes conversion.
- No paper-wide 121,233 rebuild.
