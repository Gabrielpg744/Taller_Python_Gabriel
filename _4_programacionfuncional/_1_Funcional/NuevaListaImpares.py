if __name__ == '__main__':
    numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    listaImpares = list(filter(lambda x: x % 2 == 0, numeros))
    listaPares = list(filter(lambda x: x % 2 == 1, numeros))

    print(f"Lista impares son: {listaImpares}")
    print(f"Lista pares son: {listaPares}")

    #listaImparesConPotencia = list(map(lambda z:z**2, lista))
    listaImparesConPotencia = list(map(lambda z: z ** 2, filter(lambda t: t%2 == 1,numeros)))
    print(listaImparesConPotencia)