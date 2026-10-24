# DYAD LH2012 external receiving review — hash-checked placement receipt

**Date:** 24 October 2026
**Class/status:** SESSION / archive provenance only; not a scientific adoption, owner DSN amendment, release, certificate or notice.
**Governing baseline:** DYAD v6.4.22 (tag `dyad-v6.4.22`); Methodology v1.4 and repository-root CONVENTIONS.md.
**Source custody:** Original, unchanged external files imported via `upload/dyad-lh2012-review`, PR #20, intake commit `c5e4427dc6f89f65d32dec32679f01170eca6fda`. The first commit preserves the flat `incoming/dyad-lh2012-review/` originals in Git history. This follow-up placement reuses those exact Git blob IDs; no evidence content has been rewritten.

## Input identity and byte-exact placement

All seven payload entries in the original `SHA256SUMS.txt` were independently hash-checked against the bytes read from the intake branch (7/7 PASS). The original manifest is itself unchanged; SHA-256 `1e35e8c31206ac9a72b696aa485fa382ca484b5c2fba788539aa84bbe1153873`. Its original relative filenames describe the **flat intake** and are archival references, not paths at the new locations.

| Original filename | Placed repository path | SHA-256 | Git blob SHA-1 |
|---|---|---|---|
| `DYAD_LH2012_SUMMABILITY_REVIEW.md` | `records/dyad/DYAD_LH2012_SUMMABILITY_REVIEW.md` | `e5b815eacdcf99706bd6d3f28c2f2240223bb929cae9ba2eeab7cf822bd18d9f` | `2a627ab4a827a6fdeab73b37f037aa0a10deb2d2` |
| `check_lh2012_dyad_transfer.py` | `evidence/dyad/scripts/check_lh2012_dyad_transfer.py` | `71bf1c70cc637eba08823998d380cb85ba76a5d8776138dc4605c0defa79853d` | `350498fc820fa0f2b61c820924fada7c63d2af77` |
| `transfer_checks.json` | `evidence/dyad/open20-an/lh2012-external-review/transfer_checks.json` | `f2432d19cc833e15a52f7574c63c8a7285c6d178f08410807529f9c57e8fb85a` | `99f758944315195770aa505931da083eae033159` |
| `negative_branch.json` | `evidence/dyad/open20-an/lh2012-external-review/negative_branch.json` | `4028fb5e0aef15d371284f185bce1cd70e62aa7857a2088699078cfcc444ebf7` | `ae12027cf7acc3cf12ce15f27785de4439da657d` |
| `negative_coefficient.json` | `evidence/dyad/open20-an/lh2012-external-review/negative_coefficient.json` | `0b096f88b065b1c50e25730831a7a5f7b8271f400b89f7bcb7c018a4a4fa2ae9` | `02da0932ba9542929a5a0dd78c47b0b1159958a5` |
| `negative_controls.json` | `evidence/dyad/open20-an/lh2012-external-review/negative_controls.json` | `d6988c3d8ae5343009ad8e67947cc8f63b0d45dff3ad5b254a811ce20cba5fda` | `45ac17019ed7668bfb6347e86cad3fef77cf50fd` |
| `negative_ratio.json` | `evidence/dyad/open20-an/lh2012-external-review/negative_ratio.json` | `5af0cc538a52aacf6c41551ecc5779cb7c9d9f7d0788f06699a4dbf2fdf2e5b9` | `5cea6768d39ba09090fd9e7060393cdda5e2707a` |
| `SHA256SUMS.txt` | `evidence/dyad/open20-an/lh2012-external-review/ORIGINAL_SHA256SUMS.txt` | `1e35e8c31206ac9a72b696aa485fa382ca484b5c2fba788539aa84bbe1153873` | `473304aa80ca123e3b21c2ce846ab6f7e158713f` |

**Evidence states of this placement:** EV-BYTES and EV-HASH for the seven payload files and original manifest; repository blob-identity check; EV-NOT-RERUN for the scientific script. Prior owner/reviewer execution receipts are in PR #21's working records; same-engine replay is not independent theorem proof. All scientific interpretations remain SESSION-only.

**Exclusions:** The copyrighted López-Hernanz (2012) article, its private transcription (SHA-256 `9aa1ffa88ab87a92c5d77e0a672f409eaca17ee696dbb0f17cb605629d622978`) and unavailable original Turkish cover (reported `ef7fbc12…915b`) are **not** included or reconstructed.

**Dependency and release boundary:** This placement neither changes `dsn/RTG_DYADIC_OSCILLATOR_DSN.md` nor creates a new owner theorem/RID/grade, scientific adoption, tag, OPEN-20 status, Stage-3 authorization, or outgoing notice. PR #21 carries the accepted Stage-2 SESSION/NUM scope; it is archived separately from these unchanged external inputs.
