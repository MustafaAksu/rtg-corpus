# Genesis v2.8.6 — Owner-Pass Scope Manifest and Occurrence Map v0.1

**Date:** 16 October 2026
**State:** Stage B preparation manifest only (authorized by the Genesis owner decision of 16 Oct 2026). No owner edit, no draft, no RID finalized, no adoption. Adopted Genesis v2.8.5 and the frozen GCL are unchanged.
**Target:** `RTG_GENESIS_GEOMETRY_DSN_v2_8_6_DRAFT`, built on the exact adopted v2.8.5 bytes.

## 0. Pinned inputs

| Input | Role | SHA-256 |
|---|---|---|
| `RTG_GENESIS_GEOMETRY_DSN_v2.8.5` | owner baseline (all line numbers below refer to this file) | `41ed76602c1c87c42972ac5b3f0a53f6973ac484427473ac371c57db1ab475cf` |
| `RTG_DYADIC_OSCILLATOR_DSN_v6.4.11` (adopted 16 Oct 2026) | upstream source for N1/N2/NF6 | `6fccd429758adb729032a68c2a99e24a7bab6f5226aae5df1453b09b189ccb2e` |
| `K3_CUBIC_FACTOR_OBSTRUCTION_SESSION_RECORD_v0_1_2.md` | Stage-A proof record (G-B01 source) | `9f95d48d23a340738146271d4bcf1a483b04252e9210c9f403a7f23172dd083a` |
| `k3_obstruction_exact_check.py` | exact source-data certificate for G-B01 | `384aaa5f17ecd0786960b3a97fc08a5d332c9e12809a2c92796616f2615a01ee` |
| `GENESIS_V2_8_5_OWNER_PASS_QUEUE_v0_3.md` | prior successor queue (see §4, naming collision) | `71b17a73e2b138ee83666d673ff2fdb22c04beab221e7b0df9d34750422230d5` |

All Dyadic RIDs that v2.8.5 currently cites resolve in v6.4.11: `DYAD-THM-C21`, `DYAD-ALG-LIEGAUGE-NORM`, `DYAD-ALG-P567-LEDGER`, `DYAD-ALG-GLATTICE5`, `DYAD-ALG-ALIAS-PHASE`, `DYAD-ALG-A1A2-LIEGAUGE`, `DYAD-CAND-P0-DYADIC`. The pointer refresh therefore hides no deleted RID. A value-by-value check is still a gate (§5, M2).

## 1. Scope

**In:** G-B01 K3 theorem · G-B02 N1 alias · G-B03 N2 repin (plus NF6 citation only where the chart h is actually used) · G-B04 RRF G2-CLOCK export statement · G-B05 provenance · mechanical Dyadic pointer refresh v6.4.10 → v6.4.11.

**Out:** physical network–dyad bridge; OPEN-B/E1 selection; analytic odd carrier (Problem B); optional V20-O1–O5; Candidates A–C; Dyadic OPEN 19 (Dyadic-owned, not re-proved here); Q-2.8.6-01 UV-interface type split (trigger not met, see §4); any GCL edit.

## 2. Work packages and occurrence map (v2.8.5 line numbers)

### G-B01 — K3 planar-factor obstruction (new owner theorem candidate)

| Location | Action |
|---|---|
| new §6.3a (after §6.3, before §6.4 at line 718) | Insert theorem block: statement, four-step proof, dimension table (d=1,3 at C¹; d=2 at C³), scope/OPEN. Text from SESSION v0.1.2 §1–§4; proposed RID `GEN-THM-K3-PLANAR-FACTOR-NOGO` (name is an owner decision). |
| §1 Current Canonical State (after the OPEN 1C pump entry, line 49) | One-line `[THM]` summary with the §6.3a pointer. |
| §5 High-Risk Claims Ledger (table from line 589) | New row. Valid: "no local C³ rank-2 planar factor (any target); d=1,3 none at C¹". Forbidden: "projected K3 has no node-exchange symmetry", "physical network realization excluded", "C¹/C² d=2 excluded". |
| §3 Scope Guards (after SG-14, line 558) | Proposed SG-15: the no-go concerns semiconjugacy of the named projected K3 primitive map only. It does not select or exclude a physical node exchange, a carrier, or a network–dyad bridge, and it does not make EF=TE and EF=T⁶E equivalent. |
| §7 Export protocol (line 996) | Add the K3 no-go to the theorem-grade exportable list, with its scope. |
| §8 Artifact Registry | New RID entry: proof = SESSION v0.1.2 §2; data certificate = `k3_obstruction_exact_check.py`; confirmatory = `fac.py`, `exact_chiral.py`, `k3.py` [NUM]. |

**Typing to preserve:** source primitive cited as `DYAD-DEF-PRIMITIVE-MAP` (alias, G-B02). (ν, χ) are triad-network coefficients and are not the dyad μ₆ (ER-2B §2). The relation to Dyadic §6.15 is an analogy, not a dependency.

### G-B02 — N1: primitive-map alias

| Line | Current | Action |
|---|---|---|
| 29 | `[RID: GEN-DEF-PRIMITIVE-MAP]` §1 | Keep the RID and add: "import/alias of `DYAD-DEF-PRIMITIVE-MAP` (Dyadic v6.4.11 §1; custody OFN CUST-O09-01). Genesis network theorem RIDs unchanged." |
| 624 §6.1 boxed T | `[DEF]` "RTG dyad generator", no RID | Add a cross-reference to the same alias. Do not create a third RID. |
| 569 §4 routing | "Genesis §6.1–§6.3; Dyadic §6.1" | No change (already correct). |
| §7 Dyadic import list | — | Add an import line for `DYAD-DEF-PRIMITIVE-MAP` (definition-level). |

### G-B03 — N2: frame / protection-matrix repin (+ NF6 where used)

| Line | Current | Action |
|---|---|---|
| 956 | `[RID: DYAD-ALG-LIEGAUGE-NORM] :: Birkhoff frame, v⊥, antisymmetric channel, protection matrix … [conv: Lie strict-kernel gauge]` | Split into three. (a) Linear frame W=ℒ(ρ,η), v⊥ → `DYAD-DEF-BRIDGE-EXPORT-CONTRACT` (item 1, no gauge). (b) Protection matrix → `DYAD-ALG-PROTECTION-MATRIX` (linear eigenframe, cubic order). (c) "Antisymmetric channel" is **not** a contract item; the Genesis §6.2 `[THM]` (line 642) is Genesis-native, so mark it local, not imported (owner check D3). Remove the Lie-gauge tag from (a)/(b); keep `DYAD-ALG-LIEGAUGE-NORM` only if some live text still uses the archival Lie-gauge normalization. |
| 570 §4 routing | "μ₆, τ, v⊥, antisymmetric channel — DYAD-THM-C21" | Point v⊥ to the contract RID; μ₆ and τ stay on C21. |
| 640 §6.2 eigenframe | `[ALG]` W, s, c, v⊥, no RID | Add a source pointer to the contract item (a). |
| 653, 685 | "adopted isolated-dyad normalizing chart h" | Cite `DYAD-ALG-NF6` here only (the two places h is actually used). Do not add it elsewhere. |
| 662 OPEN 9 imports | c_θ^(6) `[conv: Lie strict-kernel gauge]` | No change; legitimate archival-gauge use. Pointer refresh only. |

### Mechanical pointer refresh (Dyadic v6.4.10 → v6.4.11)

Lines 8 (companion header), 211 (P0-DYADIC status), 276 (OPEN 9), 662, 951 (§7 header), 993, 994, 1024 (§8 P0). Historical lines 1066 and 1331 stay unchanged (version history).
**Optional, owner decision D2:** line 8/989 OFN v0.8 → v0.9 (adopted). This is mechanical, but outside the stated N1/N2 scope.

### G-B04 — RRF G2-CLOCK export

Export only: "the projected K3 primitive map has no local C³ submersive factor of strictly lower real dimension; d=1,3 already at C¹; d=2 C¹/C² OPEN; Genesis RID [name]". RRF cites it and does not repeat the proof. Genesis does not select RRF's physical admissibility condition. Delivered as a §7 export line plus an outbound notice. No RRF edit by Genesis.

### G-B05 — Provenance

The draft carries a provenance block: SESSION v0.1.2 SHA, certificate SHA, Dyadic v6.4.11 SHA, ER-2B Observable Response v1 package SHA `06d5e0c9…82b1` (historical coefficient source), and `K3_factor_obstruction.zip` `046ac458…85cc` with its open item (no internal manifest; `fac.py` receipt pending, confirmatory only).

## 3. Status-summary and changelog entries

- **Status summary:** one added sentence (K3 no-go; Dyadic v6.4.11 sync). Existing items (i)–(x) unchanged.
- **Appendix A:** a v2.8.6 entry listing G-B01–05 and the mechanical refresh. "No v2.8.5 claim corrected or retracted" must be verifiably true (tag-count audit, §5).

## 4. Naming collision — decision required (D1)

Queue v0.3 already reserves `Q-2.8.6-01` for the UV-interface type split (H_V/H_* , M_V/M_*, ℓ). Its trigger is the OPEN-M Task-3 return, which has **not** occurred. This manifest therefore excludes it from v2.8.6. Options:
- (a) rename it `Q-SUCC-UV-01`, version-agnostic, in queue v0.4;
- (b) keep the ID and record "deferred past v2.8.6".

Recommendation: (a). An ID that names a version it will not ship in invites a false "v2.8.6 resolved Q-2.8.6-01" reading.

## 5. Gates (checker for the draft)

| # | Gate |
|---|---|
| M1 | Baseline v2.8.5 SHA pinned; frozen GCL, adopted Dyadic/Triadic/RRF files unmodified by the build. |
| M2 | Every refreshed Dyadic pointer: cited RID present in v6.4.11 **and** cited value unchanged (μ₆, τ, p=5,6,7 ledger, alias phase, a₁/a₂, λ=e^{iF_f/2}). |
| M3 | Line 956 no longer routes frame/v⊥/protection matrix through `DYAD-ALG-LIEGAUGE-NORM`. |
| M4 | `DYAD-ALG-NF6` appears only at the h-chart uses (653, 685 equivalents). |
| M5 | `GEN-DEF-PRIMITIVE-MAP` still present and resolves to the identical formula; alias recorded. |
| S1 | New theorem text matches SESSION v0.1.2 statement and scope verbatim in substance; `k3_obstruction_exact_check.py` reruns 8/8, χ=1/4 control exits 1. |
| S2 | No claim in the draft states node-exchange exclusion, physical realization, C¹/C² d=2 exclusion, or EF=TE ⇔ EF=T⁶E. |
| S3 | Tag-count audit vs v2.8.5: only additions (new `[THM]`, `[DEF]` lines); no tag decrease; no `[COR]`/`[RETRACTED]` added. |
| S4 | Q-2.8.6-01 content absent from the draft (or D1 resolved otherwise). |

## 6. Owner decisions needed before drafting

- **D1:** Q-2.8.6-01 naming (§4).
- **D2:** include the OFN v0.8 → v0.9 pointer refresh, or leave it.
- **D3:** confirm the "antisymmetric channel" is Genesis-native and should not be imported (line 956 split).
- **D4:** RID names for the theorem (`GEN-THM-K3-PLANAR-FACTOR-NOGO` proposed) and for SG-15.
