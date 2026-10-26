#!/usr/bin/env python3
"""Number Genesis v1.21, stage 1: corrected intermediate (a build stage, not an edition).

Applies, to the adopted v1.20.8 file (tag numgen-v1.20.8, sha256 835a56f8...817e), the stage-1 corrections fixed by
the owner dispositions of 26 Oct 2026 and the PI's "başla" (26 Oct 2026):
  records/numgen/NUMGEN_OWNER_DISPOSITION_ADVISORY_v1_20_8_CLAUDE_20261026.md (PR #70),
  records/numgen/NUMGEN_OWNER_DISPOSITION_ADVISORY_v1_20_8_chatgpt_20261026.md (PR #72),
  records/numgen/NUMGEN_OWNER_DISPOSITION_RECONCILIATION_v1_20_8.md (PR #73; five form resolutions fixed),
  records/numgen/ATLAS_ADVISORY_NUMGEN_v1_20_8_RECONCILIATION.md §3 (the merged row list).

Round 2 (26 Oct 2026; ChatGPT co-owner review on PR #74, comment 6416152715, ACCEPT WITH CHANGE): R1 the acceptance
matrix domain column names each side's domain with "comparison only; no inclusion claimed" instead of arrows; R2 the
evidence-availability clause says that the held records are on the branch upload/numgen-records at the listed paths and
are reachable at the release commit only if that branch is merged first. Applied in place to E11 and E31. Round-1
intermediate (superseded, kept on record): 702e3917126edfeeda41e43b6a8ad820695b5feec19a61e724b12849dfb83880.

Groups (labels only; every edit is applied):
  NA02  Dyadic row-A import (DYAD-THM-LPHASE-ROWA-REMAINDER) replacing the §6.6 OPEN sub-item; §9.1 import row; N15 states
  NA01  explicit-domain counterparts (RECOG v0.3.24) recorded as consumer-side confirmations: pointer sentences at the
        affected §6.6 statements; §9.1 acceptance matrix; inbox-item disposition row. Nothing imported from RECOG.
  NA03  domain alias table (U_NG, U_NG,tube, U_D,base, U_D,tube, U_R,base; U_NG = RECOG's U_NUMGEN) and labels at the
        explicit-domain points of use
  NB07  tier-1 RIDs at GAP-LOCK 1-3, INF-2 and the first-nonlinear cyclic-average theorem; NB08 identifier guard
  NA04  stale pins in place (Programme v1.3, Genesis v2.9, §7 Q403 pin, DZT provenance, §9.1 column label, one
        abbreviated hash); NC19 consumers-and-pins block
  NA05  scope words at the N-1 tree and the N-1A0/N-1A1 status lines
  NB09  evidence-state clause and in-ledger keys at §9.2; artifact availability (upload/numgen-records/)
  NB11  sampled L-PHASE ratio range made live at L-PHASE as [NUM] with its evidence pointer
  NC12  SG-NG-23 cross-reading of e^{pi/(3 tau)}
  NC13  Dyadic owner aliases: DYAD-ALG-P5-RADIAL at Delta Q_5 (gate: numgen_v1_21_stage1_checks.py A1), the relay RIDs
  NC14  phi* vs C_D^ext comparison conventions at the NG-0R-COV pin; stays OPEN
  NC16  §9.2 RECOG consumer row -> v0.3.24 (both facts, no grade asserted)
  I06   C7C-M4 hold: TDR-G request pointer and sensitivity-audit condition at §2 item 1
  I11   NG-7A/NG-7B hand-off wording and OFN v0.10 consumer pointer at §6.8
  CHG   one stage-1 entry under "## Changelog" (stage 2 turns the changelog into Appendix A)
Not edited in stage 1: the header block (lines 1-15) and the dated `[v1.20.x]` markers of untouched rows (stage 2);
NC-17 (q*) is deferred (no Dyadic answer at the stage-1 checkpoint); NC-18 tube bound unchanged.

Rules:
- the input must be the adopted v1.20.8 bytes;
- mode "line": `old` is a line prefix that must start exactly one line of the live region; the whole line is replaced
  by fn(line) (the log stores the full old and new line);
- mode "str": `old` is an exact substring occurring exactly once in the live region;
- live region = everything before "## Changelog"; the changelog region receives only the CHG insertion directly
  under its heading.

usage: build_numgen_v1_21_stage1.py BASE OUT EDITLOG_JSON
  BASE = `git show numgen-v1.20.8:dsn/RTG_NUMBER_GENESIS_DSN.md`
"""
import hashlib, json, sys

BASE_SHA = "835a56f82b2641343a0e2fa116b049a167c62efd4d13fe41236966c117f4817e"
BASE_TAG = "numgen-v1.20.8"
CHG_START = "## Changelog\n"
ROUND1_SHA = "702e3917126edfeeda41e43b6a8ad820695b5feec19a61e724b12849dfb83880"  # superseded by round 2 (R1, R2)
NEW_RIDS = ["NUMGEN-RESULT-N5AS1-GAPLOCK-ALPHABET", "NUMGEN-RESULT-N5AS1-GAPLOCK-COUNT",
            "NUMGEN-RESULT-N5AS1-GAPLOCK-SLIP-RATIO", "NUMGEN-RESULT-N5AS1-INF2", "NUMGEN-RESULT-N3CP-CYCLIC-AVERAGE"]
CHECK_SCRIPT = "evidence/numgen/scripts/numgen_v1_21_stage1_checks.py"

R24 = "`recog-v0.3.24` §6.13b"
REC_PTR = "See the acceptance matrix in §9.1."

def app(s):            # append a sentence to a line
    return lambda line: line + " " + s

def rep(a, b):         # exact single replacement inside the line
    def f(line):
        assert line.count(a) == 1, (a[:60], line.count(a))
        return line.replace(a, b)
    return f

def after(s):          # keep the line, add a new paragraph after it
    return lambda line: line + "\n\n" + s

def after_row(s):      # keep the table row, add a new row directly after it
    return lambda line: line + "\n" + s

# ---------------------------------------------------------------- texts
ROWA_BLOCK = (
"`[THM]` [import: RTG_DYADIC_OSCILLATOR_DSN_v6.4.22 §6.14 (producer edition v6.4.19) | DYAD-THM-LPHASE-ROWA-REMAINDER] "
"`[scope: block base points in U_D,base = {0 < Q_true <= 1/625}; one-step branch on U_D,tube; primitive observable]` "
"**L-PHASE explicit constant on the explicit Dyadic tube (imported).** For every start `x` in `U_D,base` and every block `m >= 0`: "
"(R) `phi_hat_(6(m+1)) - phi_hat_(6m) = 2 pi - tau Q_m + r_m` with `|r_m| <= (403/250) Q_m^(3/2)`; "
"(B) for every `y` in `U_D,tube`, `|W(Ty)/(lambda W(y)) - 1| <= 0.04654`, so `|delta_T - pi/3| <= arcsin(0.04654) < pi/6`. "
"Typed interface (Dyadic I1–I5, confirmed by NUMGEN at receipt): Dyadic's frame `𝓛` is NUMGEN's `W = rho + omega eta`; "
"Dyadic's `Q_m` is NUMGEN's block-sampled primitive `q_m`; Dyadic's increasing lift is NUMGEN-DEF-N5AS1-PRIMITIVE-LIFT; "
"the block defect is a lag (`D_M` increases); block base points lie in `U_D,base`, intermediate steps in `U_D,tube`. "
"Only this imported statement carries the constant `403/250`; NUMGEN-RESULT-N5AS1-L-PHASE above keeps its existential "
"constant on `U_NG`, its proof and its grade. Depends on: DYAD-THM-PRIM-CTR (`U_D,base`, `U_D,tube`), DYAD-THM-NF-REM "
"row A (owner proof). Evidence: statement read at `dyad-v6.4.22` (`EV-SRC-READ`); the Dyadic certificate was replayed "
"byte-identically by NUMGEN at receipt (§9.2), not rerun for this edition (`EV-NOT-RERUN`). See §9.1.\n\n"
"`[RESULT] [from: NUM]` `[scope: seed-family sampling on U_NG; not a proof input]` **Sampled ratio range.** "
"`sup|r|/Q^(3/2)` lies in `[1.3449, 1.3565]` across a 256-fold `Q_0` range (`NG_N5AS1_INF_REDUCTION_v1.md`, "
"`90eb6658…6e0b`; `ng_n5as1_inf_reduction_cert_v1.py` / `.log`, `41917710…ee36` / `4100e3a5…f755`; `EV-NOT-RERUN`), "
"below the imported ceiling `403/250`. The Dyadic owner cites this range beside its own sampled values.")

ALIAS_BLOCK = (
"`[DEF]` **Domain labels.** Five domains share the letters `U` and `U_T` across Number Genesis, Dyadic and RECOG; they are "
"not identified with each other beyond what is proved at the point of use.\n\n"
"| Label | Set | Source | Used for |\n|---|---|---|---|\n"
"| `U_NG` | `{0 < Q_true < delta}`, the existential L1 base sector above (radius chosen by continuity, not stated) | this section | every NUMGEN statement proved \"after shrinking\"; RECOG writes it `U_NUMGEN` |\n"
"| `U_NG,tube` | `U_NG union T(U_NG) union ... union T^5(U_NG)` (the `U_T` above) | this section | N-1/N-3A one-chart tube, L-MONO, the canonical B predicate |\n"
"| `U_D,base` | `{0 < Q_true <= 1/625}` | DYAD-THM-PRIM-CTR (`dyad-v6.4.22` §6.14; Dyadic writes `U`) | explicit base; seed admission; row-A block base points |\n"
"| `U_D,tube` | `union_(j<6) T^j(U_D,base)`, contained in `{|W| < 47/1000}` | DYAD-THM-PRIM-CTR (Dyadic writes `U_T`) | explicit tube; row-A branch clause |\n"
"| `U_R,base` | the set `U_D,base`, as RECOG's start domain | RECOG §6.13b (RECOG writes `U`) | RECOG's A1a/A1b explicit-domain theorems |\n\n"
"In this document an unlabelled `U` or `U_T` in a theorem scope means `U_NG` or `U_NG,tube`. No inclusion between "
"`U_NG` and `U_D,base` is asserted. The L1 coordinate `U = sqrt(3) rho/2` is a coordinate, not a domain. `q_m` is the "
"primitive `Q_true` at block base points (Dyadic's `Q_m`), not the Dyadic/RECOG chart variable `q = |z|^2`.")

PTR_LBACK = (
"*Explicit-domain counterpart (consumer theorem; not imported):* `RECOG-THM-A1A-RECIPROCAL-AMPLITUDE` (" + R24 + ") "
"bounds the per-block reciprocal increment by `(15/2) sqrt(Q_m)` on `U_R,base`. It is an increment bound (error type 1), "
"not an L-BACKBONE constant; L-BACKBONE keeps `U_NG` and its existential constants. " + REC_PTR)
PTR_LMONO = (
"*Explicit-domain counterparts:* `RECOG-THM-A1A-LIFT-ALIGNMENT` (" + R24 + "; consumer theorem, not imported) proves "
"`pi/6 < delta_T < pi/2` on `U_D,tube`; the branch clause (B) of the imported DYAD-THM-LPHASE-ROWA-REMAINDER (below) "
"gives `|delta_T - pi/3| <= arcsin(0.04654)` there. L-MONO keeps `U_NG,tube`. " + REC_PTR)
PTR_INF1 = (
"*Explicit-domain counterpart (consumer theorems; not imported):* `RECOG-THM-A1A-PHASE-EXISTENCE-U` (" + R24 + ") proves on "
"all of `U_R,base`, without RECOG R9 and without INF-1, that `lim_N (D_N^U - tau log N)` exists, with an explicit "
"absolutely convergent series (its tails are error type 2); `D_N^U` is RECOG's extension of NUMGEN-DEF-N5AS1-DEFECT to "
"`U_R,base`. `RECOG-RESULT-A1A-CD-AGREEMENT` identifies the limit with `C_D` on `U_R,base ∩ U_NG`. INF-1 keeps `U_NG`; "
"NUMGEN registers no explicit-domain INF-1 of its own. " + REC_PTR)
PTR_GAPLOCK = (
"*Explicit-domain counterpart (consumer theorem; not imported):* `RECOG-THM-A1B-SLIP-SCHEDULE-U` (" + R24 + ") proves on "
"`U_R,base`, with estimates on `U_D,tube`: events are lift crossings; every gap is `6` or `7`; "
"`s(M) = (3 tau/pi) log M + O(1)`; the digamma slip schedule `tau psi(a+M_k) - (k-1) pi/3 = L + epsilon_k` with an "
"a-priori ceiling `epsilon_k` (error type 3, not computable from `(a,k,M_k)` alone); hence `M_(k+1)/M_k -> exp(pi/(3 tau))`. "
"RECOG states that GAP-LOCK Lemmas 1–3 and INF-1 remain NUMGEN's. INF-2 and GAP-LOCK 1–3 keep `U_NG`; the digamma "
"schedule is RECOG's result and is not a NUMGEN statement. " + REC_PTR)

MATRIX = (
"**Acceptance matrix — explicit-domain theorems of RECOG v0.3.24 on NUMGEN objects** (owner dispositions of 26 Oct 2026). "
"Relationship ∈ {independent agreement, consumed theorem, not adopted}. Custody of every NUMGEN statement is unchanged; "
"nothing is imported from RECOG. Error types: (1) per-block reciprocal-amplitude increment; (2) summed tail / backbone "
"constant; (3) slip-schedule `epsilon_k`. None substitutes for another.\n\n"
"| NUMGEN statement | Counterpart RID | Event predicate / anchor | Primitive lift | Domains (no inclusion claimed; `U_R,base = U_D,base` as sets) | Clock | Estimate scope | Evidence grade | Relationship | Receiving status |\n"
"|---|---|---|---|---|---|---|---|---|---|\n"
"| L-BACKBONE `NUMGEN-RESULT-N5AS1-L-BACKBONE` | `RECOG-THM-A1A-RECIPROCAL-AMPLITUDE` | none (amplitude) | — | NUMGEN: `U_NG`; RECOG: starts in `U_R,base` (comparison only; no inclusion claimed) | block `m` | increment `(15/2) sqrt(Q_m)` (type 1) | THM | independent agreement | statement accepted; not imported |\n"
"| L-MONO `NUMGEN-RESULT-N5AS1-L-MONO` | `RECOG-THM-A1A-LIFT-ALIGNMENT` | — | NUMGEN-DEF-N5AS1-PRIMITIVE-LIFT (principal one-step increments) | NUMGEN: `U_NG,tube`; RECOG: `U_D,tube` (comparison only; no inclusion claimed) | one step | branch bound | THM | independent agreement | statement accepted; not imported |\n"
"| L-PHASE `NUMGEN-RESULT-N5AS1-L-PHASE` | `DYAD-THM-LPHASE-ROWA-REMAINDER` (Dyadic, not RECOG) | — | same (I1–I5) | NUMGEN: `U_NG`; imported Dyadic theorem: `U_D,base` base points (no inclusion claimed) | block `m`; `q_m` ≡ Dyadic `Q_m` | remainder ceiling `403/250` | THM | consumed theorem | adopted use: §6.6 import and the row above |\n"
"| INF-1 `NUMGEN-RESULT-N5AS1-INF1` | `RECOG-THM-A1A-PHASE-EXISTENCE-U`; `RECOG-RESULT-A1A-CD-AGREEMENT` | none (block defect) | same; `D_N^U` extends NUMGEN-DEF-N5AS1-DEFECT | NUMGEN: `U_NG`; RECOG: `U_R,base` (comparison only; no inclusion claimed); RECOG's agreement result holds on `U_R,base ∩ U_NG` | block count | existence and series; tails (type 2) | THM; RESULT | independent agreement | statement accepted; not imported |\n"
"| INF-2 `NUMGEN-RESULT-N5AS1-INF2` | `RECOG-THM-A1B-SLIP-SCHEDULE-U` (A), (B) | canonical B predicate | same | NUMGEN: `U_NG`; RECOG: `U_R,base` (comparison only; no inclusion claimed) | steps / blocks | `O(1)` | THM | independent agreement | statement accepted; not imported |\n"
"| GAP-LOCK 1 `NUMGEN-RESULT-N5AS1-GAPLOCK-ALPHABET` | `RECOG-THM-A1B-SLIP-SCHEDULE-U` (B), (C′) | NUMGEN: token `x -> T(x)` with `w(x) < 0 <= w(Tx)`, positive `rho`; RECOG: same predicate, anchor `n+1`; gaps coincide | same | NUMGEN: `U_NG,tube`; RECOG: starts in `U_R,base`, estimates on `U_D,tube` (comparison only; no inclusion claimed) | primitive steps | deficit `0.927 tau Q < Delta < tau Q + 1.82 Q^(3/2)` | THM | independent agreement | statement accepted; not imported |\n"
"| GAP-LOCK 2 `NUMGEN-RESULT-N5AS1-GAPLOCK-COUNT` | `RECOG-THM-A1B-SLIP-SCHEDULE-U` (B) | as above | same | NUMGEN: `U_NG`; RECOG: `U_R,base` (comparison only; no inclusion claimed) | `6M` primitive steps | `O(1)` | THM | independent agreement | statement accepted; not imported |\n"
"| GAP-LOCK 3 and slip rate `NUMGEN-RESULT-N5AS1-GAPLOCK-SLIP-RATIO` | `RECOG-THM-A1B-SLIP-SCHEDULE-U` (S) | as above; `M_k` = block index of the `k`-th 7-gap anchor | same | NUMGEN: `U_NG`; RECOG: `U_R,base` (comparison only; no inclusion claimed) | blocks | a-priori `epsilon_k` (type 3) | THM | independent agreement for the ratio limit; digamma schedule not adopted | statement accepted; not imported |")

CONSUMERS = (
"**Consumers and pins.** Owner record of the interfaces; the Programme interface register (IF rows) is the Programme's. "
"`Current companion` is the governing edition at this build; `Pin used` is the edition actually used for the claim.\n\n"
"| Direction | Counterpart | Objects | Pin used | Current companion | Programme row |\n|---|---|---|---|---|---|\n"
"| import | Dyadic | §6.1/§6.4 map and winding, SG-14, §6.11 DYAD-THM-Q403-PHASELAW, §6.14 DYAD-THM-PRIM-CTR | v6.4.18 (statements unchanged at v6.4.22) | `dyad-v6.4.22` | IF12 |\n"
"| import | Dyadic | §6.14 DYAD-THM-LPHASE-ROWA-REMAINDER | v6.4.22 (producer v6.4.19) | `dyad-v6.4.22` | IF12 |\n"
"| import | TDR-G | `Z_N`, finite recurrence, SG-10 firewall, DISC harness input | v2.12.13 | `tdrg-v2.12.13` | IF13 |\n"
"| import | OFN | §1.1 definitions, holonomy-rank diagnostic | v0.10 | `ofn-v0.10` | — |\n"
"| import | Programme | SG-PROG-1, SG-PROG-2 (`RTG-OPEN-GENERATOR-SELECTION`) | v1.3 | `programme-v1.3` | — |\n"
"| import | Genesis | §6.6 GEN-ART-SATURATION (NG-10 only) | v2.9 | `gen-v2.9` | — |\n"
"| export | RECOG | by RID: NUMGEN-DEF-N5AS1-DEFECT, NUMGEN-RESULT-N5AS1-INF1, NUMGEN-THM-N5AS1-DEFECT-THRESHOLD-RATIO, NUMGEN-RESULT-L1-PRIMITIVE-CONTRACTION, NUMGEN-OPEN-N1C; GAP-LOCK Lemma 3 as cited in RECOG §7 | v1.20.8 (RECOG keeps v1.15 producer pins where load-bearing) | `recog-v0.3.24` | IF14 |\n"
"| received | RECOG | A1a/A1b explicit-domain theorems: consumer-side confirmations (acceptance matrix above) | v0.3.24 | `recog-v0.3.24` | IF27 |\n"
"| export | OFN | NG-7A additive operator and representation results (OFN §11 inspected NUMGEN v1.20.7 §6.8) | as declared in OFN §11 | `ofn-v0.10` | IF24 |\n"
"| reference | RRF | cites §6.6 M2-1/Census-1, §6.4 N-3A, §6.8 NG-7A | v1.20.7 | `rrf-v0.8.4` | — |")

EVID_CLAUSE = (
"**Evidence states and availability.** Rows keyed `[in-ledger]` are complete written proofs in this DSN with no separate "
"certificate (Methodology §12.1; `EV-SRC-READ`), not a lower grade. The files held by the Number Genesis co-owner "
"session were uploaded unchanged on the branch `upload/numgen-records` (PR #69), at the paths `upload/numgen-records/<file>` "
"listed in that branch's `SHA256SUMS.txt` (hash check `records/numgen/NUMGEN_UPLOAD_HASH_CHECK_20261026.md`). A cited file "
"among them is reachable at the release commit only if that branch is merged before the release; the release record states "
"which is the case. A file cited below that is not among them, or not reachable at the release commit, is not in the "
"repository, and its cited state is `EV-SRC-REPORTED`. No certificate was rerun for this edition (`EV-NOT-RERUN`).\n")

STAGE1_CHG = (
"### v1.21 — stage 1 intermediate (build stage, not adopted)\n\n"
"Corrections of the v1.20.8 advisory (owner dispositions of 26 Oct 2026; reconciliation `records/numgen/NUMGEN_OWNER_DISPOSITION_RECONCILIATION_v1_20_8.md`), "
"built by `evidence/numgen/scripts/build_numgen_v1_21_stage1.py` from `numgen-v1.20.8`. "
"Dyadic row-A theorem imported at §6.6 (the explicit-constant OPEN sub-item is closed by the import; NUMGEN's L-PHASE unchanged); "
"RECOG v0.3.24 explicit-domain theorems recorded as consumer-side confirmations with an acceptance matrix (§9.1; nothing imported); "
"domain labels (§6.2); RIDs NUMGEN-RESULT-N5AS1-GAPLOCK-ALPHABET, -GAPLOCK-COUNT, -GAPLOCK-SLIP-RATIO, -INF2 and "
"NUMGEN-RESULT-N3CP-CYCLIC-AVERAGE registered; pins Programme v1.3, Genesis v2.9, §7 Q403 v6.4.18; consumers-and-pins block; "
"evidence-state clause; owner alias DYAD-ALG-P5-RADIAL; scope words at N-1A0/N-1A1; C7C-M4 hold pointer. No grade, proof or "
"domain of an existing statement changes.\n\n")

# (key, group, row, mode, old, fn-or-new)
EDITS = [
# ---------------- NA02
("E01", "NA02", "§6.6 L-PHASE OPEN sub-item -> imported Dyadic row-A theorem + live [NUM] range (NB-11)", "line",
 "`[OPEN]` `[target: THM]` `[v1.20.8]` **L-PHASE explicit constant — Dyadic row-A theorem adopted upstream; NUMGEN import deferred.**",
 lambda line: ROWA_BLOCK),
("E02", "NA02", "§9.1 import row for DYAD-THM-LPHASE-ROWA-REMAINDER", "line",
 "| `q=4,(0,3)` all-`p` cascade closure |",
 after_row("| L-PHASE row-A remainder and branch (explicit domain) | `[import: RTG_DYADIC_OSCILLATOR_DSN_v6.4.22 §6.14 (producer edition v6.4.19) | DYAD-THM-LPHASE-ROWA-REMAINDER]` | §6.6 explicit L-PHASE constant on `U_D,base`; branch clause on `U_D,tube` | statement read at `dyad-v6.4.22`, unchanged since v6.4.19 (`EV-SRC-READ`); certificate replayed byte-identically by NUMGEN at receipt, not rerun (`EV-NOT-RERUN`); received (N15), statement accepted (owner dispositions, 26 Oct 2026), adopted use (this row) |")),
("E03", "NA02", "§9.1 N15 disposition row: states", "line",
 "| N15 — `DYAD-THM-LPHASE-ROWA-REMAINDER` |",
 lambda line: "| N15 — `DYAD-THM-LPHASE-ROWA-REMAINDER` | Dyadic (v6.4.19, `40c9e63f…6ec9`) | RECEIVED; statement accepted (owner dispositions, 26 Oct 2026); adopted use: §6.6 import and §9.1 import row, at `dyad-v6.4.22` §6.14 |"),
# ---------------- NA03
("E04", "NA03", "§6.2 domain alias table after the tube definition", "str",
 "and L1's strict `F`-contraction holds at every point of the tube, not only on the base phase.\n",
 "and L1's strict `F`-contraction holds at every point of the tube, not only on the base phase.\n\n" + ALIAS_BLOCK + "\n"),
("E05", "NA03", "explicit-domain block (§6.6): labels U_D,base / U_D,tube", "line",
 "`[RESULT] [from: THM] [import: RTG_DYADIC_OSCILLATOR_DSN_v6.4.18 §6.14 | DYAD-THM-PRIM-CTR]` **Explicit-domain boundary CLOSED (v1.20).**",
 lambda line: rep("with `U = {0 < Q <= 1/625}` and `U_T = U_{j<6} T^j(U)`.", "with `U_D,base = {0 < Q <= 1/625}` and `U_D,tube = U_{j<6} T^j(U_D,base)` (§6.2 domain labels).")(
     rep("so it lies in `U`;", "so it lies in `U_D,base`;")(
     rep("with the owner's enclosure `U_T ⊂ {Q < 2209/10^6}`", "with the owner's enclosure `U_D,tube ⊂ {Q < 2209/10^6}`")(line)))),
("E06", "NA03", "§9.1 PRIM-CTR row: label of the seed domain", "line",
 "| explicit primitive contraction / six-phase invariant tube |",
 rep("canonical seed in `U` |", "canonical seed in `U_D,base` |")),
# ---------------- NA01
("E07", "NA01", "§6.6 L-BACKBONE: explicit-domain counterpart pointer", "str",
 "sum_(m<M) q_m = log M + C_Q + o(1).\n```\n",
 "sum_(m<M) q_m = log M + C_Q + o(1).\n```\n\n" + PTR_LBACK + "\n"),
("E08", "NA01", "§6.6 L-MONO: explicit-domain counterpart pointer", "line",
 "`[RESULT] [from: ALG]` [RID: NUMGEN-RESULT-N5AS1-L-MONO] **L-MONO CLOSED",
 None),  # placeholder replaced below (pointer goes after the paragraph that ends the L-MONO block)
("E09", "NA01", "§6.6 INF-1: explicit-domain counterpart pointer", "str",
 "D_M = tau log M + C_D + o(1) -> infinity.\n```\n",
 "D_M = tau log M + C_D + o(1) -> infinity.\n```\n\n" + PTR_INF1 + "\n"),
("E10", "NA01", "§6.6 GAP-LOCK/INF-2: explicit-domain counterpart pointer after the SG-NG-23 guard", "line",
 "`[GUARD]` SG-NG-23 remains unchanged: N-5A closure and the physical 7-gap count law",
 after(PTR_GAPLOCK)),
("E11", "NA01", "§9.1 acceptance matrix and inbox-item disposition row (before §9.2)", "str",
 "\n### §9.2 Artifact Registry\n",
 "\n" + MATRIX + "\n\n" + CONSUMERS + "\n\n### §9.2 Artifact Registry\n"),
("E12", "NA01", "§9.1 dispositions: RECOG v0.3.24 notice row", "line",
 "| FMS v0.6.4 R8 provenance label |",
 after_row("| A1a/A1b explicit-domain theorems (`RECOG-THM-A1A-PHASE-EXISTENCE-U`, `RECOG-THM-A1B-SLIP-SCHEDULE-U`) | RECOG (v0.3.24; `pipes/NUMGEN/20261026-RECOG-a1b-slip-schedule-informed.md`) | statement accepted as independent agreement (acceptance matrix below); not imported; custody of GAP-LOCK 1–3 and INF-1 unchanged |")),
# ---------------- NB07 / NB08
("E13", "NB07", "RID: GAP-LOCK Lemma 1", "line",
 "`[RESULT] [from: ALG]` **GAP-LOCK Lemma 1 CLOSED — local return alphabet `{6,7}`.**",
 rep("`[RESULT] [from: ALG]` **GAP-LOCK Lemma 1", "`[RESULT] [from: ALG]` [RID: NUMGEN-RESULT-N5AS1-GAPLOCK-ALPHABET] **GAP-LOCK Lemma 1")),
("E14", "NB07", "RID: GAP-LOCK Lemma 2", "line",
 "`[RESULT] [from: ALG]` **GAP-LOCK Lemma 2 CLOSED — physical bookkeeping.**",
 rep("`[RESULT] [from: ALG]` **GAP-LOCK Lemma 2", "`[RESULT] [from: ALG]` [RID: NUMGEN-RESULT-N5AS1-GAPLOCK-COUNT] **GAP-LOCK Lemma 2")),
("E15", "NB07", "RID: GAP-LOCK Lemma 3", "line",
 "`[RESULT] [from: ALG]` **GAP-LOCK Lemma 3 CLOSED — event-time physical-slip locking.**",
 rep("`[RESULT] [from: ALG]` **GAP-LOCK Lemma 3", "`[RESULT] [from: ALG]` [RID: NUMGEN-RESULT-N5AS1-GAPLOCK-SLIP-RATIO] **GAP-LOCK Lemma 3")),
("E16", "NB07", "RID: INF-2", "line",
 "`[RESULT] [from: ALG]` **INF-2 / crossing count.**",
 rep("`[RESULT] [from: ALG]` **INF-2", "`[RESULT] [from: ALG]` [RID: NUMGEN-RESULT-N5AS1-INF2] **INF-2")),
("E17", "NB07", "RID: first-nonlinear cyclic-average theorem", "line",
 "`[RESULT][from: ALG]` **First-nonlinear cyclic-average theorem.**",
 rep("`[RESULT][from: ALG]` **First-nonlinear", "`[RESULT][from: ALG]` [RID: NUMGEN-RESULT-N3CP-CYCLIC-AVERAGE] **First-nonlinear")),
("E18", "NB08", "§6.6 identifier-scope guard: result RIDs under the module RID; category word is not a grade", "line",
 "`[GUARD]` `[v1.20.8]` **Identifier scope.**",
 app("The module record points to the result RIDs of its closed statements: NUMGEN-RESULT-N5AS1-INF1, NUMGEN-RESULT-N5AS1-INF2, "
     "NUMGEN-RESULT-N5AS1-GAPLOCK-ALPHABET, NUMGEN-RESULT-N5AS1-GAPLOCK-COUNT, NUMGEN-RESULT-N5AS1-GAPLOCK-SLIP-RATIO. "
     "The category word in an identifier is not a grade (Methodology v1.4 §4.2): NUMGEN-THM-N5AS1-DEFECT-THRESHOLD-RATIO "
     "is graded RESULT-from-ALG as tagged at its statement, and module RIDs of the form `NUMGEN-OPEN-*` stay lifecycle records of closed modules.")),
# ---------------- NA04 / NC19
("E19", "NA04", "§1.1 firewall import: Programme v1.3 SG-PROG-1", "line",
 "`[RESULT]` `[from: DEF]` `[import: RTG_DISCRETE_GENESIS_DSN_v2.12.13 SG-10; RTG_DYADIC_OSCILLATOR_DSN_v6.4.18 SG-14; RTG_PROGRAMME_OVERVIEW_v1.2 SG-PROG-1 | RID unavailable]`",
 rep("RTG_PROGRAMME_OVERVIEW_v1.2 SG-PROG-1", "RTG_PROGRAMME_OVERVIEW_v1.3 SG-PROG-1")),
("E20", "NA04", "§1.1 generator-selection guard: Programme v1.3 SG-PROG-2", "line",
 "`[GUARD]` **Programme generator-selection ceiling.** `[import: RTG_PROGRAMME_OVERVIEW_v1.2 SG-PROG-2 | RTG-OPEN-GENERATOR-SELECTION]`",
 rep("RTG_PROGRAMME_OVERVIEW_v1.2 SG-PROG-2", "RTG_PROGRAMME_OVERVIEW_v1.3 SG-PROG-2")),
("E21", "NA04", "§9.1 Programme row: v1.3", "line",
 "| programme generator-selection ceiling |",
 lambda line: "| programme generator-selection ceiling | `[import: RTG_PROGRAMME_OVERVIEW_v1.3 SG-PROG-2 | RTG-OPEN-GENERATOR-SELECTION]` | scope of all continuous-`T` Number Genesis results | read at `programme-v1.3` (SG-PROG-1–4 restated there as clarifications; this use unchanged); no status promotion |"),
("E22", "NA04", "§9.1 column label", "line",
 "| Imported object | Current pointer target | Use in this DSN | Validation state carried into v1.19 |",
 lambda line: "| Imported object | Current pointer target | Use in this DSN | Validation state at the pin |"),
("E23", "NA04", "§6.9a NG-10 source: Genesis v2.9", "line",
 "`[RESULT]` `[from: NUM]` `[scope: reduced birth-race model]` `[source: RTG_GENESIS_GEOMETRY_DSN_v2.8.9 §6.6; RID: GEN-ART-SATURATION]`",
 rep("RTG_GENESIS_GEOMETRY_DSN_v2.8.9 §6.6", "RTG_GENESIS_GEOMETRY_DSN_v2.9 §6.6")),
("E24", "NA04", "§9.1 Genesis row: v2.9", "line",
 "| Genesis reduced-sector saturation ceiling |",
 lambda line: "| Genesis reduced-sector saturation ceiling | `RTG_GENESIS_GEOMETRY_DSN_v2.9 §6.6`, RID `GEN-ART-SATURATION` | NG-10 only | read at `gen-v2.9` (§6.6 and the §8 artifact row): `Q_d* approx 1.13e-2`, reduced birth-race scope retained |"),
("E25", "NA04", "§7 N-3 item 7: Q403 pin aligned with the live imports (v6.4.18)", "line",
 "7. `[CLOSED by import]` the specific `q=4,(0,3)` nonlinear cascade item is closed by Dyadic v6.4.10 `DYAD-THM-Q403-PHASELAW`",
 rep("closed by Dyadic v6.4.10 `DYAD-THM-Q403-PHASELAW`", "closed by Dyadic v6.4.18 `DYAD-THM-Q403-PHASELAW` (§9.1)")),
("E26", "NA04", "§8 DZT provenance restated (no DZT v0.17 in the repository)", "line",
 "`[PROVENANCE]` The programme-review audit reports DZT v0.17 as a frozen closure state",
 lambda line: "`[PROVENANCE]` The programme-review audit `RTG_NG_PROGRAMME_REVIEW_AUDIT_v1.md` reports a DZT edition it calls \"v0.17\" as a frozen closure state containing all-`p` odd-support and denominator theorems and numerically reproduces them with `ng_review_dzt_independent_audit_v1.py`. No DZT document of that number is in the repository; the governing DZT edition is `dzt-v0.8` (`RTG_DYADIC_ARITHMETIC_RESONANCE_TRANSFORM_DSN.md`). Number Genesis imports nothing from DZT and uses the audit memo as no owner source."),
("E27", "NA04", "§9.2 abbreviated hash written as prefix…last four", "str",
 "(`cefb7180…b165b`)", "(`cefb7180…165b`)"),
# ---------------- NA05
("E28", "NA05", "N-1 tree: scope words", "str",
 "-> N-1C  operational history quotient / free-history test  [CLOSED local dyad by L1]",
 "-> N-1C  operational history quotient / free-history test  [CLOSED on U_NG,tube by L1; abstract N-1A0/N-1A1 open]"),
("E29", "NA05", "N-1A0 status: scope words", "str",
 "**RID:** `NUMGEN-OPEN-N1A0`  \n**Status:** ACTIVE  \n",
 "**RID:** `NUMGEN-OPEN-N1A0`  \n**Status:** ACTIVE (abstract question; the local primitive-dyad instance is closed on `U_NG,tube` by N-1 / L1)  \n"),
("E30", "NA05", "N-1A1 status: scope words", "str",
 "**Status:** PARTIAL — closed for N-1A-MIN; general boundary-aware form continues in N-1A2  \n",
 "**Status:** PARTIAL — closed for N-1A-MIN and, locally, on `U_NG,tube` by N-1 / L1; the general boundary-aware form continues in N-1A2  \n"),
# ---------------- NB09
("E31", "NB09", "§9.2 evidence-state and availability clause", "str",
 "### §9.2 Artifact Registry\n",
 "### §9.2 Artifact Registry\n\n" + EVID_CLAUSE),
("E32", "NB09", "§9.2 N5-C1–C4 in-ledger key", "line", "| `N5-C1–C4 in-ledger proofs (v1.15)` |",
 rep("`[RESULT][from: ALG]` — no separate external certificate yet", "`[RESULT][from: ALG]` — `[in-ledger]`")),
("E33", "NB09", "§9.2 C5 in-ledger key", "line", "| `C5-SYN-13 in-ledger control (v1.15)` |",
 rep("`[RESULT][from: ALG]` — not an RTG physical realization", "`[RESULT][from: ALG]` — `[in-ledger]`; not an RTG physical realization")),
("E34", "NB09", "§9.2 N5-PHYS-1 in-ledger key", "line", "| `N5-PHYS-1 in-ledger proof (v1.15)` |",
 rep("`[RESULT][from: ALG]` — local continuous-dyad physical witness", "`[RESULT][from: ALG]` — `[in-ledger]`; local continuous-dyad physical witness")),
("E35", "NB09", "§9.2 C7A in-ledger key", "line", "| `N5-C7A in-ledger theorem (v1.15; notation corrected at v1.16)` |",
 rep("| `[RESULT][from: ALG]` |", "| `[RESULT][from: ALG]` — `[in-ledger]` |")),
("E36", "NB09", "§9.2 P3 in-ledger key", "line", "| `N-2-ORD P3 in-ledger refinement (v1.19)` |",
 rep("`[RESULT][from: ALG]` — no explicit maximal-radius/seed-inclusion certificate", "`[RESULT][from: ALG]` — `[in-ledger]`; no explicit maximal-radius/seed-inclusion certificate")),
("E37", "NB09", "§9.2 NG-7A extension in-ledger key", "line", "| `NG-7A abelian fundamental-cycle extension (v1.19)` |",
 rep("`[RESULT][from: ALG]` — in-ledger extension; no new physical-source claim", "`[RESULT][from: ALG]` — `[in-ledger]`; no new physical-source claim")),
# ---------------- NC12
("E38", "NC12", "SG-NG-23: cross-reading of exp(pi/(3 tau))", "line",
 "**[SG-NG-23] Non-relabeling ≠ nontrivial commensurability.**",
 app("The number `exp(pi/(3 tau)) = exp(sqrt(3) pi/6)` appears with three scopes: here a representation-level diagnostic (SG-NG-19); "
     "in RECOG a clock ratio under RECOG's own SG-R10; and in `RECOG-THM-A1B-SLIP-SCHEDULE-U` (`recog-v0.3.24`) a THM consequence on "
     "`U_R,base`. They are not identified beyond their stated scopes.")),
# ---------------- NC13
("E39", "NC13", "L1: owner alias of Delta Q_5 (gate A1)", "str",
 "Delta Q_5 = Q_true*(5 eta^3 - 43 eta^2 rho\n                    + 4 eta rho^2 - 5 rho^3)/24.\n```\n",
 "Delta Q_5 = Q_true*(5 eta^3 - 43 eta^2 rho\n                    + 4 eta rho^2 - 5 rho^3)/24.\n```\n\n"
 "*Owner alias:* `Delta Q_5` is the polynomial `P_5` of `DYAD-ALG-P5-RADIAL` (`dyad-v6.4.22` §6.14), the identity used inside "
 "DYAD-THM-PRIM-CTR. Exact equality, together with `Delta Q_4 = -Q_true^2` and vanishing degrees 1–3, is recomputed from "
 "`T` in `" + CHECK_SCRIPT + "` gate A1 (exact rational arithmetic; negative control fails). The L1 constants of this "
 "section are NUMGEN's; no Dyadic ceiling replaces them.\n"),
("E40", "NC13", "§9.2 relay row: Dyadic owner RIDs", "line",
 "| `NG_TO_DYAD_RELAY_RIEMANN_LENS_v1.md` |",
 rep("`[RESULT][from: ALG]` relay — not claimed in NG", "`[RESULT][from: ALG]` relay — not claimed in NG; owner records `DYAD-ALG-Q-INVARIANT-FORM`, `DYAD-ALG-TAU-DETB`, `DYAD-ALG-CUBIC-PARABOLIC` (`dyad-v6.4.22` §6.3)")),
# ---------------- NC14
("E41", "NC14", "NG-0R-COV pin: comparison conventions for phi* vs C_D^ext", "line",
 "`[DEF]` **Declared primary transformation (pre-registration pin).**",
 app("Available comparison (not an identification): `RECOG-THM-A1A-CD-IDENTIFICATION` (`recog-v0.3.24` §6.13b) gives "
     "`C_D^ext(x_0) = tau log Q_0 - M_W(x_0)` on `U_R,base`, so `Q_0 -> lambda Q_0` at fixed phase shifts `C_D^ext` by "
     "`tau ln lambda + O(sqrt(Q_0))`. Whether `phi*` equals `C_D^ext` stays OPEN (`NUMGEN-OPEN-NG0R-COV`) until chart, lift, "
     "readout, clock, start state and overlap (`U_R,base ∩ U_NG`) are matched; RECOG's infinite-record readout (A1c) "
     "recovers neither the start amplitude nor any change to its memory classification.")),
# ---------------- NC16
("E42", "NC16", "§9.2 RECOG consumer rows (v0.3.5; v0.3.22) -> one current row, RECOG v0.3.24, both facts", "lines2",
 ("| known consumer: `RECOG v0.3.5` / `RECOG-ALG-LATTICE-CLOCK` |", "| known consumer (v1.20.8): `RECOG v0.3.22`"),
 "| known consumer: `RECOG v0.3.24` (`recog-v0.3.24`, `8c64bea2…69e7c1`) | imports by RID `NUMGEN-THM-N5AS1-DEFECT-THRESHOLD-RATIO`, `NUMGEN-DEF-N5AS1-DEFECT`, `NUMGEN-RESULT-N5AS1-INF1`, `NUMGEN-RESULT-L1-PRIMITIVE-CONTRACTION`, `NUMGEN-OPEN-N1C` (RECOG §7); GAP-LOCK Lemma 3 is tagged `[HEUR cross-reference]` in RECOG §7 and is used inside the ALG identity `RECOG-RESULT-BTOKEN-LOG-EQUIVALENCE`; RECOG's explicit-domain route is `RECOG-THM-A1B-SLIP-SCHEDULE-U`. Number Genesis asserts no grade for RECOG's use (finding filed: `pipes/RECOG/20261026-NUMGEN-gap-lock-3-grade-of-import.md`) | `[PROVENANCE]` consumer record, not a theorem change |"),
# ---------------- I06
("E44", "I06", "§2 item 1: C7C-M4 hold — TDR-G request pointer and sensitivity audit", "line",
 "1. **C7C-M — interface-typed WD-DOM / partial-composition closure (next active target).**",
 app("**TDR-G dependency:** the request for TDR-G's orientation-policy disposition at `S=0`, `|E|=N/2` is filed as "
     "`pipes/TDRG/20261026-NUMGEN-orientation-policy-s0-e-half-n.md` (`blocks: C7C-M4`); before any status change, the 40 "
     "convention-exposed DISC-2 witnesses (§6.6 P2 audit) receive a sensitivity audit under the policy TDR-G adopts. The abstract "
     "WD-DOM design continues meanwhile.")),
# ---------------- I11
("E45", "I11", "§6.8 Foundations export: OFN v0.10 consumer pointer and additive-rank scope", "line",
 "`[RESULT] [from: ALG]` **Foundations export.** T1–T7 discharge the operator half",
 app("The current OFN edition (`ofn-v0.10`, §11; Programme IF24) records the additive result and the fundamental-integral-cycle "
     "extension from NUMGEN v1.20.7 §6.8; OFN's acceptance is OFN's. `r_hol` is the additive multichannel rank only: it is not a "
     "non-Abelian holonomy invariant and not a curvature; NG-7A closed does not close NG-7B.")),
]

def lmono_after(t):
    """E08: pointer after the L-MONO paragraph (the line ending 'retires the gate-1 orientation caveat.')"""
    anchor = "This also retires the gate-1 orientation caveat.\n"
    assert t.count(anchor) == 1
    return anchor, anchor + "\n" + PTR_LMONO + "\n"

def apply_edit(live, k, mode, old, fn):
    if mode == "lines2":
        lines = live.split("\n")
        hits = [i for i, l in enumerate(lines) if l.startswith(old[0])]
        assert len(hits) == 1 and lines[hits[0] + 1].startswith(old[1]), f"{k}: lines2 anchor"
        assert sum(1 for l in lines if l.startswith(old[1])) == 1, f"{k}: second prefix not unique"
        o = lines[hits[0]] + "\n" + lines[hits[0] + 1]
        assert live.count(o) == 1
        return live.replace(o, fn), o, fn
    if mode == "str":
        assert live.count(old) == 1, f"{k}: str anchor count {live.count(old)}"
        new = fn
        assert old != new, f"{k}: no-op"
        return live.replace(old, new), old, new
    lines = live.split("\n")
    hits = [i for i, l in enumerate(lines) if l.startswith(old)]
    assert len(hits) == 1, f"{k}: line prefix hits {len(hits)}"
    i = hits[0]
    o = lines[i]
    n = fn(o)
    assert n != o, f"{k}: no-op"
    lines[i] = n
    return "\n".join(lines), o, n

def build(base_text):
    assert hashlib.sha256(base_text.encode()).hexdigest() == BASE_SHA, f"base is not adopted v1.20.8 ({BASE_TAG})"
    keys = [e[0] for e in EDITS]
    assert len(keys) == len(set(keys)), "duplicate edit keys"
    i = base_text.index(CHG_START)
    live, chg = base_text[:i], base_text[i:]
    record = []
    for k, grp, row, mode, old, fn in EDITS:
        if k == "E08":
            a, b = lmono_after(live)
            live = live.replace(a, b)
            o, n, m = a, b, "str"
        else:
            m = mode
            live, o, n = apply_edit(live, k, mode, old, fn)
        record.append({"key": k, "group": grp, "row": row, "mode": m, "old_sha256": hashlib.sha256(o.encode()).hexdigest(),
                       "new_sha256": hashlib.sha256(n.encode()).hexdigest(), "old": o, "new": n})
    assert chg.count(CHG_START) == 1
    chg = chg.replace(CHG_START, CHG_START + STAGE1_CHG)
    record.append({"key": "CHG", "group": "CHG", "row": "stage-1 changelog entry", "mode": "chg-insert",
                   "old_sha256": hashlib.sha256(CHG_START.encode()).hexdigest(),
                   "new_sha256": hashlib.sha256((CHG_START + STAGE1_CHG).encode()).hexdigest(),
                   "old": CHG_START, "new": CHG_START + STAGE1_CHG})
    return live + chg, record

def main(argv):
    base, out, log = argv[1:4]
    text, record = build(open(base, "rb").read().decode("utf-8"))
    data = text.encode("utf-8")
    open(out, "wb").write(data)
    json.dump({"base_sha256": BASE_SHA, "base_tag": BASE_TAG, "intermediate_sha256": hashlib.sha256(data).hexdigest(),
               "round": 2, "round1_intermediate_sha256": ROUND1_SHA,
               "declared_new_numgen_rids": NEW_RIDS, "evidence_script": CHECK_SCRIPT,
               "edit_count": len(record), "edits": record},
              open(log, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(hashlib.sha256(data).hexdigest(), len(record), "edits")

if __name__ == "__main__":
    main(sys.argv)
