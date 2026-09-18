# IRexp reference audit — Crossref / DOI check

**Date:** 2026-09-18 (ET)
**Manuscript:** `scientific_data.tex` + `references.bib`
**Repo HEAD audited:** `7a0c587` (`release v0.50` on `origin/main`)
**Crossref User-Agent:** `IRexp-ReferenceAudit/1.0 (mailto:ilkhamfy@gmail.com)`
**API:** `GET https://api.crossref.org/works/{doi}` (DOI URL-encoded); DataCite fallback for Crossref 404s; bibliographic query for no-DOI entries.

## Scope note (execution environment)

Delegated task requested QuantumNode `machineId` `732973e7-c092-4590-9a37-4297fcbd8d73` paths under `C:\Users\zolot\.openclaw\workspace\paper_repos_build\IRexp\`. This executor Shell/Read schema did **not** route to that machine (`machineId` not effective; commands stayed on the Linux box). Audit was therefore run on the public GitHub clone `IlkhamFY/IRexp` at the commit above (same postcard layout / files). Commit/push of this report targets that GitHub remote.

## Summary counts

| Bucket | Count |
|--------|------:|
| Crossref OK (title/year/author align) | 26 |
| Crossref metadata mismatch | 0 |
| DOI present but Crossref 404 (validated on DataCite) | 2 |
| No Crossref DOI (software / web / book) | 4 |
| Cite-key issues (cited∉bib or bib∉cited) | 0 |
| **Bib entries total** | **32** |
| **Unique cite keys in tex** | **32** |

**Top blockers:** none blocking submission. Two DOIs are DataCite-only (not Crossref-indexed); four entries lack Crossref DOIs by nature (software/web/book). No unambiguous DOI typos found — **no `.bib` DOI fixes applied**.

## Cite-key integrity

- Cited but missing from `.bib`: *(none)*
- In `.bib` but uncited in `scientific_data.tex`: *(none)*
- Unique keys cited: 32 — matches bib entry count 32.

## Table A — Crossref OK

| Key | Type | Bib year | CR year | Bib first author | CR family | Title sim | DOI |
|-----|------|---------:|--------:|------------------|-----------|----------:|-----|
| `wang2025nmrexp` | article | 2025 | 2025 | Wang | Wang | 1.0 | `10.1038/s41597-025-06245-5` |
| `zipoli2025uspto` | article | 2025 | 2025 | Zipoli | Zipoli | 1.0 | `10.1038/s41597-025-05729-8` |
| `yang2026nmrtrans` | article | 2026 | 2026 | Yang | Yang | 1.0 | `10.1145/3770855.3818935` |
| `lowe2011opsin` | article | 2011 | 2011 | Lowe | Lowe | 1.0 | `10.1021/ci100384d` |
| `krenn2020selfies` | article | 2020 | 2020 | Krenn | Krenn | 1.0 | `10.1088/2632-2153/aba947` |
| `kim2023pubchem` | article | 2023 | 2023 | Kim | Kim | 1.0 | `10.1093/nar/gkac956` |
| `wilkinson2016fair` | article | 2016 | 2016 | Wilkinson | Wilkinson | 1.0 | `10.1038/sdata.2016.18` |
| `rosonovski2024europepmc` | article | 2024 | 2024 | Rosonovski | Rosonovski | 1.0 | `10.1093/nar/gkad1085` |
| `blum2012atrftir` | article | 2012 | 2012 | Blum | Blum | 0.984 | `10.1002/dta.374` |
| `krasnov2025bigsoldb` | article | 2025 | 2025 | Krasnov | Krasnov | 1.0 | `10.1038/s41597-025-05559-8` |
| `horai2010massbank` | article | 2010 | 2010 | Horai | Horai | 1.0 | `10.1002/jms.1777` |
| `neumann2026massbank` | article | 2026 | 2026 | Neumann | Neumann | 1.0 | `10.1093/nar/gkaf1193` |
| `tremouilhac2017chemotion` | article | 2017 | 2017 | Tremouilhac | Tremouilhac | 1.0 | `10.1186/s13321-017-0240-0` |
| `tremouilhac2020chemotionrepo` | article | 2021 | 2021 | Tremouilhac | Tremouilhac | 1.0 | `10.1002/cmtd.202000034` |
| `swain2016chemdataextractor` | article | 2016 | 2016 | Swain | Swain | 1.0 | `10.1021/acs.jcim.6b00207` |
| `heller2013inchi` | article | 2013 | 2013 | Heller | Heller | 0.992 | `10.1186/1758-2946-5-7` |
| `kemp2022crossref` | article | 2022 | 2022 | Kemp | Kemp | 1.0 | `10.3233/ISU-220170` |
| `hrynaszkiewicz2012open` | article | 2012 | 2012 | Hrynaszkiewicz | Hrynaszkiewicz | 1.0 | `10.1186/1756-0500-5-494` |
| `carroll2011openaccess` | article | 2011 | 2011 | Carroll | Carroll | 1.0 | `10.1371/journal.pbio.1001210` |
| `krishnadas2026squirl` | article | 2026 | 2026 | Krishnadas | Krishnadas | 1.0 | `10.1038/s41597-026-07240-0` |
| `alberts2024multimodal` | article | 2024 | 2024 | Alberts | Alberts | 1.0 | `10.52202/079017-3996` |
| `elyashberg2009case` | article | 2009 | 2009 | Elyashberg | Elyashberg | 1.0 | `10.1186/1758-2946-1-3` |
| `pesek2021elucidation` | article | 2021 | 2021 | Pesek | Pesek | 0.949 | `10.1021/acs.jcim.0c01332` |
| `alberts2024irstruct` | article | 2024 | 2024 | Alberts | Alberts | 1.0 | `10.1038/s42004-024-01341-w` |
| `chacko2024spectro` | article | 2024 | 2024 | Chacko | Chacko | 1.0 | `10.26434/chemrxiv-2024-37v2j` |
| `sondhi2025jirvis` | article | 2025 | 2025 | Sondhi | Sondhi | 1.0 | `10.26434/chemrxiv-2025-d0j2v` |

All rows: Crossref HTTP 200; title similarity ≥ 0.94; year exact match; first-author family name match (after brace/corporate normalization).

### Container-title spot checks (bib journal/booktitle vs Crossref `container-title`)

Not flagged as mismatches when words align after normalization. Notable bib↔CR containers:

- `wang2025nmrexp`: bib `Sci. Data` ↔ CR `Scientific Data`
- `zipoli2025uspto`: bib `Sci. Data` ↔ CR `Scientific Data`
- `yang2026nmrtrans`: bib `{Proc. 32nd {ACM} {SIGKDD} Conf. Knowledge Discovery and Data Mining}` ↔ CR `Proceedings of the 32nd ACM SIGKDD Conference on Knowledge Discovery a`
- `lowe2011opsin`: bib `J. Chem. Inf. Model.` ↔ CR `Journal of Chemical Information and Modeling`
- `krenn2020selfies`: bib `Mach. Learn.: Sci. Technol.` ↔ CR `Machine Learning: Science and Technology`
- `kim2023pubchem`: bib `Nucleic Acids Res.` ↔ CR `Nucleic Acids Research`
- `wilkinson2016fair`: bib `Sci. Data` ↔ CR `Scientific Data`
- `rosonovski2024europepmc`: bib `Nucleic Acids Res.` ↔ CR `Nucleic Acids Research`
- `blum2012atrftir`: bib `Drug Test. Anal.` ↔ CR `Drug Testing and Analysis`
- `krasnov2025bigsoldb`: bib `Sci. Data` ↔ CR `Scientific Data`
- `horai2010massbank`: bib `J. Mass Spectrom.` ↔ CR `Journal of Mass Spectrometry`
- `neumann2026massbank`: bib `Nucleic Acids Res.` ↔ CR `Nucleic Acids Research`
- `tremouilhac2017chemotion`: bib `J. Cheminform.` ↔ CR `Journal of Cheminformatics`
- `tremouilhac2020chemotionrepo`: bib `Chemistry--Methods` ↔ CR `Chemistry–Methods`
- `swain2016chemdataextractor`: bib `J. Chem. Inf. Model.` ↔ CR `Journal of Chemical Information and Modeling`
- `heller2013inchi`: bib `J. Cheminform.` ↔ CR `Journal of Cheminformatics`
- `kemp2022crossref`: bib `Inf. Serv. Use` ↔ CR `Information Services and Use`
- `hrynaszkiewicz2012open`: bib `BMC Res. Notes` ↔ CR `BMC Research Notes`
- `carroll2011openaccess`: bib `PLoS Biol.` ↔ CR `PLoS Biology`
- `krishnadas2026squirl`: bib `Sci. Data` ↔ CR `Scientific Data`
- `alberts2024multimodal`: bib `Adv. Neural Inf. Process. Syst.` ↔ CR `Advances in Neural Information Processing Systems 37`
- `elyashberg2009case`: bib `J. Cheminform.` ↔ CR `Journal of Cheminformatics`
- `pesek2021elucidation`: bib `J. Chem. Inf. Model.` ↔ CR `Journal of Chemical Information and Modeling`
- `alberts2024irstruct`: bib `Commun. Chem.` ↔ CR `Communications Chemistry`

## Table B — DOI in bib, Crossref 404 (DataCite OK)

| Key | Bib DOI | Crossref | DataCite title | DataCite year | Notes |
|-----|---------|----------|----------------|---------------|-------|
| `chemotion2024` | `10.22000/OGoEQGlsZGElrgst` | 404 | Chemotion Repository - Data collection: FT-IR spectroscopy data (Chemotion IR) | 2024 | DOI resolves via DataCite/Handle; not registered in Crossref. Bib title/year/first author align with DataCite. Not a DOI typo. |
| `nist_webbook` | `10.18434/T4D303` | 404 | NIST Chemistry WebBook, NIST Standard Reference Database 69 | 1997 | DOI resolves via DataCite/Handle; not in Crossref. Bib uses corporate author + access year 2026; DataCite registration year is 1997. Title matches. Living-database citation convention — not a DOI typo. |

Handle API (`doi.org/api/handles/...`) also returned HTTP 200 for both DOIs.

## Table C — Missing Crossref DOI / unresolved as journal works

| Key | Type | Year | URL | Classification | Crossref bibliographic query |
|-----|------|------|-----|----------------|------------------------------|
| `landrum_rdkit` | misc | 2026 | https://www.rdkit.org | Software (RDKit). No Crossref work DOI expected. | best weak/non-applicable hit doi=`10.59350/0srwr-zhx63` year=2009 sim=0.693 |
| `pmc_oa` | misc | 2026 | https://www.ncbi.nlm.nih.gov/pmc/tools/openftlist/ | Web/database (NCBI PMC OA Subset). Access-dated misc. | best weak/non-applicable hit doi=`10.59350/3gagv-h1y07` year=2011 sim=0.627 |
| `sdbs` | misc | 2026 | https://sdbs.db.aist.go.jp | Web/database (AIST SDBS). Access-dated misc. | best weak/non-applicable hit doi=`10.5571/syntheng.4.35` year=2011 sim=0.696 |
| `silverstein2014sioc` | book | 2014 | — | Book (Wiley, 8th ed., ISBN 978-0-470-61637-6). No Crossref book DOI found via ISBN filter. | REJECTED false-positive `10.1016/0026-265x(63)90068-7` (1963 *Microchemical Journal* item with same title string; not the 2014 Wiley book). ISBN query returned no book DOI. |

## Table D — Cite-key issues

| Issue | Keys |
|-------|------|
| Cited but missing | *(none)* |
| In bib but uncited | *(none)* |

## Inventory — every bib entry (parsed)

| Key | Type | Title (truncated) | Year | DOI | URL |
|-----|------|-----------------|------|-----|-----|
| `wang2025nmrexp` | article | {NMRexp}: a database of 3.3 million experimental {NMR} spectra | 2025 | `10.1038/s41597-025-06245-5` | — |
| `zipoli2025uspto` | article | {IR}-{NMR} multimodal computational spectra dataset for 177{K} pate... | 2025 | `10.1038/s41597-025-05729-8` | — |
| `yang2026nmrtrans` | article | {NMRTrans}: structure elucidation from experimental {NMR} spectra v... | 2026 | `10.1145/3770855.3818935` | https://doi.org/10.1145/3770855.3818935 |
| `lowe2011opsin` | article | Chemical name to structure: {OPSIN}, an open source solution | 2011 | `10.1021/ci100384d` | — |
| `landrum_rdkit` | misc | {RDKit}: Open-source cheminformatics | 2026 | `—` | https://www.rdkit.org |
| `krenn2020selfies` | article | Self-referencing embedded strings ({SELFIES}): a 100\% robust molec... | 2020 | `10.1088/2632-2153/aba947` | — |
| `pmc_oa` | misc | {NCBI PMC Open Access Subset} | 2026 | `—` | https://www.ncbi.nlm.nih.gov/pmc/tool... |
| `chemotion2024` | techreport | {Chemotion Repository} -- data collection: {FT-IR} spectroscopy dat... | 2024 | `10.22000/OGoEQGlsZGElrgst` | https://doi.org/10.22000/OGoEQGlsZGEl... |
| `nist_webbook` | misc | {NIST Chemistry WebBook}, {SRD} 69 | 2026 | `10.18434/T4D303` | https://webbook.nist.gov |
| `sdbs` | misc | {Spectral Database for Organic Compounds} ({SDBS}) | 2026 | `—` | https://sdbs.db.aist.go.jp |
| `kim2023pubchem` | article | {PubChem} 2023 update | 2023 | `10.1093/nar/gkac956` | — |
| `wilkinson2016fair` | article | The {FAIR} Guiding Principles for scientific data management and st... | 2016 | `10.1038/sdata.2016.18` | — |
| `rosonovski2024europepmc` | article | {Europe PMC} in 2023 | 2024 | `10.1093/nar/gkad1085` | — |
| `blum2012atrftir` | article | Historical perspective and modern applications of {Attenuated Total... | 2012 | `10.1002/dta.374` | — |
| `silverstein2014sioc` | book | Spectrometric Identification of Organic Compounds | 2014 | `—` | — |
| `krasnov2025bigsoldb` | article | {BigSolDB} 2.0, dataset of solubility values for organic compounds ... | 2025 | `10.1038/s41597-025-05559-8` | — |
| `horai2010massbank` | article | {MassBank}: a public repository for sharing mass spectral data for ... | 2010 | `10.1002/jms.1777` | — |
| `neumann2026massbank` | article | {MassBank}: an open and {FAIR} mass spectral data resource | 2026 | `10.1093/nar/gkaf1193` | — |
| `tremouilhac2017chemotion` | article | {Chemotion ELN}: an {Open Source} electronic lab notebook for chemi... | 2017 | `10.1186/s13321-017-0240-0` | — |
| `tremouilhac2020chemotionrepo` | article | {Chemotion Repository}, a curated repository for reaction informati... | 2021 | `10.1002/cmtd.202000034` | — |
| `swain2016chemdataextractor` | article | {ChemDataExtractor}: a toolkit for automated extraction of chemical... | 2016 | `10.1021/acs.jcim.6b00207` | — |
| `heller2013inchi` | article | {InChI} -- the worldwide chemical structure identifier standard | 2013 | `10.1186/1758-2946-5-7` | — |
| `kemp2022crossref` | article | The {Research Nexus} vision for a more connected scholarly community | 2022 | `10.3233/ISU-220170` | — |
| `hrynaszkiewicz2012open` | article | Open by default: a proposed copyright license and waiver agreement ... | 2012 | `10.1186/1756-0500-5-494` | — |
| `carroll2011openaccess` | article | Why full open access matters | 2011 | `10.1371/journal.pbio.1001210` | — |
| `krishnadas2026squirl` | article | Spectral Quantum Chemistry and Infrared Resonance Library for Data-... | 2026 | `10.1038/s41597-026-07240-0` | — |
| `alberts2024multimodal` | article | Unraveling molecular structure: a multimodal spectroscopic dataset ... | 2024 | `10.52202/079017-3996` | — |
| `elyashberg2009case` | article | Computer-assisted methods for molecular structure elucidation: real... | 2009 | `10.1186/1758-2946-1-3` | — |
| `pesek2021elucidation` | article | Database independent automated structure elucidation of organic mol... | 2021 | `10.1021/acs.jcim.0c01332` | — |
| `alberts2024irstruct` | article | Leveraging infrared spectroscopy for automated structure elucidation | 2024 | `10.1038/s42004-024-01341-w` | — |
| `chacko2024spectro` | article | Spectro: A multi-modal approach for molecule elucidation using {IR}... | 2024 | `10.26434/chemrxiv-2024-37v2j` | https://doi.org/10.26434/chemrxiv-202... |
| `sondhi2025jirvis` | article | j-{IR}-vis: Vision model for {Infrared} spectroscopy embeddings | 2025 | `10.26434/chemrxiv-2025-d0j2v` | https://doi.org/10.26434/chemrxiv-202... |

## Actions taken

1. Parsed all 32 `references.bib` entries (key, type, title, year, doi, url).
2. Extracted all `\cite` / `\citep` keys from `scientific_data.tex` (48 uses, 32 unique).
3. Queried Crossref for every DOI; DataCite + Handle for Crossref 404s.
4. Bibliographic Crossref queries for no-DOI entries; **did not invent or write DOIs**.
5. **No unambiguous DOI typos** identified → `.bib` left unchanged (report-only).
6. This file added under `docs/`.

## Method notes

- Title comparison: brace/LaTeX stripped; Jaccard / SequenceMatcher on normalized tokens; mismatch threshold sim < 0.55 (none triggered for Crossref-200 works).
- Year: exact string compare to Crossref issued/published year.
- First author: bib `author` first token family (comma form) vs Crossref `author[0].family`.
- ChemRxiv / proceedings DOIs (`10.26434/...`, `10.52202/...`) are indexed in Crossref and matched OK.

