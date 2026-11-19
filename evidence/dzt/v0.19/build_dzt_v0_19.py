#!/usr/bin/env python3
"""DZT v0.19: the all-p amplitude-norm theorem, built from the tagged v0.18 bytes.

    python3 -I evidence/dzt/v0.19/build_dzt_v0_19.py [--out PATH] [--log PATH]

Reads the base with `git show dzt-v0.18:<DSN>` and asserts its SHA-256. Each edit replaces a text
span that must occur exactly once in the current text; a missing or repeated span stops the build.

Scope (PI decisions of 20 Nov 2026 on records/dzt/DZT_NORM_LAW_OWNER_REVIEW.md §8):
  1. grade `[THM]` `[assuming: DYAD-THM-Q403-PHASELAW]` for the combined statement;
  2. a new RID for it (DZT-THM-CASCADE-NORM-LAW);
  3. entry by a new edition, which closes DZT-OPEN-NORM-LAW (Methodology §5.2: proof in §6,
     one-line closed reference at the end of §2, §1 updated), retires the `[HYP]` mechanism of the
     mod-4 gate into Appendix B, and registers the review check in §8.
The layout is already Methodology v1.4 (v0.18); there is no compaction stage. No other claim or grade
changes; the sign of N_+ stays outside the theorem.
"""
import argparse
import hashlib
import subprocess
import sys

DSN = "dsn/RTG_DYADIC_ARITHMETIC_RESONANCE_TRANSFORM_DSN.md"
BASE_TAG = "dzt-v0.18"
BASE_SHA = "04581d1e8d8a187ec231d670d9639591e2b8d3aefb9834d5dd9f5cdf792a8dee"
THM = "DZT-THM-CASCADE-NORM-LAW"
LOG = []


def sha(b):
    return hashlib.sha256(b).hexdigest()


def die(msg):
    sys.stderr.write("BUILD STOP: %s\n" % msg)
    sys.exit(1)


def edit(t, key, old, new, note):
    n = t.count(old)
    if n != 1:
        die("%s: span occurs %d times: %r" % (key, n, old[:80]))
    i = t.index(old)
    LOG.append((key, t[:i].count("\n") + 1, sha(old.encode())[:16], len(old), len(new), note))
    return t.replace(old, new)


THEOREM = r"""`[THM]` `[assuming: DYAD-THM-Q403-PHASELAW]` `[proof: written derivation]` `[RID: DZT-THM-CASCADE-NORM-LAW]` **Amplitude-norm law.** For every $p=4s\ge12$,
$$\lvert N_+(M_p)\rvert=\frac{\ell(p)^2}{2^{d_p}},\qquad d_p=\frac{\varphi(p)}{4}+[p=2^k]+[p=3\cdot2^k],$$
where $\ell(p)=\ell$ if $p=8\ell^a$ with $\ell$ an odd prime and $\ell^a\equiv1\!\pmod4$, and $\ell(p)=1$ otherwise. Hence the odd part of the numerator is $\ell^2$ exactly at the points $p=8\ell^a$, $\ell^a\equiv1\!\pmod4$, and $1$ elsewhere; the denominator is always $2^{d_p}$; on that set $\lvert N_+(M_{8\ell^a})\rvert=\ell^2/2^{\varphi(\ell^a)}$. The sign of $N_+(M_p)$ is not part of the statement. The assumption is the imported closed form of $Q_p$ (§7); $L=\zeta_p$ and $I=L^s$ are field elements of $K=\mathbb{Q}(\zeta_p)$.
*Proof.* (i) Roots of unity in $K$ have norm 1 and $M_p\in K^+$, so $N_+(M_p)^2=N_{K/\mathbb{Q}}(M_p)=N_{K/\mathbb{Q}}(A_s)\big/\big(N_{K/\mathbb{Q}}(2)\,N_{K/\mathbb{Q}}(L+1)^4\,N_{K/\mathbb{Q}}(L^2+L+1)\big)$ with $A_s=IL^2+I-L^2+1$. (ii) $A_s=(I-1)(L^2-I)$ and $L^2-I=L^2(1-L^{s-2})$. (iii) `[MATH]` For $\eta\in K$ of exact order $n>1$: $N_{K/\mathbb{Q}}(1-\eta)=\Phi_n(1)^{\varphi(p)/\varphi(n)}$, with $\Phi_n(1)=\ell$ if $n=\ell^a$ and $\Phi_n(1)=1$ otherwise. (iv) By (iii): $N(2)=2^{\varphi(p)}$; $N(I-1)=2^{\varphi(p)/2}$ ($I$ has order 4; $I-1$ is not a unit); $N(L+1)=2$ if $p=2^k$ and $1$ otherwise ($1+L=1-L^{2s+1}$, of order $p$); $N(L^2+L+1)=4$ if $p=3\cdot2^k$ and $1$ otherwise ($L^2+L+1=(1-L^3)/(1-L)$). The order of $L^{s-2}$ is $n=p/\gcd(p,s-2)$; with $p=2^\alpha m$, $m$ odd: $n=p$ if $\alpha=2$; $n=2^{\alpha-1}m$ if $\alpha\ge4$; and for $p=8q$, $n=q$ if $q\equiv1\!\pmod4$ and $n=2q$ if $q\equiv3\!\pmod4$. So $N(1-L^{s-2})=\ell^4$ if $p=8\ell^a$ with $\ell^a\equiv1\!\pmod4$, $4$ if $p=2^k$, and $1$ otherwise; at $p=8$, $n=1$ and $Q_8=0$. (v) Assembling, $N_+(M_p)^2=2^{-\varphi(p)/2}\,\ell(p)^4\,4^{[p=2^k]}\big/\big(16^{[p=2^k]}\,4^{[p=3\cdot2^k]}\big)$, the square of the stated value ($4\mid\varphi(p)$). $\square$
The mod-4 gate is the order of $L^{s-2}$: for $p=8q$ it is $q$ exactly when $8\mid s-2$. Step-by-step audit of the proof sources (named in §9): `records/dzt/DZT_NORM_LAW_OWNER_REVIEW.md` §3. Exact check for $12\le p\le4000$: DZT-ART-NORMLAW-CHECK (§8). It contains DZT-ALG-CASCADE-NORM and DZT-ALG-CASCADE-ANOMALY-SET as finite cases.

"""

APPB_HYP = r"""---

`[SUPERSEDED]` **DZT19-C01** (administrative correction key; the statement had no RID) Original (`dzt-v0.18` §2 and §6.3, `[HYP]`): "the $\equiv1\!\pmod4$ gate is the reality of $\mathbb{Q}(\sqrt q)\subset\mathbb{Q}(\zeta_q)^+$ — for $q\equiv1$, $\sqrt q$ is real and $\ell$ enters $N_+$; for $q\equiv3$, only $\sqrt{-q}$ (imaginary) lies in $\mathbb{Q}(\zeta_q)$". Reason: the proof of DZT-THM-CASCADE-NORM-LAW locates the gate in the order of $L^{s-2}$ ($q$ when $q\equiv1\!\pmod4$, $2q$ when $q\equiv3$); no quadratic subfield enters. The reading cannot be the reason at $q=9$: $p=72$ is an anomaly ($\lvert N_+\rvert=9/64$) while $\sqrt9$ is rational and $\mathbb{Q}(\zeta_9)^+$ is cubic; the same holds for every $q=\ell^{2b}$. Replacement: §6.3, DZT-THM-CASCADE-NORM-LAW, proof step (iv). Recorded in: v0.19.

"""

APPA_V019 = r"""### v0.19 — 20 November 2026 — DRAFT
The all-$p$ amplitude-norm law enters as DZT-THM-CASCADE-NORM-LAW, `[THM]` `[assuming: DYAD-THM-Q403-PHASELAW]`, after the owner review `records/dzt/DZT_NORM_LAW_OWNER_REVIEW.md` and the PI's decisions of 20 November 2026 on its grade, RID and entry by edition; it closes DZT-OPEN-NORM-LAW (DZT-OPEN-0B-R). The `[HYP]` mechanism of the mod-4 gate is retired (Appendix B). The review check is registered as DZT-ART-NORMLAW-CHECK. No other claim or grade changes; the sign of $N_+(M_p)$ stays outside the theorem. Record: `records/dzt/DZT_v0_19_RELEASE_RECORD.md`.

"""

EDITS = [
    ("H1 title", "# RTG_DYADIC_ARITHMETIC_RESONANCE_TRANSFORM_DSN_v0.18\n",
     "# RTG_DYADIC_ARITHMETIC_RESONANCE_TRANSFORM_DSN_v0.19\n", "edition number"),
    ("H2 date", "**Date:** 18 November 2026\n", "**Date:** 20 November 2026\n", "edition date"),
    ("H3 status",
     "**Document status:** ADOPTED — PI, 19 November 2026 (corrections and synchronization after the reactivation triage, list (i); Methodology v1.4 layout; no new claim, no grade raised). Adoption record: `records/dzt/DZT_v0_18_RELEASE_RECORD.md`.",
     "**Document status:** DRAFT — candidate of v0.19; not adopted. `dzt-v0.18` governs until the PI adopts and tags this edition.",
     "draft status"),
    ("H4 supersedes",
     "**Supersedes:** `RTG_DYADIC_ARITHMETIC_RESONANCE_TRANSFORM_DSN` v0.8 (tag `dzt-v0.8`, SHA-256 `cad20982d294775d52592c304d743695c6ec2d8cf4975c78de203db3d6a92ff2`)",
     "**Supersedes:** `RTG_DYADIC_ARITHMETIC_RESONANCE_TRANSFORM_DSN` v0.18 (tag `dzt-v0.18`, SHA-256 `04581d1e8d8a187ec231d670d9639591e2b8d3aefb9834d5dd9f5cdf792a8dee`)",
     "one predecessor with its hash"),
    ("H5 summary",
     "The active frontier is DZT-OPEN-0B-R: prove or reject the anomaly rule for all $p$ from a resultant identity (§2). No Dyadic result",
     "DZT-OPEN-0B-R is closed by the all-$p$ theorem DZT-THM-CASCADE-NORM-LAW (§6.3), conditional on the imported Dyadic closed form; the open items are DZT-OPEN-B1 and DZT-OPEN-B2 (§2). No Dyadic result",
     "status summary: closure; still four sentences"),
    ("S1a anomalies",
     "`[ALG]` `[scope: finite horizon p≤1000, 249 points]` **Odd-prime anomalies.** On the audited range the values with an odd prime in their numerator are exactly those at $p=8\\ell^a$ ($\\ell$ an odd prime, $\\ell^a\\equiv1\\!\\pmod4$; 20 points), with numerator $\\ell^2$; on the 14-point table the only such point is $p=40$. Statement: §6.3, DZT-ALG-CASCADE-ANOMALY-SET.",
     "`[THM]` `[assuming: DYAD-THM-Q403-PHASELAW]` **Amplitude-norm law.** For every $p=4s\\ge12$, $\\lvert N_+(M_p)\\rvert=\\ell(p)^2/2^{d_p}$ with $d_p=\\varphi(p)/4+[p=2^k]+[p=3\\cdot2^k]$, where $\\ell(p)=\\ell$ if $p=8\\ell^a$ ($\\ell$ an odd prime, $\\ell^a\\equiv1\\!\\pmod4$) and $1$ otherwise. The odd-prime anomalies are exactly these points (20 for $p\\le1000$; on the 14-point table only $p=40$). The sign is not part of the statement. Statement and proof: §6.3, DZT-THM-CASCADE-NORM-LAW.",
     "§1 readout of the theorem (one home: §6.3)"),
    ("S1b frontier",
     "The active frontier is DZT-OPEN-0B-R: prove or reject the anomaly rule for all $p$ from a resultant identity (§2). Then the Track B objects.",
     "DZT-OPEN-0B-R is closed by DZT-THM-CASCADE-NORM-LAW (§6.3). The open items are the Track B objects DZT-OPEN-B1 and DZT-OPEN-B2 (§2).",
     "§1 frontier"),
    ("S2a priority",
     "2. **DZT-OPEN-0B-R** — prove or reject the corrected resultant pattern: $\\lvert N_+(M_{8q})\\rvert$ has odd-prime support iff $q=\\ell^a$ is a prime power with $q\\equiv1\\!\\pmod4$, with numerator $\\ell^2$. Verified `[ALG]` `[scope: finite horizon p≤1000, 249 points]`; candidate mechanism `[HYP]` (below and §6.3).",
     "2. **DZT-OPEN-0B-R** — CLOSED for all $p=4s\\ge12$ by DZT-THM-CASCADE-NORM-LAW (§6.3), conditional on DYAD-THM-Q403-PHASELAW; closed reference at the end of this section.",
     "priority list"),
    ("S2b 0A sub-items",
     "The norm-mechanism question (post-falsification) is tracked under DZT-OPEN-0B.",
     "The norm-mechanism question (post-falsification) was tracked under DZT-OPEN-0B-R and is closed by DZT-THM-CASCADE-NORM-LAW (§6.3).",
     "pointer"),
    ("S2c 0A next",
     "the remaining all-$p$ work (DZT-OPEN-0B-R) is the **DZT-native** resultant-identity proof and no longer depends on any upstream gate.",
     "the all-$p$ norm law (DZT-OPEN-0B-R) is proved as DZT-THM-CASCADE-NORM-LAW (§6.3).",
     "pointer"),
    ("S2d 0B-R block",
     None, None, "the ACTIVE block of DZT-OPEN-0B-R is removed (Methodology §5.2): its finite-horizon statement and the correction of the imported note are in §6.3; its `[HYP]` goes to Appendix B"),
    ("S2e closed reference",
     "Deferred until B1 and 0A are settled.\n",
     "Deferred until B1 and 0A are settled.\n\n---\n\n**DZT-OPEN-0B-R — Corrected odd-prime anomaly law (resultant pattern)** [RID: DZT-OPEN-NORM-LAW] :: CLOSED :: `[THM]` `[assuming: DYAD-THM-Q403-PHASELAW]` :: all $p=4s\\ge12$ :: Results: DZT-THM-CASCADE-NORM-LAW :: §6.3\n",
     "one-line closed reference at the end of §2 (Methodology §5.2)"),
    ("S5 high-risk",
     "| Amplitude norm | rational $\\lvert N_+(M_p)\\rvert$ per point, `[ALG]` `[scope: validation table p=12–64; audit p≤1000]`; on the audited range the odd-prime anomalies are exactly $p=8\\ell^a$, $\\ell^a\\equiv1\\!\\pmod4$ | the 2-power/support-on-2 *law* — **falsified** at $p=40$; any $k_p$ formula; a sign of $N_+(M_p)$ read off the tables | §6.3 |",
     "| Amplitude norm | $\\lvert N_+(M_p)\\rvert=\\ell(p)^2/2^{d_p}$ for all $p=4s\\ge12$, `[THM]` `[assuming: DYAD-THM-Q403-PHASELAW]` (DZT-THM-CASCADE-NORM-LAW); per-point values `[ALG]` `[scope: validation table p=12–64; audit p≤1000]` | the 2-power/support-on-2 *law* — **falsified** at $p=40$; the law without its Dyadic assumption; a sign of $N_+(M_p)$ read off the tables or the law | §6.3 |",
     "high-risk row"),
    ("S6a heading", "### §6.3 Cascade amplitude norm `[ALG]` — mixed content {#sec-6-3-nearmiss-norm}",
     "### §6.3 Cascade amplitude norm `[THM]` — mixed content {#sec-6-3-nearmiss-norm}",
     "primary status of the subsection (Methodology §3.5); anchor kept"),
    ("S6b theorem",
     "`[ALG]` `[RID: DZT-ALG-CASCADE-NORM]`",
     THEOREM + "`[ALG]` `[RID: DZT-ALG-CASCADE-NORM]`",
     "theorem record with proof, before the finite records"),
    ("S6c open para",
     "`[OPEN]` What survives the falsification: the norm is rational; the Dyadic factorization holds; the certified boundaries are reproduced. The odd-prime support question is DZT-OPEN-0B-R (§2); the anomaly set found so far is DZT-ALG-CASCADE-ANOMALY-SET below — not support-on-2.\n\n",
     "",
     "status paragraph superseded by the theorem (the question it names is closed)"),
    ("S6d anomaly set",
     "Machine-verified `dzt_anomaly_rule_check.py` (exit 0, 0 mismatches / 249; run source-reported, §8).",
     "Machine-verified `dzt_anomaly_rule_check.py` (exit 0, 0 mismatches / 249; run source-reported, §8). It is the $p\\le1000$ case of DZT-THM-CASCADE-NORM-LAW.",
     "pointer"),
    ("S6e note correction",
     "The note's $N_+=2^{-\\varphi(q)}$ denominator formula also fails in general (only the anomaly *locations* and the $\\ell^2$ *numerators* are clean); **no denominator law is asserted**.",
     "The note's formula $N_+=2^{-\\varphi(q)}$ is also wrong as a value: on the anomaly set only its denominator exponent is right ($d_{8\\ell^a}=\\varphi(\\ell^a)$, while $\\lvert N_+(M_{8\\ell^a})\\rvert=\\ell^2/2^{\\varphi(\\ell^a)}$, e.g. $25/16\\ne2^{-\\varphi(5)}$ at $p=40$). The general law, denominators included, is DZT-THM-CASCADE-NORM-LAW.",
     "the denominator law is now asserted (theorem); only the exponent of the note's formula is right on the anomaly set (review 5984329391 R1)"),
    ("S6f hyp",
     "`[HYP]` Candidate mechanism for the mod-4 gate: $q\\equiv1\\!\\pmod4\\Rightarrow\\mathbb{Q}(\\sqrt q)\\subset\\mathbb{Q}(\\zeta_q)^+$ real (so $\\ell$ enters the real-subfield norm); $q\\equiv3\\Rightarrow$ only $\\mathbb{Q}(\\sqrt{-q})$, imaginary, excluded. To be settled by the DZT-OPEN-0B-R resultant identity.\n\n",
     "",
     "[HYP] retired; record in Appendix B"),
    ("S7 phaselaw use",
     ":: §6.3 norm object; closed-form audit of DZT-OPEN-0B-R ::",
     ":: §6.3 norm object; the assumption of DZT-THM-CASCADE-NORM-LAW; closed-form audit ::",
     "consumer of the import"),
    ("S7 checked", "checked against that edition for v0.18;", "checked against that edition for v0.18 and v0.19 (no newer Dyadic tag);", "pin check"),
    ("S8a artifact",
     "Every exit code in this section is source-reported; none was rerun for v0.18.",
     "- [RID: DZT-ART-NORMLAW-CHECK] :: `evidence/dzt/norm_law_review/dzt_norm_law_review_check.py` (repository path) :: exact integer resultants for $12\\le p\\le4000$ checking every norm in the proof of DZT-THM-CASCADE-NORM-LAW and the law itself, $p=8$, the recovered CSV and the 14-point table; signed products for $p\\le1000$; the LIT sign pattern for $p\\le100000$ :: `[ENG]` exit 0\n  Files: SHA-256 `566867bb541cd3f5cb4fb1aa11c43ddd4f9b9c0a1e5149697c35a805ac4cebb7`; output `check_output_4000_1000_100000.txt` (`2cc86b9e88f94aa0ca4133bbc961fa3a3f1ae0c1f760c981734ac699d0be188f`); six negative controls PASS (`negative_controls.py`). Run for the owner review on 19 November 2026; a finite check, not the proof.\n\nThe exit codes of the recovered files are source-reported and were not rerun; DZT-ART-NORMLAW-CHECK was run in the repository for the owner review.",
     "registry entry for the review check"),
    ("S9a hyp row",
     "| Claude (v0.7) | `[ALG]` `[scope: finite horizon p≤1000]`; mechanism `[HYP]` |",
     "| Claude (v0.7) | `[ALG]` `[scope: finite horizon p≤1000]`; mechanism `[HYP]` (superseded, Appendix B) |",
     "provenance of the retired [HYP]"),
    ("S9b thm row",
     "| Object-vs-pattern discipline: anomaly law stays finite-horizon despite (R)-closure | Claude (v0.8) | `[DEF]` (scope rule) |",
     "| Object-vs-pattern discipline: anomaly law stays finite-horizon despite (R)-closure | Claude (v0.8) | `[DEF]` (scope rule) |\n| All-$p$ amplitude-norm law $\\lvert N_+(M_p)\\rvert=\\ell(p)^2/2^{d_p}$; the mod-4 gate is the order of $L^{s-2}$ | recovered DZT proof notes (odd support: `DZT_OPEN_0B_R_odd_support_proof_note.md`, SHA-256 `9ce5e99f012319d5cd5d095ed32261857e009d905ed8cf9cf3274f7b6355a30f`; denominator: `DZT_THM_CASCADE_DENOMINATOR_proof.md`, `2a8354ca43d9c33b443a4f8f5d8fdf03548304b39e22badf46aedd598c1b5e39`; both [RECOVERED]); LIT note `DZT_NORM_LAW_PROOF_NOTE.md` at rtg-lit `8e2fb5cb` (complete derivation; Claude, LIT co-owner); owner review (Claude) and independent review (ChatGPT, review `5983698371`); PI grade decision, 20 Nov 2026 (v0.19) | `[THM]` `[assuming: DYAD-THM-Q403-PHASELAW]` |",
     "provenance of the theorem"),
    ("A v0.19 entry", "### v0.18 — 18 November 2026 — adopted 19 November 2026\n",
     APPA_V019 + "### v0.18 — 18 November 2026 — adopted 19 November 2026\n", "Appendix A entry"),
    ("A lineage", "their content enters v0.18 only through the corrections above.",
     "their content enters this lineage only through the corrections of v0.18 and the owner review of v0.19.", "lineage line"),
    ("B hyp record",
     "*END OF DOCUMENT — RTG_DYADIC_ARITHMETIC_RESONANCE_TRANSFORM_DSN_v0.18*",
     APPB_HYP + "*END OF DOCUMENT — RTG_DYADIC_ARITHMETIC_RESONANCE_TRANSFORM_DSN_v0.19 — DRAFT; adoption pending; `dzt-v0.18` governs until adoption and tag.*",
     "Appendix B record of the retired [HYP]; footer"),
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=DSN)
    ap.add_argument("--log", default="evidence/dzt/v0.19/edit_log.txt")
    a = ap.parse_args()
    base = subprocess.run(["git", "show", "%s:%s" % (BASE_TAG, DSN)], capture_output=True, check=True).stdout
    if sha(base) != BASE_SHA:
        die("base is not dzt-v0.18")
    t = base.decode("utf-8")
    for key, old, new, note in EDITS:
        if key == "S2d 0B-R block":
            i = t.index("**DZT-OPEN-0B-R — Corrected odd-prime anomaly law (resultant pattern)** [RID: DZT-OPEN-NORM-LAW]\n")
            j = t.index("**DZT-OPEN-B1 — Formal local NF/dynamical zeta near $P_1$**", i)
            if t.count("**DZT-OPEN-0B-R — Corrected odd-prime anomaly law (resultant pattern)** [RID: DZT-OPEN-NORM-LAW]\n") != 1:
                die("S2d anchor")
            t = edit(t, key, t[i:j], "", note)
            continue
        t = edit(t, key, old, new, note)
    live = t[:t.index("## Appendix A")]
    for bad in ["Status: ACTIVE (corrected pattern", "Candidate mechanism", "no denominator law is asserted",
                "no denominator formula is asserted", "any $k_p$ formula", "prove or reject the anomaly rule",
                "To be settled by the DZT-OPEN-0B-R"]:
        if bad in live:
            die("superseded wording left in the live text: %r" % bad)
    for rid in ["DZT-THM-CASCADE-NORM-LAW", "DZT-OPEN-NORM-LAW", "DZT-ALG-CASCADE-NORM", "DZT-ALG-CASCADE-ANOMALY-SET",
                "DZT-ALG-P12-NORM", "DZT-HYP-MAHLER-NEARMISS", "DZT-ART-NORMLAW-CHECK", "DZT-DEF-CHANNEL-TRANSFORM",
                "DZT-DEF-CHANNEL-STATE", "DZT-DEF-AMBIENT-FIELD", "DZT-OPEN-REPRODUCTION-AUDIT", "DZT-ALG-B5-RESULTANT",
                "DZT-ALG-B234-STRUCTURAL", "DZT-ALG-CASCADE-ROW", "DZT-OPEN-LOCAL-FORMAL-ZETA", "DZT-OPEN-ANALYTIC-ZETA",
                "DZT-RETRACT-MAHLER-RESULT", "DZT-ART-VERIFY-0A", "DZT-ART-CHANNEL-AUDIT", "DZT-ART-CASCADE-AUDIT",
                "DZT-ART-NORMLAW", "DZT-ART-CASEV-AUDIT", "DZT-ART-CF-AUDIT", "DZT-ART-ANOMALY-RULE"] + ["SG-DZT-%d" % k for k in range(1, 9)]:
        if rid not in t:
            die("lost identifier %s" % rid)
    if t.count("[RID: DZT-THM-CASCADE-NORM-LAW]") != 1:
        die("theorem RID must be declared once")
    out = t.encode("utf-8")
    open(a.out, "wb").write(out)
    with open(a.log, "w", encoding="utf-8", newline="\n") as f:
        f.write("DZT v0.19 build log. Base: git show %s:%s, SHA-256 %s\n" % (BASE_TAG, DSN, BASE_SHA))
        f.write("key | line in the text before the edit | sha256[:16] of the replaced span | old chars | new chars | note\n")
        for row in LOG:
            f.write("%s | %d | %s | %d | %d | %s\n" % row)
        f.write("candidate SHA-256 %s, %d bytes, %d edits\n" % (sha(out), len(out), len(LOG)))
    print("candidate %s  %d bytes  (%d edits)" % (sha(out), len(out), len(LOG)))


if __name__ == "__main__":
    main()
