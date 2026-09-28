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
  - 10K<n<100K
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
---

# IRexp — experimental IR band lists (commercial dataset of record)

**Data Descriptor:** [IRexp: A database of experimental infrared band lists from open literature](https://github.com/IlkhamFY/IRexp). Harvest/pipeline code is [IlkhamFY/spectro-agent](https://github.com/IlkhamFY/spectro-agent).

This Hugging Face repository is the public dataset of record for the commercial pool only. It is packaged under CC-BY-4.0, with per-record CC-BY/CC0 stamps.

IRexp is a collection of **experimental infrared band lists** mined from open-access chemistry papers, often with co-reported ¹H/¹³C shift lists and resolved structures. The multi-licence research corpus holds **121,233** records. That total is not in this upload.

> **Important:** IRexp contains **band lists** (peak positions in cm⁻¹), not digitised absorbance traces. This is the form reported in publication text and is not directly comparable to SDBS or NIST full spectra.

## Dataset summary

Files in this upload:

| Config / file | Records | Description |
|---|---:|---|
| `commercial` / `irexp_commercial.jsonl.gz` | **88,519** | **Dataset of record.** CC-BY-4.0 packaging; per-record CC-BY/CC0 stamps. Hub revision `4312254c279300f881ad12671476e877027ed3da`. Zenodo `10.5281/zenodo.23023528` archives this Hub revision. |
| `resolved_commercial` / `irexp_resolved_commercial.jsonl.gz` | 29,255 | Commercial rows with non-empty SMILES |
| `train_no_bench_commercial` / `train_no_bench_commercial.jsonl.gz` | 29,109 | That subset with benchmark InChIKeys held out |
| `sharealike` / `irexp_sharealike.jsonl.gz` | 1,897 | Companion; CC-BY-SA-4.0; excluded from the CC-BY dataset of record |
| `non_commercial` / `irexp_non_commercial.jsonl.gz` | 21,823 | Companion; NC*; excluded from the CC-BY dataset of record; named on the dataset card |
| `other` / `irexp_other.jsonl.gz` | 5 | Companion; CC-BY-ND; excluded from the CC-BY dataset of record |

Public downloadable total of the commercial, ShareAlike, and non-commercial files: **112,239** (1,256,623 bands). **8,994** rows lie outside those files (8,963 empty/unknown + 5 CC-BY-ND + 26 rows with fewer than three bands). The five CC-BY-ND rows are the `other` companion and are excluded from the commercial dataset of record (*n* = 88,519). Empty/unknown (8,963) and the full multi-licence file (`irexp.jsonl.gz`, 121,233) are not part of this upload. The corpus contains 1,360,866 bands. Zenodo https://doi.org/10.5281/zenodo.23023528 archives this Hub revision (commercial *n* = 88,519). An earlier version DOI (https://doi.org/10.5281/zenodo.22822285) archived the pre-clean commercial snapshot (88,545).

**Provenance:** 119,345 PMC-sourced + 1,888 Chemotion/RADAR4Chem. Per-article stamps (`license` / `license_pool`) are on every row. The card `license` is `cc-by-4.0` for the commercial dataset of record. ShareAlike and NC* companions stay under their source licences and are excluded from that pool. See `NOTICE` and `LICENCE_REMEDIATION.md`.

**Zenodo:** data-only archival deposit of this Hub revision (commercial *n* = 88,519), https://doi.org/10.5281/zenodo.23023528.

## Load

```python
from datasets import load_dataset

# Dataset of record (88,519 commercial rows)
ds = load_dataset("ilkhamfy/IRexp", "commercial", split="train")

# Commercial rows with non-empty SMILES (29,255)
res = load_dataset("ilkhamfy/IRexp", "resolved_commercial", split="train")

# That subset with benchmark InChIKeys held out (29,109)
train = load_dataset("ilkhamfy/IRexp", "train_no_bench_commercial", split="train")
```

## Record schema

`id` is an opaque stable key (a mix of hashes and InChIKey-shaped strings), not a guaranteed molecule join key. InChIKey is stored in `inchikey` and is not unique across structure-linked records in the research corpus (57,646 records; 54,985 InChIKeys). `source_doi` is a source identifier: a PMC accession (`PMC:…`) or a DOI, not always a DOI. Non-commercial and ShareAlike rows use the core columns. The commercial file adds `ir_bands_old_cm-1`, `ir_shared_in_paper`, `ir_table_flatten_suspect`, `ir_refetch_confirmed`, and `ir_refetch_merged` (flag-only where boolean; rows not dropped).

```json
{
  "id": "73c2e8a41a6601afa622",
  "inchikey": null,
  "smiles": "CCOc1cccc2cc(C(C)=O)c(=O)oc12",
  "ir_bands_cm-1": [3060.0, 2976.0, 2874.0, 1730.0, 1678.0],
  "h_nmr": "...",
  "c_nmr": "...",
  "ir_source": "experimental",
  "source_doi": "PMC:6268696",
  "pmcid": "PMC6268696",
  "license": "CC-BY",
  "license_pool": "commercial",
  "license_raw": "cc by",
  "license_source": "europepmc",
  "ir_shared_in_paper": false,
  "ir_table_flatten_suspect": false
}
```

The `id` in this row is an internal identifier, not an InChIKey. Some resolved rows elsewhere in the corpus set `id` equal to the InChIKey as a convenience; that key is still stored in `inchikey`.

## Limitations (read before citing)

- **Band lists, not spectra** — median 9 bands (PMC) vs 39 (Chemotion).
- **Literature-transcribed** — heterogeneous labs/instruments; not raw `.jdx` files.
- **Structure resolution 47.5%** of the research corpus (57,646 / 121,233). Supervised structure tasks on this upload use `resolved_commercial`.
- **Dataset of record is the commercial pool.** ShareAlike, NC*, and the CC-BY-ND `other` companion are on the same revision and are excluded from that pool. Empty/unknown and the full multi-licence dump are not here.
- **Extraction recall** of IR strings per paper is not a completed human audit (transcription fidelity: 560/560 bands on n=60).

## Links

- **Dataset (Hugging Face):** https://huggingface.co/datasets/ilkhamfy/IRexp
- **Data Descriptor (paper + manifests):** https://github.com/IlkhamFY/IRexp
- **Harvest / pipeline code:** https://github.com/IlkhamFY/spectro-agent
- **Zenodo:** this Hub revision (commercial *n* = 88,519), https://doi.org/10.5281/zenodo.23023528
- **Licence details:** `NOTICE` / `LICENCE_REMEDIATION.md`

When uploading to Hugging Face, this file is the repository `README.md`.
