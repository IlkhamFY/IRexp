---
language:
  - en
license:
  - cc-by-4.0
  - cc-by-sa-4.0
tags:
  - chemistry
  - spectroscopy
  - infrared
  - nmr
  - structure-elucidation
  - cheminformatics
size_categories:
  - 100K<n<1M
pretty_name: IRexp
configs:
  - config_name: commercial
    data_files: data/irexp_commercial.jsonl.gz
  - config_name: resolved
    data_files: data/irexp_resolved.jsonl.gz
  - config_name: train_no_bench
    data_files: data/train_no_bench.jsonl.gz
  - config_name: train_no_bench_nmr
    data_files: data/train_no_bench_nmr.jsonl.gz
  - config_name: pretrain_ir
    data_files: data/pretrain_ir.jsonl.gz
  - config_name: non_commercial
    data_files: data/irexp_non_commercial.jsonl.gz
  - config_name: sharealike
    data_files: data/irexp_sharealike.jsonl.gz
  - config_name: other
    data_files: data/irexp_other.jsonl.gz
---

# IRexp — experimental IR band lists from open-access literature

**Data Descriptor:** [IRexp: A database of experimental infrared band lists from open literature](https://github.com/IlkhamFY/IRexp) (*Scientific Data* manuscript). Bulk JSONL is this Hugging Face dataset; harvest/pipeline code is [IlkhamFY/spectro-agent](https://github.com/IlkhamFY/spectro-agent).

IRexp is a collection of **experimental infrared band lists** mined from open-access chemistry papers, often with co-reported ¹H/¹³C shift lists and resolved structures. The multi-licence research corpus holds **121,233** records. Public redistribution is limited to stamped-licence pools.

> **Important:** IRexp contains **band lists** (peak positions in cm⁻¹), not digitised absorbance traces. This is the form reported in publication text — the regime IRSpectra-Bench evaluates — and is not directly comparable to SDBS or NIST full spectra.

## Dataset summary

Public redistributable files:

| Split / file | Records | Packaging |
|---|---:|---|
| `irexp_commercial.jsonl.gz` | **88,545** | **Commercial dataset of record.** CC-BY-4.0 packaging; per-record CC-BY/CC0 stamps (`license_pool=commercial`). Zenodo primary file. |
| `irexp_sharealike.jsonl.gz` | 1,897 | CC-BY-SA-4.0 (Chemotion + rare PMC SA). |
| `irexp_non_commercial.jsonl.gz` | 21,823 | Source-stamped NC*. Packaging is research redistribution under those terms. |
| `irexp_other.jsonl.gz` | 5 | Source-stamped CC-BY-ND. Packaging is research redistribution under those terms. |

Not redistributed: the full multi-licence file (`irexp.jsonl.gz`, 121,233) and the empty/unknown rows (8,963). Those counts stay in the research-corpus description. Empty/unknown rows are removed from the public Hugging Face redistribution.

Research splits below are multi-licence. They are not a single-licence public deposit; filter by `license_pool` or use the stamped pools above.

| Split / file | Records | Description |
|---|---:|---|
| `irexp_resolved.jsonl.gz` | 57,646 | Structure-linked research split (multi-licence) |
| … full IR + ¹H + ¹³C + structure | 39,118 | Multimodal quadruples in the research corpus |
| `train_no_bench.jsonl.gz` | 42,808 | `irexp_resolved` minus IRSpectra-Bench InChIKey-14 (multi-licence) |
| `train_no_bench_nmr.jsonl.gz` | 32,949 | Same, requiring both ¹H and ¹³C |

**Provenance & licensing:** 119,345 PMC-sourced + 1,888 Chemotion/RADAR4Chem. Per-article Europe PMC join stamps `license` / `license_pool` on every row (`scripts/join_pmc_licences.py`). **Commercial training / Zenodo primary = `commercial` config (88,545), CC-BY-4.0 packaging.** The card `license` list is `cc-by-4.0` (commercial packaging) and `cc-by-sa-4.0` (ShareAlike file). NC* and ND files are separate stamped pools and are not covered by the CC-BY-4.0 packaging. See `NOTICE` and `LICENCE_REMEDIATION.md`.

**Companion benchmark:** [IRSpectra-Bench](https://github.com/IlkhamFY/spectro-agent/blob/main/docs/LEADERBOARD.md) — 194 blind elucidation problems built from IRexp; score submissions with `scripts/score_submission.py`.

## Load in three lines

```python
from datasets import load_dataset

# Structure-linked research split (57,646; multi-licence — filter license_pool)
ds = load_dataset("ilkhamfy/IRexp", "resolved", split="train")

# Preferred redistributable commercial pool
comm = load_dataset("ilkhamfy/IRexp", "commercial", split="train")

row = ds[0]
print(row["ir_bands_cm-1"][:5], row["smiles"][:40])
```

For **fine-tuning without benchmark leakage**, use the `train_no_bench` config:

```python
ds = load_dataset("ilkhamfy/IRexp", "train_no_bench", split="train")
```

Or load a file path directly:

```python
ds = load_dataset("ilkhamfy/IRexp", data_files="data/train_no_bench.jsonl.gz", split="train")
```

## Record schema

`id` is a unique stable internal record identifier. The example below is a resolved row and sets `id` to that row's InChIKey; that is a convenience for the example. InChIKey is stored in `inchikey` and is not unique across structure-linked records (57,646 records; 54,985 InChIKeys). `source_doi` is a source identifier: a PMC accession (`PMC:…`) or a DOI, not always a DOI. `ir_shared_in_paper` and `ir_table_flatten_suspect` exist on the commercial dataset of record only.

Each JSONL row:

```json
{
  "id": "AJCQUIFRMABSOZ-UHFFFAOYSA-N",
  "inchikey": "AJCQUIFRMABSOZ-UHFFFAOYSA-N",
  "smiles": "Cc1ccccc1NC(=O)Cn1cc...",
  "selfies": "[C][C][=C]...",
  "ir_bands_cm-1": [3318.0, 3146.0, 1704.0],
  "h_nmr": "9.79 (s, 1H, NH-amide), ...",
  "c_nmr": "164.87, 161.57, ...",
  "ir_source": "experimental",
  "source_doi": "PMC:13234927",
  "pmcid": "PMC13234927",
  "license": "CC-BY",
  "license_pool": "commercial",
  "license_source": "europepmc"
}
```

## Training vs benchmarking

| Use case | File | Benchmark overlap |
|---|---|---|
| Pretrain IR encoder | commercial DoR, or `pretrain_ir.jsonl.gz` (multi-licence research split) | N/A (mostly unlabeled) |
| Supervised IR→structure | commercial DoR; `train_no_bench.jsonl.gz` is the multi-licence holdout split | **None** on that split (248 IK-14 held out) |
| Evaluate elucidation | [IRSpectra-Bench](https://github.com/IlkhamFY/spectro-agent/blob/main/docs/LEADERBOARD.md) | — |
| ⚠️ Legacy split | `irexp_release/train.jsonl.gz` | **117/200 IK-14 overlap** — do not use for benchmark evaluation |

Rebuild the held-out training pool:

```bash
python scripts/build_train_no_bench.py              # 42,808 rows
python scripts/build_train_no_bench.py --require-nmr  # 32,949 rows (H+C required)
```

## Limitations (read before citing)

- **Band lists, not spectra** — median 9 bands (PMC) vs 39 (Chemotion).
- **Literature-transcribed** — heterogeneous labs/instruments; not raw `.jdx` files.
- **Structure resolution 47.5%** of the research corpus (57,646 / 121,233); supervised structure tasks need a structure-linked subset of a stamped-licence pool.
- **Extraction recall** of IR strings per paper not yet human-audited (transcription fidelity audited: 560/560 bands on n=60).

## Citation

```bibtex
@article{yabbarov2026irspectra,
  title   = {{IRexp} and {IRSpectra-Bench}: redistributable experimental {IR} band lists,
             a blind peak-list benchmark, and a recall-bound diagnosis of {LLM} elucidation},
  author  = {Yabbarov, Ilkham and Sondhi, Rudra and Vargas-Hern{\'a}ndez, Rodrigo A.},
  year    = {2026},
  note    = {Manuscript in preparation; target J. Chem. Inf. Model.}
}
```

## Links

- **Dataset (Hugging Face):** https://huggingface.co/datasets/ilkhamfy/IRexp
- **Data Descriptor (paper + manifests):** https://github.com/IlkhamFY/IRexp
- **Harvest / pipeline code:** https://github.com/IlkhamFY/spectro-agent
- **Companion benchmark:** https://github.com/IlkhamFY/spectro-agent/blob/main/docs/LEADERBOARD.md
- **Zenodo:** data-only archival deposit of the commercial CC-BY/CC0 pool, https://doi.org/10.5281/zenodo.22822285 (`10.5281/zenodo.22822285`)
- **Licence details:** `NOTICE` / `LICENCE_REMEDIATION.md` (this card’s sibling files; also `docs/LICENCE_REMEDIATION.md` on IRexp)

When uploading to Hugging Face, this file is the repository `README.md`.
