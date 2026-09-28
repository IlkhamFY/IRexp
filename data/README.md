# IRexp data pointers

Full redistributable dumps are **not** stored in this manuscript repository (size / licence clarity).

## Primary locations

| Artifact | Where |
|---|---|
| This manuscript + frozen manifests | https://github.com/IlkhamFY/IRexp (`data/` here is manifests only — no bulk JSONL) |
| Hugging Face dataset (bulk JSONL) | https://huggingface.co/datasets/ilkhamfy/IRexp |
| Harvest / pipeline code | https://github.com/IlkhamFY/spectro-agent |
| Archival deposit | Zenodo data-only deposit of this Hub revision (commercial *n* = 88,519), https://doi.org/10.5281/zenodo.23023528 (`10.5281/zenodo.23023528`; concept `10.5281/zenodo.22822284`). An earlier version DOI (`10.5281/zenodo.22822285`) archived the pre-clean snapshot (*n* = 88,545). See `ZENODO_DATA_ONLY_CHECKLIST.md` |

## Local manifests (this repo)

- `pmc_licence_summary.json` — Europe PMC licence join summary
- `irexp_stats.json` / `release_stats.json` / `resolved_stats.json` — frozen counts
- `f1_commercial_build_stats.json` — Hub commercial dataset-of-record shared-IR and table-flatten flag rates (flag-only; schema fields `ir_shared_in_paper`, `ir_table_flatten_suspect`)
- `chem_composition.json` — unique-InChIKey MW / aromatic-ring / N-atom / carbonyl histograms (Fig. 3e)
- `train_no_bench_stats.json` (+ `_nmr`) — held-out split stats
- `NOTICE` — redistribution / licence policy
- `README_HF.md` — Hugging Face dataset card source
- `README_RELEASE.md` — release split notes
- `seen_papers.txt.gz` — 188,016 PMC IDs scanned at harvest (not a Hub file)
- `structure_nmr_quarantine.jsonl.gz` — 1,882 diagnostic quarantine IDs (on Zenodo https://doi.org/10.5281/zenodo.23023528; not a Hub file)

## Public Hugging Face files (revision `4312254c279300f881ad12671476e877027ed3da`)

`irexp_commercial.jsonl.gz` — **88,519** CC-BY/CC0 records (dataset of record). `irexp_resolved_commercial.jsonl.gz` — **29,255**. `train_no_bench_commercial.jsonl.gz` — **29,109**. Companions on the same revision: ShareAlike **1,897**, non-commercial **21,823**, CC-BY-ND **5** (`irexp_other.jsonl.gz`). Public downloadable total of the commercial, ShareAlike, and non-commercial files **112,239** (1,256,623 bands; full corpus 1,360,866).

The research corpus remains **121,233**. **8,994** rows lie outside the commercial, ShareAlike, and non-commercial Hub files (8,963 empty/unknown + 5 CC-BY-ND + 26 rows with fewer than three bands). The five CC-BY-ND rows are on the Hub as `irexp_other.jsonl.gz` and are excluded from the commercial dataset of record (*n* = 88,519). Hub revision `4312254c279300f881ad12671476e877027ed3da` sets `has_structure` when SMILES is present and names the non-commercial companion on the dataset card. Zenodo https://doi.org/10.5281/zenodo.23023528 archives this Hub revision (commercial *n* = 88,519). An earlier version DOI (https://doi.org/10.5281/zenodo.22822285) archived the pre-clean commercial snapshot (88,545).
