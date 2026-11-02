# Chapitre 3 — Exercices

[🏠 Accueil](../../README.md) · [⬅ Cours](1-Cours.md) · [Exemples corrigés](2-Exemples-corriges.md) · **Corrections : [4-Corrections.md](4-Corrections.md)**

> ⭐ = échauffement · ⭐⭐ = entraînement · ⭐⭐⭐ = niveau DS

---

## Exercice 1 ⭐ — Terminale ou pas ?

Pour chaque ligne récursive, réponds « terminale » ou « non terminale », et justifie en une phrase.

```haskell
a)  longueur (_:l)          = 1 + longueur l
b)  appartient k (x:l) | x == k    = True
                       | otherwise = appartient k l
c)  revAux (x:l) acc        = revAux l (x:acc)
d)  somme (x:l)             = x + somme l
e)  dernier (_:l)           = dernier l
f)  double (x:l)            = 2*x : double l
g)  pgcd a b | a > b        = pgcd (a-b) b
h)  puissance2 n            = 2 * puissance2 (n-1)
```

---

## Exercice 2 ⭐ — Calculer pas à pas

```haskell
factAux :: Int -> Int -> Int
factAux 0 acc = acc
factAux n acc = factAux (n-1) (acc*n)
```

1. `factAux 4 1`
2. `revAux [1,2,3] []` (définition dans le cours)
3. `divAux 17 5 0` (définition dans le cours)

Dans chaque cas, la ligne de calcul s'allonge-t-elle ?

---

## Exercice 3 ⭐ — Traduire en boucle `while`

Traduis en Python, avec la recette du cours :
1. `factAux` (exercice 2) ;
2. `dernier` : `dernier [x] = x` et `dernier (_:l) = dernier l` ;
3. `appartient` (exercice 1, b), avec le cas `appartient k [] = False`.

---

## Exercice 4 ⭐⭐ — Rendre terminale

Pour chaque fonction, écris une version **terminale** avec accumulateur (une fonction `…Aux` + la fonction principale qui l'appelle avec la bonne valeur de départ).

| Fonction | Définition non terminale |
|---|---|
| `longueur` | `longueur [] = 0` ; `longueur (_:l) = 1 + longueur l` |
| `produit` | `produit [] = 1` ; `produit (x:l) = x * produit l` |
| `compte k` | `compte k [] = 0` ; `compte k (x:l) \| x == k = 1 + compte k l \| otherwise = compte k l` |
| `puissance2` | `puissance2 0 = 1` ; `puissance2 n = 2 * puissance2 (n-1)` |

> 💡 Quelle est la **valeur de départ** de la calculatrice ? Celle du cas de base (`0` pour une somme, `1` pour un produit).

---

## Exercice 5 ⭐⭐ — Le piège des deux lignes

```haskell
suiteAux :: Int -> Int -> Int -> Int
suiteAux 0 a b = a
suiteAux n a b = suiteAux (n-1) b (a+b)
```

Voici deux traductions :

```python
def version1(n, a, b):              def version2(n, a, b):
    while n != 0:                       while n != 0:
        n, a, b = n - 1, b, a + b           n = n - 1
    return a                                a = b
                                            b = a + b
                                        return a
```

1. Calcule `suiteAux 5 0 1` à la main.
2. Exécute `version1(5, 0, 1)` et `version2(5, 0, 1)` à la main (tableau `n`, `a`, `b`).
3. Laquelle est juste ? Pourquoi l'autre se trompe-t-elle ?

---

## Exercice 6 ⭐⭐ — Trouver la propriété « déjà fait + reste à faire »

Pour chaque fonction à accumulateur, écris la propriété **valable pour tout `acc`**, puis ce qu'on en déduit.

| Fonction | Appel principal |
|---|---|
| `factAux n acc` (exercice 2) | `factAux n 1` |
| `produitAux l acc` (exercice 4) | `produitAux l 1` |
| `compteAux k l acc` (exercice 4) | `compteAux k l 0` |
| `p2Aux n acc` (exercice 4) | `p2Aux n 1` |

---

## Exercice 7 ⭐⭐ — Prouver `factAux`

Démontre : pour `n ≥ 0` et pour tout `acc`, `factAux n acc = acc × n!`.
En déduire que `factAux n 1 = n!`.

---

## Exercice 8 ⭐⭐⭐ — Prouver `longAux`

```haskell
longAux :: [a] -> Int -> Int
longAux []    acc = acc
longAux (_:l) acc = longAux l (acc + 1)
```

1. Démontre : pour toute liste `l` et tout `acc`, `longAux l acc = acc + length l`.
2. En déduire que `longAux l 0 = length l`.
3. Pourquoi une preuve qui ne parle que de `acc = 0` ne marcherait-elle pas ?

---

## Exercice 9 ⭐⭐⭐ — De Python à Haskell : la somme des chiffres

> 🔢 La somme des chiffres sert à vérifier un numéro (par exemple la preuve par 9).

```python
def somme_chiffres(n):
    s = 0
    while n > 0:
        s = s + n % 10      # on ajoute le dernier chiffre
        n = n // 10         # on l'enlève
    return s
```

1. Exécute `somme_chiffres(472)` (tableau `n`, `s`).
2. Écris la fonction Haskell **terminale** `chiffresAux n s` qui correspond à cette boucle.
3. Avec `sc 0 = 0` et ``sc n = n `mod` 10 + sc (n `div` 10)`` (pour `n > 0`), démontre que pour `n ≥ 0` et pour tout `s`, `chiffresAux n s = s + sc n`.

---

## Exercice 10 ⭐⭐⭐ — La longueur de la pile retournée 📚

Démontre que, pour toutes listes `l` et `acc` :

```text
length (revAux l acc) = length l + length acc
```

En déduire que `revRT l` a la même longueur que `l`.
