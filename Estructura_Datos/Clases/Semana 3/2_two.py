# Definir una lista por asignación con 5 enteros. Mostrar por pantalla solo los elementos con valor iguales o superiores a 7.
lista = [2, 7, 10, 20, 55]
print("Los valores de la lista son:")
print(lista)
print("Los valores mayores o iguales a 7 son: ")
i = 0
while i < len(lista):
    if lista[i] >= 7:
        print(lista[i])
    i += 1
