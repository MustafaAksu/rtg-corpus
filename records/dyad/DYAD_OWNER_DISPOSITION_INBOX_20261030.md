# Dyadic inbox D1–D6 — owner disposition (Claude, DSN owner)

**Date:** 30 October 2026. **From:** Dyadic DSN owner (Claude). **To:** the Dyadic co-owner (ChatGPT) for reconciliation; copy to the PI and the Atlas owner.
**Status:** owner disposition record (SESSION). It changes no Dyadic text, grade, RID, constant or pipe state. The governing edition stays `dyad-v6.4.22` (`dsn/RTG_DYADIC_OSCILLATOR_DSN.md`, SHA-256 `2363ca409c08bc571378125771f27239b6426d3e7cdbe75e0306a2a728778c29`; L… below refer to it).
**Inputs read:** the owners' entry note `records/dyad/DYAD_OWNER_ENTRY_NOTE_INBOX_20261030.md`, the Atlas advisory `records/dyad/ATLAS_ADVISORY_DYAD_INBOX_20261030.md`, the hash check `records/dyad/DYAD_UPLOAD_HASH_CHECK_20261030.md` (all on PR #125, branch `claude/atlas-advisory-dyad-inbox`, commit `80f1c7e`), the six items in `pipes/DYAD/`, the recovered `open18_arb_cert3.cpp` (self-named `open18_arb_cert_final.cpp`), the row-A certificate source and the P2-B v2 `certificate.json`.
**Independence:** written before reading the co-owner's record (PR #127, `f1a0e19`). From the PI's relay I know only its decision row (D1 and D3 accept with change; D2, D4–D6 accept), its D1 caution about the footprint definition, and its D3 figure $C\le1.611372$. Reconciliation follows separately.

## 0. Summary

| # | Item | Owner disposition | Basis |
|---|---|---|---|
| D1 | NUMGEN: is DYAD-THM-OPEN18's $q_*$ NUMGEN's $q_*$? | **ACCEPT WITH CHANGE.** Answer **no**. Dyadic's value is the unique zero of $\rho_4$ in the certificate gap, certified here; it is not a root of $\eta_6(q)-q$. The Atlas *value* is confirmed. Its *footprint* reading is corrected: $q_*$ is not where the first funnel step changes. At v6.4.23 state OPEN 18 without the unrecovered footprint notion, rename the symbol to $q_{3/4}$ | O1–O4 (§2) |
| D2 | RECOG: register the $C_7$ ceilings | **ACCEPT.** New RID, separate from NF-REM; NF-REM's $100/30$ unchanged | O5 (§3) |
| D3 | RECOG: register the (D5) row-A bridge constants | **ACCEPT WITH CHANGE.** New RID with $c_Q=0.79246$ and $c'_Q=0.36916$ (not $0.36915$); `[COR]` of the displayed $c'_Q$ at L902; $403/250$ unchanged, owner-checked in exact arithmetic | O6–O7 (§4) |
| D4 | NUMGEN v1.21 notice | **ACCEPT**; consumer register | §5 |
| D5 | RECOG v0.3.26 notice | **ACCEPT**; consumer register. The optional OPEN 21 re-basing is **deferred**, not in v6.4.23 | §5 |
| D6 | OFN v0.11 notice | **ACCEPT**; consumer register, including the Genesis v2.9 row found by the Atlas | §5 |

## 1. Owner checks (evidence)

Script `evidence/dyad/scripts/dyad_inbox_20261030_owner_checks.py` (SHA-256 `21aec87c555b8b68e0ea2e84833b13fae0f1a1a63f3b1c66959805e2791649e1`). Outputs are in `evidence/dyad/inbox-20261030/` (`SHA256SUMS.txt`; commands in `run.sh`). The inputs are PR #125's unchanged uploads, hash-checked by the script against the DSN-recorded values: row-A certificate `117484ae…9cdb`, `qw.py` `3a913062…cce8`, `tzw.py` `f007d42c…5609`; the P2-B v2 zip is `e4e2bab0…dbe4`.

| Check | Content | Result |
|---|---|---|
| O1 | $\rho_4$ changes sign on $[q_*-10^{-30},q_*+10^{-30}]$; $d\rho_4/dq\in[-0.6849\pm2.6\times10^{-5}]$ on the whole certificate gap $G=[1.26021320256,1.26021520256]$; $\eta_4<0$ on $G$ | PASS (python-flint, 256 bits) |
| O2 | $\eta_6(q_*)-q_*\in[-0.5536956463\pm2.5\times10^{-11}]$ | PASS (excludes 0) |
| O3 | $n=3$ and $n=4$ on all of $G$: $dQ_n/dq>0$, $N_{\Theta,n}<0$, $\Theta$-denominator $>0$ | PASS |
| O4 | `[NUM]` footprint reading on a 200 000-point grid of $(0,2]$ (§2.2) | reported, not a gate |
| O5 | P-2B v2 exact upper bounds: $C_7\le85.0731933471\ldots\le85.1$ (row $1/20$) and $\le27.6022209836\ldots\le27.7$ (row $1/40$); both exceed the displayed $85.07$ / $27.60$ | PASS |
| O6 | Row-A exact constants: $0.36915<c'_Q=0.3691523046\ldots\le0.36916$; $c_Q=0.7924576152\ldots\le0.79246$; the certificate's own gates pass and N1–N6 fail | PASS |
| O7 | The FIN constant recomputed with the published ceilings $c_Q=0.79246$, $c'_Q=0.36916$ is $1.611121735\ldots\le403/250$ (margin $8.8\times10^{-4}$); with the exact constants it is $1.611120963\ldots$ | PASS |

Negative controls exit 1 as intended:
- `--control A`: $q_*$ shifted by $10^{-20}$, so O1 fails.
- `--control B`: ceiling $0.36915$, so O6 fails.
- `--control C`: ceiling $85.07$, so O5 fails.

The JSON is byte-identical on rerun. Evidence level: **OWNER-RUN**. These checks verify statements and constants. Like the Atlas reruns, they are not a re-audit of the recovered certificates' arguments (for example the OPEN 18 micro-strip MVT step or the P2-B v2 tail).

## 2. D1 — the $q_*$ question

### 2.1 Answer to NUMGEN

**No.** On the canonical family $(\rho_0,\eta_0)=(0,q)$, Dyadic's branch-split value is
$$q_{3/4}=1.26021420256347711487243856095650439\ldots,$$
the unique zero of $\rho_4$ in $G$ (O1). Since $\eta_4<0$ there, $\Theta_4(q_{3/4})=-\pi/3$, the edge of the ISP-safe funnel (L602). It does not satisfy NUMGEN's condition: $\eta_6(q_{3/4})-q_{3/4}\approx-0.5537\neq0$ (O2). NUMGEN's $0.3156258836\ldots$ is a different number. This settles NUMGEN's precision note of 26 October as well.

### 2.2 Correction to the footprint reading

The recovered certificate defines nothing called a footprint. It sweeps the step-3 quantities on $[0.001,\inf G]$ (with a micro strip on $(0,0.001]$) and the step-4 quantities on $[\sup G,2]$. It assigns "branch legality and $q_*$ root isolation" to independent footprint audits, which are not recovered.

The Atlas reading says $q_*$ is where "the fourth iterate meets the ISP-funnel edge". That is true as an identity, but it does not make $q_*$ the point where the *first* funnel step changes:
- Step 3 stays inside the angular window $[-2\pi/3,-\pi/3]$ until $\Theta_3=-2\pi/3$ at $q=1.36713045\ldots$. With the $Q<Q_c$ condition of the funnel, it stays inside until $Q_3=Q_c$ at $q=1.34159703\ldots$.
- On $(q_{3/4},1.367)$, both steps 3 and 4 are in the window (10 692 of the 200 000 grid points, O4).
- Step 4 leaves the funnel's $Q<Q_c$ part at $q=1.97865695\ldots$, inside the certificate's $\Gamma_4$ range $[\sup G,2]$.

So "first footprint = first step in the ISP-safe funnel" does not reproduce the certificate's split. `[NUM]` (O4) gives the following reading. The split is reproduced on every grid point by "the **last** step $k\le6$ whose $\Theta_k$ lies in the closed window $[-2\pi/3,-\pi/3]$, without the $Q<Q_c$ condition". It is not reproduced by "the first such step" (10 692 mismatches). This is a reading of the certificate's ranges, not the historical audit definition, and nothing here certifies branch legality under it.

### 2.3 What is certified now

- The step-3 monotonicity holds on $(0,\sup G]$ and the step-4 monotonicity on $[\inf G,2]$: the recovered certificate (Atlas rerun) plus O3, which closes the gap $G$ for both steps.
- $q_{3/4}$ is isolated to $\pm10^{-30}$ and is unique in $G$ (O1).

Together these give the analytic content of DYAD-THM-OPEN18 without any footprint notion. The only parts that rest on the unrecovered audits are the words "first footprint" and the claim that $\Gamma_3$, $\Gamma_4$ *are* footprint branches.

### 2.4 Proposed v6.4.23 change (for reconciliation)

1. **Restate DYAD-THM-OPEN18 definition-free, at the unchanged grade `[THM-ALG via IA]`.** The text would read: "On the canonical family, $dQ_3/dq>0$ and $d\Theta_3/dq<0$ for $q\in(0,q_{3/4}]$; $dQ_4/dq>0$ and $d\Theta_4/dq<0$ for $q\in[q_{3/4},2]$; $q_{3/4}$ is the unique zero of $\rho_4$ near $1.2602142$ ($\Theta_4=-\pi/3$), $q_{3/4}=1.260214202563477114872438\ldots$."
   - Certificates: DYAD-ART-OPEN18 plus this owner gap closure.
   - The RID stays, because the proposition is the same certified monotonicity with its scope made explicit (a definition and scope repair, D-SCOPE). The co-owner may argue for a new RID.
2. **Footprint.** Do **not** substitute a new definition for the unrecovered one; I agree with the co-owner's caution. Either keep the phrase "first footprint" only as a labelled historical name with a `[scope:]` note saying that its definition and the branch legality audits are unrecovered (`records/dyad/DYAD_SOURCE_RECOVERY_LIST.md`), or drop it from the statement. I prefer dropping it from the theorem line and keeping one sentence in the §6.8 text. The "last window step" reading may be recorded as `[NUM]` observation only. A footprint definition can enter later as a `[DEF]` with its own legality certificate, as a separate item.
3. **Symbol.** Dyadic renames its value to $q_{3/4}$, in the pattern of OPEN 11's $q_{10/11}$ (L642, L1157). NUMGEN keeps $q_*$. The NUMGEN cross-citation becomes a disambiguation line on NUMGEN's side.
4. **Evidence row L1456.** Replace "not recorded" with the recovered file's hash (`a9acb69f…6ae4`, PI-supplied, identified by its first line), and add this record's script as the gap-closure and isolation evidence.

## 3. D2 — $C_7$ ceilings

**ACCEPT.** The certified exact bounds are $85.0731933471\ldots$ ($|z|\le1/20$) and $27.6022209836\ldots$ ($|z|\le1/40$), so RECOG's $85.1$ / $27.7$ are valid outward ceilings (O5).

**Form: a new RID**, proposed name `DYAD-THM-NF-REM-C7-SHARP`:
- Statement: $|\widehat F(z)-J(z)|\le C_7|z|^7$ with $C_7=85.1$ on $|z|\le1/20$ and $C_7=27.7$ on $|z|\le1/40$, same chart and norm as DYAD-THM-NF-REM.
- Grade and evidence: `[THM]`, `[proof: exact-rational certificate]`, DYAD-ART-RE-P2B2, `certificate.json` `value_rational_upper` (file SHA-256 `d59b0ff6…c6ce` inside the zip `e4e2bab0…dbe4`).
- I reject the alternative (an RID-labelled row of the NF-REM table), because a strengthened constant is a changed proposition (Methodology v1.4 §4.4), and a separate RID keeps every existing NF-REM citation exact.
- NF-REM's adopted $C_7=100/30$ and $C_D=1000/250$ stay. The certificate's $C_D$ bounds $812.89$ / $216.77$ were computed with $C_7=100/30$ and are not re-derived with the sharper values; the new RID states $C_7$ only.
- The downstream uses of $100/30$ are not touched: L-PHASE $c_7=157.58$ (L902), OPEN 3 (L829), the row-A certificate's imported $C_7=100$, and RECOG's unconditional rows.
- **Display fix:** in the NF-REM row table (L797–798), "certificate value $85.07$ / $27.60$" becomes "certified bound $85.0732\ldots$ / $27.6023\ldots$" (truncated upward), so that no displayed value reads like a ceiling below the bound. This is a `[COR]` of displayed numbers only.

## 4. D3 — row-A bridge constants

**ACCEPT WITH CHANGE.** New RID, proposed name `DYAD-THM-LPHASE-ROWA-BRIDGE`, with the content RECOG asked for and no wider:
1. `[ALG]` The exact decomposition $r=\Lambda_3+[S_\Theta-L_\Theta]+\tau[D_Q-D_3]+[\operatorname{Arg}(J/z)+\tau q]+\operatorname{Arg}(\widehat F/J)$, $\Lambda_3=L_\Theta+\tau D_3$, under (B), with the definitions of $D_Q$ and $D_3$ (L808–811).
2. `[THM]` `[proof: exact-rational certificate]` On the row-A disk $|z|\le1/20$ of the NF-INV chart, used at block base points in $U$:
   - $|D_Q|\le c_Qq^{3/2}$ with $c_Q=0.79246$;
   - $|D_Q-D_3|\le c'_Qq^2$ with $c'_Q=0.36916$.

   Gates P-a (P-a1, P-a2) of DYAD-ART-LPHASE-ROWA. The certified values are $0.7924576152\ldots$ and $0.3691523046\ldots$ (O6).

**`[COR]` at L902.** "$c'_Q=0.36915$" becomes "$c'_Q=0.36916$". Reason: the certificate's exact majorant is $0.3691523\ldots>0.36915$, so $0.36915$ is not a certified ceiling. This does not show that the true supremum exceeds $0.36915$.

**$403/250$ is unchanged.** The certificate's FIN uses the exact $c'_Q$. The owner check O7 substitutes both published ceilings and still finds $C_*\le1.6111218<1.612$. The co-owner relayed $C\le1.611372$, a different conservative figure; both are below $1.612$. The difference in method is to be reconciled; it does not affect the disposition.

**RECOG** must re-check every block that carries `[assuming: c'_Q = 0.36915]`. Examples:
- `evidence/recog/scripts/recog_a1c_tail_averaging_cert.py` L55 enters it as `I("0.36915")`; this is a receiver item;
- the sharpened schedule, the decoder blocks and the log-free envelope.

## 5. D4–D6 — consumer register

**ACCEPT all three.** All the tags exist in the repository: `numgen-v1.21`, `recog-v0.3.26`, `ofn-v0.11`, `gen-v2.9`, `programme-v1.3`, `methodology-v1.4`.

At v6.4.23, update the §7.0 rows and the §7 consumer list (Atlas advisory §4 gives the line ranges) to current state only, as listed there:

| Consumer | Update |
|---|---|
| NUMGEN | v1.21: LPHASE-ROWA imported; P5-RADIAL owner name; Q403 pin |
| RECOG | v0.3.26: rows NF6, NF-REM, LPHASE, NF-INV, PRIM-CTR |
| OFN | v0.11: IMP-O10-06/07, IMP-O08-12, receipts N4/N6/N14 |
| Genesis | v2.9: scoped import of SMOOTH-EMBEDDING and SMOOTH-EQUIVARIANT-CHART |
| Programme / Methodology | v1.3 / v1.4 companion rows |

Receiver-side pins are not Dyadic's to state: RECOG still pins NUMGEN v1.20.8, and Genesis keeps its other v6.4.13 pins.

**D5 option (OPEN 21 re-basing): deferred.** It is a changed proposition with new constants. It needs an exact recomputation of $K_j$, and it rests on RECOG-THM-R9-SHARPENED-ROWS, which the Dyadic owners have not audited. It does not belong in a maintenance edition. A separate owner item can take it up after v6.4.23; it must use the unconditional rows only, never the -C7 rows.

## 6. Proposed v6.4.23 scope (owner side)

The edition carries:
- the D2 RID with the NF-REM display fix;
- the D3 RID with the `[COR]` at L902;
- the D1 restatement of OPEN 18 (§2.4: definition-free statement, $q_{3/4}$, footprint scope note, evidence row L1456);
- the consumer register (D4–D6).

One stage, no compaction. Then come a change-focused co-owner review, the Atlas row check, PI adoption, merge and tag.

After the tag:
- close the six pipe items;
- send notices to RECOG (the two RIDs and $c'_Q=0.36916$, with the re-check request), NUMGEN (the "no" and $q_{3/4}$) and OFN (receipt).

## 7. Not claimed

- No pipe state, DSN text, grade, RID or constant is changed by this record.
- The recovered certificates' arguments are not re-audited; the checks here are at statement and constant level.
- The O4 footprint reading is `[NUM]` and is not proposed as a definition.
- Nothing here touches the OPEN 20 analytic track.
