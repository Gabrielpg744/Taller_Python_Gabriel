import statistics as burra
if __name__ == '__main__':
    numeros=[10,20,50,80,90,30,40]

    conteo=0;
    suma=0
    promedio=0
    for valor in numeros:
        suma+=valor#incrementar
        conteo+=1

    promedio=suma/conteo
    print(promedio)


    #opcion medio lenta
    suma=0
    for valor in numeros:
        suma+=valor
    promedio=suma/len(numeros)#tamaño de arreglo
    print("Opcion lenta")
    print(promedio)

    #opcion rapida
    promedio==burra.mean(numeros)#invocamos como si fuera objeto y llama una funcion para calcular numeros en una lista
    print(promedio)
    