#!/usr/bin/env python3
"""AZ v0.9 candidate: one content stage from the tagged v0.8 bytes.

    python3 -I evidence/az/v0.9/build_az_v0_9.py [--out PATH] [--log PATH]

Adds the Action 1 Stage 1 diagnostic (PI decision of 12 Nov 2026, 16:54 +03:00) as one
[NUM diagnostic] block, §4.2.1, with the pointers to it. Reads the base with git show az-v0.8,
asserts its SHA-256, applies exact-once edits, and asserts that every line of the base that is
not named in an edit is unchanged and in order. No compaction; no other content change.
"""
import argparse, hashlib, os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
DSN = "dsn/RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN.md"
BASE_TAG = "az-v0.8"
BASE_SHA = "146fcc2837f69e3d6a4fd626d29b5b038c7948c239eaedf7e55b57e74dd0ee76"
PKG = "81c87dcfc8d326e3c29861b9124c9654535f1c64cc6e5f9c7a9c9cafa6abd6eb"
DATA = "5ddbc60516acbeb75f2fc09fabdcaa017a320a68d88ee4904767c1c59b88500a"
sha = lambda b: hashlib.sha256(b).hexdigest()
LOG = []


def die(m):
    sys.stderr.write("BUILD STOP: %s\n" % m)
    sys.exit(1)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=os.path.join(ROOT, DSN))
    ap.add_argument("--log", default=os.path.join(HERE, "edit_log.txt"))
    a = ap.parse_args()
    base = subprocess.run(["git", "-C", ROOT, "show", "%s:%s" % (BASE_TAG, DSN)], capture_output=True, check=True).stdout
    if sha(base) != BASE_SHA:
        die("base is not the adopted v0.8 file")
    for path, want in (("evidence/az/token_resonance/SHA256SUMS", PKG), ("upload/az-token-resonance-stage1/HASHES.txt", DATA)):
        if sha(open(os.path.join(ROOT, path), "rb").read()) != want:
            die("%s does not have the recorded hash" % path)
    B = base.decode("utf-8").split("\n")
    L = list(B)
    touched = set()          # indices of base lines replaced

    def find(prefix):
        hits = [i for i, l in enumerate(L) if l.startswith(prefix)]
        if len(hits) != 1:
            die("anchor %r occurs %d times" % (prefix[:60], len(hits)))
        return hits[0]

    def set_line(key, prefix, new, why):
        i = find(prefix)
        LOG.append((key, "set-line", L[i], new, why)); L[i] = new

    def sub(key, prefix, old, new, why):
        i = find(prefix)
        if L[i].count(old) != 1:
            die("%s: %r occurs %d times" % (key, old[:50], L[i].count(old)))
        LOG.append((key, "sub", old, new, why)); L[i] = L[i].replace(old, new)

    def insert_before(key, prefix, text, why):
        i = find(prefix)
        new = text.rstrip("\n").split("\n")
        L[i:i] = new
        LOG.append((key, "insert-before", prefix, "%d lines" % len(new), why))

    def insert_after(key, prefix, text, why):
        i = find(prefix)
        new = text.rstrip("\n").split("\n")
        L[i + 1:i + 1] = new
        LOG.append((key, "insert-after", prefix, "%d lines" % len(new), why))

    # ---- header and footer (edition identity; DRAFT until adoption)
    set_line("H-title", "# RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN_v0.8", "# RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN_v0.9", "edition")
    set_line("H-status", "**Document status:** ADOPTED — PI, 12 November 2026",
             "**Document status:** DRAFT — candidate of v0.9; not adopted. `az-v0.8` governs until the PI adopts and tags this edition.  ", "edition")
    set_line("H-supersedes", "**Supersedes:** `RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN` v0.7",
             "**Supersedes:** `RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN` v0.8 (tag `az-v0.8`, SHA-256 `%s`)  " % BASE_SHA, "edition")
    sub("H-summary", "**Status summary:**", "**No Level B promotion. No OPEN-P1 / Dyadic bridge-candidate is promoted.**",
        "**No Level B promotion. No OPEN-P1 / Dyadic bridge-candidate is promoted.** One AZ-owned `[NUM diagnostic]` on seed-token "
        "resonance in the TDR-G dynamics is registered (§4.2.1); by the PI's outcome rule it changes neither the maturity level nor "
        "any OPEN.", "status summary names the new diagnostic and its limit")
    set_line("F", "*END OF DOCUMENT — RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN_v0.8*",
             "*END OF DOCUMENT — RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN_v0.9 — DRAFT candidate; adoption pending; `az-v0.8` governs until adoption and tag.*", "edition")

    # ---- routing, current state, criterion
    insert_after("S0.1-row", "| Phase-2 diagnostics computed on TDR-G defect-graph exports |",
                 "| Seed-token resonance diagnostic computed on the TDR-G engine (Action 1) | this DSN, Thread B §4.2.1 | `[NUM diagnostic]`, "
                 "AZ-owned, scoped to its cells, horizon and threshold; not a TDR-G result and **not** a bridge-candidate |", "routing row")
    sub("S0.2-B", "- **Thread B** (discrete $\\mathbb{Z}_N$ arithmetic structure):", "`AZ-OPEN-SCOPE-ARITH` is open (§2).",
        "`AZ-OPEN-SCOPE-ARITH` is open (§2). One item of this thread is owned here: `AZ-NUM-TOKRES-S1` `[NUM diagnostic]` — in a "
        "registered paired intervention at $N=120$ and $N=122$, replacing one initial token by a value with $4x\\equiv0\\pmod N$ "
        "raises the probability of a run ending with $M\\ge100$ nodes against its $\\pm1$ neighbour (§4.2.1); mechanism not "
        "established; no statement beyond its cells, horizon and threshold.", "current-state readout")
    sub("S1.1-crit", "`[OPEN]` **Success criterion.**", "and is disqualified as a bridge observable (§4.3.4).",
        "and is disqualified as a bridge observable (§4.3.4). The seed-token resonance diagnostic (§4.2.1) is an arithmetic condition "
        "with an effect on the dynamics, at two cells and one horizon; by the PI's outcome rule of 12 November 2026 it does not by "
        "itself meet this criterion or change the maturity level, and whether it bears on the criterion is left to a separate decision.",
        "the criterion's status is not changed; the new diagnostic is named with the rule that limits it")

    # ---- Thread B
    sub("S4.2-status", "**Status here:** Branch-local context and bridge-candidate observable family under OPEN-P1.",
        "and no TDR-G fact is used as evidence for a Dyadic claim.",
        "and no TDR-G fact is used as evidence for a Dyadic claim. One item of this thread is owned by this DSN: the diagnostic of §4.2.1.",
        "ownership of the new subsection stated")
    insert_before("S4.2.1", "### §4.3 Thread C — Graph/Transfer-Zeta Diagnostics", open(os.path.join(HERE, "block_4_2_1.md"), encoding="utf-8").read() + "\n",
                  "the diagnostic block (PI decision of 12 Nov 2026, 16:54 +03:00)")

    # ---- high-risk ledger
    insert_after("S5-row", "| TDR-G BIND3 / advance-spectrum |",
                 "| **Seed-token resonance diagnostic** (`AZ-NUM-TOKRES-S1`) | **`[NUM diagnostic]`: registered paired contrast at $N\\in\\{120,122\\}$, "
                 "$k=8$, 800 ticks, endpoint $M\\ge100$** | A mechanism; persistence at other $N$, $k/N$, policies, horizons or thresholds; an "
                 "explanation of TDR-26; a relation to the `4\\|q` rule or to Dyadic/DZT $q=4$; a TDR-G result; grounds for promotion | "
                 "SG-PROG-1, SG-AZ-3, SG-AZ-7 |", "high-risk row")

    # ---- artifact registry
    insert_before("S9", "**Two definitions of `G_birth(w)` in the deposited files — recorded, not resolved.**",
                  "- [RID: AZ-ART-TOKRES-S1] :: registration `records/az/AZ_TOKEN_RESONANCE_PREREGISTRATION.md` with its package "
                  "`evidence/az/token_resonance/` (`SHA256SUMS`, SHA-256 `%s`: runner, analysis, fixtures, negative controls, driver; the pinned "
                  "TDR-G engine `upload/tdrg-records/genesis_mode_b_mc.py` and orientation reference `evidence/tdrg/scripts/tdrg_orient_v2_12_14.py` "
                  "are used unchanged); campaign output `upload/az-token-resonance-stage1/` (`HASHES.txt`, SHA-256 `%s`; 19,900 records); report "
                  "`records/az/AZ_TOKEN_RESONANCE_STAGE1_REPORT.md`; verification `evidence/az/token_resonance/stage1/verify.sh` with its stored "
                  "output :: evidence for `AZ-NUM-TOKRES-S1` (§4.2.1)  \n"
                  "  Availability: in the repository (`EV-BYTES`, `EV-HASH`). The registered analysis was inspected and executed on the campaign "
                  "machine and again from the stored records, byte-identical (`EV-CODE`, `EV-RUN`); the engine runs were made once, on the PI's "
                  "server (Python 3.12.3), and are not rerun. The registration was reviewed and accepted before the run (reviews `5855522171`, "
                  "`5857601141`); the report was reviewed after it (`5869662603`).\n" % (PKG, DATA), "artifact entry")

    # ---- Appendix A
    insert_before("AppA", "### v0.8 — November 2026",
                  "### v0.9 — November 2026\n"
                  "One addition: the Action 1 Stage 1 result enters as an AZ-owned `[NUM diagnostic]`, `AZ-NUM-TOKRES-S1` (§4.2.1), by the PI's "
                  "decision of 12 November 2026 under the outcome rule of the same day — a registered paired contrast on seed-token resonance at "
                  "$N=120$ and $N=122$, with its scope and its evidence (`AZ-ART-TOKRES-S1`, §9). Pointers to it in §0.1, §0.2, §1.1, §4.2 and §5. "
                  "The maturity level, the OPEN registry and every earlier statement are unchanged. Record: `records/az/AZ_v0_9_RELEASE_RECORD.md`.\n",
                  "version entry")

    out = "\n".join(L)
    # ---- every base line not named in an edit survives, in order
    changed_old = {old for (_, op, old, _, _) in LOG if op == "set-line"}
    sub_lines = set()
    it = iter(L)
    kept = 0
    for bl in B:
        if bl in changed_old:
            continue
        if any(op == "sub" and old in bl for (_, op, old, _, _) in LOG):
            sub_lines.add(bl); continue
        for cl in it:
            if cl == bl:
                kept += 1
                break
        else:
            die("a base line is missing or out of order: %r" % bl[:80])
    if len(changed_old) != 4 or len(sub_lines) != 4:
        die("unexpected number of changed base lines: %d set, %d substituted" % (len(changed_old), len(sub_lines)))
    for bad in ("v0.8*", "candidate of v0.8"):
        if bad in out:
            die("stale string %r" % bad)
    open(a.out, "w", encoding="utf-8", newline="").write(out)
    with open(a.log, "w", encoding="utf-8") as f:
        f.write("AZ v0.9 edit log\nbase %s %s\nresult sha256 %s, %d bytes\nbase lines: %d; unchanged and in order: %d; replaced: %d; edited in place: %d\n\n" % (
            BASE_TAG, BASE_SHA, sha(out.encode()), len(out.encode()), len(B), kept, len(changed_old), len(sub_lines)))
        for k, (key, op, old, new, why) in enumerate(LOG, 1):
            f.write("E%02d %-12s %-13s\n    old: %s\n    new: %s\n    why: %s\n" % (k, key, op, old[:240], new[:240], why))
    print("base   %s" % BASE_SHA)
    print("result %s  %d bytes  (%d edits; %d of %d base lines unchanged and in order)" % (sha(out.encode()), len(out.encode()), len(LOG), kept, len(B)))


if __name__ == "__main__":
    main()
