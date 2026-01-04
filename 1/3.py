import sympy as sp

x, a, b, c, d = sp.symbols('x a b c d')

poly = a*x**3 + b*x**2 + c*x + d

solutions = sp.solve(poly, x)

solutions
//https://chatgpt.com/share/695a08f3-7e3c-8004-bb4b-163201c8ccc0
