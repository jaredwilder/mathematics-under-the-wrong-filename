#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Recomputes the claims this repository states in its own voice.

    python verify.py

Standard library only. Exit 0 means everything reproduced.
"""
from __future__ import annotations

import random
import sys
from itertools import combinations

FAILURES = []


def check(label, got, want):
    ok = got == want
    print("  %-54s %s" % (label, "PASS" if ok else "FAIL got=%r want=%r" % (got, want)))
    if not ok:
        FAILURES.append(label)


def paley(q=17):
    qr = sorted({(i * i) % q for i in range(1, q)})
    V = list(range(q))
    E = sorted((u, v) for u in V for v in V if u < v and (v - u) % q in qr)
    return V, E, qr


def neighbours(V, E):
    a = {u: set() for u in V}
    for u, v in E:
        a[u].add(v)
        a[v].add(u)
    return a


def triangles(V, adj):
    return [t for t in combinations(V, 3)
            if all(y in adj[x] for x, y in combinations(t, 2))]


def test_paley17():
    print("Paley(17)")
    V, E, qr = paley(17)
    check("quadratic residues mod 17", qr, [1, 2, 4, 8, 9, 13, 15, 16])
    adj = neighbours(V, E)
    check("edges", len(E), 68)
    check("triangles", len(triangles(V, adj)), 68)
    k4 = sum(1 for q in combinations(V, 4)
             if all(y in adj[x] for x, y in combinations(q, 2)))
    check("K4 count among all 2380 quadruples", k4, 0)

    print("  triangle cover number: 2-colour 68 edges, no mono triangle")
    idx = {e: i for i, e in enumerate(E)}
    tris = [(idx[(a, b)], idx[(a, c)], idx[(b, c)])
            for a, b, c in triangles(V, adj)]

    def unsat(col):
        return [t for t in tris if col[t[0]] == col[t[1]] == col[t[2]]]

    random.seed(12345)
    sol = None
    for _ in range(400):
        col = [random.randint(0, 1) for _ in E]
        for _ in range(20000):
            bad = unsat(col)
            if not bad:
                sol = col[:]
                break
            t = random.choice(bad)
            if random.random() < 0.35:
                v = random.choice(t)
            else:
                v, bn = None, None
                for w in t:
                    col[w] ^= 1
                    n = len(unsat(col))
                    col[w] ^= 1
                    if bn is None or n < bn:
                        v, bn = w, n
            col[v] ^= 1
        if sol:
            break
    check("a proper 2-colouring exists", sol is not None, True)
    if sol:
        for part in (0, 1):
            es = [E[i] for i in range(len(E)) if sol[i] == part]
            a = neighbours(V, es)
            check("  part %d is triangle-free" % part, triangles(V, a), [])


def test_theta_core():
    print("The theta-collision core on domain 4")
    p1, p2, p3 = (0, 1, 2, 3), (0, 2, 3, 1), (1, 2, 0, 3)

    def ag(a, b):
        return {i for i in range(4) if a[i] == b[i]}

    check("agree(pi1, pi2)", ag(p1, p2), {0})
    check("agree(pi2, pi3)", ag(p2, p3), {1})
    check("agree(pi1, pi3)", ag(p1, p3), {3})
    check("common agreement is empty", ag(p1, p2) & ag(p2, p3) & ag(p1, p3), set())


def test_golomb():
    print("Five-mark Golomb rulers")
    for L in range(4, 16):
        found = []
        for m in combinations(range(L + 1), 5):
            if m[0] or m[-1] != L:
                continue
            d = [m[j] - m[i] for i in range(5) for j in range(i + 1, 5)]
            if len(d) == len(set(d)):
                found.append(m)
        if found:
            check("optimum length", L, 11)
            check("number of optimal witnesses", len(found), 4)
            check("the witnesses", found,
                  [(0, 1, 4, 9, 11), (0, 2, 7, 8, 11),
                   (0, 2, 7, 10, 11), (0, 3, 4, 9, 11)])
            return
    FAILURES.append("no Golomb ruler found")


def main():
    for fn in (test_paley17, test_theta_core, test_golomb):
        fn()
        print()
    if FAILURES:
        print("FAILED: %d check(s)" % len(FAILURES))
        for f in FAILURES:
            print("   " + f)
        return 1
    print("ALL CHECKS PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
