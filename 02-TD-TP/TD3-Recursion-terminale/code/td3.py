"""TD3 — versions NON récursives (boucles while) à compléter.

Méthode : arguments -> variables, arrêt -> while not (...),
appel récursif -> affectation simultanée.
Lancer : python3 td3.py
"""


def expAux(a: int, b: int, acc: int) -> int:
    """Q1.1 — Pré : b >= 0. Post : acc * a**b."""
    raise NotImplementedError


def expR(a: int, b: int) -> int:
    return expAux(a, b, 1)


def revAux(l: list[int], acc: list[int]) -> list[int]:
    """Q2.2 — Post : reverse(l) + acc."""
    raise NotImplementedError


def insererAux(k: int, l: list[int], acc: list[int]) -> list[int]:
    """Q2.2 — insertion de k dans une liste triée (acc : déjà parcouru, à l'envers)."""
    raise NotImplementedError


# ---------------------------------------------------------------------------
# Tests : ne pas modifier
# ---------------------------------------------------------------------------
def _tester(nom, test):
    try:
        test()
        print(f"✅ {nom}")
    except NotImplementedError:
        print(f"⏳ {nom} : à faire")


def _test_exp():
    for a in range(-3, 4):
        for b in range(10):
            for acc in (1, 2, -1):
                assert expAux(a, b, acc) == acc * a ** b, (a, b, acc)
    assert expR(2, 10) == 1024


def _test_rev():
    assert revAux([1, 2, 3], [9]) == [3, 2, 1, 9]
    assert revAux([], [4]) == [4]


def _test_inserer():
    import random
    for _ in range(200):
        l = sorted(random.randint(-5, 5) for _ in range(random.randint(0, 8)))
        k = random.randint(-6, 6)
        assert insererAux(k, l, []) == sorted(l + [k]), (k, l)


if __name__ == "__main__":
    _tester("expAux", _test_exp)
    _tester("revAux", _test_rev)
    _tester("insererAux", _test_inserer)
