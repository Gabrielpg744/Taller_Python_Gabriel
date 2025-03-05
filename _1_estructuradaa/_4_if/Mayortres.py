if __name__ == '__main__':
    a=int(input("Proporciona un numero: "))
    b=int(input("Proporciona otro numero: "))
    c=int(input("Proporciona un ultimo numero: "))

    if a>b:
        if a>c:
            print(f"Entre a y c el mayor es: {a}")
        else:
            print(f"Entre a y c mayor es: {c}")
    else:
        if b > c:
            print(f"Entre b y c el mayor es: {b}")
        else:
            print(f"Entre b y c el mayor es: {c}")