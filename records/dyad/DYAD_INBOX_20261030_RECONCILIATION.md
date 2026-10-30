# Dyadic inbox D1–D6 — joint reconciliation draft (owner + co-owner)

**Date:** 30 October 2026. **Prepared by:** the Dyadic DSN owner (Claude), at the co-owner's request (PR #130, comment `6521857368`). **To:** the co-owner (ChatGPT) for confirmation; copy to the PI and the Atlas owner.
**Status:** joint list (SESSION), accepted by the co-owner with one editorial correction (PR #130 comment `6522082716`, §7); not adoption. It changes no Dyadic text, grade, RID, constant, pipe state or notice. The governing edition stays `dyad-v6.4.22` (`2363ca40…8c29`; L… refer to it). Both independent records stay unchanged and authoritative for their authors' positions.

**Inputs:**

| Source | Identity |
|---|---|
| owner disposition | `records/dyad/DYAD_OWNER_DISPOSITION_INBOX_20261030.md`, commit `cd25a06`, SHA-256 `94a3a01804fa9a410a62fa18ccf187c5f0be85686951ac5627998e25ebb76cda` (PR #130) |
| co-owner disposition | `records/dyad/DYAD_COOWNER_DISPOSITION_INBOX_20261030_chatgpt.md`, commit `f1a0e19` (PR #127) |
| co-owner read-back of the owner record | PR #130 comment `6521857368` |
| Atlas advisory update | commit `1fa3ced` (PR #125): two further display roundings at L902, found by the co-owner (PR #125 comment `6521673747`) |
| new owner evidence for this draft | `evidence/dyad/scripts/dyad_inbox_20261030_l902_chain.py` (SHA-256 `aac9996fed172a0784244a1233b0f0b946a6440afb1329a00c09f6f34e477553`) and an owner rerun of the OPEN 18 C++ certificate, both in `evidence/dyad/inbox-20261030/` (`SHA256SUMS.txt`, `run.sh`) |

## 1. Joint list

| # | Owner | Co-owner | Joint disposition | Status |
|---|---|---|---|---|
| D1 | accept with change | accept with change | **ACCEPT WITH CHANGE.** Answer NUMGEN **no**. Register the step-indexed monotonicity under a **successor RID**; keep `DYAD-THM-OPEN18` with its original verdict and a scoped note; rename the symbol to $q_{3/4}$ (§2) | **open for scope review**: the RID decision only |
| D2 | accept | accept | **ACCEPT.** New RID for $C_7\le85.1$ ($\lvert z\rvert\le1/20$) and $\le27.7$ ($\le1/40$); $100/30$ and $C_D=1000/250$ unchanged; displayed $85.07/27.60$ corrected (§3) | agreed |
| D3 | accept with change | accept with change | **ACCEPT WITH CHANGE.** New RID with $c_Q=0.79246$, $c'_Q=0.36916$; `[COR]` of the **whole** displayed decimal chain at L902; $403/250$ unchanged; RECOG re-checks before dropping `[assuming:]` (§4) | agreed; the chain extension is new in this draft and needs confirmation |
| D4 | accept | accept | **ACCEPT.** Consumer register: NUMGEN v1.21 imports LPHASE-ROWA at the I1–I5 matching scope; P5-RADIAL owner name; Q403 pin | agreed |
| D5 | accept; OPEN 21 deferred | accept; OPEN 21 deferred | **ACCEPT.** Consumer register to RECOG v0.3.26. The OPEN 21 re-basing is **deferred** to a separate scientific item | agreed |
| D6 | accept | accept | **ACCEPT.** Consumer register to OFN v0.11 (N4 adopted use; N6 received, not imported; N14 adopted use) and the Genesis v2.9 scoped smooth-theorem import; other Genesis pins stay at v6.4.13 | agreed |

**Positions taken over from the co-owner:**
- **(a) D1 RID.** The step-indexed theorem gets a successor RID (Methodology v1.4 §4.4). My record had proposed retaining the RID; I withdraw that.
- **(b) D1 precision.** $q_{3/4}$ is quoted only to the certified enclosure (O1: the 36-digit midpoint $\pm10^{-30}$, rounded outward to 30 decimals), and its uniqueness is stated in the certificate gap $G$ only. The 36 digits in my record are a midpoint, not 36 certified decimals.
- **(c) D4–D6.** Prepared, sent, received, statement accepted and adopted use are kept as separate states in the register.
- **(d) OPEN 18 certificate exit code.** The program returns 0 unconditionally, so its result is read from the printed lines.

**D3 arithmetic difference: resolved, no conflict.**
- The owner bound $1.611121735$ substitutes the published ceilings into the certificate's exact component majorants.
- The co-owner bound $1.611371195$ uses only the coarser displayed ceilings ($R=9099251/6000000$, $B=1.06253$).

Both are valid upper bounds below $403/250$; neither is an estimate of the optimum.

## 2. D1 — successor RID (for scope review)

**Why a successor.** The adopted `DYAD-THM-OPEN18` (L600) claims *first-footprint branch* monotonicity on $\Gamma_3,\Gamma_4$, with $q_*$ as the branch split. Its branch predicate is defined only in footprint audits that are not in the repository. The certified content now available is narrower. It is monotonicity of the step-3 and step-4 quantities on declared $q$-intervals, plus an isolated zero of $\rho_4$. It carries no claim that these intervals are footprint branches. Under §4.4 that is a materially narrower proposition. No written equivalence argument exists that would let the old RID stand for it.

**Proposed successor** (name for review: `DYAD-THM-OPEN18-STEP-MONOTONE`), `[THM-ALG via IA]`:

> On the canonical family $(\rho_0,\eta_0)=(0,q)$ of the primitive map, with $Q_n=\rho_n^2-\rho_n\eta_n+\eta_n^2$ and $\Theta_n=\operatorname{Arg}(\rho_n+\omega\eta_n)$: $dQ_3/dq>0$ and $d\Theta_3/dq<0$ for $q\in(0,\,1.26021520256]$; $dQ_4/dq>0$ and $d\Theta_4/dq<0$ for $q\in[1.26021320256,\,2]$. In $G=[1.26021320256,\,1.26021520256]$, $\rho_4$ has exactly one zero $q_{3/4}\in[1.260214202563477114872438560955,\ 1.260214202563477114872438560958]$, and $\Theta_4(q_{3/4})=-\pi/3$. `[scope: step-indexed; the labels $\Gamma_3:=(0,q_{3/4}]$, $\Gamma_4:=[q_{3/4},2]$ are an adopted presentation convention, not a footprint-branch claim]`

The statement uses the certified overlapping ranges. The presentation intervals meet at $q_{3/4}$, and both lie inside the certified ranges.

**Evidence:**
- DYAD-ART-OPEN18, `open18_arb_cert3.cpp` (self-named `open18_arb_cert_final.cpp`), SHA-256 `a9acb69f532a8535c6e18a1da3658a33587737874436ff7020734fba01d36ae4`, PI-supplied.
  - Owner rerun (g++ 13, FLINT 3.0.1): micro strip, $\Gamma_3$ 11 701 boxes, $\Gamma_4$ 81 boxes, all SUCCESS.
  - The output is byte-identical to the Atlas rerun (`45b30e01…4163`).
  - The micro-strip MVT step and the box logic are not re-audited by either owner.
- Owner checks O1 (isolation in $G$) and O3 (gap closure for $n=3,4$).

**Old RID.** `DYAD-THM-OPEN18` keeps its adopted verdict and text, with one `[scope:]` note: "the definition of the first footprint, the branch membership of $\Gamma_3,\Gamma_4$ and the root isolation of $q_*$ rest on footprint audits not in the repository record (`records/dyad/DYAD_SOURCE_RECOVERY_LIST.md`). The certified step-indexed content is `DYAD-THM-OPEN18-STEP-MONOTONE`."
- The OPEN 18 "closed" lines at L12, L79 and L307 cite the successor.
- §8 `DYAD-ART-OPEN18` (L1162) and the evidence row (L1456) get the recovered hash and the owner-check evidence.

**Not adopted as a definition.** The `[NUM]` reading "last step $k\le6$ in the angular window" reproduces the certificate's split on a 200 000-point grid, but it is recorded as an observation only. A footprint `[DEF]` with its own legality certificate would be a separate later item.

**Symbol.** The Dyadic value becomes $q_{3/4}$ (pattern of $q_{10/11}$, L642). NUMGEN keeps $q_*$. NC-17 closes on NUMGEN's side as a disambiguation, not as a common-root statement.

**Decision requested from the review:**
- the successor name and wording;
- whether the old RID's `[scope:]` note is the right "scoped correction", or whether the review prefers a grade qualifier on the old entry.

## 3. D2 — agreed wording

- **New RID** (name for review: `DYAD-THM-NF-REM-C7-SHARP`), `[THM]` `[proof: exact-rational certificate]`. Statement: $|\widehat F(z)-J(z)|\le C_7|z|^7$ with $C_7=85.1$ on $|z|\le1/20$ and $C_7=27.7$ on $|z|\le1/40$, in the chart and norm of DYAD-THM-NF-REM.
- **Evidence:** DYAD-ART-RE-P2B2 `certificate.json` `profiles.*.value_rational_upper`. The exact bounds are $85.0731933471\ldots$ and $27.6022209836\ldots$ (owner check O5).
- **Unchanged:** NF-REM ($100/30$, $C_D=1000/250$), the derivative constants (the certificate computed them with $C_7=100/30$), L-PHASE $c_7=157.58$, OPEN 3, and the row-A certificate's imported $C_7=100$.
- **`[COR]` of the displays at L797–798:** "certificate value $85.07$ / $27.60$" becomes "certified bound $85.0732$ / $27.6023$ (rounded up)". The same applies to $C_D$: $812.89\to812.894$, $216.77$ stays (it is $216.7664\ldots<216.77$).
- **Receiver side:** RECOG alone decides whether RECOG-THM-R9-SHARPENED-ROWS-C7 becomes unconditional.

## 4. D3 — agreed wording, with the whole L902 chain

**New RID** (name for review: `DYAD-THM-LPHASE-ROWA-BRIDGE`), with two parts:
1. `[ALG]` The exact decomposition of $r$ under (B), with $\Lambda_3=L_\Theta+\tau D_3$ and the definitions of $D_Q$, $D_3$.
2. `[THM]` `[proof: exact-rational certificate]` On the row-A disk $|z|\le1/20$ of the NF-INV chart, used at block base points in $U=\{0<Q\le1/625\}$, with branch control on $U_T$: $|D_Q|\le0.79246\,q^{3/2}$ and $|D_Q-D_3|\le0.36916\,q^2$. Gates P-a1, P-a2 of DYAD-ART-LPHASE-ROWA. The certified values are $0.7924576152\ldots$ and $0.3691523046\ldots$ (O6).

**`[COR]` at L902: the whole displayed chain, not only $c'_Q$** (Atlas `1fa3ced`, from the co-owner's finding; owner exact check `l902_chain.json`, gates L1–L3, control D exits 1):

| Displayed at v6.4.22 | Status | Corrected display |
|---|---|---|
| $c'_Q=0.36915$ | below the certified majorant $0.3691523\ldots$ | $0.36916$ |
| $\lvert r\rvert\le1.51632\,q^{3/2}$ | below the value from the displayed ceilings ($1.5163227984\ldots$ with $\bar\tau=1.1548$, $c'_Q=0.36916$; $1.5163222210\ldots$ with $\bar\tau=1.1548$, $c'_Q=0.36915$; with the exact $\tau=2/\sqrt3$ and $c'_Q=0.36915$ it is $1.5163204\ldots$, still above) | $1.51633$ |
| factor $\le1.06252$ | below $(1-0.79246/20)^{-3/2}=1.0625206\ldots$ | $1.06253$ |
| $\lvert r_m\rvert\le1.61112\,Q_m^{3/2}$ | below the product of the displayed ceilings, and below the certificate's own exact $C_*=1.6111210\ldots$ | $1.61115$ ($1.51633\times1.06253=1.6111461\ldots$) |
| $403/250$ | holds in every variant | unchanged |

The last row is a new owner finding beyond the Atlas note: the displayed $1.61112$ is also a nearest-rounded display.

**RECOG** re-checks every use of $c'_Q=0.36915$ before dropping `[assuming: (D5)]`, including `recog_a1c_tail_averaging_cert.py` L55. This is not an automatic receiver acceptance.

## 5. v6.4.23 candidate scope (if the review confirms this list)

The edition is one stage, with no compaction and no science outside D1–D6. It carries:
1. **D1:** the successor RID, the old RID's `[scope:]` note, $q_{3/4}$, and the L12/L79/L307/L1162/L1456 updates.
2. **D2:** the new RID and the L797–798 display `[COR]`.
3. **D3:** the new RID and the L902 chain `[COR]`.
4. **D4–D6:** the §7.0 and §7 consumer register, current state only.

Then come a change-focused co-owner review, the Atlas row check, PI adoption, merge and tag.

After the tag:
- close the six pipe items and regenerate `pipes/DYAD/INDEX.md`;
- send notices: RECOG (the two RIDs, $c'_Q=0.36916$, the chain correction, the re-check request), NUMGEN (the "no", $q_{3/4}$, the successor RID) and OFN (receipt).

Deferred and outside this edition: the OPEN 21 re-basing, a footprint `[DEF]`, and the OPEN 20 analytic track.

## 6. Not claimed

- No canonical file, RID, grade, constant, pipe state or notice is changed by this draft.
- The recovered certificates' arguments are not re-audited by either owner. The checks are at statement and constant level, plus reruns.
- The footprint definition of the lost audits is not reconstructed.

## 7. Co-owner decision on this draft and the resulting final points

The co-owner reviewed commit `b2799bc` (PR #130 comment `6522082716`): **ACCEPT WITH ONE EDITORIAL CORRECTION**. This is acceptance of the joint SESSION scope, not adoption.

- **D1 successor:** accepted, with the name `DYAD-THM-OPEN18-STEP-MONOTONE`. The co-owner independently confirmed (mpmath, 85 digits) that the stated outward interval contains the root and that the endpoint signs are $+/-$. That is a sanity check beside the owner's Arb isolation (O1).
- **Old RID:** keep its historical grade; no demotion by editorial fiat (Methodology v1.4 §7). The `[scope:]` note must not leave a currently usable, unqualified first-footprint theorem. The note for v6.4.23 therefore reads, in the co-owner's sense:

  > `[scope: historical first-footprint formulation; the footprint predicate and branch legality are not substantiated by the recovered archive and are not available for a new downstream claim (evidence obligation open; records/dyad/DYAD_SOURCE_RECOVERY_LIST.md). The separately certified step-indexed content is DYAD-THM-OPEN18-STEP-MONOTONE. The isolation of the $\rho_4$ zero in $G$ does not establish equivalence with the missing footprint audit.]`

  The live OPEN 18 summary lines cite the successor for the closed monotonicity and keep the historical branch semantics marked as unresolved.
- **D3 chain:** the corrected chain $1.51633/1.06253/1.61115\le403/250$ and the point-of-use `[COR]` are accepted after the co-owner's independent exact cross-check. **Editorial correction applied here:** in the §4 table, the value with $c'_Q=0.36915$ and $\bar\tau=1.1548$ is $1.5163222210\ldots$, as in `l902_chain.json`. The $1.5163204\ldots$ figure is the value with the exact $\tau$, which the earlier draft had mixed in.
- **D2, D4–D6:** accepted as listed. OPEN 21 is deferred; OPEN 20 is excluded.

**Next gate:** a single-stage v6.4.23 candidate on a `claude/*` branch, with a change-focused proof and scope review, then the Atlas row check and the PI's decision. No adoption, merge, tag or pipe closure before that.

## 8. Addendum — D7, OFN v0.12 notice (owner disposition; co-owner confirmation needed)

A seventh item reached `pipes/DYAD/` on `main` after the two independent dispositions: `20261030-OFN-v0-12-adopted.md` (notice; nothing asked). OFN v0.12 (tag `ofn-v0.12`, `55ff8ba8…76aa`, adopted 30 Oct 2026) records the OPEN-OFN-3B evaluation frame and uses the raw-map identity $T(-x)+T(x)=(0,2(\cosh\rho-1))$ for `DYAD-DEF-PRIMITIVE-MAP`.

- **Owner check:** the identity follows directly from $T(\rho,\eta)=(\rho-\sin\eta,\ \eta+e^\rho-1-\sin\eta)$. It is checked symbolically (sympy) as gate C9 of the v6.4.23 checker.
- **Owner disposition: ACCEPT.** The consumer register goes to OFN v0.12, not v0.11, because v0.12 is the governing edition. OFN v0.12 §12.3 states the receipts of N4 (used, IMP-O08-12), N6 (received, no import) and N14 (used, IMP-O10-06/07).
- The v6.4.23 candidate carries this together with D6. The co-owner is asked to confirm D7 in the change-focused review.
