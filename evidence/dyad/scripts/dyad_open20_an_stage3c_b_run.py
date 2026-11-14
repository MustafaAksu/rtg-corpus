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
  compare     compare two finished run directories: same manifest, both accepted, every output byte-identical.
  manifest    (owner, at freeze) write the manifest of the frozen code and input.
  rule-test   run only the test of the acceptance rule.

What a run does
  1. Manifest: every file listed in MANIFEST_SHA256.txt has the listed SHA-256, and the list is exactly the driver, the
     scripts of the job table, every dyad_* module they import (transitively), and the stage-2 input.
  2. Environment: python-flint 0.9.0, mpmath 1.3.0, sympy 1.14.0 (the versions of the development runs); otherwise it
     stops.  Python version, platform, CPU, the FLINT library of the wheel and the mpmath backend are recorded.
  3. Git (production, replay): the working tree is clean on the paths of the package; the commit is recorded.
  4. Rule test: the acceptance rule is applied to synthetic ledgers (one good, six bad).  A wrong answer stops the run.
  5. Jobs: 11 positive processes (expected exit 0, every gate true) and 23 negative controls (expected exit 1, not
     all gates true).  Each is run once; exit code, time, output hashes and gates go to the ledger.
  6. Verdict by the rule: ACCEPTED iff every job occurs exactly once with its expected outcome (selftest: and every
     output is identical to its committed reference).  Then LEDGER.json and SHA256SUMS.txt are written.

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
DRIVER = SD + '/dyad_open20_an_stage3c_b_run.py'
REQUIRED = {'python-flint': '0.9.0', 'mpmath': '1.3.0', 'sympy': '1.14.0'}
RUN_ENV = 'DYAD_OPEN20_3CB'
PACKAGE_ID = 'DYAD-OPEN20-AN-3CB-1'

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
    return sorted(closure({j['script'] for j in job_table()}) | {DRIVER, STAGE2})


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
    def g(*a):
        r = subprocess.run(['git', '-C', ROOT] + list(a), capture_output=True, text=True)
        return r.stdout.strip() if r.returncode == 0 else None
    head = g('rev-parse', 'HEAD')
    dirty = g('status', '--porcelain', '--', SD, PKG, os.path.dirname(STAGE2))
    st = dict(commit=head, dirty_paths=(dirty.splitlines() if dirty else []), git_available=head is not None)
    if strict and (head is None or dirty):
        raise SystemExit('STOP: production and replay need a git checkout that is clean on the package paths; found %s' % st)
    return st


# ---------------------------------------------------------------- the acceptance rule

def verdict(table, records, selftest):
    """ACCEPTED iff every job of the table occurs exactly once in the records with its expected outcome:
    positive: exit code 0, the output has all_pass true and every gate true;
    control:  exit code 1, the output has all_pass false;
    selftest: in addition json and stdout are byte-identical to the committed reference.
    Returns (accepted, list of reasons)."""
    why = []
    by = {}
    for r in records:
        by.setdefault(r['name'], []).append(r)
    for j in table:
        rs = by.get(j['name'], [])
        if len(rs) != 1:
            why.append('%s: %d records (expected 1)' % (j['name'], len(rs))); continue
        r = rs[0]
        if r.get('exit') != j['expect']:
            why.append('%s: exit %s (expected %d)' % (j['name'], r.get('exit'), j['expect'])); continue
        gates = r.get('gates')
        if not isinstance(gates, dict) or not gates:
            why.append('%s: no gates in the output' % j['name']); continue
        if j['expect'] == 0 and not (r.get('all_pass') is True and all(v is True for v in gates.values())):
            why.append('%s: positive process with a gate that is not true' % j['name'])
        if j['expect'] == 1 and r.get('all_pass') is not False:
            why.append('%s: control whose output does not say all_pass false' % j['name'])
        if selftest and not (r.get('same_json') is True and r.get('same_stdout') is True):
            why.append('%s: output differs from the committed reference' % j['name'])
    extra = sorted(set(by) - {j['name'] for j in table})
    if extra:
        why.append('records of unknown jobs: %s' % extra)
    return (not why), why


def rule_test():
    """The rule on synthetic ledgers.  Each case must get the stated answer."""
    T = job_table()
    def good(selftest=True):
        return [dict(name=j['name'], exit=j['expect'], gates={'G': j['expect'] == 0}, all_pass=(j['expect'] == 0),
                     same_json=selftest, same_stdout=selftest) for j in T]
    first_pos = next(i for i, j in enumerate(T) if j['expect'] == 0)
    first_neg = next(i for i, j in enumerate(T) if j['expect'] == 1)
    cases = []
    cases.append(('complete and as expected', good(), True, True))
    r = good(); r[first_pos]['exit'] = 1
    cases.append(('a positive process with the right output and exit code 1', r, True, False))
    r = good(); del r[first_pos]
    cases.append(('a missing process', r, True, False))
    r = good(); r.append(dict(r[first_pos]))
    cases.append(('a process recorded twice', r, True, False))
    r = good(); r[first_neg]['exit'] = 0; r[first_neg]['all_pass'] = True; r[first_neg]['gates'] = {'G': True}
    cases.append(('a control that passes', r, True, False))
    r = good(); r[first_pos]['gates'] = {'G': True, 'H': False}; r[first_pos]['all_pass'] = False
    cases.append(('a positive process with exit code 0 and a false gate', r, True, False))
    r = good(); r[first_pos]['same_json'] = False
    cases.append(('selftest: an output that differs from its reference', r, True, False))
    out, ok = [], True
    for name, recs, st, want in cases:
        got, _ = verdict(T, recs, st)
        out.append(dict(case=name, expected='ACCEPTED' if want else 'REJECTED', got='ACCEPTED' if got else 'REJECTED'))
        ok = ok and (got == want)
    return ok, out


# ---------------------------------------------------------------- running

def run_jobs(table, out, production_env, workers):
    env = dict(os.environ)
    env.pop(RUN_ENV, None)
    if production_env:
        env[RUN_ENV] = '1'
    done, records, lock = set(), [], threading.Lock()
    pending = list(table)

    def one(j):
        args = [a.replace('{OUT}', out) for a in j['args']]
        oj = os.path.join(out, j['stem'] + '.json'); so = os.path.join(out, j['stem'] + '.stdout.txt')
        se = os.path.join(out, j['stem'] + '.stderr.txt')
        cmd = [sys.executable, '-I', '-B', j['script']] + args + ['--out', oj]
        t0 = time.time()
        with open(so, 'wb') as fo, open(se, 'wb') as fe:
            rc = subprocess.run(cmd, cwd=ROOT, env=env, stdout=fo, stderr=fe).returncode
        rec = dict(name=j['name'], kind='positive' if j['expect'] == 0 else 'control', expected_exit=j['expect'], exit=rc,
                   seconds=round(time.time() - t0, 1), command=' '.join(['python3', '-I', '-B', j['script']] + j['args'] + ['--out', '{OUT}/' + j['stem'] + '.json']),
                   json=j['stem'] + '.json', stdout=j['stem'] + '.stdout.txt', stderr_bytes=os.path.getsize(se))
        if rec['stderr_bytes'] == 0:
            os.remove(se)
        else:
            rec['stderr'] = j['stem'] + '.stderr.txt'
        if os.path.exists(oj):
            rec['json_sha256'] = sha256(oj)
            try:
                d = json.load(open(oj, encoding='utf-8'))
                rec['gates'] = d.get('gates'); rec['all_pass'] = d.get('all_pass'); rec['status'] = d.get('status')
            except ValueError:
                rec['gates'] = None
        rec['stdout_sha256'] = sha256(so)
        return rec

    def worker():
        # every job ends with a record, whatever its exit code, so a dependency is always satisfied in the end
        while True:
            with lock:
                if not pending:
                    return
                j = next((x for x in pending if all(d in done for d in x['deps'])), None)
                if j is not None:
                    pending.remove(j)
            if j is None:
                time.sleep(1.0); continue
            rec = one(j)
            with lock:
                records.append(rec); done.add(j['name'])
                print('%-26s exit %s (expected %d)  %7.1f s' % (j['name'], rec['exit'], j['expect'], rec['seconds']), flush=True)

    th = [threading.Thread(target=worker) for _ in range(max(1, workers))]
    for t in th:
        t.start()
    for t in th:
        t.join()
    order = {j['name']: i for i, j in enumerate(table)}
    records.sort(key=lambda r: order[r['name']])
    return records


def compare_refs(table, records, out):
    by = {r['name']: r for r in records}
    for j in table:
        r = by.get(j['name'])
        if r is None:
            continue
        rj = os.path.join(ROOT, j['ref']); rs = rj[:-5] + '.stdout.txt'
        oj = os.path.join(out, j['stem'] + '.json'); so = os.path.join(out, j['stem'] + '.stdout.txt')
        same = lambda a, b: os.path.exists(a) and os.path.exists(b) and open(a, 'rb').read() == open(b, 'rb').read()
        r['reference'] = j['ref']; r['same_json'] = same(oj, rj); r['same_stdout'] = same(so, rs)


def run(mode, out, auth, label, workers):
    out = os.path.abspath(out)
    if os.path.exists(out) and os.listdir(out):
        raise SystemExit('STOP: the output directory exists and is not empty: %s' % out)
    selftest = mode == 'selftest'
    if not selftest and not (auth and auth.strip()):
        raise SystemExit('STOP: %s needs --pi-authorization "TEXT" (a reference to the PI\'s decision)' % mode)
    man = check_manifest()
    env = environment()
    git = git_state(strict=not selftest)
    ok_rule, rule = rule_test()
    if not ok_rule:
        raise SystemExit('STOP: the acceptance rule failed its own test: %s' % rule)
    os.makedirs(out, exist_ok=True)
    table = job_table()
    utc = lambda: datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    started = utc()
    print('%s | mode %s | %d jobs | manifest %s' % (PACKAGE_ID, mode, len(table), man['sha256'][:16]), flush=True)
    records = run_jobs(table, out, production_env=not selftest, workers=workers)
    if selftest:
        compare_refs(table, records, out)
    accepted, why = verdict(table, records, selftest)
    scope = {
        'selftest': 'SELFTEST in the development mode of the scripts. NOT a certification run. It shows only that the '
                    'frozen package reproduces the committed development outputs of stage 3c-a byte for byte.',
        'production': 'Production run of stage 3c-b. The verdict concerns the computed statements only (hand-over record '
                      'section 6). It needs an independent replay and a release record. No statement about B-an or B-6.',
        'replay': 'Replay of the production run of stage 3c-b. To be compared with the production run by the mode compare.',
    }[mode]
    led = dict(package=PACKAGE_ID, mode=mode, label=label, pi_authorization=auth, scope=scope, started_utc=started,
               finished_utc=utc(), manifest=man, environment=env, git=git, workers=workers, rule_test=rule,
               counts=dict(jobs=len(table), positive=sum(1 for j in table if j['expect'] == 0),
                           controls=sum(1 for j in table if j['expect'] == 1)),
               jobs=records, verdict='ACCEPTED' if accepted else 'REJECTED', reasons=why)
    with open(os.path.join(out, 'LEDGER.json'), 'w', encoding='utf-8', newline='\n') as f:
        json.dump(led, f, indent=1, sort_keys=True, ensure_ascii=False); f.write('\n')
    names = sorted(n for n in os.listdir(out) if n != 'SHA256SUMS.txt')
    with open(os.path.join(out, 'SHA256SUMS.txt'), 'w', encoding='utf-8', newline='\n') as f:
        for n in names:
            f.write('%s  %s\n' % (sha256(os.path.join(out, n)), n))
    print('VERDICT %s (%s)%s' % (led['verdict'], mode, '' if accepted else ': ' + '; '.join(why)))
    print(scope)
    return 0 if accepted else 1


def compare(a, b):
    la = json.load(open(os.path.join(a, 'LEDGER.json'), encoding='utf-8'))
    lb = json.load(open(os.path.join(b, 'LEDGER.json'), encoding='utf-8'))
    rows, ok = [], True
    def row(what, good, detail=''):
        nonlocal ok
        rows.append((what, 'ok' if good else 'DIFFERENT', detail)); ok = ok and good
    row('package', la['package'] == lb['package'] == PACKAGE_ID)
    row('manifest', la['manifest']['sha256'] == lb['manifest']['sha256'], la['manifest']['sha256'][:16])
    row('verdicts', la['verdict'] == lb['verdict'] == 'ACCEPTED', '%s / %s' % (la['verdict'], lb['verdict']))
    row('modes', ({la['mode'], lb['mode']} == {'production', 'replay'}) or (la['mode'] == lb['mode'] == 'selftest'),
        '%s / %s' % (la['mode'], lb['mode']))
    ja = {r['name']: r for r in la['jobs']}; jb = {r['name']: r for r in lb['jobs']}
    row('job names', set(ja) == set(jb) == {j['name'] for j in job_table()})
    for n in sorted(set(ja) & set(jb)):
        for k in ('json', 'stdout'):
            fa, fb = os.path.join(a, ja[n][k]), os.path.join(b, jb[n][k])
            same = os.path.exists(fa) and os.path.exists(fb) and sha256(fa) == sha256(fb) and sha256(fa) == ja[n].get(k + '_sha256')
            row('%s %s' % (n, k), same)
    for what, res, detail in rows:
        if res != 'ok' or ' ' not in what:
            print('%-40s %s %s' % (what, res, detail))
    print('files compared: %d' % sum(1 for w, _, _ in rows if w.endswith(' json') or w.endswith(' stdout')))
    print('COMPARE', 'AGREE' if ok else 'DISAGREE')
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('mode', choices=['selftest', 'production', 'replay', 'compare', 'manifest', 'rule-test'])
    ap.add_argument('dirs', nargs='*')
    ap.add_argument('--out'); ap.add_argument('--pi-authorization'); ap.add_argument('--label', default='')
    ap.add_argument('--jobs', type=int, default=2)
    o = ap.parse_args()
    if o.mode == 'manifest':
        write_manifest(); return 0
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
