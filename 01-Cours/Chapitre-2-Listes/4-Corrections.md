# Chapitre 2 — Corrections

[🏠 Accueil](../../README.md) · [⬅ Exercices](3-Exercices.md) · [Cours](1-Cours.md)

> ⚠️ As-tu cherché au moins 10 minutes ?

---

## Exercice 1 ⭐ — Les motifs

| Motif | `[]` | `[5]` | `[1,2,3]` |
|---|---|---|---|
| `(x:l)` | ❌ | ✅ `x = 5`, `l = []` | ✅ `x = 1`, `l = [2,3]` |
| `(x:y:l)` | ❌ | ❌ (un seul wagon) | ✅ `x = 1`, `y = 2`, `l = [3]` |
| `[x]` | ❌ | ✅ `x = 5` | ❌ (trois wagons) |
| `_` | ✅ | ✅ | ✅ |

---

## Exercice 2 ⭐ — Pas à pas

1. `length [4,4,4] = 1 + length [4,4] = 1 + 1 + length [4] = 1 + 1 + 1 + length [] = 3`
2. `[1] ++ [2,3] = 1 : ([] ++ [2,3]) = 1 : [2,3] = [1,2,3]`
3. `estOrdonnee [2,2,5]` → `2 <= 2` → `estOrdonnee [2,5]` → `2 <= 5` → `estOrdonnee [5]` → `True`
4. `estOrdonnee [3,1]` → `3 <= 1` est faux → `False`

---

## Exercice 3 ⭐ — Le relevé de notes

| Question | Expression | Résultat |
|---|---|---|
| 1 | `[n \| n <- notes, n >= 10]` | `[12,15,18]` |
| 2 | `[min 20 (n + 2) \| n <- notes]` | `[14,10,17,11,20]` |
| 3 | `length [n \| n <- notes, n >= 10]` | `3` |

---

## Exercice 4 ⭐ — Les faux tris

| | Trié ? | Permutation ? | Tri correct ? |
|---|---|---|---|
| `triVide` | ✅ `[]` est trié | ❌ (sauf si l'entrée est vide) : on a perdu les éléments | ❌ |
| `triRien` | ❌ (sauf si l'entrée est déjà triée) | ✅ c'est la même liste | ❌ |

> 💡 Chacun ne vérifie qu'**une** des deux conditions. Un vrai tri doit vérifier **les deux**.

---

## Exercice 5 ⭐⭐ — Les fonctions

```haskell
somme :: [Int] -> Int
somme []    = 0
somme (x:l) = x + somme l

compte :: Int -> [Int] -> Int
compte k []    = 0
compte k (x:l) | x == k    = 1 + compte k l
               | otherwise = compte k l

appartient :: Int -> [Int] -> Bool
appartient k []    = False
appartient k (x:l) = x == k || appartient k l
```

> 💬 Les trois suivent le même plan : **un cas pour `[]`**, **un cas pour `x : l`** qui traite `x` et rappelle la fonction sur `l`.

---

## Exercice 6 ⭐⭐ — Le dernier et le plus grand

```haskell
dernier :: [Int] -> Int
dernier [x]   = x
dernier (_:l) = dernier l

maxi :: [Int] -> Int
maxi [x]   = x
maxi (x:l) = max x (maxi l)
```

| Fonction | Pré | Post |
|---|---|---|
| `dernier l` | `l ≠ []` | le résultat est le dernier élément de `l` |
| `maxi l` | `l ≠ []` | le résultat est un élément de `l`, et il est ≥ tous les éléments de `l` |

**Pourquoi une pré-condition ?** Une liste vide n'a ni dernier élément ni maximum : aucune équation ne correspond à `[]`, et le programme **plante**.

> 💬 Dans `dernier (_:l) = dernier l`, la liste `l` n'est jamais vide : si elle l'était, c'est la première équation `[x]` qui aurait été choisie. La pré-condition est donc conservée.

---

## Exercice 7 ⭐⭐ — Deux paniers

**Variant** `length l1` (car `++` avance dans `l1`).
**HI** : pour toute `l1'` plus courte que `l1` (et toute `l2`), `somme (l1' ++ l2) = somme l1' + somme l2`.

- **Cas `l1 = []`** : `somme ([] ++ l2) = somme l2 = 0 + somme l2 = somme [] + somme l2` ✅
- **Cas `l1 = a : l1'`** :

  ```text
  somme ((a:l1') ++ l2) = somme (a : (l1' ++ l2))      définition de ++
                        = a + somme (l1' ++ l2)        définition de somme
                        = a + somme l1' + somme l2     HI (variant ↓)
                        = somme l1 + somme l2          définition de somme  ✅
  ```

Ce qui achève la preuve par induction. ∎

---

## Exercice 8 ⭐⭐ — Les prix doublés

**Variant** `length l`. Deux preuves avec les mêmes cas.

| | Cas `l = []` | Cas `l = x : l'` (HI sur `l'`, variant ↓) |
|---|---|---|
| 1 | `length (double []) = length [] = 0` ✅ | `length (2x : double l') = 1 + length (double l') = 1 + length l' = length l` ✅ |
| 2 | `somme (double []) = 0 = 2 × 0` ✅ | `somme (2x : double l') = 2x + somme (double l') = 2x + 2 × somme l' = 2 × (x + somme l') = 2 × somme l` ✅ |

Ce qui achève les deux preuves par induction. ∎

---

## Exercice 9 ⭐⭐ — Filtrer

1. `positifs [3,-1,0,5] = 3 : positifs [-1,0,5] = 3 : positifs [0,5] = 3 : positifs [5] = 3 : 5 : [] = [3,5]`

2. **Variant** `length l`. **HI** : pour toute `l'` plus courte, `length (positifs l') ≤ length l'`.
   - **Cas `[]`** : `0 ≤ 0` ✅
   - **Cas `x : l'` avec `x > 0`** : `length (x : positifs l') = 1 + length (positifs l') ≤ 1 + length l'` (HI) `= length l` ✅
   - **Cas `x : l'` avec `x ≤ 0`** : `length (positifs l') ≤ length l'` (HI) `< length l` ✅

   Ce qui achève la preuve par induction. ∎

3. Dans la preuve du **tri rapide** : on a besoin de `length bas ≤ length l'`, et `bas` est justement une liste filtrée.

---

## Exercice 10 ⭐⭐ — L'erreur

1. `[1] ++ [2] = [1,2]` mais `[2] ++ [1] = [2,1]`. La propriété est **fausse**.
2. La dernière égalité : **`a : (l2 ++ l1') = l2 ++ (a : l1')`** est fausse. À gauche, `a` est **en tête** ; à droite, `a` est **après** tous les éléments de `l2`. (Les étapes précédentes sont justes.)

> 💡 **Leçon :** chaque égalité d'une preuve doit être justifiée par une **règle précise** (une définition, l'HI, un résultat prouvé). Celle-ci n'en avait aucune.

---

## Exercice 11 ⭐⭐⭐ — Compter dans deux listes

**Variant** `length l1`. **HI** : pour toute `l1'` plus courte, `compte k (l1' ++ l2) = compte k l1' + compte k l2`.

- **Cas `l1 = []`** : `compte k ([] ++ l2) = compte k l2 = 0 + compte k l2` ✅
- **Cas `l1 = a : l1'`** : `compte k ((a:l1') ++ l2) = compte k (a : (l1' ++ l2))`. Deux sous-cas :

  | Sous-cas | Calcul |
  |---|---|
  | `a == k` | `1 + compte k (l1' ++ l2) = 1 + compte k l1' + compte k l2` (HI) `= compte k l1 + compte k l2` ✅ |
  | `a ≠ k` | `compte k (l1' ++ l2) = compte k l1' + compte k l2` (HI) `= compte k l1 + compte k l2` ✅ |

Ce qui achève la preuve par induction. ∎

---

## Exercice 12 ⭐⭐⭐ — Insérer une carte

1. ```text
   inserer 4 [1,3,5,7] = 1 : inserer 4 [3,5,7]       (4 > 1)
                       = 1 : 3 : inserer 4 [5,7]     (4 > 3)
                       = 1 : 3 : 4 : 5 : [7]         (4 ≤ 5)
                       = [1,3,4,5,7]
   ```

2. **Variant** `length l`. HI sur toute liste plus courte.
   - `l = []` : `length [k] = 1 = 1 + 0` ✅
   - `l = n : l'`, `k ≤ n` : `length (k : n : l') = 1 + length (n : l') = 1 + length l` ✅
   - `l = n : l'`, `k > n` : `length (n : inserer k l') = 1 + length (inserer k l') = 1 + 1 + length l'` (HI) `= 1 + length l` ✅

3. **Pré** `l` ordonnée · **Post** P1 et P2 · **Variant** `length l`.
   **HI** : pour toute `l'` ordonnée plus courte que `l`, `inserer k l'` est ordonnée et commence par `k` ou par le premier élément de `l'`.

   **Cas `l = []`** : le résultat `[k]` est ordonné (un seul élément) et commence par `k` ✅

   **Cas `l = n : l'` et `k ≤ n`** : le résultat est `k : n : l'`.
   - P1 : `estOrdonnee (k : n : l') = (k ≤ n) && estOrdonnee (n : l')`. `k ≤ n` (cas) et `n : l' = l` est ordonnée (pré) ✅
   - P2 : il commence par `k` ✅

   **Cas `l = n : l'` et `k > n`** : le résultat est `n : inserer k l'`.
   - HI sur `l'` : ① `length l' < length l` ② `l'` est ordonnée (c'est la fin de `l`, qui est ordonnée) ✅
   - Donc `inserer k l'` est ordonnée, non vide, et son premier élément `p` vaut `k` ou le premier élément de `l'`.
   - P1 : `estOrdonnee (n : inserer k l') = (n ≤ p) && estOrdonnee (inserer k l')`.
     - si `p = k` : `n < k` (cas) ✅
     - si `p` est le premier élément de `l'` : `n ≤ p` car `l = n : l'` est ordonnée ✅
   - P2 : le résultat commence par `n`, le premier élément de `l` ✅

   Ce qui achève la preuve par induction. ∎
