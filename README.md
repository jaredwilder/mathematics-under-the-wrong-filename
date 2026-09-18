# Mathematics recovered from non-mathematical archives

A systematic sweep of archives whose filenames did not advertise mathematical content found a substantial amount of real mathematics hidden under project, product, and opaque names.

## Audit

| | count |
|---|---:|
| archives examined | 907 |
| filenames initially matching a mathematics keyword | 234 |
| remaining archives opened in this sweep | **673** |
| opened and readable | 664 |
| non-excluded archives containing mathematics | **105** |
| project/product/opaque-named mathematical archives | **93** |
| session-transcript mathematical archives | 12 |

The practical conclusion is simple: filename-based discovery missed 93 archives containing mathematics.

## Major recovered subjects

### Erdős #595 and fiber coherence

Eight archives with names such as `FIBER-COHERENCE`, `COHERENCE-CSP`, `THETA-COLLISION`, and `RANK-THREE-KERNEL` form one sustained program connected to Erdős #595.

The mathematics has dedicated public homes and should be read there rather than in this recovery ledger:

- [`erdos595-barrier-tower`](https://github.com/jaredwilder/erdos595-barrier-tower) — Erdős #595 itself: triangle-cover number, the continuum threshold, formal cardinal reductions, and structural consequences for a hypothetical `K_4`-free witness;
- [`triangle-cover-number`](https://github.com/jaredwilder/triangle-cover-number) — triangle-cover formulations and related finite/structural theory;
- [`fiber-coherence-cycle-rank`](https://github.com/jaredwilder/fiber-coherence-cycle-rank) — the recovered fiber/coherence program, including rank-one and rank-two structure, cycle-rank-three kernels, exact finite realizations, and complexity results.

Recovered fiber/coherence results include:

- complete rank-one coherence classification;
- rank-two theta obstruction structure;
- a domain-4 minimal three-relation collision with pairwise nonempty but empty triple agreement;
- four cycle-rank-three branch kernels: `Q4`, `T221`, `D22`, and `K4`;
- exact finite K4-free fiber-coherence realizations for binary CSPs;
- NP-completeness at domain size three for the unbounded-rank finite problem.

This repository preserves the discovery provenance only. The mathematical citation surfaces are the dedicated repositories above.

### Paley(17) triangle-cover computation

For the Paley graph on 17 vertices:

```text
68 edges
68 triangles
0 K4s
tc(G)=2
```

An explicit partition of the 68 edges into two triangle-free classes is recorded in the source material.

### Induced-`P6` Erdős–Hajnal structure

The archive contains the structural chain later promoted to [`p6-erdos-hajnal`](https://github.com/jaredwilder/p6-erdos-hajnal): stable-slice defect disjointness, complete-bipartite-minus-rectangles normal form, trace bounds, pure-pair bounds, and crown structure.

### Strongly regular graph transport

A recovered graph package contains:

- 119 strongly regular graph parameter rows;
- 141 typed transport edges;
- 211 endpoints;
- zero recorded disagreements in the finite transport checks.

The focused release is [`strongly-regular-graph-transport-atlas`](https://github.com/jaredwilder/strongly-regular-graph-transport-atlas).

### Transition monoid

A three-resource open/close automaton generates exactly **3,536** transition summaries, with shortest-word depth histogram

```text
1, 6, 36, 145, 432, 876, 1088, 776, 176
```

and radius 8. The result is now presented in [`three-resource-transition-monoid`](https://github.com/jaredwilder/three-resource-transition-monoid).

### Other recovered finite mathematics

The sweep also surfaced or cross-checked:

- a 24-element binary Sidon set in dimension 7;
- four optimal five-mark Golomb rulers of length 11;
- finite covering and Ramsey construction-class calculations;
- a 74-row triangle-free chromatic theorem bank;
- information-representation inequalities and finite coding results.

## Corrections found during the sweep

The audit also identified bad or overstated source claims, including:

- a seeded numerical table with dozens of wrong values;
- a refuted Ramsey decomposition candidate;
- an incomplete table incorrectly flagged as novel;
- a formal statement about `Ω(n)` attached to a problem asking about `ω(n)`.

Those corrections are routed with the relevant subject material rather than promoted as independent mathematical results.

## Publication rule

No substantive result should live **only** in a recovery ledger, campaign archive, transcript dump, or opaque source directory.

When a recovered subject has enough coherent mathematics to stand on its own, it should receive a dedicated public repository with a human-readable statement, scope, evidence, and verification path. Recovery repositories are provenance layers: they explain where the mathematics came from, not where a reader should be expected to discover or cite it.

## Purpose of this repository

This is a discovery ledger, not the preferred citation surface for the mathematics it found. Mature subjects are routed to focused repositories; this page records why those subjects were discovered and where they came from.

Author: Jared Wilder. License: Apache-2.0.
