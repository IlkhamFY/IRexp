# Referee response checklist — IRexp Sci Data (2026-09-10)

Internal tracking for pre-submit editorial / M6 cleanups. Postcard root stays clean; this file lives under `docs/`.

## Done in release v0.15 (prose / structure; numbers unchanged)

| Item | Status | Notes |
|---|---|---|
| Strip internal / project voice | **Done** | Removed PI / git-snapshot / remirror / Scrapling-fence / do-not-reuse `.zenodo.json` / casual Zenodo–Sci Data pool phrasing; Scrapling reduced to one sober non-release adapter sentence. |
| NMRexp disclaimer once | **Done** | Single automated-not-expert-audited statement retained in Technical Validation; abstract shortened; figure-caption and scattered Methods/TV repeats cut; Limitations tightened. |
| `\section*{Funding}` separate | **Done** | NSERC #596133-2025 / AccelD / Acceleration Consortium under Funding; Acknowledgements = McMaster thanks only. |
| End-matter order | **Done** | Author contributions → Competing interests → Funding → Acknowledgements → `\bibliography` last. |
| Band window 400–4000 cm⁻¹ | **Done** | Prose updated from 350 to 400 consistently (headline band/count totals unchanged). |
| “Chemist-proxy” display language | **Done** | Reader-facing labels → automated consistency audit; script name `audit_chemist_proxy.py` kept in Code Availability. |
| Inline script paths → Code Availability | **Done** | Methods cite modules lightly; compact inventory list in Code Availability. |
| Fig 1 caption NMRexp wording | **Done** | Rephrased (NMR peak-list corpus excluded from IR bar comparison). |
| Related-work cites | **Done** | SQuIRL Krishnadas *Sci. Data* 2026 (`10.1038/s41597-026-07240-0`); Alberts/IBM multimodal NeurIPS 2024 (`10.52202/079017-3996`). |
| Headline counts frozen | **Done** | 121,233 / 43,060 / 88,545 / 33,201 etc. untouched pending rebuild. |
| Figure binaries | **Untouched** | No PDF/PNG regeneration in v0.15. |

## Done in release v0.16 (Data Availability / Access; HF commercial DoR)

| Item | Status | Notes |
|---|---|---|
| Cite HF revision after F1 commercial publish | **Superseded (v0.24)** | Pin Hub revision `8db58466e3ddfd2fbe09bd47fdd5eb4cfc3e1975` in Access + Data Availability (was `2fb44992…`). |
| Sci Data dataset of record = commercial 88,545 | **Done (v0.24 counts)** | Commercial CC-BY/CC0 DoR (n=88,545) with F2/F3 flags `ir_shared_in_paper`, `ir_table_flatten_suspect` (flag-only). Companion Hub configs: `resolved_commercial` 28,899; `train_no_bench_commercial` **28,753** (⊆ resolved; 29,111 was wrong). |
| F1 thousands-separator note | **Done** | Note spectro-agent F1 fix + band reparse; commercial pool size unchanged vs pre-F1 stamp. |
| Full multi-licence vs commercial DoR | **Done** | Keep paper-wide 121,233 methodology headlines; state clearly that Sci Data / commercial redistribution uses the 88,545 commercial deposit while full multi-licence corpus remains construction reference. |
| Zenodo DOI | **Minted later (data-only)** | v0.16 left the archival DOI unminted. Data-only version DOI is now https://doi.org/10.5281/zenodo.22822285 (commercial CC-BY/CC0 pool). No software DOI is claimed. |
| Headline counts 121,233 | **Untouched** | No paper-wide rebuild of full-corpus headlines in v0.16. |
| Figure binaries | **Untouched** | No PDF/PNG regeneration in v0.16. |

## Done in release v0.23 (manuscript + figures; Hub-only items untouched)

| Item | Status | Notes |
|---|---|---|
| Fig 2 IR window 400–4000 | **Done** | Pipeline graphic + caption; gates labeled post-hoc / optional. |
| Fig 2 no Zenodo cylinder | **Done** | Step 5 = Hugging Face JSONL pools. |
| Fig 3e C–F leftover | **Done** | Caption sentence deleted. |
| Fig 3f chemist-proxy / MAE | **Done** | Consistency-audit label; MAE removed from transcription panel. |
| Background open with IRexp | **Done** | Peer situating after; “does not contain” paragraph removed. |
| End-matter order | **Done** | Usage Notes → Code Availability → Data Availability. |
| F2/F3 fields + rates | **Done** | Data Records table + TV; Hub stats 18651 / 3154 / 21075. |
| F1 defined once | **Done** | PMC6268696 thousands-separator example in Methods. |
| spectro-agent F1 commit | **Done** | `35808ea` / snapshot `3af6f5a` (2026-09-11). |

## Done in release v0.24 (DAS pin after Hub B1+B3)

| Item | Status | Notes |
|---|---|---|
| Hub revision pin | **Done** | Access + Data Availability cite `8db58466e3ddfd2fbe09bd47fdd5eb4cfc3e1975`. |
| `train_no_bench_commercial` | **Done** | n=28,753 (⊆ `resolved_commercial` 28,899); 29,111 withdrawn. |
| LEADERBOARD / card | **Done (cite)** | Hub card is data-only; LEADERBOARD purged. Data-only archival DOI https://doi.org/10.5281/zenodo.22822285. |

## Open / pending (not in v0.16)


| Item | Status | Notes |
|---|---|---|
| **F1 code** | **Done** (spectro-agent + Hub commercial DoR) | Thousands-separator fix applied; bands reparsed; commercial Hub revision cited in v0.16. |
| **Data rebuild (full multi-licence headlines)** | **Pending** | Commercial DoR published on Hub; do **not** change paper-wide 121,233 headlines until a consistent full vs commercial rebuild lands. |
| Band-window QC gate vs prose | **Aligned (v0.37)** | Prose restored to **350–4000** to match locked Fig.~2 H (Cleaning rules) and frozen QC `out_of_range_outside_350_4000=0`. Do not redesign Fig.~2. |
| Zenodo data-only DOI mint | **Done** | Commercial-pool primary deposit: https://doi.org/10.5281/zenodo.22822285. See `ZENODO_DATA_ONLY_CHECKLIST.md`. |
| ORCID confirmation (authors) | **Done** | Ilkham Yabbarov https://orcid.org/0009-0004-9393-9822; Rudra Sondhi https://orcid.org/0009-0003-3034-7347; Rodrigo A. Vargas-Hernández https://orcid.org/0000-0002-5559-6521. In `scientific_data.tex`. |
| Expert human structure spot-check ($n\geq100$) | **Deferred** | Optional TV strengthen vs NMRexp. |
| Human extraction-recall mark-up | **Deferred** | Optional. |
| Software / release tag + software DOI | **Open** | Pin spectro-agent snapshot when archival deposit minted. |

## Out of scope for this Descriptor (companion paper)

- IRSpectra-Bench protocol, model tables, stage decomposition — cite companion research manuscript only.

## Contacts

- Manuscript / manifests: https://github.com/IlkhamFY/IRexp
- Code: https://github.com/IlkhamFY/spectro-agent
- Dataset (commercial DoR): https://huggingface.co/datasets/ilkhamfy/IRexp (rev `8db58466e3ddfd2fbe09bd47fdd5eb4cfc3e1975`)
