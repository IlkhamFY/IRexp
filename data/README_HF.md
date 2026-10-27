---
language:
  - en
license:
  - cc-by-4.0
  - cc-by-sa-4.0
  - cc-by-nc-4.0
tags:
  - chemistry
  - spectroscopy
  - infrared
  - nmr
  - cheminformatics
  - open-data
size_categories:
  - 100K<n<1M
pretty_name: IRexp
configs:
  - config_name: commercial
    data_files: data/irexp_commercial.jsonl.gz
  - config_name: resolved_commercial
    data_files: data/irexp_resolved_commercial.jsonl.gz
  - config_name: train_no_bench_commercial
    data_files: data/train_no_bench_commercial.jsonl.gz
  - config_name: sharealike
    data_files: data/irexp_sharealike.jsonl.gz
  - config_name: non_commercial
    data_files: data/irexp_non_commercial.jsonl.gz
  - config_name: other
    data_files: data/irexp_other.jsonl.gz
  - config_name: structure_quarantine
    data_files: data/structure_quarantine.jsonl.gz
---

# IRexp: experimental IR band lists

IRexp is an openly redistributable collection of **experimental infrared band lists** mined from open-access chemistry literature (PMC Open Access main text and supporting information) and a Chemotion deposit, often with co-reported ¹H/¹³C NMR strings and resolved structures (SMILES / InChIKey / SELFIES).

> **Important:** IRexp contains **band lists** (peak positions in cm⁻¹), not digitised absorbance traces.

This repository is the Scientific Data **dataset of record (DoR)** for the commercial (CC-BY / CC0) pool, plus separately licensed companions on the same revision. It is a data release only: no model scores are shipped here.

## Files on this revision

| Config / file | Records | Role |
|---|---:|---|
| `commercial` / `data/irexp_commercial.jsonl.gz` | **163,931** | **Dataset of record**: CC-BY + CC0; CC-BY-4.0 packaging |
| `resolved_commercial` / `data/irexp_resolved_commercial.jsonl.gz` | 67,235 | Commercial rows with a structure (tiers A–D) |
| `train_no_bench_commercial` / `data/train_no_bench_commercial.jsonl.gz` | 67,093 | That subset without the 248 benchmark InChIKey-14 keys |
| `sharealike` / `data/irexp_sharealike.jsonl.gz` | 1,897 | Companion: Chemotion + rare PMC ShareAlike; CC-BY-SA-4.0; **excluded from** the CC-BY DoR |
| `non_commercial` / `data/irexp_non_commercial.jsonl.gz` | 65,007 | Companion: NC* (CC-BY-NC, CC-BY-NC-ND, CC-BY-NC-SA, stamped per row); **excluded from** the CC-BY DoR |
| `other` / `data/irexp_other.jsonl.gz` | 5 | Companion: CC-BY-ND; **excluded from** the CC-BY DoR |
| `structure_quarantine` / `data/structure_quarantine.jsonl.gz` | 8,431 | Ids only: tier-X structures withheld (8,132) plus formula–NMR diagnostic flags (299) |

Also present: `data/seen_papers.txt.gz` (220,159 PMC identifiers scanned), `data/irexp_release_build_stats.json`, `data/SHA256SUMS.txt`, `NOTICE`, `LICENCE_REMEDIATION.md`, `scripts/release_check.py`, `scripts/build_release.py`.

Public downloadable total (commercial + non-commercial + ShareAlike + ND): **230,840**. The research corpus is **239,735** records; the 8,895 rows with an empty or unknown licence are not redistributed.

## What changed in this release

1. **IR-attachment fix (v4 parser).** IR blocks are assigned within each compound's own section of the experimental text instead of to the nearest NMR block. Rows whose IR belonged to a neighbouring compound were repaired or removed. The PMC main-text part is now 116,320 research rows (previously 119,345).
2. **Supporting-information expansion.** 121,527 new band lists from the SI files of 5,688 PMC Open Access papers, parsed with the same rules (≥3 bands, 400–4000 cm⁻¹, within-list integer-band dedup, dedup against existing rows, licence join per article). Rows from articles without a redistributable licence were not kept.
3. **Strict structure tiers.** Every structure now carries `structure_tier`:

| Tier | Rule | Research corpus (239,735) |
|---|---|---:|
| A | formula/HRMS match in the compound's own block **plus** an independent second method (PubChem name lookup or OCSR drawing) agreeing on InChIKey-14 | 7,366 |
| B | formula/HRMS match in the own block | 48,669 |
| C | no formula; the source passed a ≥97% held-out agreement check | 21,455 |
| D | IR-only rows, OCSR without a formula, or the Chemotion deposit structure on IR-only rows | 24,134 |
| X | contradiction (for example IR and NMR from two different compounds, invalid or salt structure): **structure withheld**, row kept | 8,473 |
| none | no structure | 129,638 |

Tiers A–B: 56,035 (23.4%). Tiers A–D (rows with a released structure): 101,624 (42.4%). OCSR alone is never tier A. Methods ship only at ≥97% held-out precision.

## New and changed columns

- `structure_tier` (A/B/C/D/X/null), `structure_method`, `structure_second_method` (tier A only), `formula_match`, `structure_flags` (`formula_conflict`, `pubchem_conflict`, IR plausibility flags; flag-only).
- `source_set`: `pmc_v4` (main text), `si_2026` (supporting information), `chemotion`.
- SI rows also carry `si_label`, `si_name`, `ir_raw` (author IR string) and `parser`.
- `ir_bands_old_cm-1` on SI rows is the list before within-list integer dedup. `ir_table_flatten_suspect` is null on SI rows (not computed for that set).

## Quality checks (automated)

- OCSR label-B rule on 100 held-out papers: 104/104 (Wilson 96.4–100%). On the full main-text OCSR run the same rule scored 95.1%, below the 97% bar, so those structures were shipped as tier D only.

## Licence

- Commercial DoR: YAML `cc-by-4.0` packaging; per-record source licences stamped.
- ShareAlike companion: CC-BY-SA-4.0. Do not relicense as CC-BY.
- Non-commercial companion: YAML lists `cc-by-nc-4.0` so the card reflects the NC pool; **the per-row policy licences apply** (CC-BY-NC, CC-BY-NC-ND, CC-BY-NC-SA). Not part of the CC-BY DoR.
- Other companion: five CC-BY-ND rows; not part of the CC-BY DoR.
- Every row carries `license`, `license_pool`, `license_raw`, `license_source`, plus `source_doi` / `pmcid` / `doi`.
- Only extracted numbers and identifiers are redistributed; no article text, figures or PDFs.

## Load

```python
from datasets import load_dataset

dor = load_dataset("ilkhamfy/IRexp", "commercial", split="train")
res = dor.filter(lambda r: r["structure_tier"] in ("A", "B"))  # formula-verified structures
nc = load_dataset("ilkhamfy/IRexp", "non_commercial", split="train")
```

## Training without benchmark leakage

`train_no_bench_commercial` withholds the 248 InChIKey-14 keys of the locked benchmark rounds (locked 194 and electrolyte). Keys of later expansion rounds are not filtered, so fine-tuned models should be scored on the locked 194.

## Citation

Cite the Scientific Data Data Descriptor (when published) and this Hub revision. Zenodo version DOI for the commercial files of this release: https://doi.org/10.5281/zenodo.23463965 (concept DOI, always the latest version: https://doi.org/10.5281/zenodo.22822284).

## Links

- Dataset: https://huggingface.co/datasets/ilkhamfy/IRexp
- Manuscript / figures: https://github.com/IlkhamFY/IRexp
- Extraction tooling: https://github.com/IlkhamFY/spectro-agent
- Licence details: `NOTICE`, `LICENCE_REMEDIATION.md`

## Previous revision

`4312254c279300f881ad12671476e877027ed3da`: commercial DoR 88,519 (archived at https://doi.org/10.5281/zenodo.23023528).
