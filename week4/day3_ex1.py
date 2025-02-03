import sympy as sp

x = sp.Symbol('x')
f = x**3 - 5*x + 7

print(sp.diff(f, x))