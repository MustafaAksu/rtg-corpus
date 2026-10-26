# RTG_NUMBER_GENESIS_DSN v1.20 — Change Specification (pre-patch)

**Doc ID:** `NG_V120_CHANGE_SPEC_v1_1` · co-owner APPROVED 2026-09-25 with three tightenings, incorporated below · **Date:** 2026-09-25 · **Auditor:** Claude
**Base:** `RTG_NUMBER_GENESIS_DSN_v1_19.md`, sha256 `a58d150793cbf51a3761f7f850510dacddf8fde47d84652201038adc5e09343e`, 3127 lines, LF — **verified**.
**Companion:** `disc2_p2_antipodal_exposure_annotation_v1.json`, sha256 `43d28360…6b65d550` — **verified**; 136 records, `convention_exposed: 40 True / 96 False`, matching the exposure audit exactly.
**Scope rule:** v1.20 = scientific/source synchronization + Methodology v1.3 compliance **on touched blocks only**. The §2/§6 structural migration is a separate methodology-only pass. This document specifies; it does not patch.

---

## 0. v1.19 verification closed

**Provenance (patch base `e1efdd7e…` vs frozen `908786bb…`).** The only difference between those two v1.18 byte sets was one v1.18-changelog clause. v1.19 carries **neither** the stale clause nor my exact replacement — the bullet was reworded independently and correctly. No replay against `908786bb…` is needed; the concern is closed by inspection.

**Stale-state scan on v1.19:** `trivial for unary maps` 0 · `normal-form real-ray` 0 · `Mod-N completeness is not claimed` 0 · `differ from six-block indices only by` 0 · `vanishes identically` 1 — inside the C5 `[COR v1.19]` quoting the withdrawn wording, so **not live**. Clean as claimed.

## 1. Verification ledger of the co-owner assessment

| item | claim | check | verdict |
|---|---|---|---|
| **S1/S2** | `DYAD-THM-PRIM-CTR` exists; seed `(1/100, 1/250)` has `Q₀ = 19/250000 < 1/625`; NUMGEN listed as proposed consumer, acceptance pending | Dyadic v6.4.10 line 644 (RID, `[THM]`), line 677 (consumer, "acceptance pending"); `Q₀ = 10⁻⁴ − 4·10⁻⁵ + 1.6·10⁻⁵ = 7.6·10⁻⁵ = 19/250000` ✓ `< 1.6·10⁻³` ✓ | **confirmed** |
| **S2 corollary** | explicit tube fits the v1.19 injectivity box | `Q ≥ ½(ρ²+η²)`, so `Q < 2209/10⁶ ⟹ ρ²+η² < 0.004418 ⟹ \|ρ\|,\|η\| < 0.0665 < 0.1` — arithmetic verified; the `2209/10⁶` tube bound itself is owner-attributed | **confirmed (arithmetic); bound cited to owner** |
| **S3** | `37/40` (ray burst) and `47/54` (raw angular mean) are distinct objects; provenance resolved upstream | Dyadic v6.4.10 lines 44, 46, 414, 420, 422 — `[DEF]` "distinct objects; must not be conflated"; `[COR v6.4.10]` on the half-power term | **confirmed** |
| **S4** | chain identity `Δ^{AC}_{pu:qv} = v·Δ^{AB}_{p:q} + p·Δ^{BC}_{u:v}` exact | matches my C7C-M derivation (`v·e₁ + p·e₂`, `N_B` cancels) | **confirmed** |
| **S4 negative results** | `(A,B)·(B,A) = (A,A) ∉ R_pair` is a **closure counterexample** for the unrestricted rule, not merely an "inverse law fails later" remark; untyped WD-DOM fails | correct and sharper than my design memo's framing; adopted | **confirmed; supersedes my §4 wording** |
| **S4 associativity** | only "both bracketings admitted ⇒ same endpoint pair" is `[ALG]`; "one admitted ⇒ other admitted" unproved | correct refinement of my "free at realization level" | **accepted — my claim was one step too strong** |
| **S5** | `C_NG` "category" overloads the common home | consistent with S4: partial, interface-sensitive, no identities on the carrier | **agreed** |
| **S6** | live self-contradiction: ORD-2 reflection `[NUM-audited]` vs P3 `[ALG]` at v1.19 | line 2318 (live §6 mirror): reflection "tagged `[NUM-audited]` below, not asserted as ALG"; lines 2578/2673: P3 closed `[ALG]` | **confirmed — live contradiction** |
| **S7** | live self-contradiction: §7 proof package "mod-N completeness explicitly not claimed" vs §6.8 `ℤ_N` completeness certified | line 2535 (live §7): "mod-`N` completeness explicitly not claimed" | **confirmed — live contradiction** |
| **S8** | D15 no longer pending; OFN v0.8 inspected NUMGEN v1.19 NG-7A/NG-7B | line 2598 (live ledger): "OFN-side synchronization pending (D15)"; OFN v0.8 line 664: "inspected NUMGEN v1.19 NG-7A / NG-7B; RF-O08-10 records the additive result and fundamental-integral-cycle extension" | **confirmed — stale** |
| **G2–G4** | Methodology v1.3 requires exactly one canonical status with `[RESULT]`, `[import:]` grammar, alias table | Methodology v1.3 lines 297, 263–285, 423, 592–595 | **confirmed** |
| **P2** | no Discrete-owner antipodal policy yet; DISC state unchanged | consistent with all prior audits; annotation JSON matches | **confirmed** |

**One refinement to carry into the spec.** Line 2318 says the reflection direction is "tagged `[NUM-audited]` **below**" — so S6 has two touch points, the mirror paragraph and the referenced block beneath it, not one.

---

## 2. Section-by-section specification

### Header
- Bump to **v1.20**, date of patch.
- Add `Document class` / `Document status` / `Supersedes: v1.19` / `DSN Methodology: v1.3` / current companions (Programme v1.2, OFN v0.8, Dyadic v6.4.10, Discrete Genesis v2.12.13, RECOG v0.3.1).
- **Replace** the cumulative v0.4→v1.19 status narrative with a 2–4 sentence current state; move the narrative verbatim to Appendix A history.
- Add: *"This ledger does not itself constitute an OPEN-P1 physical bridge"* (Programme v1.2 SG-PROG-4 alignment).
- Add `## Local Tag Aliases` per Methodology v1.3 §592: `[INTERP] → [HEUR] [scope: interpretation]`; `[POSTHOC-DIAG] → [NUM] [scope: post-hoc diagnostic; non-admission evidence]`; `[MATH] → [THM] [scope: standard mathematical input]`. Declare `[REPRO]`, `[PROVENANCE]`, `[GUARD]` as **structural markers, not truth statuses**.

### §1.3 / §2 queue head / §8 mirror
- Queue head: **`C7C-M — interface-typed WD-DOM / partial-composition closure`** (not "C7C-M design"). §8 must mirror §2 verbatim, with the existing "mirrors §2" note retained.
- Sub-items listed under the head: full-interface typed WD-DOM `[OPEN]`; admissibility-transfer for associativity `[OPEN]`; identity/inverse on the physical carrier `[OPEN — fails on current carrier]`; M-4 realization search `[HOLD pending P2 Discrete-owner policy]`.

### N-1 / N-2-ORD (§2 block and §6 mirror) — **S2, S6**
- Add `[import: RTG_DYADIC_OSCILLATOR_DSN_v6.4.10 §… | DYAD-THM-PRIM-CTR]` as an **independent upstream explicit-domain certificate**: `U = {0 < Q ≤ 1/625}`, `U_T = ⋃_{j<6} T^j(U)`, contraction bounds for `Q ≤ 1/400`. Record NUMGEN's **consumer acceptance** (closes Dyadic line 677 "acceptance pending").
- Corollary `[ALG]`: canonical seed `(1/100, 1/250)`, `Q₀ = 19/250000 < 1/625`, lies in `U`. **Explicit-domain boundary CLOSED** for the N-1 / N-2-ORD tube-membership use of the long-horizon seed. Replace every live "no explicit radius places the seed in `U_T`" sentence.
- Corollary `[ALG]`: `U_T ⊂ {Q < 2209/10⁶}` (owner-attributed) and `Q ≥ ½(ρ²+η²)` give `|ρ|,|η| < 0.0665`, so the whole explicit tube sits inside the v1.19 injectivity box. N-1 / N-2-ORD may now be exhibited on a **named explicit tube**, not only a shrunken existential one.
- **Guard, verbatim:** seed ∈ certified tube ⇏ all GAP-LOCK angular hypotheses certified by Dyadic. Ownership of L1 remains NUMGEN; Dyadic is an independent strengthening.
- **S6 fix (two places):** line 2318 `[GUARD]` — reflection is `[ALG]` on the shrunken/explicit tube via P3; and the "below" block it references. Remove `[NUM-audited]` from live text.

### SG-NG-18 (§3) and the duplicate wording — **S3**
- Rewrite: *primitive ray burst (`37/40`, with `−5/24·Q^{5/2}`) ≠ raw fixed-radius angular mean (`47/54`) ≠ normalized-chart observable ≠ long-orbit backbone; only the leading `−Q²` transfers without an explicit representation/observable bridge.* Cite Dyadic v6.4.10 `[DEF]` line 422 and the two `[COR v6.4.10]`. Remove both live "provenance unresolved upstream" sentences.

### N5-C7C-M (§6) — **S4**
- New block, all `[ALG]`, no data:
  - **M-1A** exact chain identity `Δ^{AC}_{pu:qv} = v·Δ^{AB}_{p:q} + p·Δ^{BC}_{u:v}` — **CLOSED**.
  - **M-1B** conditional carrier closure on the **repaired domain** `D_chain = {((A,B),(B,C)) : both in R_bd; the three streams share one certified comparison context — the same triple comparison prefix domain, or a certified cofinal transport between the two prefix domains; (A,C) ∈ R_pair}` (symbolic equality of `B` is insufficient: M-1A combines two defects linearly on a common `H`) — the last condition is pre-bounded physical admissibility, **not** boundedness; boundedness then follows from M-1A and `ρ_Q(A,C) = ρ_Q(A,B)·ρ_Q(B,C)` **emerges** — **CLOSED**.
  - **Unrestricted WD-CLOSE: FAIL** — `x ∘ Sx = (A,A) ∉ R_pair` (closure counterexample, via C7C-0).
  - **Naive/global label-only WD-DOM: FAIL for `D_chain`** — the label-quotiented shared-middle domain is not saturated under `==_Q`. **Scoped:** this does not rule out a richer interface-typed saturated carrier; that is exactly the remaining OPEN.
  - **WD-VAL on admitted chains: PASS** `[ALG]`.
  - **Associativity:** `[ALG]` only as *both bracketings admitted ⇒ same endpoint pair*; admissibility transfer `[OPEN]`.
  - **Identity / inverse:** not available on the current chain carrier — the literal unit `(B,B)` and inverse composite `(A,A)` fail carrier closure; the C7C-0 reciprocal *label* theorem stands; enriched carrier OPEN.
  - **Physical commutativity:** OPEN (representation-level product commutes; domain swap-equivariance of the physical operation not established).
  - **Full-interface typed WD-DOM:** `[OPEN]` — the actual frontier.
- Register `NG_C7C_M_DESIGN_v1.md` as **historical**; a v2 / domain-repair certificate supersedes its "typed by `B` suffices" and "associativity free" statements. Module status: **partially resolved**, not "design not yet certified".

### `C_NG` common home (§4 / wherever "relational category" appears) — **S5**
- Replace with: *"`C_NG` is a typed relational architecture with partial physical composition. Certified sectors may carry stronger structure — `G_adm` groupoids, `M_T` endomorphism monoids, the N-2 group completion. No global category/groupoid structure is presumed across sector or birth/interface changes."* Do **not** weaken the sector-level structures that are actually certified.

### NG-7 (§7 proof package) — **S7**
- Line 2535: replace "mod-`N` completeness explicitly not claimed" with *"fundamental-integral-cycle completeness over `ℤ_N` is certified (§6.8); completeness for arbitrary nonprimitive/rescaled integer cycle-row presentations is not claimed."*

### Import ledger (§9.1) — **S8, G1, G4**
- Line 2598: D15 → **SYNC COMPLETE** (OFN v0.8 RF-O08-10); OFN whole target remains ACTIVE for physical source / non-Abelian / curvature. Add a one-line alignment note (OFN v0.8 quotient/presentation guards ↔ C7C-WD and P2). No load-bearing theorem import.
- Pointer refresh: Programme v1.1→v1.2, OFN v0.7→v0.8, Dyadic v6.4.9→v6.4.10. Convert every **touched** live import to `[import: SOURCE_vX.Y §… | RID]`; leave untouched historical `[source:]` records as migration inputs.
- **E1:** register known consumer `RECOG v0.3.1 / RECOG-ALG-LATTICE-CLOCK` against `NUMGEN-THM-N5AS1-DEFECT-THRESHOLD-RATIO`; note RECOG must repin from v1.15 at its next owner pass.
- **E2 (optional):** PRR / RRF as noncanonical working-methodology references under §9 provenance only — no theorem import, no `RRF-*` profile as canonical fact.

### Status tags on touched blocks — **G3**
- Every touched `[RESULT]` gets **exactly one** canonical source status. Normalize `[from: ALG/MATH]`, `[from: MATH/ALG]`, `[from: THM/ALG]`, `[from: NUM/ALG …]` in touched blocks only; list untouched occurrences in the changelog as migration debt for the structural pass.

### Appendix A / B / Changelog
- Appendix A: v1.20 epistemic status (explicit tube, C7C-M partial resolution, D15 complete, `C_NG` reframing).
- Appendix B: add `[REJECTED]` *"unrestricted chain composition is closed on `R_bd`"* and *"`C_NG` is a category"*.
- Changelog v1.20: S1–S8, G1–G4, E1, the two live-contradiction `[COR]`s, migration-debt list, and **P2: no scientific change**. v1.19 and earlier changelog text untouched.

## 3. Explicitly not changed
Ten-label lower bound; 136 frozen DISC-2 records with 40 `CONVENTION-EXPOSED`; C7C-0; GAP-LOCK 1–3; N-1/N-2/N-2-ORD ownership; NG-7A closure; N-6, N-4, NG-7B, full NG-8, C7B global breadth all OPEN; C7C-A not opened; M-4 HOLD; no NF-INV/NF-REM dependency without charted use; historical changelog wording.

## 4. Acceptance checks (to run after patch, before freeze)
Live-text zero hits for: `NUM-audited` · `explicitly not claimed` (mod-N context) · `pending (D15)` · `provenance unresolved upstream` · `no explicit radius` · `relational category` · `v6.4.9` / `v0.7` / `v1.1` as *current* pointers · `C7C-M design` as queue head. §2 and §8 heads identical. Every touched `[RESULT]` carries one status. Hash + LF + line count recorded; old owner bannered at supersession with successor verified present.

## 5. Sequencing (agreed)
1. v1.20 patch per §2 → freeze/audit.
2. Methodology-only structural migration (§2 compact OPEN registry, §6 authoritative ledger), zero scientific change → freeze/audit.
3. Consumer sync (RECOG repin, Dyadic consumer acceptance echoed upstream).
4. Only then: C7C-M interface-typed WD-DOM work, and M-4 once the Discrete owner rules on P2.
