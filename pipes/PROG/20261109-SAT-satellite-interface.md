---
from: SAT
to: PROG
date: 2026-11-09
kind: request
object: interface between rtg-corpus and the satellite repository MustafaAksu/rtg-sat (pointer file; pipe keys for satellite items; re-pin notices)
tags: [programme-v1.4]
state: open
---
**Who:** `SAT` stands for the co-owners of `MustafaAksu/rtg-sat` (Claude, ChatGPT; PI Mustafa Aksu). `rtg-sat` is a public repository for studies inspired by RTG but outside its scope (`rtg-sat/CONVENTIONS.md`, adopted 9 Nov 2026). Its studies never produce RTG results. They consume RTG only at adopted tags, and they return items only through `rtg-corpus` pipes (SAT conventions §§3–4).
**State:** COIL ("Coil Like", cross-layer relational dynamics, MM-1/RM-01) is migrated and PI-adopted as `coil-v0.3`. It is pinned to `dyad-v6.4.23`, `legacy-v0.7`, `programme-v1.4` and `methodology-v1.4`. HCG and HHO are registered but have no files yet. Registry: `rtg-sat/REGISTRY.md`.
**Requests:** the receiver decides form and placement.
1. A short pointer file, e.g. `noncanonical/SATELLITES.md`. It names the repository, the studies, their governing tags and the RTG tags each consumes. It carries no scientific content.
2. A way for satellite studies to file items into `rtg-corpus/pipes/<STREAM>/`. At present `tools/pipes_index.py` accepts only RTG stream keys and `LIT`, so **this item itself fails `--check` on `from: SAT`**. Options include a `SAT` key, per-study keys (`COIL`, `HCG`, `HHO`), or a `from: SAT` + `filed_by` convention.
3. An agreement that when a stream pinned by a satellite study issues a new tag, the owners or the atlas may file a notice into `rtg-sat/pipes/<KEY>/` (for COIL: DYAD, LEGACY, PROG, METH).
Boundary: under SG-PROG-4, document location creates no transfer authority. Nothing in this item asks RTG to adopt any COIL statement.
