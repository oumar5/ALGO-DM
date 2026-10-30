"""Logique propositionnelle en Python objet (code du cours C4, version corrigée).

Traduction du type Haskell Prop :
  - classe abstraite Prop            <- le type
  - une sous-classe par constructeur <- Var, Vrai, Faux, Et, Ou, Non
  - attributs                        <- arguments du constructeur
  - méthodes                         <- fonctions taille, eval, pousse_neg

Lancer les tests : python3 logique.py
"""

from __future__ import annotations


class Valuation:
    """Liste associative : nom de variable -> booléen."""

    def __init__(self, l: list[tuple[str, bool]]):
        self.val = l

    def trouve(self, x: str) -> bool:
        """Pré-condition : x est dans le domaine de la valuation."""
        for (y, b) in self.val:
            if x == y:
                return b
        raise KeyError(x)


class Prop:
    def taille(self) -> int:
        raise NotImplementedError

    def vars(self) -> set[str]:
        raise NotImplementedError

    def eval(self, v: Valuation) -> bool:
        raise NotImplementedError

    def pousse_neg(self, neg: bool) -> Prop:
        raise NotImplementedError


class Var(Prop):
    def __init__(self, x: str):
        self.nom = x

    def taille(self) -> int:
        return 1

    def vars(self) -> set[str]:
        return {self.nom}

    def eval(self, v: Valuation) -> bool:
        return v.trouve(self.nom)

    def pousse_neg(self, neg: bool) -> Prop:
        return Non(self) if neg else self

    def __repr__(self) -> str:
        return self.nom


class Vrai(Prop):
    def taille(self) -> int:
        return 1

    def vars(self) -> set[str]:
        return set()

    def eval(self, v: Valuation) -> bool:
        return True

    def pousse_neg(self, neg: bool) -> Prop:
        return Faux() if neg else self

    def __repr__(self) -> str:
        return "Vrai"


class Faux(Prop):
    def taille(self) -> int:
        return 1

    def vars(self) -> set[str]:
        return set()

    def eval(self, v: Valuation) -> bool:
        return False

    def pousse_neg(self, neg: bool) -> Prop:
        return Vrai() if neg else self

    def __repr__(self) -> str:
        return "Faux"


class Et(Prop):
    def __init__(self, p1: Prop, p2: Prop):
        self.arg1 = p1
        self.arg2 = p2

    def taille(self) -> int:
        return 1 + self.arg1.taille() + self.arg2.taille()

    def vars(self) -> set[str]:
        return self.arg1.vars() | self.arg2.vars()

    def eval(self, v: Valuation) -> bool:
        return self.arg1.eval(v) and self.arg2.eval(v)

    def pousse_neg(self, neg: bool) -> Prop:
        if neg:
            return Ou(self.arg1.pousse_neg(neg), self.arg2.pousse_neg(neg))
        return Et(self.arg1.pousse_neg(neg), self.arg2.pousse_neg(neg))

    def __repr__(self) -> str:
        return f"({self.arg1} ∧ {self.arg2})"


class Ou(Prop):
    def __init__(self, p1: Prop, p2: Prop):
        self.arg1 = p1
        self.arg2 = p2

    def taille(self) -> int:
        return 1 + self.arg1.taille() + self.arg2.taille()

    def vars(self) -> set[str]:
        return self.arg1.vars() | self.arg2.vars()

    def eval(self, v: Valuation) -> bool:
        return self.arg1.eval(v) or self.arg2.eval(v)

    def pousse_neg(self, neg: bool) -> Prop:
        if neg:
            return Et(self.arg1.pousse_neg(neg), self.arg2.pousse_neg(neg))
        return Ou(self.arg1.pousse_neg(neg), self.arg2.pousse_neg(neg))

    def __repr__(self) -> str:
        return f"({self.arg1} ∨ {self.arg2})"


class Non(Prop):
    def __init__(self, p: Prop):
        self.arg = p

    def taille(self) -> int:
        return 1 + self.arg.taille()

    def vars(self) -> set[str]:
        return self.arg.vars()

    def eval(self, v: Valuation) -> bool:
        return not self.arg.eval(v)

    def pousse_neg(self, neg: bool) -> Prop:
        return self.arg.pousse_neg(not neg)

    def __repr__(self) -> str:
        return f"¬{self.arg}"


if __name__ == "__main__":
    from itertools import product

    p = Non(Et(Var("a"), Ou(Non(Var("b")), Faux())))
    print("p              =", p)
    print("pousse_neg(p)  =", p.pousse_neg(False))
    print("taille(p)      =", p.taille())

    # Vérifie la spécification de pousse_neg sur toutes les valuations.
    for va, vb in product([True, False], repeat=2):
        val = Valuation([("a", va), ("b", vb)])
        for b in (True, False):
            q = p.pousse_neg(b)
            assert q.vars() == p.vars()
            attendu = (not p.eval(val)) if b else p.eval(val)
            assert q.eval(val) == attendu
    print("Spécification de pousse_neg vérifiée ✅")
