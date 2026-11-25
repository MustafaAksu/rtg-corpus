"""
uvm_i4_t100_pack_diagnostic.py -- I-4 diagnostic (UVM triage row I-4) [SESSION]

Reads OPEN-M-2D/2E microstate packs and prints, per pack, the row that
open_m_2f_trajectory.py (upload/uvm-originals, sha256 4f6a31cf...) prints,
using that script's definitions unchanged:
  GE, GF      = grown_edges, grown_faces (sorted tuples)
  inc[e]      = number of grown faces containing edge e
  is_int      = inc >= 2 ;  nm = #{e : inc > 2}  (equivalently inc >= 3, the
                open_m_2e_panel.py 'nonmanifold' definition on the same complex)
  dimH, z_h   = harmonic space of [B0^T ; B1] on (GE, GF), z_h = H H^T z
  corrFrac    = #(is_int & band(x_link) >= 2) / #is_int
  sig_h_int   = std(z_h[is_int])
It is an independent re-implementation for reading the data, not the original
certificate. Packs are loaded with allow_pickle=False (the two object arrays
z_convention / r_em_formula are not read). Usage:
  python3 -I uvm_i4_t100_pack_diagnostic.py <pack.npz> [<pack.npz> ...]
"""
import sys, os, hashlib, numpy as np

def band(x): return 0 if x < 0.28 else 1 if x < 0.70 else 2 if x < 1.55 else 3

def hodge(GE, GF, z):
    nodes = sorted({n for e in GE for n in e}); nid = {u: i for i, u in enumerate(nodes)}
    eidx = {e: k for k, e in enumerate(GE)}; nE, nF, N = len(GE), len(GF), len(nodes)
    B0 = np.zeros((nE, N))
    for k, (a, b) in enumerate(GE):
        B0[k, nid[a]] = -1; B0[k, nid[b]] = 1
    B1 = np.zeros((nF, nE))
    for fi, (a, b, c) in enumerate(GF):
        for (u, v) in [(a, b), (b, c), (c, a)]:
            B1[fi, eidx[tuple(sorted((u, v)))]] = 1.0 if u < v else -1.0
    M = np.vstack([B0.T, B1]); _, S, Vt = np.linalg.svd(M)
    dimH = int(nE - np.sum(S > max(M.shape) * np.finfo(float).eps * S[0]))
    zh = np.zeros(nE)
    if dimH > 0:
        H = Vt[nE - dimH:].T; zh = H @ (H.T @ z)
    return dimH, zh, N

print(f"{'pack':62s} {'N':>3s} {'nE':>3s} {'nF':>3s} {'nint':>4s} {'corrFrac':>8s} "
      f"{'sig_h_int':>9s} {'nm':>3s} {'dimH':>4s} {'L_zh':>6s}  sha256[:16]")
for path in sys.argv[1:]:
    h = hashlib.sha256(open(path, 'rb').read()).hexdigest()
    d = np.load(path, allow_pickle=False)
    fe = [tuple(sorted((int(a), int(b)))) for a, b in d["edges"]]
    xf = {e: float(d["x_link"][i]) for i, e in enumerate(fe)}
    GE = [tuple(sorted((int(a), int(b)))) for a, b in d["grown_edges"]]
    GF = [tuple(sorted((int(a), int(b), int(c)))) for a, b, c in d["grown_faces"]]
    z = d["z_edge_centered"].astype(float)
    assert len(z) == len(GE), "z_edge_centered not aligned with grown_edges"
    missing = sum(1 for e in GE if e not in xf)
    x = np.array([xf.get(e, np.nan) for e in GE])
    inc = {}
    for (a, b, c) in GF:
        for (u, v) in [(a, b), (b, c), (c, a)]:
            k = tuple(sorted((u, v))); inc[k] = inc.get(k, 0) + 1
    is_int = np.array([inc.get(e, 0) >= 2 for e in GE])
    nm = sum(1 for v in inc.values() if v > 2)
    dimH, zh, N = hodge(GE, GF, z)
    bands = np.array([band(v) for v in x])
    corr = is_int & (bands >= 2)
    cf = corr.sum() / max(is_int.sum(), 1)
    sh = float(np.std(zh[is_int])) if is_int.sum() > 1 else 0.0
    Lzh = float(zh[is_int] @ zh[is_int]) / max(float(zh @ zh), 1e-30)
    name = os.path.basename(path); short = name.replace("open_m_2d_seed_001_rank_2_", "")
    print(f"{short:62s} {N:3d} {len(GE):3d} {len(GF):3d} {int(is_int.sum()):4d} {cf:8.3f} "
          f"{sh:9.4f} {nm:3d} {dimH:4d} {Lzh:6.3f}  {h[:16]}" + (f"  [x_link missing for {missing} edges]" if missing else ""))
