<p align="center">
  <img src="figures/irexp_logo.svg" alt="IRexp" width="520">
</p>

<p align="center">
  <a href="https://huggingface.co/datasets/ilkhamfy/IRexp"><img src="https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-IRexp-C2410C" alt="Hugging Face"></a>
  <a href="https://doi.org/10.5281/zenodo.23463965"><img src="https://img.shields.io/badge/DOI-10.5281%2Fzenodo.23463965-6B7280" alt="Zenodo DOI"></a>
  <img src="https://img.shields.io/badge/data-CC--BY--4.0-6B7280" alt="Data licence">
</p>

Experimental infrared spectra are scarce in open, machine-readable form. Most of them sit as band lists in the text of published papers. IRexp extracts these band lists from open-access literature and links them to molecular structures.

## Data

| | Records |
|---|---:|
| Experimental IR band lists | 239,735 |
| Linked to a structure (tiers A–D) | 101,624 |
| Formula or HRMS matched (tiers A–B) | 56,035 |
| Public commercial pool (CC-BY / CC0) | 163,931 |

All bands are within 400–4000 cm⁻¹. Each record keeps its source paper and source licence.

## Get the data

```python
import pandas as pd
from huggingface_hub import hf_hub_download

path = hf_hub_download(
    "ilkhamfy/IRexp",
    "data/irexp_commercial.jsonl.gz",
    repo_type="dataset",
    revision="9ee1aa9b2f462cef8cf18489e45a516a4b716193",
)
df = pd.read_json(path, lines=True)
```

- Hugging Face: [ilkhamfy/IRexp](https://huggingface.co/datasets/ilkhamfy/IRexp)
- Zenodo archive: [10.5281/zenodo.23463965](https://doi.org/10.5281/zenodo.23463965)
- Extraction code: [IlkhamFY/spectro-agent](https://github.com/IlkhamFY/spectro-agent)

## Licence

Commercial pool: CC-BY-4.0, with per-record source licences kept. Code in this repository: MIT.
