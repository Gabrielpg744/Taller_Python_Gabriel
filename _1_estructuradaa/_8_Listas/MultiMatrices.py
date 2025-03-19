if __name__ == '__main__':
    #A=[1,2,3]
     # [4,5,6]

    #B=[-1,0]
     # [0,1]
      #[1,1]

    matrizA=[[1,2,3],
             [4,5,6]]#dos elementos

    matrizB=[[-1,0],
             [0,1],
             [1,1]]#tres elementos

    res=[[0,0],
         [0,0]]

    tamA=len(matrizA)
    tamB=len(matrizB)

    print(f"El tamaño de la matriz A: {tamA}")
    print(f"El tamaño de la matriz B: {tamB}")

    for i in range(len(matrizA)):#recorre la matriz A
        for j in range(len(matrizB[0])):#subelementos
            for k in range(len(matrizB)):
                res[i][j] += matrizA[i][k] * matrizB[k][j]
    print(f"El resultado es: {res}")


