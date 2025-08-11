import sympy
from sympy import *

# Defino funciones necesarias para los cálculos
def magnitud(v):
    return sqrt(v.dot(v))

def angulo(v1, v2):
    return N(acos(v1.dot(v2) / (magnitud(v1) * magnitud(v2))) * 180/pi)

def proyeccion(u, v):
    return N((u.dot(v) / v.dot(v)) * v)

# Vectores base
e1 = Matrix([1, 0, 0])
e2 = Matrix([0, 1, 0])
e3 = Matrix([0, 0, 1])

# Vectores dados
a = e1 + 2*e2 + 3*e3
b = 4*e1 + 5*e2 + 6*e3
c = 3*e1 + 2*e2 + 1*e3
d = 6*e1 + 5*e2 + 4*e3

# (a) Sumas
print("(a)")
print(N(a + b + c + d))
print(N(a + b - c - d))
print(N(a - b + c - d))
print(N(-a + b - c + d))

# (b) Ángulos con e1, e2, e3
print("\n(b)")
print(angulo(a, e1), angulo(a, e2), angulo(a, e3))
print(angulo(b, e1), angulo(b, e2), angulo(b, e3))
print(angulo(c, e1), angulo(c, e2), angulo(c, e3))
print(angulo(d, e1), angulo(d, e2), angulo(d, e3))

# (c) Magnitudes
print("\n(c)")
print(N(magnitud(a)))
print(N(magnitud(b)))
print(N(magnitud(c)))
print(N(magnitud(d)))

# (d) Ángulo entre a y b, y entre c y d
print("\n(d)")
print(angulo(a, b))
print(angulo(c, d))

# (e) Proyección de a sobre b
print("\n(e)")
print(proyeccion(a, b))

# (f) Coplanaridad
print("\n(f)")
print(simplify(a.dot(b.cross(c))) == 0 and simplify(a.dot(b.cross(d))) == 0)

# (g) (a + b) · (c + d)
print("\n(g)")
print(N((a + b).dot(c + d)))

# (h) Productos cruz y ángulos con d
print("\n(h)")
axb = a.cross(b)
bxc = b.cross(c)
cxd = c.cross(d)
print(N(axb), angulo(axb, d))
print(N(bxc), angulo(bxc, d))
print(N(cxd), angulo(cxd, d))

# (i) c · (a × b)
print("\n(i)")
print(N(c.dot(a.cross(b))))




