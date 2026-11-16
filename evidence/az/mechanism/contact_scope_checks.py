#!/usr/bin/env python3
"""[SESSION] Independent finite checks for AZ mechanism design PR #281.

Standard library only. No engine imports, registered data, endpoint outcomes, or
campaign runs. Checks the modular solver, review-test coverage, and counterexamples
against an independently implemented direct free-flight scan.
"""
from itertools import combinations
from math import gcd
import json


def pair_time(a: int, b: int, n: int, k: int) -> int | None:
    """Solve the band congruences for the first strictly positive time."""
    if n < 2 or n % 2 or k < 0 or 6 * k >= n:
        raise ValueError("Require even n >= 2 and 0 <= k < n/6")
    a, b = a % n, b % n
    g = gcd(n, b)
    period = n // g
    if period == 1:
        return 1 if min(a, n - a) <= k else None
    inverse = pow(b // g, -1, period)
    times = []
    for error in range(-k, k + 1):
        rhs = error - a
        if rhs % g == 0:
            residue = (rhs // g * inverse) % period
            times.append(residue or period)
    return min(times, default=None)


def pair_scan(a: int, b: int, n: int, k: int) -> int | None:
    for t in range(1, n + 1):
        residue = (a + t * b) % n
        if residue <= k or residue >= n - k:
            return t
    return None


def edges(theta: list[int], delta: list[int], n: int, k: int, t: int):
    phase = [(x + t * v) % n for x, v in zip(theta, delta)]
    return [(i, j) for i, j in combinations(range(len(phase)), 2)
            if n // 2 - k <= (phase[i] - phase[j]) % n <= n // 2 + k]


def first_graph(theta: list[int], delta: list[int], n: int, k: int):
    for t in range(1, n + 1):
        graph = edges(theta, delta, n, k, t)
        if graph:
            return t, graph
    return None, []


def closed(theta: list[int], delta: list[int], n: int, k: int):
    times = [pair_time(theta[i] - theta[j] - n // 2,
                       delta[i] - delta[j], n, k)
             for i, j in combinations(range(len(theta)), 2)]
    return min((t for t in times if t is not None), default=None)


def main() -> None:
    checked = 0
    for n in range(2, 41, 2):
        for k in range((n - 1) // 6 + 1):
            for a in range(n):
                for b in range(n):
                    assert pair_time(a, b, n, k) == pair_scan(a, b, n, k)
                    checked += 1

    # Reproduce the INPUTS of PR #284's targeted cases, not its implementation.
    target_times = {}
    for n, k in ((120, 8), (122, 8), (240, 16), (242, 16), (480, 32)):
        h = n // 2
        cases = [([0, 0, 0, 0], [0, 0, 0, 0]),
                 ([0, h, 3, 7], [5, 5, 9, 11]),
                 ([0, h + k, 1, 2], [0, 0, 0, 0]),
                 ([0, h, 1, 2], [1, 0, 1, 1]),
                 ([0, 1, 2, 3], [0, h, 0, h]),
                 ([0, h - k - 1, 5, 9], [0, n - 1, 0, 0]),
                 ([0, h + 2 * k + 1, 0, h + 2 * k + 1], [0, 1, 0, 1])]
        times = [first_graph(th, de, n, k)[0] for th, de in cases]
        assert times == [closed(th, de, n, k) for th, de in cases]
        assert n not in times
        target_times[f"{n},{k}"] = times

    boundary = ([0, 6, 0, 0], [1, 0, 1, 1], 12, 0)
    assert first_graph(*boundary)[0] == closed(*boundary) == 12
    unreachable = ([0, 1, 0, 1], [0, 2, 0, 2], 12, 0)
    assert first_graph(*unreachable)[0] is None
    assert closed(*unreachable) is None

    th = [109, 97, 80, 2]
    resonant, detuned = [0, 41, 21, 96], [1, 41, 21, 96]
    r, d = first_graph(th, resonant, 120, 8), first_graph(th, detuned, 120, 8)
    assert r == (2, [(1, 2)]) and d == (2, [(0, 1), (1, 2)])
    assert all(0 not in edge for edge in r[1])
    assert any(0 in edge for edge in d[1])
    # Free-contact graph is invariant under a common shift of all advances.
    for c in range(120):
        assert first_graph(th, [(v + c) % 120 for v in resonant], 120, 8) == r
        assert first_graph(th, [(v + c) % 120 for v in detuned], 120, 8) == d

    # A stationary K2,2. Source inspection, not this script, supplies the
    # bound-cycle action and the runner predicate implying fe remains absent.
    cycle_th, cycle_de = [0, 0, 60, 60], [0, 0, 0, 0]
    cycle_graph = [(0, 2), (0, 3), (1, 2), (1, 3)]
    assert all(edges(cycle_th, cycle_de, 120, 8, t) == cycle_graph
               for t in range(1, 121))
    print(json.dumps({
        "status": "PASS", "scope": "synthetic exact arithmetic; no engine or campaign data",
        "exhaustive_pair_cases": checked, "even_N": [2, 40],
        "review_284_targeted_times": target_times,
        "review_284_targeted_exact_t_equals_N_cases": 0,
        "added_boundary_tau": 12, "added_nonzero_relative_advance_unreachable": True,
        "one_arm_absence_fixture": {"N": 120, "k": 8, "slot": 0, "theta": th,
            "delta_R": resonant, "delta_D": detuned,
            "R": {"tau": r[0], "edges": r[1]}, "D": {"tau": d[0], "edges": d[1]}},
        "common_advance_shift_checks": 240,
        "stationary_cycle_graph": cycle_graph,
        "stationary_cycle_ticks_checked": 120,
        "no_growth_endpoint_evaluated": True}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
