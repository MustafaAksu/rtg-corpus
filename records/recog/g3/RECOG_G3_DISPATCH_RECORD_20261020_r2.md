# RECOG G3 — Outbound Notice Dispatch Record (r2)

**r2 (20 Oct 2026):** this revision fills the G3-DYAD row of §3 and adds §4. §§1–2 are unchanged from r1 (`7c7dcafb…8b4e`).

**Date:** 20 October 2026
**Status:** `[SESSION]` governance record. G3-DYAD is sent and acknowledged. G3-RER, G3-OFN and G3-RRF are final for dispatch and **not yet sent**. Nothing in any receiving stream's document has been modified.
**Source edition cited by every notice:** adopted RECOG v0.3.21, `RTG_RELATIONAL_RECOGNITION_DSN_v0_3_21.md`, SHA-256 `a3459522c8f58204f83f5e65e3d1a99912f9651d1c17cc4fb0c090196f670ae3`. Its release record is `RECOG_v0_3_21_RELEASE_RECORD.md` (`4b7aefeeaf5803d85e904dee246924f8f48f106a677078c167c2189a9573ef72`).

## 1. Identity chain

The contributor drafted the four notices on 20 October 2026. The RECOG co-owner (Claude) checked each claim against the owner files and applied corrections with `finalize_recog_g3_notices.py` (`d52c17563e7e6db8b14593d5b7e859be94bded6b32ac738976363c6ff02ec149`). The script makes exact-once replacements and appends an "Owner corrections" list to each notice.

| Recipient | Contributor draft (SHA-256) | Final for dispatch (SHA-256) |
|---|---|---|
| Dyadic | `4e96d0d9d6b3a9d134f681bfae080b267d67d9bbb64841f561bd64789765aed1` | `RECOG_G3_NOTICE_TO_DYADIC_20261020.md` `e42a5ca9d2ebf8abb9d70534b0d0ced3a08a54b4254de2817391bffd313fb821` |
| RER | `8b8a229fac008d9778136e6e7142cefb58eeadfb1ccdbc10572dbb7a85c23baa` | `RECOG_G3_NOTICE_TO_RER_20261020.md` `53341b9a85d9073d7ec22a2ef280b4fe206fbc5f7597256362fa5b880ca414b5` |
| OFN | `64afb1ba730313f0778838befad7b6092ce7d98637e33eb868c17c0f76957591` | `RECOG_G3_NOTICE_TO_OFN_20261020.md` `fc05d13b6e47b5be1084d97812a81beb73f861405487f36b39a7fd23ba8fe0a5` |
| RRF | `6b321dee81a01bead7e17d8a58942d11e6fc2864690bb79293043fd107954e64` | `RECOG_G3_NOTICE_TO_RRF_20261020.md` `65312e4b549e92592fb97edf5bf8110ffec62733adb7b23748dc65d9eb80e10f` |

## 2. What the owner check found

**Confirmed in the owner files:**
- RER r4.6 G9 still labels RECOG v0.3.20 a freeze candidate and pins §6.6a at lines 517–542 and §6.16g at lines 1002–1042. RECOG's measurement reproduces both ranges.
- In v0.3.21 the two sections are at lines 521–546 and 1006–1046, and their text is byte-identical to v0.3.20. §6.13a is also identical (lines 690–710 → 694–714).
- OFN v0.10 REQ-O09-02 asks for the final freeze record and the exact source hash.
- RRF v0.8.3 cites RECOG v0.3.14 in §§0.1, 4.1, 4.1a, 4.2 and 4.3.
- Dyadic v6.4.18 still carries three "freeze candidate" lines for RECOG.
- The RIDs and sections cited in the notices match v0.3.21. These are R9 in §6.13a, the B-token transport and S_h shadow in §6.16b, orientation conjugacy in §6.6a, and F4 well-posedness in §6.16g.
- The W3 wording quoted in the notices matches the RECOG text.

**Corrected in the finals:**
1. **G1 record hash.** No draft gave the G1 record's hash. All four finals now do, so OFN can close REQ-O09-02 from the notice itself.
2. **Dyadic v6.4.18.** The Dyadic draft predates v6.4.18, which was adopted 20 Oct 2026 with hash `f70308f1…458d`.
   - The final names v6.4.18 and records its change summary as owner-reported; RECOG has not claim-audited it.
   - It asks the owner to confirm that the RECOG-consumed passages are unchanged.
   - It records N14 as seen only, since N14 is addressed to FMS, RRF and OFN.
3. **RER's own W3 wording.** RER G9's [DEF] line paraphrases W3 as "a shared pre/post comparison space", which is close to RRF's RF-1 reading. The final asks RER to quote the same-space W3 verbatim, with W1's fixed-graph requirement.
4. **RRF live pins.** The draft missed two live v0.3.20 pins: the freeze-candidate provenance in §4.2a and the v0.3.20 pins in §6.3. The RF-1 candidate map now uses RECOG's $H^1(G;F)$ notation and notes that distinct pre- and post-birth graphs would depart from W1 as well as W3.
5. **Locations.** The OFN and Dyadic stale lines are now named by section.

**Unchanged from the drafts:**
- the three-state receipts, with N13 a conditional receipt only;
- the SG-R14 rows ($K_0=1101/1000$ on $|z|\le1/20$ and $533/500$ on $|z|\le1/40$, not mixed);
- the statement that nothing is said about $C_W^{(h)}$;
- OPEN-OFN-OPA ACTIVE and R6 ACTIVE;
- RRF's OPEN-B → E1 → E2 lock;
- every request for acknowledgment.

## 3. Dispatch and acknowledgment log (for the PI)

| Notice | Sent (date, channel) | File hash sent | Acknowledged (date, edition/record) | Outcome |
|---|---|---|---|---|
| G3-DYAD | 20 Oct 2026, by the PI to the Dyadic owner (the reply states "Sent by the PI") | `e42a5ca9…b821` | 20 Oct 2026, `DYAD_REPLY_TO_RECOG_G3_v0_1.md` (project `claude/`; reply text read, file hash not measured) | answered in full (§4) |
| G3-RER | | `53341b9a…b4b5` | | |
| G3-OFN | | `fc05d13b…e0a5` | | |
| G3-RRF | | `65312e4b…0e10f` | | |

A notice is **sent** only when this log records it. It is **acknowledged** only when the receiving owner's record or edition is cited here. An acknowledgment does not mean the receiving stream has made any change, and it is not a RECOG decision to use N13.

## 4. G3-DYAD outcome (Dyadic reply of 20 Oct 2026)

- **Release verification.** Dyadic reports reviewer `RELEASE VERIFICATION PASSED — ADOPTED` for each edition, with the reviewer report hashes:
  - v6.4.17 (`e07cf2b9…4bfc`), report `c0ef4446bdb2474d81cf6c218b8971a229ce82d7195273c11d2d00dc18611e39`;
  - v6.4.18 (`f70308f1…458d`), report `473b6aaa5e1b96c4cc0eee539b3313ffc1860a08c57a60dbeba8af191762db27`.
  - RECOG has not seen these reports; the identities are owner-reported. RECOG v0.3.21 §7.2 still says "pending" for v6.4.17. The N13 row's verification column can be updated in the next RECOG revision. Whether RECOG uses the N13 theorem stays a separate decision.
- **v6.4.17 → v6.4.18 compatibility.** The owner reports byte-identical passages for §6.9, §6.11, §6.14, the OPEN 12 block and §7 (up to the outbound notices), and that every §1 import line is retained.
  - RECOG independently reproduced all five passage-hash prefixes on its local v6.4.17 copy (`825685f2b9f1`, `a89d2f021062`, `a611ab681837`, `896ac89489ff`, `c3fa5de13ca7`).
  - The v6.4.18 side is owner-checked only. RECOG has not hashed v6.4.18 bytes.
  - The 18 RECOG-consumed imports are therefore unchanged on the owner's check, with the v6.4.17 side independently reproduced.
- **Receipts in Dyadic:** N10, N11 (reference-only use in SG-R14) and N12 RECEIVED; N13 RECEIVED conditionally.
- **Stale "freeze candidate" lines:** to be corrected in the next Dyadic revision. Adopted v6.4.18 is not edited.
