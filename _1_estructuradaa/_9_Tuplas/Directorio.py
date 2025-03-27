if __name__ == '__main__':
    agenda={}
    agenda["RFC"]=("Datos","correo","numero")
    agenda["RFCj"]=("Datoss","correoo","numeroo")
    agenda["RFCa"]=("Datosss","correooo","numerooo")
    agenda["RFCl"]=("Datossss","correoooo","numeroooo")

    #extraer
    nombre,correo,numero=agenda["RFC"]

    print(f"El rfc es: {nombre,correo,numero}")
