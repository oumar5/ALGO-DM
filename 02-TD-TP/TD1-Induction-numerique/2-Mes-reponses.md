# TD1 — Mes réponses

[⬅ Énoncé](1-Enonce.md) · Modèle : [F2](../../04-Fiches-revision/F2-Modele-preuve-induction.md)

## Exercice 1 : Multiplication

### Q1.1 — `mult 3 5`

```text
mult 3 5 = …
```

### Q1.2 — Python

→ dans [code/td1.py](code/td1.py)

### Q1.3 — Démonstration

- **Pré** : `x ≥ 0`
- **Post** : `mult x y = x * y`
- **Variant** : `x`

**HI** : …

**Cas `x = 0`** : …

**Cas `x ≠ 0`** : appel `mult (x-1) y`
1. variant ↓ : …
2. pré ✓ : …

Ce qui achève la preuve par induction. ∎

## Exercice 2 : Exponentiation

### Q2.1 — `exp 3 3`

### Q2.2 — Python → [code/td1.py](code/td1.py)

### Q2.3 — `exp a (b1 + b2) = exp a b1 * exp a b2`

### Q2.4 — `expR 3 3`

### Q2.5 — Python → [code/td1.py](code/td1.py)

### Q2.6 — `expR a b = exp a b`

## Exercice 3 : Plus grand facteur premier

### Q3.1 — `pgfpAux 2 2520`

### Q3.2

### Q3.3 — Pré-condition

### Q3.4 — Variant

### Q3.5 — Démonstration

## 📝 Mes erreurs à retenir

-
