#!/usr/bin/env python3
"""Publication transform for Programme Overview v1.4: status lines only (header Document status, Appendix A heading,
footer). Run on the reviewed candidate after the PI's adoption; nothing else changes.

usage (repository root):
  python -I evidence/programme/scripts/release_programme_v1_4.py CANDIDATE OUT ADOPTION_DATE
  e.g. ADOPTION_DATE = "4 November 2026"
"""
import hashlib, sys

def sha(s): return hashlib.sha256(s.encode("utf-8")).hexdigest()

def main():
    cand, out, date = sys.argv[1], sys.argv[2], sys.argv[3]
    t = open(cand, encoding="utf-8").read()
    reps = [
        ("**Document status:** DRAFT — v1.4 candidate (one content stage; no compaction); not adopted. `programme-v1.3` governs until adoption.",
         f"**Document status:** ADOPTED — PI, {date} (maintenance synchronization of the adopted v1.3 under Methodology v1.4; adoption record `records/programme/RTG_PROGRAMME_OVERVIEW_v1_4_RELEASE_RECORD.md`). Supersedes `programme-v1.3`."),
        ("### v1.4 — 4 November 2026 — DRAFT (candidate; not adopted)", f"### v1.4 — {date} — Adopted"),
        ("*END OF DOCUMENT — RTG_PROGRAMME_OVERVIEW_v1.4 (DRAFT candidate, 4 November 2026; maintenance synchronization of the adopted v1.3 under DSN Methodology v1.4).*",
         f"*END OF DOCUMENT — RTG_PROGRAMME_OVERVIEW_v1.4 (ADOPTED, {date}; maintenance synchronization of the adopted v1.3 under DSN Methodology v1.4).*"),
    ]
    for old, new in reps:
        assert t.count(old) == 1, f"status line not found exactly once: {old[:60]}"
        t = t.replace(old, new)
    open(out, "w", encoding="utf-8", newline="").write(t)
    print(f"candidate {sha(open(cand, encoding='utf-8').read())} -> adopted {sha(t)}")

if __name__ == "__main__":
    main()
