# C7B-DISC-2 — RATIFIED RESULT

**Memo ID:** `NG_C7B_DISC2_RESULT_v1` · **Date:** 2026-09-03 · **Auditor:** Claude
**Ruling:** PI, 2026-09-03 — **RATIFIED.**
**Protocol:** `NG_C7B_DISC2_PREREG_v1.md` (frozen `db87b455…919da9`), unchanged throughout.

---

## 1. Owner-facing statement

> `[RESULT] [NUM/ALG under frozen protocol]` **C7B-DISC-2 CLOSED — B-check PASS · D-check PASS.** The registered supplementary one-pass family yields 136 same-realization dynamic witnesses, 130 interior and 6 boundary-only, admitting eight new labels. Consequently `{1, 3/2, 2, 3, 4, 4/3, 5, 5/2, 7/2, 9/4} ⊆ Q_RTG^dyn`. **This is a certified lower bound on the dynamic realization spectrum, not an exhaustiveness theorem.**

Terminology: **DISC-2/B-check** and **DISC-2/D-check** under the frozen criterion, reported through legacy harness keys `disc1b` / `disc1d`. DISC-1 was not rerun.

## 2. Result

| | |
|---|---|
| domain | registered supplementary one-pass family, `\|d\|_c = 3,4,5`, 10368 seeds |
| base dual-active | 7468 |
| non-`1` base classes | 7336 → **B-check PASS** |
| survive `k = 1→2` stability fence | 208 |
| certified witnesses | **136** = 130 `PASS_INT` + 6 `PASS_BDY_ONLY` → **D-check PASS** |
| A1 owner recount | **544/544 exact** |
| A2 T4 certificates | **136/136 valid** |
| A3 domain / same-`x` reconstruction | **136/136 valid** |

**Newly ratified:** `1, 3/2, 4, 4/3, 5, 5/2, 7/2, 9/4 ∈ Q^dyn`. `2` and `3` were already ratified by DISC-1 and receive additional witnesses here.

## 3. The `1:1` upgrade, stated precisely

`1 ∈ Q^bd` was established by N5-PHYS-1 through a bounded **positive control**. DISC-2 independently establishes

```
1 ∈ Q^dyn
```

through 26 dynamically discriminating SWAP/P3 realizations (24 interior, 2 boundary). Same numeral, different and stronger epistemic status — admissible exactly because the label-neutrality ruling makes `Q^dyn` membership existential through a certified realization rather than a property of the numeral.

## 4. `k = 0` retention was load-bearing — `[COR]`

All six boundary witnesses hold the base class at `k = 1, 2, 3` and break it only at `k = 0`:

```
2:1  x4   (10,4) → (6,3) → (6,3) → (6,3)     5:2 → 2:1 → 2:1 → 2:1    C_0 = 2
1:1  x2   (33,3) → (3,3) → (3,3) → (3,3)    11:1 → 1:1 → 1:1 → 1:1    C_0 = 30
```

**All 6/6 disappear if `k = 0` is removed.** `[COR]` My earlier "four of six" was wrong — four is merely the size of the `2:1` boundary block. The architectural ruling to retain `k = 0` on grounds of axis integrity, made when DISC-1 had produced zero boundary passes, is now empirically load-bearing.

## 5. A5 does not modify the verdict

The mirror pattern `8, 26, 34, 34, 26, 8` across signed `d = -5…+5`, and the `42, 52, 42` distribution over `D_AB`, are descriptive consistency features. They are **not** an admission condition, independence test, or mechanism theorem. Concentration within the registered one-pass family would bear on realization **robustness**, never on existential membership.

## 6. What closes, and what does not

- **C7B-DISC-1:** CLOSED · **C7B-DISC-2:** CLOSED
- **C7B global breadth:** **OPEN** — no theorem establishes the full positive-rational spectrum
- **C7C physical rational arithmetic:** **OPEN**
- No claim that `Q^dyn = Q_{>0}`; no claim that the ten established labels exhaust `Q^dyn`

## 7. Artifact manifest

```
db87b45565f6c5e59ef4797abde8514d89586c1b56bfe303d29ec6fb33919da9  NG_C7B_DISC2_PREREG_v1.md      (frozen protocol)
9d787b435c42fd2024c81e614e3c6e3e076dc2bd30ad1e7e286ada8e6dfe675e  genesis_mode_b_mc_v18.py       (pinned owner)
57a15421b352f8fbe58d7642d78a6ebb936b78aae90d91b9e39034b738510d9d  disc1_analysis_harness_v1.py   (sealed engine)
b7cee9220f73252af3b7322b50a67ecff4227424b6b1309f241d5e24babb35df  disc2_supplementary_enumerator_v3_1.py
baadcdad3b048713329d30fddb3c34bd47c198db82157a6978063c59ef017760  disc2_witness_report_v2.py
3dc8317b1bf0136295e55aa6c43cc00c44006cbfae34d2ae00984acf040398f9  disc2_ratification_audit_v1.py
6840f822e9674329aeb8217b23eda14013334ab8a3cbad5b6f66a597ed5acc0a  disc2_enumeration_sup_d345.json
544a5f815182f435e188cd7433c6844e6bbdfcd9b7a43a70e42e96b062d106ef  disc2_transport_sup_d345.json
7b6d0b5983a42216d50f4110a5b33dd19f8b3c2f8e6b7930258aaf475222c0b4  disc2_harness_result.json
ccc8457086b01193bdec598a7db44508be8486659ae07feb4df15a66401faa7d  disc2_witness_report.json
1ad96df282fbb396f24b8ef8a4763c861279a0787df353703d7c139e781393d3  disc2_ratification_certs.json
```

**Line-ending provenance.** `disc2_ratification_certs.json` is declared **canonical in LF**, hashing to `1ad96df2…393d3`. A CRLF rendering of identical content hashes to `e71475c5…d9cc09`; reproduced and confirmed as serialization, not content. Recorded so the archive has one canonical byte representation.
