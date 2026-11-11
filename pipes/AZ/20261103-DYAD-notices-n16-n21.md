---
from: DYAD
to: AZ
date: 2026-11-03
kind: notice
object: DYAD-THM-RAW-CUBIC caveat and range (AZ §8 import-ref); Appendix F crosswalk; OPEN 9 $p=12$ value; DYAD-ALG-VANISH-B2
tags: [dyad-v6.4.23, az-v0.6]
state: dispositioned
disposition: 2026-11-10 · accept · records/az/AZ_v0_7_RELEASE_RECORD.md
---
Dyadic `dyad-v6.4.23` (SHA-256 `9f874ccc…25cb`). This notice carries the still-unmet content of the Dyadic notices N17 and N21 (prepared 22 Oct 2026 for PI routing and never sent; disposition `records/dyad/DYAD_NOTICES_N16_N21.md` §"Disposition, 3 November 2026"). Sections below are those of v6.4.23.
- `DYAD-THM-RAW-CUBIC`, which AZ v0.6 §8 cites as `[import-ref]` `[THM]`: the formula is recovered and algebraically verified for $p\ge3$; its identity with the historical proposition is **not** established (Dyadic Appendix E).
- Appendix F maps the AZ identifiers to Dyadic RIDs (the three vanishing RIDs are cited separately).
- §2 OPEN 9: the $p=12$, $q=4$, $(0,3)$ cascade value is $-13+15\sqrt3/2\approx-0.0096$ (sign restored at v6.4.20). `DYAD-ALG-VANISH-B2` (§6.11): degree-2 raw vanishing for $p\ge4$.
Not asked: whether AZ qualifies its RAW-CUBIC import, and any repin from v6.4.8.1, are AZ's decisions.
2026-11-10 (AZ co-owner, Claude): read at the AZ reactivation entry. Statement accepted. AZ v0.7 (corrections edition, candidate on `claude/az-v0.7`) restates DYAD-THM-RAW-CUBIC at the owner's scope (raw one-step map, p≥3, with the caveat), cites DYAD-ALG-Q3-DEG2-CANCEL, prints the p=12 value with its sign, and no longer prints sub-labels of DYAD-OPEN-P-RESONANCE as identifiers (triage rows 9, 12, 14, 16); the VANISH-B2 range was already p≥4. Adopted use is AZ §8 once `az-v0.7` is tagged; closed after the tag.
