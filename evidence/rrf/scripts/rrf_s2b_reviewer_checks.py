#!/usr/bin/env python3
"""RRF S2b reviewer checks (Claude; read-only; independent of check_rrf_s2b.py).

Run in a checkout of the S2b candidate head:
  python -I evidence/rrf/scripts/rrf_s2b_reviewer_checks.py [--base 98da97c3...]
Checks (exit 0 iff C1-C5 pass; C6 is a report):
 C1 token loss S2a->candidate: every lost identifier/guard/evidence-name/hash token occurs only in
    spans the movement map classifies as archive (else FAIL).
 C2 import coverage: every live (non-archived) S2a line with an [import: ...] tag is in import_use_index,
    and every import tag lost from the candidate occurs only in archived spans.
 C3 owner-grade readouts in the import ledger ("Current <STUDY> v<x> L<n>: [GRADE]") are on the cited
    owner line, together with the cited RID.
 C4 archive base reachability: the map's base commit is an ancestor of HEAD.
 C5 negative control: a ledger readout with a wrong grade is detected by C3.
 C6 report: archive spans that also occur verbatim in rrf-v0.8.4 (tag-retrievable) vs only in the base commit.
"""
import argparse, json, re, subprocess, sys
OWN = {'DYAD': 'dsn/RTG_DYADIC_OSCILLATOR_DSN.md', 'RECOG': 'dsn/RTG_RELATIONAL_RECOGNITION_DSN.md',
       'OFN': 'dsn/RTG_ONTOLOGICAL_FOUNDATIONS.md', 'GEN': 'dsn/RTG_GENESIS_GEOMETRY_DSN.md',
       'TRIAD': 'dsn/RTG_TRIADIC_BIRTH_LIFT_DSN.md', 'NUMGEN': 'dsn/RTG_NUMBER_GENESIS_DSN.md',
       'TDRG': 'dsn/RTG_DISCRETE_GENESIS_DSN.md', 'UVM': 'dsn/RTG_OPEN_M_DSN.md',
       'RER': 'noncanonical/RTG_RELATIONAL_EMERGENCE_REGISTRY.md'}
PATS = [r"\b[A-Z][A-Z0-9]*(?:-[A-Z0-9]+){2,}\b", r"\bSG-[A-Z0-9-]+\b", r"\bRF-O\d+-\d+\b", r"\bOPEN-[A-Z0-9-]+\b",
        r"\b[\w.-]+\.(?:zip|json|jsonl|py|md)\b", r"\b[0-9a-f]{64}\b"]
fails = []
def check(name, ok, info=""):
    print(("PASS " if ok else "FAIL ") + name + (" " + info if info else "")); (fails.append(name) if not ok else None)
def git(*a): return subprocess.check_output(["git", *a]).decode("utf-8")
def grade_rows(text):
    out = []
    for r in text.split("\n"):
        if not r.startswith("| I-"): continue
        cells = [c.strip() for c in r.strip("|").split("|")]
        rid = re.search(r"RID: ([A-Z][A-Z0-9-]+)", cells[1])
        for m in re.finditer(r"Current (\w+) v[\d.]+ L(\d+): (\[[^\]]+\])", cells[2]):
            out.append((cells[0], m.group(1), int(m.group(2)), m.group(3), rid.group(1) if rid else None))
    return out
def grade_ok(rows, cache):
    bad = []
    for key, st, ln, g, rid in rows:
        line = cache[st][ln - 1] if st in cache and ln <= len(cache[st]) else ""
        if g not in line or (rid and rid not in line): bad.append(key)
    return bad
def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--map", default="evidence/rrf/v0.9/s2b_movement_map.json")
    a = ap.parse_args()
    m = json.load(open(a.map, encoding="utf-8"))
    base_ref = m["base"]["git"]; base_commit = base_ref.split(":")[0]
    b = git("show", base_ref); c = open(m["candidate"]["path"], encoding="utf-8").read()
    v084 = git("show", "rrf-v0.8.4:dsn/RTG_RRF_REPRESENTATION_REGISTRY.md")
    bl = b.split("\n"); arch = set()
    for o in m["operations"]:
        if o["kind"] == "archive": arch.update(range(o["source"][0], o["source"][1] + 1))
    lost = {}
    for p in PATS:
        for t in set(re.findall(p, b)):
            if t not in c: lost[t] = [i for i, l in enumerate(bl, 1) if t in l]
    nonarch = sorted(t for t, ls in lost.items() if not all(i in arch for i in ls))
    check("C1 lost tokens only in archived spans", not nonarch, f"lost={len(lost)} outside-archive={nonarch}")
    live = {i for i, l in enumerate(bl, 1) if i not in arch and "[import:" in l}
    idx = {u["source_line"] for u in m["import_use_index"]}
    lost_imp = [t for t in set(re.findall(r"\[import: [^\]]+\]", b)) if t not in c]
    bad_imp = [t for t in lost_imp if not all(i in arch for i, l in enumerate(bl, 1) if t in l)]
    check("C2 live import lines indexed", not (live - idx), f"live={len(live)} unindexed={sorted(live - idx)}")
    check("C2 lost import tags only archived", not bad_imp, f"lost={len(lost_imp)}")
    cache = {k: open(v, encoding="utf-8").read().split("\n") for k, v in OWN.items()}
    rows = grade_rows(c); bad = grade_ok(rows, cache)
    check("C3 owner-grade readouts on cited owner line", rows and not bad, f"readouts={len(rows)} bad={bad}")
    anc = subprocess.run(["git", "merge-base", "--is-ancestor", base_commit, "HEAD"]).returncode == 0
    check("C4 archive base commit is ancestor of HEAD", anc, base_commit[:12])
    neg = [(k, s, l, "[SPEC]" if g != "[SPEC]" else "[THM]", r) for k, s, l, g, r in rows[:1]]
    check("C5 negative control: wrong grade detected", bool(grade_ok(neg, cache)))
    for o in m["operations"]:
        if o["kind"] == "archive":
            s, z = o["source"]; txt = "\n".join(bl[s - 1:z])
            print(f"INFO C6 {o['id']} L{s}-{z}: {'verbatim in rrf-v0.8.4' if txt in v084 else 'base commit only'}")
    sys.exit(1 if fails else 0)
if __name__ == "__main__": main()
