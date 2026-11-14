#!/usr/bin/env python3
"""TDR-G v2.13, stage 1: corrected intermediate, built from the tagged v2.12.15 bytes.

    python3 -I evidence/tdrg/v2.13/stage1/build_tdrg_v2_13_stage1.py [--base FILE] [--out PATH] [--log PATH]

Reads the base with `git show tdrg-v2.12.15:dsn/RTG_DISCRETE_GENESIS_DSN.md` (or --base FILE) and
asserts its SHA-256. Every edit is located by an anchor that must occur exactly once (inside the
stated window where one is given); a missing or repeated anchor, or an old string that does not occur
exactly once in its line, stops the build.

Stage 1 holds every change that needs a reader's judgment (Methodology v1.4 §13.6; edit plan
records/tdrg/TDRG_v2_13_EDIT_PLAN.md, rows S1–S8, PI decisions D1 (a), D2 (a), D3 (a)): pins, the
Methodology declaration, the reduced §1, the status summary, the consumer rows, the §2 superseded
hypothesis with its Appendix B record, correction labels that carry a claim tag, and the verbatim copy
of §A.sim into §8. Version labels without content, the rest of the header, Appendix A and the footer
are left for stage 2 (tools/check_compaction.py).
"""
import argparse, hashlib, json, os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))
DSN = "dsn/RTG_DISCRETE_GENESIS_DSN.md"
BASE_TAG = "tdrg-v2.12.15"
BASE_SHA = "1e35be54a37bb227cd75e34fc1cd6732ae95782bdc147a76e736f16760c92e64"
LOG = []


def sha(s):
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def block(name):
    with open(os.path.join(HERE, "blocks", name), encoding="utf-8") as f:
        return f.read()


def die(msg):
    sys.stderr.write("BUILD STOP: %s\n" % msg)
    sys.exit(1)


class Doc:
    def __init__(self, text):
        self.L = text.split("\n")

    def find(self, prefix, after=None, before=None):
        lo = 0 if after is None else self.find(after) + 1
        hi = len(self.L) if before is None else self.find(before)
        hits = [i for i in range(lo, hi) if self.L[i].startswith(prefix)]
        if len(hits) != 1:
            die("anchor %r occurs %d times in its window" % (prefix[:70], len(hits)))
        return hits[0]

    def sub(self, key, prefix, old, new, note, after=None, before=None):
        i = self.find(prefix, after, before)
        if self.L[i].count(old) != 1:
            die("%s: %r occurs %d times in its line" % (key, old[:60], self.L[i].count(old)))
        self.L[i] = self.L[i].replace(old, new)
        LOG.append({"key": key, "mode": "str", "line_anchor": prefix[:80], "old": old, "new": new,
                    "old_sha256": sha(old), "new_sha256": sha(new), "note": note})

    def line(self, key, prefix, new, note, after=None, before=None):
        i = self.find(prefix, after, before)
        old = self.L[i]
        self.L[i] = new
        LOG.append({"key": key, "mode": "line", "line_anchor": prefix[:80], "old_sha256": sha(old),
                    "new_sha256": sha(new), "old_len": len(old), "new_len": len(new), "note": note})

    def replace_range(self, key, start_prefix, end_prefix, new_text, note):
        a, b = self.find(start_prefix), self.find(end_prefix)
        if not a < b:
            die("%s: empty or reversed range" % key)
        old = "\n".join(self.L[a:b])
        new_lines = new_text.split("\n")
        self.L[a:b] = new_lines
        LOG.append({"key": key, "mode": "range", "start": start_prefix[:80], "end": end_prefix[:80],
                    "old_lines": b - a, "new_lines": len(new_lines), "old_sha256": sha(old),
                    "new_sha256": sha(new_text), "note": note})
        return old

    def delete_line(self, key, prefix, note, blank_after=True):
        i = self.find(prefix)
        old = self.L[i]
        n = 1
        if blank_after:
            if self.L[i + 1] != "":
                die("%s: no blank line after the deleted line" % key)
            n = 2
        del self.L[i:i + n]
        LOG.append({"key": key, "mode": "delete", "line_anchor": prefix[:80], "old_sha256": sha(old),
                    "old_len": len(old), "note": note})
        return old

    def insert_after(self, key, prefix, new_text, note):
        i = self.find(prefix)
        new_lines = new_text.split("\n")
        self.L[i + 1:i + 1] = new_lines
        LOG.append({"key": key, "mode": "insert", "after": prefix[:80], "new_lines": len(new_lines),
                    "new_sha256": sha(new_text), "note": note})

    def text(self):
        return "\n".join(self.L)


def build(base):
    if sha(base) != BASE_SHA:
        die("base hash %s is not %s" % (sha(base), BASE_SHA))
    d = Doc(base)

    # S2 — Methodology declaration (header field and alias-table sentence)
    d.line("E01", "**DSN Methodology:**", "**DSN Methodology:** DSN_METHODOLOGY_v1.4 (`methodology-v1.4`)  ",
           "S2: the edition migrates to Methodology v1.4 (was: v1.2 declared for the v2.12.x line)")
    d.line("E02", "Canonical tags follow `DSN_METHODOLOGY`", "Canonical tags follow `DSN_METHODOLOGY` v1.4 §8.1.",
           "S2: the alias sentence states the governing edition; its v2.12.14 history (legacy rows, with tags) "
           "stays in the tagged predecessor")

    # S7 — status summary (2–4 present-state sentences), placed in stage 1 so that stage 2 only keeps it
    d.line("E03", "**Status summary:**", block("status_summary.txt").rstrip("\n"),
           "S7: present-state summary in three sentences; every statement is a readout of §1/§2/§6")

    # D1 (a) / S6 — §1 reduced to readouts with pointers
    sec1 = block("section1.md").rstrip("\n") + "\n"
    d.replace_range("E04", "## §1. Current Canonical State", "## §2. Active Frontier / OPEN Registry", sec1,
                    "D1 (a), S6: §1 as readouts with pointers; every dropped statement has its full home "
                    "(stage-1 record, §1 home table)")

    # S4 — owner-review tasks as current open items
    d.line("E05", "**Owner-review tasks**", block("owner_review.md").rstrip("\n"),
           "S4: TDR-G's own open items with current status; Programme v1.4 does not carry them")

    # S3 — historical pins: OPEN-OFN-2 connection (TDR-1, TDR-19)
    c_old = "Connection: OPEN-OFN-2 in `RTG_ONTOLOGICAL_FOUNDATIONS_v0.6`."
    c_new = "Connection: OPEN-OFN-2 (RTG-OFN-OPEN-DISC-INTERACTION) in `RTG_ONTOLOGICAL_FOUNDATIONS` v0.12 (`ofn-v0.12`)."
    d.sub("E06", "Connection: OPEN-OFN-2", c_old, c_new, "S3: TDR-1 connection repinned; OPEN-OFN-2 is open at ofn-v0.12",
          after="**OPEN TDR-1 — Interaction onset derivation**", before="**OPEN TDR-6 — Birth invariant**")
    d.sub("E07", "Connection: OPEN-OFN-2", c_old, c_new, "S3: TDR-19 connection repinned, as E06",
          after="**OPEN TDR-19 — Multistar axiom derivation**", before="**OPEN TDR-22a — Fixed-N asymptotics**")

    # correction label carrying a claim tag (TDR-6 sub-item)
    d.sub("E08", "- Total additive momentum $P$: `[FAIL]` as a birth invariant", "(SG-3, v2.12.15 `[COR]`)", "(SG-3)",
          "label: the correction is recorded in Appendix A; the statement stays")

    # D2 (a): no relocation of the TDR-24B record
    d.sub("E09", "**Current status (v2.12.14):** the derivation target",
          " The dated paragraphs below (v2.12.1–v2.12.9) are the supporting record; moving them to Appendix A is v2.13 layout work.",
          " The paragraphs below are the supporting record.",
          "D2 (a): the record stays in §2; the announced relocation is not made")

    # S8 — superseded hypothesis leaves §2; its Appendix B record is added (E29)
    hyp = d.delete_line("E10", "**`[REVISED]` v2.8 failed-relock hypothesis",
                        "S8: superseded hypothesis removed from TDR-25; recorded in Appendix B (E29)")
    d.sub("E11", "- *But the v2.8 failed-relock framing was too late-stage*",
          "*But the v2.8 failed-relock framing was too late-stage*", "*The failed-relock framing (Appendix B) is too late-stage*",
          "S8: pointer to the Appendix B record")

    # correction labels with a claim tag, pure provenance
    d.sub("E12", "**[SG-3]**", " *(v2.12.15 `[COR]`; OFN finding `pipes/TDRG/20261029-OFN-token-sum-gauge-label.md`)*", "",
          "label: provenance of the v2.12.15 correction (Appendix A, release record)")

    # S1 — AZ pin
    d.sub("E13", "Physical consequence: fully defective $K_3$", "(`az-v0.7`; statement unchanged from `az-v0.6`)", "(`az-v0.8`)",
          "S1: the cited AZ-ALG-ANTIPODAL-LOWORDER entry is byte-identical at az-v0.6, az-v0.7 and az-v0.8 (checker C6)")

    d.sub("E14", "4. Classify each component, in this order:",
          "*(v2.12.15 `[COR]`: the precedence as implemented; ties are outcomes", "*(ties are outcomes",
          "label: the correction is recorded in Appendix A; the qualifications stay")

    # S3 — consumer pins of CONV-TICK and LEM-NOANNIHIL
    d.sub("E15", "**(v2.12)** This convention is named **CONV-TICK**",
          "(it is imported by `RTG_ONTOLOGICAL_FOUNDATIONS` v0.7)",
          "(it is imported by `RTG_ONTOLOGICAL_FOUNDATIONS` v0.12, IMP-O08-14)",
          "S3: current consumer edition and import row")
    d.sub("E16", "`[DEF]` [RID: TDRG-DEF-ORIENT] **Path orientation rule.**",
          " *(v2.12.14 `[COR]`; owner dispositions of 27 Oct 2026, option (b).)*", "",
          "label: provenance (Appendix A, v2.12.14 release record); the superseded completion stays stated in the body")
    d.sub("E17", "`[DEF]` [RID: TDRG-DEF-STAR] **Star blow-up**",
          " *(v2.12.15 `[COR]` — event domain stated as implemented; owner finding N4)*", "",
          "label: provenance; the superseded wording stays stated in the body")
    d.sub("E18", "`[DEF]` [RID: TDRG-DEF-MULTISTAR] **Multistar**",
          "(two or more valid centres, any shape; *v2.12.15 `[COR]`: stated with the precision of TDRG-DEF-STAR*)",
          "(two or more valid centres, any shape)", "label: provenance")
    d.sub("E19", "`[ALG]` `[NUM exhaustive: $N=2$–$40$, all $(\\Delta_0,d_0)$]`",
          "(exported to `RTG_ONTOLOGICAL_FOUNDATIONS` v0.7 as `[RESULT]` `[from: ALG]`)",
          "(imported by `RTG_ONTOLOGICAL_FOUNDATIONS` v0.12 as IMP-O08-06)",
          "S3: current consumer edition and import row (OFN v0.12 imports it as `[ALG]`)")
    d.sub("E20", "`[ALG]` `[NUM exhaustive: even $N\\le40$, $k\\le N/6$]`", " *(v2.12.14 `[COR]`)*", "",
          "label: provenance of the v2.12.14 correction")
    d.sub("E21", "is **exactly conserved**", "*(v2.12.14 `[COR]`: the converse fails", "*(the converse fails",
          "label: the counterexample stays")
    d.sub("E22", "is **exactly conserved**", "**Generalization** *(v2.12.15 `[COR]`)*:", "**Generalization**:",
          "label: provenance")
    d.sub("E23", "Rows $|d|_c\\le2$ are retrigger-entry ICs", "*(v2.12.14 `[COR]`: this is not node-relabelling",
          "*(this is not node-relabelling", "label: the qualification stays")

    # §7 — XFER-O08-01 is a separate decision, not v2.13 work
    d.sub("E24", "- `[ALG]` [import: RTG_ONTOLOGICAL_FOUNDATIONS_v0.12",
          "Custody transfer XFER-O08-01: **deferred** to v2.13 (the RID stays OFN's).",
          "Custody transfer XFER-O08-01: **open**, a separate decision of both owners (the RID stays OFN's).",
          "scope: custody is outside v2.13 (PI, 13 Nov 2026); the state is stated as open")

    # S1, S7 — consumer rows as current use; the notice sentence is queue history
    d.replace_range("E25", "**Consumers** (from the consumers' own records;", "**Pins.** Governing editions at this release:",
                    block("consumers.md").rstrip("\n") + "\n",
                    "S1, S7: rows state current use; AZ at az-v0.8 from its own §8; queue states and the "
                    "'notices after the tag' sentence leave")
    d.line("E26", "**Pins.** Governing editions at this release:", block("pins.md").rstrip("\n"),
           "S1, S3: current pins; no historical pin remains live")

    d.sub("E27", "- [RID: TDRG-EXPORT-DISCRETE-TRIAD]",
          " *(v2.12.15 `[COR]`: the row named the earlier D/A/B gate; Programme v1.4 §6.4 notice.)*", "",
          "label: provenance of the v2.12.15 correction")

    # D3 (a) / S5 — §A.sim verbatim into §8
    i = d.find("### §A.sim — Simulation Artifact Evolution `[ENG]`")
    j = d.find("`[RESULT]` Policy and bookkeeping bugs can invert the cosmological interpretation.")
    table = d.L[i + 2:j - 1]
    if not (table[0].startswith("| Version |") and table[-1].startswith("| v13 |") and d.L[i + 1] == "" and d.L[j - 1] == ""):
        die("E28: §A.sim layout not as expected")
    # review R1 (PR #268): only the evidence table becomes live; the closing interpretive `[RESULT]` of §A.sim,
    # which has no `[from: …]` pairing (Methodology §3.4), is not promoted and stays at the tagged predecessor
    sim = "\n".join(["", "**Simulation artifact evolution** `[ENG]` (engine lineage; the table of Appendix A §A.sim, moved verbatim):", ""]
                    + table)
    d.insert_after("E28", "- Post-edition data, not cited by any claim here:", sim,
                   "D3 (a), S5: the table carries live records (a [FAIL] row that invalidates the v1–v2 results); "
                   "review R1: the closing interpretive [RESULT] is not promoted to live text; stage 2 removes the "
                   "Appendix A copy")

    # S8 — Appendix B record of the superseded hypothesis
    rec = ("- `[SUPERSEDED]` Failed-relock hypothesis for the $N=720$ runaway (v2.8, TDR-25). Original: \"" +
           hyp.split(":** ", 1)[1] + "\" Reason: too late-stage — r43 is in the clean-star-producing mode from the "
           "first window and never engages the lock (TDR-25, bridge part 2). Replacement: early lock-nonengagement / "
           "relock-defective attractor (TDR-25, TDR-26). Recorded in: v2.13 (removed from §2 TDR-25).")
    d.insert_after("E29", "- [FAIL] $K_3$ globally explosive", rec,
                   "S8: permanent record of the hypothesis removed by E10, with its original statement")
    return d.text()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base")
    ap.add_argument("--out", default=os.path.join(ROOT, DSN))
    ap.add_argument("--log", default=os.path.join(HERE, "edit_log.json"))
    a = ap.parse_args()
    if a.base:
        base = open(a.base, encoding="utf-8").read()
    else:
        base = subprocess.run(["git", "-C", ROOT, "show", "%s:%s" % (BASE_TAG, DSN)], capture_output=True,
                              check=True).stdout.decode("utf-8")
    out = build(base)
    with open(a.out, "w", encoding="utf-8", newline="") as f:
        f.write(out)
    with open(a.log, "w", encoding="utf-8") as f:
        json.dump({"base_tag": BASE_TAG, "base_sha256": BASE_SHA, "intermediate_sha256": sha(out),
                   "edits": LOG}, f, indent=1, ensure_ascii=False)
        f.write("\n")
    print("stage-1 intermediate", sha(out), len(out.encode()), "bytes,", len(LOG), "edits")


if __name__ == "__main__":
    main()
