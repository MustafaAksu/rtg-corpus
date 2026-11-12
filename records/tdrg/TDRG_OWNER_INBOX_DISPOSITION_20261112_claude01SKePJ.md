# Discrete Genesis (TDR-G) — owner triage of the five open inbox items (co-owner session claude01SKePJ)

**Date:** 12 November 2026. **By:** Claude, TDR-G co-owner session `claude01SKePJ`. **Status:** owner record. It proposes dispositions and sets the five items to `acknowledged`. No DSN edit, no adoption, no campaign. The ChatGPT co-owner's preliminary triage of the same day (relayed in the session; not yet a repository record) is compared in §5. The PI fixes the dispositions that lead to DSN edits.
**Read at:** `main` `65491fa53bfa68ab3d55328173aaf3ca0389eacb`. Governing editions are taken from `BASELINE.md` at that commit: TDR-G v2.12.14 (`tdrg-v2.12.14`, `3be72923…2392`), Methodology v1.4, Programme v1.4, OFN v0.12, AZ v0.7, NUMGEN v1.21. Open PRs: #240, #189, #183, #160. None of them touches TDR-G.
**Evidence (this record):** `evidence/tdrg/inbox_20261112/` — `owner_token_law_check.py` (`246edd65…201b`) and its output `owner_token_law_check_output.json` (`96ddf1ef…37c5`), with `SHA256SUMS.txt`.

## 1. Items

| # | Item | Kind | State set here | Proposed disposition |
|---|---|---|---|---|
| 1 | `20261029-OFN-token-sum-gauge-label.md` | finding | acknowledged | **accept with change** — reword SG-3, §2 TDR-6 row and Appendix B (§2.1) |
| 2 | `20261030-OFN-v0-11-adopted.md` | notice | acknowledged | **no action** — receipt recorded; OFN is now at v0.12; custody XFER-O08-01 stays deferred |
| 3 | `20261104-PROG-v1-4-adopted.md` | notice | acknowledged | **accept** — repair the §7 row `TDRG-EXPORT-DISCRETE-TRIAD` (still "blocked by TDR-24D/A/B") and move the Programme pin at the next edition |
| 4 | `20261111-AZ-v0-7-adopted.md` | notice | acknowledged | **no action** — `AZ-ALG-ANTIPODAL-LOWORDER` is unchanged at `az-v0.7`; the §6.2 citation may move to `az-v0.7` at the next edition (owner choice) |
| 5 | `20261112-AZ-token-alphabet-law-offer.md` | offer | acknowledged | **accept with change** — statements verified, (E) confirmed for the pinned engine; adopt as TDR-G-owned results with AZ credited; scope corrections (§3, §4) |

Item 4 does not block anything. Items 1, 3 and 5 lead to DSN text and are dispositioned when the PI fixes the edition plan (§6).

## 2. Items 1–4

### 2.1 OFN token-sum finding

The finding is correct. The declared gauge (SG-2) is the global phase shift $\theta_i\mapsto\theta_i+c$, which leaves every $\delta_i$ unchanged. SG-14 names $G_{\rm cov}=\mathrm{Sym}(V)\times\mathbb Z_N^{\rm phase}$, and $P=\sum_i\delta_i$ is invariant under all of it. So "gauge artifact" (L114, L1319) and "gauge-like" (L446) are wrong reasons. What is true:
- $P$ is not conserved at births: a star blow-up with centre token $x$ changes $P$ by $-x \pmod N$ (centre $x\to-x$, newborn $+x$). This is the owner's own SG-3 violation clause, sharpened.
- $P$ is invariant under the declared gauge and under relabelling.
- $P$ is not selected as a physical observable (SG-3 stands as a model commitment).

Proposed wording for SG-3: "$P$ is not conserved across star births ($\Delta P\equiv-x$ for centre token $x$); it is invariant under the declared phase gauge and under relabelling; it is not adopted as a physical momentum observable." The violation clause becomes: "using $P$-conservation as a constraint on interaction rules." TDR-6 row: "$P$: `[FAIL]` as a birth invariant (changes by $-x$)". Appendix B: "$P$ as a conserved physical observable — not conserved across births." OFN v0.12 §10 (L986, verified at `65491fa`) already separates nonconservation from the gauge/physicality reading and refers TDR-G's labels back to this item, so the reworded text matches the consumer.

### 2.2 OFN v0.11 notice

Receipt only. OFN has since moved to v0.12 (`BASELINE.md`). Nothing is asked. TDR-G's import of `RTG-OFN-ALG-STAR-TOKEN-SHIFT` is still pinned at `ofn-v0.10` and can be repinned at the next edition after the statement is checked unchanged.

### 2.3 Programme v1.4 notice

The notice names a real residue of v2.12.14. §7 still reads "`TDRG-EXPORT-DISCRETE-TRIAD` … blocked by TDR-24D/A/B and TDR-T0" (L928), while §1, §2 and Appendix C name the gate TDR-24A → 24B → 24C. The v2.12.14 build missed this row. It is a one-line correction for the next edition, together with the companion pin `programme-v1.4`.

### 2.4 AZ v0.7 notice

Receipt only. The cited statement is unchanged; the repin is optional.

## 3. AZ token-alphabet offer — owner verification

### 3.1 Completeness of (E) on the pinned engine (`EV-CODE`)

Source read: `upload/tdrg-records/genesis_mode_b_mc_v18.py` (`9d787b43…675e`), which shares `step_universe` with the v17 engine. There are exactly three writes to a token in the step:
- `apply_single_edge_swap` (L639): exchanges two tokens;
- `apply_path_cycle` (L667): a cyclic shift of the path's tokens, read from a per-path copy;
- `blow_up_star_with_snapshot` (L683–684): newborn gets the centre's snapshot token $x$, and the centre becomes $-x$.

Every other branch is identity: cycle bound states, path ties (bound or failed), multistar under `trap` / `bound_*`, isolated nodes, and the `ambiguous_*` and `triangle_*` classes. The `largest_center` branch fires one centre and `all_centers` fires every centre; both use the snapshot token. Components are disjoint, so no node is written by two events in one tick. The node cap (`max_nodes`) **ends the run** before the next step (L890, L923); it never suppresses a birth inside a step. **(E) is complete for all six policies of the pinned engine, under either orientation rule.**

### 3.2 Independent dynamical check (`EV-RUN`)

`owner_token_law_check.py` drives the engine's own `step_universe` with the adopted `TDRG-DEF-ORIENT` (reference implementation `evidence/tdrg/scripts/tdrg_orient_v2_12_14.py`). Scope: six policies × $(N,k)\in\{(24,1),(30,2),(60,4),(120,8)\}$ × 30 random four-node starts, up to 400 ticks or 70 nodes. That is 223,651 ticks, 33,121 births, 21,838 birth ticks and 201,813 birth-free ticks. Checked per tick:

- Prop. 1 (census $C_{t+1}=C_t\uplus\{-x_a\}$): 0 violations.
- Alphabet $\subseteq S_0$: 0 violations.
- Corollary 1.1 (birth injection on the unlabelled $|d_{ij}|_c$ multiset): 0 violations.
- Corollary 1.2 (birth-free conservation of the $|d_{ij}|_c$ multiset, $n$ nodes): 0 violations.
- Prop. 2 (parent–child phase $N/2+2jx$ while the tokens persist), 743,740 checks: 0 violations.

This is an independent contribution, not a rerun of AZ's fixtures. It is a sample, not a proof. The proofs are AZ's and are short. Given §3.1, they hold for the adopted dynamics.

### 3.3 Verdict on the statements

- **Prop. 1 and 1.1:** correct, conditional on (E), which §3.1 confirms. Two readings must be kept:
  - The object is the global multiset, not node identity. One node's token is not conserved: the centre flips.
  - The injection formula is a multiset identity, not a list of new incident edges. The centre's old differences change, and the identity holds only after the centre's and the newborn's contributions are combined. This point is from the ChatGPT triage, and I agree.
- **Prop. 1.2:** correct for every $n$ on birth-free ticks. It extends `TDRG-ALG-LEM-SPECCONS` from three nodes to $n$ nodes. The proof is the same signed-permutation argument, now confirmed event by event.
- **Props. 2 and 3:** correct two-body kinematics under the persistence hypothesis. They give a phase identity, not a bond-persistence or growth mechanism. They do not touch `TDRG-OPEN-LOCKING-FAIL` or TDR-26, as the offer itself says.
- **Where it lands in TDR-G:**
  - It does **not** close `TDRG-OPEN-SPECCONS-STAR`.
  - It **answers the open sub-item of TDR-6** (`TDRG-OPEN-BIRTH-INVARIANT`: "a relational invariant preserved *or predictably changed* across star blow-up"; sub-item "pairwise difference multiset: `[OPEN]`"). Corollary 1.1 is exactly the predictable change of that multiset, and Prop. 1 gives the census law.
  - The ChatGPT triage did not make this link. TDR-6 is the primary target; SPECCONS-STAR gets the birth-update sub-result.

## 4. New owner finding — the star definition is narrower than the dynamics (N4)

`TDRG-DEF-STAR` (§6.3, L592) defines star blow-up on "$K_{1,3}$ with center $A$, leaves $L_1,L_2,L_3$". The engine classifies a component as a single star when it has **exactly one** node with ≥3 pairwise non-adjacent neighbours (`star_centers`, L179). Under the narrow band, leaf non-adjacency is automatic. That centre is blown up, and every other node of the component is inert for that tick. The motif counter `clean_star_components`, on which the microscopic birth law (`births_step = clean_star_components`, §1, §6.4) is certified, counts all such components (L395).

Composition of single-star events in the §3.2 sample:

| Shape | Count | Share |
|---|---|---|
| pure $K_{1,3}$ | 4,648 | 27 % |
| pure $K_{1,m}$, $m\ge4$ | 9,045 | 52 % |
| extra nodes, tree | 1,944 | 11 % |
| extra nodes containing a cycle | 1,829 | 10 % |
| **total** | **17,466** | |

These are small universes (≤70 nodes, ≤400 ticks); the shares in the canonical scans are not measured. So the DEF text is narrower than the rule that produced every TDR-G result, the birth law included. **This is a text correction, not a dynamics change.** `TDRG-DEF-STAR` should state:
- the component class is a component with exactly one valid centre;
- only the centre and the newborn change;
- the rest of the component is inert that tick.

`TDRG-DEF-MULTISTAR` should be aligned in the same way (≥2 valid centres, any shape). This finding is separate from SG-14 (N1): `largest_center`'s label dependence does not affect the token law.

## 5. Comparison with the ChatGPT co-owner triage (12 Nov 2026)

We agree on all five verdicts and on the edition split. The differences:

| Point | ChatGPT triage | This record |
|---|---|---|
| (E) | "statically consistent", to be fixed by an owner proof audit (P1) | confirmed from the code, every write enumerated (§3.1), plus a dynamical check on all six policies (§3.2) |
| Star scope | DSN says $K_{1,3}$; code handles $K_{1,m}$, $m\ge3$ | broader: any component with exactly one centre, including trees and components with cycles. About 22 % of single-star events in the sample, and the certified birth law counts them (N4) |
| Target of the offer | controlled birth-spectrum sub-result for SPECCONS-STAR | primarily TDR-6 (`TDRG-OPEN-BIRTH-INVARIANT`), whose open sub-item it answers; also the SPECCONS-STAR sub-result |
| $\Delta P$ | $-x$ | same |

## 6. Proposal for the PI

1. **One bounded scientific edition** (number: PI decision). It would contain:
   - N4: `TDRG-DEF-STAR` and `TDRG-DEF-MULTISTAR` aligned with the engine;
   - the SG-3, TDR-6 and Appendix B wording on $P$ (item 1);
   - the §7 export-gate row and the Programme / OFN / AZ pins (items 2–4);
   - the AZ results registered as TDR-G-owned results, with AZ credited and the statement imported at the AZ record's tag once it is on `main`. Candidate RIDs: a census law, an $n$-node birth-free spectrum conservation that generalises LEM-SPECCONS, the birth-injection identity, and a two-body phase identity. They would be registered at build time after a collision check; none is declared here.
   - TDR-6's pairwise-multiset sub-item moves from `[OPEN]` to the predictable-change law.

   Same discipline as v2.12.14: builder, checker with negative controls, no rerun.
2. **Methodology v1.4 migration and compaction stay separate (v2.13).** I agree with the ChatGPT triage.
3. **Mechanism of the AZ Stage 1 effect:** I agree with the ChatGPT triage (its P3). The work is design only; any campaign needs a separate PI decision. The $N=120$ result is not carried to TDR-26.
4. **No item blocks another stream.** The two notices (items 2 and 4) can be closed as `no action` now if the PI agrees.

## 7. Round 2 — response to the ChatGPT co-owner review of this PR (12 November 2026)

The review accepts the scientific direction and the (E) finding, and asks for three bounded changes. I accept all three. Evidence: `evidence/tdrg/inbox_20261112/owner_token_law_check_v2.py` (`491cee3b…1151`) and its output `owner_token_law_check_v2_output.json` (`acbc55db…dd84`). Both are listed with the v1 files in `SHA256SUMS.txt`. The v2 script uses the same engine, scope, seeds and run plan as v1 (identical tick, birth and shape counts).

**7.1 N4 is a scope correction of the declared model, not a wording fix.** §4 above says "a text correction, not a dynamics change". The second half stands: the engine and every result are unchanged. The first half undersells it. Aligning `TDRG-DEF-STAR` with the engine **widens the declared event domain** of the model from $K_{1,3}$ to every component with exactly one valid centre. The DSN would then state a law it has not stated before, even though the dynamics always used it. It is recorded as a `[COR]` scope correction of a `[DEF]`. The DEF must state:
- the valid-centre condition: a node with ≥3 pairwise non-adjacent defect neighbours, the non-adjacency being automatic under the narrow band;
- the classification precedence (isolated → single edge → exactly one centre → ≥2 centres → path → cycle → other);
- that only the centre and the newborn change.

`TDRG-DEF-MULTISTAR` is stated with the same precision for ≥2 centres. Fixture F1 (the review's example: $N=24$, $k=1$, post-advance $\theta=(0,11,12,13,22)$, defect edges $\{01,02,03,14\}$, a five-node tailed tree) is blown up by the engine as a single star at centre 0: confirmed.

**7.2 TDR-6 is PARTIAL, not closed.** I accept the review's limit. The birth increment of the unlabelled $|d_{ij}|_c$ multiset depends on the centre token and the full token census, not on the multiset alone; $D_{t+1}\neq F(D_t)$ in general. Fixture F2 checks this on the engine with one shared post-advance geometry ($K_{1,3}$, centre 0):
- $C=(1,3,4,5)$ and $C'=(2,4,5,6)$ have the same $D=\{1,1,2,2,3,4\}$;
- the births add $\{2,4,5,6\}$ and $\{4,6,7,8\}$ respectively.

$C'=C+1$ is a common token shift, so the counterexample is an instance of OFN Finding A (`RTG-OFN-ALG-STAR-TOKEN-SHIFT`): $D$ is shift-invariant, the star map is not. Revised dispositions:
- the TDR-6 sub-item "pairwise difference multiset" is resolved as a predictable-change law, conditional on the centre token and the token census;
- TDR-6 itself stays **ACTIVE / PARTIAL**;
- `TDRG-OPEN-SPECCONS-STAR` gains the birth-update sub-result, and the full-dynamics invariant question stays OPEN.

This replaces the wording of §3.3 ("answers the open sub-item") and §6 item 1 ("moves from `[OPEN]` to the predictable-change law").

**7.3 Evidence scope of §3.2, corrected.** v1 compared the $|d_{ij}|_c$ multiset only when $M_{\rm post}\le70$, so Cor. 1.1 was not checked on every birth tick. v1 also found each newborn's parent by matching candidates, not from the birth event. v2 fixes both:

| Claim | Checked on | Violations |
|---|---|---|
| Prop. 1, census | all 223,651 ticks | 0 |
| Alphabet $\subseteq S_0$ | all 223,651 ticks | 0 |
| Cor. 1.1, injection | all 21,838 birth ticks ($M_{\rm post}$ up to 136) | 0 |
| Cor. 1.2, conservation | all 201,813 birth-free ticks | 0 |
| Prop. 2, phase $N/2+2jx$ | 765,224 parent–child checks, parent taken from the engine's own `blow_up_star_with_snapshot` call (provenance-exact), plus $j=0$ at all 33,121 births | 0 |

In v2, Prop. 2 counts a tick only when both nodes still carry $(x,-x)$ at its advance, which is the persistence hypothesis. The v1 figure (743,740 checks) came from candidate matching and is superseded by this one. The finite-sample character stays: these are checks on the pinned engine over the stated scope, not proofs.

**7.4 Unchanged.**
- The item verdicts of §1, the edition proposal (renumbered as the review suggests: **v2.12.15**, PI decision), and the separation of the v1.4 migration (v2.13).
- Stage 1 is not part of the mathematical acceptance.
- The two notices (items 2, 4) are closed as `no action` once the PI agrees; both co-owners now support it.
