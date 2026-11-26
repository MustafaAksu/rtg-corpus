# RRF v0.9 — S2a corrected intermediate: build and review record

**Date:** 26 November 2026. **Status:** [SESSION] / DRAFT; not a release record or adoption.
**Authority:** PI authorization recorded PR #400 comment 7191799567, followed by verified merges #400 (b395875a19bb25c51316945327b28f1ec38fbe29) and #401 (02ed0ba96b177e1dfdb4d45259a4fe8c5ca4d387). S1 readback ACCEPT SCOPED at 2c087763, review 6074506269; records/rrf/RRF_S1_REVIEWER_VERDICT_PR400_20261126.md §5. PI opened S2a and separate BR-Q2 after merge. No S2b or adoption performed.

## Identities and method

| Object | Identity |
|---|---|
| Main checkpoint | 02ed0ba96b177e1dfdb4d45259a4fe8c5ca4d387 |
| Adopted base | rrf-v0.8.4, d7d661c0b89c6f3d9ceea2e205bf75fccfcfbf8d |
| Base SHA-256 / bytes | 2fb0a0fe9d998be91618cb731e2dee7301952ffdbe374f4889dd5e61c5cbafce / 108615 |
| S1 matrix blob | 8a32eba5578a791227af3c7de1f4bff43588a839 |
| Intermediate SHA-256 / bytes | 369938efd9779d9f12361851fe5d7be18835247258a6e7829f5b06ec2fe053e2 / 123958 |
| Build plan | `evidence/rrf/v0.9/s2a_build_plan.json` (38 nonoverlapping anchored operations) |
| Builder | `evidence/rrf/scripts/build_rrf_s2a.py` |

CONVENTIONS and Methodology v1.4 §§0.5,1.1,3.3,3.6,4.3–4.4,5.1,12.2,13.1,13.6–13.7 inspected. S1's twelve governing tags rechecked unchanged; S1 matrix has exact owner identity/reading extent; prior independent claim/interface readback accepted all 28 rows after C1–C4. Targeted rereads of base and methodology in this pass; no mathematical/owner-certificate re-audit. Exact source text retrieved via GitHub connector; SHA-256 recomputed from UTF-8 bytes (abc known-answer control), old/new anchored span digests, no overlap, all existing profile headings and owner/local identifier strings retained. Build constructed in connector-side JavaScript, not native Python execution. Python independent replay (including three negative controls) required in review:
```bash
python -I evidence/rrf/scripts/build_rrf_s2a.py
```
The first construction rejected a no-op before any write; omitted that no-op. No structural compaction, no stored unified diff. Plan contains replacement spans needed to reconstruct the intermediate, not a second DSN. Frozen history still in this stage where necessary for S2b; not governing claims.

## Matrix implementation and boundaries

| Rows | Content changes / retention |
|---|---|
| D1 | §2.2 exact lifted vs zero-winding and additional winding k≥1; DYAD owner primitive-map identifier. |
| D2–D4 | §2.4 inverse lower/upper bounds, distinct C7-SHARP and baseline rows (CD unchanged), fixed-h6 VF-1 and missing evidence. Keep certificates and proof pins. |
| D5–D6 | §§2.4,2.4b–c,4.2,6.2; local domain hypotheses, formal/finite/smooth and analytic branches, E2 zero linear part only, separate smooth equivariant chart, qualitative radius. B-∞ closed only at stated smooth scope; B-an/B-6 active. |
| D7–D8 | §§3.1,4.1a R9-dependent phase references and frame-scale/R11 names; no quantitative raw-track import. |
| R1–R5 | Current RECOG use and historical evidence distinction; separate R9 corollary and sharper rows; A1a reference only; family/twin, same predicate and W3 scope unchanged, no shadow transfer to R. |
| O1–O4 | §6.2a corrected Standard C, real C∞ test class/C³ Q6-REG, candidate family vs unregistered SESSION properties, κ/γ scope, recorded/unselected isolation contracts, P4 source-reported and one-way full-model nonconjugacy. §6.2 Q3b/Q5 boundary. |
| G1–G2 | §6.2a unchanged GEN theorem proof pin and distinct primitive ALG with its spectral condition, smooth C2 nonvacuity; §6.3 related export and source scope. No new GEN import. |
| T1 | §3.1 historical CN-05, current TRIAD source `[OPEN]` retained; metric same-vector convention only. |
| N1–N3 | §§5,6.1 retained historical pins, M-4 HOLD reason, P2 re-annotation scope; no WD-DOM verdict. |
| TD1 | §7.1 modulo N, accepted owner statement and open custody; discrete profile/bridge unregistered. |
| E1 | §§6.4,8.1 actual adopted noncanonical RER, 18+2, K6/K8, global certificate pending, no promoted evidence. |
| U1/P1 | §7.1 reference-only and actual owner/consumer pins, successor notices IF30/31/33 only after authorized release. |
| BQ | Separate work; no BR-Q2 scientific result or comparator registration in S2a. |

## Methodology and proposed local identities

Header DRAFT, §0 status grammar, §7.1–7.3 provisional source/consumer and OPEN routing. Existing five profiles, four transport keys/composite, RRF-CND-01 and OPEN-A/B/E semantics retained; proposed RRF-native IDs for existing local conventions/consequences and existing OPEN aliases are candidates only, to be reviewed and registered only by PI adoption. They do not re-own RECOG/GEN/DYAD or other owner results. No fabricated owner RID. Full claim-by-claim import-ledger/anchor and historical provenance relocation remains S2b, not asserted complete at S2a. Missing source artifacts and old proof pins remain explicitly identifiable. PRR v0.3 and GIIL separate decisions, no BASELINE update or pipe state change.

## Acceptance gates

- A1 exact replay of anchored plan from base tag, target hash and negative controls; verify changed paths only.
- A2 independent row-by-row content review against accepted S1, particularly C1–C4; every retained proof hypothesis, grade, domain, chart, clock and evidence boundary; compare changed source statements at owner tags rather than Atlas.
- A3 existing representation/transport and OPEN obligations intact; proposed local identifiers and closure criteria explicitly reviewed; no new scientific theorem/physical registration, no BR-Q2 import.
- A4 after acceptance freeze this intermediate; S2b only structural movement, deduplication and current-state/history separation with movement map and check_compaction + negative controls. Never treat this S2a candidate as adopted or merge it before release decision. The S0 custody checker is checkpoint-specific; verify old custody at the S0 commit, not by demanding current DSN equality.
- A5 final release preparation (later PI decision): actual import/reference ledger, size report, source and consumer notices, release record, tag; no historical evidence overwritten. LIT dependencies: none.

Native Python replay and linter, independent content acceptance, S2b and publication pending. No source science regraded or newly proved by these checks.
