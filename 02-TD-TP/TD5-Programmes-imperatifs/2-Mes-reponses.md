# TD5 — Mes réponses

[⬅ Énoncé](1-Enonce.md) · Méthode : [F3 WP](../../04-Fiches-revision/F3-Plus-faible-precondition.md) · [F4 Boucles](../../04-Fiches-revision/F4-Methode-boucles.md)

## Exercice 1 : Plus faible pré-condition

### Q1.1

```python
# WP = …
a = a + 1
# …
if a + b == 0:
    # …
    a = b
    # a = 0 et b != 0
else:
    # …
    b = a
    # a = 0 et b != 0
# a = 0 et b != 0
```

**Interprétation** : …

### Q1.2

```python
# WP = …
a = b * c
# …
if a != 0:
    # …
    b = c * b / a
    # …
    c = c + 1
    # …
else:
    # …
    a = (a + 1) / c
    # …
    b = b * b
    # …
# …
c = a * b
# a % (b + c) = 0
```

## Exercice 2 : Division

### Q2.1 — Variant

### Q2.2 — Invariant

### Q2.3 — Avant la boucle

### Q2.4 — Après la boucle

## Exercice 3 : Nombre de diviseurs

### Q3.1 — Variant

### Q3.2 — Invariant

### Q3.3 — Avant la boucle

### Q3.4 — Après la boucle

## 📝 Mes erreurs à retenir

-
