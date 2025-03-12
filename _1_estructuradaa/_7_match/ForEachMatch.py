import sys
from unittest import case

if __name__ == '__main__':
    lista=[1,5,6,7,8,1,9,7,7,6,5,3,3,1,1,5,8,8,3,7]
    totales = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    adoptados: int = 0
    for elemento in lista:

        #totales[2]+=1

        match elemento:
            case 1:totales[0]+=1
            case 2:totales[1]+=1
            case 3:totales[2]+=1
            case 4:totales[3]+=1
            case 5:totales[4]+=1
            case 6:totales[5]+=1
            case 7:totales[6]+1
            case 8:totales[7]+1
            case 9:totales[8]+1
            case 10:totales[9]+1
            case _:adoptados+=1

    i:int=1
    for n in totales:
        print(f"La cantidad de numeros registrados de {i}s son: {n}")
        i+=1

    """j:int=1
    for o in totales:
        print(f"La cantidad de adoptados de {j}s son: {o}")
        j+=1"""