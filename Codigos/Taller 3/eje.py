import sympy 
from sympy import *

#Variables y límites de integración

t = symbols('t')
a, b = -1, 1

#Definimos la base de monomios

base = [Matrix([1]), Matrix([t]), Matrix([t**2]), Matrix([t**3])]

#Definimos el producto interno

def producto(f, g):
    return integrate(f[0]*g[0]*sqrt(1-t**2), (t, a, b))

#Realizamos el proceso de ortogonalización de Gram-Schmidt

ortogonales = []
for v in base:
    u = v
    for o in ortogonales:
        u -= (producto(v,o) / producto(o,o)) * o
    
    ortogonales.append(u)

#Resultado

FiniteSet(*ortogonales)
print(FiniteSet(*ortogonales))
