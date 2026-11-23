# RER r4 Triadic addendum 2 — receiving review of 21:46; G5 update

**Status:** NONCANONICAL. Amends `RER_v0_2_r4_TRIAD_RECORD_CANDIDATES_20261017.md` and addendum 1 (`f1a0dfad…21a6`).

## 1. Receipt

The 21:46 disposition is accepted without change:
- the four records are ACCEPT SCOPED;
- the kernel replay is PASS as a [NUM] check;
- G6 stays OPEN;
- the birth-graph p = 4 / p ≥ 5 split is accepted under the conditional child contract;
- D3 is P0 and needs owner review;
- RER has no adoption or freeze.

**Evidence label for the kernel subclaim in r4:**
- The exact-rank result is `TRIAD_CK_PY` (exact rationals, about 90 s). Its status is source-executed; the receiving replay of that exact script is still pending.
- The independent float64 replay `TRIAD_KR_PY` has been receiving-replayed and passes. Its grade is [NUM].
- The [ALG] grade for "dimension 2 at k = 3" therefore rests on the exact script. Until it is replayed on the receiving side, the record should read: "[ALG], source-executed exact; independent [NUM] replay PASS".

## 2. G5 (six-step-clock factors) — new SESSION source, update the gap row

The project now holds `claude/K3_KAPPA_SIX_STEP_CLOCK_NOTE_v0_3.md` (17 Oct; SESSION, noncanonical; Genesis lineage).

Its 6S-core states, at κ = 1 on the carrier 𝒞:
- there is no local C³ submersive factor E∘F₁⁶ = T′∘E for d = 1, 2, 3;
- no hypothesis is placed on T′ beyond C³.

By the E-conjugacy of RER-GEN-K3-MODAL, this is exactly the six-step contract for 𝒩⁶ = ℱ.

**Triadic corroboration, exact, own engine** (`triad_six_step_factor_burnside_check.py`, about 0.5 s):
- In rational modal coordinates, take the Jacobians DX₃(x) of the six-step cubic of ℱ at 5 rational points.
- They generate the full matrix algebra M₄(ℚ), of dimension 16.
- Hence no proper nonzero subspace is invariant under all DX₃(x). This is the Lemma S mechanism (note §2.1).
- Negative control `--control`: a block-diagonal cubic (sQ(s), cQ(c)) gives dimension 8 and the script exits 1.

**What the corroboration covers:** only the linear-algebra step, exactly and for the actual RER cubic. It does not redo steps 1–3 of note §3.1 (linear part, absence of a quadratic term, degree-3 cancellation). Those steps follow the same pattern as Genesis §6.3a (b)–(c). It does not touch the 6S-κ layer (ℝ⁶, H_spec).

**Coefficient cross-check:** the note's p(1) = 1/6 − i√3/9 and q(1) = −2i√3/9 agree with the fit of the two kernel fields in RER-TRIAD-FORMAL-INVOLUTION (ii), and with `TRIAD_KR_PY`'s input.

**Proposed new G5 row:**

> G5 — six-step-clock factors of ℱ = 𝒩⁶. A SESSION proof exists (K3 κ six-step note v0.3, 6S-core: no local C³ factor, d = 1–3, no hypothesis on T′), corroborated by the exact Triadic algebra check. It is not owner-adopted (Genesis v2.8.7 candidate). RER status: **OPEN at owner grade; SESSION-supported**. C¹/C² for d = 2 stays OPEN. The note's open items (the full hash of `k3_six_step_factor_check.py`; independent reruns of `kappa_pq_symbolic.py` and `lemmaS_hand_identities.py`) are not closed by this check. Those scripts are not in this workspace.

**RER-GEN-K3-MODAL** should keep "primitive clock" in its contract. It should add one [OPEN]→pointer line: "six-step contract: SESSION 6S-core (pending Genesis adoption); see G5". No change of grade.

## Pins

| file | SHA-256 |
|---|---|
| triad_six_step_factor_burnside_check.py (needs triad_formal_involution_birth_jet.py alongside) | 1ae0df35bfd437afc935c02d3d4559582ca66bd73a9a9d35253a5952274bf575 |
| triad_six_step_factor_burnside_check.log | 74e052552e0aa7c876ebe41db5c15e6596d1c4e55ffa713d4564eedea50c7e7b |
