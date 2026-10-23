# RECOG v0.3.22 — outbound notices (prepared; none sent)

**Date:** 20 October 2026 · **From:** RECOG owner (Claude, co-owner; PI Mustafa)
**Edition announced:** `RTG_RELATIONAL_RECOGNITION_DSN_v0_3_22.md`, adopted 20 Oct 2026, SHA-256 `0dcce9e44d48fbedbcd5af083283fce12560cc17a3951a7632ff0e50db44bcd9` (release record `RECOG_v0_3_22_RELEASE_RECORD.md`)
**Status:** `[SESSION]` notice texts. **None has been sent.** The PI dispatches them. A notice is marked sent, or its acknowledgment recorded, only on a real dispatch or receipt event.

**Notification rule (RECOG §7.3).** v0.3.22 changes no statement, hypothesis, domain, row, constant, track or grade of any RID listed in §7.3. In particular, RECOG-THM-R9-MEMORY is unchanged: rows $(517,\tfrac1{400})$ on $\lvert z\rvert\le\tfrac1{20}$ and $(163,\tfrac1{1600})$ on $\lvert z\rvert\le\tfrac1{40}$, not mixed. The release is additive: one new cell, §6.13b, and twelve new RIDs. The notices below are therefore informational, plus two receipt confirmations.

---

## N-D (to Dyadic) — use of N13; R9 unchanged

1. **N13 use.** RECOG v0.3.22 §6.13b uses DYAD-THM-OPEN21-PRIMITIVE-PHASE-REMAINDER, pinned to adopted v6.4.18 §6.14 lines 843–850 (`f70308f1…458d`), in RECOG-THM-A1A-CD-PRIMITIVE-EXPANSION. RECOG discharges the theorem's R9 premise with its own adopted R9. The theorem keeps its owner grade and its rows A/B. The certified bound is taken only from OPEN 21.
2. **Primitive-variable form.** It is imported with your qualifier verbatim (v6.4.18 lines 806–809, `[ALG — formal second order; remainder not certified]`).
3. **Other imports.**
   - DYAD-ALG-OPEN3-PHASE-OFFSET (P4-0), DYAD-THM-OPEN3-PHASE-OFFSET-BOUNDS and DYAD-THM-OPEN3-ASYMPTOTIC-PHASE, pinned to v6.4.16.
   - DYAD-THM-PRIM-CTR and DYAD-THM-NF-INV.
   - No Dyadic domain is widened, and no Dyadic grade changes.
4. **Evidence class.** The OPEN 21 statement was source-checked independently against v6.4.18 (`941f42d6…126e`). The P5 certificate was not rerun. The v6.4.17 ↔ v6.4.18 §6.14 identity is recorded as owner-reported.
5. **Lift-alignment lemma.** The lemma your C4 session accepted, $\tfrac\pi6<\delta_T<\tfrac\pi2$ on $U_T$ with ceiling $\tfrac{143209}{750000}$, is registered as RECOG's own `[THM]` RECOG-THM-A1A-LIFT-ALIGNMENT. RECOG records your C4 position as a review acceptance, not a Dyadic adoption. No Dyadic RID is created.
6. **R9.** Unchanged (§7.3 rule). Nothing is required on your side. You may cite RECOG §6.13b if you wish.

## N-NG (to Number Genesis) — A1a-G1 closure receipt; repin pending v1.20.8

1. **Receipt.** RECOG recorded your reply v0.1.1 (`a2e7bf98…1902`; body byte-identical to v0.1 `184a74fc…5227`) and the co-owner allocation ruling. A1a-G1 is disposed as **allocation resolved; canonical repin pending NUMGEN v1.20.8**.
2. **RECOG text.**
   - Both imports, the $D_M$ definition and INF-1, keep `RID unavailable` with your interim line and the tracking keys `A1A-NG-D-DEF` and `A1A-NG-INF1`.
   - None of the six approved strings appears in RECOG v0.3.22. A release gate enforces this.
3. **After NUMGEN v1.20.8 is adopted.** RECOG will repin the two imports in a separate revision. Please notify RECOG of the adopted edition and its hash. The repin will cite `NUMGEN-DEF-N5AS1-DEFECT` and `NUMGEN-RESULT-N5AS1-INF1`, and the four chain RIDs in the INF-1 `Depends on:` line, only from that edition.
4. **What RECOG uses.**
   - INF-1 as true in two `[RESULT] [from: ALG]` results, both on $U\cap U_{\rm NUMGEN}$:
     - (a) existence of the asymptotic phase without R9;
     - (b′) $C_D^{\rm ext}=C_D$.
   - A **local extension** $D_M^U$ of your $D_M$ formula on $U=\{0<Q_0\le\tfrac1{625}\}$. It equals your $D_M$ only on the overlap. This extends a definition, not a NUMGEN theorem.
   - No NUMGEN domain or grade changes.
5. **Identification offered.** $C_D^{\rm ext}=\tau\log Q_0-M_W$ on $U$ (RECOG `[THM]`, using R9). This answers your optional Fatou/$C_D$ identification question at RECOG's grade. It is not an import into NUMGEN, and NUMGEN said it prefers at most a later provenance pointer.
6. **Scope note.** RECOG §7 now notes that `NUMGEN-THM-N5AS1-DEFECT-THRESHOLD-RATIO` covers the ratio theorem, not INF-1. This is consistent with your reply.

## N-O / N-R / N-E (to OFN, RRF, RER) — informational

- RECOG v0.3.22 is adopted (hash above). It adds §6.13b A1a: the asymptotic-phase existence route and the identification of the Number Genesis constant $C_D$.
- No RID consumed by OFN, RRF or RER changes (§7.3 rule).
- No physical event rule, token schedule or comparator-track transfer is introduced. R6 stays ACTIVE.
- **G3 status.** The G3 notices for v0.3.21 to OFN, RRF and RER are still unsent. If you send them together with this notice, record the two dispatches separately.
