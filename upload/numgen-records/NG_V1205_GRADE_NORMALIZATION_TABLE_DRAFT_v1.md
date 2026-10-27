# Grade Normalization — Decision Table (DRAFT, proposals only)

**Doc ID:** `NG_V1205_GRADE_NORMALIZATION_TABLE_DRAFT_v1` · **Date:** 2026-09-28 · **Base:** frozen v1.20.3 (`c3265a3a…cfd2df`)
**Status:** DRAFT. **Nothing applied.** Every row is a *grade decision*, not a relabel. Needs a co-owner ruling per row.

## Why this is not a methodology-only pass
Methodology v1.3 L318: *"There is no total strength ordering… Select the tag for the actual assertion. **Split** an exact identity, its numerical test, and its physical interpretation when they have different status. … a combined `[from: ALG/NUM/HYP]` label [is] not canonical."* §8.1's canonical compounds are only defined ones (`[THM-ALG via IA]`, `[ALG via IA]`, `[NUM strong]`, …); `MATH/ALG`, `ALG/MATH`, `NUM/ALG`, `DEF/THM` are none of them. So each of the 19 either (R) collapses to the grade of the *actual assertion*, or (S) must be split into claims of different grade. Both change the recorded grade of a claim, which the migration rules classify as a **scientific** change, not TAG-NORM.

## Rows (provisional; each needs a full-block reading before ruling)
| # | line | current | module | proposal | reasoning |
|---|---|---|---|---|---|
| 1 | L67 | DEF/THM | §1.1 imported Discrete Genesis finite phase support | **S** | definition of the branch on `Z_N` is `[DEF]`; any derived property takes the source owner's own grade via `[import:]` — check the source |
| 2 | L142 | ALG/MATH | §1.3 N-5 spine summary | R → `[THM]` | C1–C4 are proved theorems |
| 3 | L329 | ALG/MATH | §5 high-risk row (C1–C4 + N5-PHYS-1 + C7A) | **S** | row bundles results of different grade |
| 4 | L1294 | MATH/ALG | §6.4 N-3B summary | R → `[THM] [scope: standard mathematical input]` | instance of standard duality |
| 5 | L1304 | MATH/ALG | §6.4 N-3D summary | R → `[THM] [scope: standard mathematical input]` | standard quotient |
| 6 | L1348 | MATH/ALG | N-3B | R → `[THM] [scope: standard mathematical input]` | |
| 7 | L1363 | MATH/ALG | N-3B homomorphism | R → `[THM]` | explicit unique homomorphism; could be `[ALG]` |
| 8 | L1404 | MATH/ALG | N-3C sector mixing | R → `[ALG]` | exact symbolic computation |
| 9 | L1413 | MATH/ALG | N-3D | R → `[THM] [scope: standard mathematical input]` | |
| 10 | L1428 | MATH/ALG | N-3D restriction/kernel | R → `[THM] [scope: standard mathematical input]` | |
| 11 | L1449 | ALG/MATH | N-3C+ projectors | **S** | projector identity `[ALG]` (needs `ord(λ)=p`); cascade item is CLOSED-by-import from Dyadic, carries the source grade |
| 12 | L1552 | MATH/ALG | §6.6 C5 controls summary | R → `[ALG]` | explicit finite periodic computations |
| 13 | L1562 | ALG/MATH | §6.6 C7A summary | R → `[THM]` | |
| 14 | L1704 | MATH/ALG | C5-SYN-13 | R → `[ALG]` | |
| 15 | L1728 | MATH/ALG | nearby negative control | R → `[ALG]` | |
| 16 | L1835 | ALG/MATH | C7A body | R → `[THM]` | |
| 17 | L1854 | NUM/ALG under frozen protocol | C7B-DISC-1 | **S — ruling needed** | see below |
| 18 | L1881 | NUM/ALG under frozen protocol | C7B-DISC-2 | **S — ruling needed** | see below |
| 19 | L2375 | NUM/ALG | NG-7A `Z_N` zero-control | **S** | identity `C·Dᵀ = 0 (mod N)` is `[ALG]`; ring/random-graph runs are `[NUM]` |

Totals (provisional): **13 R**, **6 S**.

## The one row that needs real thought — DISC-1/DISC-2
The ten-label result currently reads `[from: NUM/ALG under frozen protocol]`. Split per L318 into: the admission gate/protocol `[DEF]`; the enumeration verdict; the `Q^dyn` membership as `[RESULT]` conditional on that `[DEF]`. The open question is the grade of the enumeration. The dynamics is exact integer arithmetic on a finite state space and the registered domain is enumerated exhaustively, with an independent owner recount (544/544) and exact integer T4 certificates. By §8.1 that is a *finite exact check* — `[ALG] [scope: registered domain; frozen protocol]` — rather than a numerical approximation. `[NUM strong]` would understate it; `[ALG]` must carry the finite scope explicitly so it is not read as a general theorem. **This changes how the headline ten-label result is graded, so it should be decided by ruling, not by a patch.**
