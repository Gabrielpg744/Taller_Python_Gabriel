import sys

if __name__ == '__main__':
    print("rango de 0 a 9")
    for i in range(10):
        print(f"{i}")

    print("rango de 6 a 11")
    for i in range(6,12):
        print(f"{i}")

    print("rango de 6 a 11 pero con incremento de 3")
    for i in range(6,12,3):
        print(f"{i}", end=" ")

    sys.stdout.write("Texto sin salto de lineaa")