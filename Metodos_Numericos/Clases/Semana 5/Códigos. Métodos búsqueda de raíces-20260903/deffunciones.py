"""
Módulo en el que se definen las funciones que se utilizan
en los métodos de búsqueda de raíces.
* funcraiz: función a la que se le calculan las raices.
* funcraizder: derivada de funcraiz.
"""

import numpy as np

# Función a la que se le busca la raíz
def funcraiz(x):
    y = np.exp(-x) - x**2
    return y

# Derivada de funcraiz
def funcraizder(x):
    y = -np.exp(-x) - 2*x
    return y