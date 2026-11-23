---
title: "RRF Registry v0.3 — bounded source and consistency review"
version: "review v1"
date: "25 September 2026"
source snapshot date: "24 September 2026"
class: "review / proposed replacements"
reviewer: "ChatGPT"
status: "Review only. Architecture supported; adoption of the unchanged submitted bytes deferred pending the bounded replacements below. No registry or owner DSN amended."
basis: "Complete supplied Registry v0.3; comparison with v0.2; targeted DYAD v6.4.10, RECOG v0.3.1, and Methodology v1.3 inspection."
---

# 1. Disposition and completed checks

The previous five main revisions are present: the principal-angle versus lifted W distinction; separate formal/delivered one-step maps; the unregistered multiplicative-network realization; the principal status-spelling repairs; and the split between transport-established involutions and physical OPEN-A. The five profile IDs and the OPEN-B/E dependency architecture need no redesign in this review.

The old v0.2 and v0.1 changelog entries are preserved verbatim. Retain their historical spelling. However, `[OPEN: transport]` still occurs in a live rule at source line 156; the claim that old spelling occurs only in history is not correct for these supplied bytes.

The remaining substantive issues are narrowly located: an exact self-return invariance claim that exceeds its source, an amplitude-transport arrow that misidentifies two observables, and an information-loss statement that applies the global covering limitation to a single-sheet local map.

This review does not reopen the adopted enclosure constants. It does not require another normal-form calculation. It supplies exact replacement text and two short deductions from the cited definitions/theorem. These deductions are identified below as review consequences, not existing owner RIDs or a new independently checked certificate campaign.

# 2. RRF03-C01 — self-return multiplier: exact versus finite/formal symmetry

**Source:** Registry §2.4, lines 113 and 116; compare its own lines 110–112 and §8 item 7.

The actual observable is defined as

\[
\chi_m(z)=\widehat F^{\circ m}(z)/z,
\qquad \widehat F=h_6^{-1}\circ F_W\circ h_6.
\]

The covariance row then declares both q and chi_m exactly invariant under z -> -z. Exact q-invariance is a direct algebraic identity. Exact chi_m-invariance would require the exact delivered map/iterate to be odd. The source establishes odd finite jets and an odd formal normal form, not all-order oddness of this exact analytic map. DYAD v6.4.10 §6.14 makes that finite-jet distinction explicit; the registry itself denies the stronger symmetry in §8.

**Disposition:** unsupported as an exact claim in this registry; not a claim that the actual map's symmetry has been numerically or algebraically falsified in this review. This leftover row was also missed in the preceding review.

## Proposed replacement

> **Covariance under -I.** q(-z)=q(z), C_z(-z_a,-z_b)=C_z(z_a,z_b), and C_z(-z_a,z_b)=-C_z(z_a,z_b) are exact algebraic identities. The self-return multiplier is defined for z != 0 and admissible iterates. For the formal odd normal form, its formal self-return multiplier is sign-invariant. For the delivered exact analytic map hatF, exact sign invariance of chi_m is not established by the finite-jet/remainder certificate. Preserve that distinction; neither a finite-order estimate nor the odd polynomial J is a replacement for the exact observable.

## Direct bounded consequence for one return

[ALG] [scope: direct consequence of DYAD-THM-NF-REM on either of its symmetric disks; one six-step return]

Set

\[
R(z):=\widehat F(z)-J(z),\qquad |R(z)|\le C_7|z|^7.
\]

Because J(-z)=-J(z), for 0<|z|<=r,

\[
\chi_1(-z)-\chi_1(z)
=-\frac{R(-z)+R(z)}{z},
\qquad
\boxed{|\chi_1(-z)-\chi_1(z)|\le2C_7|z|^6.}
\]

Use `(r,C7)=(1/20,100)` or `(1/40,30)` without mixing the profiles. This is a bound, not exact invariance. No m-uniform iteration bound is inferred here.

The equality chi_m^J(-z)=chi_m^J(z) is exact for the separately defined polynomial model chi_m^J=J^{circ m}/z, but introducing that model would be an explicit redefinition, not transport of chi_m. The registry need not add it merely to repair the covariance row.

The annotation example at line 44 should likewise use `f_hat_form`, matching §2.4, rather than reusing an unqualified `f_hat` next to the words "formal all-order."

# 3. RRF03-C02 — observable transport follows the inverse direction of coordinate substitution

**Source:** Registry §3, T-h row, line 150; §2.4 common-realisation row, line 117.

The comparator transport is now correctly stated. The same row still begins with

```
q -> Q_prim = |h|^2
```

This has the original amplitude-identification problem. q and Q_prim are different native observables, as the profile and DYAD-THM-NF-INV already say. Transporting q to W gives |h^{-1}(W)|^2, not |W|^2.

## Proposed T-h observable entry

> With h: NF -> W, the pullback of the primitive amplitude is h*Q_prim(z)=Q_prim(h(z))=|h(z)|^2, while the W-coordinate expression of the NF amplitude is (h^{-1})*q(W)=|h^{-1}(W)|^2. The primitive comparator pulls back to overline(h(z_a)) h(z_b). q=|z|^2 and C_z=overline(z_a)z_b remain separately defined native NF observables, not identifications with Q_prim and C_W.

In formulas,

\[
h^*Q_{\rm prim}=|h(z)|^2,
\qquad
(h^{-1})^*q=|h^{-1}(W)|^2.
\]

## Common-realisation direction

The two z-states are **preimages under h**, or images under h^{-1}, of W-states. Replace "images under the same registered h of states in the same W-frame" with:

> z_a=h^{-1}(W_a), z_b=h^{-1}(W_b), using the same registered h and W-frame, with both points in the registered inverse domain; or use the explicitly registered transport between the two frames.

This is direction/typing repair only. It does not decide physical co-realisation, birth inheritance, or the network bridge.

# 4. RRF03-C03 — local composite covering does not lose data on its registered sheet

**Source:** Registry §3 composite NF -> WRAPPED row, line 154; distinguish the global T-exp row, line 152.

The global covering

\[
E(\rho,\eta)=e^{\rho+i\eta}
\]

has no global single-valued inverse and identifies deck sheets. That statement remains correct.

The restricted composite

\[
p(z)=E(\mathcal L^{-1}h(z))
\]

on the delivered small h-domain does not contain multiple phase sheets. Its loss column should not say "winding" as though two different permitted NF states were identified.

[ALG] [scope: short consequence of DYAD-THM-NF-INV; no new radius certificate]

For |z|<=1/10,

\[
|h(z)|\le\frac{17}{16}|z|\le\frac{17}{160},
\qquad
|\eta|\le\frac2{\sqrt3}|h(z)|
<\frac{119}{960}<1<\pi.
\]

Thus the image is inside one principal phase sheet. On its image the composite has the local inverse

\[
p^{-1}(\zeta)=
h^{-1}\!\left(\mathcal L(\log|\zeta|,\operatorname{Arg}\zeta)\right),
\]

where h^{-1} is its actual inverse on h(D_{1/10}). The smaller explicit inverse-target disk |W|<=9/100 remains the owner certificate's sufficient target domain; this formula does not enlarge that uniform target claim to unrelated W-states.

## Proposed row replacement

> **Inverse:** local inverse on the registered image, using the fixed principal lift; no global inverse on arbitrary C*. **Loss:** none on the registered single-sheet NF domain. The global T-exp map forgets deck-sheet data when such data are part of its source; no additional winding state is being silently discarded from this restricted domain.

This does not turn the local NF profile into a global state representation or supply a physical winding interpretation.

# 5. Finishing edits and exact reference pins

These are finite editorial actions, not another research programme.

| Location | Action |
|---|---|
| §1 example, line 44 | Use f_hat_form for formal all-order equivariance, matching §2.4. |
| §3 live rule, line 156 | Replace `[OPEN: transport]` with `[OPEN] [scope: transport]`. Preserve `[OPEN: bridge]` inside the unchanged v0.2 changelog. |
| §2.1 anti-correlation source, line 62 | Correct the source to DYAD v6.4.10 §6.4 (`#sec-6-4-isp`). The anti-correlation formula is there, not §6.5. The equation and wrapped-profile placement remain correct. |
| Symbol locators in import RID slots | Q_true, the symbol L, and E_odd are definition labels in the source, not registered RIDs. Put them in the source-description field; use an exact source section/anchor and `RID unavailable` where the Methodology exception is needed. Do not invent owner identities. |
| Table cells containing import separators | Escape interior pipes as `\|` or place the import record outside the Markdown table, so RID separators do not create extra columns. This changes rendering, not the import semantics. |
| §0 provenance policy | Keep `participant-rechecked; Claude-check pending` as the agreed review-routing status. Do not attribute a universally named Claude gate to Methodology v1.3: its inspected §§0.6, 12 and 13 require truthful review/independence and recorded adoption but do not mandate a particular model by name. |

The valid owner RIDs DYAD-ALG-NF6, DYAD-ALG-NF6-OBS, DYAD-THM-NF-INV, DYAD-THM-NF-REM and RECOG-OPEN-QUINTIC-FRAME were found in the supplied owners. None is renamed or reassigned.

The prior assistant's language treating a specifically named Claude check as a universal Methodology rule was too broad. The project may keep that workflow requirement; its authority should be stated accurately. This does not mark Claude's pending check completed or weaken evidence discipline.

## Involution notation clarification, not another result requirement

When S_6 denotes the exact map h_6 o (-I) o h_6^{-1} on an invariant image h_6(D), with D sign-symmetric, involutivity S_6^2=I follows exactly from its definition. When it denotes only that map's degree-six polynomial truncation, involutivity holds only to the stated jet order. The finite-order commutation with f is a separate assertion in either case. One sentence specifying which S_6 is registered will prevent the exact-identity and finite-symmetry qualifiers from being interchanged. No all-order dynamical symmetry is added by this observation.

# 6. Evidence and adoption boundary

This turn inspected the full 243-line registry and its diff against v0.2; checked the relevant owner statements, RID occurrences, and Methodology rules; and performed text/identity checks. The two algebraic consequences above are explicit deductions from the imported theorem and definitions. No referee, majorant, normalizer, or swap-certificate script was executed in this turn. No new reviewer provenance is claimed.

The currently mounted files do not include `DYAD_RETURN_ENCLOSURE_P2B_v2_evidence.zip` or its `outputs/certificate.json`. The owner source supplies their locator, not the artifact bytes. Recover the original archived member and matching manifest for the proposed artifact-level Claude check; recreating coefficients would not itself authenticate the old artifact. Existing available .py files are not being described as missing.

The source registry and all owner files are unchanged. This output is only a Markdown review, not an edited v0.3, not a v0.4, and not an adoption record. No additional PDF, DOCX, or evidence ZIP is produced.

**Acceptance recommendation:** keep the reviewed architecture and old history, apply the stated point-of-use corrections within the current target version, and then record the actual working-standard adoption separately. Pending Claude checking and OPEN-A/B/E remain explicit evidence/research fields; they must not be silently represented as closed.

# 7. Source identity record

Source files were available locally. Locations in this review refer to their inspected bytes, not a remote archive. SHA-256 values appear below; hashes establish identity only.

**RTG_RRF_REPRESENTATION_REGISTRY_v0_3.md**

```text
SHA-256: 54703a8e32ae0241fd79bc0c66b32fded1dd40f14735d5380bece552b9e1cc31
```

**RTG_RRF_REPRESENTATION_REGISTRY_v0_2_DRAFT.md**

```text
SHA-256: 27f3219c5be0984412ceec1932d403c9c09fc62c0b37f2f9c7e3c9284784680e
```

**RTG_DYADIC_OSCILLATOR_DSN_v6_4_10.md**

```text
SHA-256: 7455811928606076b3bc3075632275dc2a24e37fdbf0ae20036db5529a1b56b7
```

**RTG_RELATIONAL_RECOGNITION_DSN_v0_3_1.md**

```text
SHA-256: 3b4dfe5e66819224dbfb2207d2b0b7157efad174a142a0057760df2eba40bff5
```

**DSN_METHODOLOGY_v1_3.md**

```text
SHA-256: 3e23ba94606706b3c8d50aecfb2184df52042cf8e65cdd3c3e0cd3159254ec7e
```
