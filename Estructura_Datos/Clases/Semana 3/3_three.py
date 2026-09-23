# Definir una lista que almacene por asignación los nombres de 5 personas. Contar cuantos de esos nombres tienen 5 o más caracteres.
lista = ["Luna", 'Leo', "Sofia", "Daniela", "Neymar"]

print('Los valores de la lista son: ')
print(lista)
print('Los nombres con 5 o mas caracteres son: ')

contador = 0 
i = 0 
while i < len(lista):
    if len(lista[i]) >= 5:
        print(lista[i])
        contador += 1
    i += 1

print(f'La cantidad de nombres con 5 o mas caracteres es: {contador}')