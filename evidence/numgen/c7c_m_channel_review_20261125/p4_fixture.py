# Review check of the #386 §9.3 static P4 fixture with the pinned v18 engine + TDR-G reference orient (one step).
import importlib.util, sys, hashlib
root = sys.argv[1]
def load(n, p):
    s = importlib.util.spec_from_file_location(n, p); m = importlib.util.module_from_spec(s); sys.modules[n] = m; s.loader.exec_module(m); return m
ep, op = f"{root}/upload/tdrg-records/genesis_mode_b_mc_v18.py", f"{root}/evidence/tdrg/scripts/tdrg_orient_v2_12_14.py"
for p in (ep, op): print(p.split('/')[-1], hashlib.sha256(open(p, 'rb').read()).hexdigest()[:16])
eng = load("eng", ep); ref = load("ref", op); eng.orient_path = ref.make_orient(eng)
N, k = 24, 1
pre, dl = (0, 12, 23, 9), (0, 1, 3, 6)
for pol in ("bound_symmetric", "bound_path_tie"):
    u = eng.Universe(N=N, k=k, theta=dict(enumerate(pre)), delta=dict(enumerate(dl)))
    c0 = (u.single_edge_swaps, u.path_interactions, u.path_ties_bound)
    eng.step_universe(u, multistar_policy=pol)
    th = tuple(u.theta[i] for i in range(4)); d = tuple(u.delta[i] for i in range(4))
    print(pol, "post theta", th, "delta'", d, "births", u.births, "counters (swap, path, tie)",
          tuple(a - b for a, b in zip((u.single_edge_swaps, u.path_interactions, u.path_ties_bound), c0)))
post = tuple((a + k * b) % N for a, b in zip(pre, dl)); print("pre+k*delta mod N =", post)
errs = {(i, j): eng.signed_defect_error(post[i], post[j], N) for i in range(4) for j in range(i + 1, 4)}
print("signed defect errors", errs)
