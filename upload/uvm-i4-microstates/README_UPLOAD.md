# upload/uvm-i4-microstates — OPEN-M-2D/2E microstate packs (I-4)

**Supplied by:** the PI as chat attachments in the UVM co-owner session on 23 November 2026, in reply to the I-4 request of `records/uvm/UVM_S0_CUSTODY_AUDIT.md` §6. Batch 1 (16:47 +03:00): the seven microstates listed first in the table. Batch 2 (17:05 +03:00): the eight `T80_to_T100_gentle` files. Batch 3 (22:23 +03:00): nine files for T80 `mid40_to_T80_minref`, T93 `T80_to_T93_2e_loadtest`, T120 `v13_loose_T80_to_T120`, and the `T98_to_T100_2e_ultra` audit pack.
**Placed by:** Claude (UVM co-owner). The bytes are unchanged. The only change is the file name: the chat upload added an 8-hex prefix and a hyphen (batch 1: `b25e7537-`, `41fa0eed-`, `de41f640-`, `74029318-`, `5bc2a8fb-`, `fbdf47d0-`, `77677474-`; batch 2: `4cec7cab-`, `20bf6f47-`, `f807730d-`, `c44058b5-`, `dac81cc7-`, `6da6a909-`, `779ad301-`, `75ac9023-`; batch 3: `d9b4f2e4-`, `1c1618a8-`, `209cd160-`, `1cae0ea7-`, `1f3d72a4-`, `2dd8c47c-`, `667325b3-`, `bb67d3ac-`, `e80972e6-`), which was removed. Each file was compared byte for byte with its attachment (`cmp`); all twenty-four are identical. `…BEST_RAW.json` and `…BEST_PEN.json` are byte-identical to each other, as supplied.
**Hashes:** `SHA256SUMS.txt`. No earlier record in the corpus gives a hash for these packs, so they can be checked for integrity only, not against a recorded identity.
**Arrays:** every microstate and the audit pack carry two object arrays, `z_convention` and `r_em_formula`, which need `allow_pickle=True`. Their pickle streams (all batches) were disassembled with `pickletools`, without executing them: they reference only `numpy.core.multiarray._reconstruct`, `numpy.ndarray` and `numpy.dtype`, and hold the two convention strings. The I-4 diagnostic loads the packs with `allow_pickle=False`. The original `open_m_2e_panel.py` loads with `allow_pickle=True`; it was run only after this check.

| File | Stage in `open_m_2f_trajectory.py` `SERIES` |
|---|---|
| `…T80_to_T89_2e_loadtest_microstate.npz` | T89 |
| `…T80_to_T90_2e_loadtest_microstate.npz` | T90 |
| `…T80_to_T91_2e_loadtest_microstate.npz` | T91 |
| `…T80_to_T92_2e_loadtest_microstate.npz` | T92 |
| `…T80_to_T94_2e_loadtest_microstate.npz` | T94 |
| `…T93_to_T102_2e_microstate.npz` | not in `SERIES` |
| `…T98_to_T100_2e_ultra_microstate.npz` | not in `SERIES` (its T100 stub is `…T80_to_T100_gentle`) |
| `…T80_to_T100_gentle_microstate.npz` | T100 |
| `…T80_to_T100_gentle_auditpack.npz` / `.json` | T100 audit pack (input of `open_m_2e_panel.py`) |
| `…T80_to_T100_gentle_grown_manifest.json`, `…_growth_log.csv` | T100 run manifest and growth log |
| `grown_cluster_v13_rank2_T80_to_T100_gentle.json`, `…_BEST_RAW.json`, `…_BEST_PEN.json` | T100 cluster output (named as `output_json` in the manifest) |
| `…mid40_to_T80_minref_microstate.npz`; `…_auditpack.npz` / `.json`; `…_growth_log.csv` | T80 |
| `…T80_to_T93_2e_loadtest_microstate.npz`; `…_auditpack.json`; `…_growth_log.csv` | T93 (audit pack as json only) |
| `…v13_loose_T80_to_T120_microstate.npz` | T120 |
| `…T98_to_T100_2e_ultra_auditpack.npz` | audit pack of the `ultra` microstate (not in `SERIES`) |

With batch 3, all nine `SERIES` microstates are present.

Not supplied: audit packs (npz) for T89–T94, T93 and T120, and for `T93_to_T102_2e`. These are not needed for I-4.
