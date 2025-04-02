import json
import sys
RESET = "\033[0m" # Restablece el color a su valor por defecto
# Colores de texto
BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

def extraer():
    with open("Edades.json","r", encoding="utf-8") as archivo:
        datos = json.load(archivo)#carga el contenido de archivo json

    for persona in datos["EdadesBD"]:
        yield (persona["id"],persona["Nombre"],persona["Edad"],persona["RFC"])

if __name__ == '__main__':
        i=1#Se inicializa i que es la variable contadora y luego abajo se incrementa
        #mientras que los colores se declaran de manera global
        for id,Nombre,Edad,RFC in extraer():
            match i:
                case 1:
                    sys.stdout.write(RED)
                case 2:
                    sys.stdout.write(GREEN)
                case 3:
                    sys.stdout.write(BLUE)
                case 4:
                    sys.stdout.write(RESET)
            print(f"Id: {id}")
            print(f"Nombre: {Nombre}")
            print(f"Edad: {Edad}")
            print(f"RFC: {RFC}")
            i+=1

            """if  int(Edad) >=18:
                print("Eres mayor de 18 años")
            else:
                print("No eres mayor a 18 años")
            print("________________________________-")"""
