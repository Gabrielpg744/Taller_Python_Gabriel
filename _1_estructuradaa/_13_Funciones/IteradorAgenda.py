def extraer(agenda:tuple):
    i:int = 0
    while (i<len(agenda)):
        nombre,correo,tel=agenda[i]
        i+=1
        yield nombre,correo,tel

if __name__ == '__main__':
    agenda=[]
    agenda.append(("Juan","Juan@correo","2481234567"))
    agenda.append(("Jose","Joseee@correo","2481234567"))
    agenda.append(("Jeronimo","Jeronimo@correo","2481234567"))
    agenda.append(("Kike","Kike@correo","2481234567"))
    agenda.append(("Luis","Luis@correo","2481234567"))
    agenda.append(("Miguel","Miguel@correo","2481234567"))
    agenda.append(("Juan","Juana@correo","2481234567"))
    agenda.append(("Gabriel","Gabriel@correo","2481234567"))
    agenda.append(("Juan","Juanga@correo","2481234567"))
    agenda.append(("Jose jose","Juan@correo","2481234567"))

    for a,b,c in extraer(agenda):
        print(f"{a},{b},{c}")
