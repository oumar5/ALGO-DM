"""TD1 — implémentations Python à compléter.

Remplace chaque `raise NotImplementedError` par ton code, puis lance :
    python3 td1.py
"""


def mult_rec(n: int, m: int) -> int:
    """Q1.2 — version récursive de mult. Pré : n >= 0."""
    raise NotImplementedError


def mult_iter(n: int, m: int) -> int:
    """Q1.2 — version itérative de mult. Pré : n >= 0."""
    raise NotImplementedError


def exp_rec(a: int, b: int) -> int:
    """Q2.2 — version récursive de exp. Pré : b >= 0."""
    raise NotImplementedError


def exp_iter(a: int, b: int) -> int:
    """Q2.2 — version itérative de exp. Pré : b >= 0."""
    raise NotImplementedError


def expR(a: int, b: int) -> int:
    """Q2.5 — exponentiation rapide récursive. Pré : b >= 0."""
    raise NotImplementedError


# ---------------------------------------------------------------------------
# Tests : ne pas modifier
# ---------------------------------------------------------------------------
def _tester(nom, f, cas):
    try:
        for args, attendu in cas:
            obtenu = f(*args)
            assert obtenu == attendu, f"{nom}{args} = {obtenu}, attendu {attendu}"
        print(f"✅ {nom}")
    except NotImplementedError:
        print(f"⏳ {nom} : à faire")


if __name__ == "__main__":
    cas_mult = [((n, m), n * m) for n in range(6) for m in range(-3, 4)]
    cas_exp = [((a, b), a ** b) for a in range(-3, 4) for b in range(7)]
    _tester("mult_rec", mult_rec, cas_mult)
    _tester("mult_iter", mult_iter, cas_mult)
    _tester("exp_rec", exp_rec, cas_exp)
    _tester("exp_iter", exp_iter, cas_exp)
    _tester("expR", expR, cas_exp)
