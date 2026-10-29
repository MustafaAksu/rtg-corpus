#!/usr/bin/env python3
"""recog_v0_3_26_claim_audit.py -- presence of the owner statements the v0.3.26 stage-1 blocks rely on, in the current
owner sources at their adopted tags (Dyadic dyad-v6.4.22; RECOG recog-v0.3.25 for the statements the package corrects
or extends), and presence of the two defects (CORR-1, CORR-2) in the adopted v0.3.25 certificate scripts.

Presence at the cited RID / line in the current source only; not a comparison with earlier editions, not a proof check.
usage (repository root): python evidence/recog/scripts/recog_v0_3_26_claim_audit.py OUT_JSON
"""
import hashlib, json, subprocess, sys

def show(tag, path):
    b = subprocess.run(["git", "show", f"{tag}:{path}"], capture_output=True, check=True).stdout
    return b.decode("utf-8"), hashlib.sha256(b).hexdigest()

DY = "dsn/RTG_DYADIC_OSCILLATOR_DSN.md"; RE = "dsn/RTG_RELATIONAL_RECOGNITION_DSN.md"
CHECKS = [
 # (source, tag, path, label, list of strings that must all be present)
 ("Dyadic", "dyad-v6.4.22", DY, "DYAD-ALG-NF6: the chart coefficients mu, a_32, a_05 whose exact combination 1-|mu|^2-2 Re a_32 = -29/216 and sixth harmonic a_05 enter RECOG-ALG-A1C-RECIPROCAL-DRIFT (i)",
  ["[RID: DYAD-ALG-NF6]", "\\mu=-\\tfrac12-\\tfrac{2i\\sqrt3}{3}", "a_{32}=-\\tfrac{97}{432}+\\tfrac{197i\\sqrt3}{324}", "a_{05}=-\\tfrac{49}{8640}-\\tfrac{307i\\sqrt3}{25920}", "\\mu=6\\bar\\lambda n_{21}", "a_{05}=6\\bar\\lambda n_{05}"]),
 ("Dyadic", "dyad-v6.4.22", DY, "DYAD-THM-NF-REM: C_7=100 on |z|<=1/20 (the dominant part of gamma_2 and K_eps) and the one-orbit contraction (sum_j q_j^2)",
  ["[RID: DYAD-THM-NF-REM]", "C_7=100", "q_0/(1+\\tfrac12q_0m)"]),
 ("Dyadic", "dyad-v6.4.22", DY, "(D5) row-A bridge proof constants c_Q, c'_Q in the LPHASE row-A proof, certified by DYAD-ART-LPHASE-ROWA (ENV [assuming:], through E^(4) and Delta_a)",
  ["[RID: DYAD-THM-LPHASE-ROWA-REMAINDER]", "0.79246", "0.36915", "[RID: DYAD-ART-LPHASE-ROWA]"]),
 ("RECOG", "recog-v0.3.25", RE, "RECOG-ALG-A1C-TAIL-HARMONICS (i), (iii): the limit sentences being corrected (CORR-1) and the untouched items",
  ["[RID: RECOG-ALG-A1C-TAIL-HARMONICS]", "$\\bar S'\\sqrt{a+M}\\to|\\phi_1|/|\\tfrac12+i\\tau|+|\\phi_3|/|\\tfrac12+3i\\tau|=0.74850$ and $\\bar R'\\sqrt{a+M}\\to1.0753$",
   "with $E'\\sqrt{a+M}\\to5.4646$ (part 1: $187.31$);", "(ii) $Q_M\\le\\bar Q_M$ with $\\bar Q_M\\approx1/(a+M)$", "`[ALG via IA]` $E'(a,M)\\le0.31$ for every $a\\ge625$, $M\\ge1$"]),
 ("RECOG", "recog-v0.3.25", RE, "RECOG-THM-A1C-SHARPENED-SCHEDULE: the order sentence being corrected (CORR-1, CORR-2); the display unchanged by the package",
  ["[RID: RECOG-THM-A1C-SHARPENED-SCHEDULE]", "and $E'''(a,M_k,r_k)=O_a\\bigl((1+\\log(a+M_k))/(a+M_k)\\bigr)=o((a+M_k)^{-1/2})$; a pure $O((a+M_k)^{-1})$ is not claimed (the logarithmic term is $\\tau A_1$).",
   "$$c'''_k(a):=\\tau\\,\\psi(a+M_k)-(k-1)\\tfrac\\pi3+\\tfrac{\\sqrt3}8(a+M_k)^{-1/2}+\\tfrac\\tau2(a+M_k)^{-1}=L+\\varepsilon''", "$4.7\\times10^{-5}$ at $10^6$, $5.8\\times10^{-6}$ at $10^7$"]),
 ("RECOG", "recog-v0.3.25", RE, "RECOG-ALG-A1C-START-OFFSET and the centred form E^(4) that ENV extends; Appendix B present with the RETRACTED entry format",
  ["[RID: RECOG-ALG-A1C-START-OFFSET]", "## Appendix B —", "**[RETRACTED | RID: ", "**[FAIL | RID: RECOG-FAIL-K-FROM-SADDLE]**"]),
 ("RECOG", "recog-v0.3.25", "evidence/recog/scripts/recog_a1c_tail_averaging_cert.py", "CORR-1 in the adopted part-1b certificate: Lg carries the M-independent first term b'^{-p}",
  ["def Lg(p, b_, M_):", "return b_**(-p) + n**(1 - p)/(p - 1)*iv.log(1 + M_/(2*b_)) + n**(1 - p)/(p - 1)**2", "A1 = Lam(I(2))/(1 - kappa)"]),
 ("RECOG", "recog-v0.3.25", "evidence/recog/scripts/recog_a1c_combined_tail_cert.py", "CORR-2 in the adopted combined-tail certificate: ref_d uses q_plus with the uniform kappa",
  ["q_plus = 1/((1 - kap_)*(bp + M)); q_minus = 1/(a + Delta_a + M + epsM)", "ref_d = I(max(up(iv.sqrt(q_plus) - n**(-I(1)/2)), up(n**(-I(1)/2) - iv.sqrt(q_minus))))"]),
]

def main():
    out = sys.argv[1] if len(sys.argv) > 1 else "claim_audit.json"
    res = {"sources": {}, "checks": []}; allok = True
    cache = {}
    for src, tag, path, label, needles in CHECKS:
        if (tag, path) not in cache: cache[(tag, path)] = show(tag, path)
        txt, h = cache[(tag, path)]; res["sources"][f"{tag}:{path}"] = h
        missing = [n for n in needles if n not in txt]
        res["checks"].append({"source": src, "tag": tag, "path": path, "label": label, "present": not missing, "missing": missing})
        allok &= not missing
        print(("PRESENT " if not missing else "MISSING ") + f"[{src} {tag}] {label}" + (f" -- missing {missing}" if missing else ""))
    res["ALL_PRESENT"] = allok
    json.dump(res, open(out, "w"), indent=1)
    print("ALL PRESENT" if allok else "NOT ALL PRESENT"); sys.exit(0 if allok else 1)

if __name__ == "__main__":
    main()
