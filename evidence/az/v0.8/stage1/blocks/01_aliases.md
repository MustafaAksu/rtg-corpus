## Local Tag Aliases

Status tags follow DSN Methodology v1.4 §8.1 and §8.3; qualifiers follow its §3.2. The entries below are local to this document.

| Local alias | Canonical expansion | Use |
|---|---|---|
| `[ENG PASS]` | `[ENG]` `[scope: certified by the named exit-code-gated check]` | Engineering item closed by a check whose artifact is named; the availability of that artifact is stated in §9 |
| `[NUM diagnostic]` | `[NUM]` `[scope: named diagnostic campaign]` | Finite numerical evidence (Methodology §8.4) |
| `[bridge-candidate]` | `[HYP]` `[bridge-required]` | Item that could become an OPEN-P1 observable if the bridge study opens; not an active import |
| `[bridge-disqualified]` | `[RESULT]` `[from: NUM]` `[scope: bridge-candidate ruled out]` | Item that was tested as a bridge-candidate and ruled out; recorded so it is not re-proposed |
| `[AZ-OPEN]` | `[OPEN]` `[scope: arithmetic-zeta infrastructure]` | OPEN problem internal to this arithmetic-resonance study |

Labels that are not status tags:

- `[import-ref]` marks a reference-only citation of a result owned by another DSN (Methodology §4.3, the first of its three uses). A status tag printed next to it is the owner's tag at the pinned edition; ownership is not transferred.
- `[ENG-blocker]`, `[ENG-blocker-n]`, `[ENG-open]` and `[ENG-open-n]` are the item labels of the engineering defects and open engineering decisions that §4.3.1 records as closed. They name those items; they do not assert validated engineering.
- A superseded, unverified artifact is described by its registry status in §9, not by a tag.

**Identifier owner map.** The following identifiers are this study's and keep their spelling (Methodology §4.2; existing identifiers are not renamed): `PROP-AZ-CORE-EQUIV` (result, §4.3.2), `TDRG-AZ-STATIC-ZN-4Q` (diagnostic result, §4.3.3), `DEF-AZ-CORE` and the `CONV-AZ-*` keys (conventions of `AZ-ART-CONVENTIONS-FROZEN`, §9), `SG-AZ-0.4` (guard, §0.1) and `TDRG-AZ-EXPORT-BASELINE` (the identifier the graph exporter prints for itself, §9). The prefix `TDRG-` in two of them names the object they describe, not a custodian: they are not entries of the `TDRG` namespace, and `RTG_DISCRETE_GENESIS_DSN` declares no such identifier.

---

