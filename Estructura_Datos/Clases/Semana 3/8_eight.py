# Una empresa tiene dos turnos ( mañana y tarde) en los que trabajan 8 empleados ( 4 por la mañana y 4 por la tarde) confeccionar un programa qu epermita almacenar los sueldos de los empleados agrupados en dos listas. imprimir las dos listas de sueldos.

sueldo_mañana = []
sueldo_tarde = []

print("Turnos por la mañana")
for i in range(4):
    sueldo_inp = float(input("Ingrese el sueldo del empleado: "))
    sueldo_mañana.append(sueldo_inp)

print("Turnos por la tarde")
for i in range(4):
    sueldo_inp = float(input("Ingrese el sueldo del empleado: "))
    sueldo_tarde.append(sueldo_inp)

print("\nLista de sueldos mañana")
print(sueldo_mañana)
print("\nLista de sueldos tarde")
print(sueldo_tarde)
