# Human audit summary (Rudra) — 2026-09-15

**Sheet:** data/audit_irexp_f1_20260910/scoring_sheet_rudra_20260915.csv  
**Auditor:** Rudra Sondhi  
**Sample:** stratified F1 commercial / multi-pool audit queue, *n* = 200  
**Status:** **partial** — 161 scored, **39 pending** (do not report *n* = 200 complete)

## Headline rates (among 161 scored)

| Metric | Count | Rate |
|--------|------:|-----:|
| Source found (Y) | 160 / 161 | 99.4% |
| Bands match: exact | 143 / 161 | 88.8% |
| Bands match: subset_ok | 13 / 161 | 8.1% |
| Bands match: mismatch | 4 / 161 | 2.5% |
| Bands match: cannot_tell | 1 / 161 | 0.6% |
| Truncation artifact: N | 153 / 161 | 95.0% |
| Truncation artifact: Y | 7 / 161 | 4.3% |
| Completeness: full | 149 / 161 | 92.5% |
| Completeness: major_missing | 12 / 161 | 7.5% |
| Confidence 4–5 | 138 / 160 | 86.3% |

Notes: one scored row (stratum B) lacks confidence / 	runcation_artifact (source_found = N / cannot_tell path). Pairing and name–structure fields are sparsely filled outside commercial structure-linked strata (many unsure / blank in B–C).

## Coverage by stratum

| Stratum | Quota | Scored | Pending | Notes |
|---------|------:|-------:|--------:|-------|
| A | 40 | 40 | 0 | Commercial structure-linked |
| B | 30 | 22 | 8 | Mostly IR-only / mixed licence; pending = NC* rows absent from HF publish |
| C | 20 | 19 | 1 | Pending = NC* row absent from HF publish |
| D | 20 | 20 | 0 | |
| E | 30 | 0 | 30 | **Untouched** — Chemotion ShareAlike; band lists absent from HF publish |
| F | 20 | 20 | 0 | |
| G | 20 | 20 | 0 | |
| H | 20 | 20 | 0 | |
| **Total** | **200** | **161** | **39** | |

Pending queue also mirrored as scoring_queue_unscored_39.csv. All 39 require rows from data/irexp_rebuild_20260910/ (or equivalent non-commercial / ShareAlike publish) before band-match / completeness can be finished; stratum E source pages are otherwise verifiable on Chemotion.

## Rates by stratum (scored only)

| Stratum | *n* | source Y | exact | subset_ok | mismatch | trunc N | full | conf 4–5 |
|---------|----:|---------:|------:|----------:|---------:|--------:|-----:|---------:|
| A | 40 | 40 | 36 | 4 | 0 | 38 | 39 | 40 / 40 |
| B | 22 | 21 | 17 | 0 | 4 | 17 | 15 | 10 / 21 |
| C | 19 | 19 | 11 | 8 | 0 | 18 | 15 | 19 / 19 |
| D | 20 | 20 | 19 | 1 | 0 | 20 | 20 | 20 / 20 |
| F | 20 | 20 | 20 | 0 | 0 | 20 | 20 | 15 / 20 |
| G | 20 | 20 | 20 | 0 | 0 | 20 | 20 | 14 / 20 |
| H | 20 | 20 | 20 | 0 | 0 | 20 | 20 | 20 / 20 |
| E | 0 | — | — | — | — | — | — | — |

Stratum B concentrates mismatch and major_missing; A/C concentrate subset_ok (extraneous non-IR numbers kept in the list). F/G/H are exact on bands among scored rows, with moderate confidence in F/G.

## Mismatch / subset themes (auditor notes)

Themes called out in free-text notes (mass / MW / LC–MS in IR lists; R²; missing peaks):

1. **Mass / MW / LC–MS numbers ingested as IR bands (subset_ok).**  
   Recurring pattern in A and C: molecular mass, molecular weight, or LC/MS *m/z* values appear in the released band list (e.g. 458 mass-spec; 447.4 MW; 426 / 426.46 / 428.35; 453.58 MW; paired LC/MS + MW doublets such as 438.56 / 437.39, 468.53 / 467.43, 449.69 / 448.92, 466.41 / 465.44; 538.39 / 537.45 LC/MS). True IR bands otherwise match; auditor marked **subset_ok** rather than mismatch.

2. **R² / non-IR numeric fields reported as bands (mismatch).**  
   Stratum B: R² values transcribed instead of wavenumbers (one case with corrected IR list 1772, 1702, 1397, 1281 and no structure); another B row has normalised maximum HRR instead of IR; one B row has wrong values with a full corrected list supplied in notes.

3. **Missing peaks / truncation (subset_ok or major_missing).**  
   Explicit missing wavenumbers (e.g. 981 and 952; 758 and 673; 757 and 672; 672 and 470). Seven scored rows carry 	runcation_artifact = Y.

4. **Range expansion.**  
   Two notes (C, D): hyphenated source ranges (e.g. 3669–3200; 2964–2869) expanded into four discrete endpoints in the release.

5. **Other.**  
   One A note: four compounds in paper share the same IR string (pairing still OK). One B cannot_tell with incomplete fields. One G row: pairing_ok = N / 
ame_structure_ok = N despite exact bands.

## Manuscript / release wording

- Report human audit as **n = 161 scored of 200** (partial; 39 pending).  
- Do **not** claim the stratified human audit is complete at *n* = 200.  
- Expert human **structure / molecular-skeleton** spot-check remains deferred (distinct from this band-list source audit).

## Remaining blockers

1. Publish or stage rebuild rows for NC* / ShareAlike so the 39-row queue (8×B, 1×C, 30×E) can be scored.  
2. Finish stratum E (Chemotion SA) band-match vs deposit lists (preview often truncated vs 18–78-band Chemotion strings).  
3. Optional cleanup pass on known mass/MW/LC–MS contamination and R² mismatches before claiming full human-audit closure.  
4. Overleaf: no git remote in this clone — **Pull from GitHub** after origin/main push (no force).
