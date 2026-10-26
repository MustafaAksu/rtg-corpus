# RTG State Atlas v0.6 — acceptance record

**Status:** DRAFT — receiving review ACCEPT (26 October 2026); PI acceptance, merge and tag pending (§3 to be completed by the atlas owner after the tag). `atlas-v0.5` governs until then.
**Object:** derived NONCANONICAL Atlas; acceptance adopts no owner science.

## 1. Candidate identities

| Object | SHA-256 |
|---|---|
| `atlas/RTG_STATE_ATLAS.md` (candidate, PR #79 head `5ebe99ab84a6dda2386e49fdaae4f0fbcf355af6`) | `35ebee6d61f4db93211f2ed6f2de2bb973aa2fc6f2ea3cdf670656b1e961bd8a` (479,995 bytes, 1,544 lines) |
| `atlas/RTG_STATE_ATLAS_METHOD.md` (unchanged, v0.2) | `fbd2efb34cae6f291d1881cf79f6c521ea337c8a513d92b7d42deb889ed42c04` |
| `evidence/atlas/v0.6/source_manifest.json` | `c4ce6967a34802c780139e08df9653883c6635d16cec399e1c62c947fded17eb` |
| `tools/atlas_check.py` (unchanged) | `0db3a23b9cb78bc87f4b9393baf417c7329421f719f7acbaec2f4ca36626004d` |
| `evidence/atlas/build/refresh_v0_6.py` | `b8cbe56068e81bbfe31fb5ff4a5969af042faffebc5ca5791159d5a321a1ab48` |

## 2. Basis and limits

Method v0.2; `records/atlas/ATLAS_V0_6_REVIEW_PACKET.md`; verification files under `evidence/atlas/v0.6/`. Source snapshot `38ed5bb1fb7324d939007981f6671d2ac18e8070` (after PR #78); the only moved source is Number Genesis v1.21 (`numgen-v1.21`, file `4805760d…5701`, tag verified 26 Oct). Impact refresh of one domain; no other domain re-extracted; no certificate replay; the five new RIDs checked for presence in the tagged source only. Carried checker results unchanged by text from v0.5: 4 link + 3 artifact UNVERIFIED, 11 DOCUMENTED-UNRESOLVED, 16 wording warnings; one new link UNVERIFIED (`NUMGEN-CAND-N5AS1-LOGSLIP`, registration line at tag `numgen-v1.20.8`; documented at NUMGEN.N-T1, not to be forced to PASS).

## 3. Decision

- Receiving review: ChatGPT, 26 Oct 2026, `records/atlas/ATLAS_V0_6_RECEIVING_REVIEW.md` (PR #80, branch `chatgpt/atlas-v0.6-review`, head `f2cdb02`, file SHA-256 `3bc06b4c…`): **ACCEPT** on the exact candidate `35ebee6d…bd8a` (PR #79 comment `6426506117`): row-A import as a separate THM without upgrading the native L-PHASE; RECOG A1a/A1b as independent agreement only; domain aliases with no inclusion; five exact owner RIDs; seven L5 retirements and `NUMGEN.N-I1` accurate; the LOGSLIP UNVERIFIED declared and non-blocking. The receiving review did not independently rerun the build or owner certificates.
- PI acceptance: *(to be filled: date, wording; the accepted bytes are `35ebee6d61f4db93211f2ed6f2de2bb973aa2fc6f2ea3cdf670656b1e961bd8a`)*.
- Merge: *(to be filled: PR #79 merge commit, merge method `merge`; PR #80 merged separately)*.
- Tag: *(to be filled: annotated `atlas-v0.6` on the PR #79 merge commit, message naming the Atlas SHA-256; verified by the atlas owner — tag type, target, file hash at the tag and on `main`, reachability of the candidate and review commits)*.
- Next: TDR-G advisory (two independent passes: atlas owner, then ChatGPT blind; reconciliation; TDR-G co-owner dispositions), centred on the orientation policy at S=0, |E|=N/2 (`pipes/TDRG/20261026-NUMGEN-orientation-policy-s0-e-half-n.md`) and the DISC witness scope; Programme next edition carries E-P13-1/E-P13-2 (PROG.G8); OFN/FMS/ER-2B class-C wording (H1).
