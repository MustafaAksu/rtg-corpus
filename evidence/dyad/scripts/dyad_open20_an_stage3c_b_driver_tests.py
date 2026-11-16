#!/usr/bin/env python3
"""dyad_open20_an_stage3c_b_driver_tests.py -- tests of the stage-3c-b driver itself (no mathematics, no campaign).

Written for the co-owner's review 5915522711 of PR #273 (findings R1-R3).  Seconds to run; standard library only.

  RULE      the driver's own rule test (16 synthetic ledgers, among them the three of R1).
  FIXTURE   a run directory assembled from the committed reference outputs (that is what an accepted selftest
            contains) with a ledger written by the driver's own writer is VALID; so the gate schema matches the
            committed outputs of every job.
  COMPARE   (R2) compare of the fixture with an unchanged copy: AGREE.  Each of the following changes, made to the
            copy only, must give DISAGREE: a wrong JSON hash in the ledger; a job recorded twice; the exit code of a
            positive process set to 7; a gate set to false in the ledger only; one byte of one output changed (with
            SHA256SUMS renewed, so only the content check can see it); one output deleted; the stored verdict changed
            to ACCEPTED on a directory whose outputs say otherwise.
  WORKER    (R3) a small job table of throw-away scripts run by run_jobs with a time limit: a job whose output is the
            JSON value [] becomes an error record; a job whose output is not JSON becomes an error record; a job that
            depends on a failed job is recorded as skipped and not run; a job that passes runs; every job has exactly
            one record; the run ends; the rule rejects.
  GIT       (R3) with git answering rev-parse but failing status (exit 128), the strict check stops and the non-strict
            check reports the tree as not clean; with both answering and no changes it is clean.

Usage:  python3 -I -B evidence/dyad/scripts/dyad_open20_an_stage3c_b_driver_tests.py --out OUT.json
Exit 0 iff every test passes.
"""
import os, sys, json, shutil, tempfile, threading, argparse, subprocess, types
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import dyad_open20_an_stage3c_b_run as R


def fixture(d):
    """A run directory from the committed reference outputs, with a ledger in the driver's format."""
    os.makedirs(d)
    recs = []
    for j in R.job_table():
        shutil.copyfile(os.path.join(R.ROOT, j['ref']), os.path.join(d, j['stem'] + '.json'))
        shutil.copyfile(os.path.join(R.ROOT, j['ref'][:-5] + '.stdout.txt'), os.path.join(d, j['stem'] + '.stdout.txt'))
        rec = dict(name=j['name'], kind='positive' if j['expect'] == 0 else 'control', expected_exit=j['expect'],
                   exit=j['expect'], json=j['stem'] + '.json', stdout=j['stem'] + '.stdout.txt', seconds=0.0)
        R.read_output(rec, os.path.join(d, j['stem'] + '.json'))
        rec['stdout_sha256'] = R.sha256(os.path.join(d, j['stem'] + '.stdout.txt'))
        recs.append(rec)
    R.compare_refs(R.job_table(), recs, d)
    ok, why = R.verdict(R.job_table(), recs, True, R.load_schema())
    led = dict(package=R.PACKAGE_ID, mode='selftest', label='driver-test fixture', pi_authorization=None,
               scope=R.SCOPE['selftest'], manifest=dict(sha256=R.sha256(os.path.join(R.ROOT, R.MANIFEST))), jobs=recs,
               verdict='ACCEPTED' if ok else 'REJECTED', reasons=why)
    R.write_ledger(d, led)
    return ok, why


def quiet(f, *a):
    import io, contextlib
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        rc = f(*a)
    return rc, buf.getvalue()


def edit_ledger(d, f, renew_sums=True):
    p = os.path.join(d, 'LEDGER.json')
    led = json.load(open(p, encoding='utf-8')); f(led)
    with open(p, 'w', encoding='utf-8', newline='\n') as fh:
        json.dump(led, fh, indent=1, sort_keys=True); fh.write('\n')
    if renew_sums:
        renew(d)


def renew(d):
    names = sorted(n for n in os.listdir(d) if n != 'SHA256SUMS.txt')
    with open(os.path.join(d, 'SHA256SUMS.txt'), 'w', encoding='utf-8', newline='\n') as fh:
        for n in names:
            fh.write('%s  %s\n' % (R.sha256(os.path.join(d, n)), n))


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--out', required=True); o = ap.parse_args()
    res, ok_all = {}, True
    def gate(name, ok, info):
        nonlocal ok_all
        res[name] = dict(pass_=bool(ok), info=info); ok_all = ok_all and bool(ok)
        print('%-8s %s' % (name, 'PASS' if ok else 'FAIL'))

    ok, rule = R.rule_test()
    gate('RULE', ok and len(rule) == 16, rule)

    tmp = tempfile.mkdtemp(prefix='dyad3cb_tests_')
    try:
        A = os.path.join(tmp, 'A')
        ok_fx, why_fx = fixture(A)
        v, why, _ = R.validate_dir(A)
        gate('FIXTURE', ok_fx and v, dict(fixture_verdict_reasons=why_fx, validate_reasons=why))

        rows = []
        B = os.path.join(tmp, 'B'); shutil.copytree(A, B)
        rc, _ = quiet(R.compare, A, B); rows.append(('unchanged copy', 'AGREE' if rc == 0 else 'DISAGREE', 'AGREE'))
        T = R.job_table(); pos = next(j for j in T if j['expect'] == 0)
        def wrong_hash(l): l['jobs'][0]['json_sha256'] = '0' * 64
        def dup(l): l['jobs'].append(dict(l['jobs'][0]))
        def exit7(l): next(r for r in l['jobs'] if r['name'] == pos['name']).update(exit=7)
        def gate_false(l):
            r = next(r for r in l['jobs'] if r['name'] == pos['name']); k = sorted(r['gates'])[0]; r['gates'][k] = False
        tampers = [('wrong JSON hash in the ledger', lambda d: edit_ledger(d, wrong_hash)),
                   ('job recorded twice', lambda d: edit_ledger(d, dup)),
                   ('exit code of a positive process set to 7', lambda d: edit_ledger(d, exit7)),
                   ('a gate set to false in the ledger only', lambda d: edit_ledger(d, gate_false))]
        def byte(d):
            p = os.path.join(d, pos['stem'] + '.stdout.txt'); b = bytearray(open(p, 'rb').read()); b[0] ^= 1
            open(p, 'wb').write(bytes(b)); renew(d)
        def delete(d):
            os.remove(os.path.join(d, pos['stem'] + '.json')); renew(d)
        def forged_verdict(d):
            p = os.path.join(d, pos['stem'] + '.json'); x = json.load(open(p))
            k = sorted(x['gates'])[0]; x['gates'][k] = False; x['all_pass'] = False
            json.dump(x, open(p, 'w'), indent=1, sort_keys=True)
            def f(l):
                r = next(r for r in l['jobs'] if r['name'] == pos['name']); r['gates'] = x['gates']; r['all_pass'] = False
                r['json_sha256'] = R.sha256(p)
            edit_ledger(d, f)
        tampers += [('one byte of one printed output changed, SHA256SUMS renewed', byte),
                    ('one output deleted, SHA256SUMS renewed', delete),
                    ('an output with a false gate under a stored ACCEPTED verdict', forged_verdict)]
        for name, f in tampers:
            C = os.path.join(tmp, 'C'); shutil.rmtree(C, ignore_errors=True); shutil.copytree(A, C); f(C)
            rc, _ = quiet(R.compare, A, C)
            rows.append((name, 'AGREE' if rc == 0 else 'DISAGREE', 'DISAGREE'))
        gate('COMPARE', all(g == w for _, g, w in rows), [dict(case=n, got=g, expected=w) for n, g, w in rows])

        # WORKER
        W = os.path.join(tmp, 'W'); os.makedirs(W); S = os.path.join(tmp, 'scripts'); os.makedirs(S)
        def script(name, body):
            p = os.path.join(S, name + '.py')
            open(p, 'w').write('import sys, json\nout = sys.argv[sys.argv.index("--out") + 1]\n' + body + '\n')
            return p
        sl = script('list', 'open(out, "w").write("[]"); sys.exit(0)')
        sn = script('notjson', 'open(out, "w").write("not json"); sys.exit(0)')
        sg = script('good', 'json.dump({"gates": {"A": True}, "all_pass": True}, open(out, "w")); sys.exit(0)')
        table = [dict(name='t_list', expect=0, script=sl, args=[], stem='t_list', ref='', deps=[]),
                 dict(name='t_dep', expect=0, script=sg, args=[], stem='t_dep', ref='', deps=['t_list']),
                 dict(name='t_notjson', expect=0, script=sn, args=[], stem='t_notjson', ref='', deps=[]),
                 dict(name='t_good', expect=0, script=sg, args=[], stem='t_good', ref='', deps=[])]
        schema = {t['name']: dict(gates=['A'], false=[]) for t in table}
        out = {}
        th = threading.Thread(target=lambda: out.update(recs=R.run_jobs(table, W, False, 2, schema)), daemon=True)
        quiet(lambda: (th.start(), th.join(60)))
        recs = out.get('recs')
        by = {r['name']: r for r in (recs or [])}
        okw = (recs is not None and not th.is_alive() and len(recs) == 4 and len(by) == 4
               and 'not a JSON object' in (by['t_list'].get('error') or '')
               and 'not valid JSON' in (by['t_notjson'].get('error') or '')
               and 'dependency t_list' in (by['t_dep'].get('skipped') or '') and not os.path.exists(os.path.join(W, 't_dep.json'))
               and by['t_good'].get('exit') == 0 and not by['t_good'].get('error'))
        acc, why = R.verdict(table, recs or [], False, schema)
        gate('WORKER', okw and not acc and len(why) == 3, dict(ended=not th.is_alive(), records=recs, reasons=why))

        # GIT
        real = R.subprocess.run
        def fake(fail_status):
            def run(cmd, **kw):
                if cmd[:1] == ['git'] and 'status' in cmd and fail_status:
                    return types.SimpleNamespace(returncode=128, stdout='', stderr='fatal')
                if cmd[:1] == ['git'] and 'status' in cmd:
                    return types.SimpleNamespace(returncode=0, stdout='', stderr='')
                if cmd[:1] == ['git']:
                    return types.SimpleNamespace(returncode=0, stdout='0123abcd\n', stderr='')
                return real(cmd, **kw)
            return run
        rows = []
        try:
            R.subprocess.run = fake(True)
            try:
                R.git_state(strict=True); stopped = False
            except SystemExit:
                stopped = True
            st = R.git_state(strict=False)
            rows.append(dict(case='status fails (128)', strict_stopped=stopped, non_strict_clean=st['clean']))
            R.subprocess.run = fake(False)
            st2 = R.git_state(strict=True)
            rows.append(dict(case='both answer, no changes', strict_clean=st2['clean']))
        finally:
            R.subprocess.run = real
        gate('GIT', rows[0]['strict_stopped'] and rows[0]['non_strict_clean'] is False and rows[1]['strict_clean'] is True, rows)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    with open(o.out, 'w', encoding='utf-8', newline='\n') as f:
        json.dump(dict(script='dyad_open20_an_stage3c_b_driver_tests.py', all_pass=ok_all, tests=res,
                       status='tests of the driver of stage 3c-b; no mathematics; not a run'), f, indent=1, sort_keys=True,
                  default=str)
        f.write('\n')
    print('RESULT', 'PASS' if ok_all else 'FAIL')
    return 0 if ok_all else 1


if __name__ == '__main__':
    sys.exit(main())
