"""TD6 — les deux commandes, exécutées en vérifiant invariant et variant à chaque tour.

Sers-t'en pour tester une idée : modifie un invariant ci-dessous et regarde
sur quel exemple il casse.
Lancer : python3 td6.py
"""

import random
from collections import Counter


def dichotomie(t, v):
    n = len(t)
    assert n > 0 and all(t[k] <= t[k + 1] for k in range(n - 1)), "pré-condition"

    def I(g, d, r):
        I1 = 0 <= g <= d < n and r >= -1
        I2 = all(t[k] != v for k in range(n) if k < g or d < k)
        I3 = r < 0 or (r < n and t[r] == v)
        return I1 and I2 and I3

    r = -1
    g = 0
    d = n - 1
    assert I(g, d, r), "invariant faux avant la boucle"
    while r == -1 and t[g] <= v and v <= t[d]:
        variant_avant = d - g - r
        assert variant_avant >= 0, "variant négatif"
        m = (g + d) // 2
        if t[m] < v:
            g = m + 1
        elif t[m] > v:
            d = m - 1
        else:
            r = m
        assert I(g, d, r), f"invariant non conservé (t={t}, v={v})"
        assert d - g - r < variant_avant, "variant ne décroît pas"
    if v in t:
        assert 0 <= r < n and t[r] == v, "post-condition"
    else:
        assert r == -1, "post-condition"
    return r


def tri_parite(t):
    m = Counter(t)
    n = len(t)

    def I(g, d):
        I1 = Counter(t) == m
        I2 = 0 <= g <= n and -1 <= d < n
        I3 = all(t[i] % 2 == 0 for i in range(g)) and all(t[i] % 2 == 1 for i in range(d + 1, n))
        return I1 and I2 and I3

    g = 0
    d = n - 1
    assert I(g, d), "invariant faux avant la boucle"
    while g <= d:
        variant_avant = d - g
        assert variant_avant >= 0
        if t[g] % 2 == 0:
            g = g + 1
        else:
            v = t[g]
            t[g] = t[d]
            t[d] = v
            d = d - 1
        assert I(g, d), "invariant non conservé"
        assert d - g < variant_avant, "variant ne décroît pas"
    k = g
    assert Counter(t) == m and all(t[i] % 2 == 0 for i in range(k)) \
        and all(t[i] % 2 == 1 for i in range(k, n)), "post-condition"
    return t


if __name__ == "__main__":
    for _ in range(2000):
        t = sorted(random.randint(-5, 5) for _ in range(random.randint(1, 10)))
        dichotomie(t, random.randint(-6, 6))
    print("✅ Dichotomie : invariant, variant et post-condition vérifiés")
    for _ in range(2000):
        tri_parite([random.randint(-9, 9) for _ in range(random.randint(0, 10))])
    print("✅ Tri par parité : invariant, variant et post-condition vérifiés")
    print("   exemple :", tri_parite([3, 8, 5, 2, 7, 4]))
