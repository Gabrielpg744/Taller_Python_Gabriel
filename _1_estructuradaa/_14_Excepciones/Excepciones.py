if __name__ == '__main__':
    try:#codigo que puede usar una excepcion
        numero=int(input("Introduce un numero: "))
        resultado=10/numero
    except ValueError:#manejo de la excepcion si se introduce un valor no valido
        print("Error debes introducir un numero entero")
    except ZeroDivisionError:#manejo de la excepcion si se intenta divir por cero
        print("Error no se puede dividir entre cero")
    else:#se ejecuta si no hubo excepciones
        print("El resultado es: ",resultado)
    finally:#Se ejecuta siemprre haya o no habido excepciones
        print("Fin del programa.")

