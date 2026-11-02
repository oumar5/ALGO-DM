# Chapitre 6 — Exercices

[🏠 Accueil](../../README.md) · [⬅ Cours](1-Cours.md) · [Exemples corrigés](2-Exemples-corriges.md) · **Corrections : [4-Corrections.md](4-Corrections.md)**

> ⭐ = échauffement · ⭐⭐ = entraînement · ⭐⭐⭐ = niveau DS
> Pour les boucles, utilise les **6 étapes** : ① le corps ne plante pas · ② le variant diminue · ③ la condition ne plante pas · ④ l'invariant reste vrai · ⑤ départ · ⑥ arrivée.

---

## Exercice 1 ⭐ — Ça plante ou pas ? 💥

Pour chaque expression, donne la condition pour qu'elle **ne plante pas** (on met de côté les indices négatifs de Python).

| | Expression |
|---|---|
| a | `a / (b - c)` |
| b | `l[i + 1]` |
| c | `sqrt(x - 4)` |
| d | `x != 0 and 10 / x > 1` |
| e | `l[i] > 0 and i < len(l)` |
| f | `i < len(l) and l[i] > 0` |

Pourquoi `e` et `f` n'ont-elles pas la même réponse ?

---

## Exercice 2 ⭐ — Remplacer des œufs 🥚

`l = [4, 9, 2, 7]`. Écris les tableaux suivants, puis dis lesquels ont **le même sac** (`val`) que `l`.

1. `l[1 → 0]`
2. `l[0 → 7, 3 → 4]`
3. `l[2 → l[0]]`

---

## Exercice 3 ⭐ — Écrire dans une case

Calcule la plus faible pré-condition de `l[0] > 5` à travers :

```python
l[0] = l[0] + 1
```

N'oublie pas la condition pour ne pas planter.

---

## Exercice 4 ⭐⭐ — Échanger deux œufs

```python
v = l[i]
l[i] = l[j]
l[j] = v
```

Calcule la WP de `l[i] ≤ l[j]`. Traduis le résultat en français. (Attention au cas `i = j`.)

---

## Exercice 5 ⭐⭐ — Le total des dépenses 🧾

```python
s = 0
i = 0
while i < len(t):
    s = s + t[i]
    i = i + 1
```

**Pré** aucune · **Post** `s = t[0] + t[1] + … + t[len(t) − 1]`.

Propose un invariant et un variant, puis fais les 6 étapes.

---

## Exercice 6 ⭐⭐ — Combien d'admis ? 🎓

```python
c = 0
i = 0
while i < len(t):
    if t[i] >= 10:
        c = c + 1
    i = i + 1
```

**Post** `c` = le nombre de cases `k` telles que `t[k] ≥ 10`.

1. Exécute le code avec `t = [12, 8, 15, 9]`.
2. Propose un invariant et fais les étapes ④, ⑤ et ⑥.

---

## Exercice 7 ⭐⭐ — Chercher un nom dans une liste 🔎

```python
i = 0
while i < len(t) and t[i] != v:
    i = i + 1
```

**Post** : soit `i < len(t)` et `t[i] = v` ; soit `i = len(t)` et `v` n'est **pas** dans `t`.

1. Exécute avec `t = [4, 7, 2, 9]` et `v = 2`, puis avec `v = 5`.
2. Pourquoi la condition ne plante-t-elle jamais, même quand `i = len(t)` ?
3. Propose un invariant et fais les 6 étapes.

---

## Exercice 8 ⭐⭐⭐ — La température maximale 🌡️

```python
m = t[0]
i = 1
while i < len(t):
    if t[i] > m:
        m = t[i]
    i = i + 1
```

**Pré** `len(t) > 0` · **Post** `m` est une valeur de `t`, et `t[k] ≤ m` pour tout `k`.

1. Exécute avec `t = [12, 17, 9, 17, 14]`.
2. Fais les 6 étapes.

---

## Exercice 9 ⭐⭐⭐ — Retourner une étagère 📚

```python
g = 0
d = len(t) - 1
while g < d:
    v = t[g]
    t[g] = t[d]
    t[d] = v
    g = g + 1
    d = d - 1
```

On note `t0` le tableau de départ et `n = len(t)`.
**Post** : pour tout `k`, `t[k] = t0[n − 1 − k]` (le tableau est retourné).

1. Exécute avec `t = [1, 2, 3, 4, 5]`, puis avec `t = [1, 2, 3, 4]`.
2. Complète cet invariant :
   - (I1) `g ≥ 0` et `g + d = n − 1`
   - (I2) pour tout `k < g` ou `k > d` : `t[k] = …`
   - (I3) pour tout `g ≤ k ≤ d` : `t[k] = …`
3. Fais les 6 étapes.

---

## Exercice 10 ⭐⭐⭐ — Le tableau est-il rangé ?

```python
ok = True
i = 1
while i < len(t) and ok:
    if t[i - 1] > t[i]:
        ok = False
    i = i + 1
```

**Pré** `len(t) ≥ 1` · **Post** `ok = True` **si et seulement si** `t` est trié.

1. Exécute avec `t = [1, 3, 2, 5]`. Combien de tours ?
2. Propose un invariant et fais les étapes ④, ⑤ et ⑥.
