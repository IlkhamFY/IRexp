# IRexp data pointers

Full redistributable dumps are **not** stored in this manuscript repository (size / licence clarity).

## Primary locations

| Artifact | Where |
|---|---|
| Hugging Face dataset | https://huggingface.co/datasets/ilkhamfy/IRexp |
| Zenodo data-only deposit | *DOI pending — do not invent; see `ZENODO_DATA_ONLY_CHECKLIST.md`* |
| Parent code/benchmark monorepo | https://github.com/IlkhamFY/spectro-agent |

## Local manifests (this repo)

- `pmc_licence_summary.json` — Europe PMC licence join summary
- `irexp_stats.json` / `release_stats.json` / `resolved_stats.json` — frozen counts
- `train_no_bench_stats.json` (+ `_nmr`) — held-out split stats
- `NOTICE` — redistribution / licence policy
- `README_HF.md` — Hugging Face dataset card source
- `README_RELEASE.md` — release split notes

## Primary Sci Data / Zenodo file (upload separately)

`irexp_commercial.jsonl.gz` — **88,545** CC-BY/CC0 records (`license_pool=commercial`).

Companion ShareAlike file and NC*/empty pools are documented in `LICENCE_REMEDIATION.md` and `ZENODO_DATA_ONLY_CHECKLIST.md`.
