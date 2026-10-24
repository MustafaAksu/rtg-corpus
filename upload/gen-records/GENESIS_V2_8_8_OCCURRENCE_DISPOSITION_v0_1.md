# Genesis v2.8.8 DRAFT (maintenance) — Occurrence Disposition v0.1

**Date:** 19 October 2026 · **State:** draft companion. Nothing is adopted; adopted Genesis v2.8.7 stays the owner file.

**Identities**
- **Baseline:** adopted v2.8.7 `d5d1e57c6eea0800cf8bf3e3f6b5905873e719df0969d15144ca55197cd2e361`. Line numbers below refer to this file.
- **Draft:** `RTG_GENESIS_GEOMETRY_DSN_v2_8_8_DRAFT.md`, `4dcf0185ab14815e34e06eb35dd52616d74cbf91726ff96e62f616c84923f884` (1577 lines).
- **Control:** manifest v0.1 `81939e5f…f542`, plus owner decisions D1–D4 and the two checker requirements of the 19 Oct review.

**Build.** `build_v2_8_8_draft.py` (`0b2270bb…c352`) applies 18 exact-once edits. Reversing them recovers v2.8.7 byte-exactly (gate M1c). The diff to v2.8.7 has 45 changed lines (`GENESIS_v2_8_7_to_v2_8_8_DRAFT.diff`, `9f36101b…ac8b`).

## 1. Edit-by-edit disposition

| ID | v2.8.7 line | Package | Change | S3 authorisation rule |
|---|---|---|---|---|
| H1 | 1 | G8-04 | title → v2.8.8_DRAFT | exact title |
| H2 | 4–5 | G8-04 | date 19 Oct (draft); status: DRAFT maintenance successor, not adopted, adopted owner v2.8.7 | prefix, "Not adopted", no claim tag |
| H3 | 7 | G8-04 | "Supersedes (on adoption)" adds v2.8.7 | exact prefix insertion |
| P11a | 11 (opening) | G8-04 | scope note → "v2.8.8 draft on the adopted v2.8.7 base; …" | prefix plus base chain |
| P11b | 11 (end) | G8-03 / D4 | maintenance sentence: live pins v6.4.13, historical v6.4.11 statements marked as such, ν₅⁽⁵⁾ attributed to `DYAD-ALG-NU5-P5`, "No scientific claim is added, changed or regraded." | append only; required phrases; no claim tag; no GEN RID |
| P1 | 8 | G8-01 | companion pin v6.4.11 → v6.4.13 | `new == old.replace(v6.4.11 → v6.4.13)` |
| P2 | 217 | G8-01 | P0-DYADIC: "repinned to Dyadic DSN v6.4.13 [v2.8.8; previous pins: v6.4.11 from v2.8.6, v6.4.10 before that]" | repin plus fixed history phrase |
| P3 | 282 | G8-01 | OPEN 9 primary ledger → v6.4.13 | pure repin |
| P4 | 582 | G8-01 | §4 routing cell → v6.4.13 | pure repin |
| P5 | 678 | G8-01 | §6.2 OPEN 9 imports primary ledger → v6.4.13 | pure repin |
| P6 | 1083 | G8-01 | §7 Dyadic import header → v6.4.13 | pure repin |
| P7 | 1129 | G8-01 | OPEN 16 continuity → v6.4.13 | pure repin |
| P8 | 1130 | G8-01 | OPEN 17 continuity → v6.4.13 | pure repin |
| P9 | 1164 | G8-01 | §8 P0-DYADIC import: "imported from Dyadic DSN v6.4.13 (…; previous pins: v6.4.11 from v2.8.6, v6.4.10 before that)" | repin plus fixed history phrase |
| P10a | 680 | G8-02 / D2 | ν₅⁽⁵⁾ formula byte-identical, followed by `` `[RID: DYAD-ALG-NU5-P5]` `` `` `[conv: one-step NF, declared K_5 family, frame W_p, resonant h=0]` `` | exact formula plus exact suffix |
| P10b | after 1093 | G8-02 | new §7 import line `DYAD-ALG-NU5-P5` (closed form, field, convention tag, Dyadic exact certificate) :: §6.2 OPEN 9 imports | one appended line; RID, tag, target; no GEN |
| APPA | before 1200 | G8-03 / D3 | Appendix A v2.8.8 DRAFT record: G8-01…04; M2c "source and numerical check RESOLVED; point-of-use metadata applied in this draft, effective on adoption"; replay recorded as [NUM] only | append only; required phrases; no backticked claim tag; no GEN RID |
| FOOT | 1561–1562 | G8-04 | draft footer; inherited v2.8.7 footer kept | prefix plus inherited tail |

**Not edited, by design:**
- **D1 historical anchors:** line 11 "v2.8.6 addition … synchronized to adopted Dyadic v6.4.11 and OFN v0.9" and line 29 "(v2.8.6: … Dyadic v6.4.11 §1, …)".
- **History and footer:** Appendix A records (lines 1213, 1229) and the inherited footer.
- **Science:** §6.3a, §6.3a.1, §6.3b (lines 725–849), SG-15, SG-16 and every line carrying the five K3/6S RIDs (24 lines).

## 2. Status after this draft (owner wording, 19 Oct)

- **M2c:**
  - source and numerical check: **RESOLVED**;
  - Genesis point-of-use metadata: applied in the draft, **PENDING RELEASE** until adoption.
- **D5 repin:** consumer compatibility is verified (D1–D7 8/8 on the adopted bytes). The new pin is **not in force** until v2.8.8 is adopted.

## 3. Gates (`check_v2_8_8_draft.py`, `eb1f3bb4…8435`)

| Gate | Content |
|---|---|
| M1a–c | baseline hash; fresh deterministic build equals the draft; every anchor occurs once; reverse edit list recovers v2.8.7 byte-exactly |
| M2 | upstream v6.4.13 SHA `5958f7fe…8542`; all 13 DYAD RIDs of the draft exist upstream; 8 cited values and ν₅ numerals printed verbatim (needs `--dyad`) |
| M3 | **anchor-based, not line-based** (owner requirement 1). The four historical anchors are removed textually (D1 sentences, P11b disclaimer, P2/P9 history phrase). After removal, no `v6.4.11` or `v6.4.12` remains in live text, and v6.4.13 appears ≥ 9 times. |
| M4 | §6.3a/§6.3a.1/§6.3b block (15 480 chars), SG-15, SG-16 and the 24 K3/6S RID lines byte-identical |
| M5 | ν₅ bullet = byte-identical formula plus exact RID and convention suffix |
| S1 | claim-tag counts and GEN RID set identical to v2.8.7 (delta `{}`) |
| S2 | DYAD RID set = v2.8.7 set ∪ {`DYAD-ALG-NU5-P5`} (13); no formal-ℤ₆ / Lemma F / F1–F3 / OPEN 19–20 RID |
| S3 | **rule-based authorisation** (owner requirement 2). Each of the 18 build edits must satisfy its own rule in the checker (table §1), written independently of the build text. It is not enough that "v2.8.8 / v6.4.13 appears"; every ID must be used exactly once. |
| S5 (optional) | `genesis_nu5_p5_replay.py` hash plus 4/4 PASS; [NUM] evidence, not an acceptance condition |

**Results here.**
- **Development mode** (`checker_output_dev.txt`, `a10e0efb…f9f6`): 10/10 executed PASS, including S5. M2 is SKIP because `--dyad` was not given.
- **`--final` without `--dyad`:** exit 1, as required, since a SKIP counts as FAIL.
- **`--final --dyad`:** not run here, because the adopted v6.4.13 bytes are not in this workspace. The owner holds the verified file (`5958f7fe…8542`). This run is the remaining acceptance step:

```
python check_v2_8_8_draft.py --base RTG_GENESIS_GEOMETRY_DSN_v2_8_7.md --draft RTG_GENESIS_GEOMETRY_DSN_v2_8_8_DRAFT.md --build build_v2_8_8_draft.py --dyad RTG_DYADIC_OSCILLATOR_DSN_v6_4_13.md --replay genesis_nu5_p5_replay.py --final
```

Expected result: 11/11 PASS, exit 0.

**Negative controls** (`negative_controls_output.txt`, `e4a56459…36c4`; all exit 1):

| Tampering | Caught by |
|---|---|
| undeclared word change in §6.3a.1 (draft) | M1b, M1c, M4 |
| build smuggles a `DYAD-THM-FORMAL-Z6-GENERATOR` import | S2, S3 |
| build omits P3, leaving a live v6.4.11 | M3, S3 |
| build changes a ν₅ numeral | M5, S3 |
| build repins one pointer to v6.4.12.1 | M3, S3 |
| `--dyad` given wrong upstream bytes | M2 |

## 4. After review

1. Independent receiving review of the draft bytes, this disposition, the build and the checker, run with `--final --dyad`.
2. Owner adoption decision.
3. A metadata-only release transform and release checker, on the v2.8.7 pattern. It turns "draft maintenance", "DRAFT record (not adopted)" and the footer into their adopted forms, and records M2c and D5 as in force.
4. Outbound notices citing the adopted hash:
   - **Dyadic N8:** RECEIVED, with repin executed.
   - **RRF / FMS / OFN:** informational only; K3/6S exports are unchanged.
