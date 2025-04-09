class Auto:#Atributos clase auto
    marca="Honda"
    modelo=1000
    placa="PCH-96-04"

if __name__=="__main__":
    taxi=Auto()#Instancia de clase auto
    miauto=Auto()

    print(taxi.placa)#se invoca uno de los atributos de la clase

    #Cambio de placa solo para miauto
    miauto.placa="TCV-963-12"
    print(miauto.placa)

