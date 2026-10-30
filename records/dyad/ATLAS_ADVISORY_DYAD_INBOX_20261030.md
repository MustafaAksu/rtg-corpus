# Dyadic inbox — Atlas advisory (six pipe items against `dyad-v6.4.22`)

**Date:** 30 October 2026. **By:** Claude, Atlas owner. The Atlas owner advises and does not decide; the Dyadic owners disposition each item and the PI decides any release.
**Status:** NONCANONICAL advisory. It adopts nothing and changes no pipe state.
**Object:** the six items in `pipes/DYAD/` at `origin/main` `15f1193`. All six are `open`.
**Governing source:** `dyad-v6.4.22` (tag object `2c50b7a2…`, commit `7130978f43b417d335622d2072abe9e571b4e142`), `dsn/RTG_DYADIC_OSCILLATOR_DSN.md` SHA-256 `2363ca409c08bc571378125771f27239b6426d3e7cdbe75e0306a2a728778c29`. The file on `main` is byte-equal to the file at the tag. Line numbers (L…) below refer to that file.

**Evidence states:**
- `EV-SRC-READ`: statements read at the tags named.
- `EV-RUN`: one atlas computation (§1.1), whose script and output are in `evidence/atlas/dyad_inbox_20261030/`.
- No Dyadic certificate was rerun. The certificates the requests rest on are not in the repository (§3).

## 0. Summary

| # | Item | Kind | Proposed disposition | Needs first |
|---|---|---|---|---|
| D1 | `20261026-NUMGEN-q-star-branch-split.md` | question | **answer: no — two different numbers** (§1a, after the upload). Dyadic's q* ≈ 1.2602142026 (ρ₄ = 0 on (0,q), Θ₄ at the funnel edge −π/3); NUMGEN's ≈ 0.3156258837 (η₆ = q). Rename one symbol and state the footprint definition in the OPEN 18 entry | owner confirmation of the Atlas reading of the recovered certificate |
| D2 | `20261029-RECOG-c7-ceilings-registration.md` | request | **accept; evidence now in hand** (§2.3). Register C₇ ≤ 85.1 (|z| ≤ 1/20) and C₇ ≤ 27.7 (|z| ≤ 1/40) — outward ceilings of the certified rational bounds 85.0731… / 27.6022… — as a stated sub-result under its own RID, keeping the adopted 100 / 30 | owner decision only |
| D3 | `20261029-RECOG-d5-bridge-constants-registration.md` | request | **accept with change; evidence now in hand** (§2.3). Register the row-A bridge lemma under its own RID with **outward** ceilings: c_Q ≤ 0.79246 is one, but the certified c′_Q is 0.3691523…, so the registered ceiling must be at least that (for example 0.36916), not the published 0.36915. Tell RECOG to re-cite | owner decision; RECOG re-checks its `[assuming:]` blocks with the corrected c′_Q |
| D4 | `20261026-NUMGEN-v1-21-adopted.md` | notice | **accept; update the consumer register** (NUMGEN v1.21 imports DYAD-THM-LPHASE-ROWA-REMAINDER) | — |
| D5 | `20261029-RECOG-v0-3-26-adopted.md` | notice | **accept; update the consumer register.** Optional: re-base OPEN 21 on the sharpened R9 rows | — |
| D6 | `20261030-OFN-v0-11-adopted.md` | notice | **accept; update the consumer register** (OFN v0.11 imports the two smooth theorems and the map RID) | — |

**Proposed route:**
1. The PI uploads the three missing evidence sets unchanged to `upload/dyad-sources`. The Atlas owner hash-checks and places them (§3).
2. The Dyadic owners record their dispositions.
3. A small maintenance edition, **v6.4.23**, carries the two registrations (if the certificates support them), the OPEN 18 definitions and the consumer-register update.

D4–D6 can be closed in that edition even if the evidence for D1–D3 is still missing.

## 1. D1 — the q* question

**Asked (NUMGEN, via Atlas).** Is DYAD-THM-OPEN18's q* the same number as NUMGEN's q*? NUMGEN's q* is the root of η₆(q)−q on the canonical family (ρ₀,η₀)=(0,q), η₆ wrapped (`numgen-v1.21` L909–912). It is `[RESULT] [from: NUM]`, not stated as a branch split.

**What Dyadic states (L600, L79, L307):**

> **OPEN 18 closed.** First-footprint branch monotonicity: dQ/dq>0 and dΘ/dq<0 on both branches Γ₃, Γ₄; q=q_* is the branch split. Certificate: `open18_arb_cert_final.cpp`.

Grade `[THM-ALG via IA]`; §8 `DYAD-ART-OPEN18` (L1162); evidence row L1456 ("not recorded" hash).

**Finding (D-SCOPE / D-PROOF (b)).** The live text defines neither "first footprint", nor the branches Γ₃, Γ₄, nor q*, and gives no value for q*.
- No tag in the repository (`dyad-v6.4.19` … `v6.4.22`) contains such a definition.
- The certificate is not in the repository.
- The certificate was **missing from the Atlas recovery list** (`records/dyad/DYAD_SOURCE_RECOVERY_LIST.md`). The list's file-name extraction skipped the six `.cpp` sources. This advisory corrects the list in the same PR (§3).

A one-line confirmation cannot therefore be given from the current record.

**Atlas computation (`EV-RUN`).**
- `evidence/atlas/dyad_inbox_20261030/qstar_repro.py` (mpmath, 60 digits) reproduces NUMGEN's root to 45 significant digits: q* = 0.315625883659561602974267621967906111219946754, with the sign change on (0.31562, 0.31563) and η₆ = q* without winding.
- At the root ρ₆ = 0.030723804262743386719.
- This confirms NUMGEN's number only. It does not show that the root is a first-footprint branch split.

**Proposed disposition.** Answer the item now:

> "not confirmable from the current Dyadic record; the definitions of the first footprint, Γ₃, Γ₄ and q* live in the OPEN 18 certificate and cell, which are to be recovered"

Then, once `open18_arb_cert_final.cpp` (and its run output, if any) is recovered, the Dyadic owner states three things in the OPEN 18 entry at v6.4.23:
- the footprint and branch definitions;
- q* with the precision the certificate supports;
- the one-line yes/no NUMGEN asked for.

This is a definition and scope repair at an unchanged grade. NUMGEN's NC-17 cross-citation waits for that line.

### 1a. After the upload (same day)

The PI uploaded the lab-server C++ sources (`upload/dyad-sources`, `59b3f87`; hash check `records/dyad/DYAD_UPLOAD_HASH_CHECK_20261030.md`). Among them, `open18_arb_cert3.cpp` names itself `open18_arb_cert_final.cpp` in its first line. It reran here unchanged with FLINT 3.0.1: micro strip, Γ₃ in 11 701 boxes and Γ₄ in 81 boxes, all SUCCESS.

What the certificate shows:
- It defines the branches by footprint step: **Γ₃ ↔ step 3** on q ∈ [0.001, 1.26021320256] and **Γ₄ ↔ step 4** on [1.26021520256, 2].
- It leaves out a gap of half-width 10⁻⁶ around 1.26021420256.
- It states that the root isolation of q* and branch legality come from separate footprint audits, which are not recovered.

The Atlas reading (`evidence/atlas/dyad_inbox_20261030/qstar_dyad_split.py`) finds that inside the gap only ρ₄ — equivalently Θ₄ + π/3 — changes sign, at

  **q_*^DYAD = 1.26021420256347711487243856095650439…**

There the fourth iterate meets the ISP-funnel edge Θ = −π/3 (§6.8). The OPEN 11 bulk record splits its sub-branches (4,11) | (5,11) at the same place (1.260 | 1.261).

NUMGEN's q* is 0.3156258836…, so **the answer to the question is no.** The two documents use one symbol for two different objects on the same canonical family (a D-SYM item).

**Revised proposed disposition for D1:**
- Answer "no", citing the recovered certificate.
- At v6.4.23, state in the OPEN 18 entry the footprint definition (which step counts as the footprint, from the audits or a fresh one-line definition), Γ₃/Γ₄, and q*'s defining equation and value.
- Suggest that NUMGEN rename its witness value (or that both sides add a subscript), so the cross-citation NUMGEN NC-17 wanted becomes a disambiguation instead.

The Dyadic owner confirms or corrects the reading; it is not an owner statement.

## 2. D2, D3 — the two RECOG registration requests

The two requests share one premise: RECOG uses numbers that appear in Dyadic only as **certificate values or proof-internal constants**, not as theorem rows. RECOG carries them as `[assuming:]`. Registering them would let RECOG drop the qualifier at its next release. Both are within Dyadic custody, and both are cheap *if* the certificate output supports the exact rounded statements.

### 2.1 D2 — C₇ ceilings (DYAD-THM-NF-REM)

**Source (L793–800).** The row table of DYAD-THM-NF-REM lists:
- row |z| ≤ 1/20: C₇ = 100 (certificate value 85.07);
- row |z| ≤ 1/40: C₇ = 30 (certificate value 27.60);
- C_D = 1000 / 250 (certificate values 812.89 / 216.77).

The constants travel with their radius and chart. Evidence row L1454: "as DYAD-THM-PRIM-CTR | v6.4.10 manifest | exact rational".

**Downstream users of the adopted 100 / 30** — these must not change silently:
- the L-PHASE proof's c₇ = 157.58 (L902);
- the OPEN 3 spiral bounds (L829);
- RECOG's unconditional rows;
- RECOG's γ₂ = 212.6, in which 2C₇ = 200.

**Proposed disposition: accept, conditional on evidence.**
- Register the certified ceilings as a **separate stated result** — for example "C₇ ≤ 85.1 on |z| ≤ 1/20, C₇ ≤ 27.7 on |z| ≤ 1/40, same chart, same norm" — under its own RID, or as an explicitly RID-labelled row of the NF-REM table.
- Keep 100 / 30 as the adopted constants that the existing proofs use.
- A new RID (rather than editing NF-REM's constants) keeps every current consumer's citation exact (Methodology v1.4 §4.4: a strengthened constant is a changed proposition).

**What the owner must check first.** The displayed "certificate value 85.07" may be a nearest-rounded value rather than an upper bound. The registration must state the certificate's own outward-rounded upper bound. That bound lives in the P2-B v2 evidence package (`DYAD_RETURN_ENCLOSURE_P2B_v2_evidence.zip`, recorded hash `e4e2bab004d4e39b76920e486607acc34749037ae2638809a9c2117d548fdbe4`, recovery list Tier 1, missing). RECOG states it will re-cite whatever value is registered.

**Gain, as RECOG states it:**
- the sharpened rows (221.4, 1/400) and (75.69, 1/1600) become unconditional;
- K_ε of RECOG-ALG-A1C-RECIPROCAL-DRIFT falls by about 15 %.

### 2.2 D3 — (D5) row-A bridge constants (DYAD-THM-LPHASE-ROWA-REMAINDER)

**Source (L894–903).** The theorem's proof outline states:
- the exact decomposition r = Λ₃(z) + [S_Θ−L_Θ] + τ[D_Q−D₃] + [Arg(J/z)+τq] + Arg(F̂/J), with Λ₃ = L_Θ + τD₃, under (B);
- the row-A bounds τ|D_Q−D₃| ≤ τ̄ c′_Q q², c′_Q = 0.36915, "from the exact polynomial D_Q of degrees 3–12";
- the bridge |D_Q| ≤ c_Q q^{3/2}, c_Q = 0.79246, giving the factor (1−c_Q/20)^{−3/2} ≤ 1.06252;
- "Every irrational factor … enters through a proved rational ceiling";
- certificate DYAD-ART-LPHASE-ROWA: 10 gates and negative controls N1–N6, byte-identical JSON on rerun (§8 L1197).

NUMGEN's receipt replay (`upload/numgen-records/NUMGEN_RECEIPT_REPLAY_LPHASE_ROWA_20261020_v0_1.md`) reproduces the bridge factor 1.0625204394, consistent with c_Q = 0.79246 (atlas arithmetic). It does not tabulate c_Q or c′_Q separately.

**Proposed disposition: accept, conditional on evidence.** Register a row-A bridge lemma under its own RID (name the owner's choice), containing:
- (i) the exact identity for r, as `[ALG]`, with the definitions of D_Q and D₃ (L808–811);
- (ii) |D_Q| ≤ c_Q q^{3/2} and |D_Q−D₃| ≤ c′_Q q² on the row-A disk |z| ≤ 1/20 of the NF-INV chart, with c_Q and c′_Q stated as the proved rational ceilings the certificate uses, as `[THM]`, `[proof: exact-rational certificate]`, with the gate names.

RECOG asked for "the domain (U_T / the row-A region)". The proof states the bounds on the row-A chart disk and uses them at block base points in U. The lemma should say exactly that, and should not widen anything.

**What the owner must check first:**
- which gates certify (ii);
- that 0.79246 and 0.36915 are ceilings, not nearest-rounded values.

The certificate files were placed in a Claude project folder, `claude/lphase_rowA/` (NUMGEN receipt §1), not in the repository.

**Gain:** RECOG-THM-A1C-SHARPENED-SCHEDULE, RECOG-ALG-A1C-LOGFREE-ENVELOPE and the A1c decoder blocks lose the (D5) qualifier at RECOG's next release.

### 2.3 After the second upload (same day)

The PI pushed `DYAD_RETURN_ENCLOSURE_P2B_v2_evidence.zip` and a NUMGEN review package that contains the four L-PHASE row-A files. All five hashes equal the DSN's recorded values. Both certificates rerun here, and both regenerate byte-identical outputs (`records/dyad/DYAD_UPLOAD_HASH_CHECK_20261030.md` §4a).

- **D2.** The certified exact rational bounds are C₇ ≤ 85.0731933471… (row |z| ≤ 1/20) and ≤ 27.6022209836… (row |z| ≤ 1/40). The DSN's "certificate values 85.07 / 27.60" are nearest-rounded. RECOG's 85.1 / 27.7 are valid outward ceilings, so the registration RECOG asked for is supported as worded.
- **D3.** The certificate computes c_Q = 0.79245761523… and c′_Q = 0.36915230466… exactly.
  - The published c_Q = 0.79246 is an outward ceiling.
  - The published **c′_Q = 0.36915 is 2.3 × 10⁻⁶ below the certified value**, so the certificate does not support it as a ceiling. That is not a proof that the true supremum exceeds 0.36915; it means the certified majorant does (point made by the ChatGPT co-owner, PR #125). The theorem's own constant 403/250 is unaffected, because the certificate uses the exact c′_Q.
  - Proposed: register the lemma with an outward c′_Q, for example 0.36916. At v6.4.23, correct the decimal in the proof outline (L902) as a `[COR]` of a displayed constant.
  - Ask RECOG to re-check the blocks that carry `[assuming: c′_Q = 0.36915]` — the sharpened schedule, the decoder blocks and the log-free envelope. The effect is presumably negligible, but a certified chain needs the outward value. For example, `evidence/recog/scripts/recog_a1c_tail_averaging_cert.py` L55 enters c′_Q as the point `I("0.36915")`. The other row-A constants on that line are proper ceilings of the certified values: c_J 0.50220 ≥ 0.50219804…, c₇ 157.58 ≥ 157.57641….
  - The decomposition identity for r stays as stated (an exact `[ALG]` identity under (B)).
  - **Two further display roundings in the same proof outline (L902).** The ChatGPT co-owner found them in PR #128 / PR #125 comment `6521673747`, and the Atlas checked them in floating point:
    - (1−c_Q/20)^{−3/2} with c_Q = 0.79246 is 1.0625206…, above the displayed 1.06252. Even the certified exact c_Q gives 1.0625204…, also above it.
    - The displayed ceilings 1401/1000, 123/125, τ̄·0.36915, 0.50220 and 157.58 combine to 1.5163204…, above the displayed 1.51632.
    - The final ceiling 403/250 = 1.612 still holds with outward values: 1.61112… with the published ceilings and c′_Q = 0.36916; ChatGPT's more conservative 1.611372.
    - The v6.4.23 `[COR]` should therefore restate the whole decimal chain of L902 with outward values, not only c′_Q.

With D1–D3 answerable, step 0 of §5 is complete except for the optional files listed in the hash check. Step 2 (the owners' disposition record) can start.

## 3. Evidence prerequisite and recovery-list correction

The registrations in D2 and D3 and the definitions in D1 should rest on evidence that anyone using the repository can inspect. That is the goal of the recovery list. Three sets are needed:

| Set | Files | Recorded hash | Serves |
|---|---|---|---|
| OPEN 18 | `open18_arb_cert_final.cpp` (+ output, if kept) | not recorded | D1 — **recovered 30 Oct** as `upload/dyad-sources/rtg-engine/open18_arb_cert3.cpp`, together with STRIP1, STRIP2, IA-BULK and QMAX (§1a; hash check record) |
| NF-REM / PRIM-CTR / NF-INV | `DYAD_RETURN_ENCLOSURE_P2B_v2_evidence.zip` | `e4e2bab004d4e39b76920e486607acc34749037ae2638809a9c2117d548fdbe4` | D2, and the §6.14 base generally |
| L-PHASE row A | `dyad_numgen_lphase_rowA_cert.py`, `qw.py`, `tzw.py`, `lphase_rowA_certificate.json` (+ `lphase_rowA_numeric.*`, `lphase_scope_checks.*`) | `117484ae…9cdb`, `3a913062…cce8`, `f007d42c…5609`, `8697c697…d4fa` (full hashes in the recovery list) | D3 |

**Upload from the laptop (PowerShell),** following the recovery list's delivery rule ("unchanged, any folder layout"):

```powershell
cd C:\GIT\rtg-corpus
git fetch origin
git switch -c upload/dyad-sources origin/main
New-Item -ItemType Directory -Force upload\dyad-sources | Out-Null
# copy the found files into upload\dyad-sources\ unchanged, then:
Get-ChildItem upload\dyad-sources -File | ForEach-Object { "{0}  {1}" -f (Get-FileHash $_.FullName -Algorithm SHA256).Hash.ToLower(), $_.Name } | Set-Content upload\dyad-sources\SHA256SUMS.txt
git add upload/dyad-sources
git commit -m "upload: DYAD evidence for the inbox items (OPEN 18, P2-B v2, L-PHASE row A), unchanged"
git push -u origin upload/dyad-sources
```

After the upload, the Atlas owner hash-checks the files, places them and updates the list (its §"How to deliver").

**Correction made in this PR.** The recovery list's first extraction missed the six C++ (FLINT/Arb) sources cited in §8:

| File | Artifact | Grade |
|---|---|---|
| `open18_arb_cert_final.cpp` | DYAD-ART-OPEN18 | THM-ALG via IA |
| `certify_transition_strip2.cpp` | DYAD-ART-STRIP2 | ALG via IA |
| `certify_transition_strip.cpp` | DYAD-ART-STRIP1 | ENG |
| `rtg_ia_bulk_cert.cpp` | DYAD-ART-IA-BULK | ENG |
| `certify_q_max.cpp` | DYAD-ART-QMAX | ENG |
| `rtg_ia_cert_fixed.cpp` | DYAD-ART-IA-CERT-FIXED | ENG |

They are added to Tier 1 (the first two, which back closed theorems OPEN 18 and OPEN 11) and Tier 2. The counts become 155 cited and 149 missing (Tier 1 66, Tier 2 46). A re-check of every backticked file name at `dyad-v6.4.21` and `dyad-v6.4.22` finds no other omission.

## 4. D4–D6 — notices and the consumer register

The three notices ask nothing. What they expose is that the Dyadic consumer register (§7.0 table L1060–1073, §7 consumer list L1077–1088) is behind the governing editions:

| Register entry at v6.4.22 | Current state | Source |
|---|---|---|
| OFN v0.10; imports IMP-O10-03/04/05, PRIM-CTR | OFN v0.11 (`ofn-v0.11`, `38a2f444…e9e4`): adds IMP-O10-06 `DYAD-THM-SMOOTH-EMBEDDING`, IMP-O10-07 `DYAD-THM-SMOOTH-EQUIVARIANT-CHART`; IMP-O08-12 `DYAD-DEF-PRIMITIVE-MAP`; receipts of N4, N6, N14 | D6 |
| NUMGEN v1.20.8; "Offered import" of LPHASE-ROWA, deferred | NUMGEN v1.21 (`numgen-v1.21`, `4805760d…5701`): LPHASE-ROWA **imported** at §6.6, pin `dyad-v6.4.22`; DYAD-ALG-P5-RADIAL recorded as the owner name of ΔQ₅; the Q403 pin aligned to v6.4.18 | D4 |
| RECOG v0.3.22 (current) | RECOG v0.3.26 (`recog-v0.3.26`, `45e307f8…dd34`). Rows for NF6, NF-REM, LPHASE (the (D5) constants under `[assuming:]`), NF-INV and PRIM-CTR. RECOG-ALG-A1C-RECIPROCAL-DRIFT uses NF6 and NF-REM rows only. The v0.3.26 Appendix B retractions touch no Dyadic statement | D5 |
| Genesis v2.8.9; "live Dyadic pins remain v6.4.13" | Genesis v2.9 (`gen-v2.9`): the older rows stay pinned to v6.4.13, and a scoped import from v6.4.22 adds `DYAD-THM-SMOOTH-EMBEDDING` and `DYAD-THM-SMOOTH-EQUIVARIANT-CHART` for the §6.3c G-20 note (`gen-v2.9` L1158–1163) | not a pipe item; found while checking D6 |
| Programme Overview v1.2; DSN Methodology v1.3 | Programme v1.3 (`programme-v1.3`); Methodology v1.4 (`methodology-v1.4`); companion rows only | BASELINE |

**Proposed disposition:** accept all three. At v6.4.23, update the §7.0 rows (L1060–1073) and the §7 consumer list (L1077–1088) to these editions, as current state only (no history lines). That includes the Genesis row, which no pipe item names.

Two consequences stay with the receivers and are not Dyadic's to state:
- RECOG still pins NUMGEN v1.20.8;
- Genesis's remaining v6.4.13 pins (its rows other than the G-20 import).

**Optional science item, from D5 (owner's choice).** DYAD-THM-OPEN21-PRIMITIVE-PHASE-REMAINDER is `[assuming: RECOG-THM-R9-MEMORY]` and uses C_{2,j} = 517 / 163 (L876–884). RECOG v0.3.25 registered RECOG-THM-R9-SHARPENED-ROWS: (259.2, 1/400) and (81.49, 1/1600), `[THM]`, unconditional, with the same scope, rows and chart (recog-v0.3.26 L660).

Re-basing OPEN 21 on those rows would roughly halve the R9 term. The atlas arithmetic on the published ceilings, which is not a certificate, gives:

| Row | C_{2,j}(256/225)² | K_j |
|---|---|---|
| A | 669.28 → 335.54 | 35.32 → ≈ 19.68 |
| B | 211.01 → 105.49 | 8.83 → ≈ 6.36 |

New published ceilings would need the owner's exact rational recomputation. The sharpened -C7 rows must **not** be used for this until D2 is settled.

## 5. Proposed sequence

| Step | Who | Content |
|---|---|---|
| 0 | PI | Upload the three evidence sets of §3 to `upload/dyad-sources`. If a set cannot be found, say so; the corresponding item is then answered as "remains proof-internal / not confirmable" |
| 1 | Atlas owner | Hash-check and place; update the recovery list; check that the certificate outputs contain the bounds D2/D3 need (statement level) |
| 2 | Dyadic owners | Disposition record for D1–D6 (accept / accept with change / decline, with reasons), separately and then jointly, as for OFN |
| 3 | Dyadic owners → receiving review → PI | **v6.4.23**: the D2/D3 registrations (new RIDs), the OPEN 18 definitions and the q* line, the consumer-register update, optionally the OPEN 21 re-basing; release record; tag |
| 4 | Dyadic owners | Close the six items; notices to RECOG (registered RIDs or "proof-internal"), NUMGEN (q* line) and OFN/NUMGEN (receipts) |

**If step 0 yields nothing:**
- D1 is answered "not confirmable";
- D2 and D3 are answered "remain certificate values / proof-internal; RECOG keeps `[assuming:]`";
- v6.4.23 shrinks to the consumer register.

This would still close all six items honestly.

## 6. Not claimed

- This advisory does not decide any item. It does not change any Dyadic text, grade, RID, constant or pipe state, and it does not assert that the certificates support the registrations — that is step 1.
- It does not touch the OPEN 20 analytic track (`evidence/dyad/open20-an/`, stage 2 INCONCLUSIVE `[NUM]`), which runs on its own records.
- The q* computation confirms NUMGEN's number, not its identity with Dyadic's q*.
