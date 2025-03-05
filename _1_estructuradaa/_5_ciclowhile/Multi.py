if __name__ == '__main__':
    x = int(input("Ingresa un numero: "))
    y = int(input("Ingresa otro numero: "))

    i: int = 1
    pot: int = 0

    while i<=y:
        pot=pot+x
        i+=1
    print(f"El resultado de {x} * {y}={pot}")

