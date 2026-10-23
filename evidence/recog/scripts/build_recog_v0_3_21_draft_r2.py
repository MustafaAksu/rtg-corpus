#!/usr/bin/env python3
"""build_recog_v0_3_21_draft.py -- deterministic build of RECOG v0.3.21 DRAFT r2 (G2 synchronization).

r2 = r1 plus the receiving-review corrections of 20 Oct 2026: R1 (N1: R9 rows), R2 (A1, N1: source-fidelity
record identity), R3 (H3: v0.3.19 attribution), R4 (H5: RID wording), R5 (new edit H4b: OFN v0.8 historical pin);
optional: I7 (RRF historical source-state label). Same frozen base; r1 builder retained unchanged.

Input : RTG_RELATIONAL_RECOGNITION_DSN_v0_3_20.md (FROZEN, sha256 fdb8c9a7...b8df); refuses any other bytes.
Output: RTG_RELATIONAL_RECOGNITION_DSN_v0_3_21_DRAFT_r2.md and recog_v0_3_21_edits_r2.json.
Every edit is an exact-once replacement (old -> new); a missing or repeated anchor aborts the build.
No scientific statement, grade or OPEN status is edited; see check_recog_v0_3_21_draft.py.
Usage: python build_recog_v0_3_21_draft.py BASE.md [OUT_DIR]
"""
import sys, os, json, hashlib

BASE_SHA = "fdb8c9a72cbea67bae339a890f440b7d67c608979f7886279e2cd00bdabfb8df"

E = []
def edit(eid, purpose, old, new, allowed_new_tags=(), allowed_new_rids=()):
    E.append({"id": eid, "purpose": purpose, "old": old, "new": new,
              "allowed_new_tags": list(allowed_new_tags), "allowed_new_rids": list(allowed_new_rids)})

# ---------------------------------------------------------------- header
edit("H1", "title",
 "# RTG_RELATIONAL_RECOGNITION_DSN_v0.3.20\n",
 "# RTG_RELATIONAL_RECOGNITION_DSN_v0.3.21 (DRAFT r2)\n")
edit("H2", "date",
 "**Date:** 30 September 2026 (v0.3.20)\n",
 "**Date:** 20 October 2026 (v0.3.21 DRAFT r2 — synchronization release, no new mathematics; not adopted)\n")
edit("H3", "supersedes",
 "**Supersedes:** `RTG_RELATIONAL_RECOGNITION_DSN_v0.3.19` (frozen, sha256 `2b006b9f…2b36`; orientation conjugacy here)",
 "**Supersedes (on adoption):** `RTG_RELATIONAL_RECOGNITION_DSN_v0.3.20` (frozen 19 Oct 2026, sha256 `fdb8c9a7…b8df`; external record `RECOG_v0_3_20_FREEZE_DECISION_PROVENANCE.md`) · v0.3.19 (frozen, sha256 `2b006b9f…2b36`; R6 identification and inheritance ledger, CELL-F4). Orientation conjugacy is the v0.3.20 addition (Appendix A)")
edit("H4", "companion pins",
 "**Companion documents:** `RTG_DYADIC_OSCILLATOR_DSN_v6.4.10` (adopted 24 Sep 2026; supersedes v6.4.9 for all imports below) · `RTG_GENESIS_GEOMETRY_DSN_v2.8.4` ·",
 "**Companion documents:** `RTG_DYADIC_OSCILLATOR_DSN_v6.4.10` (adopted 24 Sep 2026; source pin of all Dyadic imports below; claim-level synchronized v0.3.21 against v6.4.17 `e07cf2b9…4bfc` as reported current — Dyadic release verification of v6.4.17 pending — and v6.4.16 `33c14c5c…59e0` as last verified, §7.2) · `RTG_GENESIS_GEOMETRY_DSN_v2.8.4` (source pin, `c145f5d2…cebd` recorded v0.3.21; current v2.8.9 `d143673e…c6fc`, claim-level synchronized v0.3.21, §7.2) · `RTG_ONTOLOGICAL_FOUNDATIONS_v0.10` (`acb70a8c…5dfa`; claim-level synchronized v0.3.21, §7.2) · `RTG_RRF_REPRESENTATION_REGISTRY_v0.8.3` (`b393657e…a187`; convention/registry reference only, synchronized v0.3.21, §7.2) ·")
edit("H4b", "companion pins: OFN v0.8 marked historical (receiving review R5)",
 "`RTG_ONTOLOGICAL_FOUNDATIONS_v0.8` (sha256 `56bc991d…a514`; claim-level synchronized v0.3.18, §7.1)",
 "`RTG_ONTOLOGICAL_FOUNDATIONS_v0.8` (historical source pin of the v0.3.18 audit, sha256 `56bc991d…a514`; claim-level synchronized v0.3.18, §7.1; not a current companion — current OFN edition v0.10 above)")
edit("H5", "status summary v0.3.21 (new paragraph above the v0.3.20 summary)",
 "**Status summary (v0.3.20):**",
 "**Status summary (v0.3.21 DRAFT r2):** Synchronization release; no new mathematics; no existing scientific RID, result grade or OPEN status changed; three new artifact IDs registered (§8). Records the external freeze of v0.3.20 (G1) and the G2 claim-level audits of every load-bearing import: Dyadic v6.4.10 → v6.4.17 (18 rows; statements unchanged; NF6 evidence strengthened, DYAD-DEF-PRIMITIVE-MAP identifier, Dyadic OPEN 12 now PARTIAL), Genesis v2.8.4 → v2.8.9 (7 rows; two identifiers; J_Q branch-independence scope narrowed by the owner, already met through SG-R9), OFN v0.8 → v0.10 (§6.2a restructured into the radial row and P1/P2/P3, consistent with R5; §7.3 identical; OPEN-OFN-OPA sharpened, status unchanged) and RRF v0.6 → v0.8.3 (network profile, `T-net`, OPEN-B → E1 → E2 lock unchanged). New §7.2 (audit summary and receipts N10–N13, N13 conditional) and §7.3 (downstream dependents register with a notification rule). SG-R14 gains the quantitative raw-track offset by reference to Dyadic N11. Outbound notices: RRF repin and the W3 paraphrase (RF-1).\n\n**Status summary (v0.3.20):**")
edit("H6", "freeze status",
 "**Freeze status:** v0.3.20 freeze candidate, 30 Sep 2026;",
 "**Freeze status:** v0.3.21 DRAFT r2 (not adopted). v0.3.20 frozen 19 Oct 2026, sha256 `fdb8c9a72cbea67bae339a890f440b7d67c608979f7886279e2cd00bdabfb8df` (PI decision in the RECOG co-owner conversation; external record `RECOG_v0_3_20_FREEZE_DECISION_PROVENANCE.md`). *Earlier freeze history:* v0.3.20 freeze candidate, 30 Sep 2026;")

# ---------------------------------------------------------------- OPEN registry (no status lines touched)
edit("O1", "R1: OFN v0.10 OPA receipt (no import)",
 "  - v0.3.20: the RECOG-side sign-identifiability question is resolved negatively (RECOG-ALG-SHEAR-ORIENTATION-CONJUGACY): within the character family, the orientation sign is exactly the pole-labelling convention under $S$. Primitive physical orientation remains OPEN upstream (OPEN-OFN-OPA); R1 is not closed.\n",
 "  - v0.3.20: the RECOG-side sign-identifiability question is resolved negatively (RECOG-ALG-SHEAR-ORIENTATION-CONJUGACY): within the character family, the orientation sign is exactly the pole-labelling convention under $S$. Primitive physical orientation remains OPEN upstream (OPEN-OFN-OPA); R1 is not closed.\n"
 "  - v0.3.21 (receipt, no import): OFN v0.10 OPEN-OFN-OPA records that the conjugacy is family conjugacy, not a symmetry of fixed $T_1$; that RRF OPEN-A's nonlinear $S_h$ is a different candidate action; that the passive/distinct-role dichotomy is exhaustive only for the isolated-dyad question (G1-P1 composition stays open); and a class-C reconciliation input. OPA status unchanged; R1 status unchanged.\n")
edit("O2", "R3 dependency: Dyadic OPEN 12 status",
 "- Dyadic OPEN 12; SG-R2; SG-R5",
 "- Dyadic OPEN 12 (PARTIAL since Dyadic v6.4.11, by RECOG-THM-P2-HET and RECOG-THM-P2-C0-FIRST; owner residual items: global $W^s(P_2)$ geometry, later re-intersections of $W^u_+(P_2)$ with $C_0$, large-amplitude dynamics — RECOG R3 owns only the first); SG-R2; SG-R5")
edit("O3", "R5 export targets (OFN v0.10)",
 "Exports to: RTG_ONTOLOGICAL_FOUNDATIONS v0.8 §6.2a (Minimal Constraint List for $T$: radial-row and phase-shear rows), OPEN-P0 generator selection",
 "Exports to: RTG_ONTOLOGICAL_FOUNDATIONS v0.10 §6.2a (Minimal Constraint List for $T$: radial row and the phase-shear rows P1 composition, P2 weight magnitude, P3 orientation; v0.8 single phase-shear row superseded upstream), OPEN-P0 generator selection")

# ---------------------------------------------------------------- scope guard: quantitative note (reference import)
edit("S1", "SG-R14 quantitative raw-track offset (Dyadic N11, reference import)",
 "final observables are track-independent, finite-initial-state comparator data are not.",
 "final observables are track-independent, finite-initial-state comparator data are not.\n"
 "*Quantified (v0.3.21, reference import).* [import: RTG_DYADIC_OSCILLATOR_DSN_v6.4.15 §6.14 | DYAD-THM-OPEN3-ASYMPTOTIC-PHASE, T2 `[THM — conditional on T1]`; T1 conditional on RECOG-THM-R9-MEMORY] On the primitive asymptotic-phase track, $M_W-M=-\\Delta_0(z_0)$ with $|M_W-M|\\le K_0\\sqrt{q_0}$; $K_0=\\tfrac{1101}{1000}$ on $|z|\\le\\tfrac1{20}$ and $K_0=\\tfrac{533}{500}$ on $|z|\\le\\tfrac1{40}$, rows not mixed (DYAD-THM-OPEN3-PHASE-OFFSET-BOUNDS). $M_W$ is the primitive-phase memory constructed through Dyadic's transported asymptotic-phase observable; this is not a theorem about the comparator $C_W^{(h)}$, no R9 coefficient is transferred to that track, and no RECOG claim changes.",
 allowed_new_tags=["[THM — conditional on T1]"])

# ---------------------------------------------------------------- §7 import ledger
edit("I1", "§7 synchronization note",
 "## §7. Import Ledger {#sec-7-imports}\n\n",
 "## §7. Import Ledger {#sec-7-imports}\n\n"
 "*Synchronization note (v0.3.21).* Source pins below are retained for provenance (v0.3.18 practice). Each load-bearing row was compared claim by claim with the current owner edition (Dyadic v6.4.17, Genesis v2.8.9, OFN v0.10, RRF v0.8.3); dispositions are in §7.2. Where a row below adds a v0.3.21 remark, it records an identifier, a scope note or a mutual-citation guard only.\n\n")
edit("I2", "§6.1 block: new Dyadic identifier",
 "- [RID: (none — §6.1 block)] ::",
 "- [RID: (none — §6.1 block); map definition registered since Dyadic v6.4.11 as DYAD-DEF-PRIMITIVE-MAP (provisional custody; identifier only, content unchanged)] ::")
edit("I3", "bridge lemma: mutual-citation guard",
 "- [RID: DYAD-ALG-BRIDGE-LEMMA] (general form) :: $\\mu_p=p\\bar\\lambda\\nu_3^{(1,p)}$ for all $p\\ge5$ :: Dyadic §6.9; general proof supplied in §6.12 (ownership offered to Dyadic) :: §6.10 :: $K_p$ family",
 "- [RID: DYAD-ALG-BRIDGE-LEMMA] (general form) :: $\\mu_p=p\\bar\\lambda\\nu_3^{(1,p)}$ for all $p\\ge5$ :: Dyadic §6.9; general proof supplied in §6.12 (ownership offered to Dyadic) :: §6.10 :: $K_p$ family :: *mutual-citation guard (v0.3.21):* the statement is the Dyadic RID; the general-$p$ proof is RECOG §6.12 (RECOG-ALG-LEADING-RETURN-EQUIVARIANCE), which Dyadic v6.4.11 cross-references as provenance; neither citation adds evidence to the other")
edit("I4", "Genesis §6.1: new identifiers",
 "- [RID: (none — Genesis §6.1)] ::",
 "- [RID: (none — Genesis §6.1); since Genesis v2.8.9: GEN-DEF-PRIMITIVE-METRIC ($B$, $Q$) and GEN-THM-PRIMITIVE-METRIC-INVARIANCE ($A^\\top BA=B$); identifiers only, content identical (§7.2)] ::")
edit("I5", "J_Q: owner scope narrowed (Genesis v2.8.9)",
 "branch-dependent sign; load-bearing properties branch-independent",
 "branch-dependent sign; metric identities ($J_Q^\\top BJ_Q=B$, $J_Q^2=-I$) branch-independent under consistent orientation transport (owner scope narrowed in Genesis v2.8.9 §6.6 CONVENTION, which no longer asserts that no downstream result depends on the sign); RECOG's sign-carrying comparator statements carry their declared orientation (SG-R9), so no RECOG claim changes")
edit("I6", "OFN row: v0.10 synchronization",
 "(restructured from v0.7 \"rows 2–3\"; content equivalence checked v0.3.18)",
 "(restructured from v0.7 \"rows 2–3\"; content equivalence checked v0.3.18; v0.10, checked v0.3.21: radial row clarified, phase-shear row split into P1/P2/P3 citing RECOG §6.6a, §7.3 identical — §7.2)")
edit("I7", "RRF v0.6 row: v0.8.3 synchronization",
 "source/registry reference only; no scientific import (the v0.4 row above is retained for the R11 convention use)",
 "source/registry reference only; no scientific import (the v0.4 row above is retained for the R11 convention use); current v0.8.3 (`b393657e…a187`, checked v0.3.21): §2.5 profile, `T-net` row, OPEN-B → E1 → E2 lock and §7 unchanged; new §6.1–§6.4 recorded, not imported (§7.2); the \"noncanonical, PI adoption pending\" wording of the v0.4 and v0.6 rows is a historical source-state description")

# ---------------------------------------------------------------- new §7.2 / §7.3
NEW72 = r"""### §7.2 Owner Synchronization Audit (v0.3.21) {#sec-7-2-sync-0321}

Claim-level consumer audit of every load-bearing import, run on the exact owner files (G2). Classes: **U** unchanged; **S** strengthened upstream (RECOG's claim not thereby strengthened); **CS** changed scope; **CST** changed statement; **ID** identifier registration only; **N** new upstream, recorded and not imported. Records: `RECOG_G2_DYADIC_CLAIM_AUDIT_v0_1_2.md`, `RECOG_G2_DYADIC_SOURCE_FIDELITY_RUN_v0_1.md` (reviewed) with `_v0_1_1.md` (receiving disposition), `RECOG_G2_GENESIS_OFN_RRF_CLAIM_AUDIT_v0_1.md` (§8). Labels are nonexclusive; they are not a partition of rows.

| owner (pinned → compared) | rows | outcome | CST |
|---|---|---|---|
| Dyadic v6.4.10 → v6.4.17 | 18 | all statements, hypotheses, domains, rows, charts, constants and grades unchanged; NF6 evidence strengthened (exact $h,J$ equality with the P2B v2 certificate, v6.4.16); DYAD-DEF-PRIMITIVE-MAP identifier; Dyadic OPEN 12 OPEN → PARTIAL (by RECOG's P₂ theorems) | 0 |
| Genesis v2.8.4 → v2.8.9 | 7 | unchanged except two identifiers (GEN-DEF-PRIMITIVE-METRIC, GEN-THM-PRIMITIVE-METRIC-INVARIANCE) and the narrowed J_Q branch-independence scope (§7 row) | 0 |
| OFN v0.8 → v0.10 | 6 | §7.3 identical; §6.2a radial row clarified; phase-shear row restructured into P1/P2/P3 consistent with R5 (RECOG notices of v0.3.17–v0.3.20 fulfilled); OPEN-OFN-OPA sharpened, status unchanged | 0 |
| RRF v0.6 → v0.8.3 | 8 | network profile, `T-net`, dependency lock and not-registered list unchanged; `T-h` constraint cell clarified; common-realisation convention now a working convention | 0 |

Scope notes: the Genesis whole-section comparison also shows changes in the birth-symmetry and saturation-ceiling paragraphs of §6.6, which RECOG does not import. RRF v0.4 (convention-only row) was not byte-audited; its conventions are present in v0.6 and were audited v0.6 → v0.8.3. Genesis v2.8.4's identity (`c145f5d2…cebd`) is PI-reported; no earlier pin existed.

**Receipts of Dyadic notices** (three separate states: received; source verification; RECOG use).

| notice | received | source verification | RECOG use |
|---|---|---|---|
| N10 (v6.4.14) | DYAD-ALG-OPEN3-LEADING `[ALG]`, DYAD-THM-OPEN3-SPIRAL-REM `[THM]` | carried unchanged in verified v6.4.16 | none; per-block chart statements; no RECOG claim made from them |
| N11 (v6.4.15) | DYAD-ALG-OPEN3-PHASE-OFFSET, DYAD-THM-OPEN3-PHASE-OFFSET-BOUNDS, DYAD-THM-OPEN3-ASYMPTOTIC-PHASE (T1, T2, memory law; conditional on RECOG-THM-R9-MEMORY) | carried unchanged in verified v6.4.16 | reference import for the SG-R14 quantitative note only (rows not mixed; no $C_W^{(h)}$ statement); RECOG claims unchanged |
| N12 (v6.4.16) | lifecycle (OPEN 3 closed in its defined scope; OPEN 21 opened) | verified adopted edition | none |
| N13 (v6.4.17) | DYAD-THM-OPEN21-PRIMITIVE-PHASE-REMAINDER, conditional on RECOG-THM-R9-MEMORY, as reported (`e07cf2b9…4bfc`) | pending: Dyadic release verification of v6.4.17 not available to this review | none decided; conditional receipt only; recorded as a downstream dependent (§7.3) |

**Outbound notices (G3).** To RRF: repin the RECOG v0.3.14 citations (§0.2, §4.1, §4.1a, §4.2, §4.3) to the frozen v0.3.20 or to this release (content unchanged); RF-1 — RRF v0.8.3 §6.3 restates W3 as comparison or transport between pre- and post-birth cohomology spaces, whereas §6.16g W3 requires $a^-$, $a^+$ in the same space; RRF is asked to quote W3 verbatim or to label its version an extension carrying an explicit map between the spaces as an additional obligation. To OFN and RER: G1 freeze record and the hash of this release on adoption. To Dyadic: the receipts above and §7.3.

### §7.3 Downstream Dependents Register (v0.3.21) {#sec-7-3-dependents}

Owner editions that consume RECOG RIDs (as inspected v0.3.21). **Notification rule:** any change to the statement, hypotheses, domain or rows, constants, track or grade of a listed RID is notified to every listed consumer before the RECOG release that makes it; adding a new row or window to a theorem is additive and is notified on release.

| RECOG RID | consumers (edition, point of use) | dependency type |
|---|---|---|
| RECOG-THM-R9-MEMORY ($\Lambda_1$, $c_{\rm iso}$, rows $(C_2,q_{\max})=(517,\tfrac1{400})$ on $\lvert z\rvert\le\tfrac1{20}$ and $(163,\tfrac1{1600})$ on $\lvert z\rvert\le\tfrac1{40}$, rows not mixed; $C_z$ track) | Dyadic v6.4.15–v6.4.17 §6.14: T1 and memory law (conditional on R9), T2 (conditional on T1), DYAD-THM-OPEN21-PRIMITIVE-PHASE-REMAINDER (conditional on R9; reported edition); Dyadic §6.14 consumer cross-reference; OFN v0.10 RF-O09-01/02; RRF v0.8.3 §2.4, §4.1a | conditional theorems (Dyadic); reference (OFN, RRF) |
| RECOG-ALG-CHART-LAWS | Dyadic v6.4.11+ §6.14 cross-reference | reference |
| RECOG-ALG-NU3-CLOSED-FORM, RECOG-ALG-NU3-NONVANISHING | Dyadic v6.4.11+ §1, §6.11 (OPEN 9 closed sub-item) | import at owner grade |
| RECOG-ALG-LEADING-RETURN-EQUIVARIANCE | Dyadic v6.4.11+ §6.9 (general-$p$ proof provenance of DYAD-ALG-BRIDGE-LEMMA) | provenance (mutual-citation guard, §7) |
| RECOG-THM-P2-HET, RECOG-THM-P2-C0-FIRST | Dyadic v6.4.11+ OPEN 12 (PARTIAL by consumer theorems) | status dependency |
| RECOG-DEF-POLE-COMPARATOR, RECOG-DEF-STATE-COMPARATOR, RECOG-ALG-SELECTION-SIN, RECOG-ALG-SWAP-SPLIT | OFN v0.10 §6.4 (IMP-O08-17/18/19 as restated) | definition / scoped input |
| RECOG-ALG-SHEAR-COCYCLE-CLASSIFICATION, RECOG-ALG-SHEAR-WEIGHT-IDENTIFICATION, RECOG-ALG-SHEAR-ORIENTATION-CONJUGACY | OFN v0.10 §6.2a, §6.3–§6.4 (IMP-O09-01/02/03), OPEN-OFN-OPA; RRF v0.8.3 §4.2a; RER v0.2 r4.6 G9 (owner-first citation) | import at owner grade / interface pin |
| RECOG-ALG-BTOKEN-TRANSPORT, RECOG-ALG-SH-SECTION-SHADOW | RRF v0.8.3 §4.3, §6.3 | reference |
| RECOG-RESULT-F4-NETWORK-WELLPOSEDNESS (W1–W5) | RRF v0.8.3 §6.3 (see RF-1); RER v0.2 r4.6 G9 | interface prerequisites |
| RECOG-THM-TWIN-RADIAL-ACCESS | RRF v0.8.3 §4.2 (generator-family limit on OPEN-A) | reference |
| RECOG §§6.13a, 6.16–6.16f (token / transition / retention inventory) | OFN v0.10 RF-O09-02 | reference |

"""
edit("N1", "new §7.2 and §7.3 before §8",
 "## §8. Artifact and Script Registry {#sec-8-artifacts}",
 NEW72 + "## §8. Artifact and Script Registry {#sec-8-artifacts}",
 allowed_new_tags=["[ALG]", "[THM]"],
 allowed_new_rids=[])

# ---------------------------------------------------------------- §8 artifacts
edit("A1", "§8: R6 addendum memo, G1 record, G2 audit artifacts",
 "- [RID: RECOG-ART-MEMO] :: `RECOG_MEMO_TO_STREAMS_2026-09-17.md` (amended 18 Sep: §3 single enclosure deliverable) :: cross-stream handovers and requests :: `[DEF]`",
 "- [RID: RECOG-ART-MEMO] :: `RECOG_MEMO_TO_STREAMS_2026-09-17.md` (amended 18 Sep: §3 single enclosure deliverable) :: cross-stream handovers and requests :: `[DEF]`\n"
 "- [RID: RECOG-ART-MEMO-R6-ADDENDUM] `[v0.3.21; registration of an existing record]` :: `RECOG_MEMO_TO_STREAMS_2026-09-30_R6_ADDENDUM.md` (sha256 `24a9fd85e35c08fb3cc7e3d5f4e35f506e080124feae036c05442bf0fed4c9f3`) :: R6 cross-stream addendum :: `[DEF]`\n"
 "- [RID: RECOG-ART-FREEZE-0320] `[v0.3.21]` :: `RECOG_v0_3_20_FREEZE_DECISION_PROVENANCE.md` (sha256 `5c00f66dae7d4de6ccd4a04d642a23edfc861bbd6bd55e432513747fbd679b55`) :: external freeze record of v0.3.20 (G1; governance, not a scientific review) :: `[SESSION]` record\n"
 "- [RID: RECOG-ART-G2-AUDIT] `[v0.3.21]` :: `RECOG_G2_DYADIC_CLAIM_AUDIT_v0_1_2.md` (`99fce74bd8f3c2151da2de548e4d66603b89ec9aefbd1773cfa2126381ba20aa`), `RECOG_G2_DYADIC_SOURCE_FIDELITY_RUN_v0_1.md` (`8cb0119331c70b52412701f9056c7db651ff87fbe5f75ebff370aa002fa15ecb`, the reviewed record) and `RECOG_G2_DYADIC_SOURCE_FIDELITY_RUN_v0_1_1.md` (`97a24f129f62060356611ef74561aeecc3e0fe8a1025ce1a65634eeb146b1d30`; identical in §§1–6, adds §7 receiving disposition of 20 Oct 2026), `RECOG_G2_GENESIS_OFN_RRF_CLAIM_AUDIT_v0_1.md` (`36e44660836f83448b871253ac0bfe98bb23a65d8033504086d84cd312ba151e`); scripts `recog_g2_dyad_passage_diff.py` v0.3 (`8af2a00da31461d557dea765af0c4a04882608f0428232d6f39eb7edf782a364`), `recog_g2_section_diff.py` v0.1.1 (`aade4354d2172b96590de70c9d6236214e84646b2527133f60ffce7a033204d9`) and their comparison reports :: claim-level synchronization audit (§7.2); reviewer dispositions: Dyadic CLOSED, Genesis/OFN/RRF ACCEPTED (20 Oct 2026) :: `[SESSION]` records; scripts `[ENG]`",
 allowed_new_tags=["[DEF]", "[ENG]", "[SESSION]"],
 allowed_new_rids=["RECOG-ART-MEMO-R6-ADDENDUM", "RECOG-ART-FREEZE-0320", "RECOG-ART-G2-AUDIT"])

# ---------------------------------------------------------------- Appendix A + footer
edit("V1", "Appendix A v0.3.21 entry",
 "### v0.3.20 — 30 September 2026 (orientation conjugacy)",
 "### v0.3.21 — DRAFT r2, 20 October 2026 (owner synchronization; not adopted)\n"
 "- **Lifecycle:** v0.3.20 frozen 19 Oct 2026 (`fdb8c9a7…b8df`), external record G1; header freeze status and supersedes line updated.\n"
 "- **§7.2 [new]:** G2 claim-level audit summary (Dyadic, Genesis, OFN, RRF), receipts N10–N13 (N13 conditional), outbound notices (RRF repin; RF-1).\n"
 "- **§7.3 [new]:** downstream dependents register and notification rule.\n"
 "- **SG-R14:** quantitative raw-track offset by reference to Dyadic N11 (T2), with its rows, conditions and the $C_W^{(h)}$ exclusion.\n"
 "- **§2:** R1 receipt of the OFN v0.10 OPA additions (no import); R3 dependency records Dyadic OPEN 12 PARTIAL and its residual items; R5 export targets moved to OFN v0.10 §6.2a rows. No status line changed.\n"
 "- **§7 rows:** synchronization note; identifiers (DYAD-DEF-PRIMITIVE-MAP; GEN-DEF-PRIMITIVE-METRIC, GEN-THM-PRIMITIVE-METRIC-INVARIANCE); bridge-lemma mutual-citation guard; J_Q row restated with the owner's narrowed scope; OFN and RRF rows note the current editions. Source pins retained.\n"
 "- **§8:** R6 addendum memo, G1 record and G2 audit artifacts registered.\n"
 "- **r1 → r2 (receiving review, 20 Oct 2026):** §7.3 R9 constants given as the two certified rows, not mixed; source-fidelity record cited as reviewed v0.1 (`8cb01193…15ecb`) plus v0.1.1 carrying the receiving disposition; supersedes line attributes F4 to v0.3.19 and orientation conjugacy to v0.3.20; status summary distinguishes existing scientific RIDs from the three new artifact IDs; OFN v0.8 marked as the historical source pin of the v0.3.18 audit; RRF row labels its old wording as historical source state. Same frozen base; r1 manifest superseded by r2 manifest.\n"
 "- **Unchanged:** every scientific statement of §§1–6 and §6.x ledgers, every RID's statement and grade, every OPEN status (R1, R3 PARTIAL; R4, R5, R6 ACTIVE; R2, R7–R11 CLOSED). Not introduced: any token/memory read-out vocabulary (reserved for a later cell). Header compaction not performed (separate mechanical change, if authorized).\n\n"
 "### v0.3.20 — 30 September 2026 (orientation conjugacy)")
edit("V2", "footer",
 "*END OF DOCUMENT — RTG_RELATIONAL_RECOGNITION_DSN_v0.3.20*",
 "*END OF DOCUMENT — RTG_RELATIONAL_RECOGNITION_DSN_v0.3.21 (DRAFT r2; not adopted; v0.3.20 frozen `fdb8c9a7…b8df` remains authoritative until adoption)*")

def main():
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(2)
    base = open(sys.argv[1], "rb").read()
    h = hashlib.sha256(base).hexdigest()
    if h != BASE_SHA:
        print(f"REFUSED: base sha256 {h} != {BASE_SHA}"); sys.exit(2)
    out_dir = sys.argv[2] if len(sys.argv) > 2 else "."
    text = base.decode("utf-8")
    for e in E:
        n = text.count(e["old"])
        if n != 1:
            print(f"ABORT: edit {e['id']} anchor count {n}"); sys.exit(2)
        text = text.replace(e["old"], e["new"], 1)
    draft = os.path.join(out_dir, "RTG_RELATIONAL_RECOGNITION_DSN_v0_3_21_DRAFT_r2.md")
    open(draft, "wb").write(text.encode("utf-8"))
    json.dump({"base_sha256": BASE_SHA, "edits": E}, open(os.path.join(out_dir, "recog_v0_3_21_edits_r2.json"), "w"),
              ensure_ascii=False, indent=1)
    print(f"BUILT {draft} sha256 {hashlib.sha256(text.encode('utf-8')).hexdigest()} ({len(E)} edits)")

if __name__ == "__main__":
    main()
