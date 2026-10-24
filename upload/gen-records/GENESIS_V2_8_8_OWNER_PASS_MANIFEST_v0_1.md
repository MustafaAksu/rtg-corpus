# Genesis v2.8.8 — Maintenance Owner-Pass Manifest and Occurrence Map v0.1

**Date:** 19 October 2026
**State:** Stage B preparation manifest only, authorized by the Genesis owner review of 19 Oct 2026 ("Genesis v2.8.8 maintenance DRAFT: AUTHORIZED"). It makes no owner edit, produces no draft and adopts nothing. Adopted Genesis v2.8.7 is unchanged.
**Target:** `RTG_GENESIS_GEOMETRY_DSN_v2_8_8_DRAFT`, built deterministically on the exact adopted v2.8.7 bytes.
**Character:** source and convention maintenance only. The draft adds no scientific claim, claim tag or GEN RID. It changes no K3/6S statement.

## 0. Pinned inputs

| Input | Role | SHA-256 |
|---|---|---|
| `RTG_GENESIS_GEOMETRY_DSN_v2.8.7` (adopted 18 Oct) | baseline; every line number below refers to it (1564 lines) | `d5d1e57c6eea0800cf8bf3e3f6b5905873e719df0969d15144ca55197cd2e361` |
| `RTG_DYADIC_OSCILLATOR_DSN_v6.4.13` (adopted 18 Oct) | new upstream pin | `5958f7fe8a3e0ec94546cb7e915c5f690d09827a3d680d13a17c9d880b968542` (owner-verified on the adopted bytes, 19 Oct) |
| `GENESIS_DYADIC_v6_4_13_CONSUMER_IMPACT_v0_1.md` | consumer record (accepted) | `1e412c43bc14a2ddd05f9588fdc72795129b878fb7885816a70797ab3c8138d1` |
| `check_genesis_dyad_v6_4_13_consumer.py` | source audit: D1–D7 8/8 PASS on real bytes (owner run) | `db9000ce27e5adb0fd399e1c89762795beece95309e2f3eed0085f6b80c1bfad` |
| `genesis_nu5_p5_replay.py` | ν₅⁽⁵⁾ replay `[NUM]`, C1–C4 4/4 PASS (owner run) | `34bab14033a1f6bdf51f47e5c9694de43b68c2e05e6f410a7d6fa91e27f661cb` |

## 1. Scope

**In:**
- **G8-01** Repin the live Dyadic pointers from v6.4.11 to v6.4.13. This skips v6.4.12 and v6.4.12.1 and executes the deferred D5.
- **G8-02** Source attribution for ν₅⁽⁵⁾ via `DYAD-ALG-NU5-P5`, with the owner-approved convention tag at §6.2 and a §7 import line.
- **G8-03** Record the M2c closure in the status sentence and in Appendix A.
- **G8-04** Mechanical header and footer changes.

**Out:**
- any import of `DYAD-THM-FORMAL-Z6-GENERATOR`, `DYAD-CAND-FLAT-CENTRALIZER` or `DYAD-CAND-SMOOTH-CENTRALIZER-COROLLARIES`, or of other v6.4.12/v6.4.13 results (OPEN 19/20 material);
- any change to the K3/6S statements, SG-15 or SG-16;
- physical G2, OPEN-B/E1 and γ selection;
- new GEN RIDs or claim tags;
- the Triadic repin (not a Genesis action);
- FMS/OFN content.

**Frozen byte-identical (gate M4):**
- §6.3a, §6.3a.1 and §6.3b in full (adopted lines 725–849, up to §6.4 at line 850);
- SG-15 and SG-16;
- every line carrying `GEN-THM-K3-PLANAR-FACTOR-NOGO`, `GEN-THM-K3-SIXSTEP-FACTOR-NOGO`, `GEN-THM-MEANFEEDBACK-SIXSTEP-NOGO`, `GEN-THM-CHIRAL-CUBIC-FACTOR-LEMMA` or `GEN-DEF-MEANFEEDBACK-FAMILY`.

## 2. Occurrence map (v2.8.7 line numbers)

v2.8.7 contains 14 occurrences of `v6.4.11`. Eleven are live; three are in the version history or footer.

### G8-01 — live pointers

| ID | Line | Current text (excerpt) | Proposed replacement |
|---|---|---|---|
| P1 | 8 | companion `RTG_DYADIC_OSCILLATOR_DSN_v6.4.11` | `…v6.4.13` |
| P2 | 217 | `(repinned to Dyadic DSN v6.4.11 [v2.8.6; previously v6.4.10]; …` | `(repinned to Dyadic DSN v6.4.13 [v2.8.8; previously v6.4.11 (v2.8.6), v6.4.10]; …` |
| P3 | 282 | `see `RTG_DYADIC_OSCILLATOR_DSN_v6.4.11` for the primary ledger` | `…v6.4.13…` |
| P4 | 582 | §4 routing cell `Dyadic DSN v6.4.11` | `Dyadic DSN v6.4.13` |
| P5 | 678 | `primary ledger in `RTG_DYADIC_OSCILLATOR_DSN_v6.4.11`` | `…v6.4.13…` |
| P6 | 1083 | `### From `RTG_DYADIC_OSCILLATOR_DSN_v6.4.11`` | `…v6.4.13…` |
| P7 | 1129 | OPEN 16 `closed in `…v6.4.11`` | `…v6.4.13…` |
| P8 | 1130 | OPEN 17 `closed under its declared convention in `…v6.4.11`` | `…v6.4.13…` |
| P9 | 1164 | `imported from Dyadic DSN v6.4.11 (`DYAD-CAND-P0-DYADIC`, conditional only; previously pinned v6.4.10)` | `imported from Dyadic DSN v6.4.13 (`DYAD-CAND-P0-DYADIC`, conditional only; previously pinned v6.4.11, v6.4.10)` |

**Dated annotations (decision D1).** Two live occurrences are dated statements about v2.8.6:
- line 11: the status-summary sentence "**v2.8.6 addition:** … synchronized to adopted Dyadic v6.4.11 and OFN v0.9";
- line 29: "*(v2.8.6: recognized as import/alias of `DYAD-DEF-PRIMITIVE-MAP`, Dyadic v6.4.11 §1, …)*".

Both are true as history. Recommendation: **leave them unchanged**, because the new v2.8.8 status sentence (P11) states the current pin. Alternative: append "(current pin: v6.4.13)" to both.

**History and footer, not edited:** lines 1213 and 1229 (Appendix A records) and 1563 (inherited footer).

### G8-02 — ν₅⁽⁵⁾ attribution and convention

| ID | Line | Change |
|---|---|---|
| P10a | 680 | `- $p=5$: $\nu_5^{(5)} = …{48}$` → same formula, byte-identical, followed by ` [RID: DYAD-ALG-NU5-P5] [conv: one-step NF, declared K_5 family, frame W_p, resonant h=0]`. The tag text is verbatim from the owner review; D2 decides whether it is backticked. |
| P10b | after 1093 | New §7 import line: `- [RID: DYAD-ALG-NU5-P5] :: $\nu_5^{(5)}$ closed form, exact over $\mathbb{Q}(\sqrt5,\sqrt{10+2\sqrt5})$ `[conv: one-step NF, declared K_5 family, frame W_p, resonant h=0]` (certificate `dyad_m2c_nu5_p5_exact.py`, Dyadic owner) :: §6.2 OPEN 9 imports` |

**Tag counting.** The existing tag grammar does not count `[conv: …]` and `[RID: …]` as claim tags. Claim-tag counts therefore stay identical; gate S1 checks this. The DYAD RID set grows from 12 to 13, with `DYAD-ALG-NU5-P5` as the only addition (gate S2).

### G8-03 / G8-04 — summary, history, header, footer

| ID | Line | Change |
|---|---|---|
| H1 | 1 | title → `v2.8.8_DRAFT` |
| H2 | 4–5 | date 19 Oct 2026 (draft); status DRAFT maintenance successor, not adopted; adopted owner stays v2.8.7 (`d5d1e57c…e361`) |
| H3 | 7 | "Supersedes (on adoption)" adds v2.8.7 |
| P11a | 11 (opening) | `*(v2.8.7 adopted release on the v2.8.6 base;` → `*(v2.8.8 draft on the adopted v2.8.7 base; v2.8.7 is built on the v2.8.6 base;` |
| P11b | 11 (end) | append "**v2.8.8 draft maintenance:** Dyadic pins move to adopted v6.4.13. The ν₅⁽⁵⁾ closed form is attributed to `DYAD-ALG-NU5-P5` with its normalization convention (M2c closed). No scientific claim is added, changed or regraded." |
| APPA | before line 1200 | Appendix A v2.8.8 DRAFT record. It covers G8-01…04 and D1–D4, and the M2c closure: source `DYAD-ALG-NU5-P5`, Dyadic exact certificate, Genesis replay `genesis_nu5_p5_replay.py` (`34bab140…61cb`) `[NUM]` 4/4 PASS, and convention sensitivity ΔIm n₃₂ = 0.01127 at h₂₁ = i/10. It also states "No v2.8.7 claim corrected, regraded or retracted." |
| FOOT | 1561–1562 | draft footer; inherited v2.8.7 footer kept |

**Where the replay is recorded (decision D3).** Recommendation: only in Appendix A and the release record, not as a §8 artifact RID. A §8 entry would need a new GEN RID, and the owner review excludes new RIDs. The replay is `[NUM]`; the exact certificate remains the Dyadic owner's.

## 3. Gates (checker for the draft)

| # | Gate |
|---|---|
| M1a–c | v2.8.7 baseline SHA; a fresh deterministic build equals the draft; every anchor occurs exactly once; reversing the edit list recovers v2.8.7 byte-exactly. |
| M2 | Upstream v6.4.13 SHA `5958f7fe…8542`. All 13 DYAD RIDs cited by the draft exist in v6.4.13. The 8 cited values and the ν₅⁽⁵⁾ numerals are printed verbatim there. |
| M3 | `v6.4.11` survives only at the whitelisted places: lines 11 and 29 (if D1 = leave), Appendix A and the inherited footer. No live pointer names v6.4.12 or v6.4.12.1. |
| M4 | §6.3a, §6.3a.1, §6.3b, SG-15, SG-16 and every line carrying one of the five K3/6S RIDs are byte-identical to v2.8.7. |
| M5 | The ν₅⁽⁵⁾ formula substring is byte-identical; the same bullet carries `DYAD-ALG-NU5-P5` and the exact convention tag. |
| S1 | Claim-tag counts are identical between v2.8.7 and the draft, and the GEN RID set is identical (no new scientific claim or RID). |
| S2 | DYAD RID set = v2.8.7 set ∪ {`DYAD-ALG-NU5-P5`}. No `DYAD-THM-FORMAL-Z6-GENERATOR`, `DYAD-CAND-FLAT-CENTRALIZER`, `DYAD-CAND-SMOOTH-CENTRALIZER-COROLLARIES` or other OPEN 19/20 RID. |
| S3 | Diff discipline: every changed or added line outside Appendix A is a P-, H- or FOOT-listed line, and each contains `v6.4.13`, `v2.8.8`, `DYAD-ALG-NU5-P5` or header metadata. |
| S4 | Negative controls: an undeclared word change in §6.3a.1 fails M1/M4; a smuggled `DYAD-THM-FORMAL-Z6-GENERATOR` import fails S2; a residual live `v6.4.11` pointer fails M3; a ν₅ numeral change fails M5. |
| S5 (optional, `--replay`) | `genesis_nu5_p5_replay.py` hash check and exit 0. Reported as `[NUM]` evidence, not as a draft-acceptance condition. |

The upstream byte gate (M2) needs the real v6.4.13 file (`--dyad`). In development mode a missing `--dyad` is reported as SKIP; in `--final` mode a SKIP counts as FAIL, as in v2.8.7.

## 4. Owner decisions needed before drafting

- **D1 — dated annotations (lines 11, 29).** Recommended: leave unchanged. Alternative: append "(current pin: v6.4.13)".
- **D2 — convention-tag formatting at §6.2.** Recommended: the owner-approved text verbatim, backticked as metadata (`` `[conv: …]` ``), matching the Genesis `[conv: Lie strict-kernel gauge]` usage at the same line block.
- **D3 — where the replay is recorded.** Recommended: Appendix A and the release record only; no §8 RID.
- **D4 — status-summary sentence (P11b).** Recommended: include it, so that the live pin is stated once in the summary. Alternative: header and Appendix A only.

## 5. Outbound (after adoption, citing the adopted hash)

- **→ Dyadic (N8):** the RECEIVED text from the owner review of 19 Oct, plus "repin executed in Genesis v2.8.8 (`<sha>`); `DYAD-ALG-NU5-P5` imported with its convention."
- **→ RRF / FMS / OFN:** informational only. Genesis K3/6S exports are unchanged.
