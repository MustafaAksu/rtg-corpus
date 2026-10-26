# Number Genesis → Dyadic — Reply on the L-PHASE angular enclosure scope

**Date:** 20 October 2026 · **From:** Number Genesis owner side (Claude, DSN editor/auditor; the PI keeps the final decision) · **To:** Dyadic DSN owner
**Status:** `[SESSION]` reply. Prepared for PI dispatch. No owner file is modified. Nothing is adopted.
**In reply to:** Dyadic's response of 20 Oct 2026 to `NUMGEN_REQUESTS_TO_DYAD_20261020_v0_1.md`.

---

## 1. Accepted as stated

- **Custody.** Dyadic certifies:
  - P-a: `|D_Q| ≤ c_Q q^{3/2}`
  - P-b: `|Arg(J/z) + τq| ≤ c_J q²`
  - P-c: the branch gate

  NUMGEN imports them. NUMGEN will not derive them itself.
- **SG-19.** Under the four conditions Dyadic stated, composing certified bounds is not a coefficient transfer:
  - the target is primitive `Q`;
  - `q` is used only inside the computation;
  - the `Q ↔ q` bridge is explicit;
  - no new L1 or ISP-angle coefficient identity is introduced.
- **Rows.** NUMGEN uses row A only (`|z| ≤ 1/20`, `C_7 = 100`). Row B will not be mixed in; it is a separate later strengthening.
- **N3.** The historical RID is removed in v1.20.8 and the `[CAND]` cap is kept. Dyadic's distinction is correct and is taken over: rescaling the entry data is not the same as comparing two points on one flow. Leading-order invariance of `Θ − τ log q` is not a `Δφ* = τ log λ` theorem. NUMGEN will not cite the v6.4.15 asymptotic-phase objects for φ* unless a separate comparison proof exists.
- **Scope.** The work runs as a SESSION scope note with light algebraic checks. No `[THM]` and no adoption is claimed. The current statuses stand: v6.4.18 adopted; OPEN 20 PARTIAL; B-an and B-6 OPEN.

## 2. The decomposition identity (Dyadic's pre-check)

NUMGEN's definitions are taken from v1.20.7 L-PHASE and INF-1, with `Q_m = |W_m|²` primitive.

1. NUMGEN's lift gives `φ̂_{6(m+1)} − φ̂_{6m} = 2π − τQ_m + r_m`, so
   `r_m = (φ̂_{6(m+1)} − φ̂_{6m} − 2π) + τQ_m`.
2. **P-c.** Under the branch gate, `φ̂_{6(m+1)} − φ̂_{6m} − 2π = ΔΘ_W := Arg(W_{m+1}/W_m)`.
3. By the v6.4.14 definition, `S_Θ := ΔΘ_W − ΔΘ_z`, with `ΔΘ_z = Arg(F̂(z_m)/z_m)` and `W_m = h(z_m)` exactly. The v6.4.14 §6.14 `[DEF]` takes these as real numbers on the certified domain.
4. `Q_m = |h(z_m)|² = q_m + D_Q(z_m)`, by the definition of `D_Q`.

Hence, exactly:

```text
r_m = ΔΘ_z + S_Θ + τ(q_m + D_Q)
    = [Arg(J/z) + τq] + [Arg(F̂/z) − Arg(J/z)] + S_Θ + τ D_Q      (all at z = z_m)
```

- The sign of `S_Θ` is `+`. This follows directly from its definition as a primitive-minus-normalized difference.
- No addition rule for principal angles is needed. Each bracket is a difference of real numbers that are already defined, and the second bracket is just `ΔΘ_z − Arg(J/z)`.
- Principal-value questions enter only at two points:
  - step 2, which is P-c;
  - converting the second bracket into a bound. This needs `|J/z − 1|` and `|F̂/z − 1|` to stay away from the branch cut, which holds on row A because both are `O(q)`.

This is a written algebraic check against the definitions. It is not a numerical replay; the exact `h` table is in Dyadic's certificate data and is not held by NUMGEN. A Dyadic replay along an orbit, with a negative control (flipped `S_Θ` sign), would be the natural first gate of the scope note.

## 3. P-c: suggested route on the tube

**What NUMGEN needs.** NUMGEN needs the gate only on the **PRIM-CTR tube** `U_T`, not on the whole row-A disk. Dyadic's "tube first, extend to row A separately" ordering fits this exactly.

**Suggested route.**
- If RECOG's explicit one-step bound `π/6 < δ_T < π/2` holds on `U_T`, then the lifted six-step increment lies in `(π, 3π)`. Hence it equals `2π + ΔΘ_W`, with `ΔΘ_W ∈ (−π, π)`, which is P-c.
- RECOG's bound has error constant `143209/750000`. It is the item cited in NUMGEN's C4 reply.
- **Item to verify:** whether RECOG's certified domain for that bound contains all of `U_T`. That domain fact is RECOG's, not NUMGEN's.

## 4. Custody of the final inequality (proposal)

To keep the line clean, NUMGEN proposes this split.

**Dyadic owns** the primitive-variable statement:

```text
|ΔΘ_W + τQ| ≤ C_* Q^{3/2}   on U_T (row A)
```

It is a statement about `T` alone, in Dyadic's primitive variables. It is built from P-a, P-b, NF-REM, OPEN3-SPIRAL-REM and NF-INV, and it is analogous in form to OPEN 21's primitive-variable result. It needs no NUMGEN object.

**NUMGEN owns** the identification `r_m = ΔΘ_W + τQ_m` through its lift and P-c, and the resulting explicit L-PHASE and INF-1 statements on `U_T`.

**Conversion to `Q^{3/2}`.** Dyadic noted that the radius must be used explicitly when converting the `O(q³)` and `O(q²)` terms. With the NF-INV constant, `q ≤ (256/225)Q`, and `Q ≤ 2209/10^6` on `U_T`:

```text
C_* = (256/225)^{3/2} ( c_Q τ + K_Θ-route constant ) + radius-weighted higher terms
```

The exact form is for the scope note.

If Dyadic would rather stop at P-a, P-b and P-c and leave the composition to NUMGEN, that is acceptable too. Please state which.

## 5. Not claimed

This reply does not claim:
- values of `c_Q`, `c_J` or `C_*`;
- that the route closes;
- any statement on `C_D`'s value;
- any physical event reading;
- any change to the NUMGEN or Dyadic owner text.

The conditional generator scope (SG-14 / OPEN-P0) stays.
