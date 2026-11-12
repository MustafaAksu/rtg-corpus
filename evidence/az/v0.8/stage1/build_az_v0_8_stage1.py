#!/usr/bin/env python3
"""AZ v0.8, stage 1: corrected intermediate, built from the tagged v0.7 bytes.

    python3 -I evidence/az/v0.8/stage1/build_az_v0_8_stage1.py [--out PATH] [--log PATH]

Reads the base with `git show az-v0.7:dsn/RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN.md`
and asserts its SHA-256. Every edit is located by an anchor that must occur exactly
once; a missing or repeated anchor stops the build. Stage 1 holds every change that
needs a reader's judgment (Methodology v1.4 §13.6): pins, availability, tag forms,
the proof of PROP-AZ-CORE-EQUIV, the Import Ledger rows and the removal of restated
owner text from the threads. The header, the dated list of §10, Appendix A and the
footer are left for stage 2.

Owner statements moved into the Import Ledger are taken from the v0.7 lines
byte for byte (function `body`); nothing in them is reworded here.
"""
import argparse
import hashlib
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))
DSN = "dsn/RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN.md"
BASE_TAG = "az-v0.7"
BASE_SHA = "2294d2a3287651802824a77ea22fb8f3896f6837cca1162fd8479ff02839fc94"
DY_OLD = "`RTG_DYADIC_OSCILLATOR_DSN` v6.4.23 (`dyad-v6.4.23`)"
DY_NEW = "`RTG_DYADIC_OSCILLATOR_DSN` v6.4.24 (`dyad-v6.4.24`)"
DY_SRC = "`RTG_DYADIC_OSCILLATOR_DSN` v6.4.24"
TD_SRC = "`RTG_DISCRETE_GENESIS_DSN` v2.12.14"

LOG = []


def sha(b):
    return hashlib.sha256(b).hexdigest()


def block(name):
    with open(os.path.join(HERE, "blocks", name), encoding="utf-8") as f:
        return f.read()


def die(msg):
    sys.stderr.write("BUILD STOP: %s\n" % msg)
    sys.exit(1)


class Doc:
    def __init__(self, text):
        self.L = text.split("\n")

    def find(self, prefix, lo=0, hi=None):
        hi = len(self.L) if hi is None else hi
        hits = [i for i in range(lo, hi) if self.L[i].startswith(prefix)]
        if len(hits) != 1:
            die("anchor %r occurs %d times" % (prefix[:70], len(hits)))
        return hits[0]

    def replace_range(self, key, start_prefix, end_prefix, new_text, note):
        """Replace lines [start, end) by new_text (which carries its own line breaks)."""
        a = self.find(start_prefix)
        b = self.find(end_prefix)
        if not a < b:
            die("%s: range is empty or reversed" % key)
        old = "\n".join(self.L[a:b])
        new_lines = new_text.split("\n")
        if new_lines and new_lines[-1] == "":
            new_lines = new_lines[:-1]
        self.L[a:b] = new_lines
        LOG.append((key, "replace-range", "%d lines, sha256 %s" % (b - a, sha(old.encode())[:16]),
                    "%d lines" % len(new_lines), note))

    def sub(self, key, line_prefix, old, new, note):
        i = self.find(line_prefix)
        if self.L[i].count(old) != 1:
            die("%s: %r occurs %d times in its line" % (key, old[:60], self.L[i].count(old)))
        self.L[i] = self.L[i].replace(old, new)
        LOG.append((key, "sub", old, new, note))

    def set_line(self, key, line_prefix, new, note):
        i = self.find(line_prefix)
        old = self.L[i]
        self.L[i] = new
        LOG.append((key, "set-line", "sha256 %s (%d chars)" % (sha(old.encode())[:16], len(old)), new[:120], note))

    def insert_before(self, key, line_prefix, new_text, note):
        i = self.find(line_prefix)
        new_lines = new_text.split("\n")
        if new_lines and new_lines[-1] == "":
            new_lines = new_lines[:-1]
        self.L[i:i] = new_lines
        LOG.append((key, "insert-before", line_prefix[:60], "%d lines" % len(new_lines), note))

    def text(self):
        return "\n".join(self.L)


def body(line, cut=None, lead=True):
    """The statement text of a v0.7 thread line: leading tags up to the first '**' removed,
    everything from `cut` on removed. No other change."""
    s = line
    if lead:
        k = s.index("**")
        s = s[k:]
    if cut is not None:
        if s.count(cut) != 1:
            die("cut %r occurs %d times" % (cut, s.count(cut)))
        s = s[: s.index(cut)]
    return s.rstrip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=os.path.join(ROOT, DSN))
    ap.add_argument("--log", default=os.path.join(HERE, "edit_log.txt"))
    a = ap.parse_args()

    base = subprocess.run(["git", "-C", ROOT, "show", "%s:%s" % (BASE_TAG, DSN)],
                          capture_output=True, check=True).stdout
    if sha(base) != BASE_SHA:
        die("base hash %s is not the adopted v0.7 hash" % sha(base))
    d = Doc(base.decode("utf-8"))
    B = list(d.L)                      # frozen copy of the base lines, for row bodies

    def bline(prefix):
        hits = [l for l in B if l.startswith(prefix)]
        if len(hits) != 1:
            die("base line %r occurs %d times" % (prefix[:60], len(hits)))
        return hits[0]

    # deposit hashes, read from the deposit's own list
    dep = {}
    with open(os.path.join(ROOT, "upload/az-records/SHA256SUMS"), encoding="utf-8") as f:
        for ln in f:
            h, p = ln.split()
            dep[p.lstrip("*")] = h
    for p, h in dep.items():
        full = os.path.join(ROOT, "upload/az-records", p)
        if os.path.exists(full) and sha(open(full, "rb").read()) != h:
            die("deposit file %s does not match its recorded hash" % p)
    chk = os.path.join(ROOT, "evidence/az/core_equiv_check/az_core_equiv_check.py")
    chk_sha = sha(open(chk, "rb").read())

    # ------------------------------------------------------------------ A5/A6 aliases, owner map
    d.replace_range("A5-A6", "## Local Tag Aliases", "## §0. What This Document Is", block("01_aliases.md"),
                    "aliases under Methodology v1.4 §8.4; [ENG-planned], [ENG-historical] dropped; labels separated "
                    "from status tags; identifier owner map")

    # ------------------------------------------------------------------ §0
    d.replace_range("S0-intro", "## §0. What This Document Is", "### §0.1 v0.6 Distributed-Ownership Map",
                    block("02_section0_intro.md"), "version-scoped wording removed; functions point to their sections")
    d.set_line("S0.1-head", "### §0.1 v0.6 Distributed-Ownership Map", "### §0.1 Ownership and Layer Routing Map",
               "serves the layer-routing function (section map, §0.3)")
    d.sub("S0.1-dyad", "| Continuous $p$-resonance arithmetic, OPEN 9", DY_OLD, DY_NEW, "pin (C5)")
    d.sub("S0.1-engine", "| Graph/transfer-zeta diagnostic engine", "internal and **now `[ENG PASS]`** (was `[ENG-blocker]` through v0.5)",
          "internal; `[ENG PASS]` (availability of the certifying files: §9)", "history removed; availability pointer")
    d.sub("S0.1-facts", "| Graph-theoretic facts about the diagnostic objects", "Thread-C-owned `[THM-ALG]` / `[ALG]`; not cross-branch",
          "Thread-C-owned `[THM]` / `[ALG]`; not cross-branch", "tag form (D3)")
    d.sub("S0.1-sg04", "`[SG-AZ-0.4]` **Refresh is not promotion.**",
          "**v0.6 note:** the two internal `[THM-ALG]`/`[ALG]` items registered this version are",
          "The two internal results of §4.3.2 (`[THM]` and `[ALG]`) are", "version note removed; tag form (D3)")
    d.insert_before("S0.2-S0.3", "## §1. Study Goal and Historical Origin", block("03_section0_state_map.md"),
                    "current-state readout and declared section map (D1 a); navigation text, mapped to its sections")

    # ------------------------------------------------------------------ §1
    d.sub("S1.1-done", "3. Stabilize the graph/transfer-zeta diagnostic infrastructure",
          " **(v0.6: this is now done — infrastructure certified, first diagnostic executed and interpreted.)**",
          " This is done: the infrastructure is certified and a first diagnostic is executed and interpreted (§4.3).",
          "version note reworded as current status")
    d.sub("S1.1-crit", "`[OPEN]` **Success criterion.**", "**v0.6 status: NOT met.**", "**Status: not met.**", "version label removed")
    a0 = d.find("The concrete arithmetic observations that make this motivation non-trivial")
    a1 = d.find("- `[import-ref]` **The dyadic channel boundary at $b=4$.**")
    old = "\n".join(d.L[a0:a1 + 1])
    d.L[a0:a1 + 1] = [
        "The arithmetic observations that make this motivation non-trivial — that elevate it above numerology — are owned "
        "by the Dyadic DSN and are cited here by identifier only; their statements, scopes and boundary cases are the "
        "owner's and are cited once, with their limitations, in §8: the $p=5$ lattice cancellation (`DYAD-ALG-GLATTICE5`); the failure of "
        "prime-horizon first-lattice transparency at $p=7$ and the near-zero but nonzero $p=12$ cascade boundary (items of "
        "the owner's record `DYAD-OPEN-P-RESONANCE`); the low-degree pure anti-holomorphic raw vanishing for "
        "$b\\in\\{2,3,4\\}$ in the ranges $p\\ge b+2$ (`DYAD-ALG-VANISH-B2`, `DYAD-ALG-VANISH-B3`, `DYAD-ALG-VANISH-B4`); "
        "and the dyadic channel boundary at $b=4$ (`DYAD-ALG-B5-ALLP-NONVANISHING`)."]
    LOG.append(("B2", "replace-range", "%d lines, sha256 %s" % (a1 + 1 - a0, sha(old.encode())[:16]), "1 line",
                "five restated Dyadic results cited by RID; statements once, in §8"))
    d.set_line("S1.3-AZ0", "`[DEF]` **Milestone AZ-0",
               "`[DEF]` **Milestone AZ-0 (closed).** Create a clean ledger of what already exists: Dyadic OPEN 9 arithmetic "
               "facts, TDR-G candidate observables, and graph-zeta engineering blockers. The ledger is kept against the pinned "
               "owner editions (§8) without adding derivations or Zeta-owned scientific claims.",
               "refresh history (v0.2–v0.6, superseded pins) removed; recoverable at az-v0.7")
    d.sub("S1.3-AZ1", "`[DEF]` **Milestone AZ-1", "**Milestone AZ-1 (CLOSED — v0.6).**", "**Milestone AZ-1 (closed).**", "version label")
    d.sub("S1.3-AZ2", "`[DEF]` **Milestone AZ-2", "**Milestone AZ-2 (ATTEMPTED — negative-clarifying — v0.6).**",
          "**Milestone AZ-2 (attempted; negative-clarifying).**", "version label")

    # ------------------------------------------------------------------ §2
    d.replace_range("S2", "## §2. Active Frontier / OPEN Registry", "## §3. Scope Guards", block("04_section2.md"),
                    "OPEN entries in the Methodology §5.1 form; questions unchanged; closed modules as one-line records")

    # ------------------------------------------------------------------ §3
    d.set_line("S3-SG5-head", "**[SG-AZ-5] — Provenance guard for imported graph-zeta results (REVISED v0.6).**",
               "**[SG-AZ-5] — Provenance guard for imported graph-zeta results.**  ", "version label")
    i = d.find("*(Through v0.5 this guard read")
    old = d.L[i]
    del d.L[i]
    LOG.append(("S3-SG5-hist", "delete-line", "sha256 %s (%d chars)" % (sha(old.encode())[:16], len(old)), "",
                "history of the guard's earlier wording; recoverable at az-v0.7; the guard text is unchanged"))
    d.sub("S3-SG6", "This document does not migrate ownership of any physics result",
          "*(v0.6 clarification: PROP-AZ-CORE-EQUIV and the antipodal-band low-order obstruction are",
          "*(PROP-AZ-CORE-EQUIV and the antipodal-band low-order obstruction are", "version label")
    d.sub("S3-SG7", "**v0.6 worked example of the trap this guard exists to catch:**",
          "**v0.6 worked example of the trap this guard exists to catch:**",
          "**Worked example of the trap this guard exists to catch:**", "version label")
    d.sub("R1-SG7", "**Worked example of the trap this guard exists to catch:**",
          "It is proven static $\\mathbb{Z}_N$ substrate geometry that would appear for *any* antipodal-band graph on *any* "
          "$\\mathbb{Z}_N$ (§4.3.2, §4.3.4); a \"resemblance\" to Dyadic cyclic selection is therefore vacuous.",
          "It is not specific to TDR-G dynamics: in the tested protocol a core-matched random-$\\theta$ antipodal-band null "
          "with no TDR-G dynamics reproduces it (`[NUM diagnostic]`; §4.3.3 Chain 2, $N\\in\\{120,180,240\\}$; §4.3.4). It is "
          "read as static $\\mathbb{Z}_N$ antipodal-band geometry on that evidence; nothing is asserted for every "
          "antipodal-band graph or every $N$. A \"resemblance\" to Dyadic cyclic selection is therefore vacuous as evidence "
          "of a bridge.",
          "review 5874174108 R1: universal quantifier and 'proven' removed; scope of the numerical evidence stated")
    for n in ("1", "2", "4"):
        d.sub("S3-PROG-%s" % n, "**[SG-PROG-%s]**" % n, "`[source: RTG_PROGRAMME_OVERVIEW v1.4 §8]`",
              "`[import: RTG_PROGRAMME_OVERVIEW v1.4 §8 | SG-PROG-%s]`" % n, "[source:] -> [import:] (Methodology §3.3); same pin")
    i = d.find("## §4. Three Threads")
    if d.L[i - 2] != "---" or d.L[i - 1] != "":
        die("unexpected lines before §4")
    d.L[i - 2:i - 2] = ["<!-- AI_CONTEXT_CORE_END -->", ""]
    LOG.append(("A7-marker", "insert", "", "<!-- AI_CONTEXT_CORE_END -->", "context-core marker at the end of §3 (section map §0.3)"))

    # ------------------------------------------------------------------ §4.1 Thread A
    thread_a = "\n".join([
        "### §4.1 Thread A — Continuous $p$-Resonance (Dyadic OPEN 9 reference index)",
        "",
        "**Ownership:** %s, §2 and §6.11.  " % DY_NEW,
        "**Status here:** Reference only. All results are cited as `[import-ref]`. This document does not own, restate, "
        "retag, or add sub-items to Dyadic OPEN 9. SG-PROG-2, SG-AZ-3 and SG-AZ-6 apply.",
        "",
        "#### §4.1.1 Certified results (cited by reference)",
        "",
        "The Dyadic results this study refers to are listed in the first group of §8, one row per owner identifier, each "
        "with a readout, its limitations, the owner's tag and its location. They are not stated a second time here.",
        "",
        "#### §4.1.2 Active open frontier (owned by the Dyadic DSN)",
        "",
        "The open arithmetic frontier is the owner's: Dyadic §2 OPEN 9 (`DYAD-OPEN-P-RESONANCE`, active sub-items). It "
        "is programme context only. Progress on it is tracked in the Dyadic DSN, and this document keeps no list of its "
        "items.",
        "",
        ""])
    d.replace_range("B1-B3", "### §4.1 Thread A", "#### §4.1.3 Arithmetic-resonance observation", thread_a,
                    "restated owner results and the owner's frontier list removed; statements once, in §8; §4.1.3 unchanged")

    # ------------------------------------------------------------------ §4.2 Thread B
    thread_b = "\n".join([
        "### §4.2 Thread B — Discrete $\\mathbb{Z}_N$ Arithmetic Structure (bridge-candidate only)",
        "",
        "**Ownership:** %s (`tdrg-v2.12.14`).  " % TD_SRC,
        "**Status here:** Branch-local context and bridge-candidate observable family under OPEN-P1. SG-PROG-1, SG-PROG-4, "
        "SG-AZ-3, and SG-AZ-0.4 apply. No TDR-G result is imported as a cross-branch claim, and no TDR-G fact is used as "
        "evidence for a Dyadic claim.",
        "",
        "`[bridge-candidate]` **Observable family.** The TDR-G objects this study treats as candidate OPEN-P1 observables "
        "are listed in the second group of §8, one row per owner identifier or group of identifiers, each with a readout, "
        "its limitations, the owner's tag, scope and convention. They are not stated a second time here. The status of "
        "the family as a whole is the hypothesis that some of these objects could serve as OPEN-P1 observables; no row is "
        "a bridge, and none is used outside its branch.",
        "",
        ""])
    d.replace_range("B4", "### §4.2 Thread B", "`[AZ-OPEN]` **AZ-OPEN-SCOPE-ARITH.**", thread_b,
                    "nine restated TDR-G paragraphs removed; statements once, in §8; AZ-OPEN-SCOPE-ARITH and the "
                    "non-claims unchanged")
    d.sub("B4-note", "`[AZ-OPEN]` **AZ-OPEN-SCOPE-ARITH.**",
          "**v0.6 note:** the Phase-2 `4|q` angular result (§4.3.3) is NOT an answer to this question in the affirmative — it is proven to be substrate geometry",
          "The Phase-2 `4|q` angular result (§4.3.3) is NOT an answer to this question in the affirmative — it is shown to be substrate geometry",
          "version label; 'proven' -> 'shown' (the reclassification is `[NUM diagnostic]`, §4.3.3)")

    # ------------------------------------------------------------------ §4.3 Thread C
    d.set_line("S4.3-status", "**Status (v0.6):** Engineering **CERTIFIED**",
               "**Status:** Engineering certified (`[ENG PASS]`; availability of the certifying files in §9). One Phase-2 "
               "diagnostic produced and interpreted; it is a **negative-clarifying** result (a bridge-candidate disqualified), "
               "not a Level-B-promoting result. SG-AZ-4, SG-AZ-5, and SG-AZ-7 apply.",
               "version label and 'was engineering-blocked through v0.5' removed; availability pointer")
    p0 = d.find("`[THM-ALG]` **PROP-AZ-CORE-EQUIV — the export core equals DEF-AZ-CORE.**")
    p1 = d.find("Consequence: the uploaded export object labeled `Core(G_T)` (a 2-core) IS DEF-AZ-CORE")
    old = "\n".join(d.L[p0:p1])
    d.L[p0:p1] = block("05_prop_core_equiv.md").replace("@CHK_SHA@", chk_sha).rstrip("\n").split("\n")
    LOG.append(("D3", "replace-range", "%d lines, sha256 %s" % (p1 - p0, sha(old.encode())[:16]), "proof block",
                "[THM-ALG] -> [THM] on a written proof (PI decision D3 a); enumeration separated as corroboration; "
                "the reading of 'closed non-backtracking walk' made explicit"))
    d.sub("A5-heur-1", "**Not promoted:** the full \"$R_q$ elevated iff $4\\mid q$\" angular rule is NOT `[ALG]`.",
          "The connection from the low-order obstruction to the angular rule is `[HEUR/NUM strong]` only.",
          "The connection from the low-order obstruction to the angular rule is `[HEUR]` only; the numerical observations "
          "it rests on are the `[NUM diagnostic]` chains of §4.3.3.",
          "mixed tag unpacked (Methodology §8.4): heuristic link, numerical support named")
    d.sub("A5-heur-2", "The underlying mechanism is partly understood",
          "The full causal link to \"$R_q$ elevated iff $4\\mid q$\" is `[HEUR/NUM strong]`, not exact:",
          "The full causal link to \"$R_q$ elevated iff $4\\mid q$\" is `[HEUR]`, not exact:",
          "mixed tag unpacked; the same sentence already records the falsified prediction")
    i = d.find("#### §4.3.5 AZ-2 status")
    if d.L[i - 1] != "" or d.L[i - 2] != "```":
        die("unexpected lines before §4.3.5")
    d.L[i - 1:i - 1] = ["", "The block is kept as registered. Its spelling `[HEUR/NUM strong]` is the pre-migration form; the "
                        "current form of that statement is in §4.3.2 and §4.3.3."]
    LOG.append(("A5-heur-3", "insert", "", "one line after the retraction block",
                "the retraction block keeps its bytes (Methodology §8.4, historical spellings)"))
    d.sub("A5-result", "`[RESULT diagnostic]` **AZ-2 attempted; negative-clarifying. No Level B promotion.**",
          "`[RESULT diagnostic]`", "`[RESULT]` `[from: NUM]` `[scope: diagnostic]`", "RESULT pairing (Methodology §3.4)")
    d.sub("R1-AZ2", "The first angular-spectrum candidate (the Core(G_T) `4|q` rule) was tested and **disqualified as a bridge-candidate**",
          "the most tempting observable was shown to be substrate geometry that any antipodal-band $\\mathbb{Z}_N$ graph would exhibit.",
          "the most tempting observable was reproduced, in the tested null protocol (§4.3.3 Chain 2), by a core-matched "
          "random-$\\theta$ antipodal-band null without TDR-G dynamics, so it is not specific to the dynamics.",
          "review 5874174108 R1: universal quantifier removed; the negative verdict is kept at the scope of the evidence")
    d.set_line("S4.3.6-head", "#### §4.3.6 Scientific open items (Thread C) — revised", "#### §4.3.6 Scientific open items (Thread C)",
               "version label")
    d.sub("C3-gbirth", "`[OPEN]` **A dynamical (non-substrate) graph observable.**",
          "birth-window graph evolution (the $G_{\\rm birth}(w)$ sequence),",
          "birth-window graph evolution (the $G_{\\rm birth}(w)$ sequence; the object has two different definitions in the "
          "deposited files, §9, and has to be fixed before use),",
          "C3: the recovered material does not define G_birth(w) uniquely")

    # ------------------------------------------------------------------ §5
    d.sub("S5-eng", "| **Thread C engineering** |", "certified, exit-code-gated, hashed artifacts (§4.3.1, §9)**",
          "certified, exit-code-gated (§4.3.1); availability of the artifacts per entry in §9**", "availability")
    d.sub("S5-eng2", "| **Thread C engineering** |", "| SG-AZ-5 (revised) |", "| SG-AZ-5 |", "version label")
    d.sub("S5-prop", "| **PROP-AZ-CORE-EQUIV** |", "**`[THM-ALG]`, scope: finite simple undirected, both-orientations, no multiedges/self-loops**",
          "**`[THM]` (proof in §4.3.2), scope: finite simple undirected, both-orientations, no multiedges/self-loops; closed "
          "walks non-backtracking at every step including the closing one**", "tag form (D3); the reading the proof depends on")
    d.sub("S5-prop2", "| **PROP-AZ-CORE-EQUIV** |", "claiming strong connectivity of the transition graph |",
          "claiming strong connectivity of the transition graph; reading the enumeration certificate as the proof |",
          "forbidden overclaim added with D3")
    d.sub("S5-4q", "| **`4|q` angular rule** |", "**`[NUM diagnostic]` / `[HEUR/NUM strong]`: static $\\mathbb{Z}_N$ antipodal-band geometry**",
          "**`[NUM diagnostic]`: static $\\mathbb{Z}_N$ antipodal-band geometry; the link to the low-order obstruction is `[HEUR]`**",
          "mixed tag unpacked")
    d.sub("S5-gz", "| Graph-zeta diagnostics generally |", "| SG-AZ-5 (revised) |", "| SG-AZ-5 |", "version label")

    # ------------------------------------------------------------------ §6, §7
    i = d.find("**To Dyadic OPEN 9:**")
    old = d.L[i + 1]
    d.L[i + 1] = ("Thread A indexes the Dyadic arithmetic horizon by reference to %s (§8). The active arithmetic frontier "
                  "is the owner's (Dyadic §2 OPEN 9) and is not listed here." % DY_NEW)
    LOG.append(("B5", "set-line", "sha256 %s (%d chars)" % (sha(old.encode())[:16], len(old)), d.L[i + 1][:100],
                "restated owner frontier replaced by the pointer; pin (C5)"))
    d.sub("S6-bd", "**v0.6 [bridge-disqualified]:**", "**v0.6 [bridge-disqualified]:**", "**`[bridge-disqualified]`:**", "version label")
    d.sub("S6-uvm", "`[bridge-candidate]` The $p=6/K_4$ face-flux identity", "`[source: RTG_OPEN_M_DSN v0.7.1 R15, R16]`",
          "`[import: RTG_OPEN_M_DSN v0.7.1 R15, R16 | UVM-NUM-2F-RHO; UVM-RESULT-AUDIT1]` (reference only)",
          "[source:] -> [import:] (Methodology §3.3); same pin; identifiers as already named in the sentence")
    d.set_line("S7-head", "## §7. Note on Programme Overview Update", "## §7. Programme Registration", "title states the current function")
    d.sub("S7-hist", "`[DEF]` This study is registered in `RTG_PROGRAMME_OVERVIEW` v1.4",
          " The request carried through v0.6 that the Programme Overview be patched to register this study is met and closed; the proposed entry text is removed.",
          "", "history sentence; recoverable at az-v0.7")
    d.sub("S7-67", "`[DEF]` This study is registered in `RTG_PROGRAMME_OVERVIEW` v1.4",
          " The Programme's maintenance proposals for this study (its §6.7 and §9.2) are Programme records and are not adopted by this edition.",
          " The Programme's maintenance proposals for this study (its §6.7 and §9.2) are Programme records; the reduction of "
          "restated owner text asked for in its §6.7 is carried out in this edition by the PI's decision, and no merger "
          "with another study is made.", "state of the §6.7 item after this edition")

    # ------------------------------------------------------------------ §8 Import Ledger
    # Each row = the v0.7 ledger readout (bytes of the v0.7 §8 row) + limitation sentences taken
    # byte for byte from the v0.7 thread text (function frag). Glue is limited to the labels below.
    loc9 = "%s §2 OPEN 9" % DY_SRC
    loc611 = "%s §6.11" % DY_SRC
    locdef = "%s §2 OPEN 9 / §6.11 (located by identifier)" % DY_SRC

    def frag(line, start, end=None):
        end = start if end is None else end
        if line.count(start) != 1 or line.count(end) < 1:
            die("fragment %r / %r not found exactly" % (start[:50], end[:50]))
        a0 = line.index(start)
        b0 = line.index(end, a0) + len(end)
        return line[a0:b0]

    def readout(rid_prefix):
        """Second field of the v0.7 §8 row that starts with the given identifier text."""
        ln = bline("- [RID: %s" % rid_prefix)
        parts = ln.split(" :: ")
        if len(parts) < 3:
            die("ledger row %r has %d fields" % (rid_prefix, len(parts)))
        return parts[1], parts[2:]

    def row(rid, text, loc, tag, extra=None):
        out = ["- [RID: %s] :: %s :: %s :: %s" % (rid, text, loc, tag)]
        if extra:
            out.append("  " + extra)
        return out

    A = {k: bline(v) for k, v in {
        "cubic": "`[import-ref]` `[THM]` **Raw cubic theorem.**",
        "p6": "- $p=6$: $c_{05}^{(1,6)}",
        "gl5": "`[import-ref]` `[ALG]` **$p=5$ lattice cancellation.**",
        "g04": "`[import-ref]` `[ALG]` **$G_{04}(10)=0$ reinterpretation.**",
        "p12": "`[import-ref]` `[ALG]` **Cascade boundary $p=12$, $q=4$, $(0,3)$.**",
        "q4f": "`[import-ref]` `[FAIL]` **Universal $q=4$, $(0,3)$ cancellation.**",
        "p7": "`[import-ref]` `[FAIL]` **Prime-horizon first-lattice transparency.**",
        "proj": "`[import-ref]` `[ALG]` **Subgroup-charge projector formalism.**",
        "q403": "`[import-ref]` `[THM]` `[scope: all $p=4s$, $s\\ge2$]` **Cubic cascade",
        "b3": "`[import-ref]` `[ALG]` **Degree-3 raw-vanishing.**",
        "b4": "`[import-ref]` `[ALG]` **Degree-4 raw-vanishing.**",
        "b5": "`[import-ref]` `[ALG]` **Channel classification boundary at $b=4$ (dyadic map).**",
        "b5m": "- `[import-ref]` **The dyadic channel boundary at $b=4$.**",
        "dw": "`[import-ref]` `[ALG, exact]` **Direct-accumulation weight vanishing.**",
        "cx": "`[import-ref]` `[ALG, exact]` **Cyclotomic cross-term identity.**",
        "q3": "`[import-ref]` `[ALG]` `[conv: raw Birkhoff-strobe]` **Degree-2 $q=3$",
        "ff": "`[import-ref]` `[ALG, exact]` **$p=6$ / $K_4$ face-flux identity.**",
        "cor": "  `[COR v0.4]` Boundary precision:",
    }.items()}
    ffq = frag(A["ff"], "The identity is exact in Dyadic, but any transfer", "is not a Zeta result.")
    if ffq.count("remains `[CAND/conditional]` and") != 1:
        die("face-flux wording changed")
    ffq = ffq.replace("remains `[CAND/conditional]` and", "remains a conditional candidate in the owner documents and")
    cor04 = A["cor"].strip().replace("`[COR v0.4]` ", "")
    R = lambda k: readout(k)[0]

    dy = []
    dy += row("DYAD-THM-RAW-CUBIC", R("DYAD-THM-RAW-CUBIC]") + ". " + frag(A["cubic"], "It is not a statement about the raw $p$-step map.", "(Dyadic Appendix E)."),
              loc9, "`[THM]`")
    dy += row("DYAD-ALG-P567-LEDGER", R("DYAD-ALG-P567-LEDGER]") + " ($p=6$: "
              + frag(A["p6"], "in the one-step engine/DSN bridge convention; distinct from the raw six-step Lie-gauge coefficient") + ")",
              locdef, "`[ALG]`")
    dy += row("DYAD-ALG-GLATTICE5", R("DYAD-ALG-GLATTICE5]") + "; " + frag(A["gl5"], "both $F_1^5(0,4)$", "certified finite ledger."), loc611, "`[ALG]`")
    dy += row("DYAD-OPEN-P-RESONANCE", "items of the owner's OPEN 9 record (the sub-labels are not identifiers). "
              + "$G_{04}(10)=0$ reinterpretation `[ALG]`: " + frag(A["g04"], "Not divisor inheritance:", "`[scope: reframed]`.")
              + " Cascade boundary $p=12$, $q=4$, $(0,3)$ `[ALG]`: " + frag(A["p12"], "Exact value", "\\approx 0.0096$.")
              + " Universal $q=4$, $(0,3)$ cancellation `[FAIL]`: " + frag(A["q4f"], "Not universal;", "counterexample.")
              + " Prime-horizon first-lattice transparency `[FAIL]`: " + frag(A["p7"], "$G_{06}(7) \\neq 0$:", "counterexample.")
              + " Subgroup-charge projector / missing-slot formalism `[ALG]`: " + frag(A["proj"], "The closed cardinality lemma", "independent computation."),
              loc9, "owner tags per item, as printed")
    dy += row("DYAD-THM-Q403-PHASELAW", R("DYAD-THM-Q403-PHASELAW]") + "; " + frag(A["q403"], "$p=8$ is the zero degeneracy", "generic-$s$ formula."),
              loc611, "`[THM]` `[scope: all $p=4s$, $s\\ge2$]`")
    dy += row("DYAD-ALG-VANISH-B2", R("DYAD-ALG-VANISH-B2]"), locdef, "`[ALG]`")
    dy += row("DYAD-ALG-VANISH-B3", R("DYAD-ALG-VANISH-B3]") + ", " + frag(A["b3"], "by automatic $\\beta$-mode path enumeration;", "case alone."), locdef, "`[ALG]`")
    dy += row("DYAD-ALG-VANISH-B4", R("DYAD-ALG-VANISH-B4]") + ", " + frag(A["b4"], "by automatic $\\beta$-mode path enumeration;", "boundary."), locdef, "`[ALG]`",
              extra="For the three vanishing rows: " + cor04)
    b5r, b5x = readout("DYAD-ALG-B5-ALLP-NONVANISHING]")
    if len(b5x) != 2:
        die("B5 row fields")
    dy += row("DYAD-ALG-B5-ALLP-NONVANISHING", b5r + ". " + frag(A["b5"], "The all-$p$ $b=5$ failure is proved by", "finite scan.")
              + " No" + frag(A["b5m"], " \"iff $b\\le4$\" statement is made (the owner withdrew that shorthand)") + ".",
              loc611, "`[ALG]`; " + b5x[1])
    dy += row("DYAD-ALG-DIRECT-WEIGHT", R("DYAD-ALG-DIRECT-WEIGHT]") + ". " + frag(A["dw"], "Scope precision:", "closed lifecycle identifier)."),
              loc9, "`[ALG]` (exact)")
    dy += row("DYAD-ALG-CROSS-IDENTITY", R("DYAD-ALG-CROSS-IDENTITY]") + ". " + frag(A["cx"], "This exact cyclotomic sum cancellation is used", "clean range."),
              loc9, "`[ALG]` (exact)")
    dy += row("DYAD-ALG-Q3-DEG2-CANCEL", R("DYAD-ALG-Q3-DEG2-CANCEL]") + ". " + frag(A["q3"], "For all $p>3$ with $3\\mid p$,", "producing a selection rule."),
              loc611, "`[ALG]` `[conv: raw Birkhoff-strobe]`")
    dy += row("DYAD-ALG-P6-FACEFLUX", R("DYAD-ALG-P6-FACEFLUX]") + ". " + ffq, locdef, "`[ALG]` (exact)")

    locT = lambda sct: "%s %s" % (TD_SRC, sct)
    T = {k: bline(v) for k, v in {
        "zn": "`[bridge-candidate]` **$\\mathbb{Z}_N$ finite-state substrate.**",
        "reach": "`[bridge-candidate]` **Reachability / superselection.**",
        "retr": "`[bridge-candidate]` **Retrigger / binding threshold.**",
        "spec": "`[bridge-candidate]` **Advance-spectrum conservation.**",
        "bind": "`[bridge-candidate]` **BIND3 arithmetic/parity diagnostics.**",
        "f1": "`[bridge-candidate]` **$k/N$ and N-scaling.**",
        "f2": "$$B_{\\rm bulk}/\\text{step}",
        "f3": "at fixed $k/N=1/15$, $T=5000$",
        "t26": "`[bridge-candidate]` **TDR-26 birth-anchored discriminator.**",
        "t24": "`[bridge-candidate]` **TDR-24 frontier.**",
    }.items()}
    zr, zx = readout("TDRG-DEF-ZN-STATE]")
    bindr = readout("TDRG-ALG-BIND3-CYCLE-N24K1;")[0]
    td = []
    td += row("TDRG-DEF-ZN-STATE", zr + " (" + zx[-1] + ")" if len(zx) > 1 else zr, locT("§6.1"), "owner `[DEF]`")
    td += row("TDRG-DEF-PHYSICAL-STATE", R("TDRG-DEF-PHYSICAL-STATE]"), locT("§6.1"), "owner `[DEF]`")
    td += row("TDRG-DEF-BAND", R("TDRG-DEF-BAND]") + ". " + frag(T["zn"], "This gives Thread B a concrete arithmetic memory horizon $(N,k)$, but not yet a bridge to Dyadic $p$-resonance."),
              locT("§6.1"), "owner `[DEF]`")
    td += row("TDRG-ALG-LEM-REACH", R("TDRG-ALG-LEM-REACH]") + "; " + frag(T["reach"], "superselection persists at $k>0$ in the two-node universe."),
              locT("(located by identifier)"), "owner tags `[THM]` (the $k=0$ statement) and `[ALG]` (band form); `[scope: branch-local]`")
    td += row("TDRG-ALG-LEM-RETRIG", R("TDRG-ALG-LEM-RETRIG]") + ", " + frag(T["retr"], "possible iff $|d|_c\\le2k$.", "Dyadic resonance closure."),
              locT("(located by identifier)"), "owner `[ALG]`; `[scope: two-node TDR-G]`")
    td += row("TDRG-ALG-LEM-SPECCONS", R("TDRG-ALG-LEM-SPECCONS]") + " — " + frag(T["spec"], "the converse fails (owner counterexample", "source-scoped/open."),
              locT("(located by identifier)"), "owner `[ALG]`; `[scope: 3 nodes, no star blow-up]`")
    td += row("TDRG-ALG-BIND3-CYCLE-N24K1; TDRG-NUM-BIND3-PARITY; TDRG-NUM-BIND3-SPECTRAL-GATE; TDRG-NUM-BIND3-MEMORY-PARITY; "
              "TDRG-NUM-BIND3-XFER; TDRG-NUM-BIND3-REGEN; TDRG-OPEN-BIND3-NKSCAN",
              bindr + ". " + frag(T["bind"], "BIND3-KNIFE is `[FAIL]`/`[REPLACED]`, and the odd-sector memory claim is `[COR]` as a composition artifact."),
              locT("(located by identifier)"),
              "owner tags `[ALG]` (cycle enumeration) and `[NUM strong]` (the `NUM` identifiers); `[scope: N=24,k=1; no-birth/three-node]` "
              "`[conv: v18 path orientation]`; "
              + frag(T["bind"], "these numbers were computed with the orientation completion the owner has since superseded and are not rerun by the owner"))
    td += row("TDRG-OPEN-NSCALING; TDRG-OPEN-CRYSTALLIZATION",
              frag(T["f1"], "TDR-G v2.12.14 reports that $k/N$ controls entry into the growth regime", "bulk-conditioned birth rate") + " " + T["f2"][1:-1] + " "
              + frag(T["f3"], "at fixed $k/N=1/15$, $T=5000$", "not theorem-grade."),
              locT("§1"), "owner tags `[NUM]` (fit) and `[HEUR]` (limit); `[conv: v18 path orientation]`")
    td += row("TDRG-OPEN-LOCKING-FAIL", R("TDRG-OPEN-LOCKING-FAIL]") + " " + frag(T["t26"], "(combined TP=2, FP=0, FN=0, TN=198).", "not a bridge theorem."),
              locT("§2 OPEN TDR-26"), "owner tags as split in the statement")
    td += row("TDRG-OPEN-TOPO-FILTER; TDRG-OPEN-CHI-SCALING; TDRG-OPEN-THERMO-SUPPRESS",
              frag(T["t24"], "In TDR-G v2.12.14 the slot-volume identity (TDR-24D)", "bridge routing."),
              locT("§2"), "owner OPEN modules; mechanism-level closures as the statement says")

    e0 = d.find("### Bridge-required / bridge-disqualified export candidates")
    e1 = d.find("## §9. Artifact and Script Registry")
    exports = d.L[e0:e1]
    exports = [l.replace("engine now `[ENG PASS]`", "engine `[ENG PASS]`") for l in exports]
    if sum(l.count("engine `[ENG PASS]`") for l in exports) != 1:
        die("export row changed")

    s8 = ["## §8. Import Ledger", "",
          "This document makes no active cross-branch imports and no load-bearing import: no result of this DSN is derived "
          "from a row below. Each owner result is cited once, here; §1.2, §4.1, §4.2 and §6 refer to these rows. The Thread C internal results (§4.3.2) and the Phase-2 diagnostic (§4.3.3) are owned by "
          "this DSN and are not imports.", "",
          "Row format: identifier :: readout of the owner statement, with its limitations :: source edition and location :: owner "
          "tag and inherited scope. A readout is not the statement: the owner's text at the pinned edition governs. "
          "The remaining fields of Methodology §4.3 are the same for every row of a group and are given once, by key:", "",
          "- **IMP-A** (rows of the first group). Local use: reference-only index of Thread A (`[import-ref]`); no local "
          "consequence is derived. Depends on: the owner's definitions and conventions and the selected continuous generator "
          "(SG-PROG-2); no bridge is used or claimed (SG-AZ-3). Verification: owner statements read at `dyad-v6.4.23` for "
          "edition v0.7 (`EV-SRC-READ`; `records/az/AZ_v0_7_RELEASE_RECORD.md`); no owner artifact inspected or rerun "
          "(`EV-NOT-RERUN`). Synchronization: checked against `dyad-v6.4.24` — the difference between the two owner "
          "editions changes no statement of a cited identifier (it changes the owner's table of consumer strings, which "
          "names this document).",
          "- **IMP-B** (rows of the second group). Local use: branch-local context and `[bridge-candidate]` observable "
          "family of Thread B; not a cross-branch import (SG-PROG-1, SG-AZ-3, SG-AZ-0.4). Depends on: the owner's "
          "definitions, clock and orientation conventions as the owner states them; any use beyond branch-local context "
          "requires a named OPEN-P1 bridge, and none exists. Verification: owner statements read at `tdrg-v2.12.14` for "
          "edition v0.7 (`EV-SRC-READ`); no owner artifact inspected or rerun for these rows (`EV-NOT-RERUN`). "
          "Synchronization: `tdrg-v2.12.14` is the governing edition; nothing pending.", "",
          "### Reference imports from %s — clauses IMP-A" % DY_NEW, ""] + dy + ["",
          "### Branch-local context from %s (`tdrg-v2.12.14`) — clauses IMP-B" % TD_SRC, ""] + td + [""] + exports
    a8 = d.find("## §8. Import Ledger")
    b8 = d.find("## §9. Artifact and Script Registry")
    old = "\n".join(d.L[a8:b8])
    d.L[a8:b8] = s8
    LOG.append(("S8", "replace-range", "%d lines, sha256 %s" % (b8 - a8, sha(old.encode())[:16]), "%d lines" % len(s8),
                "Methodology §4.3 row form with group clauses; each row = the v0.7 ledger readout plus limitation sentences "
                "taken byte for byte from the v0.7 thread text (mixed tags unpacked to the owner's tags; pin C5); export "
                "candidates unchanged but for 'now'"))

    # ------------------------------------------------------------------ §9
    s9 = block("06_section9.md")
    for key, path in (("@REG@", "az_v5/benchmarks/AZ_ARTIFACT_REGISTRY.json"), ("@CONV@", "CONVENTIONS_FROZEN.md"),
                      ("@CERT@", "az_v5/az1b_certify.py"), ("@EXP@", "export/conv_az_graph_export.py"),
                      ("@SMOKE@", "phase2/AZ_PHASE2_N120_NULL1_smoke.json")):
        if s9.count(key) != 1:
            die("placeholder %s" % key)
        s9 = s9.replace(key, dep[path])
    if s9.count("@CHK_SHA@") != 1:
        die("placeholder @CHK_SHA@")
    s9 = s9.replace("@CHK_SHA@", chk_sha)
    d.replace_range("C1-C4", "## §9. Artifact and Script Registry", "## §10. Collaboration and Audit Record", s9,
                    "availability and evidence state per artifact after the partial recovery; conventions file as found; "
                    "two definitions of G_birth(w); exporter registered by its own identifier; new finite check registered")

    # ------------------------------------------------------------------ Appendix B
    i = d.find("*END OF DOCUMENT")
    if d.L[i - 1] != "" or d.L[i - 2] != "---" or d.L[i - 3] != "":
        die("unexpected lines before the footer")
    d.L[i - 3:i - 3] = [""] + block("07_appendix_b.md").rstrip("\n").split("\n")
    LOG.append(("APPB", "insert", "", "Corrections registered at v0.8", "correction records for the status and tag changes of this stage"))

    out = d.text()
    # ------------------------------------------------------------------ assertions on the result
    live_end = out.index("## §10. Collaboration and Audit Record")
    live = out[out.index("## Local Tag Aliases"):live_end]
    stale = []
    for bad in ("v6.4.23 (`dyad-v6.4.23`)", "[THM-ALG]", "[ENG-planned]", "[ENG-historical]", "[RESULT diagnostic]",
                "[source: ", "[ALG, exact]", "[CAND/conditional]", "in source]", "v0.6 note", "(v0.6", "v0.6 status",
                "REVISED v0.6", "(revised)", "v0.5", "[COR v0.4]", "*any* antipodal-band", "any antipodal-band $\\mathbb{Z}_N$ graph would",
                "It is proven static"):
        if bad in live:
            stale.append(bad)
            for m in re.finditer(re.escape(bad), live):
                sys.stderr.write("STALE %r: ...%s...\n" % (bad, live[max(0, m.start() - 90):m.end() + 60].replace("\n", " ")))
    if stale:
        die("stale strings survive in the live body: %s" % ", ".join(sorted(set(stale))))
    if live.count("[HEUR/NUM strong]") != 2:      # the retraction code block (1) and the line that explains it (1)
        die("[HEUR/NUM strong] count is %d" % live.count("[HEUR/NUM strong]"))
    rid = re.compile(r"\b(?:DYAD|TDRG|AZ|GEN|UVM|RTG|PROG)-[A-Z0-9][A-Z0-9-]*[A-Z0-9]\b|PROP-AZ-CORE-EQUIV|DEF-AZ-CORE|CONV-AZ-[A-Z-]+|SG-AZ-[0-9.]+|SG-PROG-[0-9]")
    lost = sorted(set(rid.findall(base.decode("utf-8"))) - set(rid.findall(out)))
    allowed_lost = set()
    if set(lost) - allowed_lost:
        die("identifiers lost: %s" % ", ".join(lost))
    if out.count("<!-- AI_CONTEXT_CORE_END -->") != 1:
        die("context-core marker")

    # protected regions: byte-identical to the base
    bt = base.decode("utf-8")

    def region(t, start, end):
        if t.count(start) != 1 or t.count(end) != 1:
            die("region markers %r / %r" % (start[:40], end[:40]))
        return t[t.index(start):t.index(end)]

    PROTECTED = [
        ("header", "# RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN_v0.7", "## Local Tag Aliases"),
        ("§4.1.3", "#### §4.1.3 Arithmetic-resonance observation", "### §4.2 Thread B"),
        ("§4.2 non-claims", "**What Thread B does not contain:**", "### §4.3 Thread C"),
        ("§4.3.1 engineering closure", "#### §4.3.1 Engineering closure", "#### §4.3.2 Internal graph-theoretic results"),
        ("§4.3.2 low-order obstruction, statement", "`[ALG]` **Antipodal-band low-order obstruction.**", "**Not promoted:** the full"),
        ("§4.3.3 chains", "**Chain 1 — Null0/Null1 statistical excess.**", "The underlying mechanism is partly understood"),
        ("§4.3.4 retraction block", "#### §4.3.4 Visible correction / retraction block", "[RETRACTED] falsified prediction"),
        ("§10", "## §10. Collaboration and Audit Record", "## Appendix A — Version History"),
        ("Appendix A", "## Appendix A — Version History", "## Appendix B — Retired and Rejected Claims"),
        ("Appendix B through v0.7", "## Appendix B — Retired and Rejected Claims", "### Corrections registered at v0.7"),
        ("footer", "*END OF DOCUMENT", "\x00"),
    ]
    prot = []
    for name, st, en in PROTECTED:
        if en == "\x00":
            x, y = bt[bt.index(st):], out[out.index(st):]
        else:
            x, y = region(bt, st, en), region(out, st, en)
        if x != y:
            die("protected region changed: %s" % name)
        prot.append((name, len(x.encode()), sha(x.encode())[:16]))

    with open(a.out, "w", encoding="utf-8", newline="") as f:
        f.write(out)
    with open(a.log, "w", encoding="utf-8") as f:
        f.write("AZ v0.8 stage 1 edit log\nbase %s %s\nresult sha256 %s, %d bytes\n\n" % (BASE_TAG, BASE_SHA, sha(out.encode()), len(out.encode())))
        f.write("Protected regions, byte-identical to the base:\n")
        for name, n, h in prot:
            f.write("    %-42s %6d bytes  sha256 %s\n" % (name, n, h))
        f.write("\n")
        for k, (key, op, old, new, note) in enumerate(LOG, 1):
            f.write("E%02d %-12s %-14s\n    old: %s\n    new: %s\n    why: %s\n" % (k, key, op, old[:300], new[:300], note))
    new_ids = sorted(set(rid.findall(out)) - set(rid.findall(base.decode("utf-8"))))
    print("base   %s" % BASE_SHA)
    print("result %s  %d bytes  (%d edits)" % (sha(out.encode()), len(out.encode()), len(LOG)))
    print("identifiers lost: none; new: %s" % (", ".join(new_ids) or "none"))
    print("protected regions byte-identical: %d (%d bytes)" % (len(prot), sum(n for _, n, _ in prot)))


if __name__ == "__main__":
    main()
