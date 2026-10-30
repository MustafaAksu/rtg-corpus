# Triadic v1.6.1 — Atlas advisory, pass 1 (migration to Methodology v1.4)

**Date:** 30 October 2026. **By:** Claude, Atlas owner. The Atlas owner advises and does not decide. The Triadic co-owners (Claude and ChatGPT) disposition each item, separately and then jointly; the PI adopts.
**Status:** NONCANONICAL advisory, pass 1. A blind pass 2 by ChatGPT follows, then a reconciliation. This advisory changes no Triadic text, grade, RID or pipe state.
**Object:** `dsn/RTG_TRIADIC_BIRTH_LIFT_DSN.md` at `triad-v1.6.1` (tag object `13ff1e9b…`, commit `d7d661c0b89c6f3d9ceea2e205bf75fccfcfbf8d`), SHA-256 `95340abe57e999ed48681502152113d8fdb3102f74f45a25aa66c2d0092d451f`, 1,202 lines. `main` holds the same bytes. Line numbers (L…) refer to that file.
**Rules applied:** DSN Methodology v1.4 (`methodology-v1.4`) and `CONVENTIONS.md`.
**Governing editions read:**

| Document | Edition |
|---|---|
| Programme | `programme-v1.3` |
| OFN | `ofn-v0.12`, tagged today; `ofn-v0.11` is the edition the Atlas carries |
| Dyadic | `dyad-v6.4.22` |
| Genesis | `gen-v2.9` |
| RRF | `rrf-v0.8.4` |
| OPEN-M | `uvm-v0.7.1` |
| TDR-G | `tdrg-v2.12.14` |

**Evidence:**
- `EV-SRC-READ` for statements at those tags.
- `EV-CODE` for the line-level inventory, `evidence/atlas/triad_v1_6_1/pass1_inventory.md`. A delegated read-only sweep built it, and the Atlas owner spot-checked it. Its counts are a manual classification, not a lint result.
- No Triadic computation is rerun; the Triadic evidence is not in the repository (TC-01, TC-02).

## 0. Summary

Triadic v1.6.1 is scientifically stable at its declared scopes. The orientation-normalization correction of v1.6 is self-consistent, and its downstream consumers have recorded it. The migration work is mostly form, currency and custody:

1. **Form.** The file still declares "Methodology v1.3, bounded migration" (L10). Its header, its §§1–9 and its footers carry release history:
   - five "History —" labels in the header;
   - about 77 narrative lines in the live text;
   - two footers.
   Its tags mix v1.2, v1.3 and v1.4 spellings.
2. **Currency.**
   - The consumer state in §1, §2 and §7.4 is stale: every CN-01–CN-05 receiver has recorded a disposition, and Programme v1.3 *was* the pass-two synchronization.
   - Companion pins name editions up to six releases old.
3. **Custody.** No Triadic release record, adoption record, script or output is in the repository. Two producer scripts with matching hashes were once uploaded and then removed as "unrelated".

**Proposed edition: v1.7**, in two stages as OFN v0.11 was built:
- stage 1 carries the content and currency changes (TB and TD items and the tag repairs);
- stage 2 is layout only (TA-01, TA-02, TA-04), checked by `tools/check_compaction.py` against the stage-1 hash.

The custody intake (TC) should come first, so that the release can cite placed evidence.

## 1. TA — form under Methodology v1.4

| # | Finding | Lines | Proposed disposition |
|---|---|---|---|
| **TA-01** | **Header.** 15 fields, 752 words. Five "History —" labels (L7, L12, L13, L14, L17). Draft-chain, review and build text sits in Date (L4), Status (L7), Supersedes (L8), Companions (L9) and the release-base, co-owner, adoption and preservation fields (L12–L17). Supersedes names a versioned filename and no tag (no `triad-v1.6` tag exists). The Scope field (L5) describes the revision task rather than the science. The Status summary (L11) is 5 sentences; v1.4 asks for 2–4. The repository is named `rtg-resonance-2025` (L949) | L3–17, L949 | Rewrite the header in v1.4 form, using OFN v0.11/v0.12 as the model: one line per field, current state only; Supersedes = `triad-v1.6.1` with its hash; Companion documents = the governing editions read; a one-sentence scientific Scope. Move the release/draft history into the v1.7 release record and Appendix A. Stage 2 |
| **TA-02** | **History in live text.** About 77 lines narrate editions, drafts, reviews or repins. Examples: "Source v1.5 status … now adopted" (L73, L80, L87); "unchanged from accepted r4.2" (L552, L589, L618); "No new numerical sweep is required for this r4 model-contract correction" (L50); "**History — v1.6 release**" (L945); the per-module disposition table (L753–772), which is a v1.6 disposition record. About 26 further lines use "former / prior / no longer / withdrawn" inside live claims (L36, L44, L46, L61, …). Uses of "historical" as a result's *scope label* (for example "historical executed mis-scaled model") are legitimate and are not counted | inventory §2 | State each claim's current scope without the narrative. Keep the "records of the executed (mis-scaled) model" scope labels, which are current scope. Move the narrative and the disposition table to Appendix A/B or the release record. Stage 2, with the movement map |
| **TA-03** | **Tags and qualifiers.** (a) Compound or undeclared tags: `[ALG+NUM diagnostic]` (L916), `[NUM historical]` (L1165), `[DEF/ALG]` (L575, L821, the latter quoting Genesis); the alias `[ALG/NUM synthesis]` (L25) is declared but unused. (b) 16 section headings carry slash or mixed grades (`[ALG / mixed]`, `[ALG/NUM diagnostic / mixed]` ×3, `[COR / mixed]`, `[NUM / PARTIAL]`, `[COR / ALG]` …). (c) Mixed qualifier style: 56 backtick qualifiers against 24 plain-bracket ones. (d) Dash-style qualifiers carrying release labels: `[COR v1.6.1 — D3]`, `[COR v1.6.1 r2 — D3-R1]`, `[v1.6.1 r2 — H-R1]` (7 live lines). (e) 21 `(rep: [UNREGISTERED-TRIADIC-*])` labels. The two live `[RESULT]`s (L497, L747) already carry a single `[from: ALG]` | inventory §3 | (a) Unpack every compound into the exact assertion and its corroboration (v1.4 §8.4); drop the unused alias. (b) Give headings no grade, or one grade, as OFN does. (c) One qualifier style, v1.4 §3.2. (d) Remove release labels from live qualifiers; the change goes to Appendix B. (e) The `(rep: …)` labels follow RRF syntax for an unregistered profile. Keep them, and ask RRF whether a registered Triadic planar profile is wanted (no obligation). Stage 1 for (a), (d), (e); stage 2 for (b), (c) |
| **TA-04** | **Appendices.** Appendix A is 3,165 words in 18 entries; ten entries (about 1,640 words) are draft-round records (v1.6 r1–r4.2, v1.6.1 r1–r2). Appendix B (1,126 words) does not use the v1.4 template (original · reason · replacement · recorded in), and its `[RETRACTED]` / `[FAIL]` bullets carry no RIDs | L955–1199 | Compress Appendix A to one entry per adopted edition; draft rounds go to the release records. Restate Appendix B in the v1.4 template without changing any record's content. A `history_appendix` profile for `check_compaction.py` (PR #113) would help, once merged. Stage 2 |
| **TA-05** | **RID count.** L980 and L986 state "all 49 RIDs"; the file declares 46 distinct `TRIAD-*` RIDs. The other three cannot be identified without the v1.5/v1.6 files (not in the repository). Also, "OPEN-B-E1" (L802) is RRF's "OPEN-B/E1" | L980, L986, L802 | Owner states the actual RID set, and whether three were retired or merged (Appendix B). Fix the RRF key spelling. Stage 1 |

## 2. TB — currency (pins and consumer state)

| # | Finding | Lines | Proposed disposition |
|---|---|---|---|
| **TB-01** | **Companion and import pins.** Methodology v1.3 → v1.4; Programme v1.2 → v1.3; OFN v0.9 → v0.12; Dyadic v6.4.13 (and v6.4.8.1) → v6.4.22; Genesis v2.8.7 (v2.8.4/v2.8.5 in notices and evidence) → v2.9; RRF v0.8.2 (v0.6 at L612) → v0.8.4; TDR-G v2.12.13 → v2.12.14. OPEN-M v0.7.1 is current, but CN-02/CN-04 still target "OPEN M v0.6". Every cited DYAD, GEN, RECOG and TDRG RID exists at its governing tag; the 14 Genesis imports marked "RID unavailable" are still unassigned at `gen-v2.9` | inventory §4–5 | Use the OFN v0.11 rule: repin only where the statement was re-read at the governing tag, and label the rest as claim-level historical pins. Add one "governing editions read" line. Stage 1 |
| **TB-02** | **Consumer state of CN-01–CN-05 is stale.** §7.4 still marks CN-01, CN-02 and CN-04 "Consumer status: OPEN", and §1 (L48) and §2 (L64–67) say "consumer reconciliation pending … Send CN-01–CN-05". At the governing tags, the receivers have recorded dispositions: <br>• **Genesis:** v2.8.5 onward, retained at v2.9 — CN-01, CN-02, CN-03, CN-05 dispositioned (GCL-05/06, OPEN 1T CLOSED, `gen-v2.9` L103, L1172–1175), CN-04 routed to OPEN-M. <br>• **OPEN-M v0.7.1:** imports CN-01–CN-05 in its §7. <br>• **RRF v0.8.4 §3.1:** records the CN-05 planar convention, convention-only. <br>• **OFN:** v0.9 recorded CN-01–CN-05; v0.11/v0.12 cite Triadic v1.6.1 at reference grade (RF-O08-02/-03/-08). <br>• **Programme v1.3** *is* the pass-two synchronization (`programme-v1.3` L7, L26, L522), so L67/L841 "Programme v1.2 … pass-two synchronization is still pending" is stale. <br>What does remain open is the *physical* content each notice names: the CN-01 transverse carrier, the CN-04 HYP-M-PREFRACTURE falsifier and child-functional selection | L48, L64–67, L826–884 | Replace §7.4 with a current-state receipt table, one row per CN: receiver, edition, disposition location, and the remaining physical OPEN. Keep the notice texts as history (Appendix or release records). Remove the "send" queue from §2. Stage 1 |
| **TB-03** | **Consumers pin Triadic v1.6, not v1.6.1.** Genesis v2.9 and RRF v0.8.4 cite Triadic v1.6; OPEN-M v0.7.1 cites v1.6. Genesis also imports TRIAD-ALG-T6T-JACOBI-MODE-SIGNS under `[CAND]`, below the owner's `[ALG]` (`gen-v2.9` L243). That is the consumer's grading of its own use, with a different heading claim | — | Receivers' business, not a Triadic edit. Mention it in the v1.7 notices; the Atlas carries the `[CAND]` import as a consumer-side D-GRADE item |

## 3. TC — evidence custody

| # | Finding | Proposed disposition |
|---|---|---|
| **TC-01** | **Release and adoption records are missing.** `records/RELEASE_RECORD_v1_6_1.md`, `records/OWNER_ADOPTION_v1_6_1.json`, the v1.6 `records/OWNER_ADOPTION.json`, `RELEASE_RECORD.md` and `METADATA_EDITS.json`, and the v1.5/v1.6 files are not in the repository on any ref. `records/triad/` did not exist before this advisory | The PI uploads them unchanged to `upload/triad-records` (from current `main`); the Atlas hash-checks them against the hashes the DSN prints. The v1.7 release record then cites them, as OFN v0.11 cited `upload/ofn-records/` |
| **TC-02** | **Evidence is missing.** `evidence/accepted_r4_2/`, the manifests (`EXECUTION_MANIFEST*.json`, `FILE_IDENTITIES.json`), `t6u_certificate.json`, `triad_t6_producers.zip`, the T-6u scripts (`triad_t6u_apex_source_v1_6.py`, point-use and scope checks), the T-6b/d/e/f/h/j producers and the release build scripts are not in the repository. **Exception:** `tetrahedral_six_step_cross_phase_t6c2_patched.py` and `triad_analytic_phase_steering_t6l_patched.py` were uploaded in commit `9df0319` (`upload/tdrg-records/`), match the hashes at L903 and L915 exactly, and were removed in `07df334` as "unrelated" before the TDR-G custody merge | Recover the two files from `9df0319` into `evidence/triad/` (hash-checked; no re-upload needed). Upload the rest with TC-01. Open a Triadic source recovery list on the Dyadic model |
| **TC-03** | **T-3a file.** `triad_t3a_arb_enclosure_v4g.cpp` arrived with the Dyadic C++ upload. It is **not a certificate as written**: its forcing `dz` is a placeholder 0 and Q_c advances by a dummy `+1`, yet it prints CERTIFIED (ChatGPT finding, PR #125 comment `6521277354`; confirmed by the Atlas). The Triadic text has no T-3 module and cites no Arb or interval certificate, so no Triadic claim depends on it | List it in the Triadic recovery list as "PI-supplied scaffold, not a certificate, cited by no claim". No DSN edit. Any future T-3a interval result needs a real enclosure and its own review |
| **TC-04** | **Session-only or placeholder evidence.** TRIAD-ART-T6M-BIRTH (L916), TRIAD-ART-T6J2-PROXY (L917), "proof-source reference required" placeholders (L899–902, L905), and `apex_ratio_setup.py` / `genesis_k4_route_census.py` (stated unavailable) | Keep the text's own availability notes; carry them into the recovery list. T-6j2 stays PARTIAL with its stated limits (TD-05) |

## 4. TD — scientific scope (owner obligations, not errors found)

| # | Item | Atlas reading | Proposed disposition |
|---|---|---|---|
| **TD-01** | **T-6r: corrected orientation model.** §6.18 gives the corrected rate ΔΩ = −√3 Σ rʲHⱼ, K = 1 tangent (K̇ = (1−K) f_c/Q_c) and the large-u torsion coefficient A_θ^corr = 3√3μ² + 6μν + 9√3ν². That coefficient is positive definite: its discriminant is 36 − 4·3√3·9√3 = −288 < 0, which agrees with "> 0 for K > 0" (atlas arithmetic). What is missing is the admissible K < 1 carrier, the finite-u/r dynamics, the event taxonomy and any basin test (L59, §2 T-6r) | consistent at its scope | Keep T-6r ACTIVE. In v1.7, state the remaining contract in current-state form, with no r4 narrative |
| **TD-02** | **T-6q: sign-sector table** across the separated root and independent-orientation models | ACTIVE | Unchanged; owners may list it as the next technical artifact |
| **TD-03** | **T-6s/t/u at consumer use.** The owner scopes (|1−g₂|, no gain only for 0 ≤ g₂ ≤ 2; independently signable mode labels, not a physical transverse carrier; the T-6u ratios √14/16 and 16/√7 > 6) are restated correctly by Genesis v2.9 (L243, L264) and OPEN-M v0.7.1 (§7). Genesis types its T-6t use `[CAND]` (TB-03) | consistent | No Triadic change. Note the receivers' readings in the TB-02 receipt table |
| **TD-04** | **96:1 correspondence.** Withdrawn as a same-system dominance theorem (L36); the identification stays OPEN (L48, §6.18); the recovered graph-force generator differs from the primitive map | consistent | Keep OPEN, stated once (§1), with §6.18 pointing to it |
| **TD-05** | **T-6j2 and T-6m PARTIAL.** T-6j2's script and log are unrecoverable, and its terminal event is unresolved. T-6m is the exact quarter-turn plus the producer-frame root (2√7−1)/6 under its ansatz; its wedge and "~15×" are withdrawn | consistent, custody-limited | Keep PARTIAL, with the limits stated in current form |
| **TD-06** | **Metric-unit convention** B_T = 2B_G (§6.18): recorded by RRF as convention-only; the same-vector transport Q_c^T = (κ²/4)(Q_s^T)³ stays an obligation, not applied | consistent | Keep as stated. TB-02 records RRF's receipt |

## 5. Proposed sequence

| Step | Who | Content |
|---|---|---|
| 0 | PI → Atlas | Custody intake (TC-01, TC-02): upload to `upload/triad-records` from current `main`; the Atlas hash-checks it and recovers the two `9df0319` scripts. Open the Triadic recovery list (TC-03, TC-04) |
| 1 | ChatGPT | Blind pass 2 against the same tag, without reading this file first |
| 2 | Atlas | Reconciliation of passes 1 and 2 into one numbered list |
| 3 | Triadic co-owners | Dispositions, separately then jointly |
| 4 | Co-owners → receiving review → Atlas row check → PI | **v1.7**: stage 1 (TB, TD, TA-03 (a)(d)(e), TA-05), stage 2 (TA-01, TA-02, TA-03 (b)(c), TA-04) with a movement map; release record; tag `triad-v1.7` |
| 5 | Co-owners | Notices to Genesis, OPEN-M, RRF, OFN and Programme (receipt table, any repins); the Atlas refresh follows |

## 6. Not claimed

- No Triadic statement is found wrong.
- The TD items record that the declared scopes are consistent at the governing tags. They do not re-derive the T-6 results.
- Counts and line lists come from the inventory (`EV-CODE`) and may differ by a few lines at classification boundaries.
- OFN v0.12 was tagged the day of this advisory and is cited for currency only. The Atlas carries OFN v0.11 until its next refresh.
