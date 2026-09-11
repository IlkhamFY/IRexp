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

## Open / pending (not in v0.15)

| Item | Status | Notes |
|---|---|---|
| **F1 code** | **Done** (prior / spectro-agent) | Code-side F1 work complete; not re-opened here. |
| **Data rebuild** | **Pending** | Re-extracted numbers / refreshed manifests not landed; do **not** change headline counts until rebuild. |
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
- Dataset: https://huggingface.co/datasets/ilkhamfy/IRexp
