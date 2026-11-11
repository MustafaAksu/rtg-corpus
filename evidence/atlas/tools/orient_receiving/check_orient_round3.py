#!/usr/bin/env python3
"""Replay the unchanged PR190 round-2 21+6 contracts on revision 3.

Only TOOL_SHA and TOOL_BLOB are repinned in memory. The round-2 runner is
hash-checked and itself checks the original 21-contract harness by hash.
Forward --tool PATH, --harness PATH and --out DIR to that runner. Neither
reporter source nor any fixture/predicate is modified. No live network calls.
"""
from __future__ import annotations
import hashlib
import importlib.util
from pathlib import Path

RUNNER_SHA = '14ca8cb3f32c7d5fb09e926e97187c463c43f947ac85ac09e5f6193029e4cc7e'
TOOL_SHA = 'dfbcb1da0a7ac4d3ec942cae4a125875caa1030ddebd103821bf5c75b0c5cd0c'
TOOL_BLOB = '6848b4f0c15713f6063be797a396f066f4dafa06'


def main() -> None:
    runner = Path(__file__).with_name('check_orient_round2.py')
    if hashlib.sha256(runner.read_bytes()).hexdigest() != RUNNER_SHA:
        raise SystemExit('Unexpected round-2 runner; refusing altered tests')
    spec = importlib.util.spec_from_file_location('orient_round2_unchanged', runner)
    if spec is None or spec.loader is None:
        raise SystemExit('Cannot load the pinned round-2 runner')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.TOOL_SHA, module.TOOL_BLOB = TOOL_SHA, TOOL_BLOB
    module.main()


if __name__ == '__main__':
    main()
