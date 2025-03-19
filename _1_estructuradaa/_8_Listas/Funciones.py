if __name__ == '__main__':
    miLista=[1,2,3]
    miLista.append(4)#agregar un elemento
    print(end="Agrego: ")
    print(miLista)

    #Añade los elementos a otra lista
    miLista = [1,2,3]
    otraLista = [4,5,6]
    miLista.extend(otraLista)#Fusiona las dos listas en una
    print(end="Unio dos listas: ")
    print(miLista)

    miLista = [1,2,3]
    miLista.insert(1,4)#inserta un elemento en el indice indicado
    print(end="inserta en una posicion especificada: ")
    print(miLista)

    milista = [1,2,3,2]
    miLista.remove(1)#elimina el primer elemento encontrado
    print(end="Borrar")
    print(miLista)

    miLista = [1,2,3]
    elemento=miLista.pop(1)#elimina y devuelve elementos de una posicion especificada
    print(end="POP: ")
    print(elemento)
    print(miLista)

    miLista = ["luis","javier","luis","maria"]
    indice=miLista.index("luis")#devuelve el indice de la primera aparicion
    print(end="Indice: ")
    print(indice)

    milista=[1,2,3,2]
    conteo=miLista.count(2)#devuelve el numero de veces que aparece un valor
    print(end="Count: ")
    print(conteo)

    miLista=[3,1,4,2]
    milista.sort()#ordena los elementos de la lista en forma ascendente
    print(end="Sort: ")
    print(miLista)
    miLista.sort(reverse=True)
    print(end="Sort reverse: ")
    print(miLista)

    milista.reverse()#invierte el orden
    print(end="Reverse: ")
    print(miLista)

    miLista.clear()
    print(end="Clear: ")#borra todo e imprime dos corchetes
    print(miLista)

    miLista=[1,2,3]
    miLista2=miLista
    copiaLista=miLista.copy()
    milista.append(4)
    print(end="Copia: ")

    print(copiaLista)
    print(miLista2)

