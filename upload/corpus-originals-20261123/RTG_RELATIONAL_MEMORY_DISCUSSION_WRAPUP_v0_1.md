# RTG Relational Memory / Dynamic Constraint Graph
## Discussion Wrap-Up — v0.1

**Status:** Working research note / conceptual architecture summary  
**Scope:** This note summarizes the discussion on a possible dynamic relational memory/computation architecture inspired by RTG-style relational thinking. It is **not** a claim that the architecture is already part of certified RTG science, and it does not promote exploratory ideas to theorem status.

---

## 1. Starting intuition

The discussion began from a memory question:

> Can knowledge be represented not primarily as stored facts, but as a relational structure in which nodes constrain the admissible states of other nodes?

The central phrase that captured the idea was:

> **collapse of the locally admissible state space**

The important refinement is that "collapse" need not mean a mathematically exact singleton. In a realistic system, uncertainty is natural. A node can be strongly constrained without being known with probability exactly 1.

A useful view is:

\[
P(X_v=x\mid \mathcal E_v),
\]

where \(\mathcal E_v\) is the relational environment bearing on node \(v\).

Knowledge can then be understood as reduction of uncertainty:

\[
K_v \sim H(X_v)-H(X_v\mid \mathcal E_v).
\]

A normalized form is:

\[
\kappa_v
=
1-\frac{H(X_v\mid \mathcal E_v)}{H(X_v)}.
\]

This suggests a **gray knowledge web**:

- exterior / unconnected regions: near-zero knowledge,
- weakly constrained regions: dark gray,
- highly constrained regions: bright,
- nearly determined regions: almost white,
- exact certainty need not be required for empirical knowledge.

A key distinction is:

\[
K(x)=0 \neq P(x)=0.
\]

The first means "we know nothing about it"; the second means "it is impossible."

---

## 2. Knowledge is more than explicit stored facts

The system should distinguish:

### Stored knowledge
A fact was explicitly observed or recorded:

\[
X_v=a.
\]

### Relationally recoverable knowledge
The value was never explicitly stored, but the surrounding structure forces or strongly favors it:

\[
C_1,C_2,\ldots,C_n \models X_v=a.
\]

This leads to the working hypothesis:

> **A sufficiently constrained relational system can contain recoverable information that is not explicitly localized in any one node.**

This makes the memory potentially self-reconstructing. If an explicit fact disappears but the remaining relational structure still entails it, the system can recover it.

That introduces an error-correction-like interpretation of memory:

\[
G\setminus\{m_v\}\Rightarrow m_v.
\]

---

## 3. Dynamic, not static, graph

The proposed system is not intended to be a conventional static knowledge graph.

A new information item should not simply be appended:

\[
G_t + e \neq \text{just store }e.
\]

Instead:

\[
G_t
\xrightarrow{\text{new information }e}
\text{network-wide re-resonance}
\xrightarrow{\text{relaxation}}
G_{t+1}.
\]

The strongest changes occur near the new information, but the effect can propagate through the entire connected web. Even the core can move, although normally much less.

A useful local sensitivity concept is:

\[
\chi_{ij}
=
\frac{\partial z_i}{\partial E_j},
\]

where \(z_i\) is the current epistemic state of node \(i\), and \(E_j\) is incoming evidence at node \(j\).

This gives a possible notion of **knowledge stiffness**:

- highly constrained core regions are stiff,
- weakly constrained fringe regions are soft,
- two nodes with similar confidence can have very different stiffness depending on how much independent relational support they have.

A small new input can sometimes produce a large reconfiguration if the system is close to two competing admissible configurations. This suggests phase-transition-like behavior in the epistemic state.

---

## 4. Memory and computation should not be separate subsystems

A major conceptual borrowing from LISP is **not the programming language itself**, but the unity of representation and operation.

Working principle:

> **Memory is executable structure.**

Instead of:

\[
\text{memory database}
\rightarrow
\text{retrieve}
\rightarrow
\text{reasoning engine}
\rightarrow
\text{write result back},
\]

we want:

\[
G(t)
=
\text{memory}
=
\text{current computational state}.
\]

The graph is not merely read by the reasoning process. The changing graph **is** the reasoning process.

New information acts as perturbation:

\[
G_t + e_t
\xrightarrow{\mathcal R}
G_{t+1}.
\]

A query is then a projection of the current state:

\[
Answer(q)=\Pi_q(G_t).
\]

Facts, rules, confidence, provenance, categories, constraints, and events should ideally inhabit one relational substrate rather than separate databases.

---

## 5. Four core architectural principles

The discussion converged on four highly valuable principles, later extended to five.

### Principle 1 — Nodes are compressible relational regions

> **Nodes are compressible relational regions, not necessarily atoms.**

A node can be a handle for a larger subgraph. A node may be expanded when more detail is required and compressed when that detail is unnecessary.

\[
\text{node}
\leftrightarrow
\text{subgraph}.
\]

This applies to entities, concepts, events, and higher-order structures.

---

### Principle 2 — Knowledge is admissible-state concentration

> **Knowledge is concentration/collapse of the locally admissible state space.**

A node becomes more recognizable as its possible states shrink or concentrate:

\[
H(X_v\mid \mathcal E_v)\downarrow.
\]

Recognition need not require exact certainty.

---

### Principle 3 — Memory and computation share one dynamic substrate

> **Memory and computation inhabit the same dynamic relational structure.**

The graph stores the current epistemic state and simultaneously supports the operations that transform that state.

---

### Principle 4 — Complex relations compile into a minimal relational kernel

> **Complex relations should compile into compositions of a small set of primitive relational forms.**

Ordinary verbs should not require a special reasoning algorithm each.

\[
\text{new word}
\neq
\text{new reasoning algorithm}.
\]

Instead:

\[
\text{new word}
\rightarrow
\text{new composition of existing relational primitives}.
\]

---

### Principle 5 — Representation expands only when required

> **Representation expands only when new information requires additional relational degrees of freedom.**

This is a demand-driven expansion rule.

A simple binary relation can remain compressed until new content needs to attach to the relation itself. Then the relation can be materialized as a node and expanded recursively.

Conceptually:

\[
Encode(I,G)
=
\begin{cases}
Attach(I,G), & \text{if representable},\\
Encode(I,Expand(G)), & \text{otherwise}.
\end{cases}
\]

This prevents the system from trying to model the entire universe before storing a simple statement.

---

## 6. Encode/decode is the main practical difficulty

The real bottleneck is:

\[
\boxed{\text{world / language}\leftrightarrow\text{relational representation}}
\]

Two mappings are required:

\[
E:\text{observation}\rightarrow G,
\]

\[
D:G\rightarrow\text{human-interpretable claim}.
\]

A perfect reasoning engine operating on a bad encoding will reason correctly about the wrong world model.

Therefore representation error and reasoning error should be tested separately.

A sensible development sequence is:

1. perfect manual / oracle encoding,
2. deterministic natural-language encoding,
3. graph-to-language decoding,
4. uncertain / gray information,
5. dynamic revision and re-resonance.

---

## 7. LISP-style notation, not necessarily LISP implementation

LISP is attractive mainly as a notation and conceptual inspiration.

S-expression-like notation is useful because it is:

- recursive,
- human-readable,
- compositional,
- suitable for node expansion,
- suitable for representing facts and rules in structurally similar forms.

Example:

```lisp
(alice
  (relation petting fido))
```

or:

```lisp
(event e1
  (actor alice)
  (object steak)
  (time yesterday))
```

However, the underlying runtime does not need to be LISP. It could be implemented in Python, Rust, a graph store, factor-graph machinery, tensors, or another substrate.

The important borrowing is:

> **representation and computation should not be artificially separated.**

---

## 8. Entity, category, event, and possibility-group behavior

### Entity nodes

Alice and Fido can be the same substrate type of node.

Their meaning comes primarily from neighborhood structure:

\[
Alice\leftrightarrow Human,
\]

\[
Fido\leftrightarrow Cat.
\]

Both may also relate to:

\[
Mammal.
\]

The node itself is thin; much of its meaning lives in its relations.

---

### Categories

A category such as `Human` or `Cat` need not exist permanently as a fixed universal node.

It can become materialized when something in the current web requires the concept.

So:

\[
Alice\rightarrow Human
\]

may cause a `Human` concept node to appear if it does not already exist.

A category can itself expand into a relational web.

Potentially, category membership may ultimately be recognized from relational compatibility rather than being only a hard-coded type field.

---

### Events

Some relations are naturally events when time, location, provenance, or other content needs to attach.

Instead of only:

\[
Alice\xrightarrow{ate}Steak,
\]

we may need:

\[
Alice\rightarrow E_1\rightarrow Steak,
\]

with:

\[
E_1\rightarrow time,
\qquad
E_1\rightarrow location.
\]

Thus a relation can remain compressed as an edge until more information requires it to become a first-class node.

---

### Possibility groups and latent nodes

If the content says:

> There are exactly three people: Alice, Bob, and one other person,

then the relational constraints force creation of a latent node:

\[
?P_3.
\]

The possibility group itself may also become a node:

\[
P=\{Alice,Bob,?P_3\},
\qquad |P|=3.
\]

Later:

\[
?P_3\equiv Jack.
\]

This is an important example of **relations creating nodes before identity is known**.

---

## 9. Ordinary verbs should be compiled, not primitive

Natural-language verbs such as `has`, `eat`, `own`, `love`, `work-for`, etc. should not each require special inference code.

For example, `has` is too ambiguous:

- Alice has a cat,
- Alice has blue eyes,
- Alice has a headache,
- the box has a lid.

The encoder should map each sentence into a more specific relational structure.

Likewise:

> Alice ate steak.

may initially be represented at a semantic level as:

\[
Eat(Alice,Steak),
\]

but `Eat` can itself expand into a relational structure if deeper reasoning requires it.

Therefore:

\[
\text{surface sentence}
\rightarrow
\text{semantic relation graph}
\rightarrow
\text{primitive constraint graph}.
\]

This is analogous to compilation from a high-level language into a small instruction set.

---

## 10. Structural normalization: arbitrary relations can be reified

An arbitrary \(n\)-ary relation can be represented as a relation/event node with binary incidence links.

For:

\[
R(A,B,C),
\]

create:

\[
r_R
\]

and connect:

\[
r_R\rightarrow A,
\quad
r_R\rightarrow B,
\quad
r_R\rightarrow C
\]

with role labels if necessary.

This provides a structural normal form that can handle:

- binary relations,
- events,
- higher-order constraints,
- provenance,
- time,
- confidence,
- cardinality.

It also means that at the deepest substrate level there may be only nodes plus structured incidence, while distinctions such as entity/concept/event/constraint can emerge from topology.

---

## 11. Deterministic puzzle as the first laboratory

A very small logic-grid puzzle is a good first test because:

- the state space can be enumerated,
- the solution is deterministic,
- every inference can be checked,
- encode/decode can be tested separately,
- dynamic propagation can be observed after each clue.

Example domains:

\[
Persons=\{Alice,Bob,Jack\},
\]

\[
Foods=\{Steak,Broccoli,Pasta\}.
\]

Constraint:

> each person ate exactly one different food.

Then:

> Alice ate steak.

> Bob ate broccoli.

causes:

\[
Food(Jack)=Pasta
\]

without that fact ever being explicitly stated.

This is the simplest demonstration of:

\[
\boxed{\text{constraint structure}\rightarrow\text{new explicit knowledge}}
\]

and therefore a clean test of the core hypothesis.

---

## 12. Dynamic puzzle execution

The puzzle should not be solved only once after all clues are loaded.

Instead:

\[
C_1\rightarrow relax,
\]

\[
C_2\rightarrow relax,
\]

\[
C_3\rightarrow relax,
\]

and after each clue we record how the entire graph changes.

For every node \(i\), track something like:

\[
P_t(X_i)
\]

and for every incoming clue/evidence item \(j\), measure:

\[
\Delta P_{ij}^{(t)}.
\]

This gives an empirical picture of knowledge resonance and allows measurement of:

- local vs distant change,
- core stiffness,
- contradiction propagation,
- reconstruction,
- revision,
- dependency depth,
- collapse of admissible state space.

---

## 13. Relation algebra is the main open design problem

The main open item is now:

> **What is the smallest relational algebra/topology needed to represent and transform these structures without hard-coding every verb?**

This includes:

- relation arity,
- directionality,
- symmetry,
- transitivity,
- exclusivity,
- cardinality,
- temporal scope,
- provenance,
- confidence,
- composition behavior,
- contradiction behavior,
- inversion behavior.

The graph may ultimately be better thought of as a typed, weighted, dynamic hypergraph or factor-like network rather than a simple directed graph.

---

## 14. RTG-inspired test and the ratio correction

When testing the representation against very basic RTG-style statements, an important correction was made:

> For this encoding viewpoint, **ratio/comparison** is preferred over "difference" as the primary relational notion.

This should be treated as an architectural/representational choice in this discussion, not as an automatic rewrite of certified RTG scientific claims.

A generic relational ratio is written:

\[
R_{AB}.
\]

Its important structural property is composition:

\[
R_{AB}\circ R_{BC}=R_{AC}.
\]

Depending on representation, the same relation may appear geometrically/multiplicatively:

\[
r_{AB}r_{BC}=r_{AC},
\]

or, where an additive/logarithmic representation is available:

\[
a_{AB}+a_{BC}=a_{AC}.
\]

Thus the graph should preferably preserve the relation itself rather than prematurely committing to an additive or multiplicative numerical representation.

For phase-like quantities, a ratio form is:

\[
R_{AB}=z_Az_B^{-1}.
\]

Under an angular representation:

\[
R_{AB}=e^{i(\theta_A-\theta_B)}.
\]

The architecture-level lesson is:

> **arithmetic and geometric forms can be alternative representations of one deeper compositional relation.**

---

## 15. Candidate primitive relational kernel

After the ratio correction, the most promising current candidate kernel is:

\[
\boxed{
\begin{aligned}
1.&\quad \text{RELATIONAL RATIO / COMPARISON}\quad R_{AB}\\
2.&\quad \text{COMPOSITION}\quad R_{AB}\circ R_{BC}=R_{AC}\\
3.&\quad \text{IDENTITY}\quad R_{AA}=I\\
4.&\quad \text{TYPED INVERSION}\quad R_{BA}=R_{AB}^{-1}
\quad\text{when admissible}
\end{aligned}
}
\]

This is **not yet accepted as the final primitive set**. It is the current candidate produced by the discussion.

An important caution is that inversion should not be universally assumed. It must be relation-type dependent.

---

## 16. A useful recursive representation rule

A compact working rule emerged:

> **If the current exposed nodes cannot carry all the information in the new content, create the additional node(s) or relation-object(s) required, and recurse until the content is representable at the required resolution.**

This can create:

- new entity nodes,
- latent unknown nodes,
- relation/event nodes,
- possibility-group nodes,
- category handles,
- higher-order concept nodes,
- expanded subgraphs.

The process stops when the current representation has enough degrees of freedom to preserve the information relevant to the present task.

---

## 17. What appears similar to neural networks

There is a superficial but useful analogy:

- distributed influence,
- weighted connections,
- many weak influences combining,
- local interactions producing global behavior,
- information distributed across structure.

But the intended difference is that the relational structure remains semantically explicit.

Neural-network weight:

\[
w_{ij}
\]

usually means computational influence.

Here an edge/relation is intended to mean something like:

\[
(relation,\ value,\ confidence,\ provenance,\ status).
\]

The proposed architecture therefore propagates **changes in admissibility**, not merely activation.

The closer established relatives are likely to include:

- constraint-satisfaction systems,
- factor graphs,
- probabilistic graphical models,
- knowledge graphs,
- truth-maintenance systems,
- associative / error-correcting memory,
- graph neural networks and message passing.

The potentially interesting contribution is not "graphs can represent knowledge" but the specific combination:

\[
\boxed{
\text{dynamic relational state}
+
\text{memory/computation unity}
+
\text{admissibility collapse}
+
\text{reconstructive memory}
+
\text{minimal relational compilation}
}
\]

---

## 18. Current research question

The strongest experimental question is:

> **Can an explicit, uncertain, dynamically resonating relational constraint structure raise the effective reasoning capability of an unchanged LLM by maintaining and reconstructing its epistemic state?**

A clean comparison is:

\[
M_{linear}
\quad\text{vs}\quad
M_{relational}
\]

using the same LLM and the same task.

Candidate metrics include:

- valid deduction rate,
- false propagation rate,
- missed propagation rate,
- contradiction detection latency,
- backtracking cost,
- state reconstruction cost,
- provenance accuracy,
- final solution accuracy,
- token/computation cost,
- robustness after deleting or corrupting nodes,
- propagation depth,
- reconstruction threshold under masking.

---

## 19. Current open questions

The main unresolved items are:

1. **Primitive relation set**  
   What relation forms are truly primitive, and which are compilable combinations?

2. **Topology**  
   Simple graph, reified relation graph, hypergraph, factor graph, or a hybrid?

3. **Node ontology**  
   Should entity/concept/event/constraint be substrate types, or merely emergent topological roles?

4. **Category formation**  
   Are categories explicit handles, attractor-like relational patterns, or both?

5. **Confidence semantics**  
   How should confidence, trust, provenance, and structural support interact?

6. **Dynamic law**  
   What exactly determines how a local perturbation propagates and relaxes?

7. **Stability/plasticity balance**  
   How can the core remain revisable without becoming unstable?

8. **Encode/decode**  
   How do natural-language statements compile into canonical relational form, and how is the current relational state decoded back into claims?

9. **Normal form**  
   Can arbitrary semantic relations be reduced to a small compositional kernel analogous to compiling a high-level language into a small instruction set?

10. **Scale/resolution**  
    When should a node remain compressed, and when should it expand into a subgraph?

---

## 20. Current concise formulation

The present architecture can be summarized as follows:

> **Knowledge is not primarily a list of stored facts. It is a dynamic, uncertain relational structure whose constraints continuously reshape the locally admissible state space. Nodes are temporary compressed handles for relational regions; complex relations compile into smaller relational structures; new information perturbs the web and causes local and global reconfiguration; memory and computation therefore inhabit the same substrate.**

The current working design principles are:

\[
\boxed{
\begin{aligned}
1.&\quad \text{Nodes are compressible relational regions, not necessarily atoms.}\\
2.&\quad \text{Knowledge is concentration/collapse of locally admissible state space.}\\
3.&\quad \text{Memory and computation inhabit the same dynamic relational structure.}\\
4.&\quad \text{Complex relations compile into compositions of a minimal relational kernel.}\\
5.&\quad \text{Representation expands only when new information requires more relational freedom.}
\end{aligned}
}
\]

And the present candidate relational kernel is:

\[
\boxed{
RATIO/COMPARISON
+
COMPOSITION
+
IDENTITY
+
TYPED\ INVERSION
}
\]

subject to further testing rather than acceptance by definition.

---

## 21. Recommended immediate next experiment

Use a tiny deterministic puzzle with manually encoded statements and no automatic natural-language parser.

For each information item:

1. identify which existing nodes/relations can carry the content,
2. create new nodes only when required,
3. expand relations into event/relation nodes only when additional information needs to attach,
4. normalize complex relations toward the candidate primitive kernel,
5. recompute admissible states,
6. record how every relevant node changes,
7. verify every inferred fact against the enumerated ground-truth state space.

This provides the first controlled environment in which the proposed "little gray web" can be observed forming, resonating, constraining, reconstructing, and growing.

---

## Epistemic note

This document is a **discussion wrap-up / architectural hypothesis note**. It intentionally distinguishes:

- RTG-inspired conceptual motivation,
- representation-design proposals,
- testable AI-memory hypotheses,
- currently open mathematical and engineering questions.

Nothing in this note should be read as automatically changing the theorem/definition status of claims in existing RTG DSNs.
