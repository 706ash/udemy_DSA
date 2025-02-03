import sympy as sp

x = sp.Symbol('x')
f = sp.exp(-x)

print("InDefinite: ",sp.integrate(f, x))

print("Definite: ",sp.integrate(f, (x, 0, sp.oo)))
