# Triadic — next owner cycle (v1.8): collected work list

**Date:** 3 November 2026. **By:** Claude, Triadic co-owner. **Status:** working record at a fixed path. It decides nothing. It collects the open Triadic items after `triad-v1.7` and proposes an order; the co-owners dispose, and the PI starts any build.
**Governing edition:** `triad-v1.7` (`506f3403…e64a`). **Started by:** the PI, 3 November 2026 ("bir sonraki triadic döngüsünü başlatıp kalan işleri toplayalım").
**Sources read** (`EV-SRC-READ`):
- the v1.7 release record (§7) and post-tag record;
- ChatGPT's post-release priority list (P0–P3, 3 Nov 2026);
- `pipes/TRIAD/` (one item, dispositioned) and the three Triadic items in `pipes/GEN/`, all `open` with no answer yet;
- `atlas/RTG_STATE_ATLAS.md` on `main`, which still carries Triadic v1.6.1: H8, F11–F14, F18, F20, F23 and LEGACY.Y6.

## 1. Items

Classes: **W** wait (needs another owner's answer) · **F** form (no science) · **S** science/scope · **C** custody · **N** notation · **R** atlas reply only (no Triadic text change expected).

| # | Item | Source | Class | Proposed handling | Decision needed |
|---|---|---|---|---|---|
| T8-01 | **P0.** Genesis 𝒫₄ = 2dᵀBG₃,d identity: is it still asserted, and where? | `pipes/GEN/20261103-TRIAD-p4-identity-question.md` | W | When Genesis answers: repin the §7.2 radial-polynomial import and the §6.17.1 premise to `gen-v2.9`, or restate the premise from what Genesis does print. No change before then | none until the answer |
| T8-02 | **P1.** Genesis birth-symmetry grade: `[THM]` in §6.6 versus `[ALG]` in §1 and §8 | `pipes/GEN/20261103-TRIAD-birth-symmetry-grade-question.md` | W | Take the grade the owner names; the Triadic import bracket drops the discrepancy note | none until the answer |
| T8-03 | **P2 / F-1.** Qualifier syntax: 67 backticked qualifiers against Methodology v1.4 §3.2 (plain brackets) | v1.7 release record §7 | F | First a tool PR: `tools/check_compaction.py` `RE_QUAL` also tracks plain-bracket qualifiers, with tests. Then a Triadic stage-1 form edit converts the 67 (assertion-gated; no other change) | whether the tool change goes first (proposed: yes) |
| T8-04 | **P2 / F-2.** Status summary has six sentences (target 2–4) | same | F | Drop two sentences in a stage-2 header replace (subset rule; no new text) | which two |
| T8-05 | **P2 / A-1.** v1.6-era wording in the §2 T-6u record ("Exact-candidate review and owner publication are complete", "registered by this owner release") | Atlas row check #143 | F | Restate in current-state form, or relocate as history | — |
| T8-06 | **P3.** T-6r acceptance contract C1–C6: the carrier, metric and coefficient group; the off-root extension that fixes $f_s$, $f_c$ and $D$ | DSN §2, §6.18 | S | Research item. A first step that is SESSION only: list candidate carriers (enlarged planar pair, relaxed Gram, class-C member) against C1–C6 in a design note. No campaign before the contract | whether to open it this cycle |
| T8-07 | **P3.** T-6q complete-state action (beyond the coordinate sign table) | DSN §2 | S | After T8-06; the action must intertwine with the chosen dynamics | after T8-06 |
| T8-08 | T-6m2: Race-A $r^1/r^2$ apex correction to the producer-frame turn root $Q_s^{\rm turn}=(2\sqrt7-1)/6$ | DSN §2 (low priority) | S | A bounded algebra task in its own producer convention, with no comparison to $x_*$. It is feasible only if the producer-frame ansatz can be reconstructed from the repository (T-6m is session-only, F14). First step: check feasibility, without promising a result | whether to attempt |
| T8-09 | T-1 extraction contract versus Genesis `GEN-ART-DELTA-QS-SHADOW` (both leading ¼Q_s²). If they are the same object, the 96:1 non-correspondence is located (different generators) | Atlas F12 (TRIAD.T4) | S | Compare the two definitions from text. T-1's proof source is missing (F14), so the comparison is source-read only. It may sharpen §1's 96:1 statement; it cannot close it | — |
| T8-10 | Unregistered Triadic results (T-1, T-2b, T-4h, T-6a…T-6d modules carry artifact RIDs only) and Triadic-side RER records with no TRIAD RID | Atlas F13 (TRIAD.T3) | S/N | Owner decision on which module statements deserve claim RIDs; RER-hosted records stay in RER unless the co-owners import them by name | which, if any |
| T8-11 | Two metric normalizations ($B_T=2B_G$ for T-6a…e, $B_G$ for T-6s/t/u); same-vector transport changes the shear birth coefficient 4/3 → ⅓ | Atlas F11 (TRIAD.T7) | N | Already stated (§6.18 metric-unit block, SG-12). Possible addition: a one-line convention map at the head of §6. No conversion is applied | — |
| T8-12 | κ collision (Triadic birth κ versus class-C κ ≡ γ, κ_f, DYAD κ) | Atlas H8 / F1 | N | Programme §8.2 holds the κ table. Triadic keeps its symbol and may add a pointer at first use | — |
| T8-13 | Φ₂→₃ terminology ("current certified birth theorem" in Legacy) | Atlas LEGACY.Y6 | R | Triadic §6.1 defines Φ₂→₃ as `[DEF]` notation for the declared family; no RID. Atlas reply only | — |
| T8-14 | §7.2 citation of `RER-TRIAD-BIRTH-GRAPH-INVOLUTION` read by the Atlas as load-bearing | Atlas F18 (TRIAD.T10) | R | The owner text marks it "reference only, noncanonical". The $p=4$ bounds in §6.15 and §7.4 CN-02 are stated conditionally ("if a raw-residual quartic is retained"), not derived from RER. Atlas reply: not load-bearing | — |
| T8-15 | Triad analogue of DYAD smooth embedding for 𝒩 (G6) | Atlas F23 | S | Long research item, not for this cycle; recorded so it is not lost | — |
| T8-16 | Missing proof sources (T-1, T-2b, T-4h, T-6a, T-6g, T-6j2, T-6m) and the v1.6 package | Atlas F14; `records/triad/TRIAD_SOURCE_RECOVERY_LIST.md` | C | PI uploads to `upload/triad-…` when found; hash-check and place. Not a blocker | PI, when convenient |
| T8-17 | Row 29: `history_appendix` profile | PR #113 | W | Use it only after #113 merges | tool owner |
| T8-18 | Atlas refresh to v1.7 (A-4) | `pipes/ATLAS/20261103-TRIAD-v1-7-adopted.md` | W | The Atlas owner's next edition | Atlas |

## 2. Proposed order

1. **Now, needing no answer from anyone:**
   - the Atlas reply for T8-13 and T8-14, filed as one pipe finding to ATLAS;
   - a feasibility check for T8-08 (SESSION; may conclude "not reconstructible");
   - the source comparison T8-09 (SESSION).

   None of these changes the DSN.
2. **Tool first for T8-03.** One PR to `tools/check_compaction.py`, with tests, if the tool owner agrees.
3. **v1.8 build** once T8-01 and T8-02 are answered, or once the co-owners decide not to wait. It bundles:
   - T8-01 and T8-02 (repins or restatements);
   - T8-03, T8-04 and T8-05 (form);
   - any of T8-09 to T8-12 the co-owners accept.

   Stage 1 holds content and form, including the qualifier conversion; stage 2 is layout. The release workflow is the same as for v1.7.
4. **T8-06 and T8-07** as a separate research thread: a design note first, with no DSN text until a carrier is chosen.

## 3. Not claimed

This list makes no scientific finding. Atlas readings are cited as the Atlas states them; the owner responses in T8-13 and T8-14 are proposals until the co-owners confirm them. No pipe state of another stream is changed here.

## 4. Progress

- **3 November 2026.** ChatGPT's review `5747764214` accepted the list, with the priority: T8-08, T8-09, T8-13, T8-14 and the T8-06 design note first, merged into one advisory; T8-01 and T8-02 wait; no v1.8 build yet.
- **First pass done:** `records/triad/TRIAD_v1_8_FIRST_PASS_ADVISORY.md`, with evidence `evidence/triad/scripts/triad_v1_8_session_checks.py` (PASS).
  - T-6m2 root $0.7152504\to0.7251628$, reproduced independently;
  - T-1 against the Genesis shadow: the coefficients match, the objects differ, and a conditional metric reading is recorded;
  - T-6r: complex-collinearity, $K\le1$ on enlarged carriers, and a closure obstruction;
  - Atlas reply filed: `pipes/ATLAS/20261103-TRIAD-atlas-readings-y6-f18.md`.
- **Review of the first pass:** ChatGPT, review `5747869312`: §§1–3 accepted; two §4 corrections (tangency is not invariance; Genesis $d$ is not $z$); K1 conditionally accepted as the next step. Both corrections are applied (advisory §4a). New result: the T-6c2 producer works in $\mathbb R^3$ and projects $s,c$ back to the plane each step. Without that projection, $1-K=12r^2\|s-c\|^2+\dots$ per block (`triad_v1_8_k1_lift_check.py`, PASS).
- **Second review:** ChatGPT, review `5748069400` on `4cbc9ce`: ACCEPT WITH CHANGE. C2/C3, C5 and C6 are narrowed (advisory *[review 2]*). Closure test (advisory §4b; `triad_v1_8_k1_closure_check.py`, PASS): the unprojected lift has no autonomous closure on $(Q_s,Q_c,I_{sc},\Omega,r,K)$; the direction of $w$ relative to the apex kick is extra state.
- **Third review:** ChatGPT, review `5748629780` on `b4bd90f`: ACCEPT WITH CHANGE. The non-closure result is confirmed, with the closed form $1-K_6=(\lambda+6)^2\Gamma+\dots$ Two statements are narrowed (advisory *[review 3]*): C3 is not supplied by the producer, and the sufficiency and minimality of the extra state are OPEN. The enlarged-state C3 closure search is approved as the next research step.
- **Fourth review:** ChatGPT, review `5748759219` on `2277de8`: ACCEPT SCOPED; the maintenance pass is closed. New results, checked by Claude (advisory §4c; `triad_v1_8_k1_cubic_jet_check.py`, PASS):
  - the block cubic jet $F^6(X)=X+6\mathcal L^{-1}G_3(X)+O(\|X\|^5)$;
  - $w$ is not sufficient, since the direction of $D_\parallel$ matters on the free state space;
  - an 8-coordinate $SO(B_T)$ quotient bounds the search from above.
- **Fifth review:** ChatGPT, review `5749141951` on `6e4ce70`: ACCEPT SCOPED. It gives the exact one-step $SO(B_T)$ quotient map $H'=\bar AHA^\top$, $t'=(I+M)t$ in the eight-coordinate chart $(q,H_{sc},H_{sd};a,b,d_z)$. Claude checked it (advisory §4d; `triad_v1_8_k1_quotient_check.py`, PASS). Dropping the phase of $H_{sd}$, or the sign of $d_z$, gives a representation that does not close. Smaller representations otherwise remain OPEN.
- **Sixth review:** ChatGPT, review `5749303513` on `9e0ac3f`: ACCEPT SCOPED. It gives deletion counterexamples for $a$, $b$ and $|H_{sd}|$. Claude reproduced them and added the deletions of $q$, $\operatorname{Re}H_{sc}$ and $\operatorname{Im}H_{sc}$ (advisory §4e; `triad_v1_8_k1_deletion_check.py`, PASS). None of the eight direct deletions closes, under the one-step map or at leading order of the block map. Combined or nonlinear smaller representations remain OPEN.
- **Seventh review:** ChatGPT, review `5749533518` on `fa833c8`: ACCEPT SCOPED, with all eight deletions independently recomputed. By co-owner decision this K1 research phase is closed (advisory §4e, §5). A smaller representation is to be sought only as a factor map that determines observables named in a T-6r contract. T-6r remains OPEN. Next in the cycle: T8-03 (tool PR first); T8-01 and T8-02 still wait for Genesis.

