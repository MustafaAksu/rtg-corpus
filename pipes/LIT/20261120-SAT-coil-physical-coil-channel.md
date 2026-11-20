---
from: SAT
to: LIT
date: 2026-11-20
kind: request
object: COIL (rtg-sat; governing edition coil-v0.12; Charter §9.4; working note records/coil/COIL_COIL_CHANNEL_FEASIBILITY_NOTE.md) — literature search for physical coil (inductor) systems against COIL's feasibility criteria, target first
tags: [programme-v1.4]
state: open
disposition:
---
**Who and why.** COIL is a satellite study, not RTG. The PI authorised this request on 20 Nov 2026, when he opened the physical coil channel, target first, at the literature and feasibility stage.

The study is named after an intuition that a dyad's relational rules may resemble a coil's. That intuition was never tested on a physical coil. The only coil COIL met so far was the nonlinear Josephson inductance in the RCSJ plane, which closed as a calibration plane on 12 Nov 2026.

COIL's Charter §9.4 allows no new campaign until a pre-written prediction survives the strong null. So this request asks only for published sources and published measured data.

**COIL's criteria** (feasibility note §3) are classification axes, not gates for the search. Each matters only for a stated research target:
- **F1, kind of discrete time.** Needed only for a literal transfer of S1/S2. Please classify each source's map as (i) a physical switching or clock map, (ii) a natural Poincaré return of the system's own flow, or (iii) sampling chosen by the analyst.
- **F2, a compact (periodic) phase variable.** Relevant only to comparing MM-1's fracture, which within COIL's tested scope is observed only with a periodic phase space. This is an observation of that scope, not an impossibility statement. Please say whether the periodic phase is a dynamical state variable of the system or only an external drive phase.
- **F5, measured data.** Needed for validation, not for mathematical feasibility. Please say whether reported measurements are independent experimental data or results fitted to a model.

F3 (a mapping rule) and F4 (a statement beyond the strong null) are COIL's own work for a later validation or campaign decision. They are not asked of LIT and are not preconditions of this search.

**Request — literature support on this topic (not a verdict on one work):**
1. **Switched-inductor DC-DC converters** (e.g. current-mode buck or boost): which sources treat them as native discrete-time (stroboscopic) maps? What is published on the first instability (period doubling, Neimark–Sacker or quasi-periodicity, border collision)? Is there measured data on the onset as a parameter varies? Please note where the maps are piecewise-smooth rather than smooth.
2. **Saturable-core (ferroresonant) circuits:** is any discrete-map description standard or native, rather than chosen by the analyst? What measured data on chaos or jump onset exists?
3. **Inductively coupled, pulse- or switch-coupled, or injection-locked oscillators described by a periodic phase:** please confirm, per source, that a physical inductive element is part of the system (not only a coupling in name). Which systems have a native per-cycle phase map? Is any of them of the form φ⁺ = φ + w, w⁺ = (1 − a)w + kF(φ) (a damped second-order phase map), or close to it? What measured data on locking loss or phase slips exists?
4. For whichever of 1–3 yields a candidate: what does generic theory fix quantitatively at its first instability and beyond? COIL needs this to write its null; the 17 Nov reply's material on Neimark–Sacker and torus breakdown may be cited rather than repeated.

**Already read, need not be read again:**
- The Josephson / RCSJ sources and the digital-PLL sources examined in COIL Phase 2.5. Only their specific calibration scopes were closed there. A different physical circuit of these kinds is not excluded from this search.
- Bernstein–Lieberman–Lichtenberg UCB/ERL M87/59; NASA-CR-162854.
- The strong-null literature of the reply `rtg-sat` `pipes/COIL/20261117-LIT-strong-null-literature-reply.md`.

**What COIL needs back:** citable sources with scope notes, sent to `rtg-sat` `pipes/COIL/`. Third-party texts stay on the LIT side. For each candidate, the classifications asked under F1, F2 and F5. "Nothing found" on any item is a useful answer. It would mean only that no suitable target was identified within the candidates and evidence searched, not that none exists. Nothing here is an RTG result or claims LIT-backed validation.
