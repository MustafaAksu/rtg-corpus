# RTG_ONTOLOGICAL_FOUNDATIONS v0.10 — Release Record

**Date:** 19 October 2026 · **Release editor:** Claude (OFN co-owner) · **Decision owner:** Mustafa (PI)

## 1. Decision

The PI's message of 19 October 2026, 18:26 TRT, reads "Onay veriyorum". It answers the request to decide on O10-P1–P7 on Draft 2. It is recorded as approval of **O10-P1–P7 in full, at their stated scopes**, bound to:

`RTG_ONTOLOGICAL_FOUNDATIONS_v0_10_DRAFT2.md` — SHA-256 `58e2dec54ad600dec189119adc16c8ca89872e74419f78ae317f33558a913610`

Both OFN co-owners accepted Draft 2 before the decision. The second co-owner's final disposition was "ACCEPT — OWNER ADOPTION READY", given after an independent rebuild and hash check.

## 2. Identities

| Object | SHA-256 | Status |
|---|---|---|
| OFN v0.9, adopted baseline | `5ae8fdabad35a370f5709afa4d5dca6491e154c75f8a6f15fbb32d251fe59795` | Superseded on 19 Oct 2026; unchanged |
| Governing handoff v0.8.2 | `6e4fc3c3a999617a63482d0c19d3aa388031e8dbc55c5d7742fb6eadaf564b1d` | Co-owner-accepted working record |
| `build_ofn_v0_10_draft1.py` | `6a4fe7afc1384ae8763eba5f2bf091db0160d39bb3be5b5f6165873de66258ff` | Rebuild reproduced by both co-owners |
| Draft 1 | `d94e1e39f90fd66a485be0e40b614bf36a16a07324aa4e29397ed4be04db8c36` | Historical; unchanged |
| `build_ofn_v0_10_draft2.py` | `930b0aefe7b123d36ae6376a7ada05881680f69075a0756652aa69423c665c82` | Rebuild reproduced by both co-owners |
| **Draft 2 (approved object)** | `58e2dec54ad600dec189119adc16c8ca89872e74419f78ae317f33558a913610` | Historical; unchanged |
| `release_ofn_v0_10.py` | `2aca119f95df7b8274f1df40d37fca9495887850c7201e2e870e6fe2e07a4f5f` | Generates the final file from Draft 2; refuses any other input |
| **Final `RTG_ONTOLOGICAL_FOUNDATIONS_v0_10.md`** | `acb70a8cfc7962abcc047dedffb59e9ceca8f2e9843d6203df6eba54f5ed5dfa` | **ADOPTED — active canonical OFN**, 1,660 lines |

The final hash differs from Draft 2 only because of the publication edits in §3.

## 3. Publication edits (Draft 2 → final), 35 anchored edits

1. **Header block replaced** with adoption metadata: status, supersession, the adoption and approved-draft lines, the chain of identities, a pointer to this record, and updated registered-record counts.
2. **Proposed → registered wording**, applied only to v0.10-added text:
   - `[proposed RID: …]` → `[RID: …]`;
   - "OFN custody proposed" → "OFN custody";
   - the new OPEN record's "(proposed)" markers removed;
   - §12.3 custody rows changed to "Registered 19 Oct 2026";
   - the §5.5, §11.4, §11.5 and §12.5 headings, and the Appendix B record title;
   - "(v0.10 Draft 1)" labels → "(v0.10)".
3. **§0.3 and §12.5:** adoption sentence added.
4. **Appendix C:** "v0.10 ADOPTED" entry added. The Draft 1 and Draft 2 history entries are kept verbatim.
5. **Footer** replaced.

**Release checks** (`release_ofn_v0_10.py`, exit 0):
- RID set identical to Draft 2;
- anchor set identical to Draft 2;
- all twenty v0.9 `Status:` lines present unchanged, plus one new line (OPEN-OFN-TRIAD-CLASS: ACTIVE);
- the only remaining "adoption pending" markers are in the preserved history entries.

No scientific statement, grade, scope or OPEN status differs from Draft 2.

## 4. Registered by this adoption

| RID | Type |
|---|---|
| `RTG-OFN-DEF-TRIAD-MODEL-CONTRACT` | Definition: Q1–Q6, Q6-REG, declared test model, class-C model contract |
| `RTG-OFN-DEF-STANDARD-C` | Definition: Standard C at cubic order |
| `RTG-OFN-ALG-RAW-STANDARD-C-NOGO` | Local result, OFN custody; OPEN-C19-L gap recorded |
| `RTG-OFN-ALG-NARROW-Q6-PLANAR-PRODUCT` | Local result, OFN custody |
| `RTG-OFN-OPEN-TRIAD-CLASS` | Foundational OPEN, ACTIVE |

Totals after adoption: 11 definitions; FSP-U as hypothesis; 4 local results; 21 OPEN records (twenty inherited statuses unchanged — 19 ACTIVE, 1 PARTIAL — plus 1 new ACTIVE).

## 5. Not decided by this release

- OPEN-OFN-3B stays ACTIVE.
- DYAD OPEN 20 (existence of $J$) stays open.
- No independent all-κ audit of FMS P4 has been made.
- The physical carrier, ψ and chirality are not selected; this is the subject of OPEN-OFN-TRIAD-CLASS.
- The 13 October OPEN-narrowing package is not integrated.
- No owner file other than OFN is changed.
- **Not done by this file action:** no project-root installation, no deletion of v0.9, no remote deposit.

## 6. Outbound notices (O10-P7; effective from adoption)

**N-O10-1 → DYAD (owner).**
- OFN v0.10 is adopted.
- Notice N9 is answered at owner level.
- OFN imports `DYAD-THM-FORMAL-Z6-GENERATOR`, Lemma F and F3 (v6.4.13), and the OPEN 3 RIDs (v6.4.14–15), at their owner grades (IMP-O10-03–05).
- The OPEN 3 results are used edgewise and only on the class-C lock surfaces, conditional on $J$. No separator or basin statement is drawn from them.
- v6.4.16 is recorded as lifecycle-only (RF-O10-04).
- DYAD OPEN 20 (B-6 / B-∞ existence) is the realization dependency of class C.
- N12 was not read for this release.

**N-O10-2 → Genesis (owner).**
- The v2.8.9 notice erratum on OFN Q6 is received (RF-O10-05).
- `GEN-THM-TRANSPORTED-CHIRAL-FACTOR-NOGO` and the raw-family six-step RIDs are imported at their scope (IMP-O10-01–02).
- The narrow-Q6 corollary is registered as `RTG-OFN-ALG-NARROW-Q6-PLANAR-PRODUCT` under OFN custody. It uses the six-step theorems, not the primitive-clock `[ALG]` statement.

**N-O10-3 → RRF (editor).**
- Interface request: register class C, the transported κ-family $F^N_\kappa=P_\kappa\circ N^{\times3}$, as a **model-contract row** and not as a new native profile, while OPEN-B/E1 stays locked.
- The contract: a different conditional model under §0.3; formal regularity, or real $C^3$ for the polynomial representatives, with analytic or $C^\infty$ realization conditional on DYAD OPEN 20; primitive clock $T$; a local domain; transported readout chart (§5.5.4).
- Also requested: a readout contract for the in-class modulus. $|c|$ reads $m$ only up to the reflection $m\mapsto2m_*-m$.
- The registration decision is RRF's.

**N-O10-4 → FMS (session ledger).**
- The FMS receiving interface is answered at owner level by OFN v0.10 §5.5: Q1–Q6, Standard C, the scoped disposition, and class C as the primary formal candidate.
- FMS ψ results are reference-only (RF-O10-02). The universal finite-$a$ statement keeps the P4 qualification.
- Open FMS tasks: the chiral basin boundary and the parabolic rate, per member or uniformly across the modulus family; the seven unreached first-order moduli; jets beyond degree 5; κ ∈ {0, 2}.
- FMS pilot closeout remains FMS's own act.
