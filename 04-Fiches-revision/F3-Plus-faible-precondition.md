# F3 — Plus faible pré-condition (WP)

[🏠 Accueil](../00-Commencer-ici.md)

> ⏰ **L'idée :** pour arriver à 8h avec 40 min de trajet, il faut partir avant 7h20. On part de l'**objectif** (en bas du code) et on **remonte** ligne par ligne.

## Les règles

| Commande | WP de `P` |
|---|---|
| `x = e` | `P[x ← e]` **et** succès(`e`) |
| `l[i] = e` | `P[l ← l[i → e]]` **et** `0 ≤ i < len(l)` **et** succès(`e`) |
| `c1` puis `c2` | `WP(c1, WP(c2, P))` |
| `if e: c1 else: c2` | `((e et WP(c1,P)) ou (non e et WP(c2,P)))` **et** succès(`e`) |
| `pass` | `P` |

> 🔑 On **remonte** : on part de la post-condition **en bas** et on écrit la WP **au-dessus** de chaque ligne.

## Conditions de succès

| Expression | Réussit ssi |
|---|---|
| `a / b`, `a // b`, `a % b` | `b ≠ 0` |
| `sqrt(x)` | `x ≥ 0` |
| `log(x)` | `x > 0` |
| `l[i]` | `0 ≤ i < len(l)` |
| `e1 and e2` | succès(`e1`) et (`non e1` ou succès(`e2`)) |
| `e1 or e2` | succès(`e1`) et (`e1` ou succès(`e2`)) |

## Exemple rédigé

```python
# (a % 2 == 0 et a + 4 pair) ou (a % 2 != 0 et a + 1 pair)   ⇔ vrai
if a % 2 == 0:
    # a + 4 pair
    a = a + 4
    # a pair
else:
    # a + 1 pair
    a = a + 1
    # a pair
# a pair
```

## ✅ Checklist

- [ ] Je calcule **de bas en haut**, une ligne de commentaire entre chaque instruction.
- [ ] Je remplace la variable affectée **partout** dans la propriété.
- [ ] Pour un `if`, je calcule **chaque branche** séparément, puis je combine.
- [ ] Je **simplifie** le résultat (et je l'interprète : toujours vrai ? toujours faux ?).
- [ ] Je n'oublie pas les **conditions de succès** (divisions, indices).
- [ ] Pour conclure : **Pré ⇒ WP**.

## Variables fraîches (pour le variant)

Pour savoir comment évolue `i` : calculer `WP(corps, i = a)` avec `a` une **nouvelle** variable.
Si on obtient `i + 1 = a` au début, alors `i` augmente de 1 à chaque tour.
