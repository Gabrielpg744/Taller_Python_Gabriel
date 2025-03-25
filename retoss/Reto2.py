inventario = []

while True:
    print("\nInventario Básico")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Vender producto")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del producto: ").strip().lower()
        cantidad = int(input("Ingrese la cantidad: "))

        encontrado = False
        for producto in inventario:
            if producto[0] == nombre:
                producto[1] += cantidad
                print(f"Se ha actualizado el stock de {nombre}. Nuevo stock: {producto[1]}")
                encontrado = True
                break

        if not encontrado:
            inventario.append([nombre, cantidad])
            print(f"Producto {nombre} agregado con cantidad {cantidad}.")

    elif opcion == "2":
        if not inventario:
            print("El inventario está vacío.")
        else:
            print("\nInventario actual:")
            for producto in inventario:
                print(f"{producto[0].capitalize()}: {producto[1]} unidades")

    elif opcion == "3":
        nombre = input("Ingrese el nombre del producto a vender: ").strip().lower()
        encontrado = False

        for producto in inventario:
            if producto[0] == nombre:
                encontrado = True
                cantidad_vender = int(input(f"Ingrese la cantidad a vender (Stock disponible: {producto[1]}): "))

                if cantidad_vender > producto[1]:
                    print("No hay suficiente stock para la venta.")
                else:
                    producto[1] -= cantidad_vender
                    print(f"Se vendieron {cantidad_vender} unidades de {nombre}. Stock restante: {producto[1]}")
                    if producto[1] == 0:
                        inventario.remove(producto)
                        print(f"{nombre} ha sido eliminado del inventario.")
                break

        if not encontrado:
            print("Producto no encontrado en el inventario.")

    elif opcion == "4":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción no válida. Intente de nuevo.")