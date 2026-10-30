# Chapitre 5 — Exemples corrigés

[⬅ Cours du chapitre 5](1-Cours.md) · [🏠 Accueil](../../00-Commencer-ici.md) · Méthode : [F4](../../04-Fiches-revision/F4-Methode-boucles.md)

> 🏋️ Chaque preuve suit les **4 vérifications** : ① départ, ② un tour, ③ terminaison, ④ arrivée.

---

## Exemple 1 ⭐⭐ — La factorielle

```python
i = 1
res = 1
while i <= n:
    res = res * i
    i = i + 1
```

**Pour comprendre, avec `n = 4` :**

| Moment | `i` | `res` | `(i − 1)!` |
|---|---|---|---|
| départ | 1 | 1 | `0! = 1` |
| après 1 tour | 2 | 1 | `1! = 1` |
| après 2 tours | 3 | 2 | `2! = 2` |
| après 3 tours | 4 | 6 | `3! = 6` |
| après 4 tours | 5 | 24 | `4! = 24` → stop car `5 > 4` |

On voit que `res = (i − 1)!` à chaque ligne : c'est l'**invariant**.

| | |
|---|---|
| **Pré** | `n ≥ 0` |
| **Post** | `res = n!` |
| **Invariant** | (I1) `res = (i−1)!` et (I2) `n − i + 1 ≥ 0` (c'est-à-dire `i ≤ n + 1`, la borne) |
| **Condition** | (CB) `i ≤ n` |
| **Variant** | `n − i + 1` (le nombre de tours restants) |

### ③ Le variant diminue

```python
# n = a et i = b - 1
res = res * i
# n = a et i + 1 = b
i = i + 1
# n = a et i = b
```

> 💬 En remontant : si `i = b` à la fin du tour, alors `i = b − 1` au début. `i` augmente de 1, donc `n − i + 1` **diminue** de 1. Il est ≥ 0 grâce à (I2).

### ② L'invariant reste vrai pendant un tour

```python
# res * i = i!  et  n - i ≥ 0         ← ce qu'il faut au début du tour
res = res * i
# res = i!  et  n - i ≥ 0
i = i + 1
# res = (i-1)!  et  n - i + 1 ≥ 0     ← l'invariant à la fin du tour
```

Je sais (I1), (I2) et (CB). Je dois montrer :
- `res × i = i!` : par (I1), `res × i = (i−1)! × i = i!` ✅
- `n − i ≥ 0` : par (CB), `i ≤ n` ✅

### ① Au départ

```python
# 1 = (1-1)!  et  n - 1 + 1 ≥ 0      c'est-à-dire : n ≥ 0
i = 1
# 1 = (i-1)!  et  n - i + 1 ≥ 0
res = 1
# res = (i-1)!  et  n - i + 1 ≥ 0
```

On obtient `n ≥ 0` : c'est **exactement** la pré-condition ✅

### ④ À l'arrivée

À la sortie, (CB) est **fausse** : `i > n`. Avec (I2) : `i ≤ n + 1`. Donc **`i = n + 1`**.
Par (I1) : `res = (n + 1 − 1)! = n!` ✅

---

## Exemple 2 ⭐⭐⭐ — L'exponentiation rapide

> 💡 **L'idée :** pour calculer `3¹³`, au lieu de faire 12 multiplications, on **élève au carré** : `3, 3², 3⁴, 3⁸`, et on ne garde que ce qu'il faut.
> `13 = 8 + 4 + 1`, donc `3¹³ = 3⁸ × 3⁴ × 3¹`. Résultat : **6 multiplications** au lieu de 12. Pour `n = 1 000 000`, il en faut moins de 40 au lieu d'un million.

```python
res = a
rem = 1
i = n
while 1 < i:
    if i % 2 == 1:        # i impair : on met un « res » de côté dans rem
        rem = rem * res
    res = res * res       # on élève au carré
    i = i // 2            # on divise l'exposant par 2
res = res * rem
```

**Avec `a = 3`, `n = 13` :**

| Moment | `i` | `res` | `rem` | `rem × resⁱ` |
|---|---|---|---|---|
| départ | 13 | 3 | 1 | `3¹³` |
| tour 1 (13 impair) | 6 | `3²` | `3` | `3 × (3²)⁶ = 3¹³` |
| tour 2 (6 pair) | 3 | `3⁴` | `3` | `3 × (3⁴)³ = 3¹³` |
| tour 3 (3 impair) | 1 | `3⁸` | `3⁵` | `3⁵ × 3⁸ = 3¹³` → stop |
| fin : `res = res * rem` | | `3¹³` | | |

`rem × resⁱ` vaut **toujours** `3¹³` : c'est l'invariant.

| | |
|---|---|
| **Pré** | `n > 0` |
| **Post** | `res = aⁿ` |
| **Invariant** | (I1) `rem × resⁱ = aⁿ` et (I2) `i > 0` |
| **Condition** | (CB) `i > 1` |
| **Variant** | `i` |

### ③ Le variant diminue

`i` devient `i // 2`. Comme `i ≥ 2` (CB), `i // 2 < i` ✅. Et `i > 0` par (I2) ✅

### ② L'invariant reste vrai pendant un tour

```python
# (i impair et rem*res*(res*res)^(i//2) = a^n et i//2 > 0)
#   ou (i pair et rem*(res*res)^(i//2) = a^n et i//2 > 0)
if i % 2 == 1:
    # rem * res * (res*res)^(i//2) = a^n  et  i//2 > 0
    rem = rem * res
    # rem * (res*res)^(i//2) = a^n  et  i//2 > 0
res = res * res
# rem * res^(i//2) = a^n  et  i//2 > 0
i = i // 2
# rem * res^i = a^n  et  i > 0
```

- `i // 2 > 0` : (CB) donne `i ≥ 2`, donc `i // 2 ≥ 1` ✅
- **`i` impair** (par exemple `i = 13 = 2 × 6 + 1`) : `res × (res²)^(i//2) = res^(2 × (i//2) + 1) = resⁱ`. Avec (I1), on obtient `aⁿ` ✅
- **`i` pair** (par exemple `i = 6 = 2 × 3`) : `(res²)^(i//2) = resⁱ`. Avec (I1), on obtient `aⁿ` ✅

### ① Au départ

Avec `res = a`, `rem = 1`, `i = n`, il faut `1 × aⁿ = aⁿ` (toujours vrai) et `n > 0` (la pré-condition) ✅

### ④ À l'arrivée

```python
# rem * res = a^n
res = res * rem
# res = a^n
```

À la sortie, `i ≤ 1` (condition fausse) et `i > 0` (I2), donc `i = 1`. Par (I1), `rem × res¹ = aⁿ` ✅
