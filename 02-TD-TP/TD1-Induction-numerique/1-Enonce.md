# TD1 — Induction et fonctions numériques

[⬅ TD / TP](../README.md) · Cours : [C1 Induction](../../01-Cours/C1-Induction/README.md) · [Mes réponses](mes-reponses.md) · [Code](code/td1.py)

## 🎯 Objectifs

- Exécuter pas à pas une fonction Haskell.
- Traduire une fonction en Python (récursif **et** itératif).
- Prouver une spécification par induction.

| Exercice | Fonction | Notion travaillée |
|---|---|---|
| 1 | `mult` | première preuve par induction |
| 2 | `exp`, `expR` | lemme intermédiaire + exponentiation rapide |
| 3 | `pgfpAux` | **trouver** soi-même pré-condition et variant |

---

## Exercice 1 : Multiplication

```haskell
mult :: Int -> Int -> Int
mult 0 m = 0
mult n m = m + mult (n-1) m
```

| Q | Ce qu'on demande |
|---|---|
| 1.1 | Exécuter pas à pas `mult 3 5`. |
| 1.2 | Deux versions Python : **récursive** et **itérative**. |
| 1.3 | Pré : `x ≥ 0`. Post : `mult x y = x * y`. Démontrer par induction sur `x`. |

<details><summary>💡 Piste Q1.3</summary>

Deux cas : `x = 0` et `x ≠ 0`. Pour l'appel `mult (x-1) y`, la pré-condition `x − 1 ≥ 0` vient de `x ≥ 0` **et** `x ≠ 0` (on est dans la 2ᵉ équation).

</details>

---

## Exercice 2 : Exponentiation rapide

```haskell
exp :: Int -> Int -> Int
exp a 0 = 1
exp a b = a * exp a (b-1)
```

| Q | Ce qu'on demande |
|---|---|
| 2.1 | Calculer pas à pas `exp 3 3`. |
| 2.2 | Deux versions Python de `exp` : récursive et itérative. |
| 2.3 | Montrer, pour `b1 ≥ 0` et `b2 ≥ 0` : `exp a (b1 + b2) = exp a b1 * exp a b2`, par induction sur `b1`. |

```haskell
expR :: Int -> Int -> Int
expR a 0 = 1
expR a b | b `mod` 2 == 0 = e * e
         | otherwise      = a * e * e
  where e = expR a (b `quot` 2)
```

> Rappel : pour `b ≥ 0`, ``b = 2 * (b `quot` 2) + b `mod` 2``.
> (L'énoncé original écrit `a = 2*(a quot b) + a mod b`, c'est une coquille.)

| Q | Ce qu'on demande |
|---|---|
| 2.4 | Calculer `expR 3 3`. |
| 2.5 | Version Python récursive de `expR`. |
| 2.6 | Pré : `b ≥ 0`. Post : `expR a b = exp a b`. Démontrer par induction sur `b`. |

<details><summary>💡 Piste Q2.3</summary>

Cas `b1 = 0` : `exp a b2 = 1 * exp a b2`. Cas `b1 > 0` : `b1 + b2 ≠ 0`, donc c'est la 2ᵉ équation qui s'applique à `exp a (b1 + b2)`.

</details>

<details><summary>💡 Piste Q2.6</summary>

Trois cas : `b = 0`, `b` pair non nul, `b` impair. Posons `q = b quot 2`. Variant : `q < b` car `b > 0`. Utilise **Q2.3** : `exp a (q + q) = exp a q * exp a q`.

</details>

---

## Exercice 3 : Plus grand facteur premier

```haskell
pgfpAux :: Int -> Int -> Int
pgfpAux i n | i == n         = i
            | n `mod` i == 0 = pgfpAux i (n `quot` i)
            | otherwise      = pgfpAux (i+1) n

pgfp :: Int -> Int
pgfp n = pgfpAux 2 n          -- pour n ≥ 2
```

| Q | Ce qu'on demande |
|---|---|
| 3.1 | Calcul pas à pas de `pgfpAux 2 2520`. Pour quels `i` fait-on l'appel `pgfpAux i (n quot i)` ? Propriété commune ? |
| 3.2 | Quelle propriété lie `n` et les entiers `k` entre `2` et `i − 1` lors des appels ? |
| 3.3 | En déduire la **pré-condition** de `pgfpAux i n`. |
| 3.4 | Donner le **variant** et justifier qu'il est positif. |
| 3.5 | Démontrer que `pgfpAux i n` renvoie le plus grand diviseur premier de `n`. |

<details><summary>💡 Piste Q3.1–3.3</summary>

`2520 = 2³ × 3² × 5 × 7`. Regarde quels `i` divisent : ils sont tous… premiers ! Quand on arrive à `i`, on a déjà retiré de `n` tous les facteurs plus petits.

</details>

<details><summary>💡 Piste Q3.4</summary>

Un appel fait **baisser** `n`, l'autre fait **monter** `i`. Cherche une expression qui diminue dans les deux cas, par exemple une différence entre `n` et `i`. Pour la positivité, la pré-condition doit contenir `i ≤ n`.

</details>

---

## ✅ Avant de rendre

- [ ] Chaque preuve annonce le **variant** et l'**HI**.
- [ ] Chaque appel récursif : **variant ↓** et **pré ✓**.
- [ ] `python3 code/td1.py` ne signale aucune erreur.
