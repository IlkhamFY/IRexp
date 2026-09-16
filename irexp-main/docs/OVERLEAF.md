# Overleaf setup — IRexp (Scientific Data)

## GitHub sync
1. Import `IlkhamFY/IRexp` from GitHub.
2. Main document: `scientific_data.tex` (repo root).
3. Compiler: **pdfLaTeX**.
4. Styles resolve via `latexmkrc` → `tex/`.

## Root (postcard)
`README.md`, `LICENSE`, `scientific_data.tex`, `references.bib`, `.gitignore`, `latexmkrc`.

## Folders
- `tex/` — sn-jnl.cls, bst files, sn-article provenance
- `figures/`, `scripts/`, `data/`, `docs/`

## Bibliography
`latexmkrc` sets `TEXINPUTS` / `BSTINPUTS` so pdfLaTeX and BibTeX find `sn-jnl.cls`
and `sn-nature.bst` under `tex/`. Do not add a second `\bibliographystyle` — the
class option `[sn-nature]` already writes one, and a duplicate is a BibTeX error.

