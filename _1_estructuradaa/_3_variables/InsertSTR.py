if __name__ == '__main__':
    palabra: str = "%s"
    lista: list = ["Nombre", "Apellido_paterno", "Usuario", "edad", "correo", "Contrasennia"]

    print(palabra)
    #palabra = palabra * 5
    print(palabra)

    t = len(lista)#Obtiene el total de elementos de una lista
    print(t)

    palabra = palabra * len(lista)
    print(palabra)#Imprime 4 veces hola

    campos = ", ".join(lista)#El espacio es un objeto y con punto llama los metodos
    print(campos)#imprime los campos con espacios y comas

    palabraa = " ,".join(palabra)  # El espacio es un objeto y con punto llama los metodos
    print(palabraa)  # imprime los campos con espacios y comas

    querySQL = f"INSERT INTO tabla ({campos}) VALUES ({palabraa})"
    print(querySQL)


