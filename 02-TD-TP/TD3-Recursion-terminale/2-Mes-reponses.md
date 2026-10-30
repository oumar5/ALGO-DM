# TD3 — Mes réponses

[⬅ Énoncé](1-Enonce.md) · Modèle : [F2](../../04-Fiches-revision/F2-Modele-preuve-induction.md)

## Exercice 1 : Exponentiation rapide terminale

### Q1.1 — Python → [code/td3.py](code/td3.py)

### Q1.2 — `expAux a b acc = acc × aᵇ`

- **Pré** : `b ≥ 0`
- **Variant** : `b`

**HI** : …

**Cas `b = 0`** : …

**Cas `b` pair, `b ≠ 0`** : …

**Cas `b` impair** : …

Ce qui achève la preuve par induction. ∎

### Q1.3 — `expR a b = aᵇ`

## Exercice 2 : Insertion terminale

### Q2.2 — Python → [code/td3.py](code/td3.py)

### Q2.3 — Spécification de `insererAux`

**Cas `l = []`** : …

**Cas `l = n:l'`, `k ≤ n`** : …

**Cas `l = n:l'`, `k > n`** : …

## 📝 Mes erreurs à retenir

-
