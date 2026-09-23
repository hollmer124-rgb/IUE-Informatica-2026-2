'''
Módulo que contiene las funciones que implementan los métodos de solución de problemas de valores iniciales (PVI) para ecuaciones diferenciales ordinarias (EDO) de primer orden.
'''

import numpy as np
import deffuncionespvi as dfp

# Método de Euler
def euler_meth(t0,y0,n,h):
    # t0: Valor inicial del intervalo (float)
    # y0: Valor inicial de la solución (float).
    # n: Número de pasos (int).
    # h: Tamaño del paso (float).
    # t: Arreglo con los valores de t (numpy array).
    # y: Arreglo con los valores aproximados de la solución (numpy array).

    t = np.zeros(n+1)
    y = np.zeros(n+1)
    t[0] = t0
    y[0] = y0
    for i in range(n):
        y[i+1] = y[i] + h*dfp.funced(t[i], y[i])
        t[i+1] = t[i] + h
    return t,y

# Método de Heun
def heun_meth(t0,y0,n,h):
    # t0: Valor inicial del intervalo (float)
    # y0: Valor inicial de la solución (float).
    # n: Número de pasos (int).
    # h: Tamaño del paso (float).
    # t: Arreglo con los valores de t (numpy array).
    # y: Arreglo con los valores aproximados de la solución (numpy array).

    t = np.zeros(n+1)
    y = np.zeros(n+1)
    t[0] = t0
    y[0] = y0
    for i in range(n):
        yaux = y[i] + h*dfp.funced(t[i], y[i])
        t[i+1] = t[i] + h
        pend = (dfp.funced(t[i], y[i]) + dfp.funced(t[i+1], yaux))/2.0
        y[i+1] = y[i] + h*pend
    return t,y

# Método del Punto Medio
def ptomed_meth(t0,y0,n,h):
    # t0: Valor inicial del intervalo (float)
    # y0: Valor inicial de la solución (float).
    # n: Número de pasos (int).
    # h: Tamaño del paso (float).
    # t: Arreglo con los valores de t (numpy array).
    # y: Arreglo con los valores aproximados de la solución (numpy array).

    t = np.zeros(n+1)
    y = np.zeros(n+1)
    t[0] = t0
    y[0] = y0
    for i in range(n):
        yaux = y[i] + h*dfp.funced(t[i], y[i])/2.0
        taux = t[i] + 0.5*h
        y[i+1] = y[i] + h*dfp.funced(taux, yaux)
        t[i+1] = t[i] + h
    return t,y

# Método de Runge-Kutta de 4to orden
def rk4_meth(t0,y0,n,h):
    # t0: Valor inicial del intervalo (float)
    # y0: Valor inicial de la solución (float).
    # n: Número de pasos (int).
    # h: Tamaño del paso (float).
    # t: Arreglo con los valores de t (numpy array).
    # y: Arreglo con los valores aproximados de la solución (numpy array).
    t = np.zeros(n+1)
    y = np.zeros(n+1)
    t[0] = t0
    y[0] = y0
    for i in range(n):
        k1 = dfp.funced(t[i],y[i])
        k2 = dfp.funced(t[i] + h/2, y[i] + k1*h/2)
        k3 = dfp.funced(t[i] + h/2, y[i] + k2*h/2)
        k4 = dfp.funced(t[i] + h,y[i] + k3*h)
        m = (k1 + 2*k2 + 2*k3 + k4)/6
        y[i+1] = y[i] + m*h
        t[i+1] = t[i] + h
    return t,y