'''
Código ecrito para aproximar una raíz, r, de una función f.
El intervalo inicial para los métodos cerrados es [a_0, b_0].
a_0 es la aproximación inicial para los métodos abiertos que 
utilizan una única aproximación, aquellos que requieren dos
aproximaciones inciales utilizan adicionalmente r_.
Este código implementa los siguientes métodos:
1. Bisección
2. Falsa posición
3. Newton
4. Secante
'''

import numpy as np
import deffunciones as deff
import Met_busqraices as metb
import matplotlib.pyplot as plt

# Intervalo inicial (métodos cerrados) ó 
# aproximación inicial (métodos abiertos)
a_0 = 0.0   # Hace las veces de r_0 en los métodos abiertos
b_0 = 1

# Aproximación inicial adicional para aquellos 
# métodos que requieren dos condiciones iniciales
# como el método de la secante
r_ = -0.8

# Tolerancia establecida para la medición del error
tol = 0.0001

# Máximo número de iteraciones
maxit = 50

# Utilización de los métodos de búsqueda de raíces
solb, nitb, erb = metb.biseccion(a_0,b_0,tol,maxit)
solfp, nitfp, erfp = metb.falsapos(a_0,b_0,tol,maxit)
soln, nitn, ern = metb.newton(a_0,tol,maxit)
solsec, nitsec, ersec = metb.secante(r_,a_0,tol,maxit)

# Resultados
print('=======================')
print('Método de Bisección')
print('=======================')
print('Solución obtenida: ',solb)
print('Iteraciones: ',nitb)
print('Error: ',erb)
print('=======================')
print('Método de Falsa posición')
print('=======================')
print('Solución obtenida: ',solfp)
print('Iteraciones: ',nitfp)
print('Error: ',erfp)
print('=======================')
print('Método de Newton')
print('=======================')
print('Solución obtenida: ',soln)
print('Iteraciones: ',nitn)
print('Error: ',ern)
print('=======================')
print('Método de la secante')
print('=======================')
print('Solución obtenida: ',solsec)
print('Iteraciones: ',nitsec)
print('Error: ',ersec)


# Gráficas
# Cantidad de puntos en la gráfica
cpg = 200
# Generación de puntos en el intervalo [a,b]
xg = np.linspace(a_0,b_0,cpg)
# extensión de intervalo [a,b] para graficar eje x
ext = np.abs(b_0 - a_0)*0.2
xeje = np.linspace(a_0 - ext,b_0 + ext,cpg)
ejex = xeje*0
plt.figure()
plt.plot(xg,deff.funcraiz(xg),label='Función dada')
plt.plot(xeje,ejex,'--k')
plt.plot(solb,0,'or',label='Solución bisección')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend()
plt.show()


