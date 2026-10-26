# Number Genesis held records (PR #69, `upload/numgen-records`) — atlas hash check

**Date:** 26 October 2026. **By:** Claude, atlas owner. **Status:** record; nothing placed, nothing reconstructed, nothing rerun.
**Object:** branch `upload/numgen-records`, commit `925a39195c101a9b07690246a5e0e406404956de`, folder `upload/numgen-records/` (280 files: 278 held files incl. the two of `census1_tdrg_replay/`, plus `SHA256SUMS.txt` and `README_UPLOAD.md`), uploaded unchanged by the NUMGEN co-owner session (Claude) per the entry note §2.
**Script and inventory:** `evidence/numgen/inventory/build_numgen_upload_check.py` (SHA-256 `7b52d082e47118f532afcaa2ab86c9e4b4a0fb7f1b573083f46b73ed02701a1c`) → `evidence/numgen/inventory/numgen_upload_inventory_20261026.json` (`d21e443ace78e2d61191b07855fcfcb09a73c36eca2816ef46609712e227bae8`; two runs identical). Reads the branch; writes only the inventory.

## 1. Result

- `SHA256SUMS.txt`: **278/278 entries match** the uploaded bytes; no listed file absent; no unlisted file. **PASS.**
- Zip packages: 48 members hashed (`NUMGEN_v1_20_8_DRAFT_r2_REVIEW.zip`, `…_r3_REVIEW.zip`). 23 `.md` files carry the `> **[SUPERSEDED …]**` banner described in `README_UPLOAD.md`; their banner-stripped payloads (everything after the first blank line) were hashed as well.
- Identities cited by `numgen-v1.20.8` (`835a56f8…817e`, read at the tag): 31 distinct. **26 are present** in the upload (as files, zip members or banner-stripped payloads), including:
  - the adopted edition itself (`RTG_NUMBER_GENESIS_DSN_v1_20_8.md`, byte-equal to `main`), the predecessor v1.20.7 (`c4637e7a…ab28`) and the v1.20.6 payload (`2a51c4b1…48c5`, under the banner of `RTG_NUMBER_GENESIS_DSN_v1_20_6.md`);
  - the reviewed DRAFT r3 (`9d59cfa1…e7b3`, in the r3 package and as the r3 payload), r2 (`423cd719…7b78`), r1 payload (`eef001d1…c63c`);
  - the C7C-M2 Census-1 chain: protocol `f2a4a9a4…5795`, preregistration draft v4 `248f128c…8987`, freeze manifest `cefb7180…b165b`, opening manifest `d170efb5…5d73`, analysis log `e7b85fd2…0139`, U_DYAD and U_TDRG results (`ed3c72af…eae9`, `23f298dc…d33a`), E4 density `c67342a9…6fa8`, TDRG replay script/manifest/records (`73cfa2e3…8188`, `19e929aa…a30a`, `7b7dc451…77c8`);
  - the Dyadic row-A replay inputs (`dyad_numgen_lphase_rowA_cert.py` `117484ae…9cdb`, `lphase_rowA_certificate.json` `8697c697…d4fa`, `qw.py`, `tzw.py`), the independent L-PHASE check script and log (`d9d89bae…7ccf`, `e2a0d15a…f661`), the interface confirmation and replay receipt (`7a91c223…f78f`, `71bfc4c5…b66f`), the RF-06 spot check (`2a064eb9…f148`), `NG_SELFCHECK_REFERENCE_TRANSPORT_v1.md` (`b39de45c…ded4`).
- **5 cited identities are not in the upload** — all are other streams' editions, none a NUMGEN file:

| Cited in NUMGEN v1.20.8 | What it is | State |
|---|---|---|
| `0dcce9e4…bcd9` | RECOG v0.3.22 | present in the repository: `recog-v0.3.22:dsn/RTG_RELATIONAL_RECOGNITION_DSN.md` hashes to it (verified) |
| `2fb0a0fe…afce` | RRF v0.8.4 | present: `rrf-v0.8.4:dsn/RTG_RRF_REPRESENTATION_REGISTRY.md` (verified) |
| `40c9e63f…6ec9` | Dyadic v6.4.19 | present: `dyad-v6.4.19:dsn/RTG_DYADIC_OSCILLATOR_DSN.md` (verified) |
| `a3459522…0ae3` | RECOG v0.3.21 (predecessor citation) | no `recog-v0.3.21` tag; RECOG owner's history |
| `b393657e…a187` | RRF v0.8.3 (predecessor citation) | no `rrf-v0.8.3` tag; RRF owner's history |

- **v1.20.8 release record** (`NUMGEN_v1_20_8_RELEASE_RECORD.md`, `fb699967bbacc3eee5e8772a9b08d0cca2331ce8bf304fe96020ab776b4d1f97`, uploaded): cites 18 identities; all 18 are in the upload by 8-character prefix (release transform `5f219ee9…`, edit list, checker, checker output, the two diffs, the r3 package `a7fc9ed6…ee84`, the fingerprint and inventory tools).
- **Citation irregularities (editorial, for stage 1 / NA-04):** three abbreviated citations do not end in the last four characters of the hash they name — NUMGEN §9.2 `cefb7180…b165b` (5-character suffix; the file ends `…3b165b`, so it is the same hash written one character longer), release record `3354621b…f7a145` (file ends `…1a7f145`) and `8697c697…a4fa` (file ends `…c3ad4fa`). The 8-character prefixes identify the files uniquely in the upload; nothing else matches.

## 2. Placement

Following PI decision V2 for Genesis (25 Oct 2026, `records/gen/GEN_UPLOAD_HASH_CHECK_20261024.md` §2), the proposed home is **`upload/numgen-records/` on `main`, unchanged** (merge PR #69 as is): names, bytes and SHA-256 identities kept; `records/numgen/` stays the home of current review, disposition and release records; `BASELINE.md` gets a pointer when the NUMGEN co-owners next touch it. The PI decides; until then nothing is moved.

## 3. Atlas-side consequence

NUMGEN's cited evidence chain for C7C-M2 Census-1, the Dyadic row-A replay and the v1.20.x edition history is recoverable from the repository once PR #69 is merged; no NUMGEN citation points to a missing NUMGEN file. The atlas D2/D5 NUMGEN rows need no "missing proof source" diagnostic of the Genesis kind. The two untagged predecessor editions (RECOG v0.3.21, RRF v0.8.3) are those owners' history and are not NUMGEN gaps.
