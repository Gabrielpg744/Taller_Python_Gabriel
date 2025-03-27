import json

if __name__ == '__main__':
    #version corta de abrir un archivo Json
    #abre el archivo JSON en modo lectura y with se ecarga de cerrarlo de forma automatica
    with open("Datos.json","r", encoding="utf-8") as archivo:
        datos = json.load(archivo)#carga el contenido de archivo json

        #muestra el contenido de JSON
    for persona in datos["personas"]:
        print("Nombre: ",persona["nombre"])
        print("Edad: ",persona["edad"])
        print("Ciudad: ",persona["ciudad"])
        print("Estado: ",persona["estado"])
        print("________________________________-")
