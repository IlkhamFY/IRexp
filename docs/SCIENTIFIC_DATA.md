# IRexp: A database of experimental infrared band lists from open literature

**Ilkham Yabbarov**^1,†^ — https://orcid.org/0009-0004-9393-9822
**Rudra Sondhi**^1^ — https://orcid.org/0009-0003-3034-7347
**Rodrigo A. Vargas-Hernández**^1,2,3,†^ — https://orcid.org/0000-0002-5559-6521

^1^ Department of Chemistry and Chemical Biology, McMaster University, Hamilton, Ontario L8S 4L8, Canada.  
^2^ Brockhouse Institute for Materials Research, McMaster University, Hamilton, Ontario L8S 4L8, Canada.  
^3^ School of Computational Science and Engineering, McMaster University, Hamilton, Ontario L8S 4L8, Canada.

† Corresponding authors. E-mail: yabbaroi@mcmaster.ca, vargashr@mcmaster.ca  
(No equal-contribution footnote — distinct roles; both corresponding.)

<!-- ORCID — confirmed; same URLs as scientific_data.tex \orcid.
       Ilkham Yabbarov               https://orcid.org/0009-0004-9393-9822
       Rudra Sondhi                  https://orcid.org/0009-0003-3034-7347
       Rodrigo A. Vargas-Hernández   https://orcid.org/0000-0002-5559-6521
-->

## Abstract

IRexp is a collection of experimental infrared band lists (cm⁻¹ peak positions) mined from open chemistry literature, optionally with author-reported ¹H/¹³C NMR strings and resolved structures. The multi-licence research corpus holds 121,233 records (119,345 PMC Open Access Subset; 1,888 Chemotion/RADAR4Chem), including 57,646 structure-linked entries and 39,118 IR + ¹H + ¹³C + structure quadruples. IRexp stores numeric band lists, not absorbance traces. Each record carries a source identifier and a stamped source licence. Public redistribution is limited to stamped-licence pools. The commercial dataset of record is the CC-BY/CC0 pool of 88,545 records, packaged under CC-BY-4.0. Intended reuse is multimodal training, retrieval, and tool input. Technical validation covers automated transcription, harvest-path recall proxies, stratified automated consistency audits, full-corpus quarantine, and a stratified expert human band-list audit of 161 records on the commercial dataset of record. Complementary elucidation benchmarks are described in a companion research manuscript and are not analysed here.

<!-- Abstract word count: 143 (whitespace tokens after expanding math). Cap ≤170. Filenames are in Data Records, not here. -->

Dataset: Hugging Face `ilkhamfy/IRexp`. Paper/manifests: `IlkhamFY/IRexp`. Code: `IlkhamFY/spectro-agent`. Archival DOI: https://doi.org/10.5281/zenodo.22822285. File names and packaging for ShareAlike, NC*, and ND are in Data Records.

## Background & Summary

Infrared (IR) spectroscopy is routine in organic characterisation, yet **open, redistributable** collections of *experimental* IR data remain sparse relative to modern machine-learning needs. Digitised absorbance libraries such as the NIST Chemistry WebBook[@nist_webbook] and AIST SDBS[@sdbs] are valuable but either modest in size or **view-only** (no bulk redistribution). Computational infrared sets in *Scientific Data* supply simulated spectra, including an IR–NMR multimodal collection[@zipoli2025uspto] and an infrared resonance library[@krishnadas2026squirl]. A computational multimodal spectroscopic dataset that includes infrared was released in the NeurIPS Datasets and Benchmarks track[@alberts2024multimodal]. Large literature mines for **NMR** peak lists (notably NMRexp[@wang2025nmrexp]) demonstrate that peer-reviewed experimental spectral *lists* with DOI traceability are in scope for this journal. NMRTrans reports experimental NMR spectra and the NMRSpec corpus[@yang2026nmrtrans].

**Relation to NMRexp and other peers.** NMRexp is the natural comparator: ~3.3 million experimental NMR records mined from supporting-information PDFs, with expert-scale manual checks and replicate consistency metrics. IRexp is *not* an NMR database, does not claim size superiority, and is orders of magnitude smaller. Its contribution is complementary: redistributable **IR band lists** (cm⁻¹ positions only) from PMC Open Access full text plus a Chemotion ELN deposit, with per-record licence pools suitable for commercial vs non-commercial reuse. Absorbance-curve libraries (NIST, SDBS) remain the right choice when full digitised spectra are required; computational IR–NMR sets remain the right choice when simulated multimodal coverage is required.

Spectroscopic workflows that consume structured experimental peak lists need redistributable numeric lists with source-identifier attribution and explicit licence pools (commercial vs non-commercial vs ShareAlike). IRexp is built as that substrate.

IRexp fills a specific wedge. Experimental sections of chemistry papers conventionally report per-compound **IR band lists** (wavenumbers in cm⁻¹) together with ¹H/¹³C NMR shift lists. That textual convention is the object language models and many elucidation pipelines consume, and it is a **different object** from a digitised spectrum. IRexp therefore:

1. Harvests open-access full text from the **PMC Open Access Subset** bulk S3 mirror and peak lists from the **Chemotion** FT-IR deposit.
2. Extracts deterministic numeric IR band lists (and co-reported NMR strings where present).
3. Resolves compound names to canonical structures with OPSIN[@lowe2011opsin], RDKit[@landrum_rdkit], and SELFIES[@krenn2020selfies] where possible.
4. Releases **extracted numbers only** — no PDFs, figures, or article full text — with source accessions for attribution.

Among openly redistributable *text-derived IR band lists*, IRexp's public release is the stamped-licence pools in Data Records. SDBS is a view-only archive of digitised absorbance spectra (~54,000 FT-IR entries). Those pools are redistributable text-mined band lists. The two resources are complementary object types. The scientific contribution of this Descriptor is the curated dataset, harvest provenance, licence segregation, and validation artefacts. The intended reuse is multimodal pretraining and supervised IR→structure modelling on structure-linked rows from a stamped-licence pool.

**Figures (see `FIGURE_DESIGN_BRIEF.md`).**

| Figure | File | Section |
|--------|------|---------|
| Positioning vs peers | `figures/fig_irexp_positioning.pdf` | Background |
| Construction pipeline | `figures/fig_irexp_pipeline.pdf` | Methods |
| Distribution + validation | `figures/fig_irexp_distribution.pdf` | Data Records / TV |

Regenerate: `bash scripts/build_all_scidata_figures.sh` (or individual `scripts/make_fig_irexp_*.py`). Manuscript tables are ≤3 (schema; files+licence pools; chemist-proxy).

**What this Data Descriptor does not contain.** No hypothesis tests, no large-language-model accuracy tables, and no stage-decomposition of elucidation performance. Those belong in the complementary research paper.

## Methods

### Source corpora

**PMC Open Access Subset.** Primary harvest uses the NCBI PMC OA bulk distribution on Amazon S3 (`s3://pmc-oa-opendata`, HTTPS endpoint `https://pmc-oa-opendata.s3.amazonaws.com`)[@pmc_oa]. **Harvest window (recoverable from git snapshots):** the bulk S3 IR crawl and `seen_papers` / `ir_harvest_snapshot` artefacts were produced on **2026-06-07 (UTC)** (`scripts/s3_ir_harvest.py`; incremental auto-snapshots that day through ~134,893 raw IR rows). Chemotion was ingested the same day. A harvest snapshot records **188,016** distinct PMC identifiers scanned (`data/irexp/seen_papers.txt.gz`). The released corpus retains records from **15,416** unique `PMC:*` accessions. Extraction operates on open-access **plain text** objects at flat S3 keys `PMC{id}.{v}/PMC{id}.{v}.txt` (not a directory walk of the commercial / non-commercial / other package trees). Europe PMC full-text XML is used for some validation re-fetches. Released `source_doi` values are `PMC:*` accessions or the Chemotion deposit DOI; no paywalled publisher DOI appears in the research corpus. `source_doi` is a source identifier, not always a DOI.

**Discovery vs `oa_comm` / `oa_noncomm` packages.** Identifier discovery used NCBI E-utilities `esearch` over PMC with an IR-characterisation query **and** `open access[filter]` (`scripts/s3_ir_harvest.py`), then fetched matching IDs from the flat S3 text layout. The harvest therefore did **not** pre-filter by walking the PMC OA Subset’s `oa_comm` vs `oa_noncomm` vs other package directories. PMC OA is still **not** a single licence[@pmc_oa]. Licence truth for redistribution is applied **post-hoc**: every unique PMCID in IRexp (15,416) was joined to Europe PMC `license` metadata (`scripts/join_pmc_licences.py`); each record carries `license` / `license_pool`. Commercial-use (CC-BY/CC0) rows form the primary archival pool; NC* are held aside; remaining empty/unknown rows are **not redistributed** — aligning redistributable intent with the OA commercial/non-commercial distinction via article-level licences rather than S3 package paths (`data/NOTICE`; `docs/LICENCE_REMEDIATION.md`).

**Reproducibility of discovery.** Re-running live `esearch` will drift as PMC grows. The frozen discovery set for this release is `data/irexp/seen_papers.txt.gz` (188,016 PMC identifiers); the curated release retains 15,416 of those accessions. Third parties should treat `seen_papers` + the released JSONL as the reproducible snapshot, not a fresh API crawl.

**Chemotion / RADAR4Chem.** **1,888** records come from the Chemotion Repository FT-IR collection deposited at RADAR4Chem (DOI `10.22000/OGoEQGlsZGElrgst`)[@chemotion2024], licensed **CC-BY-SA-4.0**. Ingest (`scripts/chemotion_to_irexp.py`, 2026-06-07): download the MD5-verified deposit; for each of **2,116** ATR-IR analyses, flatten the Quill-delta `content` field to plain text; parse an **author-curated** IR band list with the **same** regex extractor and quality gates as the PMC path; resolve the deposit’s canonical SMILES with RDKit → InChIKey + SELFIES; keep the richest band list per InChIKey; drop the **8** molecules already present in the PMC pool → **+1,888** new structure-resolved rows. All 1,888 Chemotion rows are structure-linked (`has_structure=true`; `inchikey` equals the record `id` on these rows). That equality is a convenience for this row type (Data Records). These are **not** algorithmic peak-picks from absorbance curves; they are author-entered experimental band lists from the ELN deposit, denser than typical paper prose (median **39** bands vs **9** for PMC). Rows carry `license=CC-BY-SA-4.0`, `source=Chemotion`, and `source_doi` equal to the deposit DOI.

**Excluded.** AIST SDBS (view-only; no bulk export)[@sdbs]; NIST WebBook join code exists in the repository but contributes **0** records to the released IRexp (`ir_source` is always `experimental` for released rows).

### Discovery and fetch (released corpus)

1. Discover IR-reporting OA PMCIDs via NCBI `esearch` (`open access[filter]` + characterisation-format IR query; year/month sliced).
2. Fetch OA full text from PMC-OA S3 plain-text objects (`PMC{id}.{v}.txt`).
3. Ingest Chemotion deposit author-curated band lists + structures (`scripts/chemotion_to_irexp.py`).
4. Persist harvest provenance in `seen_papers.txt.gz` and optional rawer rows in `ir_harvest_snapshot.jsonl.gz` (134,893 rows including intermediate prose fields used to diagnose materials-text false positives; the curated research corpus is the multi-licence total in Data Records, which is not a public redistribution file).

**Non-OA / Scrapling fence.** Development adapters for ChemRxiv, Beilstein, and generic publisher pages (`spectro_scraper/fetch.py` Scrapling / StealthyFetcher TLS-impersonation stack; `spectro_scraper/sources/*`) exist for exploration. They are **outside the construction path of the released dataset** and are an optional dependency. **No released `source_doi` is a paywalled publisher DOI.** Methods for IRexp as published here cite only **PMC-OA S3 + Chemotion**.

### Extraction (band lists, not spectra)

A deterministic regular-expression pipeline (`spectro_scraper/extract.py`) segments experimental text per compound and extracts:

- IR wavenumbers → `ir_bands_cm-1` (list of floats, cm⁻¹);
- ¹H and ¹³C payloads → `h_nmr` / `c_nmr` (author strings, when present).

Gates reject scan-range artefacts and common prose false positives (for example hydrogel / materials narrative mistaken for IR lists). **No curve digitisation** is performed: figures are not traced; JCAMP-DX is not stored.

### Structure resolution

Where an IUPAC or systematic name is available, names are converted with OPSIN (py2opsin)[@lowe2011opsin], canonicalised with RDKit[@landrum_rdkit], and encoded as InChIKey and SELFIES[@krenn2020selfies]. An optional PubChem[@kim2023pubchem] name fallback (`USE_PUBCHEM`) handles trivial names. Name→structure failures are expected for trade names, mixtures, and non-IUPAC prose; unresolved rows keep `has_structure=false`. Structure coverage of the full release is **47.5%** (57,646 / 121,233). The structure-complete split is shipped as `irexp_resolved`.

### Licence handling

| Pool | Records | Stamp |
|---|---:|---|
| commercial (CC-BY + CC0) | **88,545** | Public; CC-BY-4.0 packaging; per-record stamps |
| non_commercial (CC-BY-NC*) | 21,823 | Public; source-stamped NC*; redistribution under those terms |
| sharealike (Chemotion + rare PMC SA) | 1,897 | Public; CC-BY-SA-4.0 |
| other (CC-BY-ND) | 5 | Public; source-stamped CC-BY-ND; redistribution under those terms |
| empty_unknown | 8,963 | Research-corpus count; not redistributed |

`scripts/join_pmc_licences.py` stamps every row; `scripts/split_license_pools.py` reports provenance (`pool_of`) and materialises pool files under `data/irexp/licence_pools/`. Narrative and policy: `docs/scientific_data/LICENCE_REMEDIATION.md`.

### Quality tooling

IR-range and basic count gates may be applied as construction filters (at least three bands; wavenumbers in 350–4000 cm⁻¹). Formula–NMR physics checks in `spectro_scraper/quality.py` (¹H integral sum ≤ formula hydrogen count + 2; ¹³C peak count ≤ carbon count) are diagnostic, post-hoc quarantine flags. They were **not** hard filters at harvest. Flagged rows remain in the release files. Technical Validation reports a full-corpus post-hoc quarantine on `irexp_resolved` (`scripts/quarantine_structure_nmr.py` → `data/audit/structure_nmr_quarantine.jsonl.gz`). Transcription and recall-proxy scripts: `scripts/audit_extraction.py`, `scripts/audit_extraction_recall.py`.

## Data Records

### Object definition

Each IRexp record is a JSON object. Required chemistry fields for an IR entry:

| Field | Type | Description |
|---|---|---|
| `id` | string | Unique stable internal record identifier. Listing 1 uses the InChIKey as `id` for that resolved row (a convenience). InChIKey is stored in `inchikey` and is not unique (57,646 structure-linked records; 54,985 InChIKeys; about 2.7 thousand extra rows repeat a molecule). |
| `ir_bands_cm-1` | float list | Experimental IR peak positions (cm⁻¹) |
| `ir_source` | string | `experimental` for all released rows |
| `source_doi` | string | Source identifier: PMC accession (`PMC:…`) or Chemotion deposit DOI; not always a DOI |
| `pmcid` | string or null | PMC accession when PMC-sourced |
| `h_nmr` / `c_nmr` | string or null | Author-reported NMR shift *strings* (not parsed peak tables) |
| `smiles` / `selfies` / `inchikey` | string or null | Resolved structure encodings |
| `has_structure` | bool | Convenience flag (true when SMILES present) |
| `license` / `license_pool` | string | Per-article stamp (Europe PMC join or Chemotion) |
| `license_raw` / `license_source` | string | Upstream licence token + join provenance |
| `source` | string (Chemotion) | Present on Chemotion rows (`Chemotion`) |
| `ir_shared_in_paper` | bool | Commercial DoR only: identical IR list shared by ≥2 records in one paper; flag-only |
| `ir_table_flatten_suspect` | bool | Commercial DoR only: suspected table-flatten or column-misread list; flag-only |

**Not included:** absorbance traces, intensities, instrument metadata beyond what appears in source text, PDFs, figures, or full article bodies. Frozen counts: `docs/scientific_data/qc_structure_nmr.json`.

### Files and counts

Paths relative to the project repository / Hugging Face mirror.

| File | Records | Description |
|---|---:|---|
| `data/irexp/irexp.jsonl.gz` | 121,233 | Multi-licence research total; not redistributed |
| `data/irexp_resolved/irexp_resolved.jsonl.gz` | 57,646 | Structure-linked research split (multi-licence) |
| `data/irexp_release/train_no_bench.jsonl.gz` | 42,808 | Research split (multi-licence); benchmark InChIKeys held out |
| `data/irexp_release/train_no_bench_nmr.jsonl.gz` | 32,949 | Same research split with both ¹H and ¹³C |
| `data/irexp_release/pretrain_ir.jsonl.gz` | 119,345 | PMC-only IR pretrain pool (multi-licence) |
| `data/irexp/seen_papers.txt.gz` | 188,016 lines | PMC IDs scanned at harvest |
| `data/irexp/ir_harvest_snapshot.jsonl.gz` | 134,893 | Intermediate harvest snapshot |
| `data/irexp/licence_pools/irexp_commercial.jsonl.gz` | 88,545 | Public; CC-BY-4.0 packaging; CC-BY/CC0 stamps |
| `data/irexp/licence_pools/irexp_sharealike.jsonl.gz` | 1,897 | Public; CC-BY-SA-4.0 |
| `data/irexp/licence_pools/irexp_non_commercial.jsonl.gz` | 21,823 | Public; source-stamped NC*; redistribution under those terms |
| `data/irexp/licence_pools/irexp_other.jsonl.gz` | 5 | Public; source-stamped CC-BY-ND; redistribution under those terms |
| `data/irexp/licence_pools/irexp_empty_unknown.jsonl.gz` | 8,963 | Research-corpus count; not redistributed |

**Composition of `irexp.jsonl.gz`:**

| Slice | Count |
|---|---:|
| All IR band-list records | 121,233 |
| With ¹H and/or ¹³C NMR | 87,075 (72%) |
| With resolved structure | 57,646 (47.5%) |
| Structure + any NMR | 47,521 |
| Full IR + ¹H + ¹³C + structure | 39,118 |
| PMC OA provenance | 119,345 |
| Chemotion provenance | 1,888 |
| Unique PMC accessions | 15,416 |

**Licence-pool counts (Europe PMC join + Crossref recovery, 2026-08-27).** Lookup over **15,416** unique PMCIDs; stamped pool files under `data/irexp/licence_pools/` (see `docs/scientific_data/LICENCE_REMEDIATION.md`, `data/irexp/pmc_licence_summary.json`). Sum of pools = **121,233** (unchanged).

| Pool file | Count | Notes |
|---|---:|---|
| `irexp_commercial.jsonl.gz` | **88,545** | Public; CC-BY-4.0 packaging; per-record CC-BY/CC0 stamps; Zenodo primary |
| `irexp_sharealike.jsonl.gz` | **1,897** | Public; CC-BY-SA-4.0 (Chemotion 1,888 + rare PMC SA) |
| `irexp_non_commercial.jsonl.gz` | **21,823** | Public; source-stamped NC*; research redistribution under those terms |
| `irexp_other.jsonl.gz` | **5** | Public; source-stamped CC-BY-ND; research redistribution under those terms |
| `irexp_empty_unknown.jsonl.gz` | **8,963** | Research-corpus count; not redistributed |

The multi-licence research total is not a public redistribution file. Public redistribution is the stamped-licence pools above. Commercial reuse must use `license_pool == "commercial"`. Empty/unknown rows remain in the pool sum and are removed from the public Hugging Face redistribution. Chemotion rows were schema-backfilled with `inchikey` / `has_structure` (2026-08-27).

**Overview figure:** `docs/scientific_data/figures/fig_irexp_overview.pdf` (provenance / licence pools / composition cascade). See also positioning (`fig_irexp_positioning`), pipeline (`fig_irexp_pipeline`), and validation (`fig_irexp_validation`) figures — `FIGURE_DESIGN_BRIEF.md`.

Median bands: **9** (PMC), **39** (Chemotion). All **1,360,866** released IR band values fall inside 350–4000 cm⁻¹ (full-corpus range check; Technical Validation).

### Access

- **Hugging Face (public redistributable files only):** https://huggingface.co/datasets/ilkhamfy/IRexp — `irexp_commercial.jsonl.gz` (CC-BY-4.0 packaging), `irexp_sharealike.jsonl.gz` (CC-BY-SA-4.0), `irexp_non_commercial.jsonl.gz` (source-stamped NC*; research redistribution under those terms), `irexp_other.jsonl.gz` (source-stamped CC-BY-ND; research redistribution under those terms). The multi-licence total and empty/unknown rows are not redistributed. See `LICENCE_REMEDIATION.md`.
- **Manuscript + manifests:** https://github.com/IlkhamFY/IRexp
- **Harvest / pipeline code:** https://github.com/IlkhamFY/spectro-agent
- **Archival snapshot:** https://doi.org/10.5281/zenodo.22822285 (data-only; same commercial pool / Hub revision `8db58466e3ddfd2fbe09bd47fdd5eb4cfc3e1975`).

## Technical Validation

Machine-readable package: `docs/scientific_data/qc_structure_nmr.json` (and artefacts under `data/audit/`). **Validation summary figure:** `figures/fig_irexp_validation.pdf` (transcription, recall proxy, chemist-proxy, quarantine). Numbers below are descriptive fidelity / consistency checks (fixed seeds); Wilson 95% intervals reported for recall proxy and chemist-proxy.

### Transcription fidelity (PMC)

On a seed-fixed random sample of **60** PMC-sourced records (`scripts/audit_extraction.py --n 60 --seed 0`), each article was re-fetched from Europe PMC and every recorded wavenumber was checked against the source text (±1 cm⁻¹ integer match). Result: **560/560 bands** and **60/60 records** confirmed. Enlarged sample **n=200** (same script/seed family, `data/audit/extraction_audit_n200.json`): **2,250/2,261 bands (99.51%)** and **196/200 records (98.0%)** fully confirmed. The four incomplete records (PMCIDs 5713685, 4189708, 12202350, 6259152) missed 11 bands total on re-fetch match — consistent with plain-text / formatting drift, not wholesale hallucination. This bounds **automated** transcription error; it is not a human PDF mark-up of the kind reported for NMRexp.

### Extraction-recall proxy (PMC, harvest path)

A human mark-up of every IR string in every paper remains the gold standard. As an automatic **proxy** on the actual harvest path (`scripts/audit_extraction_recall.py --n 120 --seed 0`): re-fetch PMC-OA S3 plain text for **120** distinct source PMCIDs; re-run `extract_records`; compare band-sets to released rows (±1 cm⁻¹). Result (`data/audit/extraction_recall_proxy_n120.json`): **7,981/8,059** released bands confirmed (0.9903; Wilson 95% CI [0.9879, 0.9922]); **845/858** released IR lists recovered (list-level recall proxy **0.9848**; Wilson 95% CI [0.9743, 0.9911]); **115/120** papers recovered every released list. Of **871** re-extracted IR lists, **811** matched a released list (0.9311); **18/120** papers yielded *extra* re-extracted lists (parser over-fire vs curation). Prior n=40 archive: `data/audit/extraction_recall_proxy.json`. This is **not** a substitute for expert human recall.

### Stratified chemist-proxy audit (automated; not human)

`scripts/audit_chemist_proxy.py --n 280 --seed 0` — stratified across PMC structure-linked commercial / other licence / IR-only / Chemotion. Joint automated pass **271/280 (0.9679)**; stratified structure-physics pass **177/182 (0.9725)**; PMC transcription on the same sample **2,500/2,508 bands (0.9968)**. Artefacts: `data/audit/chemist_proxy_audit.json`. Explicitly **not** an NMRexp-style human molecular-skeleton audit.

### Structure–NMR consistency and quarantine (resolved)

**Sample (prior).** On **500** `irexp_resolved` records with ¹³C text (seed 0): **17/500 (3.4%)** listed more peaks than carbons. On **500** with ¹H text: integrals > formula H+2 in **17/497 (3.4%)**.

**Full resolved corpus.** `scripts/quarantine_structure_nmr.py` applied the same formula–NMR physics checks post hoc to all **57,646** structure-linked rows. They are diagnostic quarantine flags, not hard harvest filters. **1,882 (~3.3%)** fail at least one diagnostic check and are listed in `data/audit/structure_nmr_quarantine.jsonl.gz` (diagnostic only — release files unchanged). Among rows with the relevant modality: ¹³C peaks > carbons **1,194/34,231 (3.49%)**; ¹H integral > formula+2 **1,141/39,672 (2.88%)**; IR out-of-range **0**; unparseable SMILES **0**. Sample rates and full-corpus rates agree closely. Re-users should **drop** quarantined IDs by default before supervised training. These rates are integrity diagnostics, **not** an expert skeleton audit (NMRexp-scale n≈300 manual checks remain optional future work).

### IR physical window

Every band in the full 121,233-record release lies in **[350, 4000] cm⁻¹** (0 / 1,360,866 out of range). This is a necessary range gate only: IRexp does not store intensities, solvents, or ATR vs transmission metadata.

### QC status

| Check | Status |
|---|---|
| Per-PMCID licence join + Crossref empty recovery | **Done** — commercial 88,545 |
| Transcription fidelity n=60 and n=200 | **Done** (automated re-fetch) |
| Extraction-recall automatic proxy (n=120 papers) | **Done** (human recall still optional) |
| Stratified chemist-proxy audit (n=280) | **Done** (automated; not human expert) |
| Full-corpus structure–NMR quarantine | **Done** — 1,882 / 57,646 flagged |
| Stratified expert human band-list audit | **161 scored** on the commercial Hugging Face dataset of record |
| Expert human structure spot-check (n≥100) | Deferred (human) |
| NMRexp-style replicate MAE for IR lists | Not applicable / not claimed |

## Usage Notes

- **Band lists ≠ spectra.** Do not evaluate models trained on IRexp as if they had seen full absorbance curves.
- **Licence filter.** Public redistribution is the stamped-licence pools in Data Records. Commercial reuse uses `irexp_commercial.jsonl.gz` (CC-BY-4.0 packaging). ShareAlike reuse uses `irexp_sharealike.jsonl.gz` (CC-BY-SA-4.0); do not relicence those rows as CC-BY. NC* and ND files stay under their source stamps. The multi-licence research total and the empty/unknown rows are not redistributed. `source_doi` may hold a PMC accession (`PMC:…`) rather than a DOI.
- **Separate pools by density and licence.** PMC (sparse) vs Chemotion (denser ELN lists). Higher median band count ≠ more complete vibrational assignment.
- **Structure–NMR quarantine.** Before supervised training on `irexp_resolved`, **drop** IDs in `data/audit/structure_nmr_quarantine.jsonl.gz` by default (~3.3% of resolved rows) unless a noisier set is intentional.
- **Training without benchmark leakage.** If using complementary IRSpectra-Bench problems, withhold those InChIKeys. `train_no_bench.jsonl.gz` is the multi-licence research split (rebuild with `scripts/build_train_no_bench.py`). Commercial training uses the commercial companion named in Data Availability. Protocol and model results live only in the companion manuscript.
- **Structure coverage.** Supervised structure tasks need rows with SMILES; 52.5% of the research corpus lack SMILES. Use a structure-linked subset of a stamped-licence pool.
- **Attribution.** Cite this Data Descriptor and the archival version DOI https://doi.org/10.5281/zenodo.22822285, and attribute originating articles through each record’s `source_doi` (PMC accession or DOI).

### Limitations

- **Object.** Band-list corpus — not an absorbance-spectrum library and not an NMR resource comparable to NMRexp in scale or annotation richness.
- **Technical Validation depth.** Automated transcription (n=200), harvest-path recall proxies (n=120 papers with Wilson intervals), and a stratified consistency audit (n=280) are machine checks. A stratified expert human band-list audit scored 161 records on the commercial Hugging Face dataset of record. No human molecular-skeleton audit has been completed for IRexp.
- **Metadata sparsity.** Intensities, solvents, and instrument modes are generally absent; the IR window check is necessary but narrow.
- **Structure coverage and name resolution.** Only 47.5% of records are structure-linked; OPSIN/PubChem failures leave many IR lists without SMILES.
- **Licence mix.** The research corpus is multi-licence. Public redistribution is the stamped-licence pools in Data Records. Empty/unknown rows are not redistributed.
- **Scope of this paper.** Elucidation benchmarks and model results are out of scope; cite the companion research manuscript for those claims.

## Data Availability

IRexp numeric extracts are available at:

- Hugging Face Datasets (bulk JSONL): https://huggingface.co/datasets/ilkhamfy/IRexp, revision `8db58466e3ddfd2fbe09bd47fdd5eb4cfc3e1975`  
- Manuscript + manifests: https://github.com/IlkhamFY/IRexp (no bulk JSONL under `data/`)  
- Harvest / pipeline code: https://github.com/IlkhamFY/spectro-agent  
- Archival deposit (Zenodo; same commercial pool / same Hub revision): https://doi.org/10.5281/zenodo.22822285 (`10.5281/zenodo.22822285`)

Licensing summary (honest):

- Commercial DoR (Hugging Face commercial configuration and the Zenodo primary file): CC-BY-4.0 packaging, with per-record source licences still stamped.
- ShareAlike file: CC-BY-SA-4.0. **Chemotion (1,888):** CC-BY-SA-4.0[@chemotion2024]. These rows are not in the commercial DoR.
- Non-commercial file (21,823): source-stamped NC*; packaging is research redistribution under those terms.
- ND file (`irexp_other.jsonl.gz`, 5): source-stamped CC-BY-ND; packaging is research redistribution under those terms.
- **PMC (119,345):** mixed Creative Commons — stamped per article (`LICENCE_REMEDIATION.md`). Empty/unknown rows (8,963) are not redistributed.
- Only extracted numeric fields and identifiers are redistributed; source full texts are not.

## Code Availability

Manuscript and manifests: https://github.com/IlkhamFY/IRexp. Harvesting, extraction, licence-pool splitting, and validation scripts: https://github.com/IlkhamFY/spectro-agent (MIT License). A release tag (`irexp-scidata` placeholder) will be pinned at Zenodo deposit; until then `main` @ `6c18914` (2026-08-31) is the public script snapshot.

## Author contributions

**I.Y.:** conceptualization, methodology, software, data curation, validation, writing (original draft).  
**R.S.:** validation (human band-list audit), writing (review and editing).  
**R.A.V.-H.:** conceptualization, supervision, writing (review and editing).

## Competing interests

The authors declare no competing interests.

## Acknowledgements

We acknowledge the support of the Natural Sciences and Engineering Research Council of Canada (NSERC), funding reference number 596133-2025 (CREATE for Accelerated Discovery, AccelD), delivered through the Acceleration Consortium. We thank the Department of Chemistry and Chemical Biology, McMaster University, for institutional support.

Sponsor logos are omitted from this Data Descriptor (Nature style); use the official Acceleration Consortium mark on posters/slides if required by AccelD.

## References

References are maintained in `docs/scientific_data/references.bib` (pandoc/CSL build) and overlap the project bibliography where shared.
