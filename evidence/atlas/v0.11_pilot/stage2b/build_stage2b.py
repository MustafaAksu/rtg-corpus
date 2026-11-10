#!/usr/bin/env python3
"""Atlas v0.11 D3 pilot, stage 2b: source correction (not a compaction) against the accepted stage-2a output.

Three D3 sites still carry the (D5) [assuming:] qualifier that the pinned owner edition recog-v0.3.27 replaced by
imported owner theorem rows (owner DSN lines 43, 180, 764, 1056; Appendix A v0.3.27 "Source conditions changed").
Each edit replaces one declared span; the rest of the line is byte-identical.
Usage: build_stage2b.py STAGE2A.md OUT.md MAP.json CHANGES.md
"""
import hashlib, json, sys, importlib.util, pathlib
BASE_SHA = 'ace0b408def88c78291e7f26eaa8e358ade87205b738a9dcf8f7952a9818a5d6'
IMP = 'DYAD-THM-LPHASE-ROWA-BRIDGE, DYAD-THM-OPEN3-SPIRAL-REM (dyad-v6.4.23) and RECOG-ALG-A1C-JET-REMAINDER-BOUNDS'
EDITS = [  # (line prefix, old span, new span, owner evidence)
 ('RECOG-THM-A1B-SLIP-SCHEDULE-U THM | ', '[assuming: Dyadic (D5) row-A bridge proof constants]', f'[import: {IMP}]',
  'RECOG-THM-A1C-SHARPENED-SCHEDULE: owner DSN line 764 carries [import: … DYAD-THM-LPHASE-ROWA-BRIDGE, DYAD-THM-OPEN3-SPIRAL-REM] and "the former (D5) qualifier is discharged, v0.3.27"'),
 ('RECOG-RESULT-A1C-RECORD-PHASE-READOUT RES[from THM] | ', '; [assuming: (D5)];', f'; [import: {IMP}];',
  'RECOG-ALG-A1C-JOINT-CONTRACTOR: owner DSN line 1056 carries the same [import:] and "the former (D5) qualifier is discharged, v0.3.27"'),
 ('RECOG-OPEN-EVENT-RULE (R6) ACTIVE | ', 'under the (D5) [assuming:] (RECOG-ALG-A1C-JOINT-CONTRACTOR)', f'with the row-A remainder constants of {IMP} (RECOG-ALG-A1C-JOINT-CONTRACTOR)',
  'A1c-decoder sub-item: owner DSN line 180 "with the row-A remainder constants of the envelope (…; the former (D5) qualifier discharged at v0.3.27)"'),
]
def main():
    src, out, mapf, chf = sys.argv[1:5]
    raw = open(src, 'rb').read(); assert hashlib.sha256(raw).hexdigest() == BASE_SHA, 'base is not the accepted stage-2a output'
    lines = raw.decode('utf-8').split('\n'); log = []
    for prefix, old, new, ev in EDITS:
        hits = [i for i, l in enumerate(lines) if l.startswith(prefix)]; assert len(hits) == 1, (prefix, hits); i = hits[0]
        assert 608 <= i + 1 <= 857 and lines[i].count(old) == 1, (prefix, old)
        lines[i] = lines[i].replace(old, new); log.append((i + 1, prefix.split(' ')[0], old, new, ev))
    cand = '\n'.join(lines).encode('utf-8'); open(out, 'wb').write(cand)
    assert b'(D5) [assuming' not in cand.split(b'\n## D3 ')[1].split(b'\n## D4a')[0].replace(b'the (D5) [assuming:] removed', b'') and b'[assuming: (D5)' not in cand and b'[assuming: Dyadic (D5)' not in cand
    tool = pathlib.Path(__file__).resolve().parents[4] / 'tools' / 'atlas_preservation.py'
    sp = importlib.util.spec_from_file_location('ap', tool); ap = importlib.util.module_from_spec(sp); sp.loader.exec_module(ap)
    B, C = ap.extract(raw), ap.extract(cand); recs = []; why = 'stage 2b source correction: stale (D5) [assuming:] replaced by the owner import of recog-v0.3.27'
    for rb, rc in zip(B['regions'], C['regions']):
        assert rb['kind'] == rc['kind'] and rb['line'] == rc['line']
        if rb['sha256'] == rc['sha256']: continue
        if rb['kind'] == 'node':
            bh = [f['sha256'] for f in rb['fields']]; ch = [f['sha256'] for f in rc['fields']]
            lost = [h for h in bh if h not in ch]; new = [h for h in ch if h not in bh]; assert len(lost) == len(new) == 1
            recs.append(dict(base=ap.okey(rb), cand=ap.okey(rc), reason=why, fields=[dict(base_sha256=lost[0], cand_sha256=new[0], reason=why)]))
        else: recs.append(dict(base=ap.okey(rb), cand=ap.okey(rc), reason=why))
    json.dump(dict(base_sha256=BASE_SHA, candidate_sha256=hashlib.sha256(cand).hexdigest(), stage='v0.11 D3 pilot, stage 2b (source correction)', records=recs, inserts=[]), open(mapf, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    o = ['# Stage 2b — the three corrected spans, verbatim', '', f'Base: stage-2a output `{BASE_SHA}`. Candidate: `{hashlib.sha256(cand).hexdigest()}`. {len(raw):,} → {len(cand):,} bytes.', '']
    for n, (ln, rid, old, new, ev) in enumerate(log, 1):
        o += [f'## {n}. L{ln} `{rid}`', '', '**Base:**', '', '```text', old, '```', '', '**Stage 2b:**', '', '```text', new, '```', '', f'**Owner evidence (`recog-v0.3.27`):** {ev}', '']
    open(chf, 'w', encoding='utf-8').write('\n'.join(o)); print(hashlib.sha256(cand).hexdigest(), len(raw), len(cand), len(recs), 'records')
if __name__ == '__main__': main()
