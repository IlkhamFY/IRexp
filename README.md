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

- Data on Hugging Face: https://huggingface.co/datasets/ilkhamfy/IRexp
- Companion research: `IRSpectra-Bench` (ICLR track)
- Historical monorepo: https://github.com/IlkhamFY/spectro-agent
