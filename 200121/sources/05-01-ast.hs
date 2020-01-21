data Expr = Const Int | Add Expr Expr | Sub Expr Expr | Mul Expr Expr | Div Expr Expr

eval :: Expr -> Int
eval (Const x) = x
eval (a `Add` b)  = eval a + eval b
eval (a `Sub` b)  = eval a - eval b
eval (a `Mul` b)  = eval a * eval b
eval (a `Div` b)  = eval a `div` eval b

a = (Const 10) `Add` (Const 10)
