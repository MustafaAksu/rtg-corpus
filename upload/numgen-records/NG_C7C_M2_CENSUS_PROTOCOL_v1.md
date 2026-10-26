# C7C-M2 Evidence-Sufficiency Census — Protocol v1 (Census-1)

**Doc ID:** `NG_C7C_M2_CENSUS_PROTOCOL_v1` · from draft `3979531…21a0` · **Date:** 2026-09-30
**Governed by:** frozen preregistration `NG_C7C_M2_PREREG_DRAFT_v4` (`248f128c…8987`) and its freeze manifest (`cefb7180…b165b`). Where this protocol and the preregistration differ, the preregistration governs.
**Status:** FROZEN under the co-owner's conditional GO (C-1, C-2, C-3 ruled; F5 wording repaired). No record has been examined under this protocol.

> **Hard guard.** The census tests evidential reconstructability only. It does not evaluate interface equivalence, Π, N1/N2, WD-DOM, or any PASS/FAIL condition. A record is admissible when the frozen evidence is sufficient for those questions to be decided later without generating new data or changing the preregistered definitions.

---

## 1. Unit and universe

**Unit.** One *record* = one certified pair `x = (A,B)` of the carrier, with its frozen provenance. Chains `(x,[φ],y)` are **not** formed in the census; chain formation is analysis.

**Universe (fixed by rule, applied in this order).**
- **U-DYAD (C-3):** each explicit ordered physical pair `(A,B; domain, order, provenance)` whose membership in `R_bd` is certified by a **live owner block** of Number Genesis v1.20.6 within the continuous-dyad family — including a certified carrier-preserving image when the owner explicitly proves that the image lies in `R_bd`. **Object granularity:** records are owner-certified carrier objects, not points, orbits or initial conditions inside a certified sector. Do **not** manufacture records from equal labels, from C7A's abstract existence statement, or by enumerating points or orbits of a sector. An image is included because an owner carrier-preservation theorem certifies it (e.g. C7C-0 for an orientation swap), never because of its label.
- **U-TDRG (C-2) — Census-1 TDR-G evidence universe:** **all** frozen DISC-1 and DISC-2 witness records, **22 + 136 = 158**, identified by the witness IDs of the sealed DISC-1 harness output and the DISC-2 witness report. **All 158 enter the universe**, including the 40 P2-exposed DISC-2 witnesses; exclusion on P2 grounds happens only in F6 (`R6-P2`), never in universe construction. **Scope statement:** the frozen DISC-1/DISC-2 witness records only; **no claim of exhaustiveness over `R_bd`**. A carrier-extension census over all certified dual-active `R_bd` records of the DISC panels is a separate, future preregistration (Census-2), with its own P2 audit procedure.

The universe is enumerated by the rule, completely, before any field is assessed. No record is added or dropped afterwards; a record that cannot be located is reported NOT ADMISSIBLE with reason `R0-MISSING`.

## 2. Frozen fields (assessed in order; each is PASS / FAIL with a reason code and an evidence pointer)

| # | field | PASS iff | frozen basis |
|---|---|---|---|
| **F1** | record identity / provenance | artifact name, hash/version, owner, frozen source and (if applicable) witness ID are all present and the hash verifies | G-sufficiency |
| **F2** | family eligibility | the record maps to one registered family, **and every component of `κ_b`** — schema key, owner+version+hash, sector-class key, gauge policy, orientation/event semantics, common-order semantics — is reconstructable from its provenance | prereg §4.3; G-sufficiency |
| **F3** | interface-data reconstructability | at **both** ends, `B`, the prefix poset `𝒫`, and the single-stream attachment `ι = N_B` on `𝒫` are defined from the record; no bounded class, ratio, label or fate is used to define them | prereg §2, §3 |
| **F4** | witness-germ assessability | the data required to **evaluate** a candidate tail representative later are present: explicit order structure of `𝒫` and the count functions of F3. **The census does not construct any `φ`, does not decide whether one exists, and computes no discrepancy bound.** | prereg §2, §4.1; G-sufficiency |
| **F5** | Π-decidability provenance | the record carries the **endpoint-level** instance, order and prefix-cofinal provenance required so that, once a counterpart and a witness germ are chosen in the later analysis, transported outer `R_pair` membership can be adjudicated **without generating new physical data** — in particular instance identity (which orbit/realization each stream lives on), common-order structure and prefix-cofinal repeatability data. **F5 does not adjudicate that membership**, and records no Π value. A witness germ is not such provenance (G-bridge) | prereg §2 (Π, T-inv, G-bridge); G-sufficiency |
| **F6** | P2 eligibility (TDR-G only; dyad records: N/A) | the record is P2-unexposed, **or** carries a separate policy-independence certificate | G-P2 |

**F7 — verdict.** `ADMISSIBLE_FOR_M2_ANALYSIS` iff F1–F6 all PASS (F6 N/A counts as PASS for dyad records); otherwise `NOT_ADMISSIBLE_FOR_M2_ANALYSIS` with the **first** failing field and its reason code.

**Forbidden columns — must not appear in any census output:** N1, N2, Π truth value, `≈_L`, `~_a`/`~_b` verdicts, existence of `φ`, discrepancy bounds, WD-DOM, PASS/FAIL of M2, any rational label or bounded class used as a sorting or selection key.

## 3. Evidence rules

- **E-frozen.** Only frozen artifacts whose hashes verify against their manifests.
- **E-nonew.** No new seed, trajectory, parameter, panel, or event policy (G-search).
- **E-rederive (C-1) — frozen replay contract.** Re-deriving a frozen record's own trajectory from its frozen seed is **reconstruction of that record, not new data**, under all of:
  1. **Frozen input tuple.** Seed, every parameter, owner-code hash and every load-bearing convention are taken from frozen artifacts; nothing is supplied from outside them.
  2. **Preregistered extraction only.** The replay yields only what F3/F4 need — prefix order and single-stream count functions. No new diagnostic, statistic or selection metric is computed.
  3. **Replay consistency.** The replay must reproduce **exactly** the cycle-level totals and verdict-neutral aggregates already stored in the sealed artifact. On any mismatch the reconstruction **fails** (`R3-REPLAY`); no other code, parameter or convention is tried.
  4. **Hashed evidence.** Replay output and its invocation/config manifest are hashed and stored as the census evidence pointer. If the code's behaviour depends on environment or nondeterminism that cannot be pinned, the record fails F3/F4 (`R3-REPLAY`).
  Any other seed, parameter or code is new data (G-search).
- **E-noeval.** If assessing a field would require deciding interface equivalence or Π, the field is scored on **availability of the data** only; the question itself is left for analysis.

## 4. Order of application
1. Freeze this protocol.
2. Enumerate U-DYAD and apply F1–F7.
3. Then enumerate U-TDRG and apply F1–F7.
4. Report each family separately. The report closes the census; it contains no analysis.

**No overclaim from Census-1.** Admissibility of witness records says nothing about `R_bd` at large. In particular, *"no counterexample appeared among the witnesses ⇒ WD-DOM holds on TDR-G `R_bd`"* is **not** an admissible inference: a FAIL needs one certified counterexample, while a PASS requires the universal proof fixed in the preregistration (§9), never exhaustion of a witness census.

## 5. Output format
One row per record: `record_id · family · F1 … F6 (PASS/FAIL/N-A + reason code + evidence pointer) · F7 verdict`. Reason codes: `R0-MISSING`, `R1-HASH`, `R2-KEY` (which `κ_b` component), `R3-IFACE` (which end, which datum), `R3-REPLAY` (replay-contract failure), `R4-ORDER`, `R5-PROV` (which provenance item), `R6-P2`. A summary counts admissible and non-admissible records per family and per first-failing field — nothing else.

## 6. Decisions — ruled by the co-owner (2026-09-30)

- **C-1 deterministic re-derivation — GO with conditions:** the frozen replay contract of §3 (E-rederive 1–4).
- **C-2 TDR-G universe — GO, option (i):** all 158 witnesses enter before F6; scope named "Census-1 TDR-G evidence universe", no exhaustiveness claim; option (ii) deferred to a separate Census-2 preregistration.
- **C-3 continuous-dyad universe — GO with object-granularity clarification** (§1).
- **F5 wording** made record-level (§2): endpoint provenance sufficient for later adjudication; no adjudication in the census.
