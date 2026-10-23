# Atlas v0.2 build scripts

Edit scripts used by the atlas owner to build atlas v0.2 from v0.1 (`main` `44b55d6`), in this order:
`d2.py` (DYAD slice, 42 operations) → `rer.py` (RER nodes, 18 operations) → `l5.py` (L5 dispositions) → `pass.py` (PASS lists → `*ATLAS:checked-Dk`) → `wording.py` (process wording, two L3 lines) → `av02.py` (receiving-review corrections AV02-02–04).
A few single edits made after `wording.py` (RER key spelling, CROSS-DOMAIN index lines, source-table RER row, five wording fixes) are in the branch history.

`lib.py` is the edit helper: every operation asserts that its anchor occurs exactly once. Paths inside the scripts point to the atlas owner's session scratchpad; they are kept as a record of the operations, not as a rerunnable pipeline. `l5.py` and `pass.py` also wrote the disposition list behind `records/atlas/ATLAS_V0_2_L5_DISPOSITIONS.md`.
