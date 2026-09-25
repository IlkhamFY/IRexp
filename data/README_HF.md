---
language:
  - en
license:
  - cc-by-4.0
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
| `commercial` / `irexp_commercial.jsonl.gz` | **88,545** | **Dataset of record.** CC-BY-4.0 packaging; per-record CC-BY/CC0 stamps. Zenodo primary file. |
| `resolved_commercial` / `irexp_resolved_commercial.jsonl.gz` | 28,899 | Structure-linked commercial subset |
| `train_no_bench_commercial` / `train_no_bench_commercial.jsonl.gz` | 28,753 | `resolved_commercial` with benchmark InChIKeys held out |

Retained for research and **not part of this public DoR upload**: non-commercial (NC*, 21,823), ShareAlike (1,897; Chemotion CC-BY-SA-4.0 plus rare PMC SA), ND (5; CC-BY-ND), empty/unknown (8,963), and the full multi-licence file (`irexp.jsonl.gz`, 121,233).

**Provenance:** 119,345 PMC-sourced + 1,888 Chemotion/RADAR4Chem. Per-article stamps (`license` / `license_pool`) are on every commercial row. The card `license` is `cc-by-4.0` for this commercial upload. ShareAlike and NC* source stamps apply to corpus pools that are not in this upload. See `NOTICE` and `LICENCE_REMEDIATION.md`.

**Zenodo:** data-only archival deposit of this commercial pool, https://doi.org/10.5281/zenodo.22822285.

## Load

```python
from datasets import load_dataset

# Dataset of record (88,545 commercial rows)
ds = load_dataset("ilkhamfy/IRexp", "commercial", split="train")

# Structure-linked commercial subset (28,899)
res = load_dataset("ilkhamfy/IRexp", "resolved_commercial", split="train")

# Commercial subset with benchmark InChIKeys held out (28,753)
train = load_dataset("ilkhamfy/IRexp", "train_no_bench_commercial", split="train")
```

## Record schema

`id` is a unique stable internal record identifier. InChIKey is stored in `inchikey` and is not unique across structure-linked records in the research corpus (57,646 records; 54,985 InChIKeys). `source_doi` is a source identifier: a PMC accession (`PMC:…`) or a DOI, not always a DOI. `ir_shared_in_paper` and `ir_table_flatten_suspect` are on the commercial dataset of record only (flag-only; rows not dropped).

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
- **This upload is the commercial pool only.** NC*, ShareAlike, ND, empty/unknown, and the full multi-licence dump are not here.
- **Extraction recall** of IR strings per paper is not a completed human audit (transcription fidelity: 560/560 bands on n=60).

## Links

- **Dataset (Hugging Face):** https://huggingface.co/datasets/ilkhamfy/IRexp
- **Data Descriptor (paper + manifests):** https://github.com/IlkhamFY/IRexp
- **Harvest / pipeline code:** https://github.com/IlkhamFY/spectro-agent
- **Zenodo:** commercial pool, https://doi.org/10.5281/zenodo.22822285
- **Licence details:** `NOTICE` / `LICENCE_REMEDIATION.md`

When uploading to Hugging Face, this file is the repository `README.md`.
