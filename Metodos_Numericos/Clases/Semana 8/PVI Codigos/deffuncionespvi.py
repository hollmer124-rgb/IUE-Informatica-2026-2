"""
Módulo en el que se definen las funciones que se utilizan
en los métodos de solución de PVIs.
* funced: función presente en la ecuación diferencial.
* funcsolex: solución exacta del PVI en caso de existir.
"""

import numpy as np
from scipy.integrate import solve_ivp

# Función f de la EDO (y' = f(t,y)) 
def funced(t,y):
    # yder = t**2 - 4*y
    yder = 1+ y**2+t**3
    return yder

# Derivada de funcraiz
def funcsolex(t):
    y = 31*np.exp(-4*t)/32 + t**2/4 - t/8 + 1/32
    return y

# Solución de referencia del PVI
def funcsolref(t_0, T, y_0):
    sol = solve_ivp(lambda t, y: y*t**3 - 1.1*y, [t_0, T], [y_0], rtol = 1e-10)
    return sol