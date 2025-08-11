import sympy
from sympy import *

# Parámetro
t = symbols('t', real=True)

# Parametrización de la trayectoria
r = Matrix([cos(t), sin(t)])

# Campo de fuerza F(x,y)
x, y = symbols('x y', real=True)
F = Matrix([ -y/(x**2 + y**2),  x/(x**2 + y**2) ])

F_t = F.subs({x: r[0], y: r[1]})
dr_dt = r.diff(t)
F_dr = F_t.dot(dr_dt)

# (a) Trabajo en contra desde 0 a π (sentido antihorario)
W_a = -integrate(F_dr, (t, 0, pi))

# (b) Trabajo en contra desde 0 a -π (sentido horario)
W_b = -integrate(F_dr, (t, 0, -pi))

print("(a) Trabajo en contra del campo de 0 a π:", W_a)
print("(b) Trabajo en contra del campo de 0 a -π:", W_b)
