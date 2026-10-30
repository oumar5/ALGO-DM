# F6 — Pièges et errata

[⬅ Fiches](README.md)

## ⚠️ Les 12 erreurs les plus coûteuses

| # | Erreur | Bon réflexe |
|---|---|---|
| 1 | Oublier de vérifier la **pré-condition** de l'appel récursif | ① variant ↓ **et** ② pré ✓, à chaque appel |
| 2 | HI appliquée à une valeur **non strictement** plus petite | `<`, jamais `≤` |
| 3 | Oublier un cas (une équation, une garde, un constructeur) | un cas par équation / garde |
| 4 | Induction sur la mauvaise liste pour `++` | sur la **première** |
| 5 | Prouver « trié » sans « permutation » pour un tri | les deux |
| 6 | Accumulateur : prouver seulement pour `acc` initial | généraliser à **tout** `acc` |
| 7 | Traduction en `while` avec affectations séquentielles | affectation **simultanée** |
| 8 | WP calculée de haut en bas | de **bas en haut** |
| 9 | Oublier une branche du `if` dans la WP | `(e et Q1) ou (non e et Q2)` |
| 10 | Utiliser la condition de boucle à la sortie | c'est **non cond** à la sortie |
| 11 | Invariant trop faible (pas de borne) | ajouter `i ≤ n+1`, `i > 0`… |
| 12 | Oublier les conditions de succès (`/`, `l[i]`) | les lister dès l'étape 1 |

## 📌 Errata des documents d'origine

Ces coquilles ont été **corrigées** dans les fiches du dossier (les PDF d'origine ont été supprimés).

| Document | Coquille | Correction |
|---|---|---|
| Cours induction (diapo factorielle) | « lorsque son argument vaut 0, `factoriel n` renvoie 0 » | renvoie **1** |
| Cours listes (tri rapide) | `[0,2,4] ++ triRapide [6,4,9]` dans la trace | `triRapide [6,4]` |
| Cours arbres (arbres préfixes) | `estElement (trouve c l) cs` | `trouve l c` (ordre des arguments) |
| `logique.py` du cours | méthodes indentées dans `__init__`, `self.Prop`, `&&`, `\|\|`, `return Faux`, types `Int`/`Bool` | version corrigée et testée : [logique.py](../01-Cours/C4-Arbres/code/logique.py) |
| Notes « tableaux » (insertion) | `l' = l[j-1 -> l[i], j -> l[j-1]]` | `l[j-1 -> l[j], j -> l[j-1]]` |
| Notes « récursion terminale » (`revAux`) | « Par C1 » dans le cas C2 | « Par C2 » |
| TD1 | `a = 2*(a quot b) + a mod b` | `b = 2*(b quot 2) + b mod 2` |
| TD2 | `separe` : « la moitié de celle de `l2` » | `length l11 = min (length l1) (length l2 quot 2)` |
| TD6 | I2 : `k ≠ v` et `d < k ≤ len(t)` | `t[k] ≠ v` et `d < k < len(t)` |
| TD6 | post-condition : `val(l)` | `val(t)` |
| TD6 Q1.2 / Q2.2 | « l'invariant est positif » | « le **variant** est positif » |
| DS 2024-2025 | 2ᵉ mot de `tbList t` : `[False,False,False]` | `[False,False]` |
| DS 2024-2025 | `tbNth` : `True : tbNth (n-k) t2` | `n - card t1` (vérifié par simulation) |

> 💡 En DS, si tu repères une coquille, **signale-la** en une ligne et explique ce que tu utilises à la place.
