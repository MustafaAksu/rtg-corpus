# Number Genesis v1.20.3 — Freeze Manifest

**Manifest ID:** `NG_V1203_FREEZE_MANIFEST_v1` · **Date:** 2026-09-28
**Ruling:** co-owner — scientific migration APPROVED; NG-9 → §6.10, N-4 → §6.5, N-6 → §6.7 APPROVED; L1 depth cap APPROVED as a Markdown rendering exception (semantic parent N-1C-DYAD unchanged); metadata-finalization APPROVED. **v1.20.3 FROZEN.** Methodology-only release; scientific state identical to v1.20.2.

## Canonical bundle
```
c3265a3a12974e300789179298a732cec579ccfad98b587755e018bcc5cfd2df  RTG_NUMBER_GENESIS_DSN_v1_20_3.md                  FROZEN OWNER (3243 lines, LF)
d310ad4957b57c1ad940c95a18081c3c8cc5456dc6f93726d1481e5311b4d4a7  RTG_NUMBER_GENESIS_DSN_v1_20_3_fingerprint_v2.json  generator v2.3
1fbeb19de86afbc6b91d45539ff22c5f81120a25bfa88336e480b29b2f323ff6  ng_state_fingerprint_v2_3.py                        GENERATOR
f05042d8defe442d9036bcb4b3d1070dce2adb4b14ec46778adccc2bddcecfc7  NG_V1203_MIGRATION_LEDGER_v1.json
f4097fb20d96d2beaff35da9d4f1d4cb54d4650c86c222f3a685a06139bfa592  NG_V1203_HIER_INVENTORY_v1.json
f9654659c05104b11543818e705d26399e836ed07c6cc91d379f37545ee0a94b  NG_V1203_REVERSE_INVENTORY_v2.json
bce7b4c11f262ad11cf3d52b9fa67a1ea5775ba0d5357afc706a2f06d7839e10  ng_migration_engine_v1.py                           (K=0 reproduces v1.20.2 byte-for-byte)
e8b6f05bdd05ab8ffd0158f9772ff5178265af5d25fa77bec989a04e100f7a24  NG_V1203_MIGRATION_REPORT_v1.md
1b2b19beee7235a92452c7362a1f3810d0da4fe013659e81607453d02b8167dd  RTG_NUMBER_GENESIS_v1_20_2_to_v1_20_3.diff
1363033200e8274b7a3f0bf4552f4fc4f504c4707df5ba94774fa8a308be71d2  NG_V1203_METADATA_PATCH.diff
5f12328553fe36c4ac0cea1bdc6c5c282f819ac625c25b5929c2cfbc0b484095  verify_v1203_freeze.py                              v1.1, banner-safe
```

## Superseded, with content preservation
`RTG_NUMBER_GENESIS_DSN_v1_20_2.md` now carries a SUPERSEDED banner (file hash `66029898d9e4b2a0dd421c80034bb30ecf3bd29b719289cfee2e51f2c4186f26`); **with the banner removed its content hashes to the frozen `35fe1a65e831b620ec1d81819cdd614f07836395870f694dcc2d91a31dde1053`**.

## Verification after freeze
`python3 verify_v1203_freeze.py` → exit 0. `[COR]` v1 of the verifier read the base file as-is; once v1.20.2 was bannered, its line numbers shifted by two and INV-S mis-assigned statuses to blocks (NOT READY). v1.1 strips the banner into a temporary copy and **proves** it equals the frozen v1.20.2 before using it. The frozen content was never affected.

## Chain
v1.20 → v1.20.1 (STOP-01) → v1.20.2 (STOP-02/03) → **v1.20.3 FROZEN** (structural migration).

## Next
1. **Consumer sync** — RECOG repin of `NUMGEN-THM-N5AS1-DEFECT-THRESHOLD-RATIO` (still pinned to v1.15); Dyadic v6.4.10 consumer row ("acceptance pending") to be closed on the Dyadic side.
2. **C7C-M2 preregistration** — interface-typed composability/descent; interface equivalence must be defined without reference to `ρ_Q`.

Pending outside this owner: Discrete Genesis P2 antipodal-endpoint policy; reproducibility-contract note (owner action).
