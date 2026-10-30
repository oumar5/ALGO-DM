# Chapitre 4 — Exemples corrigés

[⬅ Cours du chapitre 4](1-Cours.md) · [🏠 Accueil](../../00-Commencer-ici.md)

> ℹ️ Le cours **énonce** ces deux propriétés. Les preuves ci-dessous sont rédigées pour t'entraîner, avec la méthode du cours.

---

## Exemple 1 ⭐⭐ — Chercher dans un ABR 🔢

```haskell
estElement :: Int -> ABR -> Bool
estElement _ Vide = False
estElement k (N p t1 t2) | k == p    = True
                         | k < p     = estElement k t1
                         | otherwise = estElement k t2
```

| | |
|---|---|
| **Pré** | `t` est bien formé (petits à gauche, grands à droite, partout) |
| **Post** | `estElement k t = True` **si et seulement si** `k` est dans `t` (`k ∈ ⟦t⟧`) |
| **Variant** | le nombre d'éléments de `t` |

> 💬 **Pourquoi le variant baisse ?** Un sous-arbre contient **moins** d'éléments que l'arbre entier : il lui manque au moins la racine `p`.

**HI :** pour tout arbre `t'` bien formé avec moins d'éléments que `t`, `estElement k t' = True` ssi `k ∈ ⟦t'⟧`.

| Cas | Résultat | Pourquoi c'est juste |
|---|---|---|
| `t = Vide` | `False` | l'arbre vide ne contient rien ✅ |
| `t = N p t1 t2` et `k == p` | `True` | `k` est la racine ✅ |
| `t = N p t1 t2` et `k < p` | `estElement k t1` | voir ci-dessous |
| `t = N p t1 t2` et `k > p` | `estElement k t2` | pareil, côté droit |

**Le cas `k < p`, en détail.**
1. **Peut-on utiliser l'HI sur `t1` ?** ① `t1` a moins d'éléments que `t` ✅ ② `t1` est bien formé, car c'est un morceau de `t` ✅
2. L'HI dit : le résultat est `True` ssi `k ∈ ⟦t1⟧`.
3. **Reste à voir que « `k` est dans `t1` » équivaut à « `k` est dans `t` ».**
   - Si `k` est dans `t1`, il est dans `t` (`t1` fait partie de `t`).
   - Si `k` est dans `t` : ce n'est pas la racine (`k ≠ p`) ; ce n'est pas à droite (à droite, tout est `> p > k`). Donc il est à gauche, dans `t1`. ✅

> 💬 C'est le jeu « plus grand / plus petit » : si le nombre cherché est plus petit, **inutile** de regarder à droite.

Ce qui achève la preuve par induction. ∎

---

## Exemple 2 ⭐⭐⭐ — Faire descendre les négations

```haskell
pousseNeg :: Prop -> Bool -> Prop
pousseNeg (Var x) b    | b = Non (Var x)  | otherwise = Var x
pousseNeg Vrai b       | b = Faux         | otherwise = Vrai
pousseNeg Faux b       | b = Vrai         | otherwise = Faux
pousseNeg (Et p1 p2) b | b = Ou (pousseNeg p1 b) (pousseNeg p2 b)
                       | otherwise = Et (pousseNeg p1 b) (pousseNeg p2 b)
pousseNeg (Ou p1 p2) b | b = Et (pousseNeg p1 b) (pousseNeg p2 b)
                       | otherwise = Ou (pousseNeg p1 b) (pousseNeg p2 b)
pousseNeg (Non p) b    = pousseNeg p (not b)
```

> 💬 Le booléen `b` veut dire : « **une négation est en attente** ». Quand on croise un `Non`, on **inverse** `b`.

**Exemple :** `pousseNeg (Non (Et (Var "a") (Var "b"))) False`
→ `pousseNeg (Et a b) True` → `Ou (pousseNeg a True) (pousseNeg b True)` → `Ou (Non a) (Non b)`.
C'est De Morgan : « pas (a et b) » = « (pas a) ou (pas b) ».

| | |
|---|---|
| **Pré** | aucune |
| **Post** | avec `p' = pousseNeg p b` : (V) `p'` a les mêmes variables que `p` ; (E) si `b` vaut `True`, `p'` a la valeur **contraire** de `p` ; sinon `p'` a la **même** valeur que `p` |
| **Variant** | `taille p` |

**HI :** la post-condition est vraie pour toute formule plus petite que `p`, et pour **tout** booléen.

> 💬 « Pour tout booléen » est indispensable : dans le cas `Non`, l'appel se fait avec `not b`, pas avec `b`.

Notons `e1 = eval val p1` et `e2 = eval val p2`.

| Cas | Calcul | Justification |
|---|---|---|
| `Var x`, `Vrai`, `Faux` | direct | `Non (Var x)` vaut le contraire de `Var x` ; `Faux` le contraire de `Vrai`… ✅ |
| `Et p1 p2` avec `b = True` | `Ou p1' p2'` vaut `(non e1) ou (non e2)` | HI sur `p1` et `p2`, puis De Morgan : `= non (e1 et e2)` ✅ |
| `Et p1 p2` avec `b = False` | `Et p1' p2'` vaut `e1 et e2` | HI ✅ |
| `Ou p1 p2` | même chose | De Morgan dans l'autre sens ✅ |
| `Non q` avec `b = True` | `pousseNeg q False` a la valeur de `q` | HI ; et `q` = contraire de `Non q` ✅ |
| `Non q` avec `b = False` | `pousseNeg q True` a la valeur contraire de `q` | HI ; et le contraire de `q`, c'est `Non q` ✅ |

**Les variables (V)** : dans chaque cas, on reconstruit la formule avec les **mêmes** sous-formules ; l'HI donne les mêmes variables pour `p1'` et `p2'`.

**Le variant** : `p1` et `p2` sont plus petits que `Et p1 p2` (il manque le symbole `Et`) ; `q` est plus petit que `Non q`.

Ce qui achève la preuve par induction. ∎

> 🧪 Le fichier [logique.py](code/logique.py) vérifie cette propriété sur un exemple : `python3 code/logique.py`.
