-- Logique propositionnelle (code du cours, C4 — Sylvain Salvati)
-- Ajout par rapport à l'original : la fonction vars, utilisée dans les spécifications.

module Logique where

data Prop = Var String   -- Variable propositionnelle
  | Vrai                 -- Proposition vraie
  | Faux                 -- Proposition fausse
  | Et Prop Prop         -- Conjonction
  | Ou Prop Prop         -- Disjonction
  | Non Prop             -- Négation
  deriving Show

-- Liste associative : nom de variable -> valeur booléenne.
type Valuation = [(String, Bool)]

-- Nombre de symboles de p. Sert de variant pour les fonctions sur Prop.
taille :: Prop -> Int
taille (Var _)    = 1
taille Vrai       = 1
taille Faux       = 1
taille (Et p1 p2) = taille p1 + taille p2 + 1
taille (Ou p1 p2) = taille p1 + taille p2 + 1
taille (Non p)    = taille p + 1

-- Variables apparaissant dans p (avec répétitions possibles).
vars :: Prop -> [String]
vars (Var x)    = [x]
vars Vrai       = []
vars Faux       = []
vars (Et p1 p2) = vars p1 ++ vars p2
vars (Ou p1 p2) = vars p1 ++ vars p2
vars (Non p)    = vars p

-- Booléen associé à x dans val.
-- Pré-condition : x ∈ dom val.
trouve :: Valuation -> String -> Bool
trouve ((x, b) : val) y | x == y    = b
                        | otherwise = trouve val y

-- Valeur de p pour la valuation val.
-- Pré-condition : vars p ⊆ dom val.
eval :: Valuation -> Prop -> Bool
eval val (Var x)    = trouve val x
eval _   Vrai       = True
eval _   Faux       = False
eval val (Et p1 p2) = eval val p1 && eval val p2
eval val (Ou p1 p2) = eval val p1 || eval val p2
eval val (Non p)    = not (eval val p)

-- Pousse les négations jusqu'aux feuilles de p.
-- Pré-condition : aucune.
-- Post-condition : en posant p' = pousseNeg p b,
--   1. vars p' = vars p
--   2. pour toute valuation val telle que vars p ⊆ dom val :
--      2.1 si b vaut True,  eval val p' = not (eval val p)
--      2.2 si b vaut False, eval val p' = eval val p
pousseNeg :: Prop -> Bool -> Prop
pousseNeg (Var x) b    | b         = Non (Var x)
                       | otherwise = Var x
pousseNeg Vrai b       | b         = Faux
                       | otherwise = Vrai
pousseNeg Faux b       | b         = Vrai
                       | otherwise = Faux
pousseNeg (Et p1 p2) b | b         = Ou (pousseNeg p1 b) (pousseNeg p2 b)
                       | otherwise = Et (pousseNeg p1 b) (pousseNeg p2 b)
pousseNeg (Ou p1 p2) b | b         = Et (pousseNeg p1 b) (pousseNeg p2 b)
                       | otherwise = Ou (pousseNeg p1 b) (pousseNeg p2 b)
pousseNeg (Non p) b                = pousseNeg p (not b)
