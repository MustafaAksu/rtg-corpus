# AZ — Reactivation triage

**[SESSION] Working record of the AZ stream (Arithmetic Resonance and Zeta); no scientific or release authority. Nothing in this record is adopted.** It proposes dispositions for the PI to decide; the AZ DSN is not edited by it.
**Date:** 10 November 2026. **By:** Claude, AZ co-owner session (BOOTSTRAP message 2 of `records/az/AZ_COOWNER_SESSION_ORIENTATION.md`; the PI asked this session to write the record, project conversation, 10 Nov 2026, 18:31 +03:00).
**Subject edition:** `az-v0.6` — `dsn/RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN.md`, SHA-256 `dec78a4721d2f34711218d9b79ba0ce6438523060098f770cad5dd3f5eb70b8a` (tag object `d0cc5e7d…13da` → commit `d7d661c`; equal on `main` `ebf1163`). Line numbers below are lines of that file.

## 1. What was read, and what was not

Read at the tag, hash computed from the tagged bytes and equal to `BASELINE.md` (`EV-SRC-READ`, `EV-HASH`):

| Source | Tag | SHA-256 | Read |
|---|---|---|---|
| AZ | `az-v0.6` | `dec78a47…0b8a` | in full |
| Dyadic | `dyad-v6.4.23` | `9f874ccc…25cb` | §1 OPEN 9 readout, §2 OPEN 9, §6.11, §7.0 consumer row, Appendix D, Appendix E rows of the RIDs AZ cites, Appendix F, Appendix G |
| TDR-G | `tdrg-v2.12.14` | `3be72923…2392` | header, §1 scaling block, §2 TDR-24 chain and TDR-26, §6.1, §6.2, §6.5, §6.12, §7 |
| Genesis | `gen-v2.10` | `63c3b020…3d62` | header, §1 OPEN 1C readout, §2 OPEN 1 / 1A / 1C / OPEN-GEN-II-7B entries |
| Programme | `programme-v1.4` | `37d857d0…28c0` | §5 OPEN-P1, §6.1, the AZ entries of §6.5, §6.6 and §6.7, §7.1, §7.2 (IF20, IF21), §8, §9.2, Appendix B |
| OPEN-M | `uvm-v0.7.1` | `0a51644d…f53e` | header, R15, R16, the §5 row on the SU(2) ×2 branch, the Appendix A/B entries on R15/R16 |
| Methodology | `methodology-v1.4` | `cdacab5f…f2df` | §4.2 and §4.3 in part; the tag registry searched for `THM-ALG` only |
| DZT | `dzt-v0.8` | `cad20982…2ff2` | only SG-DZT-1 and the anomaly-set entries (for Atlas AZ.A5) |
| Atlas | `atlas-v0.11` | `8d7a43f0…f358` | the AZ findings (AZ.A1, A2, A3, A5, A7; H2, H3) |

Also read on `main`: `CONVENTIONS.md`, `BASELINE.md`, `pipes/README.md`, `pipes/AZ/*`, `records/atlas/ATLAS_ADVISORY_TO_PI_DORMANT_OWNERS_20261110.md`, `records/dyad/DYAD_NOTICES_N16_N21.md` (the AZ rows). The release records of Dyadic v6.4.23, TDR-G v2.12.14, Genesis v2.10, Programme v1.4 and Methodology v1.4 exist and each names the hash above; they were not read beyond that check and the AZ lines of the TDR-G record.

Live state, 10 Nov 2026 15:13 UTC (`tools/orient.py`, read-only): no release record for `az-v0.6`; three open PRs (#189, #183, #160), none touching AZ paths; no remote branch differs from `main` on AZ paths (59 checked); inbox two items, both `open`; no outbound AZ item.

**UNVERIFIED:**

1. **The pinned editions are not in the repository.** No tag or file exists for Dyadic v6.4.8.1, TDR-G v2.12, Genesis v2.8.4, Programme v1.1, OPEN-M v0.6, Methodology v1.2 or AZ v0.5. Every row below compares the AZ text with the *current* owner text; whether AZ reproduced its pinned edition faithfully cannot be checked.
2. **No AZ evidence is in the repository.** `evidence/az/` does not exist, and no file named in AZ §9 was found anywhere in the tree (search by file name). PI, 10 Nov 2026: the files may still exist locally; they were not located today.
3. `MustafaAksu/rtg-lit` was not consulted. `pipes/AZ/` holds no LIT item.
4. No computation was rerun (`EV-NOT-RERUN` for every numerical or certificate statement).

A second entry report, by the ChatGPT co-owner session, and its reply to the comparison were relayed by the PI in the project conversation of 10 Nov 2026; they are not in the repository. Row 16 was raised there and rechecked here at the owner text. The two reports agree on every other row; where they first differed (pipe items carry no obligation; the evidence is absent, not merely unlocated in the tree; BIND3 is not in the TDR-G item), the ChatGPT session withdrew its reading.

## 2. Classification

**Effect on AZ** (the three classes of the bootstrap message):

- **claim** — the row changes what AZ asserts: a statement, a scope, a status, or a quoted rule. No row changes the grade of an AZ-owned result; where the changed statement is an imported one, the grade stays the owner's.
- **id/pin** — an identifier, a version pin or a section pointer only.
- **none** — AZ's text agrees with the current owner text.

**List:** (i) corrections edition, no new science, no grade raised; (ii) needs new work or a separate decision; — no action.

## 3. Rows

### 3.1 The row the PI decided first (advisory row 1)

| # | AZ v0.6 | Current owner text | Effect | Proposed disposition | List |
|---|---|---|---|---|---|
| 1 | §6 "To OPEN M" (l. 440): "the legal correction is ×2, not ×4; applying ×4 is a certified dimensional type error under AUDIT-1-DIMENSIONAL in the OPEN-M ledger" | OPEN-M v0.7.1 R16 `[COR]` (`UVM-RESULT-AUDIT1`): the v0.6 "legal SU(2) correction = 2×" is withdrawn as a physical conclusion; the 2× branch is conditional on two unproved bridges; the 4× energy factor is "not directly admissible" in the amplitude-linear inequality; "no certified numerical deficit factor exists". R15 (`UVM-NUM-2F-RHO`) is a calibration-conditional diagnostic. | claim | Replace the sentence by a pointer to OPEN-M v0.7.1 R15/R16 with its verdict. Keep what still holds in the owners: the face-flux identity is a Dyadic `[import-ref]`; $E_{\rm full}/E_{\rm half}=4$ is source-scoped; the cascade test is linear in the source amplitude. One Appendix B correction entry. Atlas AZ.A1 / H2. | (i), first |

### 3.2 Version pins

| # | AZ v0.6 | Current | Effect | Proposed disposition | List |
|---|---|---|---|---|---|
| 2 | Programme v1.1 (header l. 11; §3 l. 151–157; §7 l. 449) | `programme-v1.4` | id/pin | Repin; content rows 27, 28. | (i) |
| 3 | Dyadic v6.4.8.1 (14 places: header l. 11; §0.1 l. 63; §1.2 l. 98, 103; §4.1 l. 199–243; §6 l. 427; §7 l. 462; §8 l. 477, 479) | `dyad-v6.4.23` | id/pin | Repin every `[import-ref]` row; content rows 9–18. The dated history lines (§1.3 l. 111, §10, Appendix A) record what earlier editions did and stay as written. | (i) |
| 4 | TDR-G v2.12 (8 places: header l. 11; §0.1 l. 64; §4.2 l. 268, 271, 285; §7 l. 463, 471; §8 l. 495; also "TDR-G v2.12" at l. 281 and §5 l. 410) | `tdrg-v2.12.14` | id/pin | Repin; content rows 19–26. History lines as in row 3. | (i) |
| 5 | Genesis v2.8.4 (header l. 11; §0.1 l. 70; §6 l. 437) | `gen-v2.10` | id/pin | Repin; content row 29. | (i) |
| 6 | OPEN-M v0.6 (§0.1 l. 70) | `uvm-v0.7.1` | id/pin | Repin; content row 1. | (i) |
| 7 | *Supersedes:* v0.5, no hash (header l. 10) | — | id/pin | v0.7 header: *Supersedes* = v0.6 with its hash and tag (CONVENTIONS §3). | (i) |
| 8 | DSN Methodology v1.2 (header l. 6, l. 11; aliases l. 29) | `methodology-v1.4` | id/pin | **Keep the v1.2 declaration in v0.7** and name v1.4 as the governing edition beside it, as TDR-G v2.12.14 did by PI decision. Declaring v1.4 without restructuring the file would be false. The migration is a separate, PI-decided edition (orientation note, BOOTSTRAP 4). | (ii) |

### 3.3 Dyadic — Thread A (§1.2, §4.1, §6, §8)

| # | AZ v0.6 | Dyadic v6.4.23 | Effect | Proposed disposition | List |
|---|---|---|---|---|---|
| 9 | `DYAD-THM-RAW-CUBIC` (l. 204, l. 481): "The raw cubic coefficient of the $p$-step map is exact." `[THM]` | §2 OPEN 9: the $z^2\bar z$ coefficient of the **raw one-step map**; "not a statement about the raw $p$-step map"; scope $p\ge3$; formula recovered and algebraically verified, identity with the historical proposition not yet established (Appendix E). | claim | Restate at the owner's scope with the caveat and the range. Answers the DYAD notice. | (i) |
| 10 | "holds iff $b\le4$" (§1.2 l. 103); "vanishing iff $b\le4$" (§8 l. 488) | §2 and §6.11: the "iff $b\le4$" shorthand is withdrawn (v6.4.11); vanishing for $b\in\{2,3,4\}$, first failure at $b=5$ for every $p\ge6$, $b\ge6$ `[OPEN]`. Result RID `DYAD-ALG-B5-ALLP-NONVANISHING`; `DYAD-OPEN-B5-ALLP` is the closed lifecycle identifier. | claim + id | Use the owner's wording in both places (§4.1.1 l. 229 already has it); cite the result RID. | (i) |
| 11 | §4.1.2 l. 245 and §6 l. 427: "exact cubic cascade formula for $q=4,(0,3)$" listed as open | Closed: `DYAD-THM-Q403-PHASELAW` `[THM]`, scope $p=4s$, $s\ge2$ (v6.4.9). | claim (status) | Move to §4.1.1 as an `[import-ref]` `[THM]` row at the owner's scope; drop from both frontier lists. Atlas AZ.A2. | (i) |
| 12 | §4.1.2 l. 250: "$-13+15\sqrt3/2\approx0.0096$" | $\approx-0.0096$, modulus $0.0096$ (sign restored at v6.4.20). | claim (sign) | Correct this line. §1.2 l. 100 and §4.1.1 l. 217 print the modulus and are right. Answers the DYAD notice. | (i) |
| 13 | §4.1.2 and §6: AZ's copy of the open Dyadic frontier (six items) | §2 OPEN 9 active sub-items: nine, of which four are not in AZ (general Lie-gauge retained-channel theorem; higher lattice harmonics; asymptotics of $G_{32}(p)$; the h-source bridge); the near-cancellation item is now the large-$p$ behaviour of $\lvert Q_p\rvert$. | claim (status) | PI choice: (a) keep AZ's list, corrected by rows 11–12, with a line that the owner's current list is Dyadic §2 OPEN 9; or (b) replace the list by that pointer (Programme v1.4 §6.7 proposes that AZ reduce duplicated owner summaries). Proposed: (a) in v0.7, (b) with the restructuring. | (i) for (a) |
| 14 | `DYAD-ALG-Q3-CANCEL` (l. 235, l. 491) | Not an owner RID. The statement is `DYAD-ALG-Q3-DEG2-CANCEL` (registered at v6.4.20); no alias is created (Appendix F). | id/pin | Repin. Atlas AZ.A7, advisory row 3. | (i) |
| 15 | l. 235: the $q=3$ cancellation is "anchored by the eigenframe linear-part lemma"; l. 237: the subgroup-charge projector objects "make the formalism computable" | Appendix D: the lemma's statement and the definitions of eight of the projector objects are not recovered; the owner keeps the names and its `[ALG]` grades. $\chi_p$, $K^{\rm extra}_{p,q}$ and $\lvert K^{\rm extra}_{p,q}\rvert=s-1$ are defined. | claim (qualification) | Carry the owner's qualification on both rows. No owner grade is questioned by AZ. | (i) |
| 16 | §8 l. 492: `[RID: DYAD-OPEN-P-RESONANCE — subgroup cardinality]` and the other "— sub-item" labels (l. 484, l. 488) | Appendix F: "sub-labels are not identifiers". The cardinality lemma is a closed sub-item of OPEN 9 with no RID of its own. | id/pin | Cite as a named sub-item of `DYAD-OPEN-P-RESONANCE`, not as a result RID. | (i) |
| 17 | `DYAD-ALG-DIRECT-WEIGHT`, `DYAD-ALG-CROSS-IDENTITY`: source "§6.11" (l. 231, l. 233) | Both RIDs are registered at §2 OPEN 9 (Appendix E location column). | id/pin | Correct the section pointer. | (i) |
| 18 | $p=5$: "$\nu_5^{(5)}$ exact over $\mathbb{Q}(\sqrt5,\sqrt{10+2\sqrt5})$" (l. 208) | Exact in $\mathbb{Q}(\zeta_5)$; the radical field is that of the real and imaginary parts (label corrected at v6.4.20, value unchanged). | id/pin (label) | Correct the label. | (i) |
| — | `DYAD-ALG-P567-LEDGER`, `DYAD-ALG-GLATTICE5`, `DYAD-ALG-VANISH-B2/B3/B4` (ranges $p\ge4,5,6$), `DYAD-ALG-P6-FACEFLUX` (transfer `[CAND]`, now `DYAD-CAND-P0-DYADIC`), `DYAD-ART-B5-SECULAR`, the $G_{04}(10)$ reinterpretation, the $p=7$ and universal-$q=4$ `[FAIL]` rows | Same identifiers, same statements. | none | Repin only (row 3). The DYAD notice's VANISH-B2 point needs no change: AZ already prints $p\ge4$. | — |

### 3.4 TDR-G — Thread B (§4.2, §8)

| # | AZ v0.6 | TDR-G v2.12.14 | Effect | Proposed disposition | List |
|---|---|---|---|---|---|
| 19 | `TDRG-ZN-STATE`, source "§1" (l. 271, l. 497) | Owner RID `TDRG-DEF-ZN-STATE`, §6.1; AZ's name resolves through the §7 map. | id/pin | Repin, correct the section. Atlas AZ.A7. | (i) |
| 20 | `LEM-REACH` (l. 273, l. 498) | `TDRG-ALG-LEM-REACH`; the $k=0$ case is `TDRG-THM-REACHABILITY-K0`. Statement unchanged. | id/pin | Repin. | (i) |
| 21 | `LEM-RETRIG`: "exact two-node period-2 retrigger criterion" (l. 275) | `TDRG-ALG-LEM-RETRIG`: bound state of period dividing 2; least period 2 for $d\ne0$, fixed point at $d=0$ (v2.12.14 `[COR]`). | claim (wording) + id | Repin; use the owner's wording. Answers the TDRG notice. | (i) |
| 22 | `LEM-SPECCONS`: "Equivalently, the multiset $\{\gcd(d_{ij},N)\}$ is conserved" (l. 277) | `TDRG-ALG-LEM-SPECCONS`: the gcd multiset is a consequence only; the converse fails ($N=24$: $\lvert d\rvert_c=1$ and $5$ share $\gcd=1$) (v2.12.14 `[COR]`). | claim + id | Repin; replace "Equivalently" by "in particular". Answers the TDRG notice. | (i) |
| 23 | `BIND3-*` (l. 279, l. 501) | `TDRG-ALG-BIND3-CYCLE-N24K1`, `TDRG-NUM-BIND3-PARITY`, `-SPECTRAL-GATE`, `-MEMORY-PARITY`, `-XFER`, `-REGEN`. The numbers carry `[conv: v18 path orientation]` and are not rerun; the suite artifact is missing at the owner. | id/pin + scope note | Repin; carry the convention tag. Atlas AZ.A7. | (i) |
| 24 | N-scaling (l. 281–283): $1.041\cdot N^{-0.869}$, "strongly supports thermodynamic crystallization", `[NUM strong / HEUR strong in source]` | Same fit and $R^2$. The exponent is window-dependent ($N^{-0.730}$ on $N=480$–$1440$), "not a structural constant"; the $N\to\infty$ reading is `[HEUR]` (§1; §5 row). | claim (qualification) | Add the window statement; use the owner's tags. | (i) |
| 25 | "TDR-24 frontier … slot-volume identity, topological filtering, and geometric compression. It must close before…" (l. 287); label `TDR-24 / N-SCALING` (l. 502) | TDR-24D and TDR-24F are closed at the mechanism level; the gate is TDR-24A → 24B → 24C. Owner RIDs: `TDRG-OPEN-TOPO-FILTER` (24A), `TDRG-OPEN-CHI-SCALING` (24B), `TDRG-OPEN-THERMO-SUPPRESS` (24C), `TDRG-OPEN-NSCALING` (TDR-23). `TDR-24 / N-SCALING` is not an owner RID. | claim (status) + id | State the current chain; cite the owner RIDs. Atlas AZ.A7. | (i) |
| 26 | `TDR-26-BIRTH-ANCHOR` (l. 503) | Not an owner RID; the entry is OPEN TDR-26, `TDRG-OPEN-LOCKING-FAIL` (§2). Rule, counts and tag split unchanged. | id/pin | Repin. Atlas AZ.A7. | (i) |
| — | §4.3.6 reference to the response-tensor branch (inter-birth-interval CV) | Exists as `[BRANCH — TDRG-RESPONSE-TENSOR]`, exploratory. | none | — | — |

### 3.5 Programme, Genesis

| # | AZ v0.6 | Current | Effect | Proposed disposition | List |
|---|---|---|---|---|---|
| 27 | §3 l. 153–157: SG-PROG-1, -2, -4 quoted in their v1.1 wording | Programme v1.4 §8: all three texts replaced (Appendix B, PROG12-C11 and others); SG-PROG-4 is no longer a tier test. | claim (quoted rule) | PI choice: quote the v1.4 texts, or replace the quotes by pointers to Programme v1.4 §8. Proposed: pointers, with AZ's own one-line application kept. | (i) |
| 28 | §0.1 l. 69 "patch requested"; §6 l. 442–443; §7 l. 447–471: request that the Programme register AZ | Met: registered since v1.2; v1.4 §6.1 (Tier 5, `az-v0.6`), §6.5, §7.1 graph, §7.2 IF20 and IF21. | claim (status) | Replace the request by a statement of the registration; delete the proposed entry text. Atlas AZ.A3. | (i) |
| 29 | §6 l. 437: "Genesis v2.8.4 closes OPEN 1C and certifies that the $\mathcal{P}_4$-only cascade is impossible in the reduced birth-race model; the cascade question routes through OPEN M" | Two separate entries: OPEN 1C (`GEN-OPEN-CHIRAL-ADMISS`) is closed `[THM]` since v2.2; the $\mathcal{P}_4$-only impossibility is an OPEN 1 sub-item, `[RESULT]` `[scope: reduced birth-race model]`, "not a theorem over arbitrary $\mathcal{M}_{\rm phase}$"; the cascade routes to `GEN-OPEN-UVJET-ALPHAF` (OPEN-GEN-II-7B) and OPEN M. OPEN 1 (`GEN-OPEN-PHASE-DIST`) stays ACTIVE. | id/pin + wording | Repin; cite the two entries separately with the owner's scope tag. Atlas AZ.A2. | (i) |
| — | OPEN-P0, OPEN-P1 (`RTG-OPEN-DISCRETE-BRIDGE`), `RTG_DISCRETE_CONTINUOUS_BRIDGE` | Both ACTIVE; the bridge document is still "Proposed". | none | — | — |

### 3.6 AZ's own content

| # | Item | Finding | Effect | Proposed disposition | List |
|---|---|---|---|---|---|
| 30 | Thread C (§4.3), the AZ-owned results and the retraction block | No owner source corrects anything here. The static-geometry reclassification, Level A and the `[bridge-disqualified]` status stand. | none | No change in v0.7. | — |
| 31 | §9 (l. 516): hashes "are stored in `AZ-ART-AZV5-REGISTRY`"; SG-AZ-5 provenance "is satisfied by the manifest reference" | The registry and every §9 file are absent from the repository (§1, UNVERIFIED 2). The grades of the Thread C results are not changed by that; their evidence cannot be inspected from the repository. | claim (availability) | (i) one sentence in §9: the files are not in the repository as of v0.7 and are not described as recreated (CONVENTIONS §5). (ii) recovery: the PI locates the files; they arrive unchanged on an `upload/…` branch, are hash-checked against the registry and placed under `evidence/az/`. | (i) + (ii) |
| 32 | `AZ-ALG-ANTIPODAL-LOWORDER` | TDR-G v2.12.14 §6.2 cites it at `az-v0.6` as a static $\mathbb{Z}_N$ graph statement (no bridge; its release record rows TC-16, I12). AZ now has a consumer. | none | Entry unchanged in v0.7. At the v0.7 release, one notice to `pipes/TDRG/` that the entry is unchanged at the new tag. | (i), release step |
| 33 | `TDRG-AZ-STATIC-ZN-4Q`, `PROP-AZ-CORE-EQUIV` | AZ-owned identifiers without the `AZ` prefix; TDR-G declares no such RID (its notice and release record). Methodology v1.4 §4.2: keep existing nonstandard IDs with an explicit owner map. | none | No rename. An owner-map line belongs to the Methodology migration. | (ii) |
| 34 | Bare `[THM-ALG]` (PROP-AZ-CORE-EQUIV) | Methodology v1.4 §8 registers only `[THM-ALG via IA]`. Under the declared v1.2 the tag stays. | none in v0.7 | Resolve at the Methodology migration; not a grade change here. | (ii) |

## 4. Inbox items

Both items are notices; neither asks for anything, and each says the repin is the receiver's decision (`pipes/README.md`: the receiver decides; an item is not an adoption). Their `state` is not changed by this record.

| Item | What it tells AZ | Rows | Proposed disposition (to be entered when v0.7 is adopted) |
|---|---|---|---|
| `pipes/AZ/20261028-TDRG-v2-12-14-adopted.md` | TDR-G v2.12.14 is adopted; owner RIDs for the state definition and three lemmas; two lemma statements corrected; TDR-G §6.2 cites `AZ-ALG-ANTIPODAL-LOWORDER`; `TDRG-AZ-STATIC-ZN-4Q` stays AZ's. | 19, 20, 21, 22, 32, 33 | `accept` · pointer: the v0.7 release record. Adopted use is then AZ's §8 rows at `tdrg-v2.12.14`. |
| `pipes/AZ/20261103-DYAD-notices-n16-n21.md` | RAW-CUBIC caveat and range $p\ge3$; Appendix F crosswalk; sign of the $p=12$ value; VANISH-B2 range. | 9, 12, 14, 16 (VANISH-B2: no change needed) | `accept` · pointer: the v0.7 release record. Adopted use is then AZ's §8 rows at `dyad-v6.4.23`. |

## 5. Atlas findings (`atlas-v0.11`; noncanonical)

| Key | Finding | Checked at the owner text | Rows |
|---|---|---|---|
| AZ.A1 (H2), advisory row 1 | the ×2 sentence contradicts OPEN-M v0.7.1 R16 | confirmed | 1 |
| AZ.A2 | $q=4,(0,3)$ cascade formula listed as open; Genesis pin | confirmed | 11, 5, 29 |
| AZ.A3 | the Programme patch request is met | confirmed | 28 |
| AZ.A5 | DZT anomaly set and AZ's $4\mid q$ rule: no relation asserted | DZT v0.8 read only at SG-DZT-1 and `DZT-ALG-CASCADE-ANOMALY-SET` ($p=8\ell^a$, $\ell^a\equiv1 \bmod 4$): it names no AZ result; AZ names no DZT result; SG-AZ-7 already forbids the link | none — no action |
| AZ.A7 (H3), advisory row 3 | consumer strings that are not owner RIDs | confirmed | 14, 19, 23, 25, 26 |

## 6. The split

**(i) Corrections edition `az-v0.7` — no new science, no grade raised.** In the order of BOOTSTRAP 3:

1. Row 1 (the ×2 sentence).
2. Statement and status corrections: rows 9, 10, 11, 12, 13(a), 15, 21, 22, 24, 25, 27, 28, 31(i).
3. Repins and identifier corrections: rows 2–7, 14, 16, 17, 18, 19, 20, 23, 26, 29.
4. Inbox answers (§4) and the notice of row 32, with the release.

**(ii) New work or a separate decision — not in v0.7:**

- Methodology v1.4 migration of the file (rows 8, 33, 34).
- Recovery of the Thread C evidence (row 31(ii)).
- Restructuring proposed by Programme v1.4 §6.7 (row 13(b)): reduce duplicated owner summaries.
- AZ's own frontier (AZ-2: a dynamical, non-substrate observable; the analytic completion of the $4\mid q$ mechanism; transfer-zeta poles) — BOOTSTRAP 4, after v0.7.

## 7. Decisions asked of the PI

1. Is list (i) the scope of `az-v0.7`? Rows may be struck or moved.
2. Row 8: keep the Methodology v1.2 declaration in v0.7 (proposed), or migrate first.
3. Row 13: (a) corrected list with a pointer (proposed), or (b) pointer only.
4. Row 27: pointers to Programme v1.4 §8 (proposed), or the v1.4 texts quoted.
5. Row 31: add the availability sentence to §9 in v0.7 (proposed).
6. Who drafts v0.7 and who reviews it.

## 8. What this record does not do

It edits no DSN, changes no pipe state, adopts nothing and regrades nothing. Every proposed change is to be made in the corrections edition through the ordinary cycle (branch, PR, review, PI decision, release record, merge, tag).
