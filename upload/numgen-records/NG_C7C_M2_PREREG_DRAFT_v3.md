> **[SUPERSEDED 2026-09-30] by NG_C7C_M2_PREREG_DRAFT_v4.md (germ witnesses, T-inv, corrected M2-2 right-end witness, G-bridge). Content without this banner hashes to 7f8ee6ec0b5611468d1ecf35509ba033d71917045e2d0a2ac494d75ecdb7c2f4.**

# C7C-M2 — Interface Object and Saturated WD-DOM · Preregistration DRAFT v3

**Doc ID:** `NG_C7C_M2_PREREG_DRAFT_v3` · supersedes `_v2` (`1abeced0…c390`) · **Date:** 2026-09-30
**Base:** frozen Number Genesis v1.20.6 (`2a51c4b1a8037105d75e68ea7f24c721a970ab5ec32c27e810139020ccb948c5`)
**Status:** DRAFT for freeze review. **No C7C-M2 scientific outcome has been evaluated and no case has been examined. M2-0, M2-1 and M2-2 are internal design lemmas** that make the instrument well-posed; they do not evaluate WD-DOM.
**Frontier (owner §6.6 N5-C7C-M):** full-interface typed WD-DOM. **Hard guard (v1.20.6 manifest):** interface equivalence is defined without reference to `rho_Q`.

**v2 → v3 (co-owner audit):** blocker 1 — the middle condition is bounded, not exact, so M-1A does not transfer verbatim and Π must know which transport it certifies → witness-typed domain (§5), transported identity **M2-1** (§6), value descent **M2-2** (§7). Blocker 2 — "owner-declared sector class" was not a single key → frozen key function `κ_b` and evidence registry (§4.3). Editorial: header wording; `~_a` proved separately; M2-0 transitivity made explicit; `φ` is a witness, not an interface component; audit table updated.

---

## 1. Carrier (owner §6.6, unchanged)

`R_pair` — certified co-realized ordered physical pairs `(A,B; domain, order, provenance)`. `R_bd ⊆ R_pair` — bounded at the reduced class. `rho_Q : R_bd → Q^bd`; `x ≡_Q x′ :⟺ rho_Q(x) = rho_Q(x′)`. Convention (owner L1639): `Δ^{AB}_{p:q}(H) := q N_A(H) − p N_B(H)` on the admissible common-order prefix poset (N5-C1).

## 2. Interface data and interface witnesses

**End interfaces (data).** For `x = (A,B)`: `𝔍^R(x) := (B, 𝒫_x, ι^R_x)` with `ι^R_x(H) = N_B(H)`. For `y = (B′,C)`: `𝔍^L(y) := (B′, 𝒫_y, ι^L_y)` with `ι^L_y(H) = N_{B′}(H)`. Here `𝒫_x` is the directed poset of finite admissible common-order prefixes of `x`'s sector (N5-C1). The left end `𝔍^L(x)` and right end `𝔍^R(y)` are defined symmetrically.

**Interface isomorphism (witness, M2 definition).** For `𝔍 = (B,𝒫,ι)`, `𝔍′ = (B′,𝒫′,ι′)`: an order isomorphism `φ : 𝒫_{≥H₀} → 𝒫′_{≥H₀′}` between cofinal principal tails with `c(φ) := sup_H |ι(H) − ι′(φH)| < ∞` — a **single-stream** bound. `φ` is a **morphism between two interfaces**, not a component of either. The owner's `D_chain` requires "a certified cofinal transport" without formalizing it; this is M2's preregistered formalization, not an inherited owner theorem.

**Outer admissibility (dependent variable).** For a witnessed chain `(x, φ, y)`, the **transported outer pair** is `(A, C)_φ`: `N_A` counted on `𝒫_x`, `N_C` counted along `φ`, i.e. `H ↦ (N_A(H), N_C(φH))` on the tail. Then
```text
Π(x, φ, y)  :⟺  (A, C)_φ ∈ R_pair
```
— co-realization, common-order and prefix-cofinal repeatability of the transported outer pair, **with the comparison context supplied by φ**. Π is never part of an interface or of any equivalence.

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

### 4.1 Lemma M2-0 — interface isomorphism is an equivalence `[ALG]`
*Reflexive:* `id`, `c = 0`. *Symmetric:* `φ⁻¹` with `c(φ⁻¹) = c(φ)`. *Transitive:* let `φ : 𝒫_{≥H₀} → 𝒫′_{≥H₀′}` and `ψ : 𝒫′_{≥G₀′} → 𝒫″_{≥G₀″}`. Since `𝒫′` is directed, choose `K ≥ H₀′, G₀′`. Then `K` lies in the image tail of `φ`; set `H_* := φ⁻¹(K)`. Because `φ` is an order isomorphism of tails, `φ⁻¹(𝒫′_{≥K}) = 𝒫_{≥H_*}`, a cofinal principal tail, and `ψ ∘ φ : 𝒫_{≥H_*} → 𝒫″_{≥ψ(K)}` is an order isomorphism of tails with `c(ψ∘φ) ≤ c(φ) + c(ψ)`. ∎

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
D̃_mid^L := { (x, φ, y) : x, y ∈ R_bd ,  φ : 𝔍^R(x) ~_L 𝔍^L(y) }
D̃_M2^L  := { (x, φ, y) ∈ D̃_mid^L : Π(x, φ, y) }
```
Π certifies the comparison context **of the specific witness φ**; the domain carries it. This preserves the owner's `D_chain` semantics — a middle comparison context plus outer `R_pair` admissibility — with both now explicit. Whether Π is independent of the choice of `φ` for fixed `(x,y)` is **not assumed**; it is part of what the test can reveal.

## 6. Lemma M2-1 — transported chain identity `[ALG]` (symbolically verified)

For `(x, φ, y) ∈ D̃_mid^L`, `x = (A,B)` at `p:q`, `y = (B′,C)` at `u:v`, and `ε_B(H) := N_{B′}(φH) − N_B(H)` with `|ε_B| ≤ c(φ)`:
```text
Δ^{AC,φ}_{pu:qv}(H)  :=  q v N_A(H) − p u N_C(φH)
                      =  v Δ^{AB}_{p:q}(H) + p Δ^{B′C}_{u:v}(φH) − p v ε_B(H) .
```
Hence `|Δ^{AC,φ}_{pu:qv}| ≤ v·sup|Δ^{AB}| + p·sup|Δ^{B′C}| + p v c(φ) < ∞` on the tail. At `B′ = B`, `φ = id`, `ε = 0` this is exactly owner M-1A. **Consequence:** if `Π(x, φ, y)`, then `(A, C)_φ ∈ R_bd` at class `pu:qv` — the bounded-transport analogue of M-1B, conditional on Π exactly as M-1B is conditional on `(A,C) ∈ R_pair`. The output label `red(pu, qv)` arises here and only here (WD-REP).

## 7. The test

**Canonical transport.** Given `(x, φ, y)`, `x ≈_L x′` with witnesses `(ψ^L_x, ψ^R_x)`, and `y ≈_L y′` with witnesses `(ψ^L_y, ψ^R_y)`, set
```text
φ′ := ψ^L_y ∘ φ ∘ (ψ^R_x)⁻¹ : 𝔍^R(x′) → 𝔍^L(y′) .
```

**WD-DOM(L).** For every `(x, φ, y) ∈ D̃_M2^L` and **every** choice of `x′, y′` and witnesses:
```text
(x′, φ′, y′) ∈ D̃_M2^L .
```
- **Middle leg — structural.** `φ′` is a composite of interface isomorphisms, hence an interface isomorphism by M2-0, and level keys are preserved by `≈_L`; so `(x′, φ′, y′) ∈ D̃_mid^L`.
- **Outer leg — the content.** `Π(x, φ, y) ⟹ Π(x′, φ′, y′)`.

**Why "every witness" and the canonical `φ′`.** Letting the replacement witness be chosen existentially after inspection would permit post-hoc witness shopping and could manufacture a PASS. The canonical transport is fixed by the given witnesses; quantifying over all of them makes the test falsifiable. A failure caused by witness choice is itself a finding: composition admissibility would then depend on the transport, not on the classes.

**Lemma M2-2 — value descent `[ALG]`.** If `(x, φ, y), (x′, φ′, y′) ∈ D̃_M2^L` with `φ′` canonical, the outputs `z = (A,C)_φ` and `z′ = (A′,C′)_{φ′}` satisfy `z ≈_L z′`. *Proof:* by M2-1 both labels are `red(pu, qv)`, and inputs with equal labels give equal outputs (owner C4 uniqueness of the reduced class); `z`'s left end is `𝔍^L(x)` and `z′`'s is `𝔍^L(x′)`, equivalent via `ψ^L_x`; the right ends are equivalent via `ψ^R_y`. ∎ So **WD-VAL(L) follows from WD-DOM(L) + M2-1 + C4** — the claim v2 made without justification, now proved.

## 8. Non-triviality — otherwise INCONCLUSIVE, never PASS
- **N1** `≈_L` identifies at least one pair of **physically distinct** realizations.
- **N2** there is at least one `(x, φ, y) ∈ D̃_M2^L` and some `x′ ≈_L x` with `x′ ≠ x`, or `y′ ≈_L y` with `y′ ≠ y`.

## 9. Evidential standards (fixed in advance)
- **PASS(L):** a proof of WD-DOM(L) for every witnessed chain and every witness choice, `[ALG]` or `[THM]` under K6, with certified N1/N2 instances.
- **FAIL(L):** one certified counterexample `(x, φ, y) ∈ D̃_M2^L`, `x′, y′`, witnesses, with `¬Π(x′, φ′, y′)`.
- **G-search:** existing certified records only; no new seed, trajectory, parameter sweep or event-policy retuning. M-4 stays HOLD pending the Discrete-owner P2 ruling.
- **G-P2:** P2-exposed DISC-2 witnesses (40/136) cannot alone decide a TDR-G PASS or FAIL. Decisive TDR-G cases come from P2-unexposed records, or carry a separate independence theorem or certificate.
- **G-sufficiency:** a DISC admission certificate is not an M2 certificate. A record counts only if `𝔍`, `κ_b`, the witness `φ`, and the provenance for `Π(x, φ, y)` can be reconstructed from it; otherwise **INCONCLUSIVE**.
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
- **Hard anti-circularity:** no `rho_Q`, `≡_Q`, `p:q`, `Δ_{p:q}` or derived quantity in `𝔍`, `φ`, `~_a`, `~_b`, `κ_b`, or `D̃_mid`; Π only in `D̃_M2`.
