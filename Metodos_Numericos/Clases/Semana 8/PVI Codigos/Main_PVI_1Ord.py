'''
Código construido para solucionar un PVI conformado 
por una EDO de primer orden de la forma y'=f(t,y) y 
condiciones iniciales y(t_0)=y_0. Este código implementa 
los métodos de Euler, Heun, Punto Medio y Runge-Kutta 
de 4to orden. Los métodos de Heun y Punto Medio surgen
de procesos de mejoramiento en el método de Euler.
'''

import numpy as np
import met_solpvi_1ord as pvim
import deffuncionespvi as dfp
import matplotlib.pyplot as plt

# Información de entrada
# Condiciones iniciales
t_0 = 0.
y_0 = -4
# Punto final del intervalo de solución
T = 2
# Tamaño de paso
hp = 0.1

# Calculo del número de pasos (ó número de iteraciones)
nit = int((T - t_0)/hp)
print(nit)

# Solución con el método de Euler
teu, yeu = pvim.euler_meth(t_0,y_0,nit,hp)
the, yhe = pvim.heun_meth(t_0,y_0,nit,hp)
tptom, yptom = pvim.ptomed_meth(t_0,y_0,nit,hp)
trk4, yrk4 = pvim.rk4_meth(t_0,y_0,nit,hp)

# Gráficas
# Cantidad de puntos en la gráfica
cpg = 200
# Generación de puntos en el intervalo [t_0,T]
t_v = np.linspace(t_0,T,cpg)

plt.figure()
# plt.plot(t_v, dfp.funcsolex(t_v), 'k', label='Solución exacta')
plt.plot(dfp.funcsolref(t_0, T, y_0).t, dfp.funcsolref(t_0, T, y_0).y[0], 'r', label='Solución de referencia (solve_ivp)')
plt.plot(teu, yeu,'--o',label='Método de Euler')
plt.plot(the, yhe,'--*',label='Método de Heun')
plt.plot(tptom, yptom,'--s',label='Método de Punto Medio')
plt.plot(trk4, yrk4,'--d',label='Método de Runge-Kutta 4to orden')
plt.xlabel('t')
plt.ylabel('y(t)')
plt.legend()
plt.title('Soluciones numéricas del PVI planteado')
plt.show()