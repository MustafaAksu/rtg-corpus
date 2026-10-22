#!/usr/bin/env python3
"""release_v6_4_20.py -- deterministic release transform: v6.4.20 DRAFT r2 (reviewed) -> adopted RTG_DYADIC_OSCILLATOR_DSN_v6_4_20.md.

Authority: external review `DYAD v6.4.20 DRAFT r2 — REVIEW ACCEPTED` (21 Oct 2026) and the PI's explicit owner adoption of
21 Oct 2026 (recorded as `DYAD v6.4.20 — OWNER ADOPTION AUTHORIZED`).
Scope: labels and metadata only.
  L1  MAPS: the "proposed / registered only at adoption" markers of the 13 new RIDs become "registered at adoption" forms
  L2  LINE_EDITS: header (Edition, Status, Supersedes, status summary, record pointer), section 7.0 Dyadic and P1 rows and intro,
      notice-table intro, section 8 ATLAS-P2 row, Appendix E intro, Appendix F/G wording, footer
  L3  Appendix A: new "v6.4.20 — adopted 21 October 2026" record before the DRAFT r2 record, quoting every replaced r2 line
Every edit outside the new record is an in-place single-line replacement; Appendix A history is not touched.
No statement, grade, scope, OPEN status, constant or RID changes.
Usage: python -B release_v6_4_20.py DRAFT_r2.md OUT.md   (writes release_v6_4_20_log.json next to OUT)
"""
import sys, os, json, hashlib
sys.dont_write_bytecode = True

R2_HASH = 'f2030f853b94a7caa1d1d7c4afd8bdf9b6059582d331100bb0033226fd68465e'
V619 = '40c9e63f14baef581db9ef4a362ea8f8ac1f124c9f29a63f6b1c3f8931686ec9'
P1_HASH = '6f30f347b4f896a512cc7f1018d57721e33889d70e039fbb69377770fdc2c905'
R1_HASH = 'a5c70f5b1468ab01ba1cdf932fb9205c4bf00976a2b6523e8b90210e5e457c4a'
DECISION = '`DYAD v6.4.20 — OWNER ADOPTION AUTHORIZED`'
REVIEW = '`DYAD v6.4.20 DRAFT r2 — REVIEW ACCEPTED`'
REG = 'RID registered at adoption, 21 Oct 2026'

MAPS = [  # applied to every line outside Appendix A, in this order
    ('`[v6.4.20 entry; proposed RID, registered only at adoption]`', '`[v6.4.20 entry; ' + REG + ']`'),
    ('`[v6.4.20; proposed RID for the b=5 statement (F_raw^p(0,5) != 0 for every p >= 6), registered only at adoption;',
     '`[v6.4.20; RID for the b=5 statement (F_raw^p(0,5) != 0 for every p >= 6), registered at adoption, 21 Oct 2026;'),
    ('`[v6.4.20; proposed RID, registered only at adoption', '`[v6.4.20; ' + REG),
    ('`[v6.4.20: result RID proposed, DYAD-ALG-B5-ALLP-NONVANISHING (§6.11);', '`[v6.4.20: result RID registered at adoption, DYAD-ALG-B5-ALLP-NONVANISHING (§6.11);'),
    (' — proposed, not adopted |', ' — new in v6.4.20 |'),
    ('| proposed RID', '| new RID (v6.4.20)'),
]
LINE_EDITS = [  # (line prefix identifying exactly one line, old substring, new substring)
    ('**Edition:** v6.4.20 DRAFT r2', '**Edition:** v6.4.20 DRAFT r2 — 21 October 2026', '**Edition:** v6.4.20 — adopted 21 October 2026'),
    ('**Status:** DRAFT r2 — not adopted', None,
     '**Status:** ADOPTED — owner/PI adoption recorded 21 October 2026 (' + DECISION + ') after external review of DRAFT r2 (' + REVIEW +
     '; r2 SHA-256 `' + R2_HASH + '`). Earlier reviews: `ATLAS P1 — SCIENTIFIC REVIEW ACCEPTED` (P1 working file `' + P1_HASH +
     '`) and `v6.4.20 r1 — REVIEW ACCEPTED WITH MINOR CORRECTIONS` (r1 `' + R1_HASH + '`). Built by `build_dyad_v6_4_20_r1.py` (P1 → r1), '
     '`build_dyad_v6_4_20_r2.py` (r1 → r2) and `release_v6_4_20.py` (r2 → this file, labels and metadata only). '
     'Release record: `RTG_DYADIC_v6_4_20_RELEASE_RECORD.md`; external verification of this file\'s SHA-256 is recorded separately.  '),
    ('**Supersedes (on adoption only):**', '**Supersedes (on adoption only):** `RTG_DYADIC_OSCILLATOR_DSN_v6.4.19`.',
     '**Supersedes:** `RTG_DYADIC_OSCILLATOR_DSN_v6.4.19` (adopted 20 Oct 2026, `' + V619 + '`; kept unchanged as the historical adopted release).'),
    ('**Status summary:**', 'This draft adds the ATLAS P1 scientific corrections and the P2 interface work (Appendix A). Proposed RIDs are registered only on adoption; no adopted RID is renamed or regraded.',
     'v6.4.20 adds the ATLAS P1 scientific corrections and the P2 interface work (Appendix A). Its 13 new RIDs are registered by this adoption; no earlier RID is renamed or regraded.'),
    ('**Draft record:** Appendix A,', '**Draft record:** Appendix A, "v6.4.20 DRAFT r2" and "v6.4.20 DRAFT r1";',
     '**Adoption and draft records:** Appendix A, "v6.4.20 — adopted 21 October 2026", "v6.4.20 DRAFT r2" and "v6.4.20 DRAFT r1";'),
    ('**Version markers.** `[v6.4.20]` marks text', 'a proposed RID carries', 'a RID new in v6.4.20 carries'),
    ('`[DEF]` `[v6.4.20]` One table of the editions this ledger uses.', 'computed from the project file for this draft;',
     'computed from the project file during the v6.4.20 draft work;'),
    ('| Dyadic (this ledger) | v6.4.19 |', '| ADOPTED 20 Oct 2026; canonical until a v6.4.20 adoption decision |',
     '| ADOPTED 20 Oct 2026; superseded by v6.4.20 (this edition, adopted 21 Oct 2026; its SHA-256 is in `RTG_DYADIC_v6_4_20_RELEASE_RECORD.md`) |'),
    ('| Dyadic ATLAS P1 working file |', '| base of this draft |', '| base of the v6.4.20 drafts |'),
    ('`[DEF]` `[v6.4.20]` One recipient per row.', 'names the consumer record read for this draft;', 'names the consumer record read for this edition;'),
    ('`[DEF]` `[v6.4.20]` One recipient per row.', 'are issued only after adoption; none is prepared in this draft.',
     'are prepared only after external verification of this edition\'s SHA-256; none is prepared in this edition.'),
    ('- [RID: DYAD-ART-ATLAS-P2]', ':: this draft: builders,', ':: the v6.4.20 drafts: builders,'),
    ('`[DEF]` `[v6.4.20]` One row per result or definition identifier', '(adopted and proposed)', '(including those new in v6.4.20)'),
    ('`[DEF]` `[v6.4.20]` One row per result or definition identifier', 'proposed identifiers read "— proposed, not adopted".',
     'identifiers registered at the v6.4.20 adoption read "— new in v6.4.20" (in r2: "— proposed, not adopted").'),
    ('`[DEF]` `[v6.4.20]` Every Dyadic-pattern string printed in DZT', 'consumer repins are requested after adoption (planned notice N17).',
     'consumer repins are requested by planned notice N17, after external verification of this edition\'s SHA-256.'),
    ('| DZT v0.8 §7 | DYAD-OPEN-B5-ALLP |', '| result RID proposed: `DYAD-ALG-B5-ALLP-NONVANISHING` |', '| result RID registered at v6.4.20 adoption: `DYAD-ALG-B5-ALLP-NONVANISHING` |'),
    ('| AZ v0.6 §8 | DYAD-ALG-Q3-CANCEL |', '| proposed `DYAD-ALG-Q3-DEG2-CANCEL` covers the statement; no alias is created; AZ may repin after adoption |',
     '| `DYAD-ALG-Q3-DEG2-CANCEL` (registered at v6.4.20 adoption) covers the statement; no alias is created; AZ may repin |'),
    ('`[DEF]` `[v6.4.20]` Every v6.4.19 heading and its place in this draft.', 'its place in this draft.', 'its place in this edition.'),
    ('| v6.4.19 | v6.4.20 DRAFT r2 (headings as in r1) | Change |', '| v6.4.20 DRAFT r2 (headings as in r1) |', '| v6.4.20 (headings as in r1) |'),
    ('| `## Appendix A — Version History {#appendix-a}` |', '| v6.4.20 DRAFT r2 and r1 records added;', '| v6.4.20 adoption record, DRAFT r2 and r1 records added;'),
    ('*END OF DOCUMENT — RTG_DYADIC_OSCILLATOR_DSN_v6.4.20 DRAFT r2*', 'v6.4.20 DRAFT r2*', 'v6.4.20*'),
    ('*DRAFT r2, 21 October 2026 — not adopted, not released.', None,
     '*Adopted 21 October 2026; supersedes RTG_DYADIC_OSCILLATOR_DSN_v6.4.19 (adopted 20 October 2026). v6.4.20 carries the ATLAS P1 scientific corrections and the P2 interface work; '
     'it registers 13 new RIDs and changes no earlier grade or OPEN status (OPEN 20 PARTIAL; B-an, B-6 OPEN). The replaced DRAFT r2 lines, including its footer, are quoted in Appendix A '
     '(v6.4.20 adoption record); the r1 footer is in the DRAFT r2 record, the v6.4.19 and inherited footers in the r1 record (H-P2-12).*'),
]
NEW_RIDS = ['DYAD-ALG-KP-FRAME-SCALE', 'DYAD-THM-SMOOTH-EQUIVARIANT-CHART', 'DYAD-ALG-B5-ALLP-NONVANISHING', 'DYAD-ALG-RAW-ANGULAR-MEAN',
            'DYAD-ALG-ONE-BLOCK-BURST', 'DYAD-ALG-P5-RADIAL', 'DYAD-ALG-SIXSTEP-CUBIC-JET', 'DYAD-ALG-Q3-DEG2-CANCEL', 'DYAD-DEF-CRITICAL-CURVE',
            'DYAD-ALG-QC-CRITICAL-AMPLITUDE', 'DYAD-ALG-ISP-MAPS', 'DYAD-ART-ATLAS-P1', 'DYAD-ART-ATLAS-P2']


def sha(b): return hashlib.sha256(b).hexdigest()


def main():
    src, out = sys.argv[1], sys.argv[2]
    raw = open(src, 'rb').read(); assert sha(raw) == R2_HASH, 'r2 identity'
    L = raw.decode('utf-8').split('\n')
    a_idx = next(i for i, l in enumerate(L) if l.startswith('## Appendix A')); b_idx = next(i for i, l in enumerate(L) if l.startswith('## Appendix B'))
    old, log = {}, {'r2_sha256': R2_HASH, 'edits': [], 'map_counts': {}}
    for o, n in MAPS:
        c = 0
        for i in range(len(L)):
            if a_idx <= i < b_idx or o not in L[i]: continue
            old.setdefault(i, L[i]); c += L[i].count(o); L[i] = L[i].replace(o, n)
        assert c > 0, o; log['map_counts'][o] = c
    for pref, o, n in LINE_EDITS:
        hits = [i for i, l in enumerate(L) if l.startswith(pref) and not (a_idx <= i < b_idx)]
        assert len(hits) == 1, (pref, len(hits)); i = hits[0]
        old.setdefault(i, L[i])
        if o is None: L[i] = n
        else:
            assert L[i].count(o) == 1, (pref, o); L[i] = L[i].replace(o, n)
    for i in sorted(old):
        assert old[i] != L[i], i
        log['edits'].append({'line': i + 1, 'sha256_r2': sha(old[i].encode()), 'sha256_final': sha(L[i].encode())})
    quoted = '\n\n'.join('**r2 line %d**\n\n> %s' % (i + 1, old[i]) for i in sorted(old))
    rec = ['### v6.4.20 — adopted 21 October 2026', '',
           '- **Owner decision:** explicit PI adoption, 21 Oct 2026 ("Ben onaylıyorum", 18:14 +03:00), recorded as ' + DECISION + '. It follows the external review ' + REVIEW +
           ' of DRAFT r2 (`' + R2_HASH + '`). Review acceptance and owner adoption are separate decisions.',
           '- **Chain:** v6.4.19 (`' + V619 + '`) → ATLAS P1 working file (`' + P1_HASH + '`; `ATLAS P1 — SCIENTIFIC REVIEW ACCEPTED`) → DRAFT r1 (`' + R1_HASH +
           '`; `v6.4.20 r1 — REVIEW ACCEPTED WITH MINOR CORRECTIONS`) → DRAFT r2 (`' + R2_HASH + '`; ' + REVIEW + ') → this file by `release_v6_4_20.py` (labels and metadata only; %d lines replaced in place, quoted below).' % len(old),
           '- **Registered by this adoption (13 RIDs):** ' + ', '.join('`' + r + '`' for r in NEW_RIDS) + '. Census A (tagged identifiers): v6.4.19 135 → v6.4.20 148; every v6.4.19 identifier is kept.',
           '- **Unchanged:** every earlier statement, grade, scope and OPEN status. OPEN 20 PARTIAL (B-∞ existence and flat uniqueness CLOSED; B-an and B-6 OPEN); OPEN 9 PARTIAL.',
           '- **Kept distinctions:** FA-08 — the `DYAD-THM-RAW-CUBIC` formula is verified, its direct match with the historical OPEN 9 source is not complete. FA-04 — `degree_b_vanishing_cert_v2.py` is not available and is not presented as recreated. FC-32 (H-NG) stays a SESSION result and is not imported. Editions without a recorded hash (Triadic, OPEN-M, Programme, Methodology, DZT, AZ) stay "not recorded".',
           '- **Evidence levels:** `REVIEWER-REPLAYED` — r2 review: r2 G0–G21, the r2 negative controls, M1–M11, S1–S4 with C1–C2 (with the RECOG v0.3.20/v0.3.21/v0.3.22 files), R1–R4 with D1–D2; r1 review: r1 hashes, builder, G0–G18, N0–N16, K1–K3. `OWNER-RUN` — this release transform and its release checker with negative controls. `REVIEWER FULL REPLAY NOT COMPLETED` — the combined G14–G15 run carried from v6.4.19 (a separate historical item, not closed by the v6.4.20 reviews); the release checker of this edition until it is replayed. The release-record hashes in the v6.4.17/v6.4.18 addenda v0.1.1 are `REVIEWER-MEASURED` (r1 review), not owner-measured.',
           '- **Outbound:** N16–N20 (ATLAS disposition §6) are prepared only after external verification of this file\'s SHA-256 and are sent by the PI. No notice is sent by this release.',
           '', '#### v6.4.20 adoption — replaced DRAFT r2 lines (verbatim)', '', quoted, '']
    r2_head = [i for i, l in enumerate(L) if l.startswith('### v6.4.20 DRAFT r2 — 21 October 2026')]
    assert len(r2_head) == 1
    L[r2_head[0]:r2_head[0]] = rec
    T = '\n'.join(L)
    with open(out, 'w', encoding='utf-8', newline='\n') as f: f.write(T)
    log['out_sha256'] = sha(T.encode('utf-8')); log['record_lines'] = len(rec); log['replaced_lines'] = len(old)
    with open(os.path.join(os.path.dirname(os.path.abspath(out)), 'release_v6_4_20_log.json'), 'w', encoding='utf-8', newline='\n') as f:
        json.dump(log, f, indent=1, sort_keys=True); f.write('\n')
    print('final', log['out_sha256'], 'replaced lines', len(old))


if __name__ == '__main__':
    main()
