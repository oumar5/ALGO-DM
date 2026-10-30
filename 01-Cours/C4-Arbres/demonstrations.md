# C4 — Démonstrations sur les arbres

[⬅ Cours C4](README.md)

> ℹ️ Le cours **énonce** ces deux propriétés ; les preuves ci-dessous sont rédigées pour la révision, selon la méthode du cours.

---

## 1. Recherche dans un ABR

```haskell
estElement :: Int -> ABR -> Bool
estElement _ Vide = False
estElement k (N p t1 t2) | k == p    = True
                         | k < p     = estElement k t1
                         | otherwise = estElement k t2
```

| | |
|---|---|
| **Pré** | `bienFormé(t)` |
| **Post** | `estElement k t = True` ssi `k ∈ ⟦t⟧` |
| **Variant** | nombre d'éléments de `⟦t⟧` |

**Pourquoi le variant diminue ?** Si `t = N p t1 t2` est bien formé, tous les éléments de `⟦t1⟧` sont `< p` donc `p ∉ ⟦t1⟧` et `⟦t1⟧ ⊆ ⟦t⟧ \ {p}` : `|⟦t1⟧| < |⟦t⟧|`. Même chose pour `t2`.

**HI** : pour tout arbre `t'` bien formé avec `|⟦t'⟧| < |⟦t⟧|`, `estElement k t' = True` ssi `k ∈ ⟦t'⟧`.

| Cas | Raisonnement |
|---|---|
| `t = Vide` | résultat `False`, et `k ∉ ∅ = ⟦Vide⟧`. ✅ |
| `t = N p t1 t2`, `k == p` | résultat `True`, et `k = p ∈ ⟦t⟧`. ✅ |
| `t = N p t1 t2`, `k < p` | voir ci-dessous |
| `t = N p t1 t2`, `k > p` | symétrique (avec `t2`) |

**Cas `k < p`** — résultat `estElement k t1`. HI sur `t1` : variant ↓ (ci-dessus) ✅ ; `t1` bien formé (sous-arbre de `t`) ✅. Donc le résultat vaut `True` ssi `k ∈ ⟦t1⟧`. Reste à voir : `k ∈ ⟦t1⟧` ssi `k ∈ ⟦t⟧`.
- ⇒ : `⟦t1⟧ ⊆ ⟦t⟧`.
- ⇐ : `k ∈ {p} ∪ ⟦t1⟧ ∪ ⟦t2⟧` ; `k ≠ p` ; et `k ∉ ⟦t2⟧` car les éléments de `⟦t2⟧` sont `> p > k`. Donc `k ∈ ⟦t1⟧`. ✅

Ce qui achève la preuve par induction. ∎

---

## 2. Pousser les négations

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

| | |
|---|---|
| **Pré** | aucune |
| **Post** | avec `p' = pousseNeg p b` : (V) `vars p' = vars p` ; (E) pour toute `val` avec `vars p ⊆ dom val` : si `b`, `eval val p' = not (eval val p)` ; sinon `eval val p' = eval val p` |
| **Variant** | `taille p` |

**HI** : pour toute formule `q` avec `taille q < taille p` et tout booléen `c`, la post-condition est vraie pour `pousseNeg q c`.

Pour les sous-formules : `taille p1 < taille p1 + taille p2 + 1 = taille (Et p1 p2)` (idem `Ou`, `Non`) ✅, et `vars p1 ⊆ vars p ⊆ dom val` donc `eval val p1` est bien défini ✅.

| Cas | Raisonnement |
|---|---|
| `Var x` | si `b` : `eval val (Non (Var x)) = not (eval val (Var x))` ✅ ; sinon identique ✅. Variables : `{x}` ✅ |
| `Vrai`, `Faux` | `eval Faux = False = not True` etc. ✅ ; aucune variable ✅ |
| `Et p1 p2`, `b` | HI : `eval p1' = not e1`, `eval p2' = not e2`. `eval (Ou p1' p2') = not e1 \|\| not e2 = not (e1 && e2)` (**De Morgan**) ✅ |
| `Et p1 p2`, `not b` | HI : `eval (Et p1' p2') = e1 && e2` ✅ |
| `Ou p1 p2` | symétrique (De Morgan : `not e1 && not e2 = not (e1 \|\| e2)`) ✅ |
| `Non q`, `b` | résultat `pousseNeg q False` ; HI : `eval = eval q = not (not (eval q)) = not (eval (Non q))` ✅ |
| `Non q`, `not b` | résultat `pousseNeg q True` ; HI : `eval = not (eval q) = eval (Non q)` ✅ |

Pour (V) dans les cas `Et`/`Ou` : `vars p' = vars p1' ∪ vars p2' = vars p1 ∪ vars p2 = vars p` (HI). Cas `Non` : `vars (Non q) = vars q`.

Ce qui achève la preuve par induction. ∎
