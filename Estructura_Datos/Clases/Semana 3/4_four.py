# Backlog de requerimiento
# Definir una lista vacía y luego solicitar la carga de 5 enteros por teclado y añadirlos a la lista. Imprimir la lista generada. 

lista = []

# Variable de iteracion
i = 0
# Bucle para solicitar 5 enteros
while i < 5:
    numero = int(input('Ingrese un numero entero para agregar a la lista: '))
    lista.append(numero)
    i += 1
# Imprimir lista
print('La lista generada es: ')
print(lista)
