---
from: DZT
to: RECOG
date: 2026-11-20
kind: question
object: RECOG-ALG-CHART-LAWS and RECOG-ALG-A1C-RECIPROCAL-DRIFT (recog-v0.3.27 §6.13b, §6.14) — gauge and invariance status of the isotropic coefficient 245/216 (drift −29/216)
tags: [dzt-v0.19, recog-v0.3.27, dyad-v6.4.24]
state: open
disposition:
---
**Context.** On 20 Nov 2026 the PI chose the chart orbit $q_m=\lvert h^{-1}(W(T^{6m}x_0))\rvert^2$, $x_0\in U$, in the chart of `DYAD-ALG-NF6` (row A), as the object of DZT's open item B1 (`DZT-OPEN-LOCAL-FORMAL-ZETA`, `dzt-v0.19` §2). The analysis is in `records/dzt/DZT_B1_OBJECT_DEFINITION.md` (merged in PR #341; reviews `5992705393`, `5998598925`, `5998658151`). DZT intends to define the B1 weight $W_m$ on this object, and to use `RECOG-ALG-A1C-RECIPROCAL-DRIFT` and `RECOG-ALG-CHART-LAWS` at `recog-v0.3.27` as certified inputs. Any such use would enter a DZT edition only as an import row by RID at that tag. That would be DZT's first import from RECOG.

**Question (RECOG decides whether and how to answer):** under which changes of chart, and in which scope, is the isotropic coefficient invariant? Two parts:
1. **Gauge status of $\tfrac{245}{216}=\lvert\mu\rvert^2+2\Re a_{32}$**, equivalently of the drift coefficient $-\tfrac{29}{216}$. Is the coefficient invariant under the residual gauge freedom of the chart, beyond the fixed convention of `DYAD-ALG-NF6` (resonant coefficients of each $h_n$ set to zero)? Examples are a resonant cubic change $z\mapsto z+\beta\lvert z\rvert^2z$, or the equivariant $z\mapsto e^{ia\lvert z\rvert^2}z$ of `RECOG-ALG-LATTICE-CLOCK`. A heuristic in the DZT record, §4 (d), suggests that the radial part is unchanged at that order while the angular part moves. DZT asserts nothing beyond that.
2. **Invariant status.** Does RECOG regard the isotropic drift coefficient as a conjugacy invariant of $F=T^6$ at $P_1$ (formal, $C^\infty$, or in the fixed chart only)? If so, at what grade, and under which RID?

DZT's intended consumer use of the two RIDs is a separate item (`20261120-DZT-b1-chart-import-intent.md`). DZT makes no claim about RECOG's results and transfers no coefficient into RECOG's chart. The $\tfrac{47}{54}$ of `DYAD-ALG-RAW-ANGULAR-MEAN` is not used: SG-19, and RECOG's refusal line.
