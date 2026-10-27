# C7C-M2 — Interface Object and Saturated WD-DOM · Preregistration DRAFT v4

**Doc ID:** `NG_C7C_M2_PREREG_DRAFT_v4` · supersedes `_v3` (`7f8ee6ec…c2f4`) · **Date:** 2026-09-30
**Base:** frozen Number Genesis v1.20.6 (`2a51c4b1a8037105d75e68ea7f24c721a970ab5ec32c27e810139020ccb948c5`)
**Status:** DRAFT for freeze review. **No C7C-M2 scientific outcome has been evaluated and no case has been examined. M2-0, M2-1 and M2-2 are internal design lemmas** that make the instrument well-posed; they do not evaluate WD-DOM.
**Frontier (owner §6.6 N5-C7C-M):** full-interface typed WD-DOM. **Hard guard (v1.20.6 manifest):** interface equivalence is defined without reference to `rho_Q`.

**v3 → v4 (co-owner audit):** witnesses are **cofinal germs**, so the canonical transport `[φ′]` is independent of any common-tail choice (§2, §4.1); Π is defined on germs through a tail-invariance stipulation (§2); the M2-2 output-right witness is corrected to `(φ′)⁻¹ ∘ ψ^R_y ∘ φ` (§7); guard: `φ` aligns comparison contexts and does not establish co-realization (§2, §11). Approved and unchanged: M2-1, `κ_b` registry, witness-typed domains, WD-DOM/P2/evidence architecture.

**v2 → v3 (co-owner audit):** blocker 1 — the middle condition is bounded, not exact, so M-1A does not transfer verbatim and Π must know which transport it certifies → witness-typed domain (§5), transported identity **M2-1** (§6), value descent **M2-2** (§7). Blocker 2 — "owner-declared sector class" was not a single key → frozen key function `κ_b` and evidence registry (§4.3). Editorial: header wording; `~_a` proved separately; M2-0 transitivity made explicit; `φ` is a witness, not an interface component; audit table updated.

---

## 1. Carrier (owner §6.6, unchanged)

`R_pair` — certified co-realized ordered physical pairs `(A,B; domain, order, provenance)`. `R_bd ⊆ R_pair` — bounded at the reduced class. `rho_Q : R_bd → Q^bd`; `x ≡_Q x′ :⟺ rho_Q(x) = rho_Q(x′)`. Convention (owner L1639): `Δ^{AB}_{p:q}(H) := q N_A(H) − p N_B(H)` on the admissible common-order prefix poset (N5-C1).

## 2. Interface data and interface witnesses

**End interfaces (data).** For `x = (A,B)`: `𝔍^R(x) := (B, 𝒫_x, ι^R_x)` with `ι^R_x(H) = N_B(H)`. For `y = (B′,C)`: `𝔍^L(y) := (B′, 𝒫_y, ι^L_y)` with `ι^L_y(H) = N_{B′}(H)`. Here `𝒫_x` is the directed poset of finite admissible common-order prefixes of `x`'s sector (N5-C1). The left end `𝔍^L(x)` and right end `𝔍^R(y)` are defined symmetrically.

**Interface isomorphism (witness, M2 definition).** For `𝔍 = (B,𝒫,ι)`, `𝔍′ = (B′,𝒫′,ι′)`, a *tail representative* is an order isomorphism `φ : 𝒫_{≥H₀} → 𝒫′_{≥H₀′}` between cofinal principal tails with `c(φ) := sup_H |ι(H) − ι′(φH)| < ∞` — a **single-stream** bound. Two representatives are **tail-equivalent**, `φ ∼_tail φ₁`, iff they coincide on some common cofinal principal tail. An **interface witness** is a **germ** `[φ]` — a `∼_tail`-class containing a bounded representative. Boundedness is a germ property: restricting a representative to a further tail can only lower `c`, and two representatives that agree on a tail have the same values there. `[φ]` is a **morphism between two interfaces**, not a component of either. The owner's `D_chain` requires "a certified cofinal transport" without formalizing it; this is M2's preregistered formalization, not an inherited owner theorem.

**Outer admissibility (dependent variable).** For a witnessed chain `(x, [φ], y)`, the **transported outer pair** is `(A, C)_φ`: `N_A` counted on `𝒫_x`, `N_C` counted along a representative `φ`, i.e. `H ↦ (N_A(H), N_C(φH))` on its tail. Then
```text
Π(x, [φ], y)  :⟺  (A, C)_φ ∈ R_pair      for a representative φ of [φ]
```
— co-realization, common-order and prefix-cofinal repeatability of the transported outer pair, **with the comparison context supplied by the witness**. Π is never part of an interface or of any equivalence.

**T-inv — tail invariance (frozen stipulation).** Restricting a certified witness to a further cofinal tail does not change Π: co-realization and provenance are unchanged, and prefix-cofinal repeatability is a cofinal property (SG-NG-25; finite-origin invariance of boundedness is owner C2). Hence Π is well defined on germs, and no choice of common tail can change a PASS or FAIL.

**G-bridge — a witness is not a physical bridge.** `[φ]` only **aligns comparison contexts**; it does not itself establish physical co-realization of `A` and `C`. Π requires **independent certified `R_pair` provenance** for the transported outer pair.

## 3. `rho_Q`-independence audit

| object | built from | uses `rho_Q`, `≡_Q`, `p:q`, `Δ_{p:q}`, or `R_bd` membership? | verdict |
|---|---|---|---|
| `B`, `𝒫_x`, `ι` | event predicate; N5-C1 prefix poset; single-stream `N_B` | no | pre-`rho_Q` |
| interface isomorphism `φ` | tail order isomorphism; single-stream bound | no | pre-`rho_Q` |
| `~_a`, `~_b` (§4) | the rows above + the frozen key `κ_b` | no | pre-`rho_Q` |
| `κ_b` (§4.3) | schema, owner, sector, gauge, event, order semantics | no — labels, bounded classes and fates are forbidden keys | pre-`rho_Q` |
| `Π` | `R_pair` of the transported outer pair | no — `R_pair` is defined before boundedness | pre-`rho_Q`; **outside every equivalence** |

Rational data enters only (i) the carrier restriction to `R_bd`, (ii) the hypothesis `x ≡_Q x′` inside `≈_L`, and (iii) the *output* label via M2-1. **Watch item:** every bound on `N_B` stays single-stream.

## 4. Equivalences

### 4.1 Lemma M2-0 — germ calculus and equivalence `[ALG]`
*(i) `∼_tail` is an equivalence on representatives.* Reflexive and symmetric trivially; transitive because two common tails of a directed poset contain a common principal tail.
*(ii) Composition of germs is well defined.* Let `φ : 𝒫_{≥H₀} → 𝒫′_{≥H₀′}` and `ψ : 𝒫′_{≥G₀′} → 𝒫″_{≥G₀″}`. Since `𝒫′` is directed, choose `K ≥ H₀′, G₀′`; `K` lies in the image tail of `φ`; set `H_* := φ⁻¹(K)`. Because `φ` is an order isomorphism of tails, `φ⁻¹(𝒫′_{≥K}) = 𝒫_{≥H_*}`, and `ψ∘φ : 𝒫_{≥H_*} → 𝒫″_{≥ψ(K)}` is an order isomorphism of tails. A different admissible `K` yields a restriction of the same map, hence the **same germ**; replacing `φ, ψ` by tail-equivalent representatives changes the composite only off a common tail, hence again the same germ. So `[ψ]∘[φ] := [ψ∘φ]` is independent of all choices, and `c(ψ∘φ) ≤ c(φ) + c(ψ)` on the common tail.
*(iii) Inverses.* `[φ]⁻¹ := [φ⁻¹]`, well defined, with `c(φ⁻¹) = c(φ)`.
*(iv) Equivalence.* "There is a bounded interface witness `𝔍 → 𝔍′`" is reflexive (`[id]`), symmetric (iii) and transitive (ii). ∎

### 4.2 The two levels
- **Level a.** `𝔍 ~_a 𝔍′` iff `B = B′` is the **same certified stream in the same co-realized sector instance** and the witness is the identity on a common tail of that one prefix poset. *Equivalence:* "same stream in the same instance" is an equality of instance-level keys, hence reflexive, symmetric and transitive; common tails of one directed poset are closed under intersection up to a common principal tail; identities compose to identities. ∎
- **Level b.** `𝔍 ~_b 𝔍′` iff `κ_b(B) = κ_b(B′)` (§4.3) **and** an interface isomorphism exists. *Equivalence:* equality of a frozen key is an equivalence, and by M2-0 so is "an interface isomorphism exists"; their conjunction is an equivalence. ∎

`~_a ⊆ ~_b`.

### 4.3 Frozen level-b key `κ_b` and evidence registry
```text
κ_b(B) := ( schema key , owner file + version + hash , sector-class key ,
            gauge policy , orientation/event semantics , common-order semantics )
B ≡_type B′  :⟺  κ_b(B) = κ_b(B′)      (exact tuple equality)
```
Orbit, seed, initial condition and realization identity are **not** components: level b deliberately varies them. **Forbidden as components:** `rho_Q`, any rational label or bounded class, any dynamic fate or PASS/FAIL outcome, a bare name or symbol, any seed-registry or panel identity.

**Registry of admissible evidence families.** The existing predicates carry no RIDs, so schema and sector keys are **frozen here** and pinned to their defining text.

| family | schema key(s) | defining text | sector-class key | gauge | orientation/event semantics | common-order semantics |
|---|---|---|---|---|---|---|
| continuous dyad | `M2-SCHEMA-DYAD-BPLUS`, `M2-SCHEMA-DYAD-BMINUS` | Number Genesis v1.20.6 (`2a51c4b1…48c5`) §6.6 N5-PHYS-1 `[DEF]` (phase-coincidence predicates) | `DYAD-THM-PRIM-CTR` tube `U_T` (Dyadic v6.4.10 §6.14) | one-chart gauge-reduced `(ρ,η)` | sign of the relational radial observable `ρ` separates `B_+`/`B_-` (N5-PHYS-1 gauge audit) | primitive-map orbit order; prefix-cofinal extension (SG-NG-25) |
| TDR-G | `M2-SCHEMA-TDRG-SWAP`, `M2-SCHEMA-TDRG-P3` | owner `genesis_mode_b_mc_v18.py` pinned `9d787b43…675e`; SWAP/P3 counters `dn_swap`, `dn_P3` | `M2-SECTOR-TDRG-N24K1` := (v18 @ `9d787b43…675e`, `N = 24`, three-node Mode-B, `k = 1`, `signed_centered ∈ (−N/2, N/2]`, IC sign `d_AB^IC = −d`) — as recorded in the DISC-2 `[REPRO]` contract | global-phase quotient; cycle key in the gauge-reduced 4-tuple | SWAP/P3 token semantics of v18 | deterministic update order; prefix-cofinal extension |

A frozen record whose `κ_b` cannot be reconstructed from its provenance yields **INCONCLUSIVE** (G-sufficiency). Adding a family, or changing any key's granularity, requires a new preregistration version.

### 4.4 Witnessed typed equivalence on pairs
`x ≈_L x′` with **witnesses** `(ψ^L, ψ^R)` iff `x ≡_Q x′`, `ψ^L : 𝔍^L(x) ~_L 𝔍^L(x′)`, and `ψ^R : 𝔍^R(x) ~_L 𝔍^R(x′)`.

## 5. Witness-typed domains

```text
D̃_mid^L := { (x, [φ], y) : x, y ∈ R_bd ,  [φ] : 𝔍^R(x) ~_L 𝔍^L(y) }
D̃_M2^L  := { (x, [φ], y) ∈ D̃_mid^L : Π(x, [φ], y) }
```
Π certifies the comparison context **of the specific witness germ `[φ]`**; the domain carries it. This preserves the owner's `D_chain` semantics — a middle comparison context plus outer `R_pair` admissibility — with both now explicit. Whether Π is independent of the choice of germ `[φ]` for fixed `(x,y)` is **not assumed**; it is part of what the test can reveal.

## 6. Lemma M2-1 — transported chain identity `[ALG]` (symbolically verified)

For `(x, [φ], y) ∈ D̃_mid^L` and any bounded representative `φ` of `[φ]`, `x = (A,B)` at `p:q`, `y = (B′,C)` at `u:v`, and `ε_B(H) := N_{B′}(φH) − N_B(H)` with `|ε_B| ≤ c(φ)`:
```text
Δ^{AC,φ}_{pu:qv}(H)  :=  q v N_A(H) − p u N_C(φH)
                      =  v Δ^{AB}_{p:q}(H) + p Δ^{B′C}_{u:v}(φH) − p v ε_B(H) .
```
Hence `|Δ^{AC,φ}_{pu:qv}| ≤ v·sup|Δ^{AB}| + p·sup|Δ^{B′C}| + p v c(φ) < ∞` on the tail. At `B′ = B`, `φ = id`, `ε = 0` this is exactly owner M-1A. **Consequence (germ-invariant: both sides are tail properties):** if `Π(x, [φ], y)`, then `(A, C)_φ ∈ R_bd` at class `pu:qv` — the bounded-transport analogue of M-1B, conditional on Π exactly as M-1B is conditional on `(A,C) ∈ R_pair`. The output label `red(pu, qv)` arises here and only here (WD-REP).

## 7. The test

**Canonical transport.** Given `(x, [φ], y)`, `x ≈_L x′` with witness germs `([ψ^L_x], [ψ^R_x])`, and `y ≈_L y′` with witness germs `([ψ^L_y], [ψ^R_y])`, set
```text
[φ′] := [ψ^L_y] ∘ [φ] ∘ [ψ^R_x]⁻¹ : 𝔍^R(x′) → 𝔍^L(y′) .
```
By M2-0 (ii)–(iii) this germ is **canonical**: it does not depend on any common-tail choice.

**WD-DOM(L).** For every `(x, [φ], y) ∈ D̃_M2^L` and **every** choice of `x′, y′` and witness germs:
```text
(x′, [φ′], y′) ∈ D̃_M2^L .
```
- **Middle leg — structural.** `[φ′]` is a composite of bounded witness germs, hence a bounded witness germ by M2-0, and level keys are preserved by `≈_L`; so `(x′, [φ′], y′) ∈ D̃_mid^L`.
- **Outer leg — the content.** `Π(x, [φ], y) ⟹ Π(x′, [φ′], y′)`.

**Why "every witness" and the canonical `φ′`.** Letting the replacement witness be chosen existentially after inspection would permit post-hoc witness shopping and could manufacture a PASS. The canonical transport is fixed by the given witnesses; quantifying over all of them makes the test falsifiable. A failure caused by witness choice is itself a finding: composition admissibility would then depend on the transport, not on the classes.

**Lemma M2-2 — value descent `[ALG]`.** If `(x, [φ], y), (x′, [φ′], y′) ∈ D̃_M2^L` with `[φ′]` canonical, the outputs `z = (A,C)_φ` and `z′ = (A′,C′)_{φ′}` satisfy `z ≈_L z′`, with explicit witnesses:
- **Label.** By M2-1 both outputs are bounded at `pu:qv` with equal inputs' labels, so both have the reduced label `red(pu, qv)` (owner C4: the reduced class is unique).
- **Left end.** `z`'s left interface is `(A, 𝒫_x, N_A) = 𝔍^L(x)` and `z′`'s is `𝔍^L(x′)`; witness `χ_L := [ψ^L_x]`.
- **Right end.** `z`'s right interface lives on `𝒫_x` as `(C, 𝒫_x, H ↦ N_C(φH))`, and `z′`'s on `𝒫_{x′}` as `(C′, 𝒫_{x′}, H′ ↦ N_{C′}(φ′H′))`. `[ψ^R_y]` maps `𝒫_y → 𝒫_{y′}` and is **not** itself a map between these; the witness is the conjugate
```text
χ_R := [φ′]⁻¹ ∘ [ψ^R_y] ∘ [φ] : 𝒫_x → 𝒫_{x′} ,
```
since `φ′∘χ_R = ψ^R_y∘φ` on a tail gives `N_{C′}(φ′χ_R H) = N_{C′}(ψ^R_y φH) = N_C(φH) + O(1)` by the bound of `ψ^R_y`. Level keys are those of `C` and `C′`, equal because `y ≈_L y′`.
∎ So **WD-VAL(L) follows from WD-DOM(L) + M2-1 + output-interface transport** — the claim v2 made without justification, proved here with the corrected right-end witness. *Note:* `ψ^L_y` and `ψ^R_y` both act `𝒫_y → 𝒫_{y′}` but may be different maps, so in general `χ_R ≠ [ψ^R_x]`.

## 8. Non-triviality — otherwise INCONCLUSIVE, never PASS
- **N1** `≈_L` identifies at least one pair of **physically distinct** realizations.
- **N2** there is at least one `(x, [φ], y) ∈ D̃_M2^L` and some `x′ ≈_L x` with `x′ ≠ x`, or `y′ ≈_L y` with `y′ ≠ y`.

## 9. Evidential standards (fixed in advance)
- **PASS(L):** a proof of WD-DOM(L) for every witnessed chain and every witness choice, `[ALG]` or `[THM]` under K6, with certified N1/N2 instances.
- **FAIL(L):** one certified counterexample `(x, [φ], y) ∈ D̃_M2^L`, `x′, y′`, witness germs, with `¬Π(x′, [φ′], y′)`.
- **G-search:** existing certified records only; no new seed, trajectory, parameter sweep or event-policy retuning. M-4 stays HOLD pending the Discrete-owner P2 ruling.
- **G-P2:** P2-exposed DISC-2 witnesses (40/136) cannot alone decide a TDR-G PASS or FAIL. Decisive TDR-G cases come from P2-unexposed records, or carry a separate independence theorem or certificate.
- **G-sufficiency:** a DISC admission certificate is not an M2 certificate. A record counts only if `𝔍`, `κ_b`, a representative of the witness germ `[φ]`, and the provenance for `Π(x, [φ], y)` can be reconstructed from it; otherwise **INCONCLUSIVE**.
- **Freeze rule:** everything in §§2–9 is frozen with this preregistration. Any change after a case has been examined is a new version, and the earlier verdict is retained.

## 10. Reading matrix
`~_a ⊆ ~_b` gives `FAIL(a) ⇒ FAIL(b)`; and PASS(a) supplies N1/N2 instances at level b, so PASS(a) excludes INCONCLUSIVE(b).

| level a | level b | reading |
|---|---|---|
| PASS | PASS | interface-typed quotient **across sector instances**; a quotient-level multiplication candidate is legitimate |
| PASS | FAIL | composition is **sector-internal** |
| FAIL | FAIL *(forced)* | composition is realization-specific even for a literally shared stream |
| INCONCLUSIVE | PASS | no distinct level-a representatives; a cross-instance typed quotient exists |
| INCONCLUSIVE | FAIL | no non-trivial level-a instance; outer admissibility does not descend across instances |
| INCONCLUSIVE | INCONCLUSIVE | no instance at either level; report, do not upgrade |

Excluded: FAIL(a) with PASS or INCONCLUSIVE(b); PASS(a) with INCONCLUSIVE(b). A report outside this table signals an analysis error. No row is the favoured outcome.

## 11. Guards
- **WD-REP:** `pu/qv` defines neither an interface, a witness, a domain, nor Π; it appears only as the output label in M2-1.
- **No law inflation:** associativity-transfer, identities, inverses, commutativity and C7C-A addition are not part of PASS; they remain separate downstream obligations.
- **K1–K6** (v1.20.6) grade any resulting claim. M2-1 is an `[ALG]` identity proved here; entering it into the owner ledger is a separate owner decision.
- **Hard anti-circularity:** no `rho_Q`, `≡_Q`, `p:q`, `Δ_{p:q}` or derived quantity in `𝔍`, `[φ]`, `~_a`, `~_b`, `κ_b`, or `D̃_mid`; Π only in `D̃_M2`.
- **G-bridge:** a witness germ aligns comparison contexts only; physical co-realization of the outer pair needs independent certified `R_pair` provenance (§2).
- **T-inv:** Π is evaluated on germs; tail restriction never changes a verdict (§2).
