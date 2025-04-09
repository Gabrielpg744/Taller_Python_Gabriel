class ListaDatos:

    def __init__(self,matricula:str,estudiante:str,asignatura:str):
        self.matricula = matricula
        self.estudiante = estudiante
        self.asignatura = asignatura

if __name__ =='__main__':
    lista=[]#instanciar
    lista.append(ListaDatos("32345","Juan","Español"))
    lista.append(ListaDatos("12545","Juan2","POO"))
    lista.append(ListaDatos("14345","Juan3","MetodosNumericos"))
    lista.append(ListaDatos("12245","Juan4","Web"))

    for obj in lista:
        print(f"Matricula es: {obj.matricula}")
        print(f"Nombre es: {obj.estudiante}")
        print(f"Asignatura es: {obj.asignatura}")
        print("____________________________________-")

