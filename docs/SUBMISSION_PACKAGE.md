# IRexp — Scientific Data + ChemRxiv submission package

**Repo HEAD verified:** `84278e0` (`release v0.49`, Ilkham Yabbarov \<ilkhamfy@gmail.com\>)  
**Overleaf:** https://www.overleaf.com/project/6aa1a6fefdbc206fbf60ab24 — Pull’d to v0.49; manuscript ~18 pp / 0 errors; cover letter ~1 pp with Zenodo DOI  
**Do not invent DOIs, ORCIDs, reviewer names, or counts beyond this package and the TeX sources.**

---

## Extracted manuscript facts (from `scientific_data.tex` / cover letter)

| Field | Value |
|---|---|
| **Title** | IRexp: A database of experimental infrared band lists from open literature |
| **Authors** | Ilkham Yabbarov\* (yabbaroi@mcmaster.ca); Rudra Sondhi; Rodrigo A. Vargas-Hernández\* (vargashr@mcmaster.ca) |
| **Affiliations** | (1) Department of Chemistry and Chemical Biology, McMaster University, Hamilton, Ontario L8S 4L8, Canada; (2) Brockhouse Institute for Materials Research, McMaster University; (3) School of Computational Science and Engineering, McMaster University. \* corresponding |
| **Signatory (cover)** | Rodrigo Vargas-Hernández \<vargashr@mcmaster.ca\> |
| **Funding** | NSERC #596133-2025 (CREATE AccelD / Acceleration Consortium) |
| **HF DoR** | `ilkhamfy/IRexp` — commercial n=88,545; full corpus n=121,233 |
| **Zenodo version DOI** | https://doi.org/10.5281/zenodo.22822285 |
| **Zenodo concept DOI** | https://doi.org/10.5281/zenodo.22822284 |
| **Main TeX** | `scientific_data.tex` |
| **Cover TeX** | `cover_letter/cover_letter.tex` |

### Abstract (verbatim sense from TeX)

IRexp is a redistributable collection of experimental infrared band lists (cm⁻¹ peak positions) mined from open chemistry literature, optionally with author-reported ¹H/¹³C NMR strings and resolved structures. The release holds 121,233 records (119,345 PMC Open Access Subset; 1,888 Chemotion/RADAR4Chem), including 43,060 structure-linked entries and 33,201 IR + ¹H + ¹³C + structure quadruples. IRexp stores numeric band lists, not absorbance traces; each record carries a source DOI and a stamped licence pool (88,545 commercially redistributable CC-BY/CC0 records). Intended reuse is multimodal training, retrieval, and tool input for spectroscopic workflows that need structured, attributable experimental peak lists rather than paywalled PDFs or view-only archives. Technical validation covers automated transcription, harvest-path recall proxies, stratified automated consistency audits, full-corpus quarantine, and a stratified expert human band-list audit of 161 records available on the commercial Hugging Face dataset of record (39 stratified NC*/ShareAlike queue rows are absent from that publish and were not scored). Complementary elucidation benchmarks are described in a companion research manuscript and are not analysed here.

### Data availability (summary)

- **Dataset of record:** commercial CC-BY/CC0 pool n=88,545 on Hugging Face `ilkhamfy/IRexp` (revision `8db58466e3ddfd2fbe09bd47fdd5eb4cfc3e1975`) + Zenodo https://doi.org/10.5281/zenodo.22822285  
- **Full construction corpus:** n=121,233 (methodology reference; not the Sci Data commercial redistribution artefact)  
- **Code:** https://github.com/IlkhamFY/spectro-agent (MIT)  
- **Manuscript + manifests + figures:** https://github.com/IlkhamFY/IRexp — **keep public until after real submit** (Access § still cites it; do not hide GH now)

### DOI verification (v0.49)

| Check | Status |
|---|---|
| Cover letter cites Zenodo version DOI `10.5281/zenodo.22822285` | ✓ |
| Cover letter has **no** “not yet minted” for the **data** DOI | ✓ |
| Manuscript Data Availability cites same Zenodo version DOI | ✓ |
| Manuscript Code Availability software-DOI hedge (“archival software DOI … not yet minted”) | ✓ intentional — leave as-is |

---

## Pre-submit checklist

- [x] Overleaf synced to GitHub `release v0.49` / `84278e0`
- [x] Cover letter PDF/source includes Zenodo data DOI (no data-DOI “not yet minted”)
- [x] Manuscript compiles clean on Overleaf (~18 pp, 0 errors) — human-confirmed
- [x] Software DOI hedge left intentional
- [ ] **Keep** GitHub manuscript public through ChemRxiv + Sci Data upload (**hide only after real submit**)
- [ ] Confirm ORCID — I. Yabbarov (still open in `HUMAN_SUBMISSION_CHECKLIST.md`)
- [ ] Confirm ORCID — R. A. Vargas-Hernández (candidate `0000-0002-5559-6521` — confirm before eJP)
- [ ] Suggested reviewers — **ask Rodrigo** (none listed in repo files)
- [ ] Export final PDFs from Overleaf: manuscript + cover letter
- [ ] ChemRxiv preprint upload, then Scientific Data eJP (order: ChemRxiv first is usual; follow journal policy)
- [ ] After **both** portals accept the upload / assignment: optionally privatize or comment GH manuscript links — **not before**

Also see: `docs/HUMAN_SUBMISSION_CHECKLIST.md`, `docs/ZENODO_DATA_ONLY_CHECKLIST.md` (data DOI already minted).

---

## ChemRxiv prep sheet

| Portal field | Value to paste |
|---|---|
| Title | IRexp: A database of experimental infrared band lists from open literature |
| Article type | Preprint (chemistry / cheminformatics / spectroscopy data) |
| Authors + emails | Ilkham Yabbarov \<yabbaroi@mcmaster.ca\>; Rudra Sondhi; Rodrigo A. Vargas-Hernández \<vargashr@mcmaster.ca\> |
| Affiliations | McMaster University — Chemistry & Chemical Biology; Brockhouse Institute for Materials Research; School of Computational Science and Engineering (Hamilton, ON, Canada) |
| Abstract | (paste from TeX abstract above) |
| Keywords | infrared spectroscopy, band lists, peak lists, PMC Open Access, Chemotion, FAIR data, licence pools, data descriptor |
| Funding | NSERC 596133-2025 (CREATE for Accelerated Discovery, AccelD), Acceleration Consortium |
| Data availability | HF `ilkhamfy/IRexp` (commercial n=88,545); Zenodo https://doi.org/10.5281/zenodo.22822285; full corpus n=121,233 described in manuscript; code `IlkhamFY/spectro-agent`; manuscript repo `IlkhamFY/IRexp` |
| Upload files | Manuscript PDF (from Overleaf); optional SI if any; do **not** upload bulk JSONL |
| Cover letter | Not required by ChemRxiv typically — keep Sci Data cover for journal portal |
| License | Follow ChemRxiv default CC-BY (confirm at upload) |
| Competing interests / ethics | None beyond manuscript statements |

---

## Scientific Data (eJP) portal prep sheet

| Portal field | Value to paste |
|---|---|
| Journal | *Scientific Data* |
| Article type | Data Descriptor |
| Title | IRexp: A database of experimental infrared band lists from open literature |
| Authors | Ilkham Yabbarov; Rudra Sondhi; Rodrigo A. Vargas-Hernández |
| Corresponding | yabbaroi@mcmaster.ca; vargashr@mcmaster.ca |
| Cover letter | Export from `cover_letter/cover_letter.tex` (signatory Rodrigo Vargas-Hernández) |
| Abstract | (from TeX) |
| Funding | NSERC #596133-2025 (CREATE AccelD / Acceleration Consortium) |
| Data DOI | https://doi.org/10.5281/zenodo.22822285 (concept 10.5281/zenodo.22822284) |
| Code | https://github.com/IlkhamFY/spectro-agent |
| Manuscript repo | https://github.com/IlkhamFY/IRexp (**public at submit time**) |
| HF dataset | https://huggingface.co/datasets/ilkhamfy/IRexp |
| **Suggested reviewers** | **ask Rodrigo** — no suggested-reviewer list found in repo files |
| ORCID | Confirm before submit (see human checklist) |

### Upload file list (Sci Data)

1. **Main manuscript PDF** — Overleaf compile of `scientific_data.tex` (~18 pp)  
2. **Cover letter PDF** — Overleaf / local compile of `cover_letter/cover_letter.tex` (~1 pp, DOI present)  
3. **Source TeX package** (if requested) — `scientific_data.tex`, `references.bib`, `figures/`, `tex/`, `latexmkrc`, `cover_letter/`  
4. **Do not** upload bulk `jsonl` / full commercial dump (point to Zenodo + HF)  
5. Optional: ChemRxiv preprint DOI once minted (cross-link)

---

## Post-submit: hide GitHub manuscript **only after real submit**

1. Complete ChemRxiv upload **and** Scientific Data eJP submission (confirmation emails / manuscript IDs in hand).  
2. **Then** optionally: make `IlkhamFY/IRexp` private, or comment Access / Data Availability GH manuscript URLs in a follow-up revision — **not before**.  
3. Do **not** hide HF dataset or Zenodo record.  
4. spectro-agent code repo stays public (MIT).

---

## Agent notes / environment

- Package drafted against GitHub `main` @ `84278e0` (public clone).  
- QuantumNode paths (`C:\Users\zolot\.openclaw\workspace\paper_repos_build\IRexp` then `...\IRexp`) were the preferred live tree; this executor had no `ListMachines` / remote Shell to QuantumNode — verify on QN that local HEAD matches `84278e0` before pushing further edits from Windows.  
- Cover letter LaTeX compile skipped here if no TeX toolchain on the agent host; Overleaf already builds cleanly.
