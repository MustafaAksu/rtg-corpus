# RER Phase A r5 — Independent receiving review

Date: 2026-10-19. Status: NONCANONICAL RECEIVING REVIEW. No adoption, freeze, publication, or record-level Phase B disposition.

## Package and executed checks

- Package SHA-256: `2cb24cc87e480624ecad854c755b9d6c4b25613ac5fa384e98a5cb5fbe9ee9ad` (receiver-computed, matches stated identity).
- Unpacked into a distinct working directory. `SHA256SUMS.txt`: **44/44 hashes match**.
- `python check_phaseA.py --tamper` freshly executed: **21/21 positive gates PASS**, **21/21 negative controls rejected**, exit 0. A2 rebuild compares regenerated outputs byte-exactly against delivered outputs.
- RER Markdown source SHA-256 `2fa878ffa32c0d4d725f53f17b86b9a43d5161f16a7adce9686cb374063a4772`; no scientific record edits.
- Matrix 89 rows: 23 VERIFIED, 6 OWNER_REPORTED, 53 HISTORICAL, 7 BLOCKED. Twenty records remain PENDING; ER-2B remains blocked. 13 gap paths non-null, editor response received, line-by-line reference audit remains distinct.

## Currency and provenance decision

- A19 is a frozen known-versions test, not live release discovery. The OFN record states v0.10 CURRENT, v0.9 SUPERSEDED. A21 correctly prevents the preparer from asserting byte authentication for v0.10, which was absent in the submitted package.
- **Supplemental receiving-side independent authentication (not included in the preparer's package):** local `/mnt/data/RTG_ONTOLOGICAL_FOUNDATIONS_v0_10.md` was hashed directly, SHA-256 `acb70a8cfc7962abcc047dedffb59e9ceca8f2e9843d6203df6eba54f5ed5dfa`. Thus the receiving side can separately issue RECEIVER_BYTE_VERIFIED, but must not retroactively rewrite the preparer's OWNER_REPORTED provenance.
- Independent section comparison against local OFN v0.9: §8 is byte-identical, shifted from lines 541–557 to 651–667. §12.4's substantive text is unchanged, shifted from lines 1186–1205 to 1394–1410; the end-of-section separator/next Appendix anchor accounts for differing whole-section hashes. Historical v0.9 pins remain valid; repin would be separate maintenance.
- The current OFN v0.10 §11.4 includes IMP-O10-01/02 to Genesis v2.8.9 §6.3c. Their relevance to RER-GEN-K3-MODAL and G6 remains Phase B-01 work.

## Disposition

**ACCEPT SCOPED — Phase A r5 mechanical/integrity and OFN currency update.** The phase-A machine deliverables are satisfactory at the documented snapshot and custody scopes. Phase B scientific dispositions, ER-2B original source/certificate custody, G6 and Stage-2 global certification remain OPEN. The RER source remains DRAFT r4.6, with no RER adoption, freeze or publication. RECOG v0.3.20 remains a freeze candidate (not adopted).
