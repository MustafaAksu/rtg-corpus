#!/usr/bin/env python3
"""Informational size and structure report for a DSN (Methodology v1.4 §13.8).

    dsn_lint.py FILE [--prev PREVIOUS_EDITION] [--json OUT.json]

Reports; never blocks. No metric is a gate: there are no fixed size budgets.

Counting method
- bytes and lines of the UTF-8 file; characters for regions.
- regions: header = start of file to the first "## " heading; live body = header end to
  "## Appendix A" plus "## Appendix B" to the footer; Appendix A = its own region.
- §1 words: whitespace-separated tokens between the "## §1." heading and the next "## " heading.
- RIDs: registered-namespace identifiers (pattern in check_compaction.py); new RIDs = RIDs in
  FILE absent from PREVIOUS_EDITION.
- header fields: characters per "**Field:**" line of the header.
- Appendix A words per edition: tokens under each "### v…" heading.
- history phrases: case-insensitive counts in the live body of the phrases in HISTORY.
- orientation core (Methodology v1.4 §6.1): "## §1." up to "## §5." for a standard technical
  ledger; characters, lines and words; whether the AI_CONTEXT_CORE_END marker is present.
- near-duplicates: paragraphs of at least 200 characters whose 8-word shingle sets have
  Jaccard similarity >= 0.8 with another paragraph of the live body.
"""
import argparse, json, re, sys, os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from check_compaction import RE_RID  # noqa: E402

HISTORY = ["kept as history", "previous wording", "overlay", "relocated", "was:", "historical",
           "superseded", "former", "retained as", "no longer"]


def regions(s):
    h = s.index("\n## ")
    a = s.find("\n## Appendix A"); b = s.find("\n## Appendix B")
    foot = s.find("\n*END OF DOCUMENT")
    body = s[h:a] + (s[b:foot] if b > 0 else "") if a > 0 else s[h:foot]
    appA = s[a:b] if a > 0 and b > a else ""
    return s[:h], body, appA


def section(s, head):
    i = s.find("\n" + head)
    if i < 0:
        return ""
    j = s.find("\n## ", i + 1)
    return s[i:j if j > 0 else len(s)]


def shingles(t, n=8):
    w = t.split()
    return {" ".join(w[i:i + n]) for i in range(max(0, len(w) - n + 1))}


def report(path, prev=None):
    s = open(path, encoding="utf-8").read()
    raw = open(path, "rb").read()
    head, body, appA = regions(s)
    r = {"file": path, "bytes": len(raw), "lines": s.count("\n"),
         "header_chars": len(head), "live_body_chars": len(body), "appendix_a_chars": len(appA)}
    r["counting_method"] = __doc__.split("Counting method", 1)[1].strip()
    r["section1_words"] = len(section(s, "## §1.").split()) - 4
    i, j = s.find("\n## §1."), s.find("\n## §5.")
    core = s[i:j] if i >= 0 and j > i else ""
    r["orientation_core"] = {"chars": len(core), "lines": core.count("\n"), "words": len(core.split()),
                             "core_end_marker_present": "AI_CONTEXT_CORE_END" in s}
    r["header_fields"] = {m.group(1): len(m.group(0)) for m in re.finditer(r"^\*\*([^*]+):\*\*.*$", head, re.M)}
    eds = re.split(r"\n### (v[0-9][^\n]*)", appA)
    r["appendix_a_words_per_edition"] = {eds[i]: len(eds[i + 1].split()) for i in range(1, len(eds) - 1, 2)}
    r["footer_lines"] = len(re.findall(r"^\*END OF DOCUMENT", s, re.M))
    low = body.lower()
    r["history_phrases_live"] = {p: low.count(p) for p in HISTORY if low.count(p)}
    paras = [p for p in re.split(r"\n\s*\n", body) if len(p) >= 200]
    sh = [shingles(p) for p in paras]
    dup = []
    for i in range(len(paras)):
        for j in range(i + 1, len(paras)):
            a, b = sh[i], sh[j]
            if a and b:
                jac = len(a & b) / len(a | b)
                if jac >= 0.8:
                    dup.append({"similarity": round(jac, 3), "a": paras[i][:90], "b": paras[j][:90]})
    r["near_duplicate_paragraphs"] = dup
    rids = set(RE_RID.findall(s))
    r["rids_total"] = len(rids)
    if prev:
        p = open(prev, encoding="utf-8").read()
        pb = len(open(prev, "rb").read())
        prids = set(RE_RID.findall(p))
        new = sorted(rids - prids)
        r["previous"] = {"file": prev, "bytes": pb}
        r["growth_bytes"] = len(raw) - pb
        r["growth_percent"] = round(100.0 * (len(raw) - pb) / pb, 1)
        r["new_rids"] = new
        r["growth_per_new_rid"] = round((len(raw) - pb) / len(new), 1) if new else "N/A"
    return r


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("file"); ap.add_argument("--prev"); ap.add_argument("--json")
    a = ap.parse_args()
    r = report(a.file, a.prev)
    if a.json:
        json.dump(r, open(a.json, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    for k, v in r.items():
        if k == "counting_method":
            continue
        if isinstance(v, (dict, list)):
            if k == "counting_method":
                continue
            if k in ("near_duplicate_paragraphs", "new_rids"):
                print(f"{k}: {len(v)}")
            elif k == "appendix_a_words_per_edition":
                print(f"{k}: {len(v)} editions, max {max(v.values()) if v else 0} words")
            else:
                print(f"{k}: {json.dumps(v, ensure_ascii=False)}")
        else:
            print(f"{k}: {v}")
    print("(informational report; no gate)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
