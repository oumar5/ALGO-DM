# C5 — Démonstrations : factorielle et exponentiation rapide

[⬅ Cours C5](README.md) · Méthode : [F4](../../04-Fiches-revision/F4-Methode-boucles.md)

---

## 1. Factorielle

```python
i = 1
res = 1
while i <= n:
    res = res * i
    i = i + 1
```

| | |
|---|---|
| **Pré** | `n ≥ 0` |
| **Post** | `res = n!` |
| **Invariant** | (I1) `res = (i−1)!` et (I2) `n − i + 1 ≥ 0` |
| **Condition** | (CB) `i ≤ n` |
| **Variant** | `n − i + 1` |

### ③ Variant

```python
# n = a et i = b - 1
res = res * i
# n = a et i + 1 = b
i = i + 1
# n = a et i = b
```

Au début du tour, le variant vaut `a − (b−1) + 1 = a − b + 2` ; à la fin `a − b + 1`. Il **diminue strictement**. Il est **≥ 0** grâce à (I2).

### ② Conservation de l'invariant

```python
# res * i = i!  et  n - i ≥ 0
res = res * i
# res = i!  et  n - (i+1) + 1 ≥ 0
i = i + 1
# res = (i-1)!  et  n - i + 1 ≥ 0
```

Hypothèses : I1, I2, CB. À montrer :
- (P1) `res × i = i!` : par I1, `res × i = (i−1)! × i = i!`. ✅
- (P2) `n − i ≥ 0` : par CB, `i ≤ n`. ✅

### ① Avant la boucle

```python
# 1 = (1-1)!  et  n - 1 + 1 ≥ 0,   c'est-à-dire  n ≥ 0
i = 1
# 1 = (i-1)!  et  n - i + 1 ≥ 0
res = 1
# res = (i-1)!  et  n - i + 1 ≥ 0
```

La WP est `n ≥ 0` : c'est exactement la pré-condition. ✅

### ④ Après la boucle

À la sortie : non CB (`i > n`) et I2 (`i ≤ n + 1`) ⇒ `i = n + 1`. Par I1 : `res = (n+1−1)! = n!`. ✅

---

## 2. Exponentiation rapide

```python
res = a
rem = 1
i = n
while 1 < i:
    if i % 2 == 1:
        rem = rem * res
    res = res * res
    i = i // 2
res = res * rem
```

| | |
|---|---|
| **Pré** | `n > 0` |
| **Post** | `res = aⁿ` |
| **Invariant** | (I1) `rem × resⁱ = aⁿ` et (I2) `i > 0` |
| **Condition** | (CB) `i > 1` |
| **Variant** | `i` |

### ③ Variant

```python
# i // 2 = x     (dans les deux branches du if)
if i % 2 == 1:
    rem = rem * res
res = res * res
# i // 2 = x
i = i // 2
# i = x
```

Le variant passe de `i` à `i // 2`. Or `i ≥ 2 × (i // 2)` ; si `i // 2 > 0` alors `i ≥ 2 × (i//2) > i // 2` ; sinon `i // 2 = 0 < i` (car `i > 1`). Il **diminue strictement** et reste **≥ 0** (I2).

### ② Conservation de l'invariant

```python
# (i%2 == 1 et rem*res*(res*res)^(i//2) = a^n et i//2 > 0)
#   ou (i%2 != 1 et rem*(res*res)^(i//2) = a^n et i//2 > 0)
if i % 2 == 1:
    # rem * res * (res*res)^(i//2) = a^n  et  i//2 > 0
    rem = rem * res
    # rem * (res*res)^(i//2) = a^n  et  i//2 > 0
res = res * res
# rem * res^(i//2) = a^n  et  i//2 > 0
i = i // 2
# rem * res^i = a^n  et  i > 0
```

Hypothèses : I1, I2, CB.
- `i // 2 > 0` : CB donne `i ≥ 2`, donc `i // 2 ≥ 1`. ✅
- **Cas `i` impair** : `2 × (i//2) + 1 = i`, donc `res × (res²)^(i//2) = res^(2(i//2)+1) = resⁱ`, et `rem × resⁱ = aⁿ` par I1. ✅
- **Cas `i` pair** : `2 × (i//2) = i`, donc `(res²)^(i//2) = resⁱ` et `rem × resⁱ = aⁿ` par I1. ✅

### ① Avant la boucle

WP : `1 × aⁿ = aⁿ` (toujours vrai) et `n > 0` — c'est la pré-condition. ✅

### ④ Après la boucle

```python
# rem * res = a^n
res = res * rem
# res = a^n
```

À la sortie : non CB (`i ≤ 1`) et I2 (`i > 0`) ⇒ `i = 1`. Par I1 : `rem × res = aⁿ`. ✅
