# F1 — Haskell et Python : mémo

[🏠 Accueil](../00-Commencer-ici.md)

## Syntaxe Haskell

| Élément | Exemple |
|---|---|
| Signature | `f :: Int -> [Int] -> Bool` |
| Équations (testées dans l'ordre) | `f 0 l = …` puis `f n l = …` |
| Application | `f x y` (pas de virgules) ; `f (n-1)` avec parenthèses |
| Gardes | `f n \| n < 2 = n` / `\| otherwise = …` |
| Conditionnelle | `if c then e1 else e2` |
| Local | `where x = …` ou `let x = … in …` |
| Tuple | `(q, r)` ; motif `incr1 (q, r) = (q+1, r)` |
| Liste | `[]`, `x : l`, `[1,2,3]`, `l1 ++ l2` |
| Compréhension | `[y \| y <- l, y < x]` |
| Opérateur infixe | ``a `mod` b`` = `mod a b` ; ``a `quot` b`` (division entière) |
| Type algébrique | `data ABR = N Int ABR ABR \| Vide` |
| Synonyme | `type MB = [Bool]` |

## Haskell → Python (récursif)

| Haskell | Python |
|---|---|
| `f [] = …` | `if l == []: …` |
| `f (x:l) = …` | `x, reste = l[0], l[1:]` |
| `f (x:y:l)` | `l[0]`, `l[1]`, `l[2:]` |
| `x : l` | `[x] + l` |
| `l1 ++ l2` | `l1 + l2` |
| ``a `quot` b``, ``a `mod` b`` | `a // b`, `a % b` (identiques pour `a, b ≥ 0`) |
| `let (a, b) = f x in …` | `a, b = f(x)` |

## Haskell → Python `while` (récursion terminale)

```text
f x1 … xn | arret     = resultat           def f(x1, …, xn):
          | otherwise = f e1 … en              while not arret:
                                                   x1, …, xn = e1, …, en   # SIMULTANÉ
                                               return resultat
```

Plusieurs gardes récursives : un `if / elif / else` dans le corps de la boucle.

## Haskell → Python objet (types algébriques)

| Haskell | Python |
|---|---|
| `data T = …` | `class T:` (abstraite, méthodes avec `pass` / `raise NotImplementedError`) |
| constructeur `C a b` | `class C(T):` avec `__init__(self, a, b)` |
| argument du constructeur | attribut `self.a` |
| fonction `f :: T -> …` | méthode `f(self, …)` redéfinie dans **chaque** sous-classe |
| `f (C a b) = … f b …` | dans `C` : `… self.b.f() …` |
| constructeur sans argument `Vide` | `Vide()` (ne pas oublier les parenthèses !) |

```python
class ABR:
    def estElement(self, k): pass

class Vide(ABR):
    def estElement(self, k): return False

class N(ABR):
    def __init__(self, n, fg, fd):
        self.valeur, self.fils_gauche, self.fils_droit = n, fg, fd
    def estElement(self, k):
        if k == self.valeur: return True
        if k < self.valeur:  return self.fils_gauche.estElement(k)
        return self.fils_droit.estElement(k)
```
