"""TD2 — implémentations Python à compléter.

Utilise les tranches de listes (l[0], l[1:], l[2:]) pour « enlever des éléments en tête ».
Lancer : python3 td2.py
"""


def separe_rec(l1: list[int], l2: list[int]) -> tuple[list[int], list[int]]:
    """Q1.1.2 — version récursive de separe."""
    raise NotImplementedError


def separe_iter(l1: list[int], l2: list[int]) -> tuple[list[int], list[int]]:
    """Q1.1.2 — version itérative de separe."""
    raise NotImplementedError


def fusionne_rec(l1: list[int], l2: list[int]) -> list[int]:
    """Q1.2.2 — version récursive de fusionne. Pré : l1 et l2 triées."""
    raise NotImplementedError


def fusionne_iter(l1: list[int], l2: list[int]) -> list[int]:
    """Q1.2.2 — version itérative de fusionne. Pré : l1 et l2 triées."""
    raise NotImplementedError


def tri_fusion(l: list[int], separe=separe_rec, fusionne=fusionne_rec) -> list[int]:
    """triFusion, déjà écrit : il utilise tes fonctions separe et fusionne."""
    if len(l) <= 1:
        return list(l)
    l1, l2 = separe(l, l)
    return fusionne(tri_fusion(l1, separe, fusionne), tri_fusion(l2, separe, fusionne))


# ---------------------------------------------------------------------------
# Tests : ne pas modifier
# ---------------------------------------------------------------------------
def _tester(nom, test):
    try:
        test()
        print(f"✅ {nom}")
    except NotImplementedError:
        print(f"⏳ {nom} : à faire")


def _test_separe(f):
    def test():
        assert f([1, 3, 2, 7, 1], [5, 3, 4, 1]) == ([1, 3], [2, 7, 1])
        for n in range(8):
            for m in range(8):
                l1, l2 = list(range(n)), list(range(m))
                a, b = f(l1, l2)
                assert a + b == l1 and len(a) == min(n, m // 2), (l1, l2, a, b)
    return test


def _test_fusionne(f):
    def test():
        assert f([1, 3], [1, 2, 7]) == [1, 1, 2, 3, 7]
        assert f([], [4]) == [4] and f([4], []) == [4]
        assert f([0, 5, 9], [1, 2, 10, 11]) == [0, 1, 2, 5, 9, 10, 11]
    return test


def _test_tri():
    import random
    for _ in range(200):
        l = [random.randint(-5, 5) for _ in range(random.randint(0, 12))]
        assert tri_fusion(l) == sorted(l), l


if __name__ == "__main__":
    _tester("separe_rec", _test_separe(separe_rec))
    _tester("separe_iter", _test_separe(separe_iter))
    _tester("fusionne_rec", _test_fusionne(fusionne_rec))
    _tester("fusionne_iter", _test_fusionne(fusionne_iter))
    _tester("tri_fusion", _test_tri)
