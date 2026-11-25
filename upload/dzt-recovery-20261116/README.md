# DZT historical recovery - received payload

**[SESSION] RECEIVED ONLY / NOT ADOPTED.** Uploaded by ChatGPT on 16 November 2026 at the PI's explicit request to place the supplied files in the repository upload folder. No canonical DSN, scientific status, source pin, pipe or release tag is changed.

## Contents and exact preservation boundary

The PI supplied `dzt_recovery_20261116T135733Z_c1afc390.zip` (618,268 bytes; SHA-256 `44e14fb53f7746b4a3bd3a70f99f5e27ab8afd8d36a3b27334964a81be3ba0ee`) and its hash sidecar. Its 67 original files total 1,725,716 bytes and represent 54 distinct content hashes. The four collection records are `MANIFEST.json`, `SHA256SUMS`, `DUPLICATE_HASHES.json` and `README.md`.

**Storage form:** `payload/` contains eight binary parts of a lossless `tar.xz` transport. All 71 entry payloads match the supplied ZIP byte-for-byte. The original outer ZIP container is **not stored here**: this connection had no local-file binary upload action, so the entry payloads were recontainerized for bounded Git-blob transfer. Its unchanged `.zip.sha256` sidecar records the received ZIP identity, not the identity of the new transport. The joined transport has its own hash in `TRANSPORT_MANIFEST.json`.

Only archive path separators were normalized from Windows backslashes to POSIX slashes. Original filenames, numbered copies, contents and the separation between `originals/downloads/` and `originals/legacy-src/` are preserved. No line ending or encoding was normalized. Deterministic tar metadata is not historical provenance; source timestamp observations remain in the original collection manifest. Neither a larger file nor a `(1)` suffix was used to select a canonical version. Both v0.17 variants remain present.

## Verification and materialization

From a checkout of this branch (Python 3, standard library only):

```bash
python3 -I upload/dzt-recovery-20261116/verify_and_extract.py
python3 -I upload/dzt-recovery-20261116/verify_and_extract.py --extract
```

The first command only verifies. The second first verifies all parts, the joined archive, collection records, original sizes and hashes, and SHA256SUMS; it then writes all 71 entries to a **new** `received/` directory beside the helper. It refuses an existing destination. It does not execute any received Python file and performs no Git action. On Windows, `python` may be used instead of `python3`.

The extracted original sources are under `received/originals/`; the unchanged collection records are directly under `received/`. Extraction or subsequent evidence placement is not adoption. Keep the transport and original manifests as custody evidence; do not silently replace recovered files while repairing dependencies or preparing tests.

## Intake checks actually performed

- Recomputed the supplied ZIP SHA-256; matched the PI's sidecar and console value; ZIP CRC test passed.
- Independently checked all 67 original file lengths and SHA-256 values against the supplied manifest and SHA256SUMS; 54 unique hashes.
- Compared every entry after recontainerization and local extraction with the supplied ZIP: **71/71 byte-identical**.
- Ran this new intake helper locally: verification and extraction PASS. A modified chunk was rejected; five unsafe-path cases were rejected.
- All eight GitHub-created binary blob SHAs matched the independently computed local Git blob identities.
- **Zero recovered scientific scripts executed.** No historical owner campaign, proof certificate or numerical claim was recertified. The generated helper is intake tooling, not original scientific evidence.

## Owner follow-up

Review the recovered v0.9-v0.17 chain against the repository-selected DZT v0.8 baseline and the current owners. Receipt does not establish historical adoption or appoint either v0.17 variant as governing. The missing engine dependencies, historical text inconsistencies and LIT comparison remain matters for DZT's bounded triage and the PI's subsequent decisions. No original is deleted, deduplicated, promoted or merged into the live DSN by this upload.
