# Chapitre 1 — Exercices

[🏠 Accueil](../../README.md) · [⬅ Cours](1-Cours.md) · [Exemples corrigés](2-Exemples-corriges.md) · **Corrections : [4-Corrections.md](4-Corrections.md)**

> ✏️ Écris tes réponses sur une feuille (ou dans un fichier à toi), puis compare avec les corrections.
> ⭐ = échauffement · ⭐⭐ = entraînement · ⭐⭐⭐ = niveau DS

---

## Exercice 1 ⭐ — Doubler, doubler, doubler

> 🦠 Une bactérie se divise en deux toutes les heures. Au bout de `n` heures, combien y en a-t-il ?

```haskell
puissance2 :: Int -> Int
puissance2 0 = 1
puissance2 n = 2 * puissance2 (n-1)
```

Calcule `puissance2 3` **pas à pas**, en remplaçant comme dans le cours.

---

## Exercice 2 ⭐ — Les mentions du bac

```haskell
mention :: Int -> String
mention note | note >= 16 = "Très bien"
             | note >= 14 = "Bien"
             | note >= 10 = "Admis"
             | otherwise  = "Ajourné"
```

1. Que valent `mention 15`, `mention 10`, `mention 9` et `mention 17` ?
2. On **échange** les deux premières lignes (`>= 14` avant `>= 16`). Que vaut maintenant `mention 17` ? Pourquoi ?

---

## Exercice 3 ⭐ — Écrire le contrat

Pour chaque fonction, écris la **pré-condition** et la **post-condition** (en français, puis en maths).

| Fonction | Ce qu'elle fait |
|---|---|
| `retrait solde montant` | 🏧 retire `montant` d'un compte qui contient `solde` (on n'a pas le droit d'être à découvert) |
| `racineEntiere n` | la racine carrée **arrondie en dessous** : `racineEntiere 10 = 3` |
| `dernierChiffre n` | le chiffre des unités : `dernierChiffre 472 = 2` |

---

## Exercice 4 ⭐ — Trouver le compte à rebours

Pour chaque fonction, donne un **variant** (et la pré-condition nécessaire), ou explique pourquoi elle **ne s'arrête pas**.

```haskell
f n   | n == 0    = 0
      | otherwise = f (n-1)

g a b | a >= b    = a
      | otherwise = g (a+1) b

h n   | n == 1    = 0
      | otherwise = h (n `div` 2)

k n   | n == 0    = 0
      | otherwise = k (n+1)
```

---

## Exercice 5 ⭐⭐ — Le carrelage

> 🟦 Un carré de `n × n` carreaux se construit en ajoutant, au carré `(n−1) × (n−1)`, une « équerre » en forme de L de `2n − 1` carreaux.

Démontre par induction que pour tout `n ≥ 0` :

```text
1 + 3 + 5 + … + (2n − 1) = n²
```

(pour `n = 0`, la somme est vide et vaut 0)

---

## Exercice 6 ⭐⭐ — Les bactéries, prouvé

Démontre que `puissance2 n = 2ⁿ` pour tout `n ≥ 0`.
Donne la pré-condition, la post-condition, le variant, l'HI, puis les cas.

---

## Exercice 7 ⭐⭐ — La tirelire

> 🐷 Une tirelire contient 10 € au départ. Chaque mois, on y glisse 5 €.

```haskell
tirelire :: Int -> Int
tirelire 0 = 10
tirelire n = tirelire (n-1) + 5
```

1. Combien contient la tirelire au bout d'un an (`tirelire 12`) ?
2. Démontre que `tirelire n = 10 + 5n` pour tout `n ≥ 0`.

---

## Exercice 8 ⭐⭐ — Pair ou impair ?

```haskell
pair :: Int -> Bool
pair 0 = True
pair n = not (pair (n-1))
```

1. Calcule `pair 3` pas à pas.
2. Démontre que, pour `n ≥ 0`, `pair n = True` **si et seulement si** `n` est pair.

---

## Exercice 9 ⭐⭐ — Trouve l'erreur 🕵️

Voici une « preuve » de la division avec **une seule** pré-condition : `a ≥ 0`.

> **Variant :** `a`. **HI :** pour tout `a' < a` avec `a' ≥ 0`, `division a' b` est correcte.
> **Cas `a < b` :** le résultat est `(0, a)`, et `a = 0 × b + a`. ✅
> **Cas `a ≥ b` :** on appelle `division (a-b) b`. Le variant baisse car `a − b < a`. La pré-condition est vraie car `a − b ≥ 0`. Par HI…

1. Quelle phrase est **fausse** ? Donne une valeur de `b` qui le montre.
2. Que se passe-t-il quand on exécute `division 7 0` ?
3. Quelle pré-condition faut-il ajouter ?

---

## Exercice 10 ⭐⭐⭐ — Le reste

> 🍕 On partage `a` parts de pizza entre `b` personnes ; `reste a b` est le nombre de parts qui restent.

```haskell
reste :: Int -> Int -> Int
reste a b | a < b     = a
          | otherwise = reste (a-b) b
```

1. Calcule `reste 17 5` pas à pas.
2. Démontre : si `a ≥ 0` et `b > 0`, alors, avec `r = reste a b` :
   - (Post1) `0 ≤ r < b`
   - (Post2) `a − r` est un multiple de `b`.

---

## Exercice 11 ⭐⭐⭐ — Le PGCD par soustractions

> 🧱 Je veux carreler une pièce de 12 m × 18 m avec des carreaux carrés **tous identiques**, les plus grands possible. Leur côté est le **PGCD** de 12 et 18.

```haskell
pgcd :: Int -> Int -> Int
pgcd a b | a == b    = a
         | a > b     = pgcd (a-b) b
         | otherwise = pgcd a (b-a)
```

1. Calcule `pgcd 12 18` pas à pas.
2. Pré-condition : `a > 0` et `b > 0`. Pourquoi `a` seul (ou `b` seul) ne convient pas comme variant ? Propose un variant.
3. Démontre que `pgcd a b` **divise** `a` et `b`.

---

## Exercice 12 ⭐⭐⭐ — Combien de chiffres ?

> 📞 Combien de chiffres faut-il pour écrire un prix, un numéro, une année ?

```haskell
nbChiffres :: Int -> Int
nbChiffres n | n < 10    = 1
             | otherwise = 1 + nbChiffres (n `div` 10)
```

``n `div` 10`` enlève le dernier chiffre : ``472 `div` 10 = 47``.

1. Calcule `nbChiffres 2026`.
2. Donne un variant (pré-condition : `n ≥ 0`) et justifie qu'il baisse.
3. Démontre que `n < 10^(nbChiffres n)` pour tout `n ≥ 0`.

> 💡 Indice : si `n ≥ 10`, on a ``n = 10 × (n `div` 10) + (n `mod` 10)`` avec ``n `mod` 10 ≤ 9``.
