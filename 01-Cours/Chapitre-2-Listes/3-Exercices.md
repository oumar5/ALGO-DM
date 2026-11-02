# Chapitre 2 — Exercices

[🏠 Accueil](../../README.md) · [⬅ Cours](1-Cours.md) · [Exemples corrigés](2-Exemples-corriges.md) · **Corrections : [4-Corrections.md](4-Corrections.md)**

> ⭐ = échauffement · ⭐⭐ = entraînement · ⭐⭐⭐ = niveau DS

Rappels utiles :

```haskell
length []    = 0                  [] ++ l2     = l2
length (_:l) = 1 + length l       (a:l1) ++ l2 = a : (l1 ++ l2)

estOrdonnee (x:y:l) | x <= y    = estOrdonnee (y:l)
                    | otherwise = False
estOrdonnee _ = True
```

---

## Exercice 1 ⭐ — Quel motif correspond ?

Complète le tableau : le motif correspond-il ? Si oui, que valent les variables ?

| Motif | `[]` | `[5]` | `[1,2,3]` |
|---|---|---|---|
| `(x:l)` | | | |
| `(x:y:l)` | | | |
| `[x]` | | | |
| `_` | | | |

---

## Exercice 2 ⭐ — Calculer pas à pas

1. `length [4,4,4]`
2. `[1] ++ [2,3]`
3. `estOrdonnee [2,2,5]`
4. `estOrdonnee [3,1]`

---

## Exercice 3 ⭐ — Le relevé de notes

> 📋 `notes = [12, 8, 15, 9, 18]`

Écris une liste en compréhension, puis donne son résultat :
1. les notes **≥ 10** ;
2. chaque note avec un **bonus de 2 points**, sans dépasser 20 (indice : `min 20 x`) ;
3. le **nombre** d'étudiants admis (note ≥ 10).

---

## Exercice 4 ⭐ — Deux faux tris

```haskell
triVide :: [Int] -> [Int]          triRien :: [Int] -> [Int]
triVide l = []                     triRien l = l
```

Pour chacune : le résultat est-il **trié** ? Est-il une **permutation** de l'entrée ? Est-ce un tri correct ?

---

## Exercice 5 ⭐⭐ — Écrire des fonctions

1. 🛒 `somme :: [Int] -> Int` : le total d'un panier. `somme [3,5,2] = 10`.
2. 🎵 `compte :: Int -> [Int] -> Int` : combien de fois la chanson `k` apparaît dans l'historique. `compte 7 [7,2,7,7] = 3`.
3. 🔎 `appartient :: Int -> [Int] -> Bool` : `k` est-il dans la liste ?

---

## Exercice 6 ⭐⭐ — Le dernier et le plus grand

1. Écris `dernier :: [Int] -> Int` qui renvoie le dernier élément (le dernier wagon 🚂).
2. Écris `maxi :: [Int] -> Int` qui renvoie le plus grand élément.
3. Donne la pré-condition et la post-condition de chacune. Pourquoi faut-il une pré-condition ?

---

## Exercice 7 ⭐⭐ — Deux paniers à la caisse

> 🛒🛒 Si on passe deux paniers ensemble, le total est la somme des deux totaux.

Avec ta fonction `somme` de l'exercice 5, démontre :

```text
somme (l1 ++ l2) = somme l1 + somme l2
```

---

## Exercice 8 ⭐⭐ — Les prix doublés

```haskell
double :: [Int] -> [Int]
double []    = []
double (x:l) = 2 * x : double l
```

Démontre :
1. `length (double l) = length l` ;
2. `somme (double l) = 2 * somme l`.

---

## Exercice 9 ⭐⭐ — Filtrer ne rallonge pas

```haskell
positifs :: [Int] -> [Int]
positifs []    = []
positifs (x:l) | x > 0     = x : positifs l
               | otherwise = positifs l
```

1. Calcule `positifs [3,-1,0,5]`.
2. Démontre que `length (positifs l) ≤ length l`.
3. Où ce résultat a-t-il servi dans le cours ?

---

## Exercice 10 ⭐⭐ — Trouve l'erreur 🕵️

On veut prouver que `l1 ++ l2 = l2 ++ l1`. Voici une « preuve » :

> Induction sur `length l1`.
> **Cas `l1 = []`** : `[] ++ l2 = l2 = l2 ++ []` ✅
> **Cas `l1 = a : l1'`** : `(a : l1') ++ l2 = a : (l1' ++ l2) = a : (l2 ++ l1')` par HI, `= l2 ++ (a : l1')` ✅

1. Trouve deux listes qui montrent que la propriété est **fausse**.
2. Quelle étape de la « preuve » est fausse ?

---

## Exercice 11 ⭐⭐⭐ — Compter dans deux listes

Avec ta fonction `compte`, démontre :

```text
compte k (l1 ++ l2) = compte k l1 + compte k l2
```

> 💡 C'est ce résultat qui permet de dire que « deux listes ont les mêmes éléments » : chaque valeur y apparaît **le même nombre de fois**.

---

## Exercice 12 ⭐⭐⭐ — Insérer une carte dans sa main 🃏

```haskell
inserer :: Int -> [Int] -> [Int]
inserer k []    = [k]
inserer k (n:l) | k <= n    = k : n : l
                | otherwise = n : inserer k l
```

1. Calcule `inserer 4 [1,3,5,7]`.
2. Démontre que `length (inserer k l) = 1 + length l`.
3. Démontre : si `l` est ordonnée, alors
   - (P1) `inserer k l` est ordonnée, et
   - (P2) le premier élément de `inserer k l` est soit `k`, soit le premier élément de `l`.

> 💡 Pourquoi ajouter P2 ? Parce que dans le cas `k > n`, pour savoir que `n : inserer k l'` est rangée, il faut connaître **le premier élément** de `inserer k l'`.
