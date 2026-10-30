# TD5 — Programmes impératifs

[⬅ TD / TP](../README.md) · Cours : [C5 Programmes impératifs](../../01-Cours/C5-Programmes-imperatifs/README.md) · [Mes réponses](mes-reponses.md) · [Code](code/td5.py)

## 🎯 Objectifs

- Calculer une **plus faible pré-condition** (WP) à travers affectations et `if`.
- Prouver une boucle avec les **4 obligations** : variant, invariant, avant, après.

| Règle | WP de `P` |
|---|---|
| `x = e` | `P` avec `x` remplacé par `e` |
| `if e: c1 else: c2` | `(e et WP(c1, P)) ou (non e et WP(c2, P))` |
| séquence | de **bas en haut** |

---

## Exercice 1 : Plus faible pré-condition

**Q1.1** — Post-condition : `a = 0 ∧ b ≠ 0`.

```python
a = a + 1
if a + b == 0:
    a = b
else:
    b = a
```

**Q1.2** — Post-condition : `a % (b + c) = 0`.

```python
a = b * c
if a != 0:
    b = c * b / a
    c = c + 1
else:
    a = (a + 1) / c
    b = b * b
c = a * b
```

<details><summary>💡 Piste Q1.1</summary>

Calcule d'abord la WP de chaque branche séparément. Le résultat peut surprendre : demande-toi ce qu'il signifie sur le programme.

</details>

<details><summary>💡 Piste Q1.2</summary>

Remonte d'abord `c = a * b` : la post-condition devient `a % (b + a*b) = 0`. Puis traite chaque branche **de bas en haut**. (Bonus C6 : quelles divisions peuvent échouer ?)

</details>

Vérifie tes réponses avec `verifie_wp` dans [code/td5.py](code/td5.py).

---

## Exercice 2 : Division euclidienne

```python
q = 0
r = a
while r >= b:
    q = q + 1
    r = r - b
res = (q, r)
```

| | |
|---|---|
| **Pré** | `a ≥ 0` et `b > 0` |
| **Post** | avec `(q', r') = res` : `a = q' × b + r'` et `0 ≤ r' < b` |
| **Variant** | `r` |
| **Invariant** | `a = q × b + r`, `r ≥ 0` et `b > 0` |

| Q | Obligation | Ce qu'on fait |
|---|---|---|
| 2.1 | Variant | WP de `r = p` à travers le corps ⇒ il décroît ; montrer qu'il est ≥ 0 |
| 2.2 | Invariant | WP de l'invariant à travers le corps ; la montrer avec invariant + condition |
| 2.3 | Avant | WP de l'invariant à travers `q = 0 ; r = a` ; la montrer avec la pré |
| 2.4 | Après | WP de la post à travers `res = (q, r)` ; la montrer avec invariant + **non** condition |

<details><summary>💡 Piste Q2.1</summary>

`WP(r = r - b, r = p)` = `r − b = p`, donc au début `r = p + b > p` car `b > 0` (invariant).

</details>

---

## Exercice 3 : Nombre de diviseurs

```python
i = 2
res = 2
while i * i < n:
    if n % i == 0:
        res = res + 2
    i = i + 1
if i * i == n:
    res = res + 1
```

Idée : les diviseurs vont **par paires** `(a, b)` avec `a × b = n`, et l'un des deux a un carré `≤ n`. On ne parcourt que les **petits** diviseurs, chacun compte pour 2.

| | |
|---|---|
| **Pré** | `n > 1` |
| **Post** | `res` = nombre de diviseurs de `n` |
| **Variant** | `n − i` |
| **Invariant** | `res = div(n, i)` avec `div(n, i) = \|{k \| k divise n et (1 ≤ k < i ou n//i < k ≤ n)}\|` |

| Q | Obligation |
|---|---|
| 3.1 | Variant : WP de `i = p`, décroissance, positivité |
| 3.2 | Invariant : WP à travers le corps, puis preuve |
| 3.3 | Avant : WP à travers `i = 2 ; res = 2` |
| 3.4 | Après : WP de la post à travers le `if` final |

<details><summary>💡 Piste Q3.3</summary>

`div(n, 2)` compte les diviseurs dans `[1, 1]` et dans `]n//2, n]` : ce sont `1` et `n` (aucun diviseur strictement entre `n/2` et `n`).

</details>

---

## ✅ Avant de rendre

- [ ] Toutes les WP sont calculées **de bas en haut**, avec les commentaires `#` entre chaque ligne.
- [ ] Chaque obligation dit **quelles hypothèses** sont utilisées (invariant, condition, non condition, pré).
- [ ] `python3 code/td5.py` confirme mes WP.
