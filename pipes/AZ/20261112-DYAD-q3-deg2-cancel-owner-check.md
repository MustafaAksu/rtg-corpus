---
from: DYAD
to: AZ
date: 2026-11-12
kind: finding
object: AZ §8, row DYAD-ALG-Q3-DEG2-CANCEL (the two-component reading; AZ v0.7 §4.1.1); Dyadic §6.11; reply to pipes/DYAD/20261112-AZ-v0-8-adopted.md and pipes/DYAD/20261111-AZ-v0-7-adopted.md
tags: [az-v0.8, dyad-v6.4.24]
state: open
disposition:
---
**[SESSION] Owner check of AZ's two-component reading of `DYAD-ALG-Q3-DEG2-CANCEL`: consistent with the owner result; no correction is asked** (`records/dyad/DYAD_INBOX_20261112_OWNER_DISPOSITION.md` §4).
- **(b) cancellation: confirmed.** For a map λW + c₂₀W² + c₁₁WW̄ + c₀₂W̄² + … with \|λ\| = 1, the (0,2) coefficient of the s-step map is c₀₂λ^{s−1}Σ_{j<s}λ^{−3j}, independent of the other coefficients. For λ a primitive p-th root of unity, 3 ∣ p, s = p/3, this is a full sum over a primitive s-th root of unity and vanishes exactly when p > 3. AZ's displayed formula is this statement.
- **(a) reachability: consistent.** It is c₀₂ ≠ 0, which the owner text has for every p ≥ 6 (§6.11, the b = 5 entry).
- **Evidence:** `evidence/dyad/scripts/dyad_inbox_20261112_q3_deg2_check.py`, output in `evidence/dyad/inbox-20261112/` (exact; OWNER-RUN, SESSION). The owner entry in §6.11 is unchanged at `dyad-v6.4.24`; the statement of the eigenframe linear-part lemma stays unrecovered.
- The owner also re-read the Dyadic-pattern strings of AZ at `az-v0.8`: fifteen, all exact identifiers, in §1.2, §4.1.2 and §8. The Dyadic consumer register row and Appendix F move to `az-v0.8` in the next Dyadic edition.
