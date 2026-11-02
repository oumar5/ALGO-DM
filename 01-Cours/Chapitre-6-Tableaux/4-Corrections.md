# Chapitre 6 — Corrections

[🏠 Accueil](../../README.md) · [⬅ Exercices](3-Exercices.md) · [Cours](1-Cours.md)

> ⚠️ As-tu cherché au moins 10 minutes ?

---

## Exercice 1 ⭐ — Ça plante ou pas

| | Expression | Ne plante pas si… |
|---|---|---|
| a | `a / (b - c)` | `b ≠ c` |
| b | `l[i + 1]` | `0 ≤ i + 1 < len(l)`, c'est-à-dire `−1 ≤ i < len(l) − 1` |
| c | `sqrt(x - 4)` | `x ≥ 4` |
| d | `x != 0 and 10 / x > 1` | **toujours** : si `x = 0`, la division n'est pas calculée |
| e | `l[i] > 0 and i < len(l)` | `0 ≤ i < len(l)` : `l[i]` est lu **en premier** |
| f | `i < len(l) and l[i] > 0` | `i ≥ 0` : si `i ≥ len(l)`, `l[i]` n'est pas lu |

`e` et `f` testent la même chose, mais **dans un ordre différent**. Dans `e`, on lit la case **avant** de vérifier qu'elle existe : c'est comme ouvrir le carton de lait avant de vérifier qu'il y en a dans le frigo. 🥛

---

## Exercice 2 ⭐ — Remplacer des œufs

| | Tableau | Même sac que `l` ? |
|---|---|---|
| 1 | `[4, 0, 2, 7]` | ❌ le 9 a disparu, un 0 est apparu |
| 2 | `[7, 9, 2, 4]` | ✅ on a **échangé** les cases 0 et 3 |
| 3 | `[4, 9, 4, 7]` | ❌ le 2 a disparu, le 4 est en double |

---

## Exercice 3 ⭐ — Écrire dans une case

```python
# l[0] + 1 > 5  et  0 ≤ 0 < len(l)      ⇔  l[0] > 4  et  len(l) ≥ 1
l[0] = l[0] + 1
# l[0] > 5
```

La post-condition parle du **nouveau** tableau `l[0 → l[0] + 1]`, dont la case 0 vaut `l[0] + 1`. La lecture et l'écriture de `l[0]` exigent que la case 0 existe : `len(l) ≥ 1`.

---

## Exercice 4 ⭐⭐ — Échanger deux œufs

```python
# l[j] ≤ l[i]  (le cas i = j est inclus : l[i] ≤ l[i])   et   0 ≤ i, j < len(l)
v = l[i]
# i = j  ou  (i ≠ j et l[j] ≤ v)
l[i] = l[j]
# (i = j et v ≤ v)  ou  (i ≠ j et l[i] ≤ v)       ← la case j vaudra v
l[j] = v
# l[i] ≤ l[j]
```

Détail de la dernière remontée : après `l[j] = v`, la case `j` vaut `v`, et la case `i` vaut `v` si `i = j`, sinon `l[i]`.

**En français :** pour qu'après l'échange la case `i` soit ≤ la case `j`, il faut qu'**avant** l'échange la case `j` soit ≤ la case `i`. Logique : on a inversé les deux œufs !

---

## Exercice 5 ⭐⭐ — Le total des dépenses

| | |
|---|---|
| **Invariant** | (I1) `0 ≤ i ≤ len(t)` et (I2) `s = t[0] + … + t[i − 1]` |
| **Condition** | (CB) `i < len(t)` |
| **Variant** | `len(t) − i` |

| Étape | Vérification |
|---|---|
| ① Corps | il lit `t[i]` : il faut `0 ≤ i < len(t)`, vrai par I1 et CB ✅ |
| ② Variant | `i` augmente de 1, donc `len(t) − i` baisse de 1 ; ≥ 0 par I1 ✅ |
| ③ Condition | `i < len(t)` ne lit aucune case ✅ |
| ④ Invariant | voir ci-dessous ✅ |
| ⑤ Départ | `s = 0` et `i = 0` : la somme de `t[0]` à `t[−1]` est **vide**, elle vaut 0 ; `0 ≤ 0 ≤ len(t)` ✅ |
| ⑥ Arrivée | `i ≥ len(t)` et `i ≤ len(t)` ⇒ `i = len(t)`, donc `s = t[0] + … + t[len(t) − 1]` ✅ |

**④ en détail**

```python
# s + t[i] = t[0] + … + t[i]   et   0 ≤ i + 1 ≤ len(t)
s = s + t[i]
# s = t[0] + … + t[i]   et   0 ≤ i + 1 ≤ len(t)
i = i + 1
# s = t[0] + … + t[i − 1]   et   0 ≤ i ≤ len(t)
```

Par I2, `s + t[i] = (t[0] + … + t[i − 1]) + t[i]` ✅. Par CB et I1, `0 ≤ i + 1 ≤ len(t)` ✅

---

## Exercice 6 ⭐⭐ — Combien d'admis

1. | `i` | `t[i]` | `c` après le tour |
   |---|---|---|
   | 0 | 12 | 1 |
   | 1 | 8 | 1 |
   | 2 | 15 | 2 |
   | 3 | 9 | 2 |

   Résultat : `c = 2`.

2. **Invariant** : (I1) `0 ≤ i ≤ len(t)` ; (I2) `c` = nombre de `k < i` tels que `t[k] ≥ 10`. **Variant** `len(t) − i`.

   - **④** Le tour regarde **une case de plus**, la case `i`.
     - si `t[i] ≥ 10` : `c` augmente de 1, et la case `i` compte ✅
     - sinon : `c` ne change pas, et la case `i` ne compte pas ✅

     Dans les deux cas, `c` compte les cases `k < i + 1`, puis `i` devient `i + 1` ✅
   - **⑤** `c = 0`, `i = 0` : aucune case avant 0, le nombre vaut 0 ✅
   - **⑥** `i = len(t)` (condition fausse + I1), donc `c` compte **toutes** les cases ✅

---

## Exercice 7 ⭐⭐ — Chercher un nom

1. - `v = 2` : `t[0] = 4 ≠ 2` → `i = 1` ; `t[1] = 7 ≠ 2` → `i = 2` ; `t[2] = 2` : arrêt. **`i = 2`**, et `t[2] = 2` ✅
   - `v = 5` : aucune case ne vaut 5 ; `i` monte jusqu'à `4 = len(t)` : arrêt car `i < len(t)` est faux.

2. `and` est **paresseux** : si `i < len(t)` est faux, `t[i]` n'est **pas** lu.

3. **Invariant** : (I1) `0 ≤ i ≤ len(t)` ; (I2) pour tout `k < i`, `t[k] ≠ v`. **Variant** `len(t) − i`.

   | Étape | Vérification |
   |---|---|
   | ① Corps | `i = i + 1` ne plante pas ✅ |
   | ② Variant | `i` augmente de 1 ; ≥ 0 par I1 ✅ |
   | ③ Condition | si `i < len(t)`, la case `t[i]` existe (I1 donne `i ≥ 0`) ; sinon, elle n'est pas lue ✅ |
   | ④ Invariant | on entre dans le tour car `i < len(t)` et `t[i] ≠ v`. Donc les cases `0` à `i` sont toutes `≠ v`, puis `i` devient `i + 1`. Et `i + 1 ≤ len(t)` ✅ |
   | ⑤ Départ | `i = 0` : aucune case avant 0 ✅ |
   | ⑥ Arrivée | voir ci-dessous ✅ |

   **⑥** La condition est fausse : `i ≥ len(t)` **ou** `t[i] = v`.
   - si `i < len(t)` : c'est donc que `t[i] = v` ✅
   - sinon `i = len(t)` (avec I1) : par I2, **aucune** case ne vaut `v`, donc `v` n'est pas dans `t` ✅

---

## Exercice 8 ⭐⭐⭐ — La température maximale

1. | Après | `i` | `m` |
   |---|---|---|
   | départ | 1 | 12 |
   | tour 1 (`17 > 12`) | 2 | 17 |
   | tour 2 (`9 > 17` ? non) | 3 | 17 |
   | tour 3 (`17 > 17` ? non) | 4 | 17 |
   | tour 4 (`14 > 17` ? non) | 5 | 17 |

   Maximum : **17**.

2. **Invariant** :
   - (I1) `1 ≤ i ≤ len(t)`
   - (I2) `m` est l'une des valeurs `t[0], …, t[i − 1]`
   - (I3) pour tout `k < i`, `t[k] ≤ m`

   **Variant** `len(t) − i`.

   | Étape | Vérification |
   |---|---|
   | ① Corps | il lit `t[i]` : `1 ≤ i < len(t)` par I1 et la condition ✅ |
   | ② Variant | `i` augmente de 1 ; ≥ 0 par I1 ✅ |
   | ③ Condition | `i < len(t)` ne lit rien ✅ |
   | ⑤ Départ | `m = t[0]`, `i = 1` : il faut `t[0]` lisible et `1 ≤ len(t)` (pré : `len(t) > 0`) ; `m` est `t[0]` ✅ ; `t[0] ≤ m` ✅ |
   | ⑥ Arrivée | `i = len(t)` (condition fausse + I1) : I2 et I3 parlent de **tout** le tableau ✅ |

   **④** Deux cas :
   - **`t[i] > m`** : le nouveau `m` vaut `t[i]`, qui est une valeur du tableau (I2) ✅. Les cases d'avant sont `≤` l'ancien `m` `< t[i]`, et `t[i] ≤ t[i]` (I3) ✅
   - **`t[i] ≤ m`** : `m` ne change pas. I2 reste vrai ; I3 s'étend à la case `i` grâce au cas ✅

   Puis `i` devient `i + 1 ≤ len(t)` ✅

---

## Exercice 9 ⭐⭐⭐ — Retourner une étagère

1. | `t` | Tours |
   |---|---|
   | `[1, 2, 3, 4, 5]` | `g=0, d=4` → `[5, 2, 3, 4, 1]` → `g=1, d=3` → `[5, 4, 3, 2, 1]` → `g=2, d=2` : arrêt |
   | `[1, 2, 3, 4]` | `g=0, d=3` → `[4, 2, 3, 1]` → `g=1, d=2` → `[4, 3, 2, 1]` → `g=2, d=1` : arrêt |

2. - (I2) pour tout `k < g` ou `k > d` : **`t[k] = t0[n − 1 − k]`** (les bords sont déjà retournés)
   - (I3) pour tout `g ≤ k ≤ d` : **`t[k] = t0[k]`** (le milieu n'a pas bougé)

   ```mermaid
   flowchart LR
       A["0 … g−1<br/>déjà retourné"] --> B["g … d<br/>pas encore touché"] --> C["d+1 … n−1<br/>déjà retourné"]
   ```

3. **Variant** `d − g`. **Condition** `g < d`.

   | Étape | Vérification |
   |---|---|
   | ① Corps | il touche `t[g]` et `t[d]`. `g ≥ 0` (I1) ; `g < d` (condition) donc `d ≥ 0` ; `d = n − 1 − g ≤ n − 1` (I1) donc `g < d < n` ✅ |
   | ② Variant | `g` monte de 1 et `d` descend de 1 : `d − g` baisse de 2. Sous la condition, `d − g > 0` ✅ |
   | ③ Condition | `g < d` ne lit rien ✅ |
   | ⑤ Départ | `g = 0`, `d = n − 1` : `0 + n − 1 = n − 1` ✅ ; I2 : aucun `k < 0` ni `k > n − 1` ✅ ; I3 : `t = t0` ✅ |

   **④** Le tour échange les cases `g` et `d`. Par I3, elles contenaient `t0[g]` et `t0[d]`. Après l'échange :
   - case `g` : `t0[d] = t0[n − 1 − g]` (car `d = n − 1 − g`) : elle est **retournée** ✅
   - case `d` : `t0[g] = t0[n − 1 − d]` : elle est **retournée** ✅
   - les autres cases ne bougent pas ✅

   Puis `g + 1` et `d − 1` : leur somme vaut toujours `n − 1`, et `g + 1 ≥ 0` ✅

   **⑥ Arrivée** : `g ≥ d` et `g + d = n − 1`.
   - toutes les cases `k < g` ou `k > d` sont retournées (I2) ;
   - s'il reste une case du milieu (`g = d`, quand `n` est impair), alors `k = g` vérifie `k = n − 1 − k` : par I3, `t[k] = t0[k] = t0[n − 1 − k]` ✅

   Donc `t[k] = t0[n − 1 − k]` pour tout `k` ✅

---

## Exercice 10 ⭐⭐⭐ — Le tableau est-il rangé ?

1. | Tour | `i` avant | test `t[i−1] > t[i]` | `ok` après | `i` après |
   |---|---|---|---|---|
   | 1 | 1 | `1 > 3` ? non | True | 2 |
   | 2 | 2 | `3 > 2` ? **oui** | False | 3 |

   La boucle s'arrête après **2 tours** car `ok` est faux : inutile de regarder la suite. Résultat `ok = False` ✅

2. **Invariant** : (I1) `1 ≤ i ≤ len(t)` ; (I2) `ok = True` ssi les cases `0` à `i − 1` sont rangées (`t[k − 1] ≤ t[k]` pour tout `0 < k < i`).

   - **④** On entre dans le tour avec `ok = True` : les cases `0` à `i − 1` sont rangées. Après le tour :
     - si `t[i − 1] > t[i]` : `ok = False`, et les cases `0` à `i` ne sont pas rangées ✅
     - sinon : `ok = True`, et les cases `0` à `i` sont rangées ✅

     Puis `i` devient `i + 1 ≤ len(t)` (car `i < len(t)`) ✅
   - **⑤** `ok = True`, `i = 1` : une seule case (la case 0), qui est forcément rangée ✅ ; `1 ≤ len(t)` par la pré-condition ✅
   - **⑥** La condition est fausse : `i ≥ len(t)` **ou** `ok = False`.
     - si `ok = False` : par I2, un début du tableau n'est pas rangé, donc `t` n'est pas trié. `ok = False` est la bonne réponse ✅
     - si `ok = True` : alors `i ≥ len(t)`, donc `i = len(t)` (I1), et par I2 **tout** le tableau est rangé ✅
