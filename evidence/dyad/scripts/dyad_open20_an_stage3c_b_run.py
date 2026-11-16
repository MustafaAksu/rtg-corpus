#!/usr/bin/env python3
"""dyad_open20_an_stage3c_b_run.py -- the one command of DYAD OPEN 20 stage 3c-b (analytic branch, tube route).

PREPARED PACKAGE.  Writing this driver is stage 3c-b PREPARATION (PI decision of 14 November 2026).  A production run
and its replay need a separate authorization of the PI.  The driver itself decides nothing about the mathematics: it
checks that the code is the frozen code, runs every process of the hand-over record (section 4) once, records every
exit code, applies one acceptance rule, and writes a ledger.

Modes
  selftest    development mode of the scripts (their outputs say "development run").  Every output is compared, byte
              for byte, with the committed development output of stage 3c-a.  Shows that the frozen package reproduces
              the reviewed state.  NOT a certification run; its ledger says so.
  production  the run of stage 3c-b.  Needs --pi-authorization TEXT (a reference to the PI's decision; recorded).
  replay      the same run by a second party or on a second machine (recorded as such; --pi-authorization as well).
  validate    check one finished run directory on its own, from its files (the stored verdict is not trusted).
  compare     validate two finished run directories, then compare them: same manifest as this checkout,
              production against replay (or two selftests), every output byte-identical.
  manifest    (owner, at freeze) write the manifest of the frozen code and input.
  schema      (owner, at freeze) write the gate schema from the committed reference outputs.
  rule-test   run only the test of the acceptance rule.

What a run does
  1. Manifest: every file listed in MANIFEST_SHA256.txt has the listed SHA-256, and the list is exactly the driver, the
     scripts of the job table, every dyad_* module they import (transitively), the stage-2 input and the gate schema
     GATE_SCHEMA.json (for every job the exact gate names and the exact set of false gates).
  2. Environment: python-flint 0.9.0, mpmath 1.3.0, sympy 1.14.0 (the versions of the development runs); otherwise it
     stops.  Python version, platform, CPU, the FLINT library of the wheel and the mpmath backend are recorded.
  3. Git (production, replay): both git queries succeed and the working tree is clean on the paths of the package; a
     failing query stops the run.  The commit is recorded.
  4. Rule test: the acceptance rule is applied to 16 synthetic ledgers (one good, fifteen bad).  A wrong answer stops
     the run.
  5. Jobs: 11 positive processes and 23 negative controls, each run once.  A job whose output is missing, not JSON,
     not a JSON object or without a gates object gets an error record; a job whose dependency did not end as expected
     is not run and gets a skipped record.  Every job ends with exactly one record.
  6. Verdict by the rule (see `verdict`): every job exactly once; exit 0 (positive) or 1 (control); exactly the gate
     names of the schema, each a boolean; all_pass equal to their conjunction; exactly the false gates of the schema
     (none for a positive process, the expected failure for a control); no error, not skipped; in selftest also
     byte-identity with the committed reference.  Then LEDGER.json and SHA256SUMS.txt are written.

Exit code 0 iff the verdict is ACCEPTED (compare: iff the two runs agree).

What an ACCEPTED production run would and would not establish: hand-over record section 6 and proof record sections
11-13.  In short: the computed hypotheses of the tube lemma, the arc, and two disjoint discs at xi*; the divergence of
the formal branch only together with the seed and the divergence step, which rest on literature inputs at SESSION
scope; nothing about B-an or B-6.  No single output file is a certificate.

Usage (from the repository root, inside the prepared Python environment):
  python3 -I -B evidence/dyad/scripts/dyad_open20_an_stage3c_b_run.py selftest   --out DIR [--jobs 2]
  python3 -I -B evidence/dyad/scripts/dyad_open20_an_stage3c_b_run.py production --out DIR --pi-authorization "TEXT"
  python3 -I -B evidence/dyad/scripts/dyad_open20_an_stage3c_b_run.py replay     --out DIR --pi-authorization "TEXT"
  python3 -I -B evidence/dyad/scripts/dyad_open20_an_stage3c_b_run.py compare DIR_A DIR_B
The driver's own tests (no campaign): evidence/dyad/scripts/dyad_open20_an_stage3c_b_driver_tests.py.
"""
import os, sys, re, json, time, hashlib, argparse, platform, subprocess, datetime, threading
sys.dont_write_bytecode = True

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, '..', '..', '..'))
SD = 'evidence/dyad/scripts'
PKG = 'evidence/dyad/open20-an/stage3c-b'
REF = 'evidence/dyad/open20-an/stage3c-a'
SEEDREF = 'evidence/dyad/open20-an/seed'
STAGE2 = 'evidence/dyad/open20-an/stage2/scout_N216_dps840.json'
MANIFEST = PKG + '/MANIFEST_SHA256.txt'
SCHEMA = PKG + '/GATE_SCHEMA.json'
DRIVER = SD + '/dyad_open20_an_stage3c_b_run.py'
REQUIRED = {'python-flint': '0.9.0', 'mpmath': '1.3.0', 'sympy': '1.14.0'}
RUN_ENV = 'DYAD_OPEN20_3CB'
PACKAGE_ID = 'DYAD-OPEN20-AN-3CB-1'
# the status that lib.run_status gives when RUN_ENV is set (the driver tests check that the library has this text)
RUN_STATUS = 'stage 3c-b run; one output of the run; the verdict is the ledger of the run with its replay, not this file'

P = lambda name: SD + '/dyad_open20_an_' + name + '.py'
W1, W2, W2B = P('stage3c_w1_check'), P('stage3c_w2_check'), P('stage3c_w2b_check')
W3, W4, W5, W6 = P('stage3c_w3_zone2'), P('stage3c_w4_zone1'), P('stage3c_w5_arc'), P('stage3c_w6_legs')
STR, BRA, SEED = P('stage3c_w7_structure'), P('stage3c_w7_branch'), P('seed_q1_check')
A = ['--stage2', STAGE2]


def job_table():
    """(name, expected exit code, script, arguments, output stem, reference json for selftest, dependencies).
    '{OUT}' is replaced by the output directory.  The flags of every job are those of the committed runs of stage 3c-a
    (hand-over record section 4): the legs with --full-fibre --strict-snd, the branch with --strict-e."""
    T = []
    def pos(name, script, args, stem, ref, deps=()):
        T.append(dict(name=name, expect=0, script=script, args=args, stem=stem, ref=ref, deps=list(deps)))
    def neg(name, script, args, stem, ref, deps=()):
        T.append(dict(name=name, expect=1, script=script, args=args, stem=stem, ref=ref, deps=list(deps)))
    z2 = ('zone2_F', 'zone2_G')
    # quick jobs first, so that a broken environment shows at once; the ledger keeps this order
    pos('structure', STR, [], 'w7_structure', REF + '/w7_structure.json')
    for c in ('SCALE', 'SHIFT'):
        neg('structure_' + c, STR, ['--control', c], 'w7_structure_control_' + c, REF + '/w7_structure_control_%s.json' % c)
    pos('seed', SEED, [], 'seed_q1_check', SEEDREF + '/q1_check.json')
    for c in ('BIG', 'HALFE'):
        neg('seed_' + c, SEED, ['--control', c], 'seed_q1_control_' + c, SEEDREF + '/q1_control_%s.json' % c)
    pos('arc', W5, [], 'w5_arc', REF + '/w5_arc.json')
    for c, ref in (('BIGSTEP', 'w5_control_BIGSTEP'), ('CORE', 'w5_control_CORE'), ('BRANCH', 'w5_control_BRANCH'),
                   ('LOGBRANCH', 'w6_control_LOGBRANCH')):
        neg('arc_' + c, W5, ['--control', c], 'w5_control_' + c, REF + '/%s.json' % ref)
    # the engine
    pos('engine_w1', W1, A, 'w1_check', REF + '/w1_check.json')
    neg('engine_w1_SHIFTCOEF', W1, A + ['--control', 'SHIFTCOEF'], 'w1_control_SHIFTCOEF', REF + '/w1_control_SHIFTCOEF.json')
    pos('engine_w2a', W2, A, 'w2_check', REF + '/w2_check.json')
    neg('engine_w2a_TAMPER', W2, A + ['--control', 'TAMPER'], 'w2_control_TAMPER', REF + '/w2_control_TAMPER.json')
    pos('engine_w2b', W2B, A, 'w2b_check', REF + '/w2b_check.json')
    for c in ('SHRINKREM', 'SHIFTINV'):
        neg('engine_w2b_' + c, W2B, A + ['--control', c], 'w2b_control_' + c, REF + '/w2b_control_%s.json' % c)
    # zone II (tube hypotheses on the cover), both sides
    pos('zone2_F', W3, A + ['--side', '0', '--rho0', '0.05'], 'w3_zone2_F', REF + '/w3_zone2_F.json')
    pos('zone2_G', W3, A + ['--side', '1', '--rho0', '0.05'], 'w3_zone2_G', REF + '/w3_zone2_G.json')
    for c in ('CORE', 'SIGMA', 'QZERO'):
        neg('zone2_' + c, W3, A + ['--side', '0', '--rho0', '0.40', '--control', c], 'w3_control_' + c,
            REF + '/w3_control_%s.json' % c)
    # zone I and the seam with zone II
    pos('zone1', W4, A + ['--w3dir', '{OUT}'], 'w4_zone1', REF + '/w4_zone1.json', z2)
    for c, ref in (('BIGZONE', 'w4_control_BIGZONE'), ('SIGMA', 'w4_control_SIGMA'), ('CORE', 'w4_control_CORE'),
                   ('ALPHA', 'w6_control_ALPHA'), ('BRANCH', 'w8_control_BRANCH')):
        neg('zone1_' + c, W4, A + ['--w3dir', '{OUT}', '--control', c], 'w4_control_' + c, REF + '/%s.json' % ref, z2)
    # the one inverse branch
    pos('branch', BRA, A + ['--w3', '{OUT}/w3_zone2_G.json', '--strict-e'], 'branch', REF + '/w8_branch.json', ['zone2_G'])
    neg('branch_SMALLSECTOR', BRA, A + ['--w3', '{OUT}/w3_zone2_G.json', '--control', 'SMALLSECTOR'],
        'branch_control_SMALLSECTOR', REF + '/w7_branch_control_SMALLSECTOR.json', ['zone2_G'])
    # the legs and the two-disc test; the two controls run in the default form of the leg, as in W6
    pos('legs', W6, A + ['--full-fibre', '--strict-snd'], 'legs', REF + '/w8_legs.json')
    neg('legs_SHORT', W6, A + ['--control', 'SHORT'], 'legs_control_SHORT', REF + '/w6_control_SHORT.json')
    neg('legs_ZEROJUMP', W6, A + ['--control', 'ZEROJUMP'], 'legs_control_ZEROJUMP', REF + '/w6_control_ZEROJUMP.json')
    known = {j['name'] for j in T}
    assert all(d in known for j in T for d in j['deps'])
    names = [j['name'] for j in T]
    assert len(set(names)) == len(names) and len(set(j['stem'] for j in T)) == len(T)
    return T


# ---------------------------------------------------------------- hashing, manifest, environment

def sha256(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for b in iter(lambda: f.read(1 << 20), b''):
            h.update(b)
    return h.hexdigest()


def closure(scripts):
    """The scripts and every dyad_* module they import, transitively (by reading the import statements)."""
    seen, todo = set(), list(scripts)
    while todo:
        p = todo.pop()
        if p in seen:
            continue
        seen.add(p)
        src = open(os.path.join(ROOT, p), encoding='utf-8').read()
        for m in re.findall(r'^\s*(?:import|from)\s+(dyad_[A-Za-z0-9_]+)', src, flags=re.M):
            q = SD + '/' + m + '.py'
            if not os.path.exists(os.path.join(ROOT, q)):
                raise SystemExit('STOP: module %s imported by %s is not in %s' % (m, p, SD))
            todo.append(q)
    return seen


def package_files():
    return sorted(closure({j['script'] for j in job_table()}) | {DRIVER, STAGE2, SCHEMA})


def write_manifest():
    os.makedirs(os.path.join(ROOT, PKG), exist_ok=True)
    with open(os.path.join(ROOT, MANIFEST), 'w', encoding='utf-8', newline='\n') as f:
        for p in package_files():
            f.write('%s  %s\n' % (sha256(os.path.join(ROOT, p)), p))
    print('manifest written: %s (%d files), SHA-256 %s' % (MANIFEST, len(package_files()), sha256(os.path.join(ROOT, MANIFEST))))


def check_manifest():
    mp = os.path.join(ROOT, MANIFEST)
    if not os.path.exists(mp):
        raise SystemExit('STOP: no manifest at %s' % MANIFEST)
    listed = {}
    for line in open(mp, encoding='utf-8'):
        h, p = line.rstrip('\n').split('  ', 1)
        listed[p] = h
    want = set(package_files())
    if set(listed) != want:
        raise SystemExit('STOP: the manifest does not list exactly the package files; missing %s, extra %s'
                         % (sorted(want - set(listed)), sorted(set(listed) - want)))
    bad = [p for p in sorted(listed) if sha256(os.path.join(ROOT, p)) != listed[p]]
    if bad:
        raise SystemExit('STOP: these files differ from the manifest: %s' % bad)
    return dict(path=MANIFEST, sha256=sha256(mp), files=len(listed))


def environment():
    from importlib import metadata
    ver = {}
    for k in REQUIRED:
        try:
            ver[k] = metadata.version(k)
        except metadata.PackageNotFoundError:
            ver[k] = None
    cpu = ''
    try:
        for line in open('/proc/cpuinfo'):
            if line.startswith('model name'):
                cpu = line.split(':', 1)[1].strip(); break
    except OSError:
        pass
    env = dict(python=sys.version.split()[0], implementation=platform.python_implementation(), platform=platform.platform(),
               machine=platform.machine(), cpu=cpu, cpu_count=os.cpu_count(), packages=ver, required=REQUIRED)
    try:                                      # recorded for the comparison of two machines; not part of the rule
        import flint, mpmath
        env['flint_library'] = getattr(flint, '__FLINT_VERSION__', None)
        env['mpmath_backend'] = getattr(mpmath.libmp, 'BACKEND', None)
    except ImportError:
        pass
    wrong = {k: ver[k] for k in REQUIRED if ver[k] != REQUIRED[k]}
    if wrong:
        raise SystemExit('STOP: package versions differ from the frozen environment %s: found %s' % (REQUIRED, wrong))
    return env


def git_state(strict):
    """The commit and the state of the working tree on the package paths.  A git query that fails is a failure of the
    check, never a clean tree (co-owner review 5915522711, R3)."""
    def g(*a):
        try:
            r = subprocess.run(['git', '-C', ROOT] + list(a), capture_output=True, text=True)
        except OSError as e:
            return None, str(e)
        return (r.stdout.strip() if r.returncode == 0 else None), ('' if r.returncode == 0 else 'exit %d' % r.returncode)
    head, e1 = g('rev-parse', 'HEAD')
    dirty, e2 = g('status', '--porcelain', '--', SD, PKG, os.path.dirname(STAGE2))
    st = dict(commit=head, rev_parse_ok=head is not None, status_ok=dirty is not None,
              dirty_paths=(dirty.splitlines() if dirty else []), errors=[x for x in (e1, e2) if x])
    st['clean'] = bool(st['rev_parse_ok'] and st['status_ok'] and not st['dirty_paths'])
    if strict and not st['clean']:
        raise SystemExit('STOP: production and replay need a git checkout whose state can be read and is clean on the '
                         'package paths; found %s' % st)
    return st


# ---------------------------------------------------------------- the gate schema and the acceptance rule

def write_schema():
    """(owner, at freeze) The gate schema from the committed reference outputs: for every job the exact set of gate
    names, and the exact set of gates that are false (empty for a positive process; the expected failure of a
    control).  The file is part of the manifest."""
    sch = {}
    for j in job_table():
        d = json.load(open(os.path.join(ROOT, j['ref']), encoding='utf-8'))
        g = d['gates']
        assert isinstance(g, dict) and all(isinstance(v, bool) for v in g.values())
        sch[j['name']] = dict(gates=sorted(g), false=sorted(k for k, v in g.items() if not v))
        assert (not sch[j['name']]['false']) == (j['expect'] == 0), j['name']
    with open(os.path.join(ROOT, SCHEMA), 'w', encoding='utf-8', newline='\n') as f:
        json.dump(dict(package=PACKAGE_ID, source='gates of the committed reference outputs named in the job table',
                       jobs=sch), f, indent=1, sort_keys=True); f.write('\n')
    print('gate schema written: %s (%d jobs)' % (SCHEMA, len(sch)))


def load_schema():
    d = json.load(open(os.path.join(ROOT, SCHEMA), encoding='utf-8'))
    sch = d['jobs']
    if set(sch) != {j['name'] for j in job_table()}:
        raise SystemExit('STOP: the gate schema does not name exactly the jobs of the table')
    return sch


def record_problems(j, r, schema, selftest):
    """Why one record is not the expected outcome of job j ([] if it is)."""
    n = j['name']
    if r.get('error'):
        return ['%s: %s' % (n, r['error'])]
    if r.get('skipped'):
        return ['%s: not run (%s)' % (n, r['skipped'])]
    if type(r.get('exit')) is not int or r['exit'] != j['expect']:
        return ['%s: exit %r (expected %d)' % (n, r.get('exit'), j['expect'])]
    g, ap, s = r.get('gates'), r.get('all_pass'), schema[n]
    if not isinstance(g, dict) or not g:
        return ['%s: no gates in the output' % n]
    why = []
    if set(g) != set(s['gates']):
        why.append('%s: gate names differ from the schema (missing %s, extra %s)'
                   % (n, sorted(set(s['gates']) - set(g)), sorted(set(g) - set(s['gates']))))
    elif not all(type(v) is bool for v in g.values()):
        why.append('%s: a gate value is not a boolean' % n)
    else:
        if type(ap) is not bool or ap != all(g.values()):
            why.append('%s: all_pass %r does not agree with the gates' % (n, ap))
        false = sorted(k for k, v in g.items() if not v)
        if false != s['false']:
            why.append('%s: false gates %s, expected %s' % (n, false, s['false']))
    if selftest and not (r.get('same_json') is True and r.get('same_stdout') is True):
        why.append('%s: output differs from the committed reference' % n)
    return why


def verdict(table, records, selftest, schema):
    """ACCEPTED iff every job of the table occurs exactly once among the records, and its record shows the expected
    outcome: exit code 0 for a positive process, 1 for a control; exactly the gate names of the schema, each a
    boolean; all_pass equal to the conjunction of the gates; exactly the false gates of the schema (none for a
    positive process, the expected failure for a control); no error and not skipped; in selftest also byte-identity
    of JSON and printed output with the committed reference.  Returns (accepted, reasons)."""
    why, by = [], {}
    for r in records:
        by.setdefault(r.get('name'), []).append(r)
    for j in table:
        rs = by.get(j['name'], [])
        if len(rs) != 1:
            why.append('%s: %d records (expected 1)' % (j['name'], len(rs))); continue
        why += record_problems(j, rs[0], schema, selftest)
    extra = sorted(str(k) for k in set(by) - {j['name'] for j in table})
    if extra:
        why.append('records of unknown jobs: %s' % extra)
    return (not why), why


def rule_test(schema=None):
    """The rule on synthetic ledgers built from the schema.  Each case must get the stated answer."""
    T = job_table(); schema = schema or load_schema()
    def good(selftest=True):
        return [dict(name=j['name'], exit=j['expect'], gates={k: k not in schema[j['name']]['false'] for k in schema[j['name']]['gates']},
                     all_pass=(j['expect'] == 0), same_json=selftest, same_stdout=selftest) for j in T]
    ix = {j['name']: i for i, j in enumerate(T)}
    P0 = next(i for i, j in enumerate(T) if j['expect'] == 0); N0 = next(i for i, j in enumerate(T) if j['expect'] == 1)
    cases = [('complete and as expected', good(), True, True)]
    def case(name, f):
        r = good(); f(r); cases.append((name, r, True, False))
    case('a positive process with the right output and exit code 1', lambda r: r[P0].update(exit=1))
    case('a missing process', lambda r: r.pop(P0))
    case('a process recorded twice', lambda r: r.append(dict(r[P0])))
    case('a control that passes', lambda r: r[N0].update(exit=0, all_pass=True, gates={k: True for k in r[N0]['gates']}))
    case('a positive process with exit code 0 and a false gate',
         lambda r: (r[P0]['gates'].update({sorted(r[P0]['gates'])[0]: False}), r[P0].update(all_pass=False)))
    case('selftest: an output that differs from its reference', lambda r: r[P0].update(same_json=False))
    # cases of review 5915522711, R1
    case('legs without the two-disc gate', lambda r: r[ix['legs']]['gates'].pop('SEP_two_disc_test'))
    case('control seed_BIG failing at the wrong gate',
         lambda r: r[ix['seed_BIG']]['gates'].update(Q12_inequality_at_r0=True, SND_independent_sampling=False))
    case('a control with every gate true and all_pass false',
         lambda r: r[N0].update(gates={k: True for k in r[N0]['gates']}))
    case('a gate value that is not a boolean', lambda r: r[P0]['gates'].update({sorted(r[P0]['gates'])[0]: 1}))
    case('an extra gate', lambda r: r[P0]['gates'].update(EXTRA=True))
    case('an exit code of 7', lambda r: r[P0].update(exit=7))
    case('a record with an error', lambda r: r[P0].update(error='output is not a JSON object'))
    case('a skipped job', lambda r: r[ix['branch']].update(skipped='dependency zone2_G did not end as expected'))
    case('a record of an unknown job', lambda r: r.append(dict(r[P0], name='unknown')))
    out, ok = [], True
    for name, recs, st, want in cases:
        got, _ = verdict(T, recs, st, schema)
        out.append(dict(case=name, expected='ACCEPTED' if want else 'REJECTED', got='ACCEPTED' if got else 'REJECTED'))
        ok = ok and (got == want)
    return ok, out


# ---------------------------------------------------------------- running

def read_output(rec, oj):
    """Gates and all_pass from an output file; a defect of the file becomes rec['error'] (R3)."""
    if not os.path.exists(oj):
        rec['error'] = 'no output file'; return
    rec['json_sha256'] = sha256(oj)
    try:
        d = json.load(open(oj, encoding='utf-8'))
    except (ValueError, UnicodeDecodeError) as e:
        rec['error'] = 'output is not valid JSON (%s)' % type(e).__name__; return
    if not isinstance(d, dict):
        rec['error'] = 'output is not a JSON object'; return
    if not isinstance(d.get('gates'), dict):
        rec['error'] = 'output has no gates object'; return
    rec['gates'] = d['gates']; rec['all_pass'] = d.get('all_pass'); rec['status'] = d.get('status')


def run_jobs(table, out, production_env, workers, schema):
    """Each job once.  Every job ends with exactly one record: run, error, or skipped because a dependency did not
    end as expected.  Dependencies point to earlier jobs of the table, so nothing can wait forever."""
    order = {j['name']: i for i, j in enumerate(table)}
    assert all(order[d] < order[j['name']] for j in table for d in j['deps']), 'dependencies must point backwards'
    env = dict(os.environ)
    env.pop(RUN_ENV, None)
    if production_env:
        env[RUN_ENV] = '1'
    done, records, lock = {}, [], threading.Lock()
    pending = list(table)
    byname = {j['name']: j for j in table}

    def one(j):
        args = [a.replace('{OUT}', out) for a in j['args']]
        oj = os.path.join(out, j['stem'] + '.json'); so = os.path.join(out, j['stem'] + '.stdout.txt')
        se = os.path.join(out, j['stem'] + '.stderr.txt')
        cmd = [sys.executable, '-I', '-B', j['script']] + args + ['--out', oj]
        rec = dict(name=j['name'], kind='positive' if j['expect'] == 0 else 'control', expected_exit=j['expect'],
                   command=' '.join(['python3', '-I', '-B', j['script']] + j['args'] + ['--out', '{OUT}/' + j['stem'] + '.json']),
                   json=j['stem'] + '.json', stdout=j['stem'] + '.stdout.txt')
        t0 = time.time()
        try:
            with open(so, 'wb') as fo, open(se, 'wb') as fe:
                rec['exit'] = subprocess.run(cmd, cwd=ROOT, env=env, stdout=fo, stderr=fe).returncode
            rec['stderr_bytes'] = os.path.getsize(se)
            if rec['stderr_bytes'] == 0:
                os.remove(se)
            else:
                rec['stderr'] = j['stem'] + '.stderr.txt'
            read_output(rec, oj)
            rec['stdout_sha256'] = sha256(so)
        except Exception as e:                                  # an error of the driver or of the file system
            rec['error'] = 'driver error: %s: %s' % (type(e).__name__, e)
        rec['seconds'] = round(time.time() - t0, 1)
        return rec

    def worker():
        while True:
            with lock:
                if not pending:
                    return
                j = next((x for x in pending if all(d in done for d in x['deps'])), None)
                if j is not None:
                    pending.remove(j)
                    bad = [d for d in j['deps'] if record_problems(byname[d], done[d], schema, False)]
            if j is None:
                time.sleep(0.2); continue
            if bad:
                rec = dict(name=j['name'], kind='positive' if j['expect'] == 0 else 'control', expected_exit=j['expect'],
                           skipped='dependency %s did not end as expected' % ', '.join(bad))
            else:
                try:
                    rec = one(j)
                except Exception as e:
                    rec = dict(name=j['name'], error='driver error: %s: %s' % (type(e).__name__, e))
            with lock:
                records.append(rec); done[j['name']] = rec
                print('%-26s %s' % (j['name'], 'SKIPPED: ' + rec['skipped'] if rec.get('skipped') else
                                    'ERROR: ' + rec['error'] if rec.get('error') else
                                    'exit %s (expected %d)  %7.1f s' % (rec['exit'], j['expect'], rec['seconds'])), flush=True)

    th = [threading.Thread(target=worker) for _ in range(max(1, workers))]
    for t in th:
        t.start()
    for t in th:
        t.join()
    records.sort(key=lambda r: order[r['name']])
    return records


def same_bytes(a, b):
    return os.path.exists(a) and os.path.exists(b) and open(a, 'rb').read() == open(b, 'rb').read()


def compare_refs(table, records, out):
    by = {r['name']: r for r in records}
    for j in table:
        r = by.get(j['name'])
        if r is None:
            continue
        rj = os.path.join(ROOT, j['ref']); rs = rj[:-5] + '.stdout.txt'
        r['reference'] = j['ref']
        r['same_json'] = same_bytes(os.path.join(out, j['stem'] + '.json'), rj)
        r['same_stdout'] = same_bytes(os.path.join(out, j['stem'] + '.stdout.txt'), rs)


SCOPE = {
    'selftest': 'SELFTEST in the development mode of the scripts. NOT a certification run. It shows only that the '
                'frozen package reproduces the committed development outputs of stage 3c-a byte for byte.',
    'production': 'Production run of stage 3c-b. The verdict concerns the computed statements only (hand-over record '
                  'section 6). It needs an independent replay and a release record. No statement about B-an or B-6.',
    'replay': 'Replay of the production run of stage 3c-b. To be compared with the production run by the mode compare.',
}


def write_ledger(out, led):
    with open(os.path.join(out, 'LEDGER.json'), 'w', encoding='utf-8', newline='\n') as f:
        json.dump(led, f, indent=1, sort_keys=True, ensure_ascii=False); f.write('\n')
    names = sorted(n for n in os.listdir(out) if n != 'SHA256SUMS.txt')
    with open(os.path.join(out, 'SHA256SUMS.txt'), 'w', encoding='utf-8', newline='\n') as f:
        for n in names:
            f.write('%s  %s\n' % (sha256(os.path.join(out, n)), n))


def run(mode, out, auth, label, workers):
    out = os.path.abspath(out)
    if os.path.exists(out) and os.listdir(out):
        raise SystemExit('STOP: the output directory exists and is not empty: %s' % out)
    selftest = mode == 'selftest'
    if not selftest and not (auth and auth.strip()):
        raise SystemExit('STOP: %s needs --pi-authorization "TEXT" (a reference to the PI\'s decision)' % mode)
    man = check_manifest()
    schema = load_schema()
    env = environment()
    git = git_state(strict=not selftest)
    ok_rule, rule = rule_test(schema)
    if not ok_rule:
        raise SystemExit('STOP: the acceptance rule failed its own test: %s' % rule)
    os.makedirs(out, exist_ok=True)
    table = job_table()
    utc = lambda: datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    started = utc()
    print('%s | mode %s | %d jobs | manifest %s' % (PACKAGE_ID, mode, len(table), man['sha256'][:16]), flush=True)
    records = run_jobs(table, out, production_env=not selftest, workers=workers, schema=schema)
    if selftest:
        compare_refs(table, records, out)
    accepted, why = verdict(table, records, selftest, schema)
    led = dict(package=PACKAGE_ID, mode=mode, label=label, pi_authorization=auth, scope=SCOPE[mode], started_utc=started,
               finished_utc=utc(), manifest=man, environment=env, git=git, workers=workers, rule_test=rule,
               counts=dict(jobs=len(table), positive=sum(1 for j in table if j['expect'] == 0),
                           controls=sum(1 for j in table if j['expect'] == 1)),
               jobs=records, verdict='ACCEPTED' if accepted else 'REJECTED', reasons=why)
    write_ledger(out, led)
    print('VERDICT %s (%s)%s' % (led['verdict'], mode, '' if accepted else ': ' + '; '.join(why)))
    print(SCOPE[mode])
    return 0 if accepted else 1


def validate_dir(d):
    """Check one finished run directory on its own, from its files (R2).  The stored verdict is not trusted: the
    checksum file must list exactly the files of the directory with their hashes; each ledger record must name the
    files of its job, carry their actual hashes and the gates that the actual output contains; then the rule is
    applied again.  Before anything else the frozen package is checked against its manifest, so the gate schema used
    is the frozen one (r3, review 5917787569 R2-A), and the ledger must carry that manifest.  The ledger must also be
    consistent with its mode (R2-B).  Returns (ok, reasons, ledger)."""
    why = []
    try:
        man = check_manifest()
    except SystemExit as e:
        return False, ['package check: %s' % e], None
    try:
        led = json.load(open(os.path.join(d, 'LEDGER.json'), encoding='utf-8'))
    except (OSError, ValueError) as e:
        return False, ['no readable ledger: %s' % type(e).__name__], None
    if not isinstance(led, dict) or not isinstance(led.get('jobs'), list):
        return False, ['the ledger is not a ledger'], None
    try:
        sums = {}
        for line in open(os.path.join(d, 'SHA256SUMS.txt'), encoding='utf-8'):
            h, n = line.rstrip('\n').split('  ', 1)
            if n in sums:
                why.append('SHA256SUMS lists %s twice' % n)
            sums[n] = h
    except (OSError, ValueError):
        return False, ['no readable SHA256SUMS.txt'], led
    files = {n for n in os.listdir(d) if n != 'SHA256SUMS.txt'}
    if set(sums) != files:
        why.append('SHA256SUMS does not list exactly the files of the directory (missing %s, extra %s)'
                   % (sorted(files - set(sums)), sorted(set(sums) - files)))
    why += ['SHA256SUMS: %s differs' % n for n in sorted(set(sums) & files) if sha256(os.path.join(d, n)) != sums[n]]
    if led.get('package') != PACKAGE_ID:
        why.append('package %r' % led.get('package'))
    mode = led.get('mode')
    if mode not in SCOPE:
        why.append('mode %r' % mode)
    if (led.get('manifest') or {}).get('sha256') != man['sha256']:
        why.append('the ledger carries manifest %r, not the frozen manifest %s'
                   % ((led.get('manifest') or {}).get('sha256'), man['sha256']))
    table = job_table(); schema = load_schema(); byname = {j['name']: j for j in table}
    rebuilt = []
    for r in led['jobs']:
        if not isinstance(r, dict):
            why.append('a ledger record is not an object'); continue
        j = byname.get(r.get('name'))
        if j is None:
            rebuilt.append(dict(name=r.get('name'))); continue
        x = dict(name=j['name'], exit=r.get('exit'), error=r.get('error'), skipped=r.get('skipped'))
        if not (x['error'] or x['skipped']):
            if r.get('json') != j['stem'] + '.json' or r.get('stdout') != j['stem'] + '.stdout.txt':
                why.append('%s: the ledger names other files than those of the job' % j['name'])
            oj, so = os.path.join(d, j['stem'] + '.json'), os.path.join(d, j['stem'] + '.stdout.txt')
            read_output(x, oj)
            if os.path.exists(oj) and r.get('json_sha256') != x.get('json_sha256'):
                why.append('%s: the hash of the JSON output differs from the ledger' % j['name'])
            if not os.path.exists(so) or r.get('stdout_sha256') != sha256(so):
                why.append('%s: the printed output is missing or differs from the ledger' % j['name'])
            if r.get('gates') != x.get('gates') or r.get('all_pass') != x.get('all_pass') or r.get('status') != x.get('status'):
                why.append('%s: the gates in the ledger differ from those of the output' % j['name'])
            if mode == 'selftest':
                x['same_json'] = same_bytes(oj, os.path.join(ROOT, j['ref']))
                x['same_stdout'] = same_bytes(so, os.path.join(ROOT, j['ref'][:-5] + '.stdout.txt'))
        rebuilt.append(x)
    why += mode_problems(led, rebuilt)
    ok, w = verdict(table, rebuilt, mode == 'selftest', schema)
    why += w
    if led.get('verdict') != ('ACCEPTED' if ok else 'REJECTED'):
        why.append('the stored verdict %r is not the verdict of the rule' % led.get('verdict'))
    return (not why), why, led


def mode_problems(led, records):
    """A ledger must not contradict its own mode (R2-B).  It cannot prove that a PI decision is real; it rejects a set
    of files that contradicts itself."""
    why, mode = [], led.get('mode')
    if mode not in SCOPE:
        return why
    if led.get('scope') != SCOPE[mode]:
        why.append('the scope text is not the text of mode %s' % mode)
    rt = led.get('rule_test')
    if not (isinstance(rt, list) and rt and all(isinstance(r, dict) and r.get('got') == r.get('expected') for r in rt)):
        why.append('the ledger does not show a passed rule test')
    env = led.get('environment') or {}
    if (env.get('packages') or {}) != REQUIRED:
        why.append('the recorded package versions are not the frozen ones')
    auth = led.get('pi_authorization')
    production = mode in ('production', 'replay')
    if production:
        if not (isinstance(auth, str) and auth.strip()):
            why.append('mode %s without a recorded PI authorization' % mode)
        git = led.get('git') or {}
        if not (git.get('clean') is True and git.get('commit')):
            why.append('mode %s without a clean, readable git state' % mode)
    elif auth not in (None, ''):
        why.append('a selftest that records a PI authorization')
    for r in records:                                   # rebuilt from the output files, not from the ledger
        if not isinstance(r, dict) or r.get('error') or r.get('skipped'):
            continue
        j = {x['name']: x for x in job_table()}.get(r.get('name'))
        if j is None:
            continue
        st = r.get('status')
        if j['script'] == STR:                          # the structure script has no status field
            if st is not None:
                why.append('%s: a status where the script writes none' % j['name'])
        elif production and st != RUN_STATUS:
            why.append('%s: the output says %r in mode %s' % (j['name'], (st or '')[:40], mode))
        elif not production and st == RUN_STATUS:
            why.append('%s: a selftest output with the status of a production run' % j['name'])
    return why


def compare(a, b):
    """Validate both directories on their own, then compare them (R2)."""
    ok = True
    leds = []
    try:
        check_manifest()
    except SystemExit as e:
        print('package check:', e); print('COMPARE DISAGREE'); return 1
    for d in (a, b):
        v, why, led = validate_dir(d)
        print('%-60s %s' % (d[-60:], 'VALID' if v else 'INVALID'))
        for w in why[:20]:
            print('   ', w)
        ok = ok and v; leds.append(led)
    la, lb = leds
    if not (la and lb):
        print('COMPARE DISAGREE'); return 1
    cur = sha256(os.path.join(ROOT, MANIFEST))
    checks = [('manifest of both runs is the manifest of this checkout',
               la.get('manifest', {}).get('sha256') == lb.get('manifest', {}).get('sha256') == cur),
              ('modes', ({la.get('mode'), lb.get('mode')} == {'production', 'replay'}) or (la.get('mode') == lb.get('mode') == 'selftest'))]
    n = 0
    for j in job_table():
        for ext in ('.json', '.stdout.txt'):
            fa, fb = os.path.join(a, j['stem'] + ext), os.path.join(b, j['stem'] + ext)
            n += 1
            if not same_bytes(fa, fb):
                checks.append(('%s%s identical' % (j['stem'], ext), False))
    for what, good in checks:
        if not good or what in ('manifest of both runs is the manifest of this checkout', 'modes'):
            print('%-60s %s' % (what, 'ok' if good else 'DIFFERENT'))
        ok = ok and good
    print('files compared: %d' % n)
    print('COMPARE', 'AGREE' if ok else 'DISAGREE')
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('mode', choices=['selftest', 'production', 'replay', 'compare', 'validate', 'manifest', 'schema', 'rule-test'])
    ap.add_argument('dirs', nargs='*')
    ap.add_argument('--out'); ap.add_argument('--pi-authorization'); ap.add_argument('--label', default='')
    ap.add_argument('--jobs', type=int, default=2)
    o = ap.parse_args()
    if o.mode == 'manifest':
        write_manifest(); return 0
    if o.mode == 'schema':
        write_schema(); return 0
    if o.mode == 'validate':
        if len(o.dirs) != 1:
            raise SystemExit('validate needs one run directory')
        v, why, _ = validate_dir(o.dirs[0])
        for w in why:
            print('   ', w)
        print('VALIDATE', 'VALID' if v else 'INVALID'); return 0 if v else 1
    if o.mode == 'rule-test':
        ok, rule = rule_test()
        for r in rule:
            print('%-62s expected %s, got %s' % (r['case'], r['expected'], r['got']))
        print('RULE TEST', 'PASS' if ok else 'FAIL'); return 0 if ok else 1
    if o.mode == 'compare':
        if len(o.dirs) != 2:
            raise SystemExit('compare needs two run directories')
        return compare(o.dirs[0], o.dirs[1])
    if not o.out:
        raise SystemExit('--out DIR is required')
    return run(o.mode, o.out, o.pi_authorization, o.label, o.jobs)


if __name__ == '__main__':
    sys.exit(main())
