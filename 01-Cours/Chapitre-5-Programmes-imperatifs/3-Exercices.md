# Chapitre 5 — Exercices

[🏠 Accueil](../../README.md) · [⬅ Cours](1-Cours.md) · [Exemples corrigés](2-Exemples-corriges.md) · **Corrections : [4-Corrections.md](4-Corrections.md)**

> ⭐ = échauffement · ⭐⭐ = entraînement · ⭐⭐⭐ = niveau DS
> Rappel : la plus faible pré-condition (WP) se calcule **de bas en haut**, en écrivant un commentaire `#` au-dessus de chaque ligne.

---

## Exercice 1 ⭐ — Une seule ligne

Calcule la plus faible pré-condition :

| Code | Post-condition |
|---|---|
| `x = x + 5` | `x > 12` |
| `y = 2 * y` | `y ≥ 10` |
| `prix = prix * 0.8` (soldes : −20 %) 🏷️ | `prix ≤ 40` |
| `x = 3` | `x > 0` |

---

## Exercice 2 ⭐ — Échanger sans verre vide 🥤

> Pour échanger le contenu de deux verres, on utilise d'habitude un troisième verre. Avec des nombres, on peut s'en passer :

```python
a = a + b
b = a - b
a = a - b
```

Calcule la WP de la post-condition `a = 7 et b = 3`. Qu'en conclus-tu sur ce que fait ce code ?

---

## Exercice 3 ⭐ — La valeur absolue

```python
if x < 0:
    x = -x
```

Calcule la WP de `x ≥ 0`. (Un `if` sans `else` revient à `else: pass`.) Que peux-tu en conclure ?

---

## Exercice 4 ⭐⭐ — Le cinéma 🎬

```python
if age < 18:
    prix = 6
else:
    prix = 10
```

1. Calcule la WP de `prix ≤ budget`.
2. Avec `budget = 8`, qui peut aller au cinéma ?

---

## Exercice 5 ⭐⭐ — Les soldes 🛍️

```python
prix = prix - remise
if prix < 0:
    prix = 0
```

Calcule la WP de `prix ≤ 30`, puis simplifie-la.

---

## Exercice 6 ⭐⭐ — Observer pour trouver l'invariant 🔍

```python
s = 0
i = 0
while i < n:
    i = i + 1
    s = s + 2 * i - 1
```

1. Avec `n = 4`, remplis un tableau `i`, `s` après chaque tour.
2. Quelle relation entre `s` et `i` reste vraie à chaque ligne ? Propose un invariant complet (avec une borne).
3. Que vaut `s` à la fin ?

---

## Exercice 7 ⭐⭐ — Trouver le variant

Pour chaque boucle, donne un variant, ou une pré-condition qui la fait terminer.

```python
a) while i < n:          b) while j > 0:          c) while x > 1:
       i = i + 1                j = j - 1                x = x // 2

d) while g <= d:                         e) while x != 0:
       if t[g] % 2 == 0:                        x = x - 2
           g = g + 1
       else:
           d = d - 1
```

---

## Exercice 8 ⭐⭐ — L'épargne mensuelle 💶

> Chaque mois, on met 50 € de côté.

```python
argent = 0
mois = 0
while mois < n:
    argent = argent + 50
    mois = mois + 1
```

**Pré** `n ≥ 0` · **Post** `argent = 50 × n`.
Propose un invariant et un variant, puis fais les **4 vérifications** (départ, un tour, terminaison, arrivée).

---

## Exercice 9 ⭐⭐⭐ — La somme 1 + 2 + … + n

```python
s = 0
i = 0
while i < n:
    i = i + 1
    s = s + i
```

**Pré** `n ≥ 0` · **Post** `s = n(n + 1) / 2`.
Fais la preuve complète, avec les calculs de WP en commentaires.

---

## Exercice 10 ⭐⭐⭐ — La puissance, version lente

```python
res = 1
i = 0
while i < n:
    res = res * a
    i = i + 1
```

**Pré** `n ≥ 0` · **Post** `res = aⁿ`. Fais la preuve complète.

---

## Exercice 11 ⭐⭐⭐ — L'invariant trop faible 🕵️

On reprend la factorielle du cours :

```python
i = 1
res = 1
while i <= n:
    res = res * i
    i = i + 1
```

Un étudiant propose l'invariant **`res = (i − 1)!`** seulement.

1. Montre que cet invariant est vrai au départ et qu'il reste vrai après un tour.
2. Montre qu'à l'arrivée, on **ne peut pas** conclure `res = n!`. Que sait-on sur `i` ?
3. Que faut-il ajouter à l'invariant ? Vérifie que l'ajout reste vrai après un tour.

---

## Exercice 12 ⭐⭐⭐ — La somme des chiffres, version boucle

```python
s = 0
m = n
while m > 0:
    s = s + m % 10
    m = m // 10
```

On note `sc(m)` la somme des chiffres de `m`, avec `sc(0) = 0` et, pour `m > 0`, `sc(m) = m % 10 + sc(m // 10)`.

**Pré** `n ≥ 0` · **Post** `s = sc(n)`.

1. Propose un invariant en pensant « déjà additionné + reste à additionner = total ».
2. Fais la preuve complète.
