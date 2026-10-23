#!/usr/bin/env python3
"""Programme Overview v1.3, stage 2: layout-only compaction of the reviewed stage-1 intermediate.

Operations (Methodology v1.4 §13.6; checked by tools/check_compaction.py with the Programme profile):
  M01 ref-subst   §2.1 "See Appendix C, PREL." -> points to Appendix C of v1.2 (tag programme-v1.2)
  M02 ref-subst   §6.4 "Its Appendix C" (TDR-G's) -> names the TDR-G tag so the reference resolves
  M03 history-appendix  Appendix A -> one compact entry per edition; full entries at tag programme-v1.2
                        and, for the stage-1 draft entry, at the stage-1 commit
  M04 history-section   Appendix C (v1.2 package ledger: inspected locations, package paths, validation scope)
                        -> removed; it lives at tag programme-v1.2. §6.1 and BASELINE.md carry the current editions.
Not moved: Appendix B (adopted replacements of v1.1 statements). It carries claim-tag spellings inside prose
(`[HYP]`, `[HEUR strong]`), which the compaction tool refuses to relocate outside table rows; it stays in the
live file and is listed in the release record as carried history.

usage (repository root): build_programme_v1_3_stage2.py INTERMEDIATE OUT_CANDIDATE OUT_MAP
"""
import hashlib, json, subprocess, sys

INTER_SHA = "08a236c0eb3d0171be2884ce672ff7701711d3db4b5483ca375fe0293845b8d9"
STAGE1_COMMIT = "c1deb5f"

def sha(s): return hashlib.sha256(s.encode("utf-8") if isinstance(s, str) else s).hexdigest()

APPA = """
## Appendix A — Version History

One compact entry per edition (Methodology v1.4 §1.1). Full entries of v1.0–v1.2, the Draft 1 history of v1.2 and the adopted replacement ledger's provenance are in Appendix A of v1.2 (tag `programme-v1.2`); the full stage-1 draft entry of v1.3 is at the stage-1 commit named in the release record.

### v1.3 — 23 October 2026 — DRAFT candidate

- **Basis:** atlas advisory `records/programme/ATLAS_ADVISORY_PROGRAMME_v1_2.md` as disposed by the PI on 23 October 2026 (its §5); Methodology v1.4.
- **Inventory and interfaces:** governing editions by tag for every home; class column; new rows for RRF (adopted working standard), RER, FMS, ER-2B (noncanonical) and the State Atlas (derived map); §6.2–6.5 reduced to custody and interface records pointing to the owners' status summaries; §7 pins at governing tags or labelled consumer pins; IF17 retired as a transfer proposal; IF26–IF36 added.
- **Pointers:** OFN v0.10 and RRF v0.8.4 as criterion homes for P0 and P2B; OPEN M v0.7.1 for P3; §8.2 cross-stream κ table; §9.2 maintenance record with the remaining queue (Pre-Legacy, TDR-G, DZT, AZ); §9.3 repository-based evidence and adoption.
- **Compaction [layout]:** compact Appendix A; Appendix C of v1.2 left at tag `programme-v1.2`; Appendix B retained (see release record).
- **Unchanged:** architecture, maturity semantics and the v1.1 maturity records, the five programme OPEN RIDs (all ACTIVE), SG-PROG-1–4, the restructuring queue, the TDR-T launch-gate record.
- **Records:** `records/programme/RTG_PROGRAMME_OVERVIEW_v1_3_RELEASE_RECORD.md`; v1.2 release and change records recorded as missing.

### v1.2 — 20 September 2026 — Adopted

- Inventory/architecture release under Methodology v1.3: 14-home inventory, typed interfaces IF01–IF25, maturity semantics, OPEN-P closure criteria, scope guards SG-PROG-1–4 clarified (P12-P1–P12-P4 accepted by the PI). No scientific claim promoted, demoted or closed. Full entry and Draft 1 history: tag `programme-v1.2`.

### v1.1 — June 2026

- Four OPEN clusters; $T$ as postulated effective generator until OPEN-P0 closes; discrete wording corrected; filenames updated to the June editions. Full entry: tag `programme-v1.2`.

### v1.0 — June 2026

- Initial release from the RTG hierarchy analysis and the multi-AI design review: OPEN-P0–P3, maturity ladder, SG-PROG-1–4, five-tier hierarchy, dependency graph. Full entry: tag `programme-v1.2`.

"""

def main(inter_path, out_path, map_path):
    s = open(inter_path, encoding="utf-8").read()
    assert sha(s) == INTER_SHA, "input is not the stage-1 intermediate"
    base_sha = sha(s)
    ops = []

    def edit(i, old, new, archive, note):
        nonlocal s
        assert s.count(old) == 1, (i, old[:60])
        s = s.replace(old, new)
        ops.append(dict(id=i, op="edit", **{"class": "ref-subst"}, old=old, new=new, archive=archive, note=note))

    def replace_section(i, cls, start, end, new, archive, note):
        nonlocal s
        a = s.find(start); assert a >= 0 and s.count(start) == 1, (i, start)
        b = s.find(end, a + len(start)); assert b >= 0, (i, end)
        s = s[:a] + new + s[b:]
        ops.append(dict(id=i, op="replace-section", **{"class": cls}, start=start, end=end, new=new, archive=archive, note=note))

    edit("M01", "See Appendix C, PREL.", "See Appendix C of v1.2 (tag `programme-v1.2`), PREL.", ["programme-v1.2"],
         "the v1.2 reference ledger stays at its tag")
    edit("M02", "Its Appendix C still carries an older D/A/B gate", "Its Appendix C (at `tdrg-v2.12.13`) still carries an older D/A/B gate", ["programme-v1.2"],
         "TDR-G's own appendix; the tag makes the reference resolvable after the Programme's Appendix C is gone")
    replace_section("M03", "history-appendix", "\n## Appendix A — Version History", "\n---\n\n<a id=\"prog-corrections\"></a>", APPA,
                    ["programme-v1.2", "programme-v1.3-stage1"], "compact Appendix A; full entries at tag programme-v1.2 and at the stage-1 commit")
    replace_section("M04", "history-section", "\n<a id=\"prog-sources\"></a>\n## Appendix C — Versioned Reference Ledger and Verification Scope",
                    "\n---\n\n*END OF DOCUMENT", "", ["programme-v1.2"],
                    "v1.2 package ledger (inspected locations, package paths, validation scope); current editions are §6.1 and BASELINE.md")

    tags = subprocess.run(["git", "tag"], check=True, capture_output=True).stdout.decode().split()
    stage1_full = subprocess.run(["git", "rev-parse", STAGE1_COMMIT], check=True, capture_output=True).stdout.decode().strip()
    mp = {
        "study": "PROG", "target": "v1.3", "stage": "compaction",
        "base": f"corrected intermediate (stage 1; commit {STAGE1_COMMIT})", "base_sha256": base_sha,
        "archives": [
            {"name": "programme-v1.2", "git": "programme-v1.2:dsn/RTG_PROGRAMME_OVERVIEW.md",
             "sha256": "4207da05dca24256e7bc528cb9814f848838bcd98e3d01222fb2a633ec9fd359",
             "role": "adopted predecessor; holds Appendices A-C of v1.2 and every relocated passage"},
            {"name": "programme-v1.3-stage1", "git": f"{stage1_full}:dsn/RTG_PROGRAMME_OVERVIEW.md",
             "sha256": INTER_SHA, "role": f"reviewed stage-1 intermediate (commit {STAGE1_COMMIT}); holds the full stage-1 Appendix A entry"},
        ],
        "profile": {"study": "PROG", "ref_words": ["PREL"], "history_words": [],
                    "checked_tag_prefixes": ["programme-"], "known_tags": sorted(tags), "summary_from": ["header"]},
        "operations": ops, "candidate_sha256": sha(s),
    }
    open(out_path, "w", encoding="utf-8").write(s)
    json.dump(mp, open(map_path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(sha(s), len(s), "bytes;", len(ops), "operations")

if __name__ == "__main__":
    main(*sys.argv[1:4])
