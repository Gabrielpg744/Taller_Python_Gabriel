class Datos:

    #constructor
    def __init__(self,nombre,correo,whatsapp):
        self.nombre=nombre
        self.correo=correo
        self.whatsapp=whatsapp#apuntador self que es como this

    def setNombre(self,nombre:str):
        self.nombre=nombre

if __name__ == '__main__':
    datos=Datos('Gabriel','holaa@gmail.com0', '248884511200')

    print(datos.nombre)#Imprime el del constructor
    datos.setNombre("Gabo")#modifica
    print(datos.nombre)#Imprime lo modificado
    datos.nombre="Gaboo"
    print(datos.nombre)