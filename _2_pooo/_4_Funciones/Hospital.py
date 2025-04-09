class Hospital:
    def __init(self):
        self.__NombrePaciente:str=""#para privtizarlo con doble guion bajo
        self.__nss:int=12345
        self.__enfermedad:str=""

    def getNombrePaciente(self)->str:
        return self.__NombrePaciente

    def getNss(self)->int:
        return self.__nss

   # @property#convierte el metodo en una propiedad de solo lectura solo se coloca en funciones en el return
    def getEnfermedad(self)->str:
        return self.__enfermedad


    #SETS
    def setNombrePaciente(self,nombre:str):
        self.NombrePaciente=nombre

    def setNss(self,ns:int):
        self.ns=ns

    #@setEnfermedad.setter #Esto convierte el metodo en una propiedad de solo lectura
    def setEnfermedad(self,enfermedad:str):
        self.enfermedad=enfermedad


if __name__ == '__main__':
    hospital=Hospital()

    hospital.__NombrePaciente="Juan"
    print(hospital.getNombrePaciente())

    #print(hospital.get)

    #hospital.setEnfermedad("Gripaa")
    #e=hospital.getEnfermedad
    #print(e)