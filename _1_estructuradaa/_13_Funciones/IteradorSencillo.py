def ciclo(vueltas:int):
        i:int=0
        while(i<vueltas):
            i+=1
            yield i#parecido a un break me paro me salgo entrego y luego regreso
        #return i

if __name__ == '__main__':
    for valor in ciclo(50):
        print(valor)
    #valor=vueltas=(25)
    #print(f"Vueltas es: {valor}")