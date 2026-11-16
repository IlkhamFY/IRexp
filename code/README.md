# IRexp code

Harvest, extraction, structure resolution, licence handling and validation code used to build IRexp. Licence: MIT (see `LICENSE`).

## Install

```bash
cd code
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

`py2opsin` needs a Java runtime for name-to-structure resolution. Without it (or without RDKit) records are still extracted but left unresolved.

## Run order

Run from `code/`. Working files go to `code/data/`, which is not tracked.

1. Harvest PMC Open Access full text and extract IR/NMR band lists:
   `python scripts/s3_ir_harvest.py --target 250000 --out data/irexp`
2. Ingest the Chemotion FT-IR deposit:
   `python scripts/chemotion_to_irexp.py --root <chemotion dataset dir> --out data/chemotion/chemotion_ir.jsonl`
3. Re-parse IR bands with the thousands-separator fix:
   `python scripts/rebuild_ir_bands_from_raw.py`, then `python scripts/refetch_unmatched_pmc_ir.py` for rows without stored raw text
4. Join source licences and split into pools:
   `python scripts/join_pmc_licences.py`,
   `python scripts/apply_crossref_licence_recovery.py`,
   `python scripts/split_license_pools.py --write <out dir>`
5. Quality flags and quarantine:
   `python scripts/flag_ir_quality.py --input <corpus>`, `python scripts/quarantine_structure_nmr.py`
6. Validation audits:
   `python scripts/audit_extraction.py --n 60 --seed 0`,
   `python scripts/audit_extraction_recall.py --n 40 --seed 0`,
   `python scripts/audit_chemist_proxy.py --n 280 --seed 0`
7. Release files:
   `python scripts/build_hf_commercial_f1.py`, and `python scripts/build_train_no_bench.py` for a training pool with held-out compounds removed

Structure resolution (name to SMILES, InChIKey, SELFIES) is in `spectro_scraper/normalize.py`. The regex extractor is `spectro_scraper/extract.py`. Every script prints its options with `--help`.

## Tests

```bash
python -m pytest tests -q
```
