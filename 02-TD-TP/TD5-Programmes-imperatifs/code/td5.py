"""TD5 — outils pour vérifier ses réponses en exécutant le code.

1. Exercice 1 : écris ta plus faible pré-condition dans WP_Q11 / WP_Q12,
   le script la compare au vrai comportement du programme sur beaucoup de valeurs
   (entiers de -6 à 6 ; attention, le % de Python prend le signe du diviseur
   et un modulo par 0 fait planter le programme).
2. Exercices 2 et 3 : les programmes s'exécutent en vérifiant l'invariant
   et la décroissance du variant à chaque tour.

Lancer : python3 td5.py
"""

from fractions import Fraction
from itertools import product

# ---------------------------------------------------------------------------
# Exercice 1 — remplace None par ta WP, par exemple : lambda a, b, c: a > 0
# ---------------------------------------------------------------------------
WP_Q11 = None   # lambda a, b: ...
WP_Q12 = None   # lambda a, b, c: ...


def prog_q11(a, b):
    a = a + 1
    if a + b == 0:
        a = b
    else:
        b = a
    return a == 0 and b != 0


def prog_q12(a, b, c):
    a = b * c
    if a != 0:
        b = Fraction(c * b) / a
        c = c + 1
    else:
        a = Fraction(a + 1) / c
        b = b * b
    c = a * b
    return a % (b + c) == 0


def verifie_wp(nom, wp, prog, nb_vars):
    if wp is None:
        print(f"⏳ {nom} : écris ta WP dans le fichier")
        return
    for vals in product(range(-6, 7), repeat=nb_vars):
        try:
            reel = prog(*vals)
        except ZeroDivisionError:
            reel = False          # le programme plante : la post-condition n'est pas atteinte
        try:
            propose = bool(wp(*vals))
        except ZeroDivisionError:
            propose = False
        if propose != reel:
            print(f"❌ {nom} : contre-exemple {vals} (ta WP dit {propose}, le programme donne {reel})")
            return
    print(f"✅ {nom} : ta WP est correcte sur les valeurs testées")


# ---------------------------------------------------------------------------
# Exercice 2 — division avec vérification de l'invariant et du variant
# ---------------------------------------------------------------------------
def division(a, b):
    assert a >= 0 and b > 0, "pré-condition"
    q = 0
    r = a
    invariant = lambda: a == q * b + r and r >= 0 and b > 0
    assert invariant(), "invariant faux avant la boucle"
    while r >= b:
        variant_avant = r
        q = q + 1
        r = r - b
        assert invariant(), "invariant non conservé"
        assert 0 <= r < variant_avant, "variant ne décroît pas"
    res = (q, r)
    assert a == res[0] * b + res[1] and 0 <= res[1] < b, "post-condition"
    return res


# ---------------------------------------------------------------------------
# Exercice 3 — nombre de diviseurs avec vérification de l'invariant
# ---------------------------------------------------------------------------
def div(n, i):
    return len([k for k in range(1, n + 1) if n % k == 0 and (1 <= k < i or n // i < k <= n)])


def nb_diviseurs(n):
    assert n > 1, "pré-condition"
    i = 2
    res = 2
    assert res == div(n, i), "invariant faux avant la boucle"
    while i * i < n:
        variant_avant = n - i
        if n % i == 0:
            res = res + 2
        i = i + 1
        assert res == div(n, i), f"invariant non conservé (n={n}, i={i})"
        assert 0 <= n - i < variant_avant, "variant"
    if i * i == n:
        res = res + 1
    assert res == len([k for k in range(1, n + 1) if n % k == 0]), "post-condition"
    return res


if __name__ == "__main__":
    verifie_wp("Q1.1", WP_Q11, prog_q11, 2)
    verifie_wp("Q1.2", WP_Q12, prog_q12, 3)
    for a in range(30):
        for b in range(1, 8):
            division(a, b)
    print("✅ Ex. 2 : invariant, variant et post-condition vérifiés à l'exécution")
    for n in range(2, 300):
        nb_diviseurs(n)
    print("✅ Ex. 3 : invariant, variant et post-condition vérifiés à l'exécution")
    print("   nb_diviseurs(42) =", nb_diviseurs(42))
