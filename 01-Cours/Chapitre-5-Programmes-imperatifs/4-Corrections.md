# Chapitre 5 — Corrections

[🏠 Accueil](../../README.md) · [⬅ Exercices](3-Exercices.md) · [Cours](1-Cours.md)

> ⚠️ As-tu cherché au moins 10 minutes ?

---

## Exercice 1 ⭐ — Une seule ligne

On **remplace** la variable par l'expression dans la post-condition :

| Code | Post | Remplacement | WP simplifiée |
|---|---|---|---|
| `x = x + 5` | `x > 12` | `x + 5 > 12` | `x > 7` |
| `y = 2 * y` | `y ≥ 10` | `2y ≥ 10` | `y ≥ 5` |
| `prix = prix * 0.8` | `prix ≤ 40` | `0,8 × prix ≤ 40` | `prix ≤ 50` |
| `x = 3` | `x > 0` | `3 > 0` | **toujours vrai** |

> 🏷️ Un article à 50 € soldé à −20 % coûte 40 € : il faut un prix de départ ≤ 50 €.

---

## Exercice 2 ⭐ — Échanger sans verre vide

```python
# b = 7  et  a = 3                  ③ remplacer a par a + b : b = 7 et (a + b) − b = 3
a = a + b
# b = 7  et  a − b = 3              ② remplacer b par a − b : a − (a − b) = 7 et a − b = 3
b = a - b
# a − b = 7  et  b = 3              ① remplacer a par a − b
a = a - b
# a = 7  et  b = 3
```

Pour finir avec `a = 7, b = 3`, il faut **commencer** avec `a = 3, b = 7` : le code **échange** `a` et `b`.

---

## Exercice 3 ⭐ — La valeur absolue

```python
# (x < 0 et −x ≥ 0)  ou  (x ≥ 0 et x ≥ 0)      ⇔  toujours vrai
if x < 0:
    # −x ≥ 0
    x = -x
    # x ≥ 0
# (sinon : pass, la condition ne change pas : x ≥ 0)
# x ≥ 0
```

- `x < 0` et `−x ≥ 0` : vrai dès que `x < 0` ;
- `x ≥ 0` et `x ≥ 0` : vrai dès que `x ≥ 0`.

La WP est **toujours vraie** : quelle que soit la valeur de départ, `x ≥ 0` à la fin. Le code calcule bien une valeur absolue.

---

## Exercice 4 ⭐⭐ — Le cinéma

1. ```python
   # (age < 18 et 6 ≤ budget)  ou  (age ≥ 18 et 10 ≤ budget)
   if age < 18:
       # 6 ≤ budget
       prix = 6
   else:
       # 10 ≤ budget
       prix = 10
   # prix ≤ budget
   ```

2. Avec `budget = 8` : `6 ≤ 8` est vrai, `10 ≤ 8` est faux. La WP devient `age < 18` : **seuls les mineurs** peuvent y aller.

---

## Exercice 5 ⭐⭐ — Les soldes

```python
# prix − remise ≤ 30                      ② remplacer prix par prix − remise
prix = prix - remise
# (prix < 0 et 0 ≤ 30)  ou  (prix ≥ 0 et prix ≤ 30)
#   ⇔  prix < 0  ou  0 ≤ prix ≤ 30
#   ⇔  prix ≤ 30                          ① les deux branches du if
if prix < 0:
    # 0 ≤ 30
    prix = 0
# prix ≤ 30
```

WP : **`prix ≤ 30 + remise`**. Par exemple, avec une remise de 15 €, tout article jusqu'à 45 € finit à 30 € ou moins.

---

## Exercice 6 ⭐⭐ — Observer

1. | Après | `i` | `s` |
   |---|---|---|
   | départ | 0 | 0 |
   | tour 1 | 1 | 1 |
   | tour 2 | 2 | 4 |
   | tour 3 | 3 | 9 |
   | tour 4 | 4 | 16 |

2. On voit **`s = i²`** à chaque ligne. Invariant : **`s = i²` et `i ≤ n`** (la borne sert à la sortie).
3. À la fin, `i ≥ n` (condition fausse) et `i ≤ n` (borne), donc `i = n` et **`s = n²`**. (C'est la somme des impairs `1 + 3 + 5 + 7` du carrelage, chapitre 1.)

---

## Exercice 7 ⭐⭐ — Les variants

| Boucle | Variant | Pourquoi |
|---|---|---|
| a) | `n − i` | `i` augmente de 1 ; sous la condition, `n − i > 0` |
| b) | `j` | `j` baisse de 1 ; sous la condition, `j > 0` |
| c) | `x` | `x // 2 < x` dès que `x ≥ 1` ; sous la condition, `x > 1` |
| d) | `d − g + 1` | à chaque tour, soit `g` monte, soit `d` descend ; sous la condition, `d − g + 1 ≥ 1` |
| e) | `x`, avec la **pré-condition** `x ≥ 0` et `x` pair | si `x` est impair ou négatif, `x` ne vaut jamais 0 : boucle infinie |

---

## Exercice 8 ⭐⭐ — L'épargne mensuelle

| | |
|---|---|
| **Invariant** | (I1) `argent = 50 × mois` et (I2) `mois ≤ n` |
| **Variant** | `n − mois` (les mois restants) |

**① Départ**

```python
# 0 = 50 × 0  et  0 ≤ n       ⇔  n ≥ 0   (la pré-condition) ✅
argent = 0
mois = 0
```

**② Un tour** (hypothèses : I1, I2, condition `mois < n`)

```python
# argent + 50 = 50 × (mois + 1)  et  mois + 1 ≤ n
argent = argent + 50
# argent = 50 × (mois + 1)  et  mois + 1 ≤ n
mois = mois + 1
# argent = 50 × mois  et  mois ≤ n
```

- `argent + 50 = 50 × mois + 50 = 50 × (mois + 1)` par I1 ✅
- `mois + 1 ≤ n` car `mois < n` ✅

**③ Terminaison** : `mois` augmente de 1, donc `n − mois` baisse de 1 ; il est ≥ 0 par I2 ✅

**④ Arrivée** : `mois ≥ n` (condition fausse) et `mois ≤ n` (I2) ⇒ `mois = n`. Par I1, `argent = 50 × n` ✅

---

## Exercice 9 ⭐⭐⭐ — La somme 1 + … + n

| | |
|---|---|
| **Invariant** | (I1) `s = i(i + 1) / 2` et (I2) `i ≤ n` |
| **Condition** | (CB) `i < n` |
| **Variant** | `n − i` |

**① Départ**

```python
# 0 = 0 × 1 / 2  et  0 ≤ n    ⇔  n ≥ 0   ✅ (pré-condition)
s = 0
i = 0
```

**② Un tour**

```python
# s + i + 1 = (i + 1)(i + 2) / 2  et  i + 1 ≤ n
i = i + 1
# s + i = i(i + 1) / 2  et  i ≤ n
s = s + i
# s = i(i + 1) / 2  et  i ≤ n
```

Avec I1 et CB :
- `s + i + 1 = i(i + 1)/2 + (i + 1) = (i + 1)(i + 2)/2` ✅
- `i + 1 ≤ n` car `i < n` ✅

**③ Terminaison** : `i` augmente de 1, `n − i` baisse ; ≥ 0 par I2 ✅

**④ Arrivée** : `i ≥ n` et `i ≤ n` ⇒ `i = n`, donc `s = n(n + 1)/2` ✅

---

## Exercice 10 ⭐⭐⭐ — La puissance

| | |
|---|---|
| **Invariant** | (I1) `res = aⁱ` et (I2) `i ≤ n` |
| **Variant** | `n − i` |

**① Départ** : `1 = a⁰` (vrai) et `0 ≤ n` (pré-condition) ✅

**② Un tour**

```python
# res × a = a^(i+1)  et  i + 1 ≤ n
res = res * a
# res = a^(i+1)  et  i + 1 ≤ n
i = i + 1
# res = a^i  et  i ≤ n
```

Par I1, `res × a = aⁱ × a = aⁱ⁺¹` ✅ ; par la condition `i < n`, `i + 1 ≤ n` ✅

**③ Terminaison** : `n − i` baisse de 1, ≥ 0 par I2 ✅

**④ Arrivée** : `i = n` (condition fausse + I2), donc `res = aⁿ` ✅

---

## Exercice 11 ⭐⭐⭐ — L'invariant trop faible

1. - **Départ** : `res = 1 = 0! = (1 − 1)!` ✅
   - **Un tour** : la WP de `res = (i − 1)!` à travers le corps est `res × i = i!`, vraie car `res = (i − 1)!` ✅

2. À l'arrivée, on sait seulement `res = (i − 1)!` et `i > n` (condition fausse). Mais `i` pourrait valoir `n + 1`, `n + 5`, `n + 100`… : **rien** ne dit que `i = n + 1`. On ne peut donc pas conclure `res = n!`.

3. On ajoute la **borne** **`i ≤ n + 1`** (dans le cours : `n − i + 1 ≥ 0`).
   - Départ : `1 ≤ n + 1` ⇔ `n ≥ 0` (pré-condition) ✅
   - Un tour : la WP de `i ≤ n + 1` est `i + 1 ≤ n + 1`, c'est-à-dire `i ≤ n` : c'est la condition de boucle ✅
   - Arrivée : `i > n` et `i ≤ n + 1` ⇒ `i = n + 1` ⇒ `res = n!` ✅

> 💡 **Leçon :** l'invariant n'est pas seulement « ce qui reste vrai ». Il doit être **assez précis** pour conclure à la sortie.

---

## Exercice 12 ⭐⭐⭐ — La somme des chiffres

1. **Invariant** : (I1) `s + sc(m) = sc(n)` (« déjà additionné + reste à additionner = total ») et (I2) `m ≥ 0`. **Variant** : `m`.

2. **① Départ**

   ```python
   # 0 + sc(n) = sc(n)  et  n ≥ 0      ✅ (la pré-condition)
   s = 0
   m = n
   ```

   **② Un tour** (hypothèses : I1, I2, `m > 0`)

   ```python
   # s + m % 10 + sc(m // 10) = sc(n)  et  m // 10 ≥ 0
   s = s + m % 10
   # s + sc(m // 10) = sc(n)  et  m // 10 ≥ 0
   m = m // 10
   # s + sc(m) = sc(n)  et  m ≥ 0
   ```

   Comme `m > 0`, `sc(m) = m % 10 + sc(m // 10)`. La première ligne vaut donc `s + sc(m) = sc(n)`, vrai par I1 ✅. Et `m // 10 ≥ 0` car `m > 0` ✅

   **③ Terminaison** : `m // 10 < m` quand `m > 0`, et `m ≥ 0` par I2 ✅

   **④ Arrivée** : `m ≤ 0` (condition fausse) et `m ≥ 0` ⇒ `m = 0`. Par I1 : `s + sc(0) = s + 0 = sc(n)` ✅

> 🔁 Compare avec l'exercice 9 du chapitre 3 : c'est **la même preuve**. La version récursive terminale et la boucle `while` sont deux écritures du même calcul.
