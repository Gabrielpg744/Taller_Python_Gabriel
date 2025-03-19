def suma(a,b):
    return a+b

def listas(lista:list)->list:
    return sum(lista)


if __name__ == '__main__':
    print(f"La suma es: {suma(15,22)}")
    lista=[1,2,3,4,5]
    print(f"La suma de arreglo es: {listas(lista)}")
