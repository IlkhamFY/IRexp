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
| Cite HF revision after F1 commercial publish | **Done** | Pin Hub revision `2fb44992d33b389e2ba30d6d03a6ac76a261855a` in Access + Data Availability. |
| Sci Data dataset of record = commercial 88,545 | **Done** | Clarify commercial CC-BY/CC0 DoR (n=88,545) with F2/F3 flags `ir_shared_in_paper`, `ir_table_flatten_suspect` (flag-only). Companion Hub configs: `resolved_commercial` 28,899; `train_no_bench_commercial` 29,111. |
| F1 thousands-separator note | **Done** | Note spectro-agent F1 fix + band reparse; commercial pool size unchanged vs pre-F1 stamp. |
| Full multi-licence vs commercial DoR | **Done** | Keep paper-wide 121,233 methodology headlines; state clearly that Sci Data / commercial redistribution uses the 88,545 commercial deposit while full multi-licence corpus remains construction reference. |
| Zenodo DOI | **Unchanged (honest)** | Still pending with PI — **no DOI invented or claimed**. |
| Headline counts 121,233 | **Untouched** | No paper-wide rebuild of full-corpus headlines in v0.16. |
| Figure binaries | **Untouched** | No PDF/PNG regeneration in v0.16. |

## Open / pending (not in v0.16)


| Item | Status | Notes |
|---|---|---|
| **F1 code** | **Done** (spectro-agent + Hub commercial DoR) | Thousands-separator fix applied; bands reparsed; commercial Hub revision cited in v0.16. |
| **Data rebuild (full multi-licence headlines)** | **Pending** | Commercial DoR published on Hub; do **not** change paper-wide 121,233 headlines until a consistent full vs commercial rebuild lands. |
| Band-window QC gate vs prose | **Pending rebuild sync** | Prose now states 400–4000; QC JSON still documents historical `[350,4000]` gate — align on rebuild. |
| Zenodo data-only DOI mint | **Open (human)** | Commercial-pool primary deposit; see `ZENODO_DATA_ONLY_CHECKLIST.md`. |
| ORCID confirmation (authors) | **Open (human)** | See `HUMAN_SUBMISSION_CHECKLIST.md`. |
| Expert human structure spot-check ($n\geq100$) | **Deferred** | Optional TV strengthen vs NMRexp. |
| Human extraction-recall mark-up | **Deferred** | Optional. |
| Software / release tag + software DOI | **Open** | Pin spectro-agent snapshot when archival deposit minted. |

## Out of scope for this Descriptor (companion paper)

- IRSpectra-Bench protocol, model tables, stage decomposition — cite companion research manuscript only.

## Contacts

- Manuscript / manifests: https://github.com/IlkhamFY/IRexp
- Code: https://github.com/IlkhamFY/spectro-agent
- Dataset (commercial DoR): https://huggingface.co/datasets/ilkhamfy/IRexp (rev `2fb44992d33b389e2ba30d6d03a6ac76a261855a`)
