if __name__ == '__main__':
    nom=str(input("ingresa tu nombre: "))
    nom2=str(input("ingresa otro nombre: "))

    n=len(nom)
    n1=len(nom2)

    if n>n1:
        print(f"El nombre 1 es mayor {nom} con {n} letras")
    else:
        if n==n1:
            print(f"Los nombres son iguales")
        else:
            print(f"El nombre mayor es {nom2} con {n1} letras")
