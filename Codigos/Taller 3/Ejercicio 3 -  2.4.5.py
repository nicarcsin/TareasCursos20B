import sympy
from sympy import *

import numpy as np
import matplotlib.pyplot as plt

# Variables y límites de integración

t = symbols('t')
a, b = -1, 1

# Defino base de monomios

base = [Matrix([1]), Matrix([t]), Matrix([t**2]), Matrix([t**3]), Matrix([t**4]), Matrix([t**5]), Matrix([t**6]), Matrix([t**7]), Matrix([t**8]), Matrix([t**9])]

# Defino producto interno 1 y 2

def producto1(f, g):
    return integrate(f[0]*g[0], (t,a,b))

def producto2(f, g):
    return integrate(f[0]*g[0]*sqrt(1-t**2), (t,a,b))

# Verificar ortogonalidad

ortogonales = True
for i, vi in enumerate(base):
    for j, vj in enumerate(base):
        if j > i:
            resultado1 = producto1(vi,vj)
            print(f"Producto interno 1 entre P{i} y P{j}: {resultado1}")
            if resultado1 != 0:
                ortogonales = False

# Resultado del test de ortogonalidad
# Prueba de que la base no es ortogonal

if ortogonales:
    print("a) El conjunto es ortogonal bajo el producto 1")
else:
    print("a) El conjunto no es ortogonal bajo el producto 1")

# Proceso de ortogonalización bajo producto interno 1

ortogonales1 = []
for v in base:
    u = v
    for o in ortogonales1:
        u -= (producto1(v,o) / producto1(o,o)) * o
    
    ortogonales1.append(u)

#Resultado de ortogonalización bajo producto interno 1

legendre10 = FiniteSet(*[o[0] for o in ortogonales1])
print("b) Polinomios de Legendre:",  legendre10)

# Proceso de ortogonalización bajo producto interno 2

ortogonales2 = []
for v in base:
    u = v
    for o in ortogonales2:
        u -= (producto2(v,o) / producto2(o,o)) * o
    
    ortogonales2.append(u)

#Resultado de ortogonalización bajo producto interno 2

chebyshev10 = FiniteSet(*ortogonales2)
print("c) Polinomios de Chebyshev:", chebyshev10)

# Defino función para aproximar

h = [Matrix([sin(3*t)*(1-t**2)])]

# Hallo los coeficientes en la base de monomios

coef1 = []
for i, vi in enumerate(base):
    c1i = producto1(h,vi) / producto1(vi,vi)

    coef1.append(c1i)

# Construyo la combinación lineal

aproximacion_basemonomios = sum(coef1[i][0]*t**i for i in range(len(coef1)))

# Hallo los coeficientes en la base de polinomios de Legendre

coef2 = []

for i, vi in enumerate(ortogonales1):
    c2i = producto1(h,vi) / producto1(vi,vi)

    coef2.append(c2i)

# Construyo la combinación lineal

aproximacion_legendre = sum(coef2[i][0]*ortogonales1[i][0] for i in range(len(coef2)))

# Hallo los coeficientes en la base de Chebyshev

coef3 = []

for i, vi in enumerate(ortogonales2):
    c3i = producto1(h,vi) / producto1(vi,vi)

    coef3.append(c3i)

# Construyo la aproximación lineal

aproximacion_chebyshev = sum(coef3[i][0]*ortogonales2[i][0] for i in range(len(coef3)))

# Graficamos aproximaciones en monomios y en Legendre

p = plot(aproximacion_basemonomios, aproximacion_legendre, h, (t, -1, 1),show=False)

# Ponemos colores y etiquetamos cada función

p[0].line_color = 'red'
p[0].label = '$Aproximación monomios$'
p[1].line_color = 'blue'
p[1].label = '$Aproximación Legendre$'
p[2].line_color = 'green'
p[2].label = '$Función original$'

# El título de la gráfica y de los ejes

p.title = 'Comparación de aproximaciones: Monomios vs Legendre'
p.xlabel = 'x'
p.ylabel = False

# Agregamos una leyenda

p.legend = True
p.legend_loc = 'upper left'

# Mostramos la gráfica

p.show()

# Graficamos aproximaciones en monomios y en Legendre

p = plot(aproximacion_basemonomios, aproximacion_chebyshev, h, (t, -1, 1),show=False)

# Ponemos colores y etiquetamos cada función

p[0].line_color = 'red'
p[0].label = '$Aproximación monomios$'
p[1].line_color = 'blue'
p[1].label = '$Aproximación Chebyshev$'
p[2].line_color = 'green'
p[2].label = '$Función original$'

# El título de la gráfica y de los ejes

p.title = 'Comparación de aproximaciones: Monomios vs Chebyshev'
p.xlabel = 'x'
p.ylabel = False

# Agregamos una leyenda

p.legend = True
p.legend_loc = 'upper left'

# Mostramos la gráfica

p.show()