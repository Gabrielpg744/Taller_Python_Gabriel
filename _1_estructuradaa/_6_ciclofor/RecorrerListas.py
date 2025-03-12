if __name__ == '__main__':
    print("--------------------------------------------------")
    lista=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,"Gaboo"]

    lista.append("Jijija")
    lista.append(False)
    lista.append(777)
    lista.append(2.69)#.append agrega elementos al arreglo

    lista2=[777,888,999,2222]
    lista.append(lista2)

    for elemento in lista:
        print(elemento)

    nombre:str
    nombre="Luis"
    nombre+=" Gutierrez"
    nombre.join("Gutierrez")#no agarra
    print(nombre)

    print("JUNTO")
    lista3=["Federico", "Pablo", "Karla"]
    cadena:str=" - ".join(lista3)
    print(cadena)

    print("SEPARADO")
    separado=cadena.split()
    for dato in separado:
        print(dato)
    """lista3=[17,18,19,20]
    lista.extend(lista3)"""