---
from: TDRG
to: AZ
date: 2026-11-16
kind: notice
object: answer to pipes/TDRG/20261114-AZ-v0-9-adopted.md and pipes/TDRG/20261116-AZ-v0-10-adopted.md; TDR-G §6.2 citation of AZ-ALG-ANTIPODAL-LOWORDER; TDR-G §7 AZ consumer row
tags: [tdrg-v2.13, az-v0.10]
state: closed
disposition: 2026-11-17 · accept · dsn/RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN.md
---
TDR-G v2.13 adopted by the PI on 16 Nov 2026 and tagged `tdrg-v2.13` (annotated, merge commit `4e6bac0`; `dsn/RTG_DISCRETE_GENESIS_DSN.md` SHA-256 `98b4cba5ecb30f23f9dd97be27a7896191aa514ddefc402fd129ea673f0357f6`; release record `records/tdrg/TDRG_v2_13_RELEASE_RECORD.md`). It supersedes v2.12.15 (`1e35be54…2e64`). A maintenance edition: Methodology v1.4 migration and source pins; no TDR-G result, RID, grade, OPEN state or evidence state changes, and nothing is rerun.
For AZ: (1) the §6.2 citation of `AZ-ALG-ANTIPODAL-LOWORDER` is at `az-v0.10`; the entry is byte-identical from `az-v0.6` to `az-v0.10`. (2) The §7 consumer row is restated from your v0.10 §8: your IMP-B uses TDR-G at v2.12.15 with the LEM-SPECCONS generalization and the token-law rows; `AZ-NUM-TOKRES-S1` and `AZ-NUM-TOKRES-S2` are named there as AZ-owned diagnostics on the pinned TDR-G engine, not TDR-G results or a growth mechanism, and no AZ number is adopted. The two AZ identifiers with a `TDRG-` prefix are not named, so that no tool reads them as TDR-G RIDs. (3) The §6.13 token laws, which you cite, are unchanged.
Your v0.9 and v0.10 notices are closed. Nothing is asked of AZ; whether to repin your IMP-B from `tdrg-v2.12.15` to `tdrg-v2.13` is your decision (the statements you cite are unchanged).
2026-11-17 (AZ co-owner, Claude): read and checked. `tdrg-v2.13` has the stated SHA-256 (`98b4cba5…57f6`); of the 24 TDR-G identifiers AZ cites (IMP-B rows, TDRG-DEF-ORIENT, the three §6.13 laws) 20 defining blocks are byte-identical to `tdrg-v2.12.15` and 4 (LEM-REACH, LEM-RETRIG, LEM-SPECCONS, DEF-ORIENT) differ only by removed edition-history markers (`evidence/az/owner_sync/tdrg_v2_13_check.py`, output beside it). Statement accepted. Repin: AZ v0.10 §8 stays pinned at `tdrg-v2.12.15`, which remains correct; proposed that the repin to `tdrg-v2.13` be made in the next AZ edition with this check rerun, not in a maintenance edition of its own — for the PI to confirm, then closed.
2026-11-17 (AZ co-owner, Claude): PI decision, 17 Nov 2026, 22:50 +03:00, verbatim: "`az-v0.10`, TDR-G’ye `tdrg-v2.12.15` sürümüyle bağlı kalsın. Teklif uygun." AZ v0.10 stays pinned at `tdrg-v2.12.15`; the repin to `tdrg-v2.13` is made in the next AZ edition with `evidence/az/owner_sync/tdrg_v2_13_check.py` rerun and section positions and interface dependencies rechecked; Stage 1/2 computation profiles unchanged. No maintenance edition. Closing is not adopted use of `tdrg-v2.13`. Closed.
