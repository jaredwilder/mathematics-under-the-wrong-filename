# Mathematics under the wrong filename

Author: Jared Wilder. First public timestamp: 2026-09-11.

## The measurement

An earlier sweep of 907 archives filtered them by filename, kept the 234 whose names announced
mathematics, and opened those. This is the other 673.

| | count |
|---|---|
| archives in the folder | 907 |
| names matching a mathematics keyword | 234 |
| **name-dropped, opened here** | **673** |
| zero-byte or corrupt | 7 |
| over 200 MB, member names only | 2 |
| opened and read | 664 |
| **held at least one mathematical claim** | **192 (28.9%)** |
| held none | 472 |

**The filename filter was wrong about 192 archives.** 143 of those 192 have project, product, or
opaque names rather than session ids. 13 carry Lean theorem declarations.

192 is a floor. The detector required three claim-lines, and `graph-bridge-real-delivery.zip` scored
two while holding a 119-row exact strongly-regular-graph existence table.

The 472 with nothing in them are fonts, clipart, WordPress plugins, bookkeeping, bank statements,
web mockups.

---

## An eight-round research program, none of whose filenames contain a mathematical word

Eight archives named `HIGH-GEAR`, `RELATIONAL`, `FIBER-COHERENCE`, `COHERENCE-CSP`, `UNICYCLE-CORE`,
`PERMUTATION-GLUING`, `THETA-COLLISION`, `RANK-THREE-KERNEL`. Together they are a sustained attack on
Erdős 595.

### Round 8, theta collision

Every 2-connected incidence block of cycle rank two is a theta graph, and it is coherent if and only
if `R1 ∩ R2 ∩ R3` is nonempty. The four-way obstruction classification is complete, with no fifth
mechanism.

The first intrinsic graph-realized core, on domain 4:

```
pi1 = (0, 1, 2, 3)    pi2 = (0, 2, 3, 1)    pi3 = (1, 2, 0, 3)

agree(pi1, pi2) = {0}     agree(pi2, pi3) = {1}     agree(pi1, pi3) = {3}

common agreement = empty
```

Recomputed here: pairwise agreements nonempty, triple intersection empty. Exhaustive normalized
search gives 0 examples on domain 2, 0 on domain 3, and 24 on domain 4. Its explicit realization has
12 constraints, 0 coherent sections, 4 sections after any single deletion, and 48 assignments
violating exactly one constraint.

For every `r >= 3`, disjoint transpositions on a domain of size `2r` give an inclusion-minimal
incoherent K4-free multi-theta of cycle rank `r-1`. **There is no finite Helly bound.**

And `sigma(C_j | C - {C_j}) = 1` for every constraint of every inclusion-minimal incoherent finite
CSP, so scalar extension slack cannot classify cores.

### Round 9, rank-three kernels

Cycle rank three has **exactly four** branch kernels: `Q4`, `T221`, `D22`, `K4`. There is no fifth.

The `K4` assignment ledger is `N0=0, N1=36, N2=18, N3=24, N6=3`, and the deletion profile
`6 / 12 / 18` (one deleted, two adjacent, two disjoint) reconstructs `L(K4)`. The atlas census of 33
rank-three blocks is `6 Q4 + 12 T221 + 4 D22 + 11 K4`.

Finite K4-free fiber coherence is **NP-complete at domain size three**; fixed cycle rank `r` is
decidable in `O(d^r poly(N))`.

### Rounds 2, 3, 4, 6

- **Rank one** is completely classified: support pruning empties a domain, or the cycle monodromy has
  no fixed point. No third mechanism. The twisted-cycle construction for every `n >= 7` has section
  count exactly 2 for even total xor and 0 for odd.
- **The coherence sandwich** `cs_P(G) <= tc(G) <= chi(R_P(G))`, and the exact reformulation:
  *Erdős 595 asks for an uncountably chromatic 3-uniform hypergraph admitting an endpoint scheme and
  containing no Berge cycle of length three.*
- `tc(G) <= bc(Q_P) + sup_P tc(G[P])`, so every cell induced-`kappa`-null with `tc(G) > kappa` forces
  `chi(Q_P) > 2^kappa`. With a correction on the record: **every graph is the quotient of a matching
  under a stable partition**, so quotient chromatic number alone implies nothing.
- `J_kappa(G) = {A : tc(G[A]) <= kappa}` is closed under unions of up to `2^kappa` members.

---

## Paley(17), recomputed here

```
connection set  {1, 2, 4, 8, 9, 13, 15, 16}   (the quadratic residues mod 17)
68 edges        68 triangles        0 K4s among all 2380 quadruples
triangle cover number exactly 2
```

The cover number needed a real search rather than sampling: 2-colouring 68 edges so neither class
contains a full triangle is hypergraph 2-colouring over a space of size `2^68`. A WalkSAT-style
local search finds one immediately. An explicit partition into a 36-edge and a 32-edge triangle-free
class:

```
part A   (0,2) (0,9) (0,13) (0,16) (1,3) (1,10) (1,14) (2,3) (2,10) (2,15) (3,4) (3,5)
         (3,11) (4,6) (4,8) (4,12) (4,13) (5,6) (5,9) (5,14) (6,7) (6,10) (6,15) (7,8)
         (7,9) (7,11) (7,16) (9,10) (10,11) (10,12) (11,13) (12,14) (12,16) (13,14)
         (14,15) (15,16)

part B   (0,1) (0,4) (0,8) (0,15) (1,2) (1,5) (1,9) (1,16) (2,4) (2,6) (2,11) (3,7)
         (3,12) (3,16) (4,5) (5,7) (5,13) (6,8) (6,14) (7,15) (8,9) (8,10) (8,12) (8,16)
         (9,11) (9,13) (10,14) (11,12) (11,15) (12,13) (13,15) (14,16)
```

The source also records an exhaustive sweep of every circulant on 13 to 17 vertices, and concludes
the vertex-partition route to Erdős 595 is dead.

**A power-blindness result from the same source:** every graph on at most `2^kappa` vertices is a
union of `kappa` triangle-free subgraphs, with no hypothesis on the graph. A smallest witness has
cover number pinned at `aleph_1 <= tc <= 2^aleph_0` on `(2^aleph_0)^+` vertices.

---

## Erdős–Hájnal for induced-P6-free graphs

A 30-theorem bank with 16 retracted routes and a deterministic verifier. The flagship
`exists c > 0, for all induced-P6-free G: max(omega(G), alpha(G)) >= |V(G)|^c` is open. Closed:

- any two distinct nonempty stable-slice row defect sets are **disjoint**
- every stable interaction is complete bipartite minus disjoint complete bipartite holes `S_r x D_r`
- the number of distinct row traces is at most `|T| + 1`, and this is sharp
- a guaranteed pure pair with sides at least `|S|/(|T|+1)` and `|T|/2`
- crown normal form: a blow-up of `K_{q,q}` minus a `q`-matching
- a one-subdivision of `K_{1,t}` contains no induced P6, since its diameter is at most 4
- **refuted:** "every weighted cograph has clique or stable weight at least `sqrt(W · w_max)`"

The exhaustive 0/1-matrix survivor census:

| shape | survivors | of |
|---|---|---|
| 2x2 | 12 | 16 |
| 2x3 | 34 | 64 |
| 2x4 | 96 | 256 |
| 3x3 | 128 | 512 |
| 3x4 | 466 | 4096 |
| 4x4 | 2100 | 65536 |

All four one-edge orientations induce P6.

---

## Other mathematics found under non-mathematical names

**A strongly-regular-graph transport atlas.** 119 parameter tuples from Brouwer, 91 existing and 28
not. The nonexistent set includes `(21,10,4,5)`, `(28,9,0,4)`, `(33,16,7,8)`, `(49,16,3,6)`,
`(50,21,4,12)`, `(56,22,3,12)`, `(57,28,13,14)`, `(64,30,18,10)`, `(69,34,16,17)`, `(75,32,10,16)`,
`(76,21,2,7)`, `(76,30,8,14)`, `(77,38,18,19)`, `(93,46,22,23)`, `(95,40,12,20)`, `(96,38,10,18)`,
`(96,45,24,18)` and complements. Alongside it, **141 verified composable transport edges** across 8
transports with 0 disagreements and 211 endpoints. The atlas refuses to emit a
`Matrix.IsHadamard <-> hadamard:n` edge on the grounds that it would collapse distinct propositions.

**A 3,536-element transition monoid**, in an archive named after a Hawaiian reef fish. The 3-resource
open/close automaton has 6 events, 9 semantic states and a trap state; its transition monoid has
exactly 3,536 elements with word-length histogram `1, 6, 36, 145, 432, 876, 1088, 776, 176` and
diameter 8. The coding law: a canonical algebra of size `N` needs `ceil(log_q N) + 2t + e` q-ary
symbols to survive `t` substitutions and `e` erasures.

**Its own Lean audit refutes its own labels.** In the companion port, `BS-04` claims a bit-savings
bound and proves `exists bits, bits >= s` by choosing `bits = s`. `HUMU-02` proves only
`quotientSize <= rawSize` — not bit savings, not a log bound, not minimality.

**A 74-row triangle-free chromatic theorem bank** (Erdős 738), 62 proved:
`chi(G[union of N(s)]) <= |S|`; the isolate-sharp form `chi(G[N[S]]) <= |S|`, plus one if `G[S]` has
isolates; `chi(G - N[S]) >= chi(G) - |S|`; the sequential ledger
`chi(G_m) >= chi(G) - sum |S_i|`; connected dominating `|S| >= 2` gives `chi(G) <= |S|`; and in a
`k`-vertex-critical triangle-free graph with `G[S]` connected and `2 <= |S| < k`, some component of
`G - N[S]` has `chi >= k - |S|`.

**Five-mark Golomb rulers**, recomputed here: optimum length **11**, with exactly four optimal
witnesses `(0,1,4,9,11)`, `(0,2,7,8,11)`, `(0,2,7,10,11)`, `(0,3,4,9,11)`.

**Binary Sidon sets.** `f(7) >= 24` with the 24-element witness rechecked: 300 pairs, 300 distinct
sums. Sequence A309370 is known for `d = 0..6` as `1, 2, 3, 5, 7, 12, 15`; `d = 7` is the first
unpublished term, and UNSAT at 25 would pin `f(7) = 24`.

**Steiner triple system walls meet the classical condition.** CP-SAT finds `v` in `{3,7,9,13,15}`
satisfiable and `{4,5,6,8,10,11,12,14}` unsatisfiable, rediscovering `v = 1, 3 (mod 6)`.

**A 51-row information-representation ledger:** `H(Z|X) >= H(B_E|X)`; a state hiding `K_x` distinct
future behaviours needs at least `ceil(log2 K_x)` auxiliary bits; two states decoding robustly within
radius `r` to distinct meanings need Hamming distance at least `2r+1`.

---

## Corrections carried in the same archives

- **An `f(n)` table with 61 wrong values.** One seeded table reports `f(103) = 161`; the value is
  **158**.
- **A Ramsey decomposition candidate for `R(4,6) = 36`** produced multiple counterexamples and was
  refuted. A projective-plane transport candidate produced contradictions.
- **A fake-novelty bug**, caught in its own source: an incomplete table flagged the known
  `C(12,3,2) = 24` as novel. A Kramer–Mesner UNSAT result was correctly downgraded from
  non-existence to `refuted_under_prescribed_symmetry`.
- **Erdős 891 quarantined**: the kernel proof is correct but controls `Omega(n)` while the problem
  asks about `omega(n)`.

## What was not covered

- **Nested archives.** 76 of the 673 are containers of containers, holding 50, 41, 15, 10 and 6 inner
  zips among others. Only top-level members were read, so mathematics one archive deeper is not in
  the 192.
- **Presence in the estate.** Distinctive-token searches for these programs returned nothing in
  `oracle/ledger`, `oracle/brain` and `brain/`, but the full-tree search timed out. Whether these
  archives duplicate material elsewhere in the estate is open.

## License

Apache-2.0.
