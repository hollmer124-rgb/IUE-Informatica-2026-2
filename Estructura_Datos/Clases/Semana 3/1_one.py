# Definir por asignación una lista con 8 elementos enteros. Contar cuantos de dichos valores almacenan un valor superior a 100

lista = [25, 500, 223, 25, 893, 126, 168, 92]
print("La lista esta constituida por los valores: ")
print(lista)
cant_valores_superiores = 0

for i in lista:
    if i > 100:
        cant_valores_superiores += 1
        print(f"{i} es mayor que 100")

    else:
        print(f"{i} no es mayor que 100")

print(f"La cantidad de numeros mayores a 100 es: {cant_valores_superiores}")
