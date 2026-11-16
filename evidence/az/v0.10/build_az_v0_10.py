#!/usr/bin/env python3
"""AZ v0.10 candidate: one content stage from the tagged v0.9 bytes.

    python3 -I evidence/az/v0.10/build_az_v0_10.py [--out PATH] [--log PATH]

Adds the Action 1 Stage 2 result as a separate AZ-owned [NUM diagnostic], AZ-NUM-TOKRES-S2,
§4.2.2, with its artifact entry AZ-ART-TOKRES-S2 and the pointers to it (PI, 16 Nov 2026, as
recorded in review 5915724946: report accepted; prepare the separate S2 entry; Level A and
AZ-OPEN-PROMO retained; TDR-G only the edition notice). AZ-NUM-TOKRES-S1 is not changed.
Reads the base with git show az-v0.9, asserts its SHA-256 and the hashes of the Stage 2
package and data, applies exact-once edits, and asserts that every line of the base that is
not named in an edit is unchanged and in order. No compaction; no other content change.
"""
import argparse, hashlib, os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
DSN = "dsn/RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN.md"
BASE_TAG = "az-v0.9"
BASE_SHA = "c198a8bbddb23ce0d546c3ed03bddcdcf02dd83b974da7651a89a3fec5ac7598"
PKG = "25b796b3890a0e49c8f99f91a8866758b826c87a40dc5918b35928b5fb35eb4b"
DATA = "3e211e6a7bab27b9e13af0dd5c0a93128b79c464d64470ea4d6b86775314a7e7"
REG_COMMIT = "74ad6946e9710a2272b9d7792d6d8f0c45cda168"
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
        die("base is not the adopted v0.9 file")
    for path, want in (("evidence/az/token_resonance/stage2/SHA256SUMS", PKG), ("upload/az-token-resonance-stage2/HASHES.txt", DATA)):
        if sha(open(os.path.join(ROOT, path), "rb").read()) != want:
            die("%s does not have the recorded hash" % path)
    for path in ("records/az/AZ_TOKEN_RESONANCE_STAGE2_REPORT.md", "evidence/az/token_resonance/stage2_result/verify.sh",
                 "records/az/AZ_TOKEN_RESONANCE_STAGE2_AUTHORISATION.md", "records/az/AZ_TOKEN_RESONANCE_STAGE2_PILOT_INTAKE.md"):
        if not os.path.exists(os.path.join(ROOT, path)):
            die("%s is cited and missing" % path)
    B = base.decode("utf-8").split("\n")
    L = list(B)

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
    set_line("H-title", "# RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN_v0.9", "# RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN_v0.10", "edition")
    set_line("H-date", "**Date:** 14 November 2026", "**Date:** 16 November 2026  ", "edition")
    set_line("H-status", "**Document status:** ADOPTED — PI, 14 November 2026",
             "**Document status:** DRAFT — candidate of v0.10; not adopted. `az-v0.9` governs until the PI adopts and tags this edition.  ", "edition")
    set_line("H-supersedes", "**Supersedes:** `RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN` v0.8",
             "**Supersedes:** `RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN` v0.9 (tag `az-v0.9`, SHA-256 `%s`)  " % BASE_SHA, "edition")
    sub("H-summary", "**Status summary:**",
        "One AZ-owned `[NUM diagnostic]` on seed-token resonance in the TDR-G dynamics is registered (§4.2.1); by the PI's outcome rule it changes neither the maturity level nor any OPEN.",
        "Two AZ-owned `[NUM diagnostic]` entries on seed-token resonance in the TDR-G dynamics are registered, at $N=120,122$ (§4.2.1) and at "
        "$N=240,242,480$ (§4.2.2); by the PI's outcome rule they change neither the maturity level nor any OPEN.", "status summary names the second diagnostic")
    set_line("F", "*END OF DOCUMENT — RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN_v0.9*",
             "*END OF DOCUMENT — RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN_v0.10 — DRAFT candidate; adoption pending; `az-v0.9` governs until adoption and tag.*", "edition")

    # ---- routing, current state, criterion
    sub("S0.1-row", "| Seed-token resonance diagnostic computed on the TDR-G engine (Action 1) |",
        "| Seed-token resonance diagnostic computed on the TDR-G engine (Action 1) | this DSN, Thread B §4.2.1 | `[NUM diagnostic]`, AZ-owned, scoped to its cells,",
        "| Seed-token resonance diagnostics computed on the TDR-G engine (Action 1, Stages 1 and 2) | this DSN, Thread B §4.2.1, §4.2.2 | `[NUM diagnostic]`, AZ-owned, each scoped to its cells,",
        "routing row covers both entries")
    sub("S0.2-B", "- **Thread B** (discrete $\\mathbb{Z}_N$ arithmetic structure):", "One item of this thread is owned here:",
        "Two items of this thread are owned here:", "current-state readout: count")
    sub("S0.2-B2", "- **Thread B** (discrete $\\mathbb{Z}_N$ arithmetic structure):",
        "mechanism not established; no statement beyond its cells, horizon and threshold.",
        "and `AZ-NUM-TOKRES-S2` `[NUM diagnostic]` — the same contrast in the registered cells $(N,k)=(240,16),(242,16),(480,32)$, on "
        "$M\\ge\\theta(N)$ at a calibrated horizon and on $M\\ge100$ at tick 800: all ten contrasts of its confirmatory family meet the "
        "registered support criterion for a risk difference above 0.05 ($2x\\equiv0$ in all three cells; $2x\\equiv N/2$ at $N=240,480$), and at "
        "$N=242$ the near-quarter arm (the token drawn from the four values nearest $N/4$, $3N/4$) is equivalent to the native state (§4.2.2); for both, mechanism not established and no statement "
        "beyond their cells, horizons and thresholds.", "current-state readout of the second diagnostic")
    sub("S1.1-crit", "`[OPEN]` **Success criterion.**",
        "The seed-token resonance diagnostic (§4.2.1) is an arithmetic condition with an effect on the dynamics, at two cells and one horizon; "
        "by the PI's outcome rule of 12 November 2026 it does not by itself meet this criterion or change the maturity level,",
        "The seed-token resonance diagnostics (§4.2.1, §4.2.2) record an arithmetic condition with an effect on the dynamics, in five cells "
        "from $N=120$ to $N=480$ at their registered horizons; by the PI's outcome rule of 12 November 2026 they do not by themselves meet "
        "this criterion or change the maturity level,", "the criterion's status is not changed; the second diagnostic is named with the rule that limits it")
    sub("S1.1-crit2", "`[OPEN]` **Success criterion.**", "and whether it bears on the criterion is left to a separate decision.",
        "and whether they bear on the criterion is left to a separate decision.", "agreement with the plural subject")

    # ---- Thread B
    set_line("S4.2-head", "### §4.2 Thread B — Discrete $\\mathbb{Z}_N$ Arithmetic Structure (bridge-candidate family; one AZ-owned diagnostic)",
             "### §4.2 Thread B — Discrete $\\mathbb{Z}_N$ Arithmetic Structure (bridge-candidate family; AZ-owned diagnostics)",
             "heading no longer says 'one'; section number unchanged")
    sub("S4.2-status", "**Status here:** Branch-local context and bridge-candidate observable family under OPEN-P1.",
        "One item of this thread is owned by this DSN: the diagnostic of §4.2.1.",
        "Two items of this thread are owned by this DSN: the diagnostics of §4.2.1 and §4.2.2.", "ownership of the new subsection stated")
    insert_before("S4.2.2", "### §4.3 Thread C — Graph/Transfer-Zeta Diagnostics",
                  open(os.path.join(HERE, "block_4_2_2.md"), encoding="utf-8").read() + "\n",
                  "the Stage 2 diagnostic block (PI, 16 Nov 2026; review 5915724946)")

    # ---- §8 local use of two owner rows
    sub("S8-census", "- [RID: TDRG-ALG-EVENT-INVENTORY; TDRG-ALG-TOKEN-CENSUS-LAW] ::",
        "the per-tick check of `AZ-ART-TOKRES-S1` tested", "the per-tick checks of `AZ-ART-TOKRES-S1` and `AZ-ART-TOKRES-S2` tested",
        "local use names the second check")
    sub("S8-phase", "- [RID: TDRG-ALG-PARENT-CHILD-PHASE] ::", "of the intervention of §4.2.1;", "of the interventions of §4.2.1 and §4.2.2;",
        "local use names the second intervention")

    # ---- high-risk ledger
    insert_after("S5", "| **Seed-token resonance diagnostic** (`AZ-NUM-TOKRES-S1`) |",
                 "| **Seed-token resonance diagnostic, Stage 2** (`AZ-NUM-TOKRES-S2`) | **`[NUM diagnostic]`: registered paired contrasts in the cells "
                 "$(N,k)=(240,16),(242,16),(480,32)$, endpoints $M\\ge\\theta(N)$ at the calibrated horizon and $M\\ge100$ at tick 800, support criterion "
                 "for $RD>0.05$ with nominal simultaneous coverage** | A mechanism; an $N$-scaling law or $N$-independence; the endpoints as the same event "
                 "at different $N$; other $k/N$, policies, horizons or thresholds; the order hierarchy below 2; an explanation of TDR-26; a relation to "
                 "the `4\\|q` rule or to Dyadic/DZT $q=4$; a TDR-G result; grounds for promotion | SG-PROG-1, SG-AZ-3, SG-AZ-7 |", "high-risk row")

    # ---- artifact registry
    insert_before("S9", "**Two definitions of `G_birth(w)` in the deposited files — recorded, not resolved.**",
                  "- [RID: AZ-ART-TOKRES-S2] :: calibration pilot `records/az/AZ_TOKEN_RESONANCE_STAGE2_PILOT_PLAN.md`, its output "
                  "`upload/az-token-resonance-s2-pilot/` and intake `records/az/AZ_TOKEN_RESONANCE_STAGE2_PILOT_INTAKE.md`; registration "
                  "`records/az/AZ_TOKEN_RESONANCE_STAGE2_PREREGISTRATION.md` at commit `%s` with its package `evidence/az/token_resonance/stage2/` "
                  "(`SHA256SUMS`, SHA-256 `%s`: Stage 2 analysis, driver, negative controls, validation outputs; the Stage 1 runner, fixtures and "
                  "analysis library and the pinned TDR-G engine and orientation reference used unchanged); decisions and authorisation "
                  "`records/az/AZ_TOKEN_RESONANCE_STAGE2_AUTHORISATION.md`; campaign output `upload/az-token-resonance-stage2/` (`HASHES.txt`, "
                  "SHA-256 `%s`; 26,300 records); report `records/az/AZ_TOKEN_RESONANCE_STAGE2_REPORT.md`; verification "
                  "`evidence/az/token_resonance/stage2_result/verify.sh` with its stored output :: evidence for `AZ-NUM-TOKRES-S2` (§4.2.2)  \n"
                  "  Availability: in the repository (`EV-BYTES`, `EV-HASH`). The registered analysis was inspected and executed on the campaign "
                  "machine and again from the stored records, byte-identical (`EV-CODE`, `EV-RUN`); the engine runs were made once, on the PI's "
                  "server (Python 3.12.3), and are not rerun. The registration was reviewed and read back before the run (reviews `5890473916`, "
                  "`5906866246`); the pilot intake was reviewed before it (`5888182978`); the report after it (`5915724946`, which recomputed the "
                  "confirmatory statistics from the published counts).\n" % (REG_COMMIT, PKG, DATA), "artifact entry")

    # ---- Appendix A
    insert_before("AppA", "### v0.9 — November 2026",
                  "### v0.10 — November 2026\n"
                  "One addition: the Action 1 Stage 2 result enters as a separate AZ-owned `[NUM diagnostic]`, `AZ-NUM-TOKRES-S2` (§4.2.2), by the "
                  "PI's decision of 16 November 2026 under the outcome rule of 12 November 2026 — registered paired contrasts on seed-token resonance "
                  "in the cells $(N,k)=(240,16),(242,16),(480,32)$ on two endpoints, with their scope and evidence (`AZ-ART-TOKRES-S2`, §9). Pointers "
                  "to it in §0.1, §0.2, §1.1, §4.2, §5 and two §8 local-use clauses. `AZ-NUM-TOKRES-S1` is unchanged. The maturity level, the OPEN "
                  "registry, the owner pins and every earlier AZ-owned statement are unchanged. Record: `records/az/AZ_v0_10_RELEASE_RECORD.md`.\n",
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
    if len(changed_old) != 6 or len(sub_lines) != 7:
        die("unexpected number of changed base lines: %d set, %d substituted" % (len(changed_old), len(sub_lines)))
    for bad in ("one AZ-owned diagnostic)", "One item of this thread", "_v0.9*", "candidate of v0.9", "k = N/15", "is at least 0.05"):
        if bad in out:
            die("stale string %r" % bad)
    if out.count("[RID: AZ-NUM-TOKRES-S2]") != 1 or out.count("[RID: AZ-ART-TOKRES-S2]") != 1:
        die("new identifiers not declared exactly once")
    s1_old = [l for l in B if "[RID: AZ-NUM-TOKRES-S1]" in l]
    if s1_old != [l for l in L if "[RID: AZ-NUM-TOKRES-S1]" in l]:
        die("the S1 entry changed")
    open(a.out, "w", encoding="utf-8", newline="").write(out)
    with open(a.log, "w", encoding="utf-8") as f:
        f.write("AZ v0.10 edit log\nbase %s %s\nresult sha256 %s, %d bytes\nbase lines: %d; unchanged and in order: %d; replaced: %d; edited in place: %d\n\n" % (
            BASE_TAG, BASE_SHA, sha(out.encode()), len(out.encode()), len(B), kept, len(changed_old), len(sub_lines)))
        for k, (key, op, old, new, why) in enumerate(LOG, 1):
            f.write("E%02d %-12s %-13s\n    old: %s\n    new: %s\n    why: %s\n" % (k, key, op, old[:240], new[:240], why))
    print("base   %s" % BASE_SHA)
    print("result %s  %d bytes  (%d edits; %d of %d base lines unchanged and in order)" % (sha(out.encode()), len(out.encode()), len(LOG), kept, len(B)))


if __name__ == "__main__":
    main()
