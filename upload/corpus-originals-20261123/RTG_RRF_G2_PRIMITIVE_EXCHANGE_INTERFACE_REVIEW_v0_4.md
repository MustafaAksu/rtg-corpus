# RRF — G2 Primitive Exchange Realization: submersion, local odd-carrier equivalence, and factor guard

**Record:** RRF-G2-INTERFACE-REVIEW-v0.4 (ACCEPT SCOPED; noncanonical; 19 October 2026)  
**Date:** 2026-10-19  
**Status:** `[SESSION] ACCEPT SCOPED — NONCANONICAL G2 v0.4; adopted DYAD v6.4.13 smooth clock/root results; physical realization OPEN`  
**Registry impact:** Supplement to `RRF-CND-01`; no new physical realization. RRF v0.8.3 is separately adopted as a working representation standard, not scientific adoption of this G2 interface or physical realization.  
**Owner source inspected:** `RTG_DYADIC_OSCILLATOR_DSN_v6_4_13.md`, ADOPTED 18 Oct 2026; §§2, 6.15–6.17 and outbound N9; SHA-256 `5958f7fe8a3e0ec94546cb7e915c5f690d09827a3d680d13a17c9d880b968542`. Baseline: accepted G2 v0.3 (unchanged) and adopted RRF v0.8.2. Historical source/version metadata remains in the v0.3 record and in §8 below.  
**Evidence boundary (v0.4 review):** Adopted DYAD v6.4.13 §6.17 Lemma F and F1–F3 were directly read, not independently certificate-rerun here. OPEN 20 B-an, B-6 and B-∞ **existence** remain open; B-∞ flat uniqueness is CLOSED. Physical G2 factor/encoding is not selected.

## 1. [ALG / SESSION] Quotient involution by a submersion

Let `X_0` be a relevant open domain of the full configuration manifold, let `E:X_0→U` be a surjective `C^r` submersion (`r≥1`), with `U:=E(X_0)`, and assume a `C^r` involution `σ:X_0→X_0` which is **fiber-preserving**:

\[
E(x)=E(y)\quad\Longrightarrow\quad E(\sigma x)=E(\sigma y)
\qquad(x,y\in X_0).
\]

Define `R(E x)=E(σx)`. This is well-defined; local `C^r` sections of the submersion give `R=Eσι`, independently of the choice of section, with `RE=Eσ`. Because `σ²=id` and `U=E(X_0)`, `R²=id` throughout the induced domain `U`. If `F:X_0→X_0` and `T:U→U` satisfy `σF=Fσ` and `EF=TE` on the same compatible domain, then `RT=TR` on `U`. Restrictions to smaller local domains require all composites and fiber comparisons to remain defined; stating only a local section without global fiber compatibility does not prove global descent.

## 2. [ALG / SESSION] Local identity-versus-minus-identity lemma

**Proposed formal statement (not a new adopted owner RID).** Let `T` be the fixed RTG dyadic primitive germ

\[
T(\rho,\eta)=(\rho-\sin\eta,\,\eta+e^\rho-1-\sin\eta).
\]

Let `R` be a `C¹` local involution on an `R`-invariant neighborhood `U` of `0`, with `RT=TR` wherever compositions are defined. Assume `U` lies within an isolating neighborhood in which `0` is the *only* fixed point of `T` (or at minimum that `R(0)` lies in that isolating neighborhood). Then:

1. `T(R(0))=R(T(0))=R(0)`; by isolated fixed-point uniqueness, `R(0)=0`.
2. `A=DT(0)=[[1,-1],[1,0]]`, with characteristic polynomial `λ²−λ+1`. Differentiation gives `L=DR(0)` commuting with `A`, and `L²=I`. The real centralizer of `A` is `R[A]≅C` (since the polynomial is irreducible over `R`). Its only square roots of the identity are `L=I` and `L=−I`.
3. If `L=I`, define `H_+(x)=(x+R(x))/2`. Then `DH_+(0)=I`, so `H_+` is locally injective by the inverse-function theorem; and `H_+(R(x))=H_+(x)`. Thus `R(x)=x` on some neighborhood of `0`.
4. If `L=−I`, define `H_-(x)=(x−R(x))/2`. Then `DH_-(0)=I`, and `H_-(R(x))=−H_-(x)` locally. This also gives a direct `C¹` local conjugacy to `−I`; the lemma itself does not imply a physical gauge choice.

**Exact scope of the acceptance gate:** `R` must be **nonidentity as a germ at `0`**, i.e. `R` is not the identity on *any* neighborhood of `0`. Merely writing global `R≠id` is insufficient: an action may be identity in the origin neighborhood and act elsewhere. Under the stated hypotheses, nonidentity germ is equivalent to `DR(0)=−I`.

**Origin caveat:** An arbitrary local involution commuting with `T` need not send `0` to itself if it is allowed to exchange `0` with a different fixed point outside the chosen isolating region. `R(0)=0` becomes automatic only with the stated image/domain restriction. The primitive `T` has fixed points `(0,kπ)` **(rep: RRF-DYAD-LIFT)**; sufficiently close to `(0,0)` the fixed point is unique. This lifted-plane statement must not omit the additional winding fixed points of the wrapped-cylinder representation (rep: RRF-DYAD-WRAPPED).

**Regularity caveat:** The local dichotomy and local linearization of a `C¹` involution use only the `C¹` inverse function theorem. No all-order Taylor series is defined for a finite `C^r` germ. The **owner-adopted** formal uniqueness in DYAD v6.4.12 §6.16 implies `j^∞ R=R_0=Ŝ_form` for `C^∞` or analytic `R` with `DR(0)=−I`; for finite `C^r`, comparisons are limited to available jets and any needed normalization assumptions.

## 3. [OPEN] Primitive edge factor is a strong independent hypothesis

The condition `EF=TE` means that the edge encoding is an **autonomous dynamical factor** of the full physical update. It is independent of the exchange fiber-locality condition. Neither the existence of `R` nor `RE=Eσ` entails `EF=TE`. An interacting network can possess a well-defined induced exchange on edges and nevertheless lack an isolated-dyad factor because an edge successor depends on other network variables. **Failure of `EF=TE` does not by itself show exchange nonlocality or invalidate full-state exchange symmetry; it makes this narrow G2 contract inapplicable.** Conversely, some interactions could cancel on a factor, so interaction alone does not prove failure.

Illustration only (not RTG): take `E(x,y)=x`, `σ(x,y)=(-x,y)`, `F(x,y)=(x(1+y),y)` in a compatible local region. `σF=Fσ` and `Eσ=-E` (edge-exchange descent holds), but there is no single `T(x)` with `EF=T E` when `y` is free. Thus the factor and locality gates are logically separate.

`RRF-CND-01` remains the broader complete-configuration admissibility interface. G2 only applies to an **isolated-edge or autonomously factored primitive** realization. A six-step-only factor `EF=T⁶E` yields `RT⁶=T⁶R`, **not the primitive factor hypothesis** `EF=TE`. Although `DT⁶(0)=I` makes the first-order commutant test vacuous, the **owner-adopted cubic return** restores `DR(0)∈{±I}` for six-step `C³` involutions under DYAD §6.15(b) (RID: `DYAD-THM-LOCAL-INVOLUTION-GERM`). For a nonidentity **analytic** six-step involution, the adopted Corollary A implies `RT=TR` exactly in the prescribed germ/domain; for an **existing C^∞** six-step involution, owner DYAD v6.4.13 §6.17 F1 proves **exact** `RT=TR` under its local hypotheses; F2 proves uniqueness, and F3 proves commutation/uniqueness of existing smooth tangent-identity roots. Existence is OPEN 20 B-∞, while B-an and B-6 remain OPEN. Finite C^r clocks are not upgraded. The separate **network factor contracts** `EF=TE` and `EF=T⁶E` remain inequivalent. `[import: DYAD v6.4.13 §6.17; RID: DYAD-CAND-SMOOTH-CENTRALIZER-COROLLARIES]`

## 4. [ALG / SESSION] G2-PRE: local odd-carrier existence test

**Scope:** mathematical germ of the isolated primitive `T` at `0`, with `r∈ℕ_{≥1}∪{∞,ω}` (`C^ω` means real analytic), no selected physical network realization. Fix a sufficiently small invariant/composition-compatible domain and `C^r` local diffeomorphisms taking `0` to `0`. A *local odd chart* is a `C^r` chart `Φ` for which `\widetilde T=Φ∘T∘Φ^{-1}` satisfies `\widetilde T(-y)=-\widetilde T(y)` wherever both sides are defined.

**Forward implication (nonidentity primitive involution → odd chart).** Suppose a `C^r` involution `R` has `R(0)=0`, `RT=TR`, and its germ at `0` is not the identity. By §2, `DR(0)=−I`. Set

\[
\Phi=H_-:=\tfrac12(\mathrm{id}-R).
\]

Since `DΦ(0)=I`, `Φ` is a local `C^r` diffeomorphism; `ΦR=-Φ`. Then

\[
\widetilde T(-\Phi(x))=\Phi(T(Rx))=\Phi(R(Tx))=-\Phi(Tx)=-\widetilde T(\Phi(x)).
\]

**Reverse implication (odd chart → nonidentity primitive involution).** For any such `C^r` odd chart `Φ`, take the local involution

\[
R=\Phi^{-1}\circ(-I)\circ\Phi.
\]

It satisfies `R²=I`, `RT=TR`, `R(0)=0`, `DR(0)=−I`, and therefore has nonidentity origin germ.

Thus **the mathematical existence gate**, and only that gate, admits the equivalence

\[
\boxed{\text{local nonidentity }C^r\text{ involution commuting with }T
\quad\Longleftrightarrow\quad
\text{local }C^r\text{ odd chart for }T,\quad r\in\mathbb N_{\ge1}\cup\{\infty,\omega\}.}
\]

**C∞ / analytic existence bridge (algebraic consequence of owner theorem + elementary G2 averaging).** `[ALG] [scope: local germ, existence equivalence only; no physical realization] [import: DYAD v6.4.13 §6.17; RID: DYAD-CAND-SMOOTH-CENTRALIZER-COROLLARIES]` Let `F=T⁶` and let the category be either C∞ or analytic Cω. If an odd chart for primitive `T` exists, its induced nonidentity involution `R` commutes with `T`, and `Q=T³R` is a same-class tangent-to-identity root `Q²=F`. Conversely, if `Q²=F`, `DQ(0)=I` exists in that class, F3 guarantees exact `QT=TQ` (analytic maps form a C∞ subclass); `R=T³Q^{-1}` is a same-class nonidentity involution commuting with `T`, and `H_-=(id-R)/2` gives a same-class odd chart. Hence

\[
\boxed{\text{local C∞ (or Cω) odd chart for }T\iff\text{local same-class }Q:\ Q^2=F,\ DQ(0)=I.}
\]

The equivalence is an **algebraic consequence** of adopted DYAD v6.4.13 F3 plus the G2 chart lemma, not a proof that either side exists and not a claim that DYAD independently adopted RRF's phrasing as a standalone theorem. Owner OPEN 20 (B-an/B-∞ existence) remains `[OPEN]` `[import: DYAD v6.4.13 §2; RID: DYAD-OPEN-INVOLUTION-REALIZATION]`. OPEN 20 B-6 separately asks for a sixth root and exact ℤ₆ chart; B-6 is stronger than B-an. No physical network realization follows.

**Guard:** This does **not** assert `G2-PRE ⇔ full G2`. The full realization still requires a physical `X_0,σ,F,E`, valid submersion and fiber descent, `EF=TE`, primitive-clock exchange covariance, domain admissibility and a selected regularity class. A negative odd-chart existence result in a given class excludes full G2 realizations *in that class* under these conditions; a positive result merely opens that mathematical gate and does not provide an admissible network encoding.

**Class preservation:** The averaging chart `H_-=(id-R)/2` has the same `C^r` regularity as `R`, and the inverse and compositions in `R=Φ^{-1}(-I)Φ` preserve that class locally, including `C^ω` (real-analytic). The equivalence is therefore valid class-by-class for `r∈ℕ_{≥1}∪{∞,ω}`. This is an equivalence of **existence questions** and does not assert existence in any class. **Regularity / provenance:** `C^∞` odd-chart existence is a distinct question from analytic odd-chart existence; their respective *existence equivalences* with same-class square roots use adopted v6.4.13 F3 but do not assert any root exists. VF-1 excludes all-order oddness only for the **fixed registered finite `h_6` chart**; it is no obstruction to the existence of another odd chart. No new odd-chart existence proof or formal G1 owner certificate was supplied or run here.

## 5. Proposed G2 gate ledger [DEF / OPEN]

| Gate | Declaration or test | Status |
|---|---|---|
| **G2-ID/DOM** | Complete physical `X_0`, physical node exchange `σ²=id`, `U=E(X_0)`; relevant domains invariant and all fiber comparisons valid | `[OPEN]` owner selection |
| **G2-CLOCK** | Primitive full-state update `F` with `σF=Fσ`; **not** solely six-step covariance | `[OPEN]` owner selection |
| **G2-ENC/LOCAL** | `E:X_0→U` surjective `C^r` submersion and `E(x)=E(y)⇒Eσx=Eσy` | `[OPEN]` realization audit |
| **G2-FACTOR** | Primitive isolated-dyad autonomy `EF=TE` on domain; separate from edge exchange locality | `[OPEN]` model audit |
| **G2-ORIGIN** | `0` an isolated `T` fixed point and induced `R` stays in its isolating region | `[OPEN]` domain/action audit |
| **G2-PRE (DYAD)** | A local `C^r` odd chart for primitive `T` exists (`r∈ℕ_{≥1}∪{∞,ω}`); C∞ and analytic subquestions each equivalent to a same-class tangent-to-identity square root of `F=T⁶` (under adopted owner F3); B-6 is separate | `[OPEN]` owner DYAD OPEN 20 (B-an, B-6, B-∞ existence); B-∞ flat uniqueness CLOSED |
| **G2-NONTRIV** | The **germ** of the physically induced `R` at `0` is nonidentity; then `DR(0)=−I` by lemma; G2-PRE alone does not provide this induced action | `[OPEN]` physical action audit |
| **G2-REG** | Declare `r∈ℕ_{≥1}∪{∞,ω}` explicitly (finite `C^r`, `C^∞`, or analytic `C^ω`); §4 preserves the class in both directions; do not conflate smooth and analytic Problem B | `[OPEN]` realization audit |

**Conditional payoff:** Passing the local hypotheses gives a well-defined `C^r` induced involution commuting with primitive `T`. Its germ is either the identity or has linear part `−I`. In the latter case, **adopted DYAD §6.16** determines the full formal Taylor series if the induced germ is `C^∞` or analytic; no formal-series claim about full jets of finite `C^r` germs is made. This is not a proof of an admissible physical network, edge carrier, pole identity, or analytic convergence.

## 6. Owner handoff [OPEN / SESSION]

| Stream | Responsibility and status boundary |
|---|---|
| **DYAD** | **Formal G1 / OPEN 19 CLOSED** by adopted v6.4.12 §6.16 (`DYAD-THM-FORMAL-INVOLUTION-UNIQUE`). Existing DYAD–RRF Odd-Carrier Existence Test is owner work on **OPEN 20**: analytic square-root/convergence (B-an), ℤ₆ realization (B-6), and smooth **existence** (B-∞). The former smooth flat-centralizer uniqueness and clock bridge are CLOSED at DYAD v6.4.13 §6.17 for existing germs; do not relaunch them. Do not duplicate its research; formal solution is not a realized `C^∞` or analytic involution. |
| **OFN** | Whether full-state node identity, physical exchange `σ`, primitive-clock covariance and single-edge locality are physically required or admissible. |
| **RRF** | Given a proposed full realization, check submersion, fiber descent, primitive `EF=TE` factor, domains, induced germ and declared regularity; keep `RRF-CND-01` as the broader network admissibility contract. |

**Historical v0.2.1 release boundary (quoted forward, not a current source assessment):** This v0.2.1 note supersedes only the noncanonical G2 interface review v0.2. The changes relative to v0.2 clarify class-preservation including analytic `C^ω`, and point G2-PRE to the existing Foundations & Model Selection / DYAD–RRF Odd-Carrier Existence Test; no existence theorem is imported. The v0.2 note remains a historical reviewed record. It does **not** revise adopted RRF v0.8 or the v0.8.1 review candidate, and does not adopt G1/Problem B results on behalf of DYAD. The mathematical equivalence in §4 is established here from the §2 elementary lemma; *existence* of either equivalent object in the selected `C^∞` or analytic class remains source-dependent and OPEN.

## 7. Interface disposition

`ACCEPT SCOPED — G2 CONTRACT REFINED; REALIZATION OPEN`.

- Accept the proposed submersion/fiber-descent mechanism and the added autonomy/factor distinction.
- Replace `R≠id` with **nonidentity origin germ**, and make the isolating-neighborhood condition explicit before dropping `R(0)=0` as an independent gate.
- Use the elementary averaging-map proof rather than requiring an external Bochner citation; source provenance remains `[SESSION]` pending owner integration.
- Do **not** add this new scientific interface to adopted RRF v0.8 or editorial v0.8.1 during this pass; retain it as a separate handoff to OFN/DYAD and future RRF owner review.
- Do not claim that formal G1 proof, Problem B, exchange locality, or primitive physical clock has been owner-adopted solely on this basis.




## 8. v0.3 review sync disposition (16 October 2026)

`ACCEPT SCOPED — OWNER N7 SOURCE VERIFIED / G2 REALIZATION STILL OPEN`.

This accepted note is a **noncanonical successor to v0.2.1**, based on adopted DYAD v6.4.12 (`c2f00eb0832e6aabcbcfd1a3c583d6f1e7b0950a2f8db97d89045ed0bcb438e8`). Its improvements are: the six-step `C³` linear dichotomy, analytic six-step → primitive clock bridge, owner-formal uniqueness and the analytic odd-chart / tangent-square-root existence equivalence; OPEN 20 (B-an/B-∞) is the sole owner realization problem. `C^∞` exact clock commutation remains open. Neither a `C³` planar factor for projected `K_3` nor a physical `X_0, σ, E` is established here. Underlying v0.2.1 history and RRF v0.8.1 remain unchanged; adopted RRF v0.8.2 separately records the owner N7 receipt without adopting G2 physical realization.


**v0.3 acceptance boundary (17 October 2026):** Following review of the full candidate, the analytic odd-chart/square-root equivalence is explicitly tagged as an RRF/SESSION elementary argument, while DYAD OPEN 20 remains the adopted-owner *open existence* entry. This note is ACCEPT SCOPED, noncanonical; it does not adopt a scientific theorem on behalf of DYAD, choose any physical exchange, or resolve the G2 realization. The original v0.2.1 and review-candidate files are preserved separately.


## 9. v0.4 review overlay (19 October 2026; NOT ADOPTED)

`[SESSION] [scope: source synchronization, not physical realization]` Supersession candidate to accepted noncanonical G2 v0.3. Directly inspected adopted DYAD v6.4.13 §§2, 6.16–6.17 (SHA-256 `5958f7fe8a3e0ec94546cb7e915c5f690d09827a3d680d13a17c9d880b968542`). Owner F1–F3 upgrades **existing** C∞ involution/root clock commutation and uniqueness from flat/formal to exact on §6.15/§6.17 local domains. Same-class odd-chart/root *existence equivalence* now follows from owner F3 and elementary G2 averaging, but existence is OPEN 20 B-an/B-∞; B-6 separately OPEN. The primitive and six-step **network factor hypotheses** are still different; finite C^r implications remain distinct. Historical v0.3 acceptance text in §8 is an archive of that date, not a current OPEN classification. No additional scientific RID, physical exchange action, network factor, or adopted RRF profile is created. This note requires independent review/acceptance before replacing v0.3.


## 10. v0.4 noncanonical acceptance boundary (19 October 2026)

`ACCEPT SCOPED — NONCANONICAL G2 v0.4; PHYSICAL REALIZATION OPEN`. The reviewed v0.4 scientific and mathematical content was accepted **without alteration**; only current record/status and independently dated acceptance metadata were updated. Section 9 remains the dated preacceptance review overlay. This note does not claim an existing physical `X, σ, E`, a valid network→edge factor, or an analytic/C∞ root's existence. DYAD v6.4.13 §§6.16–6.17 owns F1–F3 and the formal generator. RRF v0.8.3 is a separate adopted **working-standard** source synchronization; neither status constitutes scientific owner adoption of this noncanonical note.
