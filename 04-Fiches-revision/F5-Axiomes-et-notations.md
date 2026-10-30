# F5 — Axiomes et notations

[⬅ Fiches](README.md)

## Listes triées et permutations

| Nom | Axiome | Sert à |
|---|---|---|
| **TVide** | `triée([])` | cas de base |
| **TCons** | `triée(x:l)` ssi `triée(l)` et `x` ≤ chaque élément de `l` | construire / décomposer une liste triée |
| **PRefl** | `perm(l, l)` | même liste |
| **PSym** | `perm(l1, l2)` ssi `perm(l2, l1)` | retourner |
| **PTrans** | `perm(l1, l2)` et `perm(l2, l3)` ⇒ `perm(l1, l3)` | enchaîner |
| **PCons** | `perm(l1, l2)` ⇒ `perm(x:l1, x:l2)` | ajouter la même tête |
| **PApp** | `perm(l1, l1')` et `perm(l2, l2')` ⇒ `perm(l1 ++ l2, l1' ++ l2')` | concaténer |
| **PPerm** | `perm(x:(l1 ++ l2), l1 ++ (x:l2))` | déplacer un élément |

## Propriétés déjà démontrées (réutilisables)

| Propriété | Où |
|---|---|
| `l ++ [] = l` | [C2](../01-Cours/C2-Listes/demonstrations.md) |
| `l1 ++ (l2 ++ l3) = (l1 ++ l2) ++ l3` | [C2](../01-Cours/C2-Listes/demonstrations.md) |
| `length (l1 ++ l2) = length l1 + length l2` | [C2](../01-Cours/C2-Listes/README.md) |
| ordonnées + `l1 ≤ l2` ⇒ `l1 ++ l2` ordonnée | [C2](../01-Cours/C2-Listes/demonstrations.md) |
| `revAux l acc = reverse l ++ acc` | [C3](../01-Cours/C3-Recursion-terminale/demonstrations.md) |

## Ensembles et multi-ensembles

| | Ensemble `{a}` | Multi-ensemble `{\|a\|}` |
|---|---|---|
| Vide | `∅`, `{}` | `∅`, `{\|\|}` |
| Singleton | `{k}` | `{\|k\|}` |
| Union | `∪` | `⊔` (les multiplicités s'additionnent) |
| Intersection | `∩` | `⊓` |
| Différence | `\` | `−` (retire **une** occurrence par élément) |
| Appartenance, inclusion | `∈`, `⊆`, `⊂` | `∈`, `⊆`, `⊂` |

Exemple : `{|1, 2, 2|} ⊔ {|2|} = {|1, 2, 2, 2|}` et `{|1, 2, 2|} − {|2|} = {|1, 2|}`.

## Arbres

| Notation | Sens |
|---|---|
| `⟦t⟧` | ensemble (ou multi-ensemble) des éléments de l'arbre `t` |
| `bienFormé(t)` | la propriété structurelle (ABR ordonné, tournoi avec vainqueur minimal…) |
| `taille t`, `hauteur t` | variants classiques |

## Tableaux

| Notation | Sens |
|---|---|
| `l[i → v]` | `l` dans lequel la case `i` vaut `v` |
| `l[i1 → v1, i2 → v2]` | plusieurs cases modifiées (ex. un échange) |
| `val(l)` | multi-ensemble des valeurs de `l` |
| `l[0..i−1]` trié | pour tous `0 ≤ k1 < k2 < i`, `l[k1] ≤ l[k2]` |

Règle de lecture : `l[i → v][k]` vaut `v` si `k = i`, et `l[k]` sinon.

## Logique

| Symbole | Sens |
|---|---|
| `∀x. P` | pour tout `x`, `P` |
| `P ⇒ Q` | si `P` alors `Q` |
| `P ∧ Q`, `P ∨ Q`, `¬P` | et, ou, non |
| `⊤`, `⊥` | vrai, faux |
| `a \| b` | `a` divise `b` |
