#!/usr/bin/env python3
"""RECOG v0.3.23 stage 1 -- claim-level audit of the Dyadic and NUMGEN imports at their tags (FB-11).

For every load-bearing RECOG import row, the owner text at the current tag is read (git show) and the
statement-carrying strings RECOG quotes are required to occur in the owner text at the cited RID's entry
or section. This is a current-source presence check of the quoted statements (EV-SRC-READ): it does not
compare with the earlier pinned owner editions (most are not in the repository; the earlier comparisons
are RECOG's G2 audits of v0.3.18 and v0.3.21), and it is not a recertification: no owner certificate is rerun. Each row also records RECOG's pin in v0.3.22 and the current owner tag form.

usage (from the repository root):  python -I evidence/recog/scripts/recog_v0_3_23_claim_audit.py OUT_JSON
exit 0 iff every row passes.
"""
import hashlib, json, subprocess, sys

TAGS = {
    "dyad": ("dyad-v6.4.22", "dsn/RTG_DYADIC_OSCILLATOR_DSN.md",
             "2363ca409c08bc571378125771f27239b6426d3e7cdbe75e0306a2a728778c29"),
    "numgen": ("numgen-v1.20.8", "dsn/RTG_NUMBER_GENESIS_DSN.md",
               "835a56f82b2641343a0e2fa116b049a167c62efd4d13fe41236966c117f4817e"),
}

# (row key, RECOG location, owner, owner RID or section, RECOG v0.3.22 pin, current owner tag form,
#  anchor that must occur (RID or heading), list of statement strings that must occur in the owner text)
ROWS = [
 ("C21", "§7 row; §6.2", "dyad", "DYAD-THM-C21", "v6.4.10 §6.2, §6.7", "[THM]",
  "[RID: DYAD-THM-C21]", [r"-\tfrac12-i\tfrac{2\sqrt3}{3}"]),
 ("NF6", "§7 row; §6.14", "dyad", "DYAD-ALG-NF6", "v6.4.10 §6.14", "[ALG]",
  "[RID: DYAD-ALG-NF6]", [r"n_{05}=\tfrac{43}{17280}-\tfrac{227i\sqrt3}{155520}", r"a_{05}=6\bar\lambda n_{05}"]),
 ("NF6-OBS", "§7 row; §6.14", "dyad", "DYAD-ALG-NF6-OBS", "v6.4.10 §6.14", "[ALG]",
  "[RID: DYAD-ALG-NF6-OBS]", [r"\tfrac{-13+3i\sqrt3}{576}"]),
 ("PRIM-CTR", "§7 row; §6.13b; §6.14", "dyad", "DYAD-THM-PRIM-CTR", "v6.4.10 / v6.4.16 §6.14", "[THM]",
  "[RID: DYAD-THM-PRIM-CTR]", [r"|R^{\rm prim}_{\ge6,\rm rad}(x)|\le108\,Q(x)^3", r"\tfrac1{400}", r"U=\{0<Q\le\tfrac1{625}\}",
   r"\tfrac{16931}{10000}Q^{5/2}", r"\tfrac{47}{1000}", r"Q_m\le Q_0/(1+\tfrac12Q_0m)", r"\sum_mQ_m^3\le2Q_0^2"]),
 ("NF-INV", "§7 row; §6.13b; §6.14", "dyad", "DYAD-THM-NF-INV", "v6.4.10 / v6.4.16 §6.14", "[THM]",
  "[RID: DYAD-THM-NF-INV]", [r"\|Dh^{-1}\|_2<\tfrac87", r"\tfrac{15}{16}|z|\le|h(z)|\le\tfrac{17}{16}|z|",
   r"\tfrac{225}{256}|z|^2\le Q_{\rm prim}", r"\le\tfrac{289}{256}|z|^2"]),
 ("NF-REM", "§7 row; §6.14", "dyad", "DYAD-THM-NF-REM", "v6.4.10 §6.14", "[THM]",
  "[RID: DYAD-THM-NF-REM]", [r"$C_7=100$ (certificate value $85.07$)", r"$C_D=1000$", r"$C_7=30$ (certificate value $27.60$)", r"$C_D=250$"]),
 ("BRIDGE", "§7 rows; §6.10", "dyad", "DYAD-ALG-BRIDGE-LEMMA", "Dyadic §6.9", "[ALG]",
  "[RID: DYAD-ALG-BRIDGE-LEMMA]", [r"\mu_p = p\bar\lambda\nu_3^{(1,p)}"]),
 ("KP-FRAME", "§1; §2 R2; §4; §6.2; §6.10 (new citation)", "dyad", "DYAD-ALG-KP-FRAME-SCALE", "(not cited in v0.3.22)", "[ALG]",
  "[RID: DYAD-ALG-KP-FRAME-SCALE]", [r"W_p=i\cot(\pi/p)\,Z", r"\nu_3^{Z}=\cot^2(\pi/p)\,\nu_3^{W_p}", r"\mu_6^Z=3\mu_6^W"]),
 ("FACEFLUX", "§7 row", "dyad", "DYAD-ALG-P6-FACEFLUX", "Dyadic §6.2", "[ALG]",
  "[RID: DYAD-ALG-P6-FACEFLUX]", [r"e^{iF_f/2}"]),
 ("PRIMITIVE-MAP", "§7 row (§6.1 block)", "dyad", "DYAD-DEF-PRIMITIVE-MAP", "Dyadic §6.1", "[DEF]",
  "[RID: DYAD-DEF-PRIMITIVE-MAP]", [r"\rho' = \rho - \sin\eta, \qquad \eta' = \eta + (e^\rho - 1) - \sin\eta", r"\det J=1+(e^\rho-1)\cos\eta"]),
 ("CRITICAL-CURVE", "§7 row (§6.1 block)", "dyad", "DYAD-DEF-CRITICAL-CURVE", "Dyadic §6.1 (no RID then)", "[DEF]",
  "[RID: DYAD-DEF-CRITICAL-CURVE]", [r"C_0:=\{\det DT=0\}", r"k=(\cos\eta,1)"]),
 ("QC", "§7 row (§6.4 block); §6.15c", "dyad", "DYAD-ALG-QC-CRITICAL-AMPLITUDE", "v6.4.10 §4 / §6.4 (no RID then)", "[ALG]",
  "[RID: DYAD-ALG-QC-CRITICAL-AMPLITUDE]", [r"Q_c := (\arcsin(\ln 2))^2", r"If $Q < Q_c$ at pre-crossing, critical curve is unreachable at the crossing step."]),
 ("ISP", "§7 row (§6.4 block)", "dyad", "DYAD-ALG-ISP-MAPS", "Dyadic §6.4 (no RID then)", "[ALG]",
  "[RID: DYAD-ALG-ISP-MAPS]", [r"\Theta=\text{atan2}(\sqrt3\eta_{\rm wrap},2\rho-\eta_{\rm wrap})", r"**Winding-index invisibility.**"]),
 ("SIXSTEP-JET", "§7 row (§6.7/§6.8 block)", "dyad", "DYAD-ALG-SIXSTEP-CUBIC-JET", "Dyadic §6.7–6.8 (no RID then)", "[ALG]",
  "[RID: DYAD-ALG-SIXSTEP-CUBIC-JET]", [r"M+M^T=-I", r"\Theta_{m+1}=\Theta_m-\tau Q_m"]),
 ("RAW-MEAN", "§7 row (§6.5)", "dyad", "DYAD-ALG-RAW-ANGULAR-MEAN", "v6.4.10 §6.5 (no RID then)", "[ALG]",
  "[RID: DYAD-ALG-RAW-ANGULAR-MEAN]", [r"\tfrac{47}{54}"]),
 ("LIEGAUGE", "§7 row", "dyad", "DYAD-ALG-LIEGAUGE-NORM", "Dyadic §6.9", "[ALG] [conv: Lie strict-kernel gauge]",
  "[RID: DYAD-ALG-LIEGAUGE-NORM]", [r"c_{05}^{({\rm raw},6\text{-step})}=-61/2160-i\,43\sqrt{3}/6480"]),
 ("ALIAS", "§7 row", "dyad", "DYAD-ALG-ALIAS-PHASE", "Dyadic OPEN 16", "[ALG]",
  "[RID: DYAD-ALG-ALIAS-PHASE]", [r"G_-(\pi/\tau) = 1/(1-i\tau)"]),
 ("CONSTANTS", "§7 row (Dyadic §6.3); §6.13 lattice clock", "dyad", "Dyadic §6.3 constants (no RID)", "Dyadic §6.3", "[ALG]",
  r"R^*=\exp(\pi/\tau)\approx15.1909377", [r"\lambda_{\rm DSI}=e^{\pi\sqrt3}", r"\tau=\tfrac{2\sqrt3}{3}"]),
 ("H2", "§7 row (Dyadic §6.2 $h_2$); §6.13 frame correction", "dyad", "DYAD-ALG-NF6 ($h_2$ entry; no separate RID)", "Dyadic §6.2", "[ALG]",
  "[RID: DYAD-ALG-NF6]", [r"h_2=-\tfrac{1+i\sqrt3}{12}z^2-\tfrac13z\bar z+\tfrac{1-i\sqrt3}{24}\bar z^2"]),
 ("FIXED-POINTS", "§6.3 (FA-04)", "dyad", "§1 fixed-point scope table", "Dyadic §6.1", "[ALG]",
  "**Fixed-point scope.**", [r"$(\log(1+2\pi k),0)$ and $(\log(1+2\pi k),\pi)$", r"The winding inventory agrees with RECOG §6.3"]),
 ("OFFSET", "§6.13b; §7 row", "dyad", "DYAD-ALG-OPEN3-PHASE-OFFSET", "v6.4.16 §6.14 (v6.4.15 entries); primitive-variable form v6.4.18 lines 806–809",
  "[ALG]; primitive-variable form [ALG] [scope: formal second order; remainder certified separately, OPEN 21]",
  "[RID: DYAD-ALG-OPEN3-PHASE-OFFSET]", [r"(P4-0) $\Psi_W(m)-\Psi_z(m)=\Delta_0(z_m)$",
   r"\tfrac{17\sqrt3}{36}\cos\Theta-\tfrac1{12}\sin\Theta-\tfrac{7\sqrt3}{72}\cos3\Theta+\tfrac18\sin3\Theta",
   r"`[ALG]` `[scope: formal second order; remainder certified separately, OPEN 21]` **Primitive-variable form.**",
   r"P_{W2}=-\Delta_2+D\Delta_1[h_2]=|W|^2\bigl[-\tfrac{5\sqrt3}{27}+\tfrac{47\sqrt3}{1296}\cos2\Theta-\tfrac{19}{432}\sin2\Theta-\tfrac{11\sqrt3}{324}\cos4\Theta+\tfrac1{54}\sin4\Theta-\tfrac{\sqrt3}{1728}\cos6\Theta-\tfrac5{576}\sin6\Theta\bigr]"]),
 ("OFFSET-BOUNDS", "§6.13b; §7 row", "dyad", "DYAD-THM-OPEN3-PHASE-OFFSET-BOUNDS", "v6.4.16 §6.14", "[THM]",
  "[RID: DYAD-THM-OPEN3-PHASE-OFFSET-BOUNDS]", [r"\tfrac{1101}{1000}", r"\tfrac{533}{500}"]),
 ("T1T2", "§3 SG-R14; §6.13b; §7 row", "dyad", "DYAD-THM-OPEN3-ASYMPTOTIC-PHASE", "v6.4.15 / v6.4.16 §6.14",
  "T1 [THM] [assuming: RECOG-THM-R9-MEMORY]; T2 [THM] [assuming: T1]",
  "[RID: DYAD-THM-OPEN3-ASYMPTOTIC-PHASE]", [r"**T1 (limit equality)** `[THM]` `[assuming: RECOG-THM-R9-MEMORY]`",
   r"**T2 (finite-start offset)** `[THM]` `[assuming: T1]`: $M_W-M=-\Delta_0(z_0)$", r"$|M_W-M|\le K_0\sqrt{q_0}$"]),
 ("OPEN21", "§6.13b; §7 row", "dyad", "DYAD-THM-OPEN21-PRIMITIVE-PHASE-REMAINDER", "v6.4.18 §6.14 lines 843–850",
  "[THM] [assuming: RECOG-THM-R9-MEMORY]",
  "`[THM]` `[assuming: RECOG-THM-R9-MEMORY]` [RID: DYAD-THM-OPEN21-PRIMITIVE-PHASE-REMAINDER]",
  [r"|M_W-\mathcal P_2(W_0)|\le K'_jQ_0^{3/2}+C_{2,j}\bigl(\tfrac{256}{225}\bigr)^2Q_0^2",
   r"| A | $\lvert z\rvert\le\tfrac1{20}$ | $\tfrac3{64}$ | $\tfrac{3951}{1000}$ | $517$ |",
   r"| B | $\lvert z\rvert\le\tfrac1{40}$ | $\tfrac3{128}$ | $\tfrac{971}{250}$ | $163$ |"]),
 ("LPHASE-ROWA", "§6.13b RECOG-THM-A1A-PHASE-EXISTENCE-U (FC-21; new import)", "dyad", "DYAD-THM-LPHASE-ROWA-REMAINDER", "(not cited in v0.3.22)",
  "[THM] [scope: block base points in U; row A]",
  "[RID: DYAD-THM-LPHASE-ROWA-REMAINDER]", [r"\hat\varphi_{6(m+1)}-\hat\varphi_{6m}=2\pi-\tau Q_m+r_m,\qquad |r_m|\le\tfrac{403}{250}\,Q_m^{3/2}",
   r"$\varepsilon\le0.04654$", r"$\hat\varphi$ is the increasing lift whose one-step increments are $\delta_T$",
   r"Domain: block base points in $U$, intermediate steps in $U_T$", r"Block base points stay in $U$ ($F(U)\subset U$)"]),
 ("SH-R0", "§6.14 (FB-16)", "dyad", "§6.15 Relation to S_h; DYAD-THM-SMOOTH-EMBEDDING", "(not cited in v0.3.22)", "[DEF]; [THM] [scope: C-infinity local germs]",
  "[RID: DYAD-THM-SMOOTH-EMBEDDING]", [r"$S_h$ remains a finite chart object (equal to $R_0$ through degree 6)",
   r"$R:=T^3\circ K_2^{-1}$ is a $C^\infty$ local involution with $DR(0)=-I$, $RT=TR$",
   r"the unique formal involution with linear part $-I$ commuting with $F$ is $R_0=T^3\circ F^{-1/2}$"]),
 ("NF6-DEG10", "VF-1 citation (routed item)", "dyad", "DYAD-ALG-NF6-DEG10", "(RRF label VF-1)", "[ALG]",
  "[RID: DYAD-ALG-NF6-DEG10]", [r"registered in RRF v0.8 as finding VF-1"]),
 # NUMGEN
 ("NG-DEFECT", "§6.13b; §7 row (A1a)", "numgen", "NUMGEN-DEF-N5AS1-DEFECT", "v1.20.7 §6.6, RID unavailable", "[DEF]",
  "[RID: NUMGEN-DEF-N5AS1-DEFECT]", [r"`D_M := 2 pi M - (phi_hat_(6M) - phi_hat_0)`", r"D_M := 2 pi M - (phi_hat_(6M)-phi_hat_0),"]),
 ("NG-LIFT", "§6.13b (definition of the lift)", "numgen", "NUMGEN-DEF-N5AS1-PRIMITIVE-LIFT", "(no RID in v1.20.7)", "[DEF]",
  "[RID: NUMGEN-DEF-N5AS1-PRIMITIVE-LIFT]", [r"phi_hat_(n+1) = phi_hat_n + delta_T(T^n x),   delta_T(y) := Arg( W(Ty) / W(y) )   (principal value).",
   r"(`pi/6 < delta_T < pi/2`)"]),
 ("NG-INF1", "§6.13b; §7 row (A1a)", "numgen", "NUMGEN-RESULT-N5AS1-INF1", "v1.20.7 §6.6, RID unavailable", "[RESULT] [from: ALG]",
  "`[RESULT] [from: ALG]` [RID: NUMGEN-RESULT-N5AS1-INF1]", [r"D_M = tau log M + C_D + o(1) -> infinity.", r"L-BACKBONE and L-PHASE give",
   r"Allocation of the six N-5A-S1 RIDs changes no statement, proof, domain or grade."]),
 ("NG-RATIO", "§6.13; §7 row", "numgen", "NUMGEN-THM-N5AS1-DEFECT-THRESHOLD-RATIO", "v1.20.7", "[RESULT] [from: ALG]",
  "**RID:** `NUMGEN-THM-N5AS1-DEFECT-THRESHOLD-RATIO`", [r"M_(k+1)^(def) / M_k^(def) -> exp(pi/(3 tau))", r"= exp(sqrt(3) pi/6)."]),
 ("NG-L1", "§6.2; §7 row", "numgen", "NUMGEN-RESULT-L1-PRIMITIVE-CONTRACTION", "v1.15 (source pin), v1.20.7 current at v0.3.22", "[ALG]",
  "**RID:** `NUMGEN-RESULT-L1-PRIMITIVE-CONTRACTION`", [r"Delta Q_true=-Q_true^2+O(Q_true^(5/2))"]),
 ("NG-N1C", "§6.5; §7 row", "numgen", "NUMGEN-OPEN-N1C", "v1.15 (source pin), v1.20.7 current at v0.3.22", "CLOSED [RESULT][from: ALG]",
  "**RID:** `NUMGEN-OPEN-N1C`", [r"**Pure wrapped-state recurrence does not close N-1C.**"]),
 ("NG-GAPLOCK3", "§2 R6 (HEUR cross-reference); §6.16e", "numgen", "GAP-LOCK Lemma 3 (no RID)", "v1.20.7", "[ALG] (owner)",
  "GAP-LOCK Lemma 3", [r"**GAP-LOCK Lemma 3** is now CLOSED `[ALG]`", r"No theorem-level change."]),
]

def show(tag, path):
    return subprocess.run(["git", "show", f"{tag}:{path}"], check=True, capture_output=True).stdout

def main(out):
    src, ids = {}, {}
    for k, (tag, path, sha) in TAGS.items():
        b = show(tag, path)
        got = hashlib.sha256(b).hexdigest()
        assert got == sha, f"{tag}: sha {got} != {sha}"
        src[k] = b.decode("utf-8"); ids[k] = {"tag": tag, "path": path, "sha256": got}
    rows, ok = [], True
    for key, loc, owner, rid, pin, tagform, anchor, pats in ROWS:
        text = src[owner]
        a = anchor in text
        miss = [p for p in pats if p not in text]
        good = a and not miss
        ok &= good
        rows.append({"key": key, "recog_location": loc, "owner": ids[owner]["tag"], "owner_rid_or_section": rid,
                     "recog_v0_3_22_pin": pin, "current_owner_tag_form": tagform, "anchor_found": a,
                     "statement_strings": len(pats), "missing": miss,
                     "class": "P (quoted statement present at the current tag)" if good else "CHECK"})
    json.dump({"sources": ids, "rows": rows, "all_pass": ok,
               "evidence_state": "EV-SRC-READ: current-source presence of the quoted statements; no comparison with earlier pinned editions; no owner certificate rerun"},
              open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    for r in rows:
        print(("PASS " if not r["missing"] and r["anchor_found"] else "FAIL ") + r["key"], r["missing"] or "")
    print("ALL PASS" if ok else "FAILURES", f"({len(rows)} rows)")
    sys.exit(0 if ok else 1)

if __name__ == "__main__":
    main(sys.argv[1])
