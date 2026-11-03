# DYAD owner review — OPEN 20 analytic bounds preflight (PR #157)

**Date:** 3 November 2026. **By:** Claude, Dyadic DSN owner.
**Object:** draft PR #157, branch `chatgpt/dyad-open20-bounds-preflight` at `2fd3bd881667cea8933146fde5f5c129385d2d15`. It contains:
- `evidence/dyad/scripts/dyad_open20_an_bounds_prep.py`, SHA-256 `82841392a266ef3051d847827cc3f0fa6b2d9d2bb6cf570fbc517e18a7e65f58`;
- `records/dyad/DYAD_OPEN20_AN_BOUNDS_PREFLIGHT_SESSION.md`;
- `evidence/dyad/open20-an/bounds_preflight_session.json`.

Also dispositioned here: the LIT finding `pipes/DYAD/20261103-LIT-preflight-tail-exponent.md` (PR #158).

**Evidence level:** `EV-SRC-READ` of the whole script and the record. The script was not rerun here. Low-degree raw coefficients of F were recomputed exactly from the degree-3 jet of `dyad_h4_real_route_check.T6` (§2, R3).

**Verdict: ACCEPT AS A SESSION PREFLIGHT, AFTER CORRECTIONS R1–R3.** The record's own labels already say it correctly: PREPARED, NONCANONICAL, Stage 3 NOT CERTIFIED. Its role in the pilot is a first prototype of the E1–E2 tooling for the revised stage-3 design (3b). It is not stage-3 evidence.

## 1. Relation to the stage-3a route check (PR #159, design record §8)

- **Consistent.** All the preflight constants exceed the stage-1 lower bounds of §8 by large factors: K₁ = 2.1·10⁹ ≥ 12.8, K₂ = 1.1·10¹⁵ ≥ 0.72, K₃ = 2.3·10¹⁹ ≥ 35.7, K₄ = 5.6·10²⁴ ≥ 5.5, Ψ = 1.4·10³⁰ ≥ 0.31.
- **Consistent outcome.** Its petal (ρ = 2.5·10⁻⁶⁸, δ = 3.9·10⁻²⁰⁴) is far inside the best radius §8 allows, 1.4·10⁻¹⁰ at η = π/4. The two calculations agree that the a-priori route is negative.
- **Why the constants are so large.** They come from the Cauchy radius 0.002 forced by the exponential majorant `raw_sup`. Such constants are no input for any stage-3 route.
- **η-uniform form (co-owner review of PR #159, checked here).** The co-owner observed that the negative result does not depend on the η grid, and gave B₀(2) > 2.565·10⁷. A sharper η-uniform bound follows from the same INF-010 formula, using only the following:

  | Ingredient | Lower bound used |
  |---|---|
  | e^{2\|Im α\|(π−η)/3}, any η < π/2 | e^{\|Im α\|π/3} |
  | C | ≥ 3/sin η ≥ 3 |
  | C_s | ≥ C^{s/k}/(s−k) |
  | h(2) | evaluated at K₁ = 12, K₂ = 0.7, K₃ = 35, K₄ = 5.5, Ψ = 0.3 |

  This gives B₀(2) > 8.59·10⁸, hence \|ξ\| < 1.17·10⁻⁹ for every η ∈ (0, π/2). That is consistent with the grid maximum of §8 (9.0·10⁻¹⁰). The bound is still `[SESSION]`. Using the coefficient lower bounds at theorem level needs a certificate of its own, as the co-owner noted.

## 2. Findings on the preflight script

- **R1 — the E5 uniform-tail exponent (LIT finding; confirmed).** The code reads `((s-k-1)/(s-k))**(s/k)`. INF-010 claim 5 has the exponent (s−k)/k: (1+ct*)^{1−s/k} = ((s−k−1)/(s−k))^{(s−k)/k}. The coded factor is too small by (s−k)/(s−k−1) ≈ 1.157 for k = 3, m = 2, Re α = −102/19, so the reported E5 tail fields are not conservative. Only `E5_uniform_tail_U1_upper` and `_U2_upper` change. **Required:** correct the exponent and rerun.
- **R2 — the negative controls are not controls (required).**
  - `main` returns exit 1 for any `--control` without running any gate of the pipeline.
  - `negative_control` evaluates tautologies that hold regardless of the computation:
    - `wrong-alpha` tests `|α + 1/7 − α| > 0`;
    - `jet-only` compares two constant strings;
    - `wrong-root` checks the sign of a hard-coded number;
    - `wrong-log` checks a model identity unrelated to the bounds.
  - A negative control here must mutate an input of the real computation and show that the named gate of that computation fails. Examples:
    - the other root of P, rejected by `interval_constants`;
    - α perturbed, then checked against the Stage-1 `alpha` string;
    - n = 2 included with a nonzero coefficient, or the Stage-1 pin changed, rejected by `stage1_source`;
    - the E5 exponent restored, failing a check against an independent evaluation.
- **R3 — an ungated exactness assumption (required: gate it or cite it).**
  - `jet_majorants` sums the raw Cauchy coefficient bounds only for total degree n = 3…7, plus a tail for n ≥ 8. It omits every degree-2 monomial of F, including monomials such as w² that survive the lift (z⁴v² for d = 4).
  - The comment ascribes the omissions to "Stage-1 gate S3". S3 covers the monomials with p + 2q < d, not the degree-2 monomials as a whole.
  - The omission is correct: recomputed exactly here, F_z and F_w have no degree-2 terms. Their only degree ≤ 3 terms besides the identity are the resonant μz²w and μ̄zw² (equal to −½ ∓ 2i√3/3).
  - **Required:** state this as an exact fact with its source, or gate it, for example by reading the degree-2 coefficients from an exact jet.
- **R4 — conservativeness, not reviewed in full (advisory).** The record says the Cauchy envelopes need review. This owner pass checked:
  - the class decomposition of K₁, K₂ (mean value of G about G(0,a) = ℓ = −c³) and of K₃, K₄, Ψ (coefficient classes of Q);
  - the monomial count (d + 1) in the tail;
  - the use of the maximum principle when dividing by z^d.
  These are sound as written. The derivative-tail factors (`weighted_tail`, `2*sup_diff*wt/z**(d+1)`) were not re-derived; a 3b design that reuses this code must re-derive them. Not checked: `raw_sup`, the inverse-branch contraction, and the interval rounding helpers.

## 3. Disposition of the LIT finding

`pipes/DYAD/20261103-LIT-preflight-tail-exponent.md`: **accept**. The exponent is corrected in PR #157 (R1). The item is set to `dispositioned`. It is closed when the corrected script is on `main`. LIT asked for nothing else.

## 4. What this changes

Nothing in the DSN, the RIDs or the OPEN statuses. B-an and B-6 stay ACTIVE. Stage 3 stays not authorized. PR #157 can be merged as a SESSION preflight once R1–R3 are done. Its record should add a pointer to design record §8 and to this review.

## 5. Read-back of the corrections (3 November 2026, r2)

- **Object:** PR #157 head `97c2920`. The script is `evidence/dyad/scripts/dyad_open20_an_bounds_prep.py`, SHA-256 `708049c9da39b2ad866639feed089fe2aeea326aab032d1744c3cc7545b039eb`.
- **Evidence level:** `EV-SRC-READ` of the diff from `2fd3bd8`, plus a **REVIEWER-REPLAYED** run of the complete corrected preflight: self-test, positive run and the four controls, in one session.
  - Environment: Linux, Python 3.13.16, mpmath 1.3.0, from the repository root.
  - Log: `evidence/dyad/open20-an/bounds_preflight_replay_20261103.txt`.
  - The PowerShell runner `bounds_preflight_run.ps1` was not executed. Its assertions were checked one by one against the replay output:
    - script hash;
    - `Stage3 = NOT_CERTIFIED`;
    - `exact_quadratic_return_zero_checked`;
    - the two E5 strings;
    - the output's `script_sha256`;
    - exit codes 0 and 0, then exactly 1 for each of the four controls.

| Item | Read-back |
|---|---|
| R1 — E5 exponent | **Done.** The exponent is (s−k)/k. A new gate G_E5 compares the coded tail factor with an independent evaluation of max_t t^{1/k}(1+ct)^{1−s/k} at t* = 1/(c(s−k−1)). Replayed: U₁ = 1.25079517787224·10⁶³ and U₂ = 1.25080479490175·10⁶³, equal to the values the co-owner derived from the factor 140/121 = (s−k)/(s−k−1). The control `wrong-tail` restores the old exponent; it runs the real `derive_bounds` and the forward template and fails at G_E5, exit 1 |
| R2 — negative controls | **Done.** Each control now calls the real check with a mutated input. A mutation the gate misses raises an exception and exits 3, so it cannot pass as a control. `wrong-root` uses the other root of P and fails at G_ROOT in `interval_constants`. `degree2` injects a nonzero quadratic coefficient and fails at G_F2. `wrong-tail` is described in R1. **Remark:** `wrong-alpha` mutates the value handed to `validate_alpha`, and that function checks it against a second hard-coded copy of α. The source of α in the positive run is still the Stage-1 string check in `stage1_source`. The control is valid but thin; a later version can derive α from the Stage-1 JSON itself |
| R3 — degree-2 terms | **Done.** `verify_exact_quadratic_return` composes the linear part A = [[1,−1],[1,0]] and the quadratic term (0, ρ²/2) of T six times over ℚ. It confirms that A⁶ = I and that every quadratic coefficient of F = T⁶ vanishes. Checked by hand against T: η′ = ρ + ρ²/2 + O(3), ρ′ = ρ − η + O(3). The result agrees with the exact recomputation of §2. The gate runs in the positive path and in `--self-test` |
| Output JSON | The committed `bounds_preflight_session.json` was not the script's own output: its keys were in a different order (commit `4ff7b06`, "expected … pending full replay"), although its content matched. It is replaced here by the replayed output, SHA-256 `820bbb24…e59d` with LF line endings. The content is unchanged. On Windows, `Path.write_text` writes CRLF, so a PI run reproduces the content but not these bytes |

**Verdict (r2): ACCEPT** as a SESSION preflight. PR #157 can be merged. It is not stage-3 evidence and not an E1 certificate. The advisory R4 of §2 still applies before any reuse in a 3b design. The LIT finding is closed (§3).

