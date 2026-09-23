'''
Módulo que contiene las funciones que implementan los métodos de búsqueda de raíces
'''
import numpy as np
import deffunciones as deff

# Método de la bisección
def biseccion(ei,ed,tol,nmi):
    # ei: extremo izquierdo del intervalo
    # ed: extremo derecho del intervalo
    # tol: tolerancia
    # r: punto medio (aproximación de la raíz)
    # nmi : número máximo de iteraciones
    
    # Iniciación del error
    Error = 1
    
    # Cantidad de iteraciones
    iterac = 0
    
    # Se ejecuta el ciclo mientras el error esté por encima de la tolerancia
    while (Error > tol):
        # Condición que verifica en cada iteración si ei y ed 
        # tienen signos contrarios
        if (deff.funcraiz(ei)*deff.funcraiz(ed)<0):
            # Cálculo del punto medio del intervalo
            r = (ei + ed)/2
            # Condición que verifica si r y ei 
            # tienen signos contrarios
            if (deff.funcraiz(r)*deff.funcraiz(ei) < 0):
                # Si la condición se cumple entonces r 
                # pasa a ser ed en la siguiente iteración
                ed = r
            # Condición que evalúa si r es la raíz buscada
            elif (deff.funcraiz(r) == 0):
                print('La raiz de la función ingresada es: ',r)
            # ei y r tienen el mismo signo por lo que r pasa a ser ei
            else:
                ei = r
        # Si ei*ed es cero entonces uno de los dos extremos es la raíz de la función
        elif (deff.funcraiz(ei)*deff.funcraiz(ed) == 0):
            # Se evalúa la función en ei para validar si es la raíz
            if (deff.funcraiz(ei) == 0):
                print('La raiz de la función ingresada es: ',ei)
            # Si ei no es la raiz entonces ed es la raíz.
            else:
                print('La raiz de la función ingresada es: ',ed)
        # ei*ed > 0 por lo que no se cumplen todas las hipótesis 
        # del teorema del cero intermedio y no es posible utilizar 
        # el método de la bisección
        else:
            print('No es posible asegurar la existencia de una raíz para f en el intervalo ingresado')
        
        Error = abs(deff.funcraiz(r))
        
        # El método de la bisección se detiene 
        # si se alcanza el máximo de iteraciones
        if iterac == nmi:
            print('Se ha alcanzado el máximo de iteraciones')
            break
        iterac += 1
        
    return r, iterac, Error

def falsapos(ei,ed,tol,nmi):
    # ei: extremo izquierdo del intervalo
    # ed: extremo derecho del intervalo
    # tol: tolerancia
    # r: punto de corte entre el segmento 
    #    que aproxima la función y el eje x 
    #    (aproximación de la raíz)
    # nmi : número máximo de iteraciones
    
    # Iniciación del error
    Error = 1
    
    # Cantidad de iteraciones
    iterac = 0
    while (Error > tol):
        # Condición que verifica en cada iteración si ei y ed 
        # tienen signos contrarios
        if (deff.funcraiz(ei)*deff.funcraiz(ed)<0):
            # Cálculo del punto de corte entre el segmento 
            # que aproxima la función y el eje x
            r = (ei*deff.funcraiz(ed)-ed*deff.funcraiz(ei))/(deff.funcraiz(ed)-deff.funcraiz(ei))
            # Condición que verifica si r y ei 
            # tienen signos contrarios
            if (deff.funcraiz(r)*deff.funcraiz(ei) < 0):
                # Si la condición se cumple entonces r 
                # pasa a ser ed en la siguiente iteración
                ed = r
            # Condición que evalúa si r es la raíz buscada
            elif (deff.funcraiz(r) == 0):
                print('La raiz de la función ingresada es: ',r)
            # ei y r tienen el mismo signo por lo que r pasa a ser ei
            else:
                ei = r
        # Si ei*ed es cero entonces uno de los dos extremos es la raíz de la función
        elif (deff.funcraiz(ei)*deff.funcraiz(ed) == 0):
            # Se evalúa la función en ei para validar si es la raíz
            if (deff.funcraiz(ei) == 0):
                print('La raiz de la función ingresada es: ',ei)
            # Si ei no es la raiz entonces ed es la raíz.
            else:
                print('La raiz de la función ingresada es: ',ed)
        # ei*ed > 0 por lo que no se cumplen todas las hipótesis 
        # del teorema del cero intermedio y no es posible utilizar 
        # el método de la bisección
        else:
            print('No es posible asegurar la existencia de una raíz para f en el intervalo ingresado')
        
        Error = abs(deff.funcraiz(r))
        
        # El método de la falsa posición se detiene 
        # si se alcanza el máximo de iteraciones
        if iterac == nmi:
            print('Se ha alcanzado el máximo de iteraciones')
            break
        iterac += 1
        
    return r, iterac, Error

def newton(r,tol,nmi):
    # r: Recibe la aproximación inicial
    #    y durante la ejecución del método almacena
    #    el punto de corte entre la recta tangente 
    #    a la gráfica de la función y el eje x 
    #    (aproximación de la raíz)
    # tol: tolerancia
    # nmi : número máximo de iteraciones
    
    # Iniciación del error
    Error = 1
    
    # Cantidad de iteraciones
    iterac = 0
    while (Error > tol):
        iterac += 1
        # Se evalúa la derivada de la función en r
        if (deff.funcraizder(r) == 0):
            print('La pendiente de la recta tangente a la curva es cero')
            break
        # Cálculo del punto de corte entre la recta tangente 
        # a la gráfica de la función y el eje x
        else:
            r = r - deff.funcraiz(r)/deff.funcraizder(r)
            
        Error = abs(deff.funcraiz(r))

        # El método de Newton se detiene 
        # si se alcanza el máximo de iteraciones
        if iterac == nmi:
            print('Se ha alcanzado el máximo de iteraciones')
            break
        
    return r, iterac, Error

def secante(r__1,r_0,tol,nmi):
    # r__1, r_0: Aproximaciones iniciales
    # r: Almacena el punto de corte entre la recta secante a la 
    #    gráfica de la función y el eje x (aproximación de la raíz)
    # tol: tolerancia
    # nmi : número máximo de iteraciones

    # Iniciación del error
    Error = 1

    # Cantidad de iteraciones
    iterac = 0
    while (Error > tol):
        iterac += 1
        # Cálculo del punto de corte entre la recta secante 
        # a la gráfica de la función y el eje x
        r = r_0 - deff.funcraiz(r_0)*(r__1 - r_0)/(deff.funcraiz(r__1) - deff.funcraiz(r_0))
        # Actualización de los puntos
        r__1 = r_0
        r_0 = r

        Error = abs(deff.funcraiz(r))
        
        # El método de la secante se detiene 
        # si se alcanza el máximo de iteraciones
        if iterac == nmi:
            print('Se ha alcanzado el máximo de iteraciones')
            break

    return r, iterac, Error
    
    