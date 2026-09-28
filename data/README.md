# IRexp data pointers

Full redistributable dumps are **not** stored in this manuscript repository (size / licence clarity).

## Primary locations

| Artifact | Where |
|---|---|
| This manuscript + frozen manifests | https://github.com/IlkhamFY/IRexp (`data/` here is manifests only — no bulk JSONL) |
| Hugging Face dataset (bulk JSONL) | https://huggingface.co/datasets/ilkhamfy/IRexp |
| Harvest / pipeline code | https://github.com/IlkhamFY/spectro-agent |
| Archival deposit | Zenodo data-only deposit of this Hub revision (commercial *n* = 88,519), https://doi.org/10.5281/zenodo.23021932 (`10.5281/zenodo.23021932`; concept `10.5281/zenodo.22822284`). An earlier version DOI (`10.5281/zenodo.22822285`) archived the pre-clean snapshot (*n* = 88,545). See `ZENODO_DATA_ONLY_CHECKLIST.md` |

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
- `structure_nmr_quarantine.jsonl.gz` — 1,882 diagnostic quarantine IDs (not a Hub file)

## Public Hugging Face files (revision `fc238e3b600f556045bc9a3f7a37738734620cd8`)

`irexp_commercial.jsonl.gz` — **88,519** CC-BY/CC0 records (dataset of record). `irexp_resolved_commercial.jsonl.gz` — **29,255**. `train_no_bench_commercial.jsonl.gz` — **29,109**. Companions on the same revision: ShareAlike **1,897**, non-commercial **21,823**. Public downloadable total **112,239**.

The research corpus remains **121,233**. About **8,994** rows are withheld (empty/unknown licence 8,963, ND 5 with release deferred, and 26 commercial-stamp rows removed by the reapplied ≥3-band filter). Zenodo https://doi.org/10.5281/zenodo.23021932 archives this Hub revision (88,519). An earlier version DOI (https://doi.org/10.5281/zenodo.22822285) archived the pre-clean commercial snapshot (88,545).
