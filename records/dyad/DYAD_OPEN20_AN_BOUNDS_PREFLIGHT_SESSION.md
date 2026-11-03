# DYAD OPEN 20 — analytic bounds preflight (SESSION)

**Date:** 2026-11-03. **Status:** PREPARED / NONCANONICAL; R1–R3 code corrections committed, revised full replay outstanding. **Stage 3:** NOT AUTHORIZED and NOT CERTIFIED. No scientific owner adoption, canonical DSN, release, tag, RID or pipe-state change.

## Sources and reading extent

- Governing DYAD v6.4.23 at the verified tag dyad-v6.4.23: targeted owner sections; not a whole-document rereading.
- DYAD_OPEN20_AN_SECTORIAL_PILOT_DESIGN.md on main: D1–D10, §4 E1–E7, §6 guards, §7 S1–S7 and §8 Stage-3a route check (targeted reading); owner review `records/dyad/DYAD_OWNER_REVIEW_OPEN20_BOUNDS_PREFLIGHT.md` (§2 R1–R3, PR #163). The design's original baseline remains v6.4.22.
- Stage-1 evidence/dyad/open20-an/stage1_prep.json: SHA-256 2c9ae6376e0c482f2ba520a7ea8e2b38606a6821f7ac3bfa259d4d6020d04739. The script checks this pin and all S1–S7 gates before proceeding.
- LIT INF-009 and INF-010, PR #28 merge 14630e0931b7ddc14e772063218fe51de77fcc54, PR #29 merge a67bc60b9cdc5f6ec052f910e3d994b3aac5d2c5, PR #30 merge 564a1eef3be1bf541cc6c4da19093732a65b7035. All LIT conclusions remain SESSION; DYAD acceptance is separate.

## Implementation and analytic route

Source: evidence/dyad/scripts/dyad_open20_an_bounds_prep.py  
SHA-256 (corrected R1–R3 script): 708049c9da39b2ad866639feed089fe2aeea326aab032d1744c3cc7545b039eb; predecessor at PR #157 initial commit: 82841392a266ef3051d847827cc3f0fa6b2d9d2bb6cf570fbc517e18a7e65f58  
Dependencies: Python 3, mpmath 1.3.0. Scalar bound calculations use mpmath.iv at 75 decimal digits; ordinary high-precision full-map smoke calculations are not proof.

The primitive is evaluated as the **full entire map**, composed six times, in independent complex variables z,w:

\[
T(\rho,\eta)=(\rho-\sin\eta,\ \eta+e^\rho-1-\sin\eta),\quad
z=\rho+\omega\eta,\quad w=\rho+\bar\omega\eta,\quad
\omega=(-1+i\sqrt3)/2.
\]

Finite Stage-1 jets provide verified vanishing orders and normalization identities, never a substitute for the full analytic map. The revised script additionally verifies the full quadratic jet of the composed return is identically zero by an exact Fraction recurrence from the raw primitive `A=[[1,-1],[1,0]]` and quadratic term `(0,rho^2/2)`. Stage-1 S3 alone does not establish global total-degree-2 vanishing. Conservative Cauchy majorants are built for the removable functions

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
    foreach ($c in @("wrong-alpha","wrong-root","wrong-tail","degree2")) {
        python -I -B evidence/dyad/scripts/dyad_open20_an_bounds_prep.py --control $c
        if ($LASTEXITCODE -ne 1) { throw "Negative control did not reject: $c" }
    }

**Pre-correction historic run (initial PR #157, script SHA `82841392…e65f58`):** self-test PASS and four reported negative-control exit codes 1; owner review R2 found these controls tautological and they are **not evidence** of failure detection. The Stage-1 file's pinned identity and earlier preflight outputs were recorded. **Current revised script:** mutations are `wrong-alpha` (G_ALPHA), `wrong-root` (G_ROOT), `wrong-tail` (G_E5), and `degree2` (G_F2); these invoke actual calculation checks and must each exit exactly 1. Their branches were statically inspected and the exact F2/alpha/root/E5 mini-gates checked separately by the co-owner, but the **complete corrected preflight and all four controls have not yet been rerun together**. Their exit status and corrected JSON byte identity are pending; no test PASS is claimed here. This is not a replay of LIT's test suite.

## Indicative preflight output (not a scientific certificate)

| Quantity | Conservative reported result |
|---|---|
| Raw global map sup at bidisc radius 0.002 | at most 1.658563 |
| K1, K2 | 2.1155e9, 1.1470e15 |
| K3, K4, Psi | 2.2744e19, 5.5721e24, 1.3931e30 |
| Raw inverse Jacobian row sum on radius 1e-9 | below 1.246e-15 |
| Sufficient forward rho, delta | 2.5e-68, 3.90625e-204 |
| Forward L upper | 2.046e-3 |
| E5 uniform tail U1 / U2 (expected corrected upper values, 15 significant digits) | 1.25079517787224e63 / 1.25080479490175e63 |
| Exact degree-2 return jet (new computation) | zero, algebraically checked |
| Stage-3 scientific status | NOT_CERTIFIED |

The radius is unusably small for the planned numerical campaign. The original E5 tail numbers (U1≈1.0810e63, U2≈1.0811e63) were **non-conservative** because the exponent was `s/k` instead of `(s-k)/k`; R1 corrects it. The two updated tail fields in `bounds_preflight_session.json` were derived from the exact factor `(s-k)/(s-k-1)=140/121` and rounded outward to 15 significant digits. They are expected results, **not an actual script replay**. Source data other than E5 are unchanged. See the incoming LIT finding `pipes/DYAD/20261103-LIT-preflight-tail-exponent.md` and owner review cited above. R2 replaces the ineffective negative controls; R3 separately verifies vanishing quadratic terms of F. These preliminary envelopes have not been certified for Stage 3.

## Remaining obligations

1. **Rerun the corrected full script and `--self-test` from repository root, regenerate its representative JSON, and verify the four mutated-input controls each exit exactly 1 with the named gate; compare E5 fields, script SHA-256 and the exact F2 gate to this expectation.** Then have the Dyadic co-owner read back the resulting diff. Independently review the analytic majorant bounds and all normalization conventions.
2. Certify normalized inverse-map domains, branches, and K constants for odd petals.
3. Require separate PI authorization for Stage-3 certification, followed by verified orbit summation, E5/E6 residual and roundoff enclosures, and E7 transport.
4. Preserve statement acceptance, stream use and scientific adoption as separate decisions.

**No conclusion about convergence, divergence, B-an, B-6, or physical dynamics is asserted.**
