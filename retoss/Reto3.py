libros = []#Diccionario de libros y usuarios
usuarios = {}


def agregar_libro():
    print("AGREGAR LIRBO")
    titulo = input("Título: ")
    autor = input("Autor: ")
    genero = input("Género: ")
    copias = int(input("Número de copias disponibles: "))

    nuevo_libro = {
        'titulo': titulo,
        'autor': autor,
        'genero': genero,
        'copias': copias,
        'prestados': 0
    }

    libros.append(nuevo_libro)
    print(f"El libro '{titulo}' se ha agregado")


def buscar_libros():
    print("BUSCAR LIBROS: ")
    print("Buscar por:")
    print("1. Título libro")
    print("2. Autor")
    print("3. Género")
    opcion = input("Elige una opción: ")

    if opcion == '1':
        busqueda = input("Ingresa el título: ")
        for libro in libros:
            if busqueda.lower() in libro['titulo'].lower():
                mostrar_info_libro(libro)

    elif opcion == '2':
        busqueda = input("Ingresa el autor: ")
        for libro in libros:
            if busqueda.lower() in libro['autor'].lower():
                mostrar_info_libro(libro)

    elif opcion == '3':
        busqueda = input("Ingresa el género: ")
        for libro in libros:
            if busqueda.lower() in libro['genero'].lower():
                mostrar_info_libro(libro)

    else:
        print("Opción no válida")


def mostrar_info_libro(libro):
    disponibles = libro['copias'] - libro['prestados']
    print(f"Título: {libro['titulo']}")
    print(f"Autor: {libro['autor']}")
    print(f"Género: {libro['genero']}")
    print(f"Disponibles: {disponibles}/{libro['copias']}")


def prestar_libro():
    print("--- Prestar Libro ---")
    usuario = input("Nombre de usuario: ")
    titulo = input("Título del libro a prestar: ")


    if usuario not in usuarios:
        usuarios[usuario] = []


    for libro in libros:
        if libro['titulo'].lower() == titulo.lower():
            disponibles = libro['copias'] - libro['prestados']
            if disponibles > 0:
                libro['prestados'] += 1
                usuarios[usuario].append(libro['titulo'])
                print(f"Libro prestado a {usuario}")
                return
            else:
                print("No hay copias disponibles")
                return

    print("Libro no encontrado")


def devolver_libro():
    print("--- Devolver Libro ---")
    usuario = input("Nombre de usuario: ")
    titulo = input("Título del libro a devolver: ")

    if usuario not in usuarios:
        print("Usuario no encontrado")
        return

    if titulo not in usuarios[usuario]:
        print("Este usuario no tiene ese libro prestado")
        return


    for libro in libros:
        if libro['titulo'].lower() == titulo.lower():
            libro['prestados'] -= 1
            usuarios[usuario].remove(titulo)
            print("Libro devuelto correctamente")
            return

    print("Error libro no encontrado")


def mostrar_libros():

    print("--- Libros Disponibles ---")
    if not libros:
        print("No hay libros en la biblioteca")
        return

    for libro in libros:
        disponibles = libro['copias'] - libro['prestados']
        if disponibles > 0:
            mostrar_info_libro(libro)


def menu():

    while True:
        print("=== BIBLIOTECA ===")
        print("1. Agregar libro")
        print("2. Buscar libro")
        print("3. Prestar libro")
        print("4. Devolver libro")
        print("5. Mostrar libros disponibles")
        print("6. Salir")

        opcion = input("Elige una opción (1-6): ")

        if opcion == '1':
            agregar_libro()
        elif opcion == '2':
            buscar_libros()
        elif opcion == '3':
            prestar_libro()
        elif opcion == '4':
            devolver_libro()
        elif opcion == '5':
            mostrar_libros()
        elif opcion == '6':
            print("Hasta luego")
            break
        else:
            print("Opción no válida intenta de nuevo")


libros.append({
    'titulo': 'El Principito',
    'autor': 'Antoine de Saint-Exupéry',
    'genero': 'Infantil',
    'copias': 5,
    'prestados': 0
})

libros.append({
    'titulo': 'Blanca nieves',
    'autor': 'Walt',
    'genero': 'Infantil',
    'copias': 3,
    'prestados': 0
})


if __name__ == '__main__':
    menu()