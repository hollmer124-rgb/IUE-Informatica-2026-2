#cargar por teclado y alcmacenar en una lista las alturas de 5 personas (valores float) obtener el promedio de las mismas. Contar cuantas personas son mas altas que el promedio y cuantas mas bajas

alturas = []
total_suma = 0


for i in range(5):
    alturas_inp = float(input(f"Ingrese la altura de la persona {i + 1}: "))
    total_suma += alturas_inp
    alturas.append(alturas_inp)

promedio_alt = total_suma / 5
print(promedio_alt)
print(alturas)
cant_bajas_prom = 0
cant_altas_prom = 0
for x in range(len(alturas)):
    if alturas[x] < promedio_alt:
        cant_bajas_prom += 1
    elif alturas[x] > promedio_alt:
        cant_altas_prom += 1
    

print(f"La cantidad de personas mas altas que el promedio es: {cant_altas_prom}")

print(f"La cantidad de personas mas bajas del promedio es: {cant_bajas_prom}")
