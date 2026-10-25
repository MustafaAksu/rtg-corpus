# Genesis held records (PR #40, `upload/gen-records`) — atlas hash check and placement plan

**Date:** 24 October 2026. **By:** Claude, atlas owner. **Status:** record; nothing placed yet, nothing reconstructed.
**Object:** branch `upload/gen-records`, commit `2425539a24b130a34d326ff07027232ee1966879`, folder `upload/gen-records/` (38 files: 36 held files + `SHA256SUMS.txt` + `README_UPLOAD.md`), uploaded unchanged by the Genesis co-owner session (Claude) per the entry note §2.
**Script and inventory:** `evidence/gen/inventory/build_gen_upload_check.py` → `evidence/gen/inventory/gen_upload_inventory_20261024.json` (reads the branch; writes only the inventory).

## 1. Result

- `SHA256SUMS.txt`: 36/36 entries match the uploaded bytes; no listed file absent; no unlisted file. **PASS.**
- Zip packages: 101 members hashed (7 packages: v2.8.6/7/8/9 draft, release and adoption-kit packages, `K3_6S_v0_3_package.zip`, `GENESIS_DYAD_v6_4_13_CONSUMER_PACKAGE.zip`).
- Identities cited by `gen-v2.8.9` (`d143673e…c6fc`) and the OFN Q6 erratum: 36 distinct hash prefixes. **25 are present** in the upload (as files or zip members), including:
  - `GENESIS_V2_8_9_RELEASE_RECORD.md` `f6df5d11b877cfb79640290744e87cd73e2487a2c71b1492fffeb615a13e4181` — the v2.8.9 release record cited by the erratum; **recovered**;
  - the adopted editions v2.8.6 (`294c6fc2…a269`), v2.8.7 (`d5d1e57c…e361`), v2.8.8 (`9abd3616…0f37`) and v2.8.9 (`d143673e…c6fc`, byte-equal to `main`) inside the release packages — the pre-repository history editions, recoverable as files;
  - the D-4 session record (`1a5f7f56…cee3`), owner-pass manifests (`53782f85…0570`, `7519e14f…135a`, `81939e5f…f542`), occurrence disposition plan (`aee218c0…1ee3`), K3 session record (`9f95d48d…083a`), six-step clock note (`049e313e…bc9e`);
  - evidence scripts cited in §6.3a.1/§6.3b/§6.3c: `d4_transported_cubic_cert.py` (`f4c38285…3f6d`), `kappa_pq_symbolic.py` (`091a4210…42b2`), `kappa_pq_independent.py`, `lemmaS_hand_identities.py`, `lemmaS_burnside_check.py`, `genesis_nu5_p5_replay.py` (`34bab140…61cb`).
- **11 cited identities are not in the upload** (recorded as missing; consistent with the README's "not held" list):

| Cited in GEN v2.8.9 | What it is | State |
|---|---|---|
| `046ac458…85cc` | `K3_factor_obstruction.zip` (§6.3a evidence package) | missing |
| `384aaa5f…01ee` | `k3_obstruction_exact_check.py` (exact source-data certificate, §6.3a) | missing |
| `91608cb7…7f2b`, `e5e268a6…af7d`, `dcb08a27…1038`, `44105683…6001` | `fac.py`, `exact_chiral.py`, `k3.py` `[NUM]`, `exact_q.py` (confirmatory, §6.3a) | missing |
| `7d761090…d4ff` | `k3_six_step_factor_check.py` (§6.3a.1) | missing |
| `06d5e0c9…82b1` | `ER2B_OBSERVABLE_RESPONSE_v1.zip` (historical coefficient source) | missing; ER-2B owner may hold it |
| `41ed7660…475c` | adopted v2.8.5 edition bytes (build base of v2.8.6) | missing (no `gen-v2.8.5` tag; editions ≤ v2.8.5 not held) |
| `883644f5…7cec` | v2.8.9 "exact r2 bytes" (draft round) | missing (draft; the adopted bytes are present) |
| `5958f7fe…8542` | Dyadic v6.4.13 file (GEN's replay target) | not a Genesis file; no `dyad-v6.4.13` tag in the repository — Dyadic owner's history |

None of the nine `GEN-ART-*` "proof-source reference required" artifacts (GB-11) is in the upload; the Genesis co-owner's disposition §5 says the same. The scripts present are release-pipeline scripts and the §6.3 certificates.

## 2. Placement — PI decision V2 (25 October 2026)

**Decision (PI, 25 Oct 2026, 01:13):** the permanent home of the recovered Genesis records is **`upload/gen-records/`** on `main` (merged with PR #40).
- The files are **not** moved to `records/gen/` or `evidence/gen/packages/`.
- Their names, bytes and SHA-256 identities are kept.
- The `upload/gen-records/…` citations in the Genesis Appendix A (v2.9 candidate) stay as written.
- `BASELINE.md` carries a pointer to this home.
- `records/gen/` remains the home of current review, disposition and release records.

**Re-check at this update.** On `main` @ `ad7e702`, `sha256sum -c upload/gen-records/SHA256SUMS.txt` gives 36/36 OK. The folder holds 38 files: the 36 listed, plus `SHA256SUMS.txt` (`beb32a22…f8ca`) and `README_UPLOAD.md` (`ecab0818…34e5`).

**Superseded plan.** The plan first written here (24 Oct 2026) would have moved the `.md` records to `records/gen/`, the zip packages to `evidence/gen/packages/` and the manifest and README to `evidence/gen/inventory/`. It is withdrawn by the decision above and is retained in the git history of this file (commit `38ed243`).

**Unchanged.**
- The missing identities stay "missing" until a session places the originals on an `upload/…` branch.
- A new derivation (e.g. the co-owner's `gen_owner_advisory_checks.py`) is an independent contribution, never a recovery (Methodology v1.4 §12.3).

*(§2 updated on the PI's instruction by the Genesis co-owner session (Claude), 25 Oct 2026; §1 and §3 are the atlas owner's text, unchanged.)*

## 3. Atlas-side consequence

Atlas D4a F14 / D4b GEN.D3 (proof sources) stay as they are; the next atlas refresh adds "release record `f6df5d11…4181` recovered; editions v2.8.6–v2.8.8 recoverable; §6.3 certificates present" and keeps the nine `GEN-ART-*` gaps.
