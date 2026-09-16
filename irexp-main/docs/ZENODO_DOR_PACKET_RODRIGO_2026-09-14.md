# IRexp Zenodo / DoR packet — for Rodrigo (one page)

**Date:** 2026-09-14 · **Owner:** Ilkham · **Action:** mint archival DOI (do not invent one in the manuscript first)

## 1. What to mint

A **Zenodo archival deposit** that mirrors the **commercial dataset of record** already published on Hugging Face:

- HF: https://huggingface.co/datasets/ilkhamfy/IRexp  
- **Revision (pin):** `8db58466e3ddfd2fbe09bd47fdd5eb4cfc3e1975`  
- **n = 88,545** CC-BY/CC0 commercial records with F2/F3 quality flags retained as fields (rows not dropped)  
- Companion configs on the same revision: `resolved_commercial` (28,899), `train_no_bench_commercial` (28,753 ⊆ resolved)

This is the Sci Data redistribution artifact. The full multi-licence corpus (n=121,233) stays the **methodology reference**, not the commercial DoR.

## 2. Files / snapshot to upload

Prefer uploading a **frozen snapshot of HF revision `8db58466…`** (JSONL / parquet configs as on Hub), plus:

- Dataset card / README from that revision (data-only; LEADERBOARD already purged)  
- Short LICENSE note: commercial pool only (CC-BY / CC0 as stamped per record)  
- Optional: count manifest from GitHub `IlkhamFY/IRexp` (`data/f1_commercial_build_stats.json`)

Do **not** invent filenames — if the Hub UI export is awkward, download the revision tree and zip it as `IRexp_commercial_8db58466.zip`.

## 3. License & title

- **License metadata:** Creative Commons as stamped per record in the commercial pool (**CC-BY-4.0** and **CC0**); deposit-level note: “mixed CC-BY/CC0 commercial pool; see per-record `license` / `license_pool` fields.”  
- **Suggested title:** `IRexp: experimental infrared band lists from open literature (commercial redistributable pool)`  
- **Version / related:** link HF revision above; GitHub manuscript https://github.com/IlkhamFY/IRexp ; harvest code https://github.com/IlkhamFY/spectro-agent @ `3af6f5af244cbec0c8f763973fedd5d93af3de20`

## 4. What NOT to include

- `LEADERBOARD.md` / benchmark coupling  
- NC / empty-unknown / ShareAlike-only pools as the DoR  
- Companion IRSpectra-Bench as part of this deposit  
- Fake or placeholder DOI strings in the paper before mint  

## 5. Metadata (creators)

1. Ilkham Yabbarov (McMaster; ORCID if available)  
2. Rudra Sondhi (McMaster)  
3. Rodrigo A. Vargas-Hernández (McMaster) — corresponding  

**Description (paste):** Redistributable experimental IR band lists (cm⁻¹ positions) mined from PMC Open Access and Chemotion. This archival deposit mirrors Hugging Face `ilkhamfy/IRexp` revision `8db58466…` (n=88,545 commercial CC-BY/CC0 records with F2/F3 flags). Full multi-licence construction corpus is described in the Scientific Data manuscript on GitHub `IlkhamFY/IRexp`.

**Ack:** NSERC CREATE AccelD Grant #596133-2025.

## 6. After mint — what Ilkham needs

Send the **DOI string** (e.g. `10.5281/zenodo.XXXX`). Ilkham will patch `scientific_data.tex` Data Availability (replace “archival DOI not yet minted; no DOI claimed”) and recompile Overleaf.

## 7. Rodrigo checklist

- [ ] Create Zenodo deposit (community optional)  
- [ ] Upload HF `8db58466…` commercial snapshot (+ README/LICENSE note)  
- [ ] Set creators + title as above  
- [ ] Set access open; license note CC-BY/CC0 commercial pool  
- [ ] Related identifiers: HF URL + GitHub IRexp + spectro-agent commit  
- [ ] Publish → copy DOI to Ilkham  
- [ ] Do **not** upload NC/empty pools or leaderboard files  

**Unblocks:** honest archival DOI claim in Sci Data DAS; Nature Portfolio archival expectation.
