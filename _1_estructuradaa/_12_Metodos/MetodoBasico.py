import statistics as mate
#def suma(a:int,b:int):
 #   print(f"La suma de {a} + {b} es {a+b}")

def suma(a:int,b:int, c=None):#sobrecarga de metodos por el mismo nombre
    if b is None:
        print(f"Se muestra el valor de {a}")
    else:
        if c is None:
            print(f"La suma de {a} + {b} es: {a + b}")
        else:
            print(f"La suma de {a}+{b}+{c} es: {a + b + c}")

def promedioArreglo(lista):
    lista.append(5,45,56)
    #lista.append(45)
    #lista.append(56)
    p=mate.mean(lista)
    print(f"El promedio de {p} es: {p}")


if __name__ == '__main__':
    #suma(7)
    suma(10,52)
    suma(23,47,45)
    #suma(12)

    lista2=[1,2,3,4,5]
    promedioArreglo(lista2)
    print(lista2)