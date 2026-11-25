#!/usr/bin/env python3
"""Atlas v0.11 D3 pilot, stage 2a: deletion-only compaction of D3.L2 against the frozen stage-1 output.

Every edit removes one declared byte span from one line; no text is reworded, moved or added.
Classes: K1 = owner-edition label (Method v0.2 §4.1: chronology of edits is not atlas content);
         K2 = proof/method detail beyond a one-line pointer (Method v0.2 §4.7).
Usage: build_stage2a.py STAGE1.md OUT.md MAP.json SPANS.md
"""
import hashlib, json, sys, importlib.util, pathlib
BASE_SHA = '0f8ba5c0e34dcbbaaa11858e2d568a9f5d5ced63aeca8ee69a44c973d7a1a6c2'
D3 = (608, 857)   # stage-1 line range of domain D3; no edit may fall outside it
# (record-line prefix, class, exact span to delete)
SPANS = [
 ('RECOG-ALG-QUADRATURE-TYPING ALG | ', 'K1', '; v0.3.24'),
 ('RECOG-ALG-POLE-STRATUM-PERIODIC-INVENTORY ALG | ', 'K1', '; v0.3.24'),
 ('RECOG-THM-R9-MEMORY THM | ', 'K2', ', g+τg′ cancels q²-increment [c_iso+Im((1−2iτ)a₀₅e^{−6iΘ})]q², |ΔΦ|≤K_Φq³ (K_Φ≤258.49 / 81.44, Arb), Σq_m³≤2q₀², C₂=2K_Φ'),
 ('RECOG-THM-R9-MEMORY THM | ', 'K1', 'v0.3.25 '),
 ('RECOG-THM-R9-MEMORY THM | ', 'K1', '; v0.3.27, in place of the earlier [assuming:]'),
 ('RECOG-THM-A1A-LIFT-ALIGNMENT THM | ', 'K2', ' | proof: W(Tx)=λW+λ(η−sinη)+ω(e^ρ−1−ρ), ω²=−1−ω; |ρ|,|η|≤(2/√3)|W|<2R, R=47/1000, 2R<ln2; |η−sinη|<(8/6)|W|³, |e^ρ−1−ρ|<4|W|²; relative error <4R+(4/3)R²=143209/750000<1/2; six-step increments lie in (π,3π), so no branch ambiguity'),
 ('RECOG-THM-A1A-RECIPROCAL-AMPLITUDE THM | ', 'K2', ' | method: Q_{m+1}=Q_m(1−Q_m+ε_m), |ε_m|≤(16931/10000)Q_m^{3/2}+108Q_m², √Q_m≤1/20 ⇒ |θ_m|≤(7.17/0.99)√Q_m; Q_m≤min(Q₀,2/m) (sufficient, not sharp)'),
 ('RECOG-THM-A1B-SLIP-SCHEDULE-U THM | ', 'K1', '; v0.3.24'),
 ('RECOG-THM-A1B-SLIP-SCHEDULE-U THM | ', 'K1', 'v0.3.25: '),
 ('RECOG-THM-A1B-SLIP-SCHEDULE-U THM | ', 'K1', '[COR v0.3.26] '),
 ('RECOG-ALG-A1C-JET-REMAINDER-BOUNDS ALG (v0.3.27) | ', 'K1', ' (the majorants were first computed for COMBINED-TAIL, v0.3.25, and are stated source-independently here)'),
 ('RECOG-ALG-A1C-LOGFREE-ENVELOPE ALG (v0.3.26; source condition v0.3.27) | ', 'K1', '; the (D5) [assuming:] of v0.3.26 is discharged (v0.3.27), grade unchanged'),
 ('RECOG-RESULT-A1C-RECORD-PHASE-READOUT RES[from THM] | ', 'K1', '; v0.3.24'),
 ('RECOG-RESULT-A1C-RECORD-PHASE-READOUT RES[from THM] | ', 'K1', '; reworded v0.3.25'),
 ('RECOG-RESULT-A1C-RECORD-PHASE-READOUT RES[from THM] | ', 'K1', ', v0.3.25)'),
 ('RECOG-THM-P2-HET THM | ', 'K2', ' (δ=10⁻⁵, κ=2, R={|w|≤κs²}: (A) T(R∩N)⊂R, (B) |w(Ty)|≤0.60560|w| off R, (C) s-ratio∈[λ₋,λ₊], λ₋=2.618032, (D) κδ²≤δ)'),
 ('RECOG-THM-P2-HET THM | ', 'K2', ' 4096 pieces (120 bits), entry into U after 3655–3673 steps, Q_entry∈[0.0015897542,0.0015999994], max width 6.71×10⁻⁴, no splits'),
 ('RECOG-THM-P2-C0-FIRST THM | ', 'K2', ' {|dw|≤|ds|/100} (det DT≥0.99998 on N)'),
 ('RECOG-THM-P2-C0-FIRST THM | ', 'K2', ' 4096 pieces, det>0 at steps 1–13, K=14 one-piece zero block, ∇det·v₁₄<0; s*∈[4.20646,4.20725]×10⁻⁶'),
 ('RECOG-THM-TWIN-STAGE2-NONUNIVERSAL THM | ', 'K2', ': segment I={x_c+tw}, N=320, L=60, Arb 1024: C1 I⊂𝒜, C2 inf D_s>0 for n<320 (min 0.021826591… at step 235), C3 terminal curve minus (0,120π) in c+P₀R, C4 one piece [−1,1], C5 endpoints on opposite sides of h_± (margins 9.84×10⁻⁸)'),
 ('RECOG-THM-TWIN-C0-ACCESS THM | ', 'K2', ', Q(I(t)) exact quadratic, Q_min=0.0356584369…, Q_max=0.0356584375… (margins 6.58×10⁻⁴ from q₁,q₂); Arb 1024: D_s(T_s^{200}x₋)=0.090299286863097301413±1.04×10⁻²³, D_s(T_s^{200}x₊)=−0.18560195360161191558±2.44×10⁻²¹'),
]
# ', v0.3.25)' removes the label but must keep the closing bracket
KEEP_TAIL = {', v0.3.25)': ')'}
REASON = {'K1': 'owner-edition label; chronology of edits is not atlas content (Method v0.2 §4.1)',
          'K2': 'proof/method detail beyond a one-line pointer (Method v0.2 §4.7); cert and @owner§ pointers kept'}

def main():
    src, out, mapf, spansf = sys.argv[1:5]
    raw = open(src, 'rb').read(); assert hashlib.sha256(raw).hexdigest() == BASE_SHA, 'base is not the accepted stage-1 output'
    lines = raw.decode('utf-8').split('\n'); log = []
    for prefix, cls, span in SPANS:
        hits = [i for i, l in enumerate(lines) if l.startswith(prefix)]
        assert len(hits) == 1, (prefix, hits); i = hits[0]
        assert D3[0] <= i + 1 <= D3[1], ('outside D3', prefix)
        assert lines[i].count(span) == 1, ('span not unique', prefix, span, lines[i].count(span))
        lines[i] = lines[i].replace(span, KEEP_TAIL.get(span, ''))
        log.append((i + 1, prefix.split(' ')[0], cls, span, KEEP_TAIL.get(span, '')))
    cand = '\n'.join(lines).encode('utf-8'); open(out, 'wb').write(cand)
    # movement map: generated from the two extracts; every changed field is declared, nothing else
    tool = pathlib.Path(__file__).resolve().parents[4] / 'tools' / 'atlas_preservation.py'
    sp = importlib.util.spec_from_file_location('ap', tool); ap = importlib.util.module_from_spec(sp); sp.loader.exec_module(ap)
    B, C = ap.extract(raw), ap.extract(cand)
    bn = {ap.okey(r): r for r in B['regions'] if r['kind'] == 'node'}; cn = {ap.okey(r): r for r in C['regions'] if r['kind'] == 'node'}
    cls_of = {}
    for ln, rid, cls, span, _ in log: cls_of.setdefault(ln, set()).add(cls)
    recs = []
    for k, r in bn.items():
        t = cn[k]
        if t['sha256'] == r['sha256']: continue
        why = '; '.join(REASON[c] for c in sorted(cls_of[r['line']]))
        bh = [f['sha256'] for f in r['fields']]; ch = [f['sha256'] for f in t['fields']]
        lost = [h for h in bh if h not in ch]; new = [h for h in ch if h not in bh]
        fields = []
        if len(bh) == len(ch):
            assert len(lost) == len(new); fields = [dict(base_sha256=a, cand_sha256=b, reason='span deletion inside the field: ' + why) for a, b in zip(lost, new)]
        else:   # one whole field deleted, the others byte-identical
            assert not new and len(lost) == len(bh) - len(ch); fields = [dict(base_sha256=a, cand_sha256=None, reason='whole field deleted: ' + why) for a in lost]
        recs.append(dict(base=k, cand=k, reason='stage 2a deletion-only compaction', fields=fields))
    # lines the extractor keeps as raw (non-standard record head): declared as line edits at the same line number
    for rb, rc in zip(B['regions'], C['regions']):
        assert rb['kind'] == rc['kind'] and rb['line'] == rc['line']
        if rb['kind'] == 'raw' and rb['sha256'] != rc['sha256']:
            recs.append(dict(base=f"L{rb['line']}", cand=f"L{rc['line']}", reason='stage 2a span deletion inside a raw line: ' + '; '.join(REASON[c] for c in sorted(cls_of[rb['line']]))))
    json.dump(dict(base_sha256=BASE_SHA, candidate_sha256=hashlib.sha256(cand).hexdigest(), stage='v0.11 D3 pilot, stage 2a (deletion only)', records=recs, inserts=[]),
              open(mapf, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    o = ['# Stage 2a — every deleted span, verbatim', '', f'Base: stage-1 output `{BASE_SHA}`. Candidate: `{hashlib.sha256(cand).hexdigest()}`. {len(raw):,} → {len(cand):,} bytes.', '',
         'Each row is one deletion; the rest of the line is byte-identical. K1 = owner-edition label (Method v0.2 §4.1). K2 = proof/method detail beyond a one-line pointer (Method v0.2 §4.7).', '']
    for n, (ln, rid, cls, span, tail) in enumerate(log, 1):
        o += [f'## {n}. L{ln} `{rid}` — {cls}, {len(span.encode()) - len(tail.encode())} bytes', '', '```text', span, '```', ''] + ([f'Kept from the span: `{tail}`', ''] if tail else [])
    open(spansf, 'w', encoding='utf-8').write('\n'.join(o))
    print(hashlib.sha256(cand).hexdigest(), len(raw), len(cand), len(log), 'spans', len(recs), 'records')
if __name__ == '__main__': main()
