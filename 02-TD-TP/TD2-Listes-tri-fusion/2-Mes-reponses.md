# TD2 — Mes réponses

[⬅ Énoncé](1-Enonce.md) · Modèle : [F2](../../04-Fiches-revision/F2-Modele-preuve-induction.md) · Axiomes : [F5](../../04-Fiches-revision/F5-Axiomes-et-notations.md)

## Exercice 1 : Tri fusion

### Q1.1.1 — `separe [1,3,2,7,1] [5,3,4,1]`

```text
separe [1,3,2,7,1] [5,3,4,1] = …
```

### Q1.1.2 — Python → [code/td2.py](code/td2.py)

### Q1.1.3 — Spécification de `separe`

- **Post** : (1) `l11 ++ l12 = l1` ; (2) `length l11 = min (length l1) (length l2 quot 2)`
- **Variant** : `length l1`

**HI** : …

**Cas `l2 = []`** : …

**Cas `l2 = [_]`** : …

**Cas `l1 = []` (et `l2` a ≥ 2 éléments)** : …

**Cas `l1 = x:l`, `l2 = _:_:cpt`** : …

### Q1.2.1 — `fusionne [1,3] [1,2,7]`

### Q1.2.2 — Python → [code/td2.py](code/td2.py)

### Q1.2.3 — Spécification de `fusionne`

### Q1.3 — `triFusion`

## Exercice 2 : PGCD

### Q2.1

- **Variant** : …

## 📝 Mes erreurs à retenir

-
