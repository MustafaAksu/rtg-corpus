# DYAD outbound notices N16–N21 (closeout C-3)

**Date:** 22 October 2026. **From:** Dyadic DSN (prepared by Claude, atlas owner, for the Dyadic owner). **Routing:** all notices go through the PI. **Status:** working record, prepared, **not sent**. No consumer file is modified by this record.

**Sources.** N16–N20 cite the adopted, externally verified `RTG_DYADIC_OSCILLATOR_DSN_v6.4.20`, SHA-256 `0b2d5a44eb818598bb330464dfa4f2e9d75521715f577a7c2e589e165f1a4852` (tag `dyad-v6.4.20`). N21 is the v6.4.21 delta; it is sent only after v6.4.21 is adopted and cites that edition's hash.

**State fields** are kept separate for each recipient: *sent* (date, by the PI) · *received* (consumer record that shows receipt) · *statement accepted* (the consumer accepts the statement as given) · *adopted use* (a consumer result depends on it, at a recorded pin). Pending consumer decisions do not reopen the Dyadic release and do not block adoption of v6.4.21 (closeout §5).

## N16 → Genesis; OFN

- `DYAD-THM-SMOOTH-EQUIVARIANT-CHART` (§6.17, `[THM]`, corollary of DYAD-THM-SMOOTH-EMBEDDING E3–E4): a real $C^\infty$ chart $\Phi$ with $D\Phi(0)=I$, $\Phi J=A\Phi$, $[\Phi T\Phi^{-1},A]=0$. It meets a $C^2$/$C^3$ chart hypothesis at $C^\infty$ regularity.
- Chart quintic phase coefficient $c_\theta=+\tfrac{89\sqrt3}{324}$ (RECOG-ALG-CHART-LAWS), distinct from the archival Lie-gauge $c_\theta^{(6)}=-\tfrac{119\sqrt3}{648}$ (SG-19).
- Field label: $\nu_5^{(5)}$ is exact in $\mathbb Q(\zeta_5)$ (§6.11, DYAD-ALG-NU5-P5); value unchanged.
- **Not claimed:** analyticity (B-an, B-6 OPEN); a quantitative radius; finite-chart bounds for $\Phi$; a choice for Genesis C2 or OFN class C; any physical model, carrier or $\gamma$.

| Recipient | Sent | Received | Statement accepted | Adopted use |
|---|---|---|---|---|
| Genesis | — | — | — | — |
| OFN | — | — | — | — |

## N17 → DZT; AZ

- Appendix F crosswalk of the identifiers DZT and AZ use.
- $Q_{12}$ sign: $-13+\tfrac{15\sqrt3}2\approx-0.0096$ (§2 OPEN 9); DZT-ALG-P12-NORM records its norm $\tfrac14$.
- VANISH-B2 explanation (§2 OPEN 9, DYAD-ALG-VANISH-B2).
- `DYAD-THM-RAW-CUBIC` status with its caveat: formula recovered and algebraically verified; identity with the historical proposition not yet established (Appendix E). (The range $p\ge3$ is added in v6.4.21; see N21.)

| Recipient | Sent | Received | Statement accepted | Adopted use |
|---|---|---|---|---|
| DZT | — | — | — | — |
| AZ | — | — | — | — |

## N18 → NUMGEN

- §7.0a L-PHASE row-A export table (I1–I5).
- $\phi^*$ status: removed from Dyadic §4; Dyadic owns no $\phi^*$ identifier (notice N3).
- FC-DYAD-33 lag-sign corollary, base points only: on $U$, $\sqrt{Q_m}\le\tfrac1{25}$, so $|r_m|\le\tfrac{403}{6250}Q_m$ and $(\tau-\tfrac{403}{6250})Q_m\le\tau Q_m-r_m\le(\tau+\tfrac{403}{6250})Q_m$ with $\tau-\tfrac{403}{6250}\approx1.0902>0$; the six-step lifted increment is below $2\pi$ at every block base point in $U$. NUMGEN to check anchor indexing, the seven-step crossing and coverage. No tube-wide claim.
- FC-DYAD-32 for information only: a SESSION result, not adopted; OPEN 21 keeps its R9 dependency.

| Recipient | Sent | Received | Statement accepted | Adopted use |
|---|---|---|---|---|
| NUMGEN | — | — | — | — |

## N19 → RECOG; RRF

- R9 claim-level import row (§7): T1, T2, the chart-variable memory law and DYAD-THM-OPEN21-PRIMITIVE-PHASE-REMAINDER are `[THM]` `[assuming: RECOG-THM-R9-MEMORY]`.
- Routing: $S_h=j^6R_0$ (§6.15–§6.16; $S_h$ commutes with $f$ only through degree 6 and is not an exact commuting involution).
- **N11 correction (RECOG):** RECOG v0.3.22 uses T1/T2 (`DYAD-THM-OPEN3-ASYMPTOTIC-PHASE`) in `RECOG-THM-A1A-CD-IDENTIFICATION` (§6.13b). The Dyadic notice table now records this as adopted use; the earlier v0.3.21 reference import (SG-R14) stays in the notice history. RECOG is asked to reconcile its own §7.2 mirror. No receipt is assumed; nothing is repinned.
- FC-DYAD-32 offered to RECOG for its H-NG decision.
- Frame rule: compare $\mu_p$ across frames only with DYAD-ALG-KP-FRAME-SCALE.

| Recipient | Sent | Received | Statement accepted | Adopted use |
|---|---|---|---|---|
| RECOG | — | — | — | — |
| RRF | — | — | — | — |

## N20 → Triadic; RER and ER-2B (through the PI)

New v6.4.20 content only:
- `DYAD-ALG-KP-FRAME-SCALE` frame qualifier; $\kappa_{\rm shear}$ unchanged.
- `DYAD-THM-SMOOTH-EQUIVARIANT-CHART`; no transfer to the triad.

RER v0.2 already records `DYAD-THM-SMOOTH-EMBEDDING` from v6.4.18 ($C^\infty$ existence, generator uniqueness under $DX(0)=0$, qualitative radius; analyticity and triad transfer kept separate). N20 does not ask RER to close smooth existence, and that earlier acceptance does not extend to the new v6.4.20 results.

| Recipient | Sent | Received | Statement accepted | Adopted use |
|---|---|---|---|---|
| Triadic | — | — | — | — |
| RER | — | — | — | — |
| ER-2B | — | — | — | — |

## N21 → v6.4.21 delta

Source: adopted `RTG_DYADIC_OSCILLATOR_DSN_v6.4.21`, SHA-256 `a412f34d4db6a6fa92705a5c33334127b3efc3a30a903fecb3c91bd0cf1cdc7d` (tag `dyad-v6.4.21`, after the PI creates it).

| Recipient | Content |
|---|---|
| RECOG | Current-status pointers that name RECOG objects: R11 CLOSED and the chart value (§1 OPEN 13 entry); N11 adopted use (§7 notices). Request: reconcile RECOG §7.2. |
| DZT; AZ | `DYAD-THM-RAW-CUBIC`: caveat and admissible range $p\ge3$ (§2, Appendix F). |
| Genesis; Triadic | FC-DYAD-34 bookkeeping cross-reference in §6.12: $(4\sqrt3/3)^2=16/3$ equals Genesis v2.8.9 §6.3's leading homogeneous-graph ratio; selects no birth policy. |
| RECOG; Genesis | OPEN 13 archival object: $h_4$ coefficient field corrected to $\mathbb Q(i\sqrt3)$ (was "$\mathbb Q(\sqrt3)$"), confirmed exactly; $c_\theta^{(6)}$ and grades unchanged; still not a chart quantity (SG-19). |
| all consumers | Layout-only compaction under Methodology v1.4: section numbers and anchors are unchanged; Appendix A is compact and earlier records stay at tag `dyad-v6.4.20`. No RID, grade or OPEN status changes. |

State fields for N21 are added when it is sent.

## v6.4.22 (23 October 2026) — no new notice

v6.4.22 (SHA-256 `2363ca409c08bc571378125771f27239b6426d3e7cdbe75e0306a2a728778c29`, tag `dyad-v6.4.22` once the PI creates it) changes wording and labels only (release record §2). No consumer action is needed, and N16–N21 keep their content and sources. The PI may add one informational line when these notices are sent:

| Recipient | Content |
|---|---|
| OPEN-M (UVM); RECOG | Dyadic now names the owner of every "R11" it uses: "OPEN-M R11" for the OPEN-M-2B assembly formulas (cascade-gate conversion, $\theta_f=2\pi/3$) and "RECOG R11" for RECOG's final-chart ledger (CLOSED). New Appendix C row. Nothing is asked of either owner. |
