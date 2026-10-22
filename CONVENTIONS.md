# Conventions

1. **Language:** English for all documentation (DSN Methodology §0.7).
2. **Byte fidelity:** never let an editor or git convert line endings. Check the SHA-256 against the release record before committing a DSN.
3. **One commit per release.** A DSN release commit contains the new DSN, its release record (`records/<study>/`) and its evidence package (`evidence/<study>/<version>/`). Commit message: `<study> v<version>: <status> — <one-line summary>`.
4. **Tags:** annotated tag `<study>-v<version>` on the release commit. Tag message: adopted hash and adoption reference.
5. **Drafts and reviews** go through pull requests. Merge plus tag records PI/owner adoption; the release record still states the adoption decision explicitly.
6. **Study keys:** `dyad`, `triad`, `gen`, `tdrg`, `recog`, `dzt`, `az`, `uvm`, `numgen`, `ofn`, `rrf`, `rer`, `er2b`, `fms`, `programme`, `methodology`, `legacy`, `prelegacy`, `atlas`.
7. **History:** history lives in git (commits, tags). Do not keep superseded text in live sections (Methodology v1.4 draft, S1).
