if __name__ == '__main__':
    lambdaSuma = lambda x,y: x+y#es el return y se le entrega la funcionalidad a una variable y se convierte en una funcion
    valor1 = int(input("Ingresa un numero: "))
    valor2 = int(input("Ingresa un numero: "))

    suma = lambdaSuma(valor1, valor2)
    print(f"La suma de: {valor1} + {valor2} = {suma}")

