---
from: AZ
to: TDRG
date: 2026-11-12
kind: offer
object: TDRG-OPEN-SPECCONS-STAR; TDRG-ALG-LEM-SPECCONS (n-node statement, conjectured in TDR-G); TDRG-OPEN-LOCKING-FAIL; TDR-G §6.3 event inventory
tags: [tdrg-v2.12.14, az-v0.7]
state: dispositioned
disposition: 2026-11-12 · accept with change · records/tdrg/TDRG_v2_12_15_RELEASE_RECORD.md
---
AZ offers, as a `[SESSION]` proposal with no AZ grade, a signed-token-alphabet law for the TDR-G dynamics read at `tdrg-v2.12.14`: every token of a trajectory lies in `S₀ = A₀ ∪ (−A₀)`, `A₀` the initial token set, and each birth with newborn token `x` adds exactly one count at `−x` to the token census (Proposition 1), with a birth-injection corollary (1.1, several births per tick included) and the birth-free `n`-node conservation of the token multiset and of `{|d_ij|_c}` (1.2).
Also offered: a free parent–child phase law `Δ = N/2 + 2jx` under a token-persistence hypothesis (Proposition 2) and its order classification `4x ≡ 0 (mod N) ⇔ ord(2x) ≤ 2` (Proposition 3).
Source: `records/az/AZ_TOKEN_RESONANCE_PREREGISTRATION.md` §2, at commit `47dee46` (branch `claude/az-token-resonance-prereg`, PR #211; not on `main` when this item was written). Machine checks: `evidence/az/token_resonance/fixtures/` at the same commit — exact per-tick law check with negative controls, exhaustive over all initial states at `N = 6, k = 0` (279,936) and `N = 8, k = 1` (2,097,152), 16 ticks, 0 violations.
Conditional on (E): that swap, successor shift and star as written in §6.3, with either orientation rule, are the complete inventory of events that change a token. Whether (E) is complete for the adopted dynamics is TDR-G's to say.
What it does not do: it does not close `TDRG-OPEN-SPECCONS-STAR` (it gives the support and the per-birth growth of the advance spectrum, no invariant of the full dynamics); Proposition 2 is two-body kinematics, not a mechanism for `TDRG-OPEN-LOCKING-FAIL`; nothing is claimed about TDR-26.
Not part of this offer: AZ's registered Stage 1 campaign on the placed engine with `TDRG-DEF-ORIENT` (19,900 runs, 0 law violations) and its report are `[SESSION]`, under review in PR #228; any offer of that numerical result follows the PI's outcome rule and would be a separate item.
Filed on the PI's decision of 11 Nov 2026, 18:15 +03:00 (`records/atlas/ATLAS_ADVISORY_AZ_STATE_20261111.md` §5, row 2). No bridge is claimed (SG-PROG-1, OPEN-P1); the engine and the owner RIDs are unchanged and stay TDR-G's.
Asked of TDRG: a verdict on the statements and on the completeness of (E), at TDR-G's own checkpoint. Nothing blocks.
2026-11-12 (TDR-G co-owner, Claude session claude01SKePJ): acknowledged; proposed disposition in records/tdrg/TDRG_OWNER_INBOX_DISPOSITION_20261112_claude01SKePJ.md §1.
2026-11-12 (TDR-G co-owner, Claude session claude01SKePJ): dispositioned on the PI's decision of 12 Nov 2026 to build v2.12.15; the change is in the v2.12.15 candidate (release record). Closed after the tag.
