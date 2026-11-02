# Chapitre 3 — Corrections

[🏠 Accueil](../../README.md) · [⬅ Exercices](3-Exercices.md) · [Cours](1-Cours.md)

> ⚠️ As-tu cherché au moins 10 minutes ?

---

## Exercice 1 ⭐ — Terminale ou pas

| | Réponse | Pourquoi |
|---|---|---|
| a) `longueur` | ❌ non terminale | il reste `1 + …` à faire après l'appel |
| b) `appartient` | ✅ terminale | la réponse de l'appel est directement le résultat |
| c) `revAux` | ✅ terminale | rien après l'appel |
| d) `somme` | ❌ non terminale | il reste `x + …` |
| e) `dernier` | ✅ terminale | rien après l'appel |
| f) `double` | ❌ non terminale | il reste à accrocher `2*x :` devant le résultat |
| g) `pgcd` | ✅ terminale | rien après l'appel |
| h) `puissance2` | ❌ non terminale | il reste `2 * …` |

> 💡 Le piège : f). Il n'y a pas de calcul « visible » comme `+` ou `*`, mais accrocher un wagon `2*x :` est bien un travail fait **après** l'appel.

---

## Exercice 2 ⭐ — Pas à pas

1. `factAux 4 1 = factAux 3 4 = factAux 2 12 = factAux 1 24 = factAux 0 24 = 24`
2. `revAux [1,2,3] [] = revAux [2,3] [1] = revAux [3] [2,1] = revAux [] [3,2,1] = [3,2,1]`
3. `divAux 17 5 0 = divAux 12 5 1 = divAux 7 5 2 = divAux 2 5 3 = (3, 2)`

Dans les trois cas, la ligne **garde la même taille** : rien n'est en attente. ✅

---

## Exercice 3 ⭐ — En `while`

```python
def factAux(n, acc):
    while n != 0:                       # arrêt : n == 0
        n, acc = n - 1, acc * n         # appel : factAux (n-1) (acc*n)
    return acc

def dernier(l):                         # pré : l non vide
    while len(l) != 1:                  # arrêt : la liste a un seul élément [x]
        l = l[1:]                       # appel : dernier l (sans le premier)
    return l[0]

def appartient(k, l):
    while l != [] and l[0] != k:        # on continue tant qu'aucun arrêt n'est atteint
        l = l[1:]
    return l != []                      # arrêt sur [] : False ; arrêt sur x == k : True
```

> 💬 `appartient` a **deux** cas d'arrêt : la boucle continue tant qu'**aucun** des deux n'est vrai. Après la boucle, on regarde lequel nous a arrêtés.

---

## Exercice 4 ⭐⭐ — Versions terminales

```haskell
longAux []    acc = acc
longAux (_:l) acc = longAux l (acc + 1)
longueur l = longAux l 0

produitAux []    acc = acc
produitAux (x:l) acc = produitAux l (acc * x)
produit l = produitAux l 1

compteAux k []    acc = acc
compteAux k (x:l) acc | x == k    = compteAux k l (acc + 1)
                      | otherwise = compteAux k l acc
compte k l = compteAux k l 0

p2Aux 0 acc = acc
p2Aux n acc = p2Aux (n-1) (2 * acc)
puissance2 n = p2Aux n 1
```

> 💬 Le travail qui était « en attente » (`1 + …`, `x * …`, `2 * …`) est fait **tout de suite** sur l'accumulateur.

---

## Exercice 5 ⭐⭐ — Le piège des deux lignes

1. `suiteAux 5 0 1 = suiteAux 4 1 1 = suiteAux 3 1 2 = suiteAux 2 2 3 = suiteAux 1 3 5 = suiteAux 0 5 8 = 5`

2. | Tour | `version1` : `n, a, b` | `version2` : `n, a, b` |
   |---|---|---|
   | départ | 5, 0, 1 | 5, 0, 1 |
   | 1 | 4, 1, 1 | 4, 1, **2** |
   | 2 | 3, 1, 2 | 3, 2, 4 |
   | 3 | 2, 2, 3 | 2, 4, 8 |
   | 4 | 1, 3, 5 | 1, 8, 16 |
   | 5 | 0, 5, 8 | 0, 16, 32 |
   | résultat | **5** ✅ | **16** ❌ |

3. `version1` est juste. Dans `version2`, la ligne `b = a + b` utilise le **nouveau** `a` (qui vaut déjà l'ancien `b`), alors que Haskell utilise l'**ancien** `a`. L'affectation simultanée calcule toutes les nouvelles valeurs **avec les anciennes**, puis les range.

---

## Exercice 6 ⭐⭐ — Les propriétés

| Fonction | Propriété (pour tout `acc`) | On en déduit |
|---|---|---|
| `factAux n acc` | `= acc × n!` | `acc = 1` : `factAux n 1 = n!` |
| `produitAux l acc` | `= acc × produit l` | `acc = 1` : le produit de `l` |
| `compteAux k l acc` | `= acc + compte k l` | `acc = 0` : le nombre d'occurrences de `k` |
| `p2Aux n acc` | `= acc × 2ⁿ` | `acc = 1` : `2ⁿ` |

> 💡 Toujours la même phrase : **ce qui est dans la calculatrice** combiné avec **ce qui reste à calculer** donne **le résultat final**.

---

## Exercice 7 ⭐⭐ — `factAux`

**Pré** `n ≥ 0` · **Post** `factAux n acc = acc × n!` (pour tout `acc`) · **Variant** `n`.
**HI** : pour tout `k < n` avec `k ≥ 0` et **pour tout** `acc'`, `factAux k acc' = acc' × k!`.

- **Cas `n = 0`** : `factAux 0 acc = acc = acc × 0!` (car `0! = 1`) ✅
- **Cas `n ≠ 0`** : `factAux n acc = factAux (n-1) (acc × n)`.
  - ① `n − 1 < n` ② `n − 1 ≥ 0` (car `n ≥ 0` et `n ≠ 0`)
  - HI avec `acc' = acc × n` : `factAux (n-1) (acc × n) = acc × n × (n − 1)! = acc × n!` ✅

Ce qui achève la preuve par induction. ∎

**Conséquence** : avec `acc = 1`, `factAux n 1 = 1 × n! = n!`.

> 💬 L'HI est utilisée avec `acc' = acc × n`, **pas** avec `acc`. C'est pour ça qu'elle doit parler de **tout** `acc'`.

---

## Exercice 8 ⭐⭐⭐ — `longAux`

1. **Variant** `length l`. **HI** : pour toute `l'` plus courte que `l` et **tout** `acc'`, `longAux l' acc' = acc' + length l'`.
   - **Cas `l = []`** : `longAux [] acc = acc = acc + 0 = acc + length []` ✅
   - **Cas `l = x : l'`** : `longAux l acc = longAux l' (acc + 1)`.
     - ① `length l' < length l` ② rien à vérifier
     - HI avec `acc' = acc + 1` : `= acc + 1 + length l' = acc + length l` ✅

   Ce qui achève la preuve par induction. ∎

2. Avec `acc = 0` : `longAux l 0 = 0 + length l = length l`.

3. Dans le cas `x : l'`, l'appel récursif se fait avec `acc + 1`, qui ne vaut **pas** 0 (il vaut au moins 1). Une HI qui ne parle que de `acc = 0` ne s'appliquerait donc **pas** à cet appel.

---

## Exercice 9 ⭐⭐⭐ — La somme des chiffres

1. | Tour | `n` | `s` |
   |---|---|---|
   | départ | 472 | 0 |
   | 1 | 47 | 2 |
   | 2 | 4 | 9 |
   | 3 | 0 | 13 |

   Résultat : **13** (`4 + 7 + 2`).

2. ```haskell
   chiffresAux :: Int -> Int -> Int
   chiffresAux n s | n == 0    = s
                   | otherwise = chiffresAux (n `div` 10) (s + n `mod` 10)

   sommeChiffres n = chiffresAux n 0
   ```
   (La boucle s'arrête quand `n > 0` est faux, c'est-à-dire `n = 0` puisque `n ≥ 0`.)

3. **Pré** `n ≥ 0` · **Post** `chiffresAux n s = s + sc n` (pour tout `s`) · **Variant** `n`.
   **HI** : pour tout `m < n` avec `m ≥ 0` et tout `s'`, `chiffresAux m s' = s' + sc m`.
   - **Cas `n = 0`** : `chiffresAux 0 s = s = s + 0 = s + sc 0` ✅
   - **Cas `n > 0`** : posons ``m = n `div` 10`` et ``c = n `mod` 10``.
     - ① `m < n` car `n > 0` ② `m ≥ 0`
     - HI avec `s' = s + c` : `chiffresAux m (s + c) = s + c + sc m = s + sc n` (définition de `sc`) ✅

   Ce qui achève la preuve par induction. ∎

---

## Exercice 10 ⭐⭐⭐ — La longueur de la pile

**Variant** `length l`. **HI** : pour toute `l'` plus courte que `l` et **toute** `acc'`, `length (revAux l' acc') = length l' + length acc'`.

- **Cas `l = []`** : `length (revAux [] acc) = length acc = 0 + length acc` ✅
- **Cas `l = x : l'`** : `revAux l acc = revAux l' (x : acc)`.
  - ① `length l' < length l` ② rien à vérifier
  - HI avec `acc' = x : acc` : `length (revAux l' (x:acc)) = length l' + length (x : acc) = length l' + 1 + length acc = length l + length acc` ✅

Ce qui achève la preuve par induction. ∎

**Conséquence** : `length (revRT l) = length (revAux l []) = length l + 0 = length l`.

> 📚 Retourner une pile de livres ne fait ni apparaître ni disparaître de livre.
