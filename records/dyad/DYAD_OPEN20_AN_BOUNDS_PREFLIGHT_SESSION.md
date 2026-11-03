# DYAD OPEN 20 — analytic bounds preflight (SESSION)

**Date:** 2026-11-03. **Status:** PREPARED / SELF-TESTED / NONCANONICAL. **Stage 3:** NOT AUTHORIZED and NOT CERTIFIED. No scientific owner adoption, canonical DSN, release, tag, RID or pipe-state change.

## Sources and reading extent

- Governing DYAD v6.4.23 at the verified tag dyad-v6.4.23: targeted owner sections; not a whole-document rereading.
- DYAD_OPEN20_AN_SECTORIAL_PILOT_DESIGN.md on main: D1–D10, §4 E1–E7, §6 guards and §7 S1–S7 (targeted full pilot reading). Its original baseline remains v6.4.22.
- Stage-1 evidence/dyad/open20-an/stage1_prep.json: SHA-256 2c9ae6376e0c482f2ba520a7ea8e2b38606a6821f7ac3bfa259d4d6020d04739. The script checks this pin and all S1–S7 gates before proceeding.
- LIT INF-009 and INF-010, PR #28 merge 14630e0931b7ddc14e772063218fe51de77fcc54, PR #29 merge a67bc60b9cdc5f6ec052f910e3d994b3aac5d2c5, PR #30 merge 564a1eef3be1bf541cc6c4da19093732a65b7035. All LIT conclusions remain SESSION; DYAD acceptance is separate.

## Implementation and analytic route

Source: evidence/dyad/scripts/dyad_open20_an_bounds_prep.py  
SHA-256: 82c5e874c66eb06b078c177325ebb873caeea1bbaa1871516464606749c26b09  
Dependencies: Python 3, mpmath 1.3.0. Scalar bound calculations use mpmath.iv at 75 decimal digits; ordinary high-precision full-map smoke calculations are not proof.

The primitive is evaluated as the **full entire map**, composed six times, in independent complex variables z,w:

\[
T(\rho,\eta)=(\rho-\sin\eta,\ \eta+e^\rho-1-\sin\eta),\quad
z=\rho+\omega\eta,\quad w=\rho+\bar\omega\eta,\quad
\omega=(-1+i\sqrt3)/2.
\]

Finite Stage-1 jets provide ONLY verified vanishing orders and normalization identities, never a substitute for the full analytic map. Conservative Cauchy majorants are built for the removable functions

\[
G(z,v)=\frac{F_z(z,z^2v)-z}{z^4},\qquad
H(z,v)=\frac{F_w(z,z^2v)-z^2v}{z^5},
\]

with v=a+b_1 z+Y and xi=c z. The preflight derives explicit but crude K1..K4 and Psi, checks |z^3 G|<1, and bounds the **raw** local inverse by a contraction of v to w-(F(v)-v). It evaluates only the forward E3/E4 analytic-template inequalities and an E5 exact-operator tail formula.

**Not covered:** normalized F-inverse on odd petals, full Hakim orbits on curved petals, rounded E5/E6 fixed-point residuals, E7 transport, Stokes jump comparison or any Stage-3 campaign.

## Reproduction in PowerShell (repository root)

    python -m pip install "mpmath==1.3.0"
    python -I -B evidence/dyad/scripts/dyad_open20_an_bounds_prep.py --self-test
    python -I -B evidence/dyad/scripts/dyad_open20_an_bounds_prep.py --out dyad_open20_an_bounds_preflight.json
    foreach ($c in @("wrong-alpha","wrong-root","wrong-log","jet-only")) {
        python -I -B evidence/dyad/scripts/dyad_open20_an_bounds_prep.py --control $c
        if ($LASTEXITCODE -ne 1) { throw "Negative control did not reject: $c" }
    }

Local preparation checks: self-test PASS; all four negative controls rejected with expected exit 1; a corrupted Stage-1 input failed safely with exit 3. The preflight used the byte-identical Stage-1 JSON, independently hashed, and returned Stage3=NOT_CERTIFIED. This is not a replay of the LIT test suite.

## Indicative preflight output (not a scientific certificate)

| Quantity | Conservative reported result |
|---|---|
| Raw global map sup at bidisc radius 0.002 | at most 1.658563 |
| K1, K2 | 2.1155e9, 1.1470e15 |
| K3, K4, Psi | 2.2744e19, 5.5721e24, 1.3931e30 |
| Raw inverse Jacobian row sum on radius 1e-9 | below 1.246e-15 |
| Sufficient forward rho, delta | 2.5e-68, 3.90625e-204 |
| Forward L upper | 2.046e-3 |
| Stage-3 scientific status | NOT_CERTIFIED |

The radius is unusably small for the planned numerical campaign. These preliminary envelopes have not been scientifically reviewed by the DYAD owner.

## Remaining obligations

1. Independently review the analytic majorant bounds and all normalization conventions.
2. Certify normalized inverse-map domains, branches, and K constants for odd petals.
3. Require separate PI authorization for Stage-3 certification, followed by verified orbit summation, E5/E6 residual and roundoff enclosures, and E7 transport.
4. Preserve statement acceptance, stream use and scientific adoption as separate decisions.

**No conclusion about convergence, divergence, B-an, B-6, or physical dynamics is asserted.**
