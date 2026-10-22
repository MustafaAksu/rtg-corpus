# rtg-corpus

The working corpus of **RTG — Relational Time Geometry**: the canonical study ledgers (DSNs), their release records and evidence, and the cross-stream State Atlas.

Principal investigator: Mustafa Aksu. Collaborators: Claude, ChatGPT, Gemini, Grok (AI-Lab).
Earlier archive: Zenodo DOI 10.5281/zenodo.17568897.

## Layout

| Path | Content |
|---|---|
| `dsn/` | Current canonical DSNs and the DSN Methodology. **One file per study, fixed filename, no version number in the name.** The version is in the file header and in the git tag. |
| `noncanonical/` | Adopted or working registries and studies that are explicitly noncanonical (RER, ER-2B, FMS). Same fixed-name rule. |
| `records/<study>/` | Release records, advisory/disposition/closeout notes, notices. |
| `evidence/<study>/<version>/` | Release packages: scripts, logs, diffs, checksums. |
| `atlas/` | RTG State Atlas (AI-oriented relational map of all DSNs) and its method. |
| `tools/` | Lint and release/compaction checkers. |
| `BASELINE.md` | Which files are in the repository, their verified hashes, and which are still pending. |

## How history works here

- Each adopted DSN release is a commit on `main` and an annotated tag `<study>-v<version>`, e.g. `dyad-v6.4.20`.
- Earlier versions are retrieved from git, e.g. `git show dyad-v6.4.19:dsn/RTG_DYADIC_OSCILLATOR_DSN.md`. The live file therefore carries current state only; it does not need inline history or long *Supersedes* lists.
- Files are stored byte-exact (`.gitattributes`: `* -text`), so a file's SHA-256 in this repository equals the SHA-256 recorded in its release record.
- A file enters the repository only after its SHA-256 has been checked against an owner record, or it is marked otherwise in `BASELINE.md`.

## Status labels

Documents keep their own DSN status (DRAFT, ADOPTED, …). Working notes are marked SESSION / NONCANONICAL in their headers. Presence in this repository is not adoption.

See `CONVENTIONS.md` for commit, tag and review rules.
