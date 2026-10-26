# Number Genesis v1.20.7 — Freeze Manifest

**Manifest ID:** `NG_V1207_FREEZE_MANIFEST_v1` · **Date:** 2026-10-01
**Ruling:** co-owner — **v1.20.7 FROZEN.** Class: owner synchronization + scoped algebra adoption + governance repair.

## Authoritative quartet
```
c4637e7a5cfaf8eaf001746f172111385f5df2a8cd552e3ab56308ff7abfab28  RTG_NUMBER_GENESIS_DSN_v1_20_7.md                  FROZEN OWNER (3355 lines, LF)
0aa91fa4c5243af6fd99c00ca10211fe13c48a3e17db907c74ee0b70fc528f26  RTG_NUMBER_GENESIS_v1_20_6_to_v1_20_7.diff          applies to the v1.20.6 payload and reproduces the owner byte-for-byte
0fa3d95c7c5401314fa25fbf555dbc9185e3cc83fab21369e6b525b4feafd490  RTG_NUMBER_GENESIS_DSN_v1_20_7_fingerprint_v2.json  generator v2.3 (1fbeb19d…3ff6); 521 blocks, dup 0/0
d645cce8392157ebaaa54aca2ac142bcbc8aa87bd0d1b46edcf7a9ed69db2cea  NG_V1207_REMAINING_GRADE_RULINGS_v1.md              co-owner grade rulings (B2, B5, B8–B11, DI) with itemized exactness statement
```

## Predecessor payload and supersession banner
- **Frozen v1.20.6 payload (canonical, banner-stripped):** `2a51c4b1a8037105d75e68ea7f24c721a970ab5ec32c27e810139020ccb948c5`
- **Raw file `RTG_NUMBER_GENESIS_DSN_v1_20_6.md` after the banner:** `65798c9c1ca232598c5b08e6b7b2f6eb9f3c82fdfe3d193acea009630d58a9af`
- **Deterministic banner-removal procedure.** If the raw bytes begin with `> **[SUPERSEDED`, the payload is everything after the **first** occurrence of the two-byte sequence `\n\n`; otherwise the payload is the raw bytes. The banner is a single line containing no `\n\n` other than its terminator.
  ```python
  raw = open("RTG_NUMBER_GENESIS_DSN_v1_20_6.md", "rb").read()
  payload = raw.split(b"\n\n", 1)[1] if raw.startswith(b"> **[SUPERSEDED") else raw
  # sha256(payload) == 2a51c4b1…48c5
  ```
  Executed after the banner was applied: the stripped bytes equal the original v1.20.6 bytes, with SHA-256 `2a51c4b1…48c5`.
- The banner was applied only after the successor's hash was verified as `c4637e7a…fab28`. The v1.20.3 freeze verifier (v1.2, which strips banners by the same rule) still returns FREEZE CONDITIONS MET.

## Verified at freeze (independently reproduced by the co-owner)
- The diff applied to the `2a51c4b1…48c5` payload reproduces `c4637e7a…fab28` byte-for-byte.
- Relative to the superseded intermediate candidate `ad54fcef…c5815`, the only owner change is the changelog §6 exactness sentence; the claim-block set, explicit RIDs and broad identifiers are identical.
- 29 status lines identical to v1.20.6; v1.20.6-and-earlier changelog byte-identical.
- **0 live bare RESULT; 0 live combined truth-status tags**; explicit RIDs conserved; INV-LIVE PASS.

## Scientific state at v1.20.7
- **C7C-M2 Census-1 = INCONCLUSIVE / INCONCLUSIVE.** No admitted nondegenerate composable source chain in Census-1 evidence; neither PASS nor FAIL of WD-DOM.
- **M2-1** (transported chain identity) adopted at ALG grade with a no-closure guard. **Full-interface typed WD-DOM remains OPEN.**
- **Missing evidence object:** a certified composable three-stream witness `(A,B) ∈ R_bd`, `(B,C) ∈ R_bd`, `(A,C) ∈ R_pair` in one certified comparison architecture. No search is authorized.
- **M-4 realization search remains HOLD** pending the Discrete-owner P2 ruling.
- **RF-06 scope note** recorded; the source-side correction belongs to Discrete Genesis.
- **Methodology normalization debt addressed** in the live owner.

## C7C-M2 provenance (pinned in the owner's §9.2)
Preregistration `248f128c…8987` + freeze manifest `cefb7180…b165b` · Census Protocol v1 `f2a4a9a4…5795` · Census-1 results `ed3c72af…eae9` (dyad), `23f298dc…d33a` (TDR-G) · replay `73cfa2e3…8188` / `19e929aa…a30a` / `7b7dc451…77c8` · opening manifest `d170efb5…5d73` · analysis log `e7b85fd2…0139` (E0–E6) · E4 density `c67342a9…6fa8` · RF-06 self-check `b39de45c…ded4` + `2a064eb9…f148`.

## Chain
v1.20 → v1.20.1 → v1.20.2 → v1.20.3 (structural migration) → v1.20.4 → v1.20.5 (consumer sync) → v1.20.6 (grade normalization) → **v1.20.7 FROZEN** (C7C-M2 sync, M2-1, RF-06, normalization complete).
