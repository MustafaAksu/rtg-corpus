#!/usr/bin/env python3
"""Run the unchanged round-3 metadata harness against the round-4 checker.
Only CHECKER_SHA256 is updated in memory; original files and test cases stay intact.
"""
import argparse
import hashlib
import importlib.util
from pathlib import Path
import sys

CHECKER = 'd2977b3e24fd54a1d85fe53ea88f65dd51a9e26890b56b17ab5855716b57d87c'
FIXTURE = '45c3cbb5d28d550f2ddae00620b4c759c6aefa51384588c87b6977f951f78ec7'
HARNESS = '7366e17a7db3159846f58ad0f4a23d6e8465add1d2e0785b194b4bf78b9e1c29'


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for name in ('harness', 'checker', 'fixtures', 'out'):
        p.add_argument('--' + name, required=True, type=Path)
    a = p.parse_args()
    for path, expected in ((a.harness, HARNESS), (a.checker, CHECKER), (a.fixtures, FIXTURE)):
        got = hashlib.sha256(path.read_bytes()).hexdigest()
        if got != expected:
            raise SystemExit(f'Input identity mismatch: {path}: {got}')
    spec = importlib.util.spec_from_file_location('original_metadata_harness', a.harness.resolve())
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.CHECKER_SHA256 = CHECKER
    sys.argv = [str(a.harness), '--checker', str(a.checker.resolve()),
                '--fixtures', str(a.fixtures.resolve()), '--out', str(a.out.resolve())]
    return module.main()


if __name__ == '__main__':
    raise SystemExit(main())
