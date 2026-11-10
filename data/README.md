# IRexp data pointers

Full redistributable dumps are not stored in this manuscript repository.

## Primary locations

| Artifact | Where |
|---|---|
| This manuscript, manifests, and figures | https://github.com/IlkhamFY/IRexp |
| Dataset (JSONL files under `data/`) | https://huggingface.co/datasets/ilkhamfy/IRexp |
| Archive | https://doi.org/10.5281/zenodo.24117617 (concept: https://doi.org/10.5281/zenodo.22822284) |
| Harvest and pipeline code | https://github.com/IlkhamFY/spectro-agent |

## Deposit

230,946 records in three files, plus a quarantine sidecar:

| File | Records |
|---|---:|
| `irexp_commercial.jsonl.gz` | 190,049 (dataset of record: 164,016 CC-BY/CC0 and 26,033 from no-derivatives-licensed articles, marked `nd_source_licence`) |
| `irexp_non_commercial.jsonl.gz` | 39,000 (CC-BY-NC and CC-BY-NC-SA) |
| `irexp_sharealike.jsonl.gz` | 1,897 (CC-BY-SA, including 1,888 Chemotion records) |
| `structure_quarantine.jsonl.gz` | 8,457 ids (8,158 withheld tier-X and 299 formula–NMR flags) |

Checksums of those files are in `SHA256SUMS.txt`. `seen_papers.txt.gz` lists PMC identifiers scanned during harvest. 8,789 harvested records without an established licence are not deposited.

Filter on `nd_source_licence` to keep only records whose source licence permits adaptation. Licence details: `NOTICE`.
