> **[SUPERSEDED 2026-09-30] by NG_C7C_M2_CENSUS_PROTOCOL_v1.md (C-1/C-2/C-3 ruled; F5 repaired). Content without this banner hashes to 3979531421eba363170378817105a4466d398174b34505670c1b051de14021a0.**

# C7C-M2 Evidence-Sufficiency Census — Protocol DRAFT v1

**Doc ID:** `NG_C7C_M2_CENSUS_PROTOCOL_DRAFT_v1` · **Date:** 2026-09-30
**Governed by:** frozen preregistration `NG_C7C_M2_PREREG_DRAFT_v4` (`248f128c…8987`) and its freeze manifest (`cefb7180…b165b`). Where this protocol and the preregistration differ, the preregistration governs.
**Status:** DRAFT for freeze. No record has been examined under this protocol.

> **Hard guard.** The census tests evidential reconstructability only. It does not evaluate interface equivalence, Π, N1/N2, WD-DOM, or any PASS/FAIL condition. A record is admissible when the frozen evidence is sufficient for those questions to be decided later without generating new data or changing the preregistered definitions.

---

## 1. Unit and universe

**Unit.** One *record* = one certified pair `x = (A,B)` of the carrier, with its frozen provenance. Chains `(x,[φ],y)` are **not** formed in the census; chain formation is analysis.

**Universe (fixed by rule, applied in this order).**
- **U-DYAD:** every pair certified in Number Genesis v1.20.6 as a member of the carrier within the continuous-dyad family, identified by its defining owner block.
- **U-TDRG:** see decision **C-2** (§6). Default proposed: the DISC-1 and DISC-2 **witness** records (22 + 136), because P2 exposure is audited for exactly these.

The universe is enumerated by the rule, completely, before any field is assessed. No record is added or dropped afterwards; a record that cannot be located is reported NOT ADMISSIBLE with reason `R0-MISSING`.

## 2. Frozen fields (assessed in order; each is PASS / FAIL with a reason code and an evidence pointer)

| # | field | PASS iff | frozen basis |
|---|---|---|---|
| **F1** | record identity / provenance | artifact name, hash/version, owner, frozen source and (if applicable) witness ID are all present and the hash verifies | G-sufficiency |
| **F2** | family eligibility | the record maps to one registered family, **and every component of `κ_b`** — schema key, owner+version+hash, sector-class key, gauge policy, orientation/event semantics, common-order semantics — is reconstructable from its provenance | prereg §4.3; G-sufficiency |
| **F3** | interface-data reconstructability | at **both** ends, `B`, the prefix poset `𝒫`, and the single-stream attachment `ι = N_B` on `𝒫` are defined from the record; no bounded class, ratio, label or fate is used to define them | prereg §2, §3 |
| **F4** | witness-germ assessability | the data required to **evaluate** a candidate tail representative later are present: explicit order structure of `𝒫` and the count functions of F3. **The census does not construct any `φ`, does not decide whether one exists, and computes no discrepancy bound.** | prereg §2, §4.1; G-sufficiency |
| **F5** | Π-decidability provenance | independent certified provenance exists from which `R_pair` membership of a transported outer pair involving this record's streams **could be adjudicated**: instance identity (which orbit/realization each stream lives on), common-order structure, prefix-cofinal repeatability data. Recorded as *decidable: yes/no*, **never as Π true/false**. A witness germ is not such provenance (G-bridge) | prereg §2 (Π, T-inv, G-bridge); G-sufficiency |
| **F6** | P2 eligibility (TDR-G only; dyad records: N/A) | the record is P2-unexposed, **or** carries a separate policy-independence certificate | G-P2 |

**F7 — verdict.** `ADMISSIBLE_FOR_M2_ANALYSIS` iff F1–F6 all PASS (F6 N/A counts as PASS for dyad records); otherwise `NOT_ADMISSIBLE_FOR_M2_ANALYSIS` with the **first** failing field and its reason code.

**Forbidden columns — must not appear in any census output:** N1, N2, Π truth value, `≈_L`, `~_a`/`~_b` verdicts, existence of `φ`, discrepancy bounds, WD-DOM, PASS/FAIL of M2, any rational label or bounded class used as a sorting or selection key.

## 3. Evidence rules

- **E-frozen.** Only frozen artifacts whose hashes verify against their manifests.
- **E-nonew.** No new seed, trajectory, parameter, panel, or event policy (G-search).
- **E-rederive.** See decision **C-1** (§6).
- **E-noeval.** If assessing a field would require deciding interface equivalence or Π, the field is scored on **availability of the data** only; the question itself is left for analysis.

## 4. Order of application
1. Freeze this protocol.
2. Enumerate U-DYAD and apply F1–F7.
3. Then enumerate U-TDRG and apply F1–F7.
4. Report each family separately. The report closes the census; it contains no analysis.

## 5. Output format
One row per record: `record_id · family · F1 … F6 (PASS/FAIL/N-A + reason code + evidence pointer) · F7 verdict`. Reason codes: `R0-MISSING`, `R1-HASH`, `R2-KEY` (which `κ_b` component), `R3-IFACE` (which end, which datum), `R4-ORDER`, `R5-PROV` (which provenance item), `R6-P2`. A summary counts admissible and non-admissible records per family and per first-failing field — nothing else.

## 6. Decisions required before freeze

**C-1 — deterministic re-derivation.** The DISC artifacts store cycle-level counts, not the per-prefix count functions `ι` that F3/F4 need. Those can be recovered only by re-running a frozen seed's own trajectory with the pinned owner code. Proposed rule: *re-deriving a frozen record's own trajectory from its frozen seed and frozen parameters, with the hash-verified pinned owner code, is reconstruction of that record, not new data; any other seed, parameter or code is new data (G-search).* If this is not adopted, DISC records are expected to fail F3 with `R3-IFACE`; that expectation follows from the artifact format, not from any M2 outcome.

**C-2 — TDR-G universe.** M2's carrier is `R_bd`, not the dynamically admitted witnesses; the witnesses are a subset selected by the DISC gate, a criterion unrelated to composition. Two options:
- **(i) witnesses only** (22 DISC-1 + 136 DISC-2) — P2 exposure is known for exactly these; the selection criterion predates M2 and is independent of Π.
- **(ii) all certified `R_bd` records of the DISC panels** (the dual-active base seeds) — the full carrier on the registered panels, but P2 exposure is unaudited for non-witnesses, so under F6 they fail `R6-P2` unless a P2 exposure pass over them is run first. That pass would itself need C-1.

Proposed default: **(i)**. It is the narrower, already-audited universe, and it is selected by a pre-M2 criterion. (ii) can follow as a separate, preregistered extension.

**C-3 — U-DYAD rule.** Confirm the rule "every pair certified in the owner as a carrier member within the continuous-dyad family", enumerated from the owner text before any field is assessed.
