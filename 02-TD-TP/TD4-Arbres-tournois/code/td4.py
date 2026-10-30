"""TD4 Q1.3 — le type Tournoi en Python objet, à compléter.

Rappel de la méthode du cours :
  type Tournoi -> classe abstraite Tournoi
  constructeurs J, M -> sous-classes
  arguments -> attributs ; fonctions -> méthodes
Lancer : python3 td4.py
"""

from __future__ import annotations


class Tournoi:
    def vainqueur(self) -> int:
        raise NotImplementedError

    def hauteur(self) -> int:
        raise NotImplementedError

    def isJ(self) -> bool:
        raise NotImplementedError

    def delMin(self) -> tuple[int, Tournoi]:
        """Pré : le tournoi est bien formé et n'est pas un J."""
        raise NotImplementedError

    def joueurs(self) -> list[int]:
        """Valeurs des joueurs (le multi-ensemble ⟦t⟧), pour les tests."""
        raise NotImplementedError


class J(Tournoi):
    def __init__(self, valeur: int):
        self.valeur = valeur

    # À compléter : vainqueur, hauteur, isJ, joueurs
    # (delMin n'est pas défini pour un joueur seul)


class M(Tournoi):
    def __init__(self, t1: Tournoi, t2: Tournoi):
        """Construit le match de t1 et t2 (c'est la fonction match du TD).

        À compléter : ranger le vainqueur dans self.valeur, mettre à gauche
        (self.gauche) le sous-tournoi qui contient le vainqueur et l'autre
        à droite (self.droite).
        """
        raise NotImplementedError

    # À compléter : vainqueur, hauteur, isJ, delMin, joueurs


def tri_tournoi(l: list[int]) -> list[int]:
    """triTournoi, déjà écrit : il utilise tes classes."""
    if l == []:
        return []
    tournois: list[Tournoi] = [J(a) for a in l]
    while len(tournois) > 1:                     # joueTournois
        suivant = []
        for i in range(0, len(tournois) - 1, 2):  # joueTour
            suivant.append(M(tournois[i], tournois[i + 1]))
        if len(tournois) % 2 == 1:
            suivant.append(tournois[-1])
        tournois = suivant
    t = tournois[0]
    resultat = []
    while not t.isJ():                           # tournoiListe
        k, t = t.delMin()
        resultat.append(k)
    resultat.append(t.vainqueur())
    return resultat


# ---------------------------------------------------------------------------
# Tests : ne pas modifier
# ---------------------------------------------------------------------------
def _bien_forme(t: Tournoi) -> bool:
    if t.isJ():
        return True
    return (t.valeur == min(t.joueurs()) and t.valeur == t.gauche.vainqueur()
            and _bien_forme(t.gauche) and _bien_forme(t.droite))


def _tests():
    t = M(M(J(5), J(1)), M(J(4), J(3)))
    assert t.vainqueur() == 1 and t.hauteur() == 3 and _bien_forme(t)
    k, t2 = t.delMin()
    assert k == 1 and sorted(t2.joueurs()) == [3, 4, 5] and _bien_forme(t2)
    assert t2.hauteur() <= t.hauteur()
    import random
    for _ in range(200):
        l = [random.randint(-5, 5) for _ in range(random.randint(0, 12))]
        assert tri_tournoi(l) == sorted(l), l


if __name__ == "__main__":
    try:
        _tests()
        print("✅ Tournoi et tri par tas-tournoi")
    except NotImplementedError:
        print("⏳ Tournoi : à faire")
    except AttributeError as e:
        print(f"⏳ Tournoi : méthode ou attribut manquant ({e})")
