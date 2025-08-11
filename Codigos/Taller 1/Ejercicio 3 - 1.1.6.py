import sympy as sp
import numpy  as np
from sympy import *

# Vectores que forman el triángulo
a = sp.Matrix([1,0,0])
b = sp.Matrix([0,1,0])
c = sp.Matrix([0,0,np.sqrt(2)])

# Función centroide
def centroide(a,b,c):
    return (a+b+c)/3

R = centroide(a,b,c)
print(R)


