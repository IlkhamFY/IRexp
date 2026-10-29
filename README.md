# IRexp — Scientific Data Data Descriptor

Clean manuscript repository for the **IRexp** *Scientific Data* Data Descriptor.

**Main Overleaf file:** `scientific_data.tex`  
**Compiler:** pdfLaTeX (+ BibTeX)  
**Template:** Springer Nature `sn-jnl` (`[pdflatex,sn-nature]`, vendored in `tex/`)

## Layout

```
scientific_data.tex     # source of truth (repo root)
references.bib
latexmkrc               # TEXINPUTS / BSTINPUTS → tex/
tex/                    # sn-jnl.cls + *.bst + sn-article provenance
figures/                # positioning / pipeline / distribution
data/                   # manifests + HF/Zenodo pointers (no large dumps)
docs/                   # checklists and working notes
scripts/build_pdf.py
```

## Build PDF locally

```bash
python3 scripts/build_pdf.py
```

or `latexmk -pdf scientific_data.tex` from the repo root.

## Fence

This repo is **data-descriptor only**. Do not add IRSpectra-Bench diagnosis tables,
LLM accuracy claims, or ICLR manuscript content. Cross-cite the companion research
paper instead.

## Related

- This Data Descriptor (paper + manifests): https://github.com/IlkhamFY/IRexp
- Dataset card / bulk JSONL: https://huggingface.co/datasets/ilkhamfy/IRexp
- Harvest / pipeline code: https://github.com/IlkhamFY/spectro-agent
- Companion research: `IRSpectra-Bench` (ICLR track)
- Live dataset of record: Hugging Face `ilkhamfy/IRexp`, v0.2. Research corpus *n* = 239,735; released structures (tiers A-D) *n* = 101,624; formula/HRMS-matched (tiers A-B) *n* = 56,035; commercial CC-BY/CC0 pool *n* = 163,931. All bands within 400-4000 cm-1.
- Zenodo archives the v0.2 commercial pool (*n* = 163,931): https://doi.org/10.5281/zenodo.23463965 (concept https://doi.org/10.5281/zenodo.22822284). Earlier versions: https://doi.org/10.5281/zenodo.23023528 (commercial *n* = 88,519) and https://doi.org/10.5281/zenodo.22822285 (pre-clean snapshot, *n* = 88,545).
