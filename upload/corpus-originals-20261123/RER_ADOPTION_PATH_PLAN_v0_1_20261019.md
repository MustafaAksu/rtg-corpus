# RER v0.2: path to registry adoption (plan v0.1, for PI decision)

**Date:** 19 Oct 2026.
**From:** Claude, RER co-owner.
**Status:** NONCANONICAL plan. Nothing in it is authorized until the PI decides D-1 to D-4 in §4.
**Starting object:** RER v0.2 DRAFT r4.4 (`5df47386…a9d8`). It is a pointer synchronization of the accepted r4.3: Triadic v1.6.1, RRF v0.8.3 and Dyadic v6.4.14 are recorded. It is under receiving review.

## 1. What "RER adoption" can mean

RER is a registry, not an owner DSN. Most of its records restate owner results at their owner grades: Genesis, Triadic, Dyadic, ER-2B, RRF. Adopting RER therefore cannot mean adopting those results again. I propose this definition:

> **RER registry adoption** = the PI accepts, at a stated version, that
> (a) every record correctly restates its source at the source's grade, scope and exactness;
> (b) the registry's own [ALG]/[DEF] contributions (E-conjugacy transport, the four-axis status schema, record contracts, gap entries G7–G10) are correct;
> (c) open, blocked and receiver-reported items are labelled as such.
>
> It is **not** owner adoption of any source result, physical selection, RRF normative status or a freeze of the source DSNs.

## 2. Inventory: 20 records, 4 gap entries, preserved v0.1 body

| Group | Records | Grade / exactness | Source owner | Review status | Adoption readiness |
|---|---|---|---|---|---|
| Genesis K3/closure | GEN-C01 … C09 | [ALG]/[THM]; EXACT_SURROGATE / EXACT_LOCAL | Genesis | Accepted at r3/r3.1; source pins later moved v2.8.5 → v2.8.7 (8) | Re-check each against Genesis v2.8.7/2.8.8 text (Phase B) |
| Genesis K3 modal | GEN-K3-MODAL | [THM] import + [ALG] transport | Genesis + RER | ACCEPT SCOPED (r4) | Ready once Phase A passes |
| Triadic age family | TRIAD-FORMAL-AGE, -AGE-CURVATURE, -REGULAR-3FOLD | [THM]/[ALG]; FORMAL/FINITE/EXACT_LOCAL | Triadic | Accepted at r3/r3.1 | Re-check against Triadic v1.6.1 (Phase B) |
| Triadic involution / birth graph | TRIAD-FORMAL-INVOLUTION, TRIAD-BIRTH-GRAPH-INVOLUTION | [THM]+[ALG]; FORMAL_ONLY | Triadic-side evidence (author: Claude) | ACCEPT SCOPED by the receiving co-owner; kernel exact certificate PASS on both sides | Ready, subject to the non-author rule |
| Dyadic | DYAD-FORMAL-INVOLUTION | [THM] owner import | Dyadic v6.4.13 | ACCEPT SCOPED; E1 applied | Ready |
| ER-2B | ER2B-T6D, ER2B-CARRIER | [ALG]; EXACT_LOCAL / EXACT_CONDITIONAL | ER-2B | **Source package v0.2 missing** (C19–C20 receiving verification open) | **Blocked**. The project now holds `RTG_ER2B_CONSOLIDATED_STUDY_v0_3_NONCANONICAL.md`; whether it can serve as the source is decision D-2. |
| Stage-2 | F3-N7N8 | [ALG] FINITE_ORDER; GLOBAL_CERTIFICATE_PENDING | Triadic/Stage-2 | Local jets accepted; regional/global OPEN | Adoptable **as an open record** (status stated), not as a certificate |
| RRF interface | RRF-CND01 | [THM] EXACT_CONDITIONAL | RRF | Accepted at r3.1 | Needs the RRF-interface review (Phase C) |
| Gap entries | G7–G10 | contract text | RER/RRF | r4 overlays | Phase C |
| v0.1 body | 16 preserved machine entries + overlays | historical | RER | Preserved | Classified as history, not re-adopted |

**Machine registry.** The REGISTRY JSON has not been regenerated since r3.1 (`b996ba8e…a213`). The four r4 records and the r4.x status changes are not in it. Producing an r4.x JSON from the Markdown is a required, deterministic step (Phase A).

## 3. Proposed phases

| Phase | Work | Who | Gate to the next phase |
|---|---|---|---|
| **A. Integrity and currency** | Resolve every `Import/reference` pin (path, hash, evidence label). List missing sources. Regenerate the REGISTRY JSON with a Markdown↔JSON consistency checker. Add a per-record source-currency table, so that every record names the current owner version and whether its cited text is unchanged. | Preparer (Claude) builds; receiving co-owner replays | Checker PASS, receiving replay PASS |
| **B. Record-by-record scientific review** | 20 records, each against its current owner text: grade, scope, exactness, overclaims, conditions. Accept / revise / block per record. The author of Triadic-side evidence does not accept those records. | Receiving co-owner (ChatGPT) for all records; Claude reviews any record ChatGPT authored | Every record dispositioned; revisions built as r5 drafts |
| **C. RRF interface review** | The RRF editor reviews G7–G10, RRF-CND01, profile uses (RRF-DYAD-W/NF, transport rows) and RER's normative status relative to RRF v0.8.3, and decides whether the RER proposal stays nonnormative. | RRF editor | Written RRF disposition |
| **D. Release** | Metadata-only release transform of the last accepted r5.x, as done for Triadic v1.6.1: separate adoption record, history preserved, release-integrity verification. | Preparer builds; receiving co-owner verifies; **PI authorizes** | PI authorization |

**Effort estimate.** A and D are mechanical: about one session each. B is the main load: 20 records, roughly 3–4 review rounds. C depends on the RRF editor.

## 4. Decisions needed from the PI

- **D-1 — Meaning of adoption.** Accept the §1 definition, or narrow it. One possible narrowing is "adopt as working registry only", as RRF did for its working standard.
- **D-2 — ER-2B records.** Options:
  - (a) hold ER2B-T6D and ER2B-CARRIER as BLOCKED inside an adopted registry, with the block stated;
  - (b) exclude them until the source arrives;
  - (c) re-source them on ER-2B consolidated study v0.3. This needs an ER-2B owner statement on which object is authoritative.

  Recommended: (a).
- **D-3 — Freeze.** Whether an adopted RER is frozen at that version, or remains a living registry with versioned releases. Recommended: living, with versioned releases. Every release is metadata-only over a reviewed draft.
- **D-4 — Scope of Phase B.** Full re-review of all 20 records, or only records whose source changed since their last acceptance (C01–C09, the three Triadic age records, RRF-CND01) plus a spot check of the rest. Recommended: the second, because it is about half the effort, provided Phase A's currency table is complete.

## 5. Unchanged regardless of the path

G6, degree-7 graph completion, the regional/global Stage-2 certificate, physical model selection and the A1 live installation are not affected by RER adoption and remain OPEN.
