# upload/uvm-i4-microstates — OPEN-M-2D/2E microstate packs (I-4)

**Supplied by:** the PI, as seven chat attachments in the UVM co-owner session, 23 November 2026 (16:47 +03:00), in reply to the I-4 request of `records/uvm/UVM_S0_CUSTODY_AUDIT.md` §6.
**Placed by:** Claude (UVM co-owner). The bytes are unchanged. The only change is the file name: the chat upload added an 8-hex prefix and a hyphen (`b25e7537-`, `41fa0eed-`, `de41f640-`, `74029318-`, `5bc2a8fb-`, `fbdf47d0-`, `77677474-`), which was removed. Each file was compared byte for byte with its attachment (`cmp`); all seven are identical.
**Hashes:** `SHA256SUMS.txt`. No earlier record in the corpus gives a hash for these packs, so they can be checked for integrity only, not against a recorded identity.
**Arrays:** each pack has 41 arrays. Two are object arrays (`z_convention`, `r_em_formula`) and need `allow_pickle=True`. The I-4 diagnostic does not read them and loads the packs with `allow_pickle=False`.

| File | Stage in `open_m_2f_trajectory.py` `SERIES` |
|---|---|
| `…T80_to_T89_2e_loadtest_microstate.npz` | T89 |
| `…T80_to_T90_2e_loadtest_microstate.npz` | T90 |
| `…T80_to_T91_2e_loadtest_microstate.npz` | T91 |
| `…T80_to_T92_2e_loadtest_microstate.npz` | T92 |
| `…T80_to_T94_2e_loadtest_microstate.npz` | T94 |
| `…T93_to_T102_2e_microstate.npz` | not in `SERIES` |
| `…T98_to_T100_2e_ultra_microstate.npz` | not in `SERIES` (its T100 stub is `…T80_to_T100_gentle`) |

Not supplied:
- the `SERIES` stubs `…mid40_to_T80_minref` (T80), `…T80_to_T93_2e_loadtest` (T93), `…T80_to_T100_gentle` (T100) and `…v13_loose_T80_to_T120` (T120);
- any audit pack with `internal_edges` for `open_m_2e_panel.py`.
