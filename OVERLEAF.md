# Overleaf setup — IRexp (Scientific Data)

## Recommended: GitHub sync

1. Create GitHub repo `IlkhamFY/IRexp` and push this tree to `main`.
2. Overleaf → **New Project** → **Import from GitHub** → select `IlkhamFY/IRexp`.
3. Menu → **Main document** → `scientific_data.tex`.
4. Menu → **Compiler** → **pdfLaTeX**.
5. Recompile; BibTeX runs automatically on Overleaf for the bibliography.

## Alternative: zip upload

1. Upload `IRexp-overleaf.zip` (see `artifacts/` from the parent export).
2. Set main document to `scientific_data.tex`.
3. Compiler: **pdfLaTeX**.

## Folder structure Overleaf sees

```
scientific_data.tex
references.bib
sn-jnl.cls
sn-nature.bst (+ other .bst)
figures/*.pdf
sn-article/   (optional provenance; not required to compile)
```

## What NOT to upload

- Large `*.jsonl.gz` data dumps (use HF / Zenodo)
- Symlinks (Overleaf rejects them) — this tree has none
- Agent meta / peer-review simulation dumps
- IRSpectra-Bench / ICLR manuscript files
- Secrets, tokens, `.env`

## Notes

- Class option matches pdfLaTeX: `pdflatex,sn-nature` on `sn-jnl`.
- Figures resolve via `graphicspath` to `figures/`.
- *Scientific Data* may ask for a flattened standalone `.tex` at revision; this package is for authoring/review.
