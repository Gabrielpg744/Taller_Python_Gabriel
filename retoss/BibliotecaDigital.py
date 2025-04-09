#EJERCICIO: Desarrolla un programa en python que utilice la poo para registrar un libro (isbn, titulo
# y autor)
#Los atributos debe estar en privado teniendo un constructor para el registro, asi como los
#getters de cada atributo

#En otra clase debera registrar una coleccion de libros en esta clase debe tener add, delete y show
class Libro:
    def __init__(self, isbn:int, titulo:str,autor:str):#constructor privtizado
        self.__isbn: int = isbn
        self.__titulo: str = titulo
        self.__autor: str = autor

    def getIsbn(self)->int:
        return self.__isbn

    def getTitulo(self)->str:
        return self.__titulo

    def getAutor(self)->str:
        return self.__autor


class RegistroLibro:
    def __init__(self):#llama al metodo init y le pasa la lista
        self.listaLibro=[]

    def addLibro(self, isbn, titulo,autor):#AGREGAR
        self.listaLibro.append(Libro(isbn,titulo,autor))

    def show(self):#MOSTRAR
        for obj in self.listaLibro:
            print(f"ISBN es: {obj.getIsbn}")
            print(f"El Titulo es: {obj.getTitulo}")
            print(f"El autor es: {obj.getAutor}")
            print("_____________________________________")

if __name__ == "__main__":
    biblio=RegistroLibro()

    biblio.addLibro(1234,"Blanca Nieves", "Ramon")
    biblio.addLibro(1234,"Blanca Helados", "RamonUno")
    biblio.addLibro(1234,"Blanca Paletas", "RamonDos")

    biblio.show()