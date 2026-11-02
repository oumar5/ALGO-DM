# F2 — Modèle de preuve par induction

[🏠 Accueil](../README.md)

> 🧍🧍🧍 **L'idée :** comme dans une file d'attente, je m'appuie sur les cas **plus petits** (hypothèse d'induction) pour traiter le mien. Le **variant** est le compte à rebours qui garantit qu'on arrive au bout.

## 📝 Le modèle à recopier

```text
SPÉCIFICATION
  Pré  : …
  Post : …

VARIANT : v(x) = …
  C'est un entier ≥ 0 car … (souvent : par la pré-condition, ou c'est une longueur)

HYPOTHÈSE D'INDUCTION (HI)
  Pour tous y tels que v(y) < v(x) et Pré(y), on a Post(y, f y).

DÉMONSTRATION
  On suppose Pré(x). On distingue les cas (un par équation / garde) :

  Cas 1 (nom C1 : …) :
    f x = …            (par définition, C1)
    donc Post(x, f x) car …

  Cas 2 (nom C2 : …) :
    f x = … f y …      (par définition, C2)
    On applique l'HI à f y :
      1. le variant diminue : v(y) < v(x) car …
      2. la pré-condition est vraie : Pré(y) car …
    Donc Post(y, f y), c'est-à-dire …
    On en déduit Post(x, f x) : …

  Ce qui achève la preuve par induction.
```

## ✅ Checklist

- [ ] Variant **annoncé** et justifié **≥ 0**.
- [ ] HI écrite **en entier** (avec « pour tous » et la pré-condition).
- [ ] **Un cas par équation / garde** ; dans un cas de garde `gi`, je peux utiliser `non g1 … non g(i−1)`.
- [ ] Cas et hypothèses **nommés** (C1, C2, Pre1…) et **cités** à chaque étape.
- [ ] Pour **chaque** appel récursif : ① variant ↓ ② pré ✓.
- [ ] Phrase finale : « Ce qui achève la preuve par induction. »

## 🎯 Choisir le variant

| La fonction parcourt… | Variant |
|---|---|
| un entier qui décroît (`n-1`, `n quot 2`, `a-b`) | cet entier |
| une liste | `length l` |
| deux listes qui raccourcissent tour à tour | `length l1 + length l2` |
| un arbre | `taille t` ou `hauteur t` |
| un ensemble représenté par un arbre | nombre d'éléments de `⟦t⟧` |
| `i` monte vers `n` | `n − i` |

## « Expliquez pourquoi X peut servir de variant » (question de DS)

Répondre **deux** choses :
1. **X est un entier ≥ 0** quand la pré-condition est vraie (ex. : une longueur est toujours ≥ 0 ; `n ≥ 0` par la pré).
2. **X diminue strictement à chaque appel récursif** (ex. : `length (x:l) = 1 + length l > length l`) — et la pré-condition est conservée.

## 🔁 Fonction à accumulateur

1. Généraliser : prouver la propriété pour **tout** `acc` (ex. `revAux l acc = reverse l ++ acc`).
2. En déduire la fonction principale en **remplaçant** `acc` par sa valeur initiale.
