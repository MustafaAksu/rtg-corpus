#!/usr/bin/env python3
"""Build RTG_NUMBER_GENESIS_DSN_v1_20_8_DRAFT_r3.md from frozen v1.20.7 by exact-once edits.

r3 (narrow fact synchronization after the co-owner acceptance of r2, 21 Oct 2026; PI choice): Dyadic v6.4.19,
RECOG v0.3.22 and RRF v0.8.4 were adopted after r2. Only E01-E05, E16, E27, E28, E29 and E30 change;
every other edit is byte-identical to r2. No constant is imported; Dyadic import pins stay at v6.4.18.

r2 (co-owner review of r1, 20 Oct 2026): (1) the §1.1 relational-primacy import is split into two DEF imports,
one per OFN RID; (2) the L-PHASE receipt replay is pinned in the §9.2 artifact registry (record, certificate,
helpers, JSON). Everything else is r1 unchanged.

Scope (co-owner GO, 20 Oct 2026): maintenance only.
  consumer/pointer synchronization; notice and request dispositions; N3 pin removal;
  OFN Sec.1.1 import narrowing; six approved RID allocations; explicit primitive-lift DEF and D_M DEF;
  q_m typing; L-PHASE explicit-constant OPEN sub-item WITHOUT any constant.
No statement, proof, domain or grade of an existing result changes.
Usage: python3 build_v1_20_8_r2.py  (reads base from cwd, writes draft + edits json)
"""
import hashlib, json, sys

BASE = "RTG_NUMBER_GENESIS_DSN_v1_20_7.md"
BASE_SHA = "c4637e7a5cfaf8eaf001746f172111385f5df2a8cd552e3ab56308ff7abfab28"
OUT = "RTG_NUMBER_GENESIS_DSN_v1_20_8_DRAFT_r3.md"

src = open(BASE, encoding="utf-8").read()
assert hashlib.sha256(src.encode()).hexdigest() == BASE_SHA, "base hash mismatch"
L = src.split("\n")

def line_starting(prefix):
    hits = [x for x in L if x.startswith(prefix)]
    assert len(hits) == 1, (prefix, len(hits))
    return hits[0]

def sub1(s, a, b):
    assert s.count(a) == 1, (a[:60], s.count(a))
    return s.replace(a, b)

E = []   # (id, old, new)
def edit(eid, old, new):
    E.append((eid, old, new))

# ---------------- header
edit("E01", "# RTG Number Genesis DSN v1.20.7\n", "# RTG Number Genesis DSN v1.20.8 — DRAFT r3\n")
edit("E02", "**Date:** September 25, 2026  \n", "**Date:** October 21, 2026 (DRAFT r3; v1.20.7 dated September 25, 2026)  \n")
old = line_starting("**Document status:** ACTIVE owner ledger; **owner synchronization + scoped algebra adoption + governance repair.**")
edit("E03", old, "**Document status:** DRAFT r3 — not adopted. **Maintenance release: consumer synchronization + RID allocation + interface definition.** No theorem-level change. **Supersedes on adoption:** v1.20.7 (`c4637e7a…ab28`, frozen 2026-10-01), which remains the canonical owner until adoption. Predecessor document status (v1.20.7): ACTIVE owner ledger; owner synchronization + scoped algebra adoption + governance repair; supersedes v1.20.6 (`2a51c4b1…48c5`).  ")
old = line_starting("**Companion documents (current verified pointer targets):**")
edit("E04", old, "**Companion documents (current verified pointer targets):** `RTG_PROGRAMME_OVERVIEW_v1.2` · `RTG_ONTOLOGICAL_FOUNDATIONS_v0.10` · `RTG_DYADIC_OSCILLATOR_DSN_v6.4.18` · `RTG_DISCRETE_GENESIS_DSN_v2.12.13` · `RTG_GENESIS_GEOMETRY_DSN_v2.8.9`. `[v1.20.8]` OFN, Dyadic and Genesis pointers were advanced after a claim-level check of every imported statement (§9.1). The current Dyadic edition is v6.4.19 (adopted 20 Oct 2026, `40c9e63f…6ec9`); it adds the §6.14 L-PHASE row-A theorem and leaves §§2–3, §6.1, §6.4, §6.11 and the DYAD-THM-PRIM-CTR passage byte-identical to v6.4.18, so the import pins stay at v6.4.18 until the L-PHASE import edition. Consumer and reference documents (`RTG_RELATIONAL_RECOGNITION_DSN_v0.3.22`, `RTG_RRF_REPRESENTATION_REGISTRY_v0.8.4`) are recorded in §9.  ")
old = line_starting("**Status summary (scientific state fixed at v1.20;")
edit("E05", old, old + " `[v1.20.8]` Maintenance only: no result, proof, domain or grade changes; N-5A-S1 statement RIDs are allocated (§6.6) and the explicit L-PHASE constant is registered as an OPEN sub-item: Dyadic adopted the row-A theorem in v6.4.19, and its import by RID is deferred to a later NUMGEN edition; no constant is entered.")

# ---------------- §1.1 OFN import narrowing (OFN v0.10 §12.3 consumer register)
old = line_starting("`[RESULT]` `[from: DEF]` `[import: RTG_ONTOLOGICAL_FOUNDATIONS_v0.8 §1.1 | RID unavailable]` **Relational primacy.**")
edit("E06", old, "`[DEF]` `[import: RTG_ONTOLOGICAL_FOUNDATIONS_v0.10 §1.1 | RTG-OFN-DEF-RELATIONAL-CONTENT]` **Relational primacy.** Physical content is relational; an isolated node has no independently specified physical state.\n\n"
"`[DEF]` `[import: RTG_ONTOLOGICAL_FOUNDATIONS_v0.10 §1.1 | RTG-OFN-DEF-PHASE-GAUGE]` **Global phase is gauge.** A common shift of all node phases leaves physical content unchanged in the declared phase models. This concerns absolute phase only and does not make phase differences a complete state (OFN SG-OFN-STATE).")
old = line_starting("`[RESULT]` `[from: DEF]` `[import: RTG_ONTOLOGICAL_FOUNDATIONS_v0.8 §1.2 | RID unavailable]` **No external physical time.**")
edit("E07", old, "`[DEF]` `[import: RTG_ONTOLOGICAL_FOUNDATIONS_v0.10 §1.2 | RTG-OFN-DEF-BACKGROUND-TIME]` **No pre-given physical time.** Physical time is not an independent primitive background. Formal step/block indices are permitted bookkeeping; interpreting them as physical time requires a separate construction. Relational events are candidate time-bearing structure; the event rule and duration calibration remain open (OFN OPEN-OFN-7).\n\n`[COR v1.20.8]` **OFN import narrowing.** Through v1.20.7 these two blocks were graded RESULT-from-DEF with `RID unavailable` and read more broadly than the source (\"only relational phase differences are physical\"; \"the sequence of relational events constitutes RTG time\"). OFN v0.10 §12.3 flags them as overly broad. They now import the OFN definition RIDs at source grade DEF (K4) with OFN's wording. No Number Genesis result used the broader reading; the RF-06 guard below already applied the state-completeness limit.")
old = line_starting("`[RESULT]` `[from: THM]` `[import: RTG_DYADIC_OSCILLATOR_DSN_v6.4.10 §6.1, §6.4 | RID unavailable]` **Continuous phase/winding support.**")
edit("E08", old, old.replace("RTG_DYADIC_OSCILLATOR_DSN_v6.4.10 §6.1, §6.4", "RTG_DYADIC_OSCILLATOR_DSN_v6.4.18 §6.1, §6.4"))
old = line_starting("`[RESULT]` `[from: DEF]` `[import: RTG_DISCRETE_GENESIS_DSN_v2.12.13 SG-10; RTG_DYADIC_OSCILLATOR_DSN_v6.4.10 SG-14;")
edit("E09", old, old.replace("RTG_DYADIC_OSCILLATOR_DSN_v6.4.10 SG-14", "RTG_DYADIC_OSCILLATOR_DSN_v6.4.18 SG-14"))
old = line_starting("`[RESULT] [from: THM]` `[import: RTG_DYADIC_OSCILLATOR_DSN_v6.4.10 §6.11 | DYAD-THM-Q403-PHASELAW]` **Upstream cascade item synchronized:**")
edit("E10", old, old.replace("v6.4.10 §6.11", "v6.4.18 §6.11"))
old = line_starting("`[RESULT] [from: THM]` `[import: RTG_DYADIC_OSCILLATOR_DSN_v6.4.10 §6.11 | DYAD-THM-Q403-PHASELAW]` **All-`p` cascade closure imported.**")
edit("E11", old, old.replace("v6.4.10 §6.11", "v6.4.18 §6.11"))

# ---------------- §6.1 N3 pin
old = "of the `[CAND]` phi* law (`DYAD-CAND-PHISTAR-ENTRY-PHASE`)."
edit("E12", old, "of the `[CAND]` phi* law (`[RID unavailable — historical phi* entry-phase law; source not identified (Dyadic N3)]`; v1.20.8 correction: the former pin `DYAD-CAND-PHISTAR-ENTRY-PHASE` names no Dyadic RID and is removed; the Dyadic asymptotic-phase objects of v6.4.15 are not a substitute without a separate comparison proof).")

# ---------------- §6.6 N-5A-S1-INF: DEFs, RIDs, typing, OPEN sub-item
old = "`[RESULT] [from: ALG]` **L-BACKBONE CLOSED from L1.** From\n"
edit("E13", old,
"`[DEF]` [RID: NUMGEN-DEF-N5AS1-PRIMITIVE-LIFT] `[v1.20.8]` **Primitive angular lift.** For a start `x` on the declared punctured tube, write `W_n = W(T^n x)` with `W = rho + omega eta_wrap` (so `Theta = arg W`, `Q_true = |W|^2`). Fix a real representative `phi_hat_0` of `arg W_0` and set\n"
"```text\n"
"phi_hat_(n+1) = phi_hat_n + delta_T(T^n x),   delta_T(y) := Arg( W(Ty) / W(y) )   (principal value).\n"
"```\n"
"The increments `phi_hat_n - phi_hat_0` do not depend on the representative. L-MONO below makes this lift strictly increasing on the tube (`pi/6 < delta_T < pi/2`); it is the lift used by N-5A-S1, GAP-LOCK and INF-1 since v1.11. (v1.20.8: this states explicitly the lift previously defined only through L-MONO; no statement changes.)\n\n"
"`[DEF]` `[v1.20.8]` `[scope: N-5A-S1-INF]` **Block-sampled primitive amplitude.** In L-BACKBONE, L-PHASE and INF-1, `q_m := Q_true(T^(6m) x)` is the primitive observable at block base point `T^(6m) x` (block index `m`, counted from the start `x`, on the declared tube). It is not the Dyadic normalized-chart variable `q = |z|^2` (SG-NG-18; answers OFN REQ-O09-03).\n\n"
"`[RESULT] [from: ALG]` [RID: NUMGEN-RESULT-N5AS1-L-BACKBONE] **L-BACKBONE CLOSED from L1.** From\n")
edit("E14", "`[RESULT] [from: ALG]` **L-MONO CLOSED, sharpened at v1.12.1.**", "`[RESULT] [from: ALG]` [RID: NUMGEN-RESULT-N5AS1-L-MONO] **L-MONO CLOSED, sharpened at v1.12.1.**")
edit("E15", "`[RESULT] [from: ALG]` **L-PHASE CLOSED from the exact primitive six-step iterate.**", "`[RESULT] [from: ALG]` [RID: NUMGEN-RESULT-N5AS1-L-PHASE] **L-PHASE CLOSED from the exact primitive six-step iterate.**")
old = "This is an exact-primitive finite-iterate theorem, not an import from the continuous cubic-vector truncation.\n\n`[RESULT] [from: ALG]` **INF-1.** With\n"
edit("E16", old,
"This is an exact-primitive finite-iterate theorem, not an import from the continuous cubic-vector truncation.\n\n"
"`[OPEN]` `[target: THM]` `[v1.20.8]` **L-PHASE explicit constant — Dyadic row-A theorem adopted upstream; NUMGEN import deferred.** An explicit rational `C` on the Dyadic tube `U = {0 < Q_true <= 1/625}` (block base points), with the one-step branch certified on `U_T`, is an adopted Dyadic owner result: `DYAD-THM-LPHASE-ROWA-REMAINDER`, Dyadic v6.4.19 §6.14 (adopted 20 Oct 2026, `40c9e63f…6ec9`; notice N15). Its interface objects are the ones NUMGEN confirmed as I1–I5, and the NUMGEN receipt replay was byte-identical (§9.1 dispositions; execution pins in §9.2). No constant is entered in this edition: the `C` of L-PHASE stays existential here, and the import by RID is reserved for a NUMGEN edition after v1.20.8. An explicit-tube INF-1 would additionally need an explicit L-BACKBONE constant (NUMGEN-side; not started).\n\n"
"`[DEF]` [RID: NUMGEN-DEF-N5AS1-DEFECT] `[v1.20.8]` **Accumulated block defect.** For `M >= 0`, `D_M := 2 pi M - (phi_hat_(6M) - phi_hat_0)`, with `phi_hat` as in NUMGEN-DEF-N5AS1-PRIMITIVE-LIFT and the block counter taken from the start `x`; no B-event anchor enters. The INF-1 block below restates this definition verbatim.\n\n"
"`[RESULT] [from: ALG]` [RID: NUMGEN-RESULT-N5AS1-INF1] **INF-1.** With\n")
old = "D_M = tau log M + C_D + o(1) -> infinity.\n```\n\n`[RESULT] [from: ALG]` **INF-2 / crossing count.**"
edit("E17", old,
"D_M = tau log M + C_D + o(1) -> infinity.\n```\n\n"
"`[GUARD]` `[v1.20.8]` **Identifier scope.** `NUMGEN-OPEN-N5AS1-INF` remains the lifecycle RID of the closed research module; it is not the identity of INF-1 (`NUMGEN-RESULT-N5AS1-INF1`). `NUMGEN-THM-N5AS1-DEFECT-THRESHOLD-RATIO` remains the identity of the consecutive-ratio theorem that uses INF-1. Allocation of the six N-5A-S1 RIDs changes no statement, proof, domain or grade.\n\n"
"`[RESULT] [from: ALG]` **INF-2 / crossing count.**")
old = line_starting("`[RESULT] [from: THM] [import: RTG_DYADIC_OSCILLATOR_DSN_v6.4.10 §6.14 | DYAD-THM-PRIM-CTR]` **Explicit-domain boundary CLOSED (v1.20).**")
edit("E18", old, old.replace("RTG_DYADIC_OSCILLATOR_DSN_v6.4.10 §6.14 | DYAD-THM-PRIM-CTR", "RTG_DYADIC_OSCILLATOR_DSN_v6.4.18 §6.14 | DYAD-THM-PRIM-CTR"))

# ---------------- §6.8, NG-10 pins
old = line_starting("`[RESULT] [from: ALG]` `[import: RTG_ONTOLOGICAL_FOUNDATIONS_v0.8 §9 | RTG-OFN-OPEN-HOLONOMY-RANK-DIAGNOSTIC]`")
edit("E19", old, old.replace("RTG_ONTOLOGICAL_FOUNDATIONS_v0.8 §9", "RTG_ONTOLOGICAL_FOUNDATIONS_v0.10 §9"))
old = line_starting("`[RESULT]` `[from: NUM]` `[scope: reduced birth-race model]` `[source: RTG_GENESIS_GEOMETRY_DSN_v2.8.4 §6.6; RID: GEN-ART-SATURATION]`")
edit("E20", old, old.replace("RTG_GENESIS_GEOMETRY_DSN_v2.8.4 §6.6", "RTG_GENESIS_GEOMETRY_DSN_v2.8.9 §6.6"))

# ---------------- §9.1 import ledger rows
old = line_starting("| relational primacy / no external physical time |")
edit("E21", old, "| relational primacy / global-phase gauge / no pre-given physical time | `[import: RTG_ONTOLOGICAL_FOUNDATIONS_v0.10 §1.1 | RTG-OFN-DEF-RELATIONAL-CONTENT]` · `[import: RTG_ONTOLOGICAL_FOUNDATIONS_v0.10 §1.1 | RTG-OFN-DEF-PHASE-GAUGE]` · `[import: RTG_ONTOLOGICAL_FOUNDATIONS_v0.10 §1.2 | RTG-OFN-DEF-BACKGROUND-TIME]` | NG0, history/time interpretation | `[v1.20.8]` narrowed to the OFN definition RIDs and wording at source grade DEF (OFN v0.10 §12.3 consumer register); definition bodies unchanged since OFN v0.9 |")
old = line_starting("| holonomy-rank diagnostic / discrete-flat narrowing |")
edit("E22", old, old.replace("`[import: RTG_ONTOLOGICAL_FOUNDATIONS_v0.8 §4.4, §9 | RTG-OFN-OPEN-HOLONOMY-RANK-DIAGNOSTIC]`", "`[import: RTG_ONTOLOGICAL_FOUNDATIONS_v0.10 §4.4, §9 | RTG-OFN-OPEN-HOLONOMY-RANK-DIAGNOSTIC]`").rstrip(" |") + ". `[v1.20.8]` OFN v0.10: §4.4 typing and the OPEN record unchanged; status ACTIVE; NUMGEN §6.8 still cited by OFN as the inspected operator source |")
old = line_starting("| primitive dyad map, `Q_true`, order-6 structure / winding |")
edit("E23", old, old.replace("v6.4.10 §6.1, §6.4", "v6.4.18 §6.1, §6.4").replace("| verified; N-1 L1", "| verified; `[v1.20.8]` §6.1/§6.4 statements unchanged in v6.4.18 (map definition now carries `DYAD-DEF-PRIMITIVE-MAP`, provisional; not imported here); N-1 L1"))
old = line_starting("| explicit primitive contraction / six-phase invariant tube |")
edit("E24", old, old.replace("v6.4.10 §6.14 | DYAD-THM-PRIM-CTR", "v6.4.18 §6.14 | DYAD-THM-PRIM-CTR").replace("| verified (v1.20);", "| verified (v1.20); `[v1.20.8]` statement unchanged in v6.4.18 (§6.14 passage byte-identical v6.4.17→v6.4.18 per the Dyadic owner); Dyadic §7 consumer row records the NUMGEN acceptance;"))
old = line_starting("| `q=4,(0,3)` all-`p` cascade closure |")
edit("E25", old, old.replace("v6.4.10 §6.11 | DYAD-THM-Q403-PHASELAW", "v6.4.18 §6.11 | DYAD-THM-Q403-PHASELAW").replace("| verified against owner source;", "| verified against owner source; `[v1.20.8]` unchanged in v6.4.18;"))
old = line_starting("| Genesis reduced-sector saturation ceiling |")
edit("E26", old, old.replace("RTG_GENESIS_GEOMETRY_DSN_v2.8.4 §6.6", "RTG_GENESIS_GEOMETRY_DSN_v2.8.9 §6.6").replace("reduced birth-race scope retained |", "reduced birth-race scope retained; `[v1.20.8]` value and scope unchanged in v2.8.9 |"))
old = line_starting("`[GUARD]` Pointer refresh never upgrades claim status.")
edit("E27", old, old + "\n\n"
"**Notice and request dispositions (v1.20.8).** Owner-side records only; no import follows from a receipt.\n\n"
"| Item | From | Disposition |\n"
"|---|---|---|\n"
"| N3 — `DYAD-CAND-PHISTAR-ENTRY-PHASE` | Dyadic (v6.4.11) | ANSWERED: the pin names no Dyadic RID and is removed from §6.1; `[CAND]` cap kept; historical source not identified |\n"
"| N10–N13 — OPEN 3 / OPEN 3b / OPEN 3 lifecycle / OPEN 21 | Dyadic (v6.4.14–v6.4.17) | RECEIVED, no use. SG-19 accepted: no chart coefficient is read as an L1 or ISP-angle coefficient. N13 is conditional on RECOG R9; NUMGEN takes no R9-conditional input |\n"
"| N14 — smooth embedding | Dyadic (v6.4.18) | not addressed to NUMGEN; seen only |\n"
"| L-PHASE row-A certificate | Dyadic (SESSION, 20 Oct 2026) | interface I1–I5 CONFIRMED (`NUMGEN_INTERFACE_CONFIRMATION_LPHASE_ROWA_20261020_v0_1.md`, `7a91c223…f78f`); receipt replay byte-identical (`NUMGEN_RECEIPT_REPLAY_LPHASE_ROWA_20261020_v0_1.md`, `71bfc4c5…b66f`; execution pins in §9.2); no constant imported (§6.6 OPEN sub-item) |\n"
"| N15 — `DYAD-THM-LPHASE-ROWA-REMAINDER` | Dyadic (v6.4.19, `40c9e63f…6ec9`) | RECEIVED: owner theorem adopted 20 Oct 2026 at THM grade on the I1–I5 interface; import by RID deferred to a NUMGEN edition after v1.20.8 (§6.6 OPEN sub-item); no constant entered here. N3 status on the Dyadic side follows adoption of this edition |\n"
"| REQ-O09-03 — L-BACKBONE RID and `q_m` typing | OFN (v0.9) | ANSWERED: `NUMGEN-RESULT-N5AS1-L-BACKBONE`; `q_m` typed in §6.6 as block-sampled primitive `Q_true` |\n"
"| §1.1 opening-import scope | OFN v0.10 §12.3 | ANSWERED: §1.1 narrowed to three DEF imports, one per OFN RID (`RTG-OFN-DEF-RELATIONAL-CONTENT`, `RTG-OFN-DEF-PHASE-GAUGE`, `RTG-OFN-DEF-BACKGROUND-TIME`) at source grade |\n"
"| A1a RID request (INF-1, D_M) | RECOG (20 Oct 2026) | ANSWERED (option 1): `NUMGEN-RESULT-N5AS1-INF1`, `NUMGEN-DEF-N5AS1-DEFECT`; canonical on adoption of this edition |\n"
"| FMS v0.6.4 R8 provenance label | FMS (session ledger) | Outbound notice prepared (`NUMGEN_NOTICE_TO_FMS_R8_ATTRIBUTION_20261020_v0_1.md`): no such statement in v1.20.7; correction is FMS's |")

# ---------------- §9.2 consumer / reference rows
old = line_starting("| known consumer: `RECOG v0.3.5` / `RECOG-ALG-LATTICE-CLOCK` |")
edit("E28", old, old + "\n| known consumer (v1.20.8): `RECOG v0.3.22` (adopted 20 Oct 2026, `0dcce9e4…bcd9`; project copy hashed; predecessor v0.3.21 `a3459522…0ae3`) | claim-level synchronized against v1.20.7 at RECOG v0.3.18 (L1 contraction, N-1C, defect-threshold ratio, GAP-LOCK Lemma 3, GATE 1, INF-1: identical); v0.3.22 §6.13b/§7 imports INF-1 and `D_M` from v1.20.7 §6.6 verbatim with `RID unavailable` and the recorded governance line, resolved by the v1.20.8 allocations `NUMGEN-RESULT-N5AS1-INF1` / `NUMGEN-DEF-N5AS1-DEFECT` (repin is RECOG's, in a separate revision after adoption of this edition) | `[PROVENANCE]` consumer record, not a theorem change |")
old = line_starting("| working-methodology references (noncanonical) |")
edit("E29", old, old + "\n| representation registry reference (v1.20.8) | `RTG_RRF_REPRESENTATION_REGISTRY_v0.8.4` (adopted working standard, 20 Oct 2026, `2fb0a0fe…afce`; predecessor v0.8.3 `b393657e…a187`) supersedes the RRF v0.6 pointer above; it cites v1.20.7 §6.6 (M2-1, Census-1), §6.4 N-3A and §6.8 NG-7A correctly | `[PROVENANCE]` only; no theorem import; no `RRF-*` profile as canonical fact |")

old = line_starting("| `NG_SELFCHECK_REFERENCE_TRANSPORT_v1.md`")
edit("E31", old, old + "\n"
"| `NUMGEN_INTERFACE_CONFIRMATION_LPHASE_ROWA_20261020_v0_1.md` (`7a91c223691b3705c2560fca452e671442939452e11cf98820512b182f46f78f`) | v1.20.8: interface confirmation I1–I5 of the Dyadic L-PHASE row-A certificate (lift, frame, observable, sign, domain) | `[SESSION]` interface record; no import |\n"
"| `NUMGEN_RECEIPT_REPLAY_LPHASE_ROWA_20261020_v0_1.md` (`71bfc4c597b4be502129a6d0da0b1c987723979eec1701b9c1b4187140c4b66f`) | v1.20.8: receipt replay of the Dyadic row-A certificate in a clean folder; inputs `dyad_numgen_lphase_rowA_cert.py` (`117484ae1a2509b6f6065d395840bfdfe2b0c977af0505f9fe6de68c13959cdb`), `qw.py` (`3a913062c1cdc6d151a2fb5b2f76d5354a367d1fa55df43f1f31d06e1b94cce8`), `tzw.py` (`f007d42cde36d2a70115b9db25f47b107c446735fa31c66664f620c3247a5609`), all matching the Dyadic `SHA256SUMS.txt`; exit 0, 10/10 gates, 6/6 negative controls failing; regenerated `lphase_rowA_certificate.json` byte-identical to the Dyadic copy (`8697c6970bd908327c66ef2ce3b2d38386947899033ef7f720bc096c4c3ad4fa`) | `[SESSION]` execution record of the same algorithm, not an independent engine; no constant imported |\n"
"| `ng_lphase_rm_indep_check_v0_1.py` (`d9d89bae20a376a3e5992dacdb4263f4b6948af4a739ce3ab4c91c37e1e57ccf`) + `.log` (`e2a0d15a94676348d03ca74b4272b4a940b90d692dc03390cc49fd7e622cf661`) | v1.20.8: NUMGEN-side primitive-map sampling of `sup|r|/Q^(3/2)` and of the one-step ratio, independent of Dyadic code | `[NUM]` acceptance-gate support; not a proof input |")

# ---------------- changelog
edit("E30", "## Changelog\n### v1.20.7 — October 1, 2026\n",
"## Changelog\n"
"### v1.20.8 — DRAFT r3 — October 21, 2026 (not adopted)\n\n"
"**Maintenance release: consumer synchronization + RID allocation + interface definition** (co-owner GO, 20 Oct 2026). No result, proof, domain or grade changes; no constant is imported.\n\n"
"**1. Pointer synchronization.** OFN v0.8 → v0.10, Dyadic v6.4.10 → v6.4.18, Genesis v2.8.4 → v2.8.9 on the live import blocks and §9.1 rows, after a claim-level check of each imported statement (all unchanged). Inline citations that record where a statement was checked (the RF-06 guard's OFN v0.8 guards; the D15 sync record; the v1.20 provenance sentences naming Dyadic v6.4.10) are kept as verified-at-version history. RRF v0.6 pointer superseded by v0.8.4 (adopted working standard); RECOG v0.3.22 recorded as consumer. Dyadic v6.4.19 is recorded in the companion line; its consumed passages are byte-identical to v6.4.18, so the pins are not moved in this edition.\n\n"
"**2. OFN §1.1 import narrowing (OFN v0.10 §12.3).** The two opening OFN imports become three DEF imports, one per OFN RID (`RTG-OFN-DEF-RELATIONAL-CONTENT`, `RTG-OFN-DEF-PHASE-GAUGE`, `RTG-OFN-DEF-BACKGROUND-TIME`), with OFN's wording (K4), replacing RESULT-from-DEF with `RID unavailable` and the broader paraphrases. A COR v1.20.8 note in §1.1 records the change.\n\n"
"**3. RID allocation (co-owner ruling, 20 Oct 2026; RECOG A1a request; OFN REQ-O09-03).** `NUMGEN-DEF-N5AS1-PRIMITIVE-LIFT`, `NUMGEN-DEF-N5AS1-DEFECT`, `NUMGEN-RESULT-N5AS1-L-BACKBONE`, `NUMGEN-RESULT-N5AS1-L-MONO`, `NUMGEN-RESULT-N5AS1-L-PHASE`, `NUMGEN-RESULT-N5AS1-INF1`. They become canonical owner RIDs on adoption of this edition. `NUMGEN-OPEN-N5AS1-INF` stays the module lifecycle RID; `NUMGEN-THM-N5AS1-DEFECT-THRESHOLD-RATIO` stays its own theorem (§6.6 GUARD).\n\n"
"**4. Interface definitions.** Explicit DEF of the primitive lift `phi_hat` (sum of principal one-step angles; increasing by L-MONO) and of `D_M`; DEF typing of `q_m` as block-sampled primitive `Q_true` (not the Dyadic chart `q`). The INF-1 block keeps its inline restatement of `D_M` verbatim.\n\n"
"**5. L-PHASE explicit constant registered as an OPEN sub-item.** Dyadic adopted the row-A theorem (`DYAD-THM-LPHASE-ROWA-REMAINDER`, v6.4.19); its import by RID is deferred to a later NUMGEN edition; no constant entered (co-owner constraint).\n\n"
"**6. Dispositions (§9.1).** Dyadic N3 answered (pin removed, `[CAND]` cap kept); N10–N13 received, no use; N14 seen; N15 received (import deferred); OFN REQ-O09-03 and §1.1 scope answered; RECOG A1a RID request answered; FMS R8 attribution notice prepared. The L-PHASE interface confirmation, receipt replay and NUMGEN-side sampling are pinned in §9.2.\n\n"
"**Draft history.** r1 (`eef001d1…c63c`): co-owner review of 20 Oct 2026 — SCIENTIFIC SCOPE ACCEPTED, two repairs required. r2 applies exactly those: the §1.1 relational-primacy import is split into one DEF import per OFN RID; the receipt replay is pinned in §9.2 with record, certificate, helper and JSON hashes. No other change. r2 (`423cd719…7b78`): co-owner review of 20 Oct 2026 — REVIEW ACCEPTED, PI adoption pending. r3 is a narrow fact synchronization for owner editions adopted after r2 (PI choice, 21 Oct 2026): the L-PHASE OPEN sub-item and the status summary record the Dyadic v6.4.19 adoption with the import deferred; N15 receipt row; RECOG v0.3.22 and RRF v0.8.4 rows; companion-line note on v6.4.19 with the pins kept at v6.4.18; edition markers. No constant imported; every other edit byte-identical to r2.\n\n"
"### v1.20.7 — October 1, 2026\n")

# ---------------- apply
dst = src
for eid, a, b in E:
    dst = sub1(dst, a, b)
open(OUT, "w", encoding="utf-8").write(dst)
json.dump([{"id": i, "old": a, "new": b} for i, a, b in E], open("v1_20_8_r3_edits.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(OUT, hashlib.sha256(dst.encode()).hexdigest(), "edits:", len(E))
