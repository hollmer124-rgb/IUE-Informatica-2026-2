# Sistema de Gestion de Inventario para una Perfumeria

class Inv_perfumes:
    def __init__(self):
        self.nombres = []
        self.precios = []
        self.cantidades = []
        self.valor_total = 0
        self.producto_caro = 0

    def validar_datos(self, mensaje, tipo):
        while True: 
            try:
                return tipo(input(mensaje))
            except:
                print("Ingrese un valor valido")

    def cargar_productos(self):
         print("\n-------------------------------------------")
         print("\nSeleccionaste la opcion 1 (Cargar productos)")
         n_productos = self.validar_datos("Ingrese el numero de productos que va a registrar: ", int)
         for i in range(n_productos):
            print(f"\nProducto {i+1}")
            
            nombre = input("Ingrese el nombre del producto: ")
            precio = self.validar_datos("Ingrese el precio del producto: $ ", float)
            cantidad = self.validar_datos("Ingrese la cantidad de productos en stock: ", int)


            self.nombres.append(nombre)
            self.precios.append(precio)
            self.cantidades.append(cantidad)

         print("\nProductos registrados correctamente, volviendo al menu...")
         print("\n-------------------------------------------")

    def ver_inventario(self):
        print("\n-------------------------------------------")
        print("\nSeleccionaste la opcion 2 (Ver inventario completo)")
        if len(self.nombres) > 0:
            for i in range(len(self.nombres)):
                print(f"\nProducto {i+1}")
                print(f"Nombre: {self.nombres[i]}")
                print(f"Precio: $ {self.precios[i]}")
                print(f"Cantidad: {self.cantidades[i]}")
        else: 
            print("No hay productos registrados")
        print("\n-------------------------------------------")

    def stock_critico(self):
        print("\n-------------------------------------------")
        print("\nSeleccionaste la opcion 3 (Ver reporte de stock critico)")
        if len(self.nombres) > 0:
            print("Lista de productos con stock critico\n")
            numeracion = 0
            for i in range(len(self.cantidades)):
                if self.cantidades[i] < 5:
                    numeracion += 1
                    print(f"{numeracion}. {self.nombres[i]} --> {self.cantidades[i]}")
            if numeracion == 0:
                print("No hay productos en stock critico")
        else:
            print("No hay productos registrados")
        print("\n-------------------------------------------")

    def valor_total_inventario(self):
        print("\n-------------------------------------------")
        print("\nSeleccionaste la opcion 4 (Ver valor total del inventario)")
        if len(self.nombres) > 0:            
            for i in range(len(self.precios)):
                self.valor_total += self.precios[i] * self.cantidades[i]
                if self.precios[i] > self.precios[self.producto_caro]:
                    self.producto_caro = i

            print(f"El valor total del inventario es: $ {self.valor_total}")
            print(f"El producto mas caro es: {self.nombres[self.producto_caro]} --> $ {self.precios[self.producto_caro]}")
        else:
            print("No hay productos registrados")
        print("\n-------------------------------------------")

    def interfaz(self):
        print("=======================================")
        print("      BIENVENIDO AL SISTEMA           ")
        print("=======================================")
        while True:
            print("\nNuestro sistema ofrece estas opciones:")
            print("1. Cargar productos")
            print("2. Ver inventario completo")
            print("3. Ver reporte de stock critico")
            print("4. Ver valor total del inventario")
            print("5. Salir")
            opcion = input("Ingrese el numero de la opcion que desea ejecutar: ")

            if opcion == "1":
                self.cargar_productos()
               
            elif opcion == "2":
                self.ver_inventario()

            elif opcion == "3":
                self.stock_critico()

            elif opcion == "4":
                self.valor_total_inventario()

            elif opcion == "5":
                print("\n-------------------------------------------")
                print("      \nSeleccionaste la opcion 5 (Salir)")
                print("         Gracias por usar el programa...")
                print("\n-------------------------------------------")
                break
                
            else: 
                print("\n-------------------------------------------\n")
                print("   Opcion invalida, vuelva a intentarlo   ")
                print("\n-------------------------------------------")

start = Inv_perfumes()
start.interfaz()