#!/usr/bin/env python3
r"""Triadic v1.7 — stage-1 build (content and scope corrections; no layout migration).

Input: the adopted v1.6.1 file (tag triad-v1.6.1, SHA-256 95340abe...451f).
Fixed by: the two co-owner disposition records (PR #138 Claude, PR #137 ChatGPT), their joint reconciliation
records/triad/TRIAD_OWNER_DISPOSITION_RECONCILIATION_v1_6_1.md (PR #139; ChatGPT confirmed in review 5714190994,
30 Oct 2026) and the PI's stage-1 start of 30 Oct 2026 ("Stage 1'i hazırlayalım"). Rows are the 29 rows of
records/triad/ATLAS_ADVISORY_TRIAD_v1_6_1_RECONCILIATION.md §4.

Stage 1 carries rows 1-5, 7-11, 13-15, the content part of row 21 (classification of the negative records), the
custody statements of the entry note §0(a) and the row-24 record locations. Row 6 and row 16 need no edit; row 12 is
after the tag. Stage 2 (rows 17-23; row 29 deferred) is layout only and is built separately against the frozen
stage-1 hash. The header lines that would otherwise be false for a v1.7 draft (title, date, status, supersedes, base,
co-owners, records, evidence location, change boundary) are corrected here; their v1.4 layout is stage 2.

Edit modes:
  str   : `old` occurs exactly once in the whole document; replaced by `new`;
  live  : `old` occurs exactly `count` times in the live region (before Appendix A); all are replaced;
  after : `new` is inserted immediately after the unique anchor `old` (anchor kept).
Every edit is logged with old/new text and SHA-256. The token <BR> in an edit text stands for the two-space Markdown
line break at end of line.

usage: build_triad_v1_7_stage1.py BASE OUT EDITLOG_JSON
  BASE = `git show triad-v1.6.1:dsn/RTG_TRIADIC_BIRTH_LIFT_DSN.md`
"""
import hashlib, json, sys

BASE_SHA = "95340abe57e999ed48681502152113d8fdb3102f74f45a25aa66c2d0092d451f"
LIVE_END = "## Appendix A — Version History"
BR = "<BR>"

def sha(t): return hashlib.sha256(t.encode("utf-8")).hexdigest()
def br(t): return None if t is None else t.replace(BR, "  ")

E = []  # (id, row, mode, old, new, count)
def ed(i, row, old, new, mode="str", count=1): E.append((i, row, mode, br(old), br(new), count))

# =============================================================================================== header (truth of the draft)
ed("H01", "hdr", "# RTG_TRIADIC_BIRTH_LIFT_DSN_v1.6.1\n", "# RTG_TRIADIC_BIRTH_LIFT_DSN_v1.7\n")
ed("H02", "hdr",
   "**Date:** 19 October 2026 (v1.6.1 owner release; DRAFT r2 19 October, DRAFT r1 18 October 2026); v1.6 adopted 5 October 2026<BR>\n",
   "**Date:** 30 October 2026 (v1.7 stage-1 intermediate); v1.6.1 adopted 19 October 2026<BR>\n")
ed("H03", "hdr",
   "**Document status:** ADOPTED — v1.6.1 owner release, 19 October 2026,",
   "**Document status:** DRAFT — stage-1 intermediate of v1.7 (content and scope corrections; the layout migration is stage 2); adoption pending. `triad-v1.6.1` remains the governing edition until adoption and tag. Consumer acceptance is not implied.<BR>\n**Status of the governing edition (history):** ADOPTED — v1.6.1 owner release, 19 October 2026,")
ed("H04", "hdr",
   "**Supersedes:** `RTG_TRIADIC_BIRTH_LIFT_DSN_v1_6.md` (SHA-256 `c768687cec6d52ffd358dc362cee4348f076160943564adaa461e6c7c4595b36`), whose exact bytes remain preserved. v1.6 superseded `RTG_TRIADIC_BIRTH_LIFT_DSN_v1_5.md` as the designated Triadic owner. Its exact bytes remain preserved as historical evidence.<BR>\n",
   "**Supersedes:** `RTG_TRIADIC_BIRTH_LIFT_DSN_v1.6.1` (tag `triad-v1.6.1`, SHA-256 `95340abe57e999ed48681502152113d8fdb3102f74f45a25aa66c2d0092d451f`), on adoption. v1.6.1 superseded v1.6 (SHA-256 `c768687cec6d52ffd358dc362cee4348f076160943564adaa461e6c7c4595b36`); the v1.5 and v1.6 files are not in the repository.<BR>\n")
ed("H06", "hdr",
   "**DSN Methodology:** Adopted `DSN_METHODOLOGY_v1_3.md`, bounded migration: revised blocks use its grammar and claim lifecycle; unchanged v1.2-era blocks retain their former forms and grades. Full-document migration is not asserted.<BR>\n",
   "**DSN Methodology:** v1.4 (tag `methodology-v1.4`). Stage 1 applies its tag grammar to the revised blocks (compound tags unpacked, release labels removed from live qualifiers, §8.4); the layout migration (header form, Appendix A/B, single footer, heading grades) is stage 2. Unrevised blocks keep their former forms until then.<BR>\n")
ed("H07", "hdr",
   "**Release base (v1.6.1):** co-owner-accepted DRAFT r2,",
   "**Base (v1.7):** `triad-v1.6.1` (SHA-256 `95340abe57e999ed48681502152113d8fdb3102f74f45a25aa66c2d0092d451f`); stage-1 edits by `evidence/triad/scripts/build_triad_v1_7_stage1.py` (edit log `evidence/triad/v1.7/stage1_edit_log.json`), fixed by the confirmed co-owner reconciliation `records/triad/TRIAD_OWNER_DISPOSITION_RECONCILIATION_v1_6_1.md` and the PI's stage-1 start of 30 Oct 2026.<BR>\n**Release base (v1.6.1, history):** co-owner-accepted DRAFT r2,")
ed("H08", "hdr",
   "**Co-owners (v1.6.1):** Claude and ChatGPT (PI designation, 18 Oct 2026); v1.6.1 prepared by Claude,",
   "**Co-owners:** Claude and ChatGPT (PI designation, 18 Oct 2026). v1.7 stage 1 prepared by Claude; change-focused review by ChatGPT. **History — v1.6.1:** prepared by Claude,")
ed("H09", "hdr/24",
   "**Adoption record (v1.6.1):** `records/OWNER_ADOPTION_v1_6_1.json`; release record `records/RELEASE_RECORD_v1_6_1.md`. **History — v1.6 adoption record:** `records/OWNER_ADOPTION.json`; human-readable release record: `records/RELEASE_RECORD.md`. Consumer acceptance is not implied.<BR>\n",
   "**Adoption records:** v1.6.1 — `records/triad/OWNER_ADOPTION_v1_6_1.json` (SHA-256 `33bcd3cea83b467d0bc4d8cc4a37c10771cd81151831caec87c55873937cd5dd`) and `records/triad/RELEASE_RECORD_v1_6_1.md` (SHA-256 `aa3d8d773a2083908f2e576bc59f9c6d3c110c1caadbc70782c72b07e95eb45d`), placed byte-unchanged from `upload/triad-records`. v1.6 — `records/OWNER_ADOPTION.json`, `records/RELEASE_RECORD.md` and `records/METADATA_EDITS.json`, cited by name as history; they are not in the repository. v1.7 — `records/triad/TRIAD_v1_7_RELEASE_RECORD.md`, written at adoption. Consumer acceptance is not implied.<BR>\n")
ed("H10", "hdr/§0(a)",
   "**Evidence location:** the complete accepted package is preserved under `evidence/accepted_r4_2/`; inherited relative script/input/evidence paths in §8 are resolved from that package root unless another archive is explicitly named. Historical package statuses retain their original dates and are not the current owner-selection record.<BR>\n",
   "**Evidence location:** the v1.6 accepted evidence package `evidence/accepted_r4_2/` is held by the PI and is **not in the repository**. Relative script, input and evidence paths in §8 refer to that package root unless a repository path is given; the hashes printed there remain the identities. What the repository holds and what is missing: `records/triad/TRIAD_SOURCE_RECOVERY_LIST.md` (intake check: `records/triad/TRIAD_UPLOAD_HASH_CHECK_20261030.md`). Historical package statuses keep their original dates and are not the current owner-selection record.<BR>\n")
ed("H11", "hdr/13",
   "**Preservation boundary (v1.6.1):** this release changes only release metadata",
   "**Change boundary (v1.7 stage 1):** content and scope corrections only, each logged in `evidence/triad/v1.7/stage1_edit_log.json` and mapped to its reconciliation row in `records/triad/TRIAD_v1_7_STAGE1_IMPLEMENTATION_MATRIX.md`. No RID is added, removed or renamed; no live claim's grade changes; no numerical campaign or physical selection is added. The identifier set is stated in §9; the v1.6 phrase \"all 49 RIDs\" below cannot be reproduced from the repository and is addressed in the release record.<BR>\n**Preservation boundary (v1.6.1, history):** this release changes only release metadata")

# =============================================================================================== aliases (row 14)
ed("A01", "14", "| `[ALG/NUM synthesis]` | `[ALG]` co-interpreted with `[NUM]` | combined algebraic/numerical synthesis result |\n", "")
ed("A02", "14",
   "`[DEF]` Revised imports/exports in this release use canonical forms from `DSN_METHODOLOGY_v1.3`. The table above documents retained v1.5 aliases, not a new proof-grade system; inherited mixed-tag blocks await their separate migration.",
   "`[DEF]` Revised blocks use the canonical forms of DSN Methodology v1.4 (§8.4). The table above declares the local aliases in use; it is not a new proof-grade system. A mixed `[ALG/NUM]` reading is unpacked into the exact assertion and its numerical corroboration. Section-heading grade suffixes are migrated in stage 2.")

# =============================================================================================== §1 (rows 1, 4, 7, 9)
ed("S01", "7",
   "the 96:1 comparison is not used as a current same-system dominance theorem (§6.1, SG-1).",
   "the 96:1 comparison is not used as a current same-system dominance theorem (§6.1, SG-1). The ratio is also not invariant under a metric or observable dictionary that has not been proved. For the same planar vectors $B_T=2B_G$ (§6.18); in a hypothetical common model with $\\Delta Q_G=a_GQ_G^2$ one would have $\\Delta Q_T=(a_G/2)Q_T^2$, and the same arithmetic would give 192 instead of 96. The example is not a new ratio: which metric each coefficient uses is itself part of the open correspondence. A common generator, clock, carrier and metric, representation arrow, projection and compared observable are required before the two coefficients can be compared. This paragraph is the single statement of the 96:1 status; SG-1, §§4–5, §6.1, §6.11, §6.18 and CN-05 point to it.")
ed("S02", "1",
   "For the corrected coefficient extension, $K=1$ is tangent and",
   "For the corrected coefficient extension, $K=1$ is tangent (for both root-equivalent off-root extensions of §6.18; the extension itself is fixed only by the T-6r contract) and")
ed("S03", "9",
   "Consumer notices CN-01–CN-05 require Genesis/OPEN-M scientific reconciliation against this adopted release; consumer acceptance remains pending.",
   "The consumer state of notices CN-01–CN-05 is recorded per recipient in §7.4; the receipts there are the receivers' records, not Triadic acceptance, and they close none of these OPEN items.")
ed("S04", "4",
   "No new numerical sweep is required for this r4 model-contract correction.",
   "No corrected-field trajectory campaign is treated as scientifically decisive before the T-6r acceptance contract (§2) is met.")

# =============================================================================================== §2 (rows 4, 5, 11)
ed("P01", "4",
   "1. **T-6r — Corrected orientation-model/domain completion.** Specify the admissible carrier for any $K<1$ independent-orientation diagnostic, the corrected $\\dot\\Omega$, finite-$u/r$ dynamics, event taxonomy and any new basin test before restoring sector/safety claims.",
   "1. **T-6r — Corrected orientation-model/domain completion.** Meet the acceptance contract C1–C6 in the T-6r record below before any sector, safety or basin claim is restored.")
ed("P02", "5",
   "2. **T-6q — Phase-convention and sign-sector table.** Complete sign-sector and branch-extension bookkeeping across the now-separated root and independent-orientation models.",
   "2. **T-6q — Phase-convention and sign-sector table.** The coordinate sign table is recorded in the T-6q record below; the typed action on the complete state of the chosen corrected model remains open.")
ed("P03", "11",
   "**Handoff queue** — owner release issued; consumer reconciliation pending:\n1. Send CN-01–CN-05 to Genesis/OPEN M; CN-05 withdraws obsolete sector/wedge/no-basin/obstruction imports rather than rescaling them.\n2. Send the typed planar convention proposal to RRF: $B_T^{\\rm plane}=2B_G$, $Q_T=2Q_G$, $I_T=2I_G$, $\\Omega_T=-\\sqrt3\\,\\omega_{\\rm raw}$ for identified planar vectors only. No birth/generator/apex bridge is implied.\n3. Programme/OFN pass two follows technical consumer reconciliation.\n",
   "**Consumer interface.** The per-recipient state of CN-01–CN-05 is in §7.4. Notices after a release are filed as items in the receivers' inboxes (`pipes/<STREAM>/`, CONVENTIONS §7); filing is a queue event, not acceptance.\n")

T6R_OLD = (
    "Current state: the normalization blocker is closed (§6.18). In the corrected coefficient extension $K=1$ is tangent, so the historical inward/outward sector map and no-basin programme are not current-model evidence. Two actual planar vectors satisfy the Gram identity and hence $K=1$ in the normalized convention; a physical or diagnostic $K<1$ carrier requires explicit enlargement/relaxation.<BR>\n"
    "Closure criterion: specify the carrier, corrected $\\dot\\Omega$, finite-$u/r$ vector field or exact map, event guards and model/observable transport. Only then decide whether a new basin/escape calculation is scientifically meaningful. No rescaling of historical trajectories is permitted.\n")
T6R_NEW = (
    "Current state: the normalization blocker is closed (§6.18). In the corrected coefficient extension $K=1$ is tangent, so the historical inward/outward sector map and no-basin programme are not current-model evidence. Two actual planar vectors satisfy the Gram identity and hence $K=1$ in the normalized convention; a physical or diagnostic $K<1$ carrier requires explicit enlargement/relaxation. The off-root extension of the §6.4 coefficients is not unique, and $f_s$, $f_c$ and the fate of $D=\\mathcal G/Q_s$ depend on it (§6.18).<BR>\n"
    "Acceptance contract (current; all six are required):\n"
    "- **C1 — carrier and metric.** The state carrier, its metric and the coefficient group of the carrier. (OFN v0.12 `RTG-OFN-ALG-REF-CLOSURE-COMPARISON`: for $K_3$ the global reference comparison $\\kappa_3$, with one closure relation as reference, is an isomorphism over $\\mathbb R^d$ but not over $U(1)$, $\\mathbb Z_N$ with $3\\mid N$, or $\\mathbb Z$; a carrier that uses the count \"three node-difference edges minus one closure relation\" must declare its group. The current Triadic planar carrier is real.)\n"
    "- **C2 — encoding and reduction.** The maps from the carrier to $(Q_s,Q_c,I_{sc},\\Omega,r)$ and back, with their representation.\n"
    "- **C3 — full evolution.** The full $(Q_s,Q_c,I_{sc},\\Omega,r)$ vector field or exact map, including how each coefficient extends off the root; this fixes $f_s$, $f_c$ and the fate of $D$.\n"
    "- **C4 — clock and phase convention.** Primitive or six-step clock, and the phase convention.\n"
    "- **C5 — events and regularity.** Event and contact predicates, event guards, and the regularity of the field.\n"
    "- **C6 — covariance.** Covariance under the declared complete-state action (T-6q).\n\n"
    "RRF and OFN model classes enter as interface constraints; they do not identify the carrier with the physical Triadic birth carrier.<BR>\n"
    "Closure criterion: C1–C6 supplied and checked. Only then decide whether a new basin/escape calculation is scientifically meaningful. No rescaling of historical trajectories is permitted.\n")
ed("P04", "4", T6R_OLD, T6R_NEW)

T6Q_OLD = (
    "Closure criterion: produce a typed sign/action table for the chosen corrected model, including the state carrier, $\\dot\\Omega$, boundary definition, and comparison observables. Do not reuse historical sector maps by reflection alone.\n")
T6Q_NEW = (
    "\n`[ALG]` `[scope: coordinate bookkeeping on an identified planar pair]` **Coordinate sign table.** With $Q_s=s^\\top Bs$, $Q_c=c^\\top Bc$, $I_{sc}=s^\\top Bc$ and $\\omega_{\\rm raw}=-\\Omega/\\sqrt3$:\n\n"
    "| Coordinate operation | $Q_s,Q_c$ | $I_{sc}$ | $\\Omega$ | $(\\mu,\\nu)$ | root branch label $\\sigma$ |\n"
    "|---|---|---|---|---|---|\n"
    "| $(s,c)\\mapsto(c,s)$ | exchanged | unchanged | negated | $(\\mu,-\\nu)$ | flips |\n"
    "| $(s,c)\\mapsto(-s,c)$ | unchanged | negated | negated | $(-\\mu,-\\nu)$ | flips |\n"
    "| $(s,c)\\mapsto(-s,-c)$ | unchanged | unchanged | unchanged | unchanged | unchanged |\n\n"
    "$K$ is invariant under each operation. This is coordinate bookkeeping, not a physical action: not a node-exchange gauge action, a dynamical symmetry, a carrier isomorphism or a branch continuation. A physical node or pole action must act on the complete state (roles and incidence, chart, clock, event variables) and intertwine with the selected dynamics. T-6n's naive-flip failure and its OPEN continuation are unchanged; no mirrored witness, safe sector or branch continuation follows from the table. Check: `evidence/triad/scripts/check_triad_v1_7_stage1.py` gate S5 (exact SymPy).\n\n"
    "Closure criterion: a typed action on the complete state of the chosen corrected model, intertwining with its dynamics, together with the state carrier, $\\dot\\Omega$, boundary definition and comparison observables. Do not reuse historical sector maps by reflection alone.\n")
ed("P05", "5", T6Q_OLD, T6Q_NEW)

# =============================================================================================== §4 (row 9)
ed("L01", "9",
   "| Consumers | Genesis / OPEN M / Programme / OFN / RRF | CN-01–CN-05 scientific reconciliation against adopted v1.6; consumer acceptance pending |",
   "| Consumers | Genesis / OPEN M / Programme / OFN / RRF | CN-01–CN-05; per-recipient state in §7.4 |")

# =============================================================================================== §6 (rows 1, 2, 3, 7, 9, 14, 15)
ed("C01", "15", "`[COR v1.6.1 — D3]`", "`[COR]`", "live", 3)
ed("C02", "15", "`[COR v1.6.1 r2 — D3-R1]`", "`[COR]`", "live", 3)
ed("N01", "7",
   "Until that map is supplied, the coefficient comparison is bookkeeping and the global-explosiveness inference from T-1 is simply withdrawn/not established.",
   "Until that map is supplied, the coefficient comparison is bookkeeping and the global-explosiveness inference from T-1 is simply withdrawn/not established. Status and metric caveat: §1.")
ed("Q01", "1/2",
   "with $\\Omega$ reclosed from the root relation at the state-evaluation step.",
   "with $\\Omega$ reclosed from the root relation at the state-evaluation step. Time is the continuous coefficient-ODE time measured in units of one six-step block; the ODE is not the exact discrete six-step map (§6.18).")
ed("T01", "3",
   "There is no real replacement for $x_*$ at this leading order.\n",
   "There is no real replacement for $x_*$ at this leading order.\n\n"
   "`[ALG]` `[scope: corrected leading orientation model; leading coefficient only]` **Coercive bound.** $A_\\theta^{\\rm corr}=(\\mu,\\nu)\\,M_\\theta\\,(\\mu,\\nu)^\\top$ with $M_\\theta=\\begin{pmatrix}3\\sqrt3&3\\\\3&9\\sqrt3\\end{pmatrix}$, whose eigenvalues are $6\\sqrt3\\pm6$. Hence\n"
   "$$6(\\sqrt3-1)K\\le A_\\theta^{\\rm corr}\\le6(\\sqrt3+1)K.$$\n"
   "Evidence: `evidence/triad/scripts/triad_coowner_row1_row3_check.py`, check C4 (exact SymPy; `EV-RUN`, preparer; output `evidence/triad/v1.7/triad_coowner_row1_row3_check_output.txt`). No sign persistence at finite $u$ or nonzero $r$, and no trajectory, basin or global statement, follows without a proved uniform remainder smaller than the lower margin $6(\\sqrt3-1)K$.\n",
   "str")
ed("X01", "2",
   "Any separate receiving-side cubic reconstruction retains its own scope and is not an unpinned evidence leg of this paragraph.\n",
   "Any separate receiving-side cubic reconstruction retains its own scope and is not an unpinned evidence leg of this paragraph.\n\n"
   "`[ALG]` **Type of the Gram relation.** The relation $2\\Omega\\Delta\\Omega=Q_c\\Delta Q_s+Q_s\\Delta Q_c-2I_{sc}\\Delta I_{sc}$ is the first-variation (degree-3) coefficient of the exact identity $\\Delta\\mathcal G\\equiv0$ that holds for actual planar pairs, where $\\mathcal G=Q_sQ_c-I_{sc}^2-\\Omega^2$ vanishes identically on two planar vectors. Bookkeeping: with $Q_s,Q_c,I_{sc},\\Omega$ of weight 1 and $r$ of weight $\\tfrac12$, every retained $r^j$ increment ($j=0,1,2$) of §6.4 is homogeneous of degree 2. The exact finite increment also contains $\\Delta Q_s\\Delta Q_c-(\\Delta I_{sc})^2-(\\Delta\\Omega)^2$ and $Q\\times$(next-order increments), both of degree 4, which the retained six-step expansion discards. The clock is the six-step return. The relation is a coefficient-level identity, not an exact discrete conservation law of the six-step map. Homogeneity check: `evidence/triad/scripts/triad_reconciliation_row1_extension_check.py` (`EV-RUN`, preparer; output `evidence/triad/v1.7/triad_reconciliation_row1_extension_check_output.txt`).\n",
   "str")
ed("X02", "1",
   "`[ALG]` **Corrected diagnostic consequences** (formal five-variable extension used by the downstream code, $Q_c$ independent, reduced coefficient formulas retained):",
   "`[ALG]` **Corrected diagnostic consequences** (formal five-variable extension of the kind used by the downstream code, $Q_c$ independent, reduced coefficient formulas retained; domain $Q_s>0$, $Q_c>0$; time is the continuous coefficient-ODE time in units of one six-step block, not the exact discrete six-step map):")
ed("X03", "1",
   "Hence $\\dot K=0$ on $K=1$, at all retained $r$-orders. The corrected field has no outward or inward $K=1$ sectors.\n",
   "Hence $\\dot K=0$ on $K=1$, at all retained $r$-orders. The corrected field has no outward or inward $K=1$ sectors. The off-root extension is not unique, and $f_s$, $f_c$ depend on it. Two root-equivalent extensions of the displayed coefficients: **(a) literal** — $\\Delta Q_c^{(1)}=Q_c\\,q_1$ with the independent $Q_c$ and $q_1=6(5\\sqrt{14}\\Omega-\\sqrt{42}I_{sc})/(7\\sqrt{Q_s})$; **(b) $Q_c$-free** — the same coefficient with $Q_c$ replaced by $\\widehat Q_c=(I_{sc}^2+\\Omega^2)/Q_s$. They coincide on the root; all other displayed coefficients and $\\Delta\\Omega$ are $Q_c$-free. In (b), $f_s=\\dot Q_s$ and $f_c=\\dot Q_c$; in (a), $f_s=\\dot Q_s+rQ_sq_1$ and $f_c=\\dot Q_c-rQ_cq_1$. Tangency holds in both. Which extension the historical downstream code used cannot be checked from the repository; T-6r C3 (§2) fixes the extension for any future corrected-field work.\n")
ed("X04", "1",
   "There is no real replacement for $x_*$ at this order.\n",
   "There is no real replacement for $x_*$ at this order.\n\n"
   "`[ALG]` `[scope: truncated coefficient ODE; diagnostic]` **Remark — $D=\\mathcal G/Q_s=Q_c(1-K)$.** In extension (b), $\\dot D=0$: $D$ is a first integral of the truncated coefficient ODE. In extension (a), $\\dot D=r\\,q_1D$: $D$ is not constant in general; it is constant on the $r^1$-free field and on special solutions such as $D\\equiv0$ ($K=1$), and in general only the sign of $D$ (equivalently, the sets $K<1$, $K=1$, $K>1$) is preserved. $D$ is a property of the truncated diagnostic field, not a conserved physical mode, and not a statement about the exact six-step map. No RID is assigned. Evidence (`EV-RUN`, preparer; `python -I -B <script>`; outputs in `evidence/triad/v1.7/`): `evidence/triad/scripts/triad_reconciliation_row1_extension_check.py` (SHA-256 `b6c02ae56a73de55a97f0805f321453bc2035cab322df0fcaea978c09f30589f`; extensions (a) and (b)) and `evidence/triad/scripts/triad_coowner_row1_row3_check.py` (SHA-256 `ab3482b7ec96d7ac25ef3113d291545e5b7ace400235680066bd0a627e66cea5`; C2–C3). The $r^1$ and $r^2$ parts of $\\Delta\\Omega$ used there are the $Q_c$-free values fixed by the Gram identity on the root, not the $H_1,H_2$ producer bytes, which are not in the repository.\n")
ed("X05", "7",
   "The 96:1 identification stays OPEN as before.",
   "The 96:1 identification stays OPEN; its status and the metric caveat are stated once in §1.")
ed("X06", "2",
   "| `TRIAD-ALG-T6E-ORIENTATION-NORMALIZATION` | typed relation $\\Omega=-\\sqrt3\\omega_{\\rm raw}$ and rate conversion | diagnostic convention correction |",
   "| `TRIAD-ALG-T6E-ORIENTATION-NORMALIZATION` | typed relation $\\Omega=-\\sqrt3\\omega_{\\rm raw}$ and rate conversion (a first-variation identity, §6.18) | diagnostic convention correction |")
ed("X07", "9",
   "| CN-05 | required re-review of old T-6 sector/wedge/basin/obstruction imports | consumer action OPEN |",
   "| CN-05 | required re-review of old T-6 sector/wedge/basin/obstruction imports | consumer state: §7.4 |")
ed("X08", "9",
   "`[DEF]` Genesis OPEN 1T and dependent consumers must re-review prior imports under CN-05.",
   "`[DEF]` Genesis OPEN 1T and dependent consumers re-review prior imports under CN-05 (receipts: §7.4).")

# =============================================================================================== §7.3–7.4 (rows 9, 10, 11, 12-info, 15)
ed("V01", "9", "### §7.3 Exports — adopted v1.6; consumer synchronization pending\n", "### §7.3 Exports\n")
ed("V02", "9", "Current adopted exports available to Genesis/OPEN M; local consumer acceptance remains pending:\n",
   "Current exports (consumer state per notice: §7.4):\n")
ed("V03", "9", "### §7.4 Consumer correction notices — scientific reconciliation pending\n",
   "### §7.4 Consumer correction notices and consumer state\n")
ed("V04", "9",
   "`[DEF]` These notices are outbound review obligations, not amendments of another owner's records. Consumer acceptance remains OPEN until each owner records disposition against the adopted Triadic version/hash.\n",
   "`[DEF]` These notices are outbound review obligations, not amendments of another owner's records. Each receiver's disposition is its own record; the matrix below states what each receiver has recorded at its governing tag (`EV-SRC-READ`, 30 October 2026).\n")

MATRIX = (
    "**Consumer state (current).** \"Received\" means the receiver's DSN records the notice; \"statement accepted\" is the receiver's recorded verdict; \"adopted use\" is read only from the receiver's Import Ledger row or release record (CONVENTIONS §7).\n\n"
    "| CN | Recipient (governing tag) | Triadic edition the receiver cites | Queue | Statement accepted (receiver record) | Adopted use | Remaining gate |\n"
    "|---|---|---|---|---|---|---|\n"
    "| CN-01 | Genesis (`gen-v2.9`) | v1.6 | received | yes — `GEN-OPEN-APEX-SLOT` retracted as `[RESULT]`; $d$-mode label and seed retained (§8) | Import Ledger row CN-01 (§7) | physical transverse/UV embedding OPEN |\n"
    "| CN-02 | Genesis (`gen-v2.9`) | v1.6 | received | yes — live text uses $F_{\\rm face}$; the free $F_W(\\eta_*)$ target withdrawn as a live parametrization | Import Ledger row CN-02 | full-phase remainder depends on the child functional (GCL-06) |\n"
    "| CN-02 | OPEN-M (`uvm-v0.7.1`) | v1.6 | received | yes — v0.6 unit-child / fixed-$F_W$ corroboration superseded | Import Ledger (§7) | face-phase remainder depends on the child/residual order (GCL-06) |\n"
    "| CN-03 | Genesis (`gen-v2.9`) | v1.6 | received | yes, as a consistency check; proof direction stays Genesis → Triadic | Import Ledger row CN-03 | none beyond the exact $I_{sc}=0$ scope |\n"
    "| CN-04 | OPEN-M (`uvm-v0.7.1`) | v1.6 | received | yes — HYP-M-PREFRACTURE's premise \"T-6t apex independent\" withdrawn | Import Ledger (§7) | HYP-M-PREFRACTURE falsifier (OPEN-M) |\n"
    "| CN-05 | Genesis (`gen-v2.9`) | v1.6 | received | yes — historical wedge, $x_*$, no-basin, phase-steering and route-obstruction exports withdrawn from current Genesis use (OPEN 1T, SG-12) | Import Ledger row CN-05 | corrected finite-$u/r$ orientation flow (T-6r, T-6q) |\n"
    "| CN-05 | OPEN-M (`uvm-v0.7.1`) | v1.6 | received | yes — continuous phase/source route settled neither for nor against | Import Ledger (§7) | continuous phase/source route unresolved; CN-01 review separate |\n"
    "| CN-05 | RRF (`rrf-v0.8.4`) | v1.6 | received | recorded as convention only (§3.1, \"proposed consumer receipt\") | §3.1 `[DEF]` with in-text import tag; no RID-keyed row; $Q_c^T$ conversion not applied | same-vector Genesis–Triadic birth bridge OPEN |\n"
    "| CN-05 | OFN (`ofn-v0.12`) | v1.6.1 | received | reference-only — OFN half of pass two recorded (RF-O08-02, RF-O08-08) | none (reference rows, not imports) | 96:1 correspondence (§1) |\n"
    "| CN-05 | Programme (`programme-v1.3`) | v1.6 (interface register IF07, IF11) | v1.3 is the pass-two synchronization edition | no CN-05 disposition recorded | none | Programme record of CN-05 |\n\n"
    "Notes. Receivers also record notices not addressed to them (OPEN-M: CN-01, CN-03; OFN: CN-01–CN-04, reference-only). No receiver records the Triadic source hash asked for in CN-05's acknowledgment fields. A v1.6 receipt is not acceptance of a v1.6.1 or v1.7 delta. Genesis imports T-6s, T-6t and T-6u at `[CAND]`, below the Triadic `[ALG]` (`gen-v2.9` §2); that is the receiver's grading of its own use. These receipts close no physical OPEN (CN-01 transverse carrier, CN-04 HYP-M-PREFRACTURE falsifier, child-functional selection). Post-release notices are filed as pipe items (§2).\n")
ed("V05", "9/10/15",
   "**v1.6.1 consumer receipt (recorded, not a Triadic acceptance):**",
   MATRIX + "\n**v1.6.1 consumer receipt (history, as recorded at v1.6.1; superseded by the matrix above):**")
ed("V06", "15", "`[v1.6.1 r2 — H-R1]` Scoped receipts,", "Scoped receipts,")
ed("V14", "9", "Consumer acceptance remains pending.", "Consumer state: §7.4.", "live", 2)
ed("V15", "9", "; consumer acceptance remains pending.", "; consumer state: §7.4.", "live", 1)
ed("V13", "10",
   "Programme v1.2 remains an inventory/architecture first-pass source and its pass-two synchronization is still pending.",
   "Programme v1.2 was then an inventory/architecture first-pass source; Programme v1.3 (`programme-v1.3`) is the pass-two synchronization edition (matrix above).")
ed("V07", "9", "**Consumer status: OPEN; scientific review, not a pointer-only update.**", "**Consumer state:** matrix above.")
ed("V08", "9", "**Consumer status: OPEN; update sign, extent, symbol and artifact interpretation at each use.**", "**Requested action:** update sign, extent, symbol and artifact interpretation at each use. **Consumer state:** matrix above.")
ed("V09", "9", "**Consumer status: positive consistency notice; no Genesis record altered.**", "**Consumer state:** matrix above (positive consistency notice; no Genesis record altered).")
ed("V10", "9", "**Consumer status: OPEN, scientific reconciliation required.**", "**Consumer state:** matrix above.")
ed("V11", "9/11",
   "`[DEF]` **Two-pass handoff.** Exact r4.2 revision-editor review is accepted and this owner release is issued at the user's instruction. Next synchronize Genesis and OPEN M against this release's version/hash and route the convention-only items to RRF; Programme/OFN pass two follows. No consumer file or RRF profile is changed by this release.",
   "`[DEF]` **Notices.** After an adopted release, claim-specific notices are filed as items in the receivers' inboxes (`pipes/<STREAM>/`, CONVENTIONS §7). Filing is a queue event; statement acceptance and adopted use are the receivers' records (§7.4). No consumer file or RRF profile is changed by a Triadic release.")
ed("V12", "9",
   "Historical safety-wedge/no-basin/phase-steering obstruction exports are withdrawn from current use pending consumer reconciliation.",
   "Historical safety-wedge/no-basin/phase-steering obstruction exports are withdrawn from current use; Genesis records the withdrawal (CN-05, §7.4).")

# =============================================================================================== §8 (rows 14, 25, §0(a))
ed("R01", "25",
   "- [RID: TRIAD-ART-T6C-CROSSPHASE] :: `tetrahedral_six_step_cross_phase_t6c2_patched.py` :: recovered bytes SHA-256 `afb4525ccc2f459964fc3e9acade004f2aa61c03be2366f125cef63fc466d80e`;",
   "- [RID: TRIAD-ART-T6C-CROSSPHASE] :: `tetrahedral_six_step_cross_phase_t6c2_patched.py` :: recovered bytes SHA-256 `afb4525ccc2f459964fc3e9acade004f2aa61c03be2366f125cef63fc466d80e`; in the repository at `evidence/triad/scripts/` (recovered from commit `9df0319`; hash equal; not rerun in v1.7);")
ed("R02", "25",
   "- [RID: TRIAD-ART-T6L-TORSION] :: `triad_analytic_phase_steering_t6l_patched.py` :: recovered historical algebra, SHA-256 `2e0317bf90332d1fe0ab7489710a3c8c67b772e3031dd7ef95b3163f7d7a11cd`;",
   "- [RID: TRIAD-ART-T6L-TORSION] :: `triad_analytic_phase_steering_t6l_patched.py` :: recovered historical algebra, SHA-256 `2e0317bf90332d1fe0ab7489710a3c8c67b772e3031dd7ef95b3163f7d7a11cd`; in the repository at `evidence/triad/scripts/` (recovered from commit `9df0319`; hash equal); rerun unchanged 30 Oct 2026, output `evidence/triad/v1.7/t6l_patched_rerun_output_20261030.json` reproduces the historical ratio polynomial and $x_*$ (historical algebra only; no regrade);")
ed("R03", "14",
   ":: Birth angle, branch assignment, finite-$u$ torsion turn; T-6m :: `[ALG+NUM diagnostic]`",
   ":: Birth angle, branch assignment, finite-$u$ torsion turn; T-6m :: `[ALG]` `[scope: diagnostic]` for the exact reference angle and the producer-frame turn polynomial/root; numerical session values are `[NUM]` `[scope: diagnostic]` corroboration only; session log not archived")

# =============================================================================================== §9 (rows 13, hdr)
ed("W01", "hdr",
   "**This release (v1.6.1):** owner release of the co-owner-accepted DRAFT r2",
   "**This edition (v1.7, stage 1):** prepared by Claude from the confirmed co-owner reconciliation; change-focused review by ChatGPT; PI adoption pending. **History — v1.6.1 release:** owner release of the co-owner-accepted DRAFT r2")
RIDSET = (
    "**Identifier set (v1.7).** This ledger declares 46 `TRIAD-*` RIDs (13 ALG, 22 ART, 2 EXPORT, 2 NUM, 7 OPEN); none is added, removed or renamed in v1.7. "
    "Current: `TRIAD-ALG-T6E-ORIENTATION-NORMALIZATION`, `TRIAD-ALG-T6L-NORMALIZED-TORSION-SIGN`, `TRIAD-ALG-T6M-REFERENCE-QUARTER-TURN`, `TRIAD-ALG-T6S-COHERENT-CONJUGATE-FAMILY`, `TRIAD-ALG-T6T-JACOBI-MODE-SIGNS`, `TRIAD-ALG-T6U-APEX-SEED-DIAGNOSTIC`, `TRIAD-NUM-T6J2-ROOT-CLOSED-EXCURSION`, `TRIAD-EXPORT-PROTOCOL-2`, `TRIAD-OPEN-T6M2`, `TRIAD-OPEN-T6N`, `TRIAD-OPEN-T6O`, `TRIAD-OPEN-T6Q`, `TRIAD-OPEN-T6R`, and the 22 artifact RIDs of §8. "
    "Historical or replaced, retained for traceability (Appendix B, §7.3): `TRIAD-ALG-ISC-ATTRACTOR`, `TRIAD-ALG-SAFETY-WEDGE`, `TRIAD-ALG-T6M-BIRTH-OBSTRUCTION`, `TRIAD-ALG-T6S-INPLANE-CHIRALITY`, `TRIAD-ALG-T6T-CHIRALITY-COUNT`, `TRIAD-ALG-T6U-APEX-SOURCE`, `TRIAD-ALG-VERDICT`, `TRIAD-NUM-T6J2-NO-BASIN`, `TRIAD-EXPORT-PROTOCOL-1`, `TRIAD-OPEN-T6J2`, `TRIAD-OPEN-T6M`. "
    "The string `RER-TRIAD-BIRTH-GRAPH-INVOLUTION` (§7.2) is a noncanonical RER record name, not a Triadic RID. The v1.6 phrase \"all 49 RIDs\" (Appendix A) cannot be reproduced from the repository, because the v1.5 and v1.6 files are not in it.<BR>\n")
ed("W02", "13", "**Archive:** Historical project pointer inherited from v1.5:", RIDSET + "**Archive:** Historical project pointer inherited from v1.5:")

# =============================================================================================== Appendix B (rows 14, 21)
ed("B01", "14",
   "| [RID: TRIAD-NUM-T6J2-NO-BASIN] | `TRIAD-NUM-T6J2-ROOT-CLOSED-EXCURSION` `[NUM historical]` |",
   "| [RID: TRIAD-NUM-T6J2-NO-BASIN] | `TRIAD-NUM-T6J2-ROOT-CLOSED-EXCURSION` `[NUM]` `[scope: historical root-closed session]` |")
NEG = (
    "\n`[COR]` **Current reading of the negative records above (v1.7).** The v1.5 reasons that cite the torsion-safe wedge, $x_*$, the $22^\\circ$ arc or phase steering into fatal sectors belong to the executed mis-scaled model (§6.18, SG-4, SG-7) and are not current reasons. A retraction need not be a proof of falsity (Methodology v1.4). Classification:\n\n"
    "| Record | Current class | Basis |\n"
    "|---|---|---|\n"
    "| `[RETRACTED]` global $K_3$ explosiveness | retraction stands (claim not established); v1.5 reason historical | 96:1 correspondence OPEN (§1) |\n"
    "| `[RETRACTED]` universal smooth $K_4$ explosion | retraction stands (claim not established); its phase-steering reason is withdrawn | T-6g square identities retained only as fixed-expression identities (§6.8) |\n"
    "| `[RETRACTED]` stable smooth $K_4$ self-limitation | retraction stands (does not follow from $A_2\\le0$ alone); the torsional-dynamics reason is historical | §6.8, §6.11 |\n"
    "| `[RETRACTED]` annihilation from Plücker contact alone | valid current negative | contact is not annihilation (SG-5, SG-11; T-6n OPEN) |\n"
    "| `[RETRACTED]` theorem-grade completion from the constrained T-6f chart | valid, at chart scope | $Q_c$ is algebraically enslaved in that chart; T-6f is itself a historical executed-model record |\n"
    "| `[FAIL]` orthogonal slice $I_{sc}=0$ invariant | valid current failure in $M_{\\rm root}$ | $\\Delta I_{sc}^{(2)}\\ne0$ at $I_{sc}=0$ (§6.5) |\n"
    "| `[FAIL]` $I_{sc}^*$ as full-system stable attractor | not a current failure: its reason (the historical wedge) is withdrawn | §6.5, SG-6; the stability question is open again (T-6o) |\n"
    "| `[FAIL]` naive $\\sigma=+1\\to-1$ flip at contact | valid current failure of the tested naive flip | T-6d2, $\\dot W^2<0$ ($M_{\\rm root}$; SG-5) |\n"
    "| `[FAIL]` T-6f runaway as free-$Q_c$ theorem | valid, at chart scope | $Q_c$ enslaved in that chart |\n"
    "| `[FAIL]` neutral ray $\\theta=30^\\circ$ as safety criterion | not a current failure: its reason (the historical wedge) is withdrawn | SG-7 |\n"
    "| `[FAIL]` wider radial arc $\\theta\\lesssim22^\\circ$ as escape criterion | not a current failure: arc and wedge are properties of the executed mis-scaled model | SG-7, §6.11 |\n\n"
    "\"Not a current failure\" means the record stays as history and supports no current negative result; it does not assert the opposite claim.\n")
ed("B02", "21",
   "- `[FAIL]` Wider radial arc ($\\theta \\lesssim 22°$) as sufficient escape criterion — torsional safety binds at $5.5°$; sufficiency of even the $5.5°$ window is unproven.\n",
   "- `[FAIL]` Wider radial arc ($\\theta \\lesssim 22°$) as sufficient escape criterion — torsional safety binds at $5.5°$; sufficiency of even the $5.5°$ window is unproven.\n" + NEG)

# =============================================================================================== footer
ed("F01", "hdr",
   "*END OF DOCUMENT — RTG_TRIADIC_BIRTH_LIFT_DSN_v1.6.1 — ADOPTED OWNER RELEASE (19 October 2026); scientific body identical to co-owner-accepted DRAFT r2 (`dd67907fc21e457e413c3d6ee924617bc7818c1c200a9bde04fb67649d79b3e7`). The v1.6 footer below is history.*<BR>\n",
   "*END OF DOCUMENT — RTG_TRIADIC_BIRTH_LIFT_DSN_v1.7 — DRAFT, stage-1 intermediate; adoption pending; `triad-v1.6.1` governs until adoption and tag. The v1.6 footer below is history (single footer: stage 2).*<BR>\n")

# =============================================================================================== ROW 8 — claim-level repins
# Re-read at the governing tags on 30 Oct 2026 (EV-SRC-READ). REPIN where statement, value and grade are unchanged;
# HOLD (keep the historical claim-level pin, with the reason) for the radial-polynomial premise and the Programme §6.3 text.
GEN_READ = "re-read at `gen-v2.9`"
ed("M01", "8", "**Companion documents (v1.6.1 refresh):**",
   "**Companion documents (governing editions read for v1.7):** Programme Overview v1.3 (`programme-v1.3`); DSN Methodology v1.4 (`methodology-v1.4`); OFN v0.12 (`ofn-v0.12`); Dyadic Oscillator v6.4.23 (`dyad-v6.4.23`); Genesis Geometry v2.9 (`gen-v2.9`); OPEN-M v0.7.1 (`uvm-v0.7.1`); RRF v0.8.4 (`rrf-v0.8.4`); TDR-G v2.12.14 (`tdrg-v2.12.14`). Proof imports keep claim-level pins: an import is repinned only where its statement was re-read at the governing tag (§7.1–§7.2 say which); the others keep their historical proof pin.<BR>\n", "line")
ed("M02", "8", "These import records were pinned in v1.5/v1.6 to `RTG_DYADIC_OSCILLATOR_DSN_v6.4.8.1`",
   "These import records were pinned in v1.5/v1.6 to `RTG_DYADIC_OSCILLATOR_DSN_v6.4.8.1` via `dyad_triad_antisymmetric_bridge_v1_1.md`, and in v1.6.1 to v6.4.13 (SHA-256 `5958f7fe8a3e0ec94546cb7e915c5f690d09827a3d680d13a17c9d880b968542`). **v1.7 claim-level re-read (`EV-SRC-READ`, 30 Oct 2026):** each RID below is present at `dyad-v6.4.23` with the same statement, value and grade, and is repinned to Dyadic v6.4.23. `DYAD-DEF-PRIMITIVE-MAP` is still provisional there; `DYAD-DEF-BRIDGE-EXPORT-CONTRACT` item 1 and the six-item export contract are unchanged; the frame qualifier `DYAD-ALG-KP-FRAME-SCALE` (v6.4.20) is a separate RID and is not imported. Dyadic additions that concern the isolated dyad (for example `DYAD-THM-FORMAL-Z6-GENERATOR`, Lemma F and F1–F3, the OPEN 20 restructuring) are not imported. The frame/protection-matrix row no longer carries the Lie-gauge RID: Dyadic v6.4.11 `DYAD-DEF-BRIDGE-EXPORT-CONTRACT` states that none of the bridge exports depends on the Lie strict-kernel gauge. The intermediary bridge note is still not in this package. Current Dyadic SG-19 is a source of normalization discipline, not permission to identify raw, archival, projected and conjugate objects.\n", "line")
ed("M03", "8", "(Dyadic v6.4.13 §", "(Dyadic v6.4.23 §", "live", 5)
ed("M04", "8", "- `RTG_PROGRAMME_OVERVIEW_v1_2.md` §6.3 and SG-PROG-1",
   "- Programme Overview v1.3 (`programme-v1.3`, re-read) §6.3 TRIAD entry and SG-PROG-1 (§8) — cross-branch firewall: no physical law, coefficient or observable identification passes between the discrete and continuous branches without a named bridge in the importing owner's Import Ledger. The v1.2 §6.3 owner-review wording cited by v1.6.1 is not in v1.3; this reference implies no global no-cascade conclusion.\n", "line")
ed("M05", "8", "- `RTG_ONTOLOGICAL_FOUNDATIONS_v0_9.md` (v1.6.1 pointer refresh from v0.8;",
   "- OFN v0.12 (`ofn-v0.12`; pointer refresh from v0.9) — relational event interpretation; not proof of this birth law, added independent substance, or added physical dimension. Its local result `RTG-OFN-ALG-REF-CLOSURE-COMPARISON` enters T-6r C1 (§2) as an interface constraint.\n", "line")
ed("M06", "8/13", "- `RTG_RRF_REPRESENTATION_REGISTRY_v0_8_2.md` (v1.6.1 pointer refresh from v0.6;",
   "- RRF v0.8.4 (`rrf-v0.8.4`, re-read; pointer refresh from v0.8.2; its §3.1 records CN-05's planar metric convention $B_T^{\\rm plane}=2B_G$ as convention-only, with the conditional $Q_c^T=\\tfrac{\\kappa^2}{4}(Q_s^T)^3$ conversion recorded as an obligation and not applied) — convention/transport reference only. This ledger's $s,c,d$ are explicitly primitive $B$-mode coordinates; no $z_{\\rm NF}$ is substituted into network closure. A reference does not register a missing profile or close OPEN-A/OPEN-B/E1.\n", "line")
ed("M07", "8", "(retained unchanged in v2.8.6/v2.8.7)",
   "(retained unchanged through v2.9; re-read at `gen-v2.9`: `[RETRACTED]` as `[RESULT]` with the RID preserved, physical embedding `[OPEN]`)")
ed("M08", "8", "- Genesis v2.8.7 `GEN-THM-K3-PLANAR-FACTOR-NOGO`",
   "- Genesis v2.9 (`gen-v2.9`, re-read; both `[THM]`, unchanged) `GEN-THM-K3-PLANAR-FACTOR-NOGO`")
ed("M09", "8", "- `RTG_DISCRETE_GENESIS_DSN_v2_12_13.md` §2 `TDRG-OPEN-CHI-SCALING` — reference-only.",
   "- TDR-G v2.12.14 (`tdrg-v2.12.14`, re-read) §2 `TDRG-OPEN-CHI-SCALING` — reference-only.")
ed("M10", "8", "All uses remain conditional on the source model; this consumer does not promote its physical premises.",
   "All uses remain conditional on the source model; this consumer does not promote its physical premises. **v1.7 claim-level pins:** the imports below were re-read at `gen-v2.9` (`EV-SRC-READ`, 30 Oct 2026) and are repinned to Genesis v2.9 where statement, value and grade are unchanged. None of the nine \"RID unavailable\" statements has a result RID at `gen-v2.9` (artifact locators only), and Genesis records no response to the REQ-T16 requests. The radial-polynomial import keeps its v2.8.7 pin (see that entry). Other point-of-use Genesis pins (the GCL-06 remainder guard and the GSPLIT reference note in §6.15, the §6.1 history sentence) keep their v2.8.7 claim-level pins.")
ed("M11", "8", "[import: RTG_GENESIS_GEOMETRY_DSN_v2.8.7 §6.1 #sec-6-1-primitive, Quadratic form |",
   "[import: RTG_GENESIS_GEOMETRY_DSN_v2.9 §6.1 #sec-6-1-primitive, Quadratic form (" + GEN_READ + ") |")
ed("M12", "8", "owner RIDs assigned by Genesis v2.8.5 §6.1 and retained in v2.8.7.", "owner RIDs assigned by Genesis v2.8.5 §6.1 and retained through v2.9.")
ed("M13", "8", "[import: RTG_GENESIS_GEOMETRY_DSN_v2.8.7 §6.6 #sec-6-6-phase, Symplectic phase-drift operator | RID unavailable; artifact locator `GEN-ART-JQ-PHASEDRIFT`; v1.6.1 repin, value unchanged]",
   "[import: RTG_GENESIS_GEOMETRY_DSN_v2.9 §6.6 #sec-6-6-phase, Symplectic phase-drift operator | RID unavailable; artifact locator `GEN-ART-JQ-PHASEDRIFT`; " + GEN_READ + ", value unchanged]")
ed("M14", "8", "[import: RTG_GENESIS_GEOMETRY_DSN_v2.8.7 §6.3 #sec-6-3-triad, one-dimensional birth theorem | RID unavailable]",
   "[import: RTG_GENESIS_GEOMETRY_DSN_v2.9 §6.3 #sec-6-3-triad, one-dimensional birth theorem | RID unavailable; " + GEN_READ + ", statement unchanged]", "live", 2)
ed("M15", "8", "[import: RTG_GENESIS_GEOMETRY_DSN_v2.8.7 §6.3 #sec-6-3-triad, one-dimensional birth theorem | RID unavailable; artifact locator `GEN-ART-PHI-2TO3`]",
   "[import: RTG_GENESIS_GEOMETRY_DSN_v2.9 §6.3 #sec-6-3-triad, one-dimensional birth theorem | RID unavailable; artifact locator `GEN-ART-PHI-2TO3`; " + GEN_READ + ", statement unchanged]")
ed("M16", "8", "Verification: source-read against adopted v2.8.7 (§1 and §6.3 wording retained from v2.8.5 GCL-06);",
   "Verification: source-read against adopted v2.8.7 and " + GEN_READ + " (§1 and §6.3 wording retained from v2.8.5 GCL-06);")
ed("M17", "8", "[import: RTG_GENESIS_GEOMETRY_DSN_v2.8.7 §1 and §6.3, remainder clause | RID unavailable]",
   "[import: RTG_GENESIS_GEOMETRY_DSN_v2.9 §1 and §6.3, remainder clause | RID unavailable; " + GEN_READ + ": GCL-06 still OPEN, the clause still conditional]")
ed("M18", "8", "[import: RTG_GENESIS_GEOMETRY_DSN_v2.8.7 §6.3 #sec-6-3-triad, Shear policy | RID unavailable; v1.6.1 repin, value unchanged]",
   "[import: RTG_GENESIS_GEOMETRY_DSN_v2.9 §6.3 #sec-6-3-triad, Shear policy | RID unavailable; " + GEN_READ + ", value unchanged]")
ed("M19", "8", "[import: RTG_GENESIS_GEOMETRY_DSN_v2.8.7 §6.3 #sec-6-3-triad, Recoil policy | RID unavailable; v1.6.1 repin, value unchanged]",
   "[import: RTG_GENESIS_GEOMETRY_DSN_v2.9 §6.3 #sec-6-3-triad, Recoil policy | RID unavailable; " + GEN_READ + ", value unchanged]")
ed("M20", "8", "[import: RTG_GENESIS_GEOMETRY_DSN_v2.8.7 §6.4 #sec-6-4-tetrahedral, Tetrahedral chronological protection | RID unavailable; v1.6.1 repin, statement unchanged]",
   "[import: RTG_GENESIS_GEOMETRY_DSN_v2.9 §6.4 #sec-6-4-tetrahedral, Tetrahedral chronological protection | RID unavailable; " + GEN_READ + ", statement unchanged]")
ed("M21", "8", "[import: RTG_GENESIS_GEOMETRY_DSN_v2.8.7 §6.5 #sec-6-5-quartic, Full primitive quartic drift | RID unavailable; v1.6.1 repin, polynomial unchanged]",
   "[import: RTG_GENESIS_GEOMETRY_DSN_v2.8.7 §6.5 #sec-6-5-quartic, Full primitive quartic drift | RID unavailable; claim-level historical pin kept: at `gen-v2.9` the polynomial is printed unchanged as $\\Delta Q_d^{(4)}$ (§6.5, `[THM]`), but the identity $\\mathcal P_4=2d^TBG_{3,d}$ used with it here is not printed there (only the $c$-mode analogue $\\Delta Q_c^{(4)}=2c^\\top BG_{3,c}$); query to the Genesis owner]")
ed("M22", "8", "| RID unavailable; v1.6.1 r2 repin: printed $\\mathcal P_4$ and seed norms unchanged (§7.2)]",
   "| RID unavailable; claim-level historical pin: seed norms " + GEN_READ + " unchanged, the $\\mathcal P_4=2d^TBG_{3,d}$ premise not printed there (§7.2)]")
ed("M23", "8", "[import: RTG_GENESIS_GEOMETRY_DSN_v2.8.7 §6.5 #sec-6-5-quartic, Vector apex seeding | RID unavailable; artifact locator `GEN-ART-G3D-SEED`; v1.6.1 repin, values unchanged]",
   "[import: RTG_GENESIS_GEOMETRY_DSN_v2.9 §6.5 #sec-6-5-quartic, Vector apex seeding | RID unavailable; artifact locator `GEN-ART-G3D-SEED`; " + GEN_READ + ", values unchanged; source symbols $Q_{d,1}^{[s^3]}$, $Q_{d,1}^{[c^3]}$]")
ed("M24", "8", "[import: RTG_GENESIS_GEOMETRY_DSN_v2.8.7 §6.6 #sec-6-6-phase, Birth symmetry theorem | RID unavailable; v1.6.1 repin, values unchanged]",
   "[import: RTG_GENESIS_GEOMETRY_DSN_v2.9 §6.6 #sec-6-6-phase, Birth symmetry theorem | RID unavailable; " + GEN_READ + ", values unchanged; source symbols $I_{ds}^{(1)}$, $\\omega_{ds}^{(1)}$; the source states it as `[THM]` in its §6.6 and as `[ALG]` in its §1 summary and §8 artifact row — query to the Genesis owner]")
ed("M25", "8", "[import: RTG_GENESIS_GEOMETRY_DSN_v2.8.7 §6.6 #sec-6-6-phase, Birth symmetry theorem | RID unavailable; v1.6.1 r2 repin, values unchanged (§7.2)]",
   "[import: RTG_GENESIS_GEOMETRY_DSN_v2.9 §6.6 #sec-6-6-phase, Birth symmetry theorem | RID unavailable; " + GEN_READ + ", values unchanged (§7.2)]")
ed("M26", "8", "[import: RTG_GENESIS_GEOMETRY_DSN_v2.8.7 §2 OPEN-GEN-II-HINDEX, displayed norm and status-table definition row | module locator `GEN-OPEN-HINDEX`; v1.6.1 repin, definition unchanged;",
   "[import: RTG_GENESIS_GEOMETRY_DSN_v2.9 §2 OPEN-GEN-II-HINDEX, displayed norm and status-table definition row | module locator `GEN-OPEN-HINDEX`; " + GEN_READ + ", definition unchanged;")
ed("M27", "8", "[import: RTG_GENESIS_GEOMETRY_DSN_v2.8.7 §2 OPEN-GEN-II-HINDEX, displayed source-amplitude norm and status-table row | RID unavailable; v1.6.1 r2 repin, definition unchanged (§7.2)]",
   "[import: RTG_GENESIS_GEOMETRY_DSN_v2.9 §2 OPEN-GEN-II-HINDEX, displayed source-amplitude norm and status-table row | RID unavailable; " + GEN_READ + ", definition unchanged (§7.2)]")
ed("M28", "8", "[import: RTG_GENESIS_GEOMETRY_DSN_v2.8.7 §6.5 #sec-6-5-quartic, standalone chiral admissibility polynomial | GEN-THM-DELTA-QC; v1.6.1 repin, polynomial unchanged]",
   "[import: RTG_GENESIS_GEOMETRY_DSN_v2.9 §6.5 #sec-6-5-quartic, standalone chiral admissibility polynomial | GEN-THM-DELTA-QC; " + GEN_READ + ", polynomial unchanged]")

def apply(base):
    s = base; log = []
    for (i, row, mode, old, new, count) in E:
        before = s
        if mode == "str":
            n = s.count(old)
            if n != 1: raise SystemExit(f"{i}: expected 1 occurrence, found {n}: {old[:100]!r}")
            s = s.replace(old, new)
        elif mode == "live":
            a = s.index(LIVE_END); live, rest = s[:a], s[a:]
            n = live.count(old)
            if n != count: raise SystemExit(f"{i}: expected {count} live occurrences, found {n}: {old!r}")
            s = live.replace(old, new) + rest
        elif mode == "line":
            lines = s.split("\n")
            hits = [k for k, ln in enumerate(lines) if old in ln]
            if len(hits) != 1: raise SystemExit(f"{i}: expected 1 line containing prefix, found {len(hits)}: {old[:100]!r}")
            k = hits[0]
            if not lines[k].startswith(old): raise SystemExit(f"{i}: prefix is not at line start")
            old = lines[k] + "\n"
            s = s.replace(old, new, 1)
        else:
            raise SystemExit(f"{i}: unknown mode {mode}")
        log.append({"id": i, "row": row, "mode": mode, "count": count if mode == "live" else 1,
                    "old": old, "new": new, "old_sha256": sha(old), "new_sha256": sha(new),
                    "doc_sha256_before": sha(before), "doc_sha256_after": sha(s)})
    return s, log

def main(argv):
    if len(argv) != 4: raise SystemExit(__doc__)
    base = open(argv[1], "rb").read()
    if hashlib.sha256(base).hexdigest() != BASE_SHA: raise SystemExit("input is not the adopted triad-v1.6.1 file")
    out, log = apply(base.decode("utf-8"))
    for e in log:
        if e["new"] and out.count(e["new"]) < 1:
            raise SystemExit(f"{e['id']}: new text not present in candidate")
    open(argv[2], "w", encoding="utf-8", newline="\n").write(out)
    json.dump({"base_sha256": BASE_SHA, "candidate_sha256": sha(out), "edits": log}, open(argv[3], "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"edits: {len(log)}; candidate sha256: {sha(out)}; lines: {out.count(chr(10))}")

if __name__ == "__main__":
    main(sys.argv)
