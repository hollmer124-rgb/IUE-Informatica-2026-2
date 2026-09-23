# Almacenar en una lista de sueldos (valores float) de 5 operarios. Imprimir la lista y el promedio de sueldos

sueldos = []
suma = 0

for i in range (5):
    sueldos_inp = float(input(f"Ingrese el saldo del operario {i+1}: "))
    suma += sueldos_inp
    sueldos.append(sueldos_inp)

print(sueldos)
promedio = suma / 5
print(f"El promedio de los sueldos es: {promedio}")

