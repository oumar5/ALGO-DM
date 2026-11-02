# Chapitre 1 — Corrections

[🏠 Accueil](../../README.md) · [⬅ Exercices](3-Exercices.md) · [Cours](1-Cours.md)

> ⚠️ As-tu cherché au moins 10 minutes ? Une correction lue trop tôt ne s'apprend pas.

---

## Exercice 1 ⭐ — `puissance2 3`

```text
puissance2 3 = 2 * puissance2 2
             = 2 * (2 * puissance2 1)
             = 2 * (2 * (2 * puissance2 0))
             = 2 * (2 * (2 * 1))  =  8
```

Au bout de 3 heures, il y a **8 bactéries**.

---

## Exercice 2 ⭐ — Les mentions

1. | Appel | Première garde vraie | Résultat |
   |---|---|---|
   | `mention 15` | `15 >= 14` | `"Bien"` |
   | `mention 10` | `10 >= 10` | `"Admis"` |
   | `mention 9` | aucune | `"Ajourné"` |
   | `mention 17` | `17 >= 16` | `"Très bien"` |

2. Avec `>= 14` en premier, `mention 17` donne **`"Bien"`** : `17 >= 14` est vrai, et c'est **la première garde vraie** qui gagne. La ligne `>= 16` n'est jamais atteinte : plus personne n'a « Très bien ».

---

## Exercice 3 ⭐ — Les contrats

| Fonction | Pré-condition | Post-condition |
|---|---|---|
| `retrait solde montant` | `0 ≤ montant ≤ solde` (on ne retire pas plus que ce qu'on a) | le résultat `r` vérifie `r ≥ 0` et `r + montant = solde` |
| `racineEntiere n` | `n ≥ 0` | le résultat `r` vérifie `r ≥ 0` et `r² ≤ n < (r+1)²` |
| `dernierChiffre n` | `n ≥ 0` | le résultat `r` vérifie `0 ≤ r ≤ 9` et `n − r` est un multiple de 10 |

> 💬 Pour `racineEntiere 10 = 3` : `3² = 9 ≤ 10 < 16 = 4²`. La post-condition dit exactement « 3 est le plus grand nombre dont le carré ne dépasse pas 10 ».

---

## Exercice 4 ⭐ — Les variants

| Fonction | Pré-condition | Variant | Explication |
|---|---|---|---|
| `f` | `n ≥ 0` | `n` | `n` baisse de 1 et s'arrête à 0. Avec `n < 0`, on descend sans jamais atteindre 0 : **boucle infinie**. |
| `g` | aucune | `b − a` (ou `max 0 (b − a)` pour qu'il soit toujours ≥ 0) | on n'appelle que si `a < b`, donc `b − a > 0`, et `a` augmente de 1 : `b − a` baisse de 1. |
| `h` | `n ≥ 1` | `n` | on n'appelle que si `n ≥ 2` : alors `1 ≤ n div 2 < n`. Avec `n = 0` : `h 0` appelle `h 0`, **boucle infinie**. |
| `k` | `n ≤ 0` | `−n` | pour `n > 0`, `n` augmente et ne vaut jamais 0 : **boucle infinie**. Pour `n ≤ 0`, `n` remonte vers 0 : `−n` baisse. |

> 💡 **Leçon :** la pré-condition sert souvent **à garantir que le compte à rebours finit**.

---

## Exercice 5 ⭐⭐ — Le carrelage

**Objectif :** `S(n) = 1 + 3 + … + (2n − 1) = n²`.
**Induction sur `n`.** HI : pour tout `k < n`, `S(k) = k²`.

- **Cas `n = 0`** : la somme est vide, `S(0) = 0 = 0²` ✅
- **Cas `n ≥ 1`** : `S(n) = S(n − 1) + (2n − 1)`. Comme `n − 1 < n`, l'HI donne `S(n − 1) = (n − 1)²`. Donc :

  ```text
  S(n) = (n − 1)² + 2n − 1 = n² − 2n + 1 + 2n − 1 = n²  ✅
  ```

Ce qui achève la preuve par induction. ∎

> 🟦 C'est exactement le carrelage : le carré `(n−1) × (n−1)` plus l'équerre de `2n − 1` carreaux donne le carré `n × n`.

---

## Exercice 6 ⭐⭐ — `puissance2 n = 2ⁿ`

| | |
|---|---|
| **Pré** | `n ≥ 0` |
| **Post** | `puissance2 n = 2ⁿ` |
| **Variant** | `n` (≥ 0 par la pré-condition) |
| **HI** | pour tout `k < n` avec `k ≥ 0`, `puissance2 k = 2ᵏ` |

- **Cas `n = 0`** : `puissance2 0 = 1 = 2⁰` ✅
- **Cas `n ≠ 0`** : `puissance2 n = 2 * puissance2 (n-1)`.
  - ① variant : `n − 1 < n` ✅
  - ② pré : `n − 1 ≥ 0` car `n ≥ 0` et `n ≠ 0` ✅
  - HI : `puissance2 (n-1) = 2ⁿ⁻¹`, donc `puissance2 n = 2 × 2ⁿ⁻¹ = 2ⁿ` ✅

Ce qui achève la preuve par induction. ∎

---

## Exercice 7 ⭐⭐ — La tirelire

1. `tirelire 12 = 10 + 5 × 12 = 70` €.
2. **Pré** `n ≥ 0` · **Post** `tirelire n = 10 + 5n` · **Variant** `n`.
   **HI** : pour tout `k < n` avec `k ≥ 0`, `tirelire k = 10 + 5k`.
   - **Cas `n = 0`** : `tirelire 0 = 10 = 10 + 5 × 0` ✅
   - **Cas `n ≠ 0`** : ① `n − 1 < n` ② `n − 1 ≥ 0`. L'HI donne `tirelire (n-1) = 10 + 5(n − 1)`, donc
     `tirelire n = 10 + 5(n − 1) + 5 = 10 + 5n` ✅

   Ce qui achève la preuve par induction. ∎

---

## Exercice 8 ⭐⭐ — Pair ou impair

1. ```text
   pair 3 = not (pair 2) = not (not (pair 1)) = not (not (not (pair 0)))
          = not (not (not True)) = not (not False) = not True = False
   ```
2. **Pré** `n ≥ 0` · **Post** `pair n = True` ssi `n` est pair · **Variant** `n`.
   **HI** : pour tout `k < n` avec `k ≥ 0`, `pair k = True` ssi `k` est pair.
   - **Cas `n = 0`** : `pair 0 = True`, et 0 est pair ✅
   - **Cas `n ≠ 0`** : ① `n − 1 < n` ② `n − 1 ≥ 0`. Alors :

     ```text
     pair n = True  ⇔  pair (n-1) = False     (car pair n = not (pair (n-1)))
                    ⇔  n − 1 est impair       (HI)
                    ⇔  n est pair             ✅
     ```

   Ce qui achève la preuve par induction. ∎

---

## Exercice 9 ⭐⭐ — Trouve l'erreur

1. La phrase fausse : **« Le variant baisse car `a − b < a` »**. C'est vrai seulement si `b > 0`. Avec `b = 0` : `a − 0 = a`, le variant **ne baisse pas**. Avec `b = −2` : `a − (−2) = a + 2`, il **augmente**.
2. `division 7 0 = incr1 (division 7 0) = incr1 (incr1 (division 7 0)) = …` : le programme **ne s'arrête jamais** (en pratique, il plante quand la mémoire est pleine).
3. Il faut ajouter **`b > 0`**.

> 💡 **Leçon :** chaque justification doit **citer** l'hypothèse utilisée (« car `b > 0` par Pre2 »). C'est en cherchant cette hypothèse qu'on voit qu'elle manque.

---

## Exercice 10 ⭐⭐⭐ — Le reste

1. `reste 17 5 = reste 12 5 = reste 7 5 = reste 2 5 = 2` (17 parts pour 5 personnes : 3 chacune, il en reste 2).

2. | | |
   |---|---|
   | **Pre1, Pre2** | `a ≥ 0`, `b > 0` |
   | **Post1** | `0 ≤ r < b` |
   | **Post2** | `a − r` est un multiple de `b` |
   | **Variant** | `a` |

   **HI** : pour tous `a' < a` et `b'` avec `a' ≥ 0`, `b' > 0`, en posant `r' = reste a' b'` : `0 ≤ r' < b'` et `a' − r'` est un multiple de `b'`.

   **Cas `a < b`** : `r = a`.
   - Post1 : `0 ≤ a` (Pre1) et `a < b` (cas) ✅
   - Post2 : `a − a = 0 = 0 × b` ✅

   **Cas `a ≥ b`** : `r = reste (a-b) b`.
   - ① variant : `a − b < a` car `b > 0` (Pre2) ✅
   - ② pré : `a − b ≥ 0` (cas) et `b > 0` (Pre2) ✅
   - L'HI donne : `0 ≤ r < b` et `(a − b) − r = m × b` pour un certain entier `m`.
   - Post1 : c'est directement l'HI ✅
   - Post2 : `a − r = (a − b) − r + b = m × b + b = (m + 1) × b` ✅

   Ce qui achève la preuve par induction. ∎

---

## Exercice 11 ⭐⭐⭐ — Le PGCD

1. ```text
   pgcd 12 18 = pgcd 12 6      (12 < 18 : b devient 18 − 12)
              = pgcd 6 6       (12 > 6 : a devient 12 − 6)
              = 6              (a == b)
   ```
   Des carreaux de **6 m** de côté.

2. Dans le cas `a < b`, c'est `b` qui change et **`a` reste le même** : `a` ne baisse pas. Dans le cas `a > b`, c'est `b` qui ne bouge pas. Il faut une mesure qui baisse **dans les deux cas** : **`a + b`**.
   - cas `a > b` : `(a − b) + b = a < a + b` car `b > 0` ✅
   - cas `a < b` : `a + (b − a) = b < a + b` car `a > 0` ✅

3. **Pré** `a > 0`, `b > 0` · **Post** `pgcd a b` divise `a` et `b` · **Variant** `a + b`.
   **HI** : pour tous `a', b' > 0` avec `a' + b' < a + b`, `pgcd a' b'` divise `a'` et `b'`.

   | Cas | Raisonnement |
   |---|---|
   | `a == b` | le résultat `a` divise `a`, et divise `b` puisque `b = a` ✅ |
   | `a > b` | ② pré : `a − b > 0` et `b > 0`. L'HI dit que `d = pgcd (a-b) b` divise `a − b` et `b`. Donc `d` divise leur somme `(a − b) + b = a` ✅ |
   | `a < b` | ② pré : `a > 0` et `b − a > 0`. `d = pgcd a (b-a)` divise `a` et `b − a`, donc aussi `(b − a) + a = b` ✅ |

   Ce qui achève la preuve par induction. ∎

---

## Exercice 12 ⭐⭐⭐ — Le nombre de chiffres

1. ```text
   nbChiffres 2026 = 1 + nbChiffres 202 = 1 + 1 + nbChiffres 20
                   = 1 + 1 + 1 + nbChiffres 2 = 1 + 1 + 1 + 1 = 4
   ```

2. **Variant `n`.** On n'appelle que si `n ≥ 10`. Alors ``n `div` 10 ≤ n / 10 < n`` : le variant baisse. Et ``n `div` 10 ≥ 0`` : la pré-condition reste vraie.

3. **Pré** `n ≥ 0` · **Post** `n < 10^(nbChiffres n)` · **Variant** `n`.
   **HI** : pour tout `m < n` avec `m ≥ 0`, `m < 10^(nbChiffres m)`.

   - **Cas `n < 10`** : `nbChiffres n = 1` et `n < 10 = 10¹` ✅
   - **Cas `n ≥ 10`** : posons ``m = n `div` 10`` et `c = nbChiffres m`. Alors `nbChiffres n = 1 + c`.
     - ① `m < n` ② `m ≥ 0` (question 2). L'HI donne `m < 10ᶜ`, donc `m ≤ 10ᶜ − 1`.
     - ``n = 10 × m + (n `mod` 10) ≤ 10 × (10ᶜ − 1) + 9 = 10ᶜ⁺¹ − 1 < 10ᶜ⁺¹`` ✅

   Ce qui achève la preuve par induction. ∎
