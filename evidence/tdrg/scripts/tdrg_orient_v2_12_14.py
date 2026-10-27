#!/usr/bin/env python3
"""Reference implementation of TDRG-DEF-ORIENT as amended in TDR-G v2.12.14 (path orientation rule, option (b)).

Drop-in replacement for `orient_path` in the pinned engine `genesis_mode_b_mc_v18.py` (sha256 9d787b43...675e,
upload/tdrg-records/), same signature and the same counters:

    S = sum_i signed_defect_error(theta[v_i], theta[v_{i+1}], N)
    S > 0 -> forward; S < 0 -> reversed;
    S = 0: E = signed_centered(delta[v_n] - delta[v_1], N)
           0 < E < N/2 -> forward; -N/2 < E < 0 -> reversed;
           2E = 0 (mod N), i.e. E in {0, N/2} -> balanced path-tie (returns None).

The only change against v18 is the last clause: v18 returns "forward" (relative to the node-ID listing produced by
`raw_ordered_path`) when E = N/2, which depends on node labels. Under v2.12.14 that case is a tie, like E = 0.
`orient_g_alternative` is the recorded, NOT adopted, covariant alternative (G-rule on P_3, tie elsewhere), kept for the
later sensitivity campaign. Neither function changes any historical result; the engine itself is not patched in v2.12.14.

usage (as a library):  eng.orient_path = tdrg_orient_v2_12_14.make_orient(eng)
"""


def make_orient(eng):
    """Return the v2.12.14 orient_path bound to an engine module (for signed_centered / signed_defect_error)."""
    sc, sde = eng.signed_centered, eng.signed_defect_error

    def orient_path(path, theta, delta, N, u):
        if len(path) == 2:
            return path
        s = sum(sde(theta[path[i]], theta[path[i + 1]], N) for i in range(len(path) - 1))
        if s > 0:
            return path
        if s < 0:
            return list(reversed(path))
        u.orientation_ties += 1
        e = sc(delta[path[-1]] - delta[path[0]], N)
        if 0 < e < N // 2:
            return path
        if e < 0:
            return list(reversed(path))
        u.path_ties_seen += 1          # e == 0 or e == N/2: (S, E) is reversal-invariant -> balanced path-tie
        return None

    return orient_path


def make_orient_g_alternative(eng):
    """Recorded alternative (a): on S=0, E=N/2 orient P_3 by sign(G), G = sc(d_v1 - d_c) - sc(d_v3 - d_c); tie for n > 3."""
    sc, sde = eng.signed_centered, eng.signed_defect_error

    def orient_path(path, theta, delta, N, u):
        if len(path) == 2:
            return path
        s = sum(sde(theta[path[i]], theta[path[i + 1]], N) for i in range(len(path) - 1))
        if s > 0:
            return path
        if s < 0:
            return list(reversed(path))
        u.orientation_ties += 1
        e = sc(delta[path[-1]] - delta[path[0]], N)
        if 0 < e < N // 2:
            return path
        if e < 0:
            return list(reversed(path))
        if e == N // 2 and len(path) == 3:
            c = path[1]
            g = sc(delta[path[0]] - delta[c], N) - sc(delta[path[2]] - delta[c], N)
            if g == 0:
                raise AssertionError("G = 0 on the stratum contradicts atlas C2")
            return path if g > 0 else list(reversed(path))
        u.path_ties_seen += 1
        return None

    return orient_path
