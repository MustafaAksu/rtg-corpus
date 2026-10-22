#!/usr/bin/env python3
"""p2_release_controls.py -- negative controls for check_release_v6_4_20.py.
Each control mutates a temporary copy of the adopted v6.4.20 file (release log copied alongside), runs the release checker with
--norebuild (N0: full transform) and records exit code and failing gates.  Writes release_controls_v6_4_20.json (deterministic).
Exit 0 all as expected / 1 otherwise / 3 crash.   Usage: python -B p2_release_controls.py
"""
import sys, os, re, json, shutil, subprocess, tempfile
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
FINAL = 'RTG_DYADIC_OSCILLATOR_DSN_v6_4_20.md'


def sec(s, a, b):
    i = s.index(a); return i, s.index(b, i)


def in_sec(s, a, b, old, new):
    i, j = sec(s, a, b); seg = s[i:j]; assert old in seg, old
    return s[:i] + seg.replace(old, new, 1) + s[j:]


def x1(s): return in_sec(s, '## §6.', '## §7.', '403}{250}', '403}{251}')
def x2(s): return in_sec(s, '## §6.', '## §7.', '`[ALG]` **Eigenframe linear-part lemma.**', '`[THM]` **Eigenframe linear-part lemma.**')
def x3(s): return in_sec(s, '## §6.', '## §7.', '[RID: DYAD-ALG-GLATTICE5]', 'DYAD-ALG-GLATTICE5') if '[RID: DYAD-ALG-GLATTICE5]' in s[s.index('## §6.'):s.index('## §7.')] else s.replace('[RID: DYAD-ALG-P5-RADIAL]', '', 1)
def x4(s): return in_sec(s, '## §6.', '## §7.', 'RID registered at adoption, 21 Oct 2026', 'proposed RID, registered only at adoption')
def x5(s): return s.replace(' (`DYAD v6.4.20 — OWNER ADOPTION AUTHORIZED`) after external review of DRAFT r2', ' after external review of DRAFT r2', 1)
def x6(s): return s + '\n*END OF DOCUMENT — duplicate*\n'
def x7(s): return s.replace('OPEN 20 is PARTIAL: B-∞ existence and flat uniqueness are CLOSED; B-an and B-6 are OPEN.', 'OPEN 20 is PARTIAL: B-∞ existence and flat uniqueness are CLOSED; B-6 is OPEN.', 1)
def x8(s): return s.replace('`REVIEWER FULL REPLAY NOT COMPLETED` — the combined G14–G15 run carried from v6.4.19', '`REVIEWER FULL REPLAY NOT COMPLETED` — none', 1)
def x9(s): return s.replace('| ALG — new in v6.4.20 |', '| ALG — proposed, not adopted |', 1)


def x10(s):
    i, j = sec(s, '## §3.', '## §4.'); seg = s[i:j]
    m = re.search(r' not (?![^$]*\$)', seg); assert m
    return s[:i] + seg[:m.start()] + ' ' + seg[m.end():] + s[j:]


CONTROLS = [('X1', x1, 'R4', 'constant 403/250 -> 403/251 in section 6'), ('X2', x2, 'R5', 'grade tag ALG -> THM in section 6'),
            ('X3', x3, 'R3', 'one RID tag removed'), ('X4', x4, 'R6', '"registered only at adoption" back in live text'),
            ('X5', x5, 'R7', 'PI decision label removed from the header'), ('X6', x6, 'R8', 'second footer'),
            ('X7', x7, 'R9', 'OPEN 20 status sentence altered'), ('X8', x8, 'R10', 'combined G14-G15 NOT COMPLETED item dropped from the record'),
            ('X9', x9, 'R11', 'E.1 row back to "proposed, not adopted"'), ('X10', x10, 'R2', 'the word "not" removed from a section 3 sentence')]


def run(tmp, text, rebuild=False):
    d = os.path.join(tmp, FINAL)
    with open(d, 'w', encoding='utf-8', newline='\n') as f: f.write(text)
    shutil.copy(os.path.join(HERE, 'release_v6_4_20_log.json'), tmp)
    out = os.path.join(tmp, 'res.json')
    if os.path.exists(out): os.remove(out)
    cmd = [sys.executable, '-B', os.path.join(HERE, 'check_release_v6_4_20.py'), '--final', d, '--r2', os.path.join(HERE, 'RTG_DYADIC_OSCILLATOR_DSN_v6_4_20_DRAFT_r2.md'),
           '--base', os.path.join(HERE, 'base_v6_4_19.md'), '--out', out]
    if not rebuild: cmd.append('--norebuild')
    r = subprocess.run(cmd, capture_output=True, text=True, cwd=tmp)
    f = []
    if os.path.exists(out):
        g = json.load(open(out))['gates']; f = sorted((k for k, v in g.items() if v is False), key=lambda x: int(x[1:]))
    return r.returncode, f


def main():
    base = open(os.path.join(HERE, FINAL), encoding='utf-8').read()
    rows, tmp = [], tempfile.mkdtemp()
    try:
        rc, f = run(tmp, base)
        rows.append({'id': 'P0', 'description': 'unmutated final (--norebuild)', 'exit': rc, 'failing_gates': f, 'as_expected': rc == 0 and not f})
        rc, f = run(tmp, base.replace('hyperbolic saddle.', 'hyperbolic  saddle.', 1), rebuild=True)
        rows.append({'id': 'N0', 'description': 'one-byte edit (full transform)', 'expected_gate': 'R0', 'exit': rc, 'failing_gates': f, 'as_expected': rc == 1 and 'R0' in f})
        for cid, fn, gate, desc in CONTROLS:
            m = fn(base); assert m != base, cid
            rc, f = run(tmp, m)
            rows.append({'id': cid, 'description': desc, 'expected_gate': gate, 'exit': rc, 'failing_gates': f, 'as_expected': rc == 1 and gate in f})
    finally:
        shutil.rmtree(tmp)
    ok = all(r['as_expected'] for r in rows)
    for r in rows: print(r['id'], r['exit'], ','.join(r['failing_gates']), 'OK' if r['as_expected'] else 'UNEXPECTED')
    print('ALL CONTROLS AS EXPECTED' if ok else 'CONTROL FAILURE')
    with open(os.path.join(HERE, 'release_controls_v6_4_20.json'), 'w', encoding='utf-8', newline='\n') as fh:
        json.dump({'script': 'p2_release_controls.py', 'controls': rows, 'all_as_expected': ok}, fh, indent=1, sort_keys=True); fh.write('\n')
    return 0 if ok else 1


if __name__ == '__main__':
    try:
        sys.exit(main())
    except SystemExit:
        raise
    except Exception as ex:
        import traceback; traceback.print_exc(); print('CRASH', type(ex).__name__, ex); sys.exit(3)
