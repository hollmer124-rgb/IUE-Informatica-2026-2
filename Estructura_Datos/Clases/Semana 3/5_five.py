# Realizar la carga de valores enteros por teclado, almacenarlos en una lista. Finalizar la carga de enteros al ingresar el cero. Mostrar finalmente el tamaño de la lista. 

lista = []

bandera = True
while bandera:
    val_ent = int(input('Ingrese un valor (0 para finaliz  ar): '))
    if val_ent != 0:
        lista.append(val_ent)
    else: 
        bandera = False

print('La lista generada es: ')
print(lista)
print(f'El tamnano de la lista es: {len(lista)}')