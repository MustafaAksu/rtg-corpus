# Atlas v0.7 — independent change-focused receiving review

**Date:** 28 October 2026  
**Status:** [SESSION] advisory review of a derived NONCANONICAL atlas; not PI acceptance or scientific adoption.  
**Object:** PR #100, branch `claude/atlas-v0-7`, head `15793e747178aef7ec30974493bdeab4ab83d311`. Candidate `atlas/RTG_STATE_ATLAS.md` SHA-256 `3655d4043e5eee046e93811d37b1fbe7bc863146dceed8b95c4e9d031ca53078` (producer manifest: 492,007 bytes, 1,545 physical lines).  
**Verdict: ACCEPT for PI consideration, scoped to these bytes and the two moved sources.** One editorial note is nonblocking. 

## 1. Provenance and reading extent

- Atlas base: `atlas-v0.6` (owner-reported SHA-256 `35ebee6d61f4db93211f2ed6f2de2bb973aa2fc6f2ea3cdf670656b1e961bd8a`). Candidate `atlas/RTG_STATE_ATLAS.md` text retrieved; targeted changed H, D3, D5, D1/D2 links and L5 entries examined. PR #100 13-file path inventory and the complete review packet §1–5 read. No owner scientific campaign replay.
- TDR-G governing `tdrg-v2.12.14` (SHA-256 `3be72923cd40523399363e0dc044bba6246862d12b2bca190c74969e2cce2392`): targeted §1, §2, §6.3/§6.5/§6.6/§6.12, §7–8 and associated statement RIDs at the tag. Atlas source lines around 1270–1315 and 1388–1397 read.
- RECOG governing `recog-v0.3.25` (SHA-256 `86cae8ff094d63d077ec5c0887451775ec3a26485cfad95833d8390bda4bd7db`): targeted §6.13a around owner lines 658–662, §6.13b around 748–761, §6.16e around 1025–1043 and §7 owner dependency rows; Atlas D3 around lines 723, 741–742, L5 around 856–857.
- Programme `programme-v1.3` and `CONVENTIONS.md` consulted for source/pin and receiver-status rules. Earlier pins left untouched.
- Build/replay evidence: `records/atlas/ATLAS_V0_7_REVIEW_PACKET.md` and producer's checker reports claim 68 exact-once operations, two byte-identical builds, 18/18 shared and 6/6 focused negative controls, zero FAIL and no dangling H→L5. **These runs and all SHA-256 hashes are producer-reported; I did not independently execute the builder, recompute the file hashes or replay certificates.** GitHub text was retrieved at advertised refs.

## 2. Answers to review packet §4

### Q1 — TDR-G orientation and five new nodes: ACCEPT

**[OWNER: TDR-G v2.12.14 §6.3 and §6.12; Atlas v0.7 candidate H9 line 52 and D5 lines 1275–1280].** The candidate correctly records `TDRG-DEF-ORIENT`: when `S=0` and `2E≡0 (mod N)` — i.e. `E=0` or the centered antipode `E=N/2` — the event is an extended balanced path-tie. The older v18 implementation's node-ID completion is **superseded as a policy**, not rewritten out of the historical evidence. The distinct `TDRG-ALG-ORIENT-NOGO` establishes only a no-go for choosing an orientation from `(S,E)` alone on this stratum; the extra center-token G-rule is an alternative recorded but **not adopted**. The fixture, finite equivariance counts and mirror-inventory-vs-step-symmetry distinction are represented at their native grades. `TDRG-ALG-LARGEST-CENTER-ID-TIEBREAK` is correctly flagged as a residual noncanonical policy problem, not an exception silently cured by SG-14.

The finite `N=24` census / owner-check evidence, the 4.9% k=1 bound and the unreplayed v18 BIND3/trajectory numbers are explicitly qualified. The candidate does **not** infer that the amended policy has re-certified the historical BIND3 campaigns. H9 and D5.X1 distinguish the TDR-G policy ruling from NUMGEN's still-pending DISC-1/2 re-annotation and C7C-M4 release decision. These are scientifically separate owner obligations.

### Q2 — 23 owner-RID node renamings: ACCEPT

**[OWNER: TDR-G v2.12.14 §§6–7].** The node heads use newly registered `TDRG-DEF-*`, `TDRG-THM-*`, `TDRG-ALG-*` and other exact owner identifiers with the legacy Atlas/navigation aliases retained in parentheses. This is preferable to treating alias names as scientific RIDs; it preserves historical searchability. In particular `TDRG-ZN-STATE` is treated as an owner-side alias of `TDRG-DEF-ZN-STATE`, rather than being invented as a second claim. OFN and AZ historical consumers are **not** automatically repinned. H4's reduction of RID gaps and D1 METH.M2/OFN.O5 linkage are correctly conditional on their own consumer changes.

### Q3 — TDRG.G1–G7 retirements: ACCEPT

**[OWNER: TDR-G v2.12.14 §§1, 2, 6, 7, 8 and release record; Atlas D5 lines 1388–1391].** Their active points are superseded by owner edits and new registered nodes: orientation resolved within owner scope; full-vs-window exponent descriptions corrected; LEM-RETRIG least-period qualification and LEM-SPECCONS one-way implication installed; the cross-branch/pin and owner-RID handoff made explicit; custody categories are visible. Keeping `TDRG.G8` as a later v2.13 layout/Methodology migration note and `TDRG.G9` as an OPEN duplication diagnostic is appropriate. New `TDRG.G10` and `TDRG.G11` track genuinely outstanding noncanonical-policy covariance and missing proof-source custody. The retired key set is not reused in live L5 heads.

### Q4 — RECOG v0.3.25 D3/H5 and R-A1: ACCEPT SCOPED

**[OWNER: RECOG v0.3.25 §§6.13a/6.13b/6.16e/7; Atlas candidate H5 line 48, D3 lines 723, 741–742, RECOG.R-A1 line 857].** The candidate keeps the previously adopted R9 ceiling rows `(517,1/400)`, `(163,1/1600)` while accurately adding the direct sharpenings `(259.2,1/400)`, `(81.49,1/1600)`. The tighter `(221.4,1/400)` and `(75.69,1/1600)` remain explicitly **conditional** on the `C₇≤85.1/27.7` ceiling assumptions, which are source-reported Dyadic certificate values, **not** adopted Dyadic theorem statements. 

The known-`a` `RECOG-THM-A1C-SHARPENED-SCHEDULE` retains the additional Dyadic (D5) proof-constant assumption. The unknown-`a`, record-only algorithm produces an **outer enclosure/window**, not identification, uniqueness, a lower bound on individual parameters or a physical memory-carrier downgrade. The `C¹` record-fiber statement restricts fibers to a single level curve; it does **not** establish A1c-Q1′ injectivity, noninjectivity or fiber connectedness. Those open qualifications are present in D3. `RECOG.R-A1` is a legitimate **derived interface diagnostic** because the absence of adopted Dyadic statement registration affects the hypothesis-status of RECOG's claims; it does not change Dyadic custody or constitute an outgoing notice. This row should remain visibly NONCANONICAL.

### Q5 — diff scope: ACCEPT; nonblocking text hygiene

The updated H4/H5/H9 and interface nodes are within the declared TDR-G/RECOG source delta. `NUMGEN.N-I1` properly distinguishes filed/open external pipe notices from receiver adoption and notes the two TDR-G inbox items closed by TDR-G; Programme's IF register and other owners' older pins remain at their own source editions. The record `NUMGEN-CAND-N5AS1-LOGSLIP` remains UNVERIFIED as a *live* RID rather than being fabricated into a PASS. Source-level scope guards and the unchanged 16 domains are not silently rewritten.

**Nonblocking editorial note:** the D3 A1b node (candidate around line 741) ends an inserted explanation with the literal suffix `( change)`. This has no mathematical effect but can be removed in a subsequent compact editorial patch, provided the adopted candidate bytes are repinned if modified before PI acceptance. No extra scientific review is needed solely for that fix.

## 3. Acceptance boundary

**[SESSION] RECEIVING VERDICT: ACCEPT**, limited to `3655d4043e5eee046e93811d37b1fbe7bc863146dceed8b95c4e9d031ca53078`. This is a review judgment, **not** scientific adoption by the PI. The newly registered owner RIDs, v18 data caveats, missing artifacts, RECOG conditions and negative/open results must survive publication unchanged.

Next: PI may accept these exact Atlas bytes (or request the nonblocking editorial fix before acceptance). The Atlas owner prepares an acceptance record; PR #100 should be merged by merge commit, then an annotated `atlas-v0.7` tag on **PR #100's merge commit**, with the Atlas SHA-256 in its tag message. The release of Atlas neither modifies nor adopts a TDR-G/RECOG theorem. PR #81/#98 tag records remain separate pending merge and should not be silently represented as done.
