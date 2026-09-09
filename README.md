# IRexp — Scientific Data Data Descriptor

Clean manuscript repository for the **IRexp** *Scientific Data* Data Descriptor.

**Main Overleaf file:** `scientific_data.tex`  
**Compiler:** pdfLaTeX (+ BibTeX)  
**Template:** Springer Nature `sn-jnl` (`[pdflatex,sn-nature]`, vendored)

## Layout

```
scientific_data.tex     # source of truth
references.bib
sn-jnl.cls + *.bst
figures/                # Fig. positioning / pipeline / distribution
sn-article/             # full Dec 2024 package provenance
data/                   # manifests + HF/Zenodo pointers (no large dumps)
scripts/build_pdf.py
HUMAN_SUBMISSION_CHECKLIST.md
LICENCE_REMEDIATION.md
ZENODO_DATA_ONLY_CHECKLIST.md
OVERLEAF.md
COMMIT_POLICY.md
```

## Build PDF locally

```bash
python3 scripts/build_pdf.py
```

## Fence

This repo is **data-descriptor only**. Do not add IRSpectra-Bench diagnosis tables,
LLM accuracy claims, or ICLR manuscript content. Cross-cite the companion research
paper instead.

## Related

- Data on Hugging Face: https://huggingface.co/datasets/ilkhamfy/IRexp
- Companion research: `IRSpectra-Bench` (ICLR track)
- Historical monorepo: https://github.com/IlkhamFY/spectro-agent
