#!/usr/bin/env python3
"""Bounded receiving controls for PR #113 (SESSION; no owner science).

Supply the unchanged upstream fixtures from PR #113 and one or more checker files.
Every synthetic candidate is exactly derived from its declared map. Identifiers
containing PHANTOM, ALPHA or BETA, and RTG-OPEN-X, are test tokens, not owner RIDs.
Exit 0 means all supplied checkers satisfy the expected safety outcomes; exit 1
means at least one mismatch. No numerical/scientific campaign is executed.
"""
import argparse
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile


def digest(data):
    return hashlib.sha256(data).hexdigest()


def derive(base, operations):
    text = base
    for op in operations:
        if op['op'] == 'edit':
            assert text.count(op['old']) == 1
            text = text.replace(op['old'], op['new'])
        else:
            assert op['op'] == 'replace-section'
            assert text.count(op['start']) == 1
            first = text.index(op['start'])
            last = text.index(op['end'], first + len(op['start'])) if op.get('end') else len(text)
            text = text[:first] + op['new'] + text[last:]
    return text


def fixtures(f):
    profile = {'history_appendix': 'C', 'history_words': ['v0.9']}
    base = f.base_text()
    standard = f.ops('', f.new_appendix(), [f.DRAFTP])
    cases = [('P0', 'positive upstream fixture', base, copy.deepcopy(standard), profile, 'PASS')]
    ops = copy.deepcopy(standard)
    ops[-1]['new'] = f.new_appendix(' `DYAD-THM-PHANTOM`.').replace('## Appendix C —', '## Appendix D —')
    cases.append(('N1', 'declared history appendix missing in candidate', base, ops, profile, 'FAIL'))
    ops = copy.deepcopy(standard)
    ops[-1]['new'] = f.new_appendix().replace('\n---\n\n*END', '\n## 9. Added live claim\n\n`[THM]` [RID: DYAD-THM-PHANTOM] Every object is unique.\n\n---\n\n*END')
    cases.append(('N2', 'history replacement injects a new live theorem', base, ops, profile, 'FAIL'))
    claim = '`[THM]` [RID: DYAD-THM-PRIM-CTR] The following live theorem is protected.\n\n'
    extended = base.replace('\n---\n\n*END', '\n## Appendix D — Live theorem\n\n' + claim + '---\n\n*END')
    cases.append(('N3', 'history replacement deletes following live appendix; RID reference survives', extended, copy.deepcopy(standard), profile, 'FAIL'))
    ops = copy.deepcopy(standard)
    ops[-1]['new'] = f.new_appendix().replace('\n---\n\n*END', '\n## Appendix C — Second history\n\n`DYAD-THM-PHANTOM`.\n\n---\n\n*END')
    cases.append(('N4', 'duplicate history appendix makes phantom self-resolve', base, ops, profile, 'FAIL'))
    ops = f.ops('', f.new_appendix(' `RTG-OPEN-X`.'), [f.DRAFTP])
    cases.append(('N5', 'single-character programme RID description', base, ops, profile, 'FAIL'))
    paragraph = f'The proof source uses `{f.H64}`; historical provenance is audited.\n\n'
    duplicate = base.replace(f.DRAFTP, f.DRAFTP + paragraph).replace('an old scenario', f'an old scenario\n\nhistorical duplicate `{f.H64}`')
    ops = [{'id': 'DROP', 'op': 'edit', 'class': 'history-removal', 'archive': ['base'], 'old': paragraph, 'new': ''}]
    cases.append(('N6', 'default profile loses live source hash; pre-existing history copy masks deletion', duplicate, ops, {}, 'FAIL'))
    return cases


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--fixtures', type=Path, required=True)
    parser.add_argument('--checker', type=Path, action='append', required=True)
    parser.add_argument('--report', type=Path, required=True)
    args = parser.parse_args()
    spec = importlib.util.spec_from_file_location('producer_fixtures', args.fixtures.resolve())
    f = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(f)
    report = {'fixture_sha256': digest(args.fixtures.read_bytes()), 'checkers': []}
    failures = 0
    with tempfile.TemporaryDirectory() as temporary:
        root = Path(temporary)
        for checker in args.checker:
            result = {'checker_sha256': digest(checker.read_bytes()), 'cases': []}
            print('CHECKER', result['checker_sha256'])
            for name, description, base, operations, profile, expected in fixtures(f):
                candidate = derive(base, operations)
                bp, cp, mp, rp = [root / leaf for leaf in ('base.md', 'candidate.md', 'map.json', 'report.json')]
                bp.write_bytes(base.encode('utf-8'))
                cp.write_bytes(candidate.encode('utf-8'))
                mapping = {'base_sha256': digest(bp.read_bytes()), 'candidate_sha256': digest(cp.read_bytes()), 'archives': [{'name': 'base', 'path': str(bp), 'sha256': digest(bp.read_bytes())}], 'profile': profile, 'operations': operations}
                mp.write_text(json.dumps(mapping, ensure_ascii=False, indent=2), encoding='utf-8')
                rp.unlink(missing_ok=True)
                run = subprocess.run([sys.executable, '-I', str(checker.resolve()), str(bp), str(cp), str(mp), '--report', str(rp)], capture_output=True, text=True, timeout=30)
                details = json.loads(rp.read_text(encoding='utf-8')) if rp.exists() else {}
                observed = details.get('result', 'ERROR')
                ok = observed == expected and run.returncode == {'PASS': 0, 'FAIL': 1}[expected]
                failures += not ok
                row = {'id': name, 'description': description, 'expected': expected, 'observed': observed, 'exit_code': run.returncode, 'matched': ok, 'failed_checks': [entry for entry in details.get('checks', []) if entry['result'] != 'PASS']}
                if run.stderr:
                    row['stderr'] = run.stderr
                result['cases'].append(row)
                print(name, 'expected', expected, 'observed', observed, 'MATCH' if ok else 'MISMATCH')
            report['checkers'].append(result)
    report['mismatches'] = failures
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print('MISMATCHES', failures)
    return int(failures != 0)


if __name__ == '__main__':
    sys.exit(main())
