# Chapitre 3 — Exemples corrigés

[⬅ Cours du chapitre 3](1-Cours.md) · [🏠 Accueil](../../README.md) · Règles `triée` et `perm` : [F5](../../04-Fiches-revision/F5-Axiomes-et-notations.md) · Suite : [Exercices ➡](3-Exercices.md)

---

## Exemple 1 ⭐ — La division avec accumulateur 🍬

```haskell
divAux :: Int -> Int -> Int -> (Int, Int)
divAux a b acc | a < b     = (acc, a)
               | otherwise = divAux (a-b) b (acc+1)

divRT a b = divAux a b 0
```

> 💬 En bonbons : `acc` compte les tours **déjà faits**, `a` les bonbons **restants**.
> À tout moment : **bonbons déjà donnés (`acc × b`) + bonbons restants (`a`) = le même total**.

| | |
|---|---|
| **Pre1, Pre2** | `a ≥ 0`, `b > 0` |
| **Post1** | avec `(q, r) = divAux a b acc` : `acc × b + a = q × b + r` |
| **Post2** | `0 ≤ r < b` |
| **Variant** | `a` |

**HI :** pour tous `a', b', acc'` avec `a' < a`, `a' ≥ 0`, `b' > 0`, le résultat `(q', r')` de `divAux a' b' acc'` vérifie `acc' × b' + a' = q' × b' + r'` et `0 ≤ r' < b'`.

**Cas `a < b`** : le résultat est `(acc, a)`.
- Post1 : `acc × b + a = acc × b + a` ✅
- Post2 : `0 ≤ a` (Pre1) et `a < b` (cas) ✅

**Cas `a ≥ b`** : le résultat est `divAux (a-b) b (acc+1)`.
- ① variant : `a − b < a` car `b > 0` ✅
- ② pré : `a − b ≥ 0` (cas) et `b > 0` (Pre2) ✅

L'HI donne : `(acc+1) × b + (a−b) = q × b + r` et `0 ≤ r < b`.
Or `(acc+1) × b + a − b = acc × b + b + a − b = acc × b + a`. Donc Post1 ✅ et Post2 ✅.

Ce qui achève la preuve par induction. ∎

**Conséquence :** avec `acc = 0`, `divRT a b` donne `a = q × b + r` et `0 ≤ r < b`.

---

## Exemple 2 ⭐ — Retourner une pile de livres 📚

```haskell
reverse []    = []                    revAux []    acc = acc
reverse (n:l) = reverse l ++ [n]      revAux (n:l) acc = revAux l (n:acc)

revRT l = revAux l []
```

| | |
|---|---|
| **Objectif** | `revAux l acc = reverse l ++ acc` (pour tout `acc`) |
| **Variant** | `length l` |
| **HI** | pour toutes `l'`, `acc'` avec `length l' < length l` : `revAux l' acc' = reverse l' ++ acc'` |

**Cas `l = []`** : `revAux [] acc = acc` et `reverse [] ++ acc = [] ++ acc = acc` ✅

**Cas `l = x : l'`** : on calcule les deux côtés.

```text
Côté gauche :  revAux (x:l') acc = revAux l' (x:acc)

Côté droit :   reverse (x:l') ++ acc = (reverse l' ++ [x]) ++ acc
                                     = reverse l' ++ ([x] ++ acc)     associativité (chapitre 2)
                                     = reverse l' ++ (x:acc)
```

L'HI sur `revAux l' (x:acc)` (① variant ↓ ; ② rien à vérifier) donne `revAux l' (x:acc) = reverse l' ++ (x:acc)`. Les deux côtés sont égaux ✅

Ce qui achève la preuve par induction. ∎ **Conséquence :** `revRT l = reverse l ++ [] = reverse l`.

---

## Exemple 3 ⭐⭐⭐ — Fusionner deux paquets triés 🃏

> 📝 **Situation :** deux paquets de copies, **chacun déjà rangé** par note croissante, posés côte à côte.
> On regarde la copie du dessus de chaque paquet, on prend **la plus petite** et on la pose sur le tas final. On recommence.

```haskell
fusionne :: [Int] -> [Int] -> [Int]
fusionne [] l = l
fusionne l [] = l
fusionne (x1:l1) (x2:l2) | x1 <= x2  = x1 : fusionne l1 (x2:l2)
                         | otherwise = x2 : fusionne (x1:l1) l2
```

```text
fusionne [1,4] [2,3] = 1 : fusionne [4] [2,3] = 1 : 2 : fusionne [4] [3]
                     = 1 : 2 : 3 : fusionne [4] [] = [1,2,3,4]
```

### Les règles utilisées (en clair)

| Règle | En clair |
|---|---|
| **TCons** | `x : l` est triée ⇔ `l` est triée **et** `x` est ≤ tous les éléments de `l` |
| **PRefl** | une liste a les mêmes éléments qu'elle-même |
| **PCons** | si `l1` et `l2` ont les mêmes éléments, alors `x : l1` et `x : l2` aussi |
| **PPerm** | `x : (l1 ++ l2)` et `l1 ++ (x : l2)` ont les mêmes éléments (on a juste déplacé `x`) |
| **PTrans** | si A a les mêmes éléments que B, et B que C, alors A que C |

`perm(A, B)` se lit « A et B ont les mêmes éléments ».

### La preuve

| | |
|---|---|
| **Pre1, Pre2** | `l1` triée, `l2` triée |
| **Post1** | `fusionne l1 l2` est triée |
| **Post2** | `perm(fusionne l1 l2, l1 ++ l2)` |
| **Variant** | `length l1 + length l2` (le nombre total de copies : **un des deux** paquets diminue) |

**Cas `l1 = []`** : le résultat est `l2`, triée (Pre2), et `l1 ++ l2 = l2` (PRefl) ✅
**Cas `l2 = []`** : pareil avec `l1`, car `l1 ++ [] = l1` ✅

**Cas `x1 ≤ x2`** : le résultat est `x1 : fusionne l1' l2` (avec `l1 = x1 : l1'`).
- ① variant : il y a une copie de moins ✅
- ② pré : `l1'` triée (TCons sur `l1`), `l2` triée (Pre2) ✅
- L'HI dit : `fusionne l1' l2` est triée et contient les éléments de `l1' ++ l2`.
- **Triée ?** `x1` est ≤ tout `l1'` (car `l1` est triée) et `x1 ≤ x2` ≤ tout `l2'`. Donc `x1` est ≤ tout ce qui suit, et TCons conclut ✅
- **Mêmes éléments ?** PCons : `x1 : fusionne l1' l2` a les mêmes éléments que `x1 : (l1' ++ l2) = l1 ++ l2` ✅

**Cas `x1 > x2`** : même démarche avec `x2 : fusionne l1 l2'`. Seule la dernière étape change : `x2` vient de `l2`, il faut le **déplacer**.
- PCons : `x2 : fusionne l1 l2'` a les mêmes éléments que `x2 : (l1 ++ l2')`
- PPerm : `x2 : (l1 ++ l2')` a les mêmes éléments que `l1 ++ (x2 : l2') = l1 ++ l2`
- PTrans relie les deux ✅

Ce qui achève la preuve par induction. ∎

---

➡ **À toi de jouer :** [Exercices du chapitre](3-Exercices.md) · puis les [corrections](4-Corrections.md).
