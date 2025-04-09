class ListaDatos:

    def __init__(self,matricula:str,estudiante:str,asignatura:str):
        self.matricula = matricula
        self.estudiante = estudiante
        self.asignatura = asignatura

class ControlEscolar:#Hereda de lista de datos y hace lo mismo al poner la clase enttre parentesis
    def __init__(self):#llama al metodo init y le pasa la lista
        self.lista=[]

    def addEstudiante(self, matricula, estudiante,asignatura):
        self.lista.append(ListaDatos(matricula,estudiante,asignatura))

    def show(self):
        for obj in self.lista:
            print(f"Matricula es: {obj.matricula}")
            print(f"El estudiante es: {obj.estudiante}")
            print(f"Asignatura: {obj.asignatura}")
            print("_____________________________________")

if __name__ =='__main__':
    escolar=ControlEscolar()#Instanciar
    escolar.addEstudiante("1234","Gabriel","EstrDatos")
    escolar.addEstudiante("1234","Gaboo","EstrDatos")
    escolar.addEstudiante("1234","Gabii","Matematicas")
    escolar.addEstudiante("1234","Gabrielll","POO")
    escolar.show()