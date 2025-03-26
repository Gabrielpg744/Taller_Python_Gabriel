if __name__ == '__main__':
    #usar tupla como clave de diccionario
    """diccionario = {
        ('id','int'):'2',
        'nombre':'Juan',
        'apellido':'Gutierrez'
    }"""
    diccionario={}

    #agregar tupla como clave
    diccionario[("Ana",25)]="Estudiante"
    diccionario[("Luis",30)]="Ingeniero"
    diccionario[("Carlos",40)]="Abogado"

    #acceder a los valores del diccionario usando la tupla como clave
    ocupacion_ana = diccionario[("Ana",25)]
    ocupacion_luis=diccionario[("Luis",30)]
    print(f"Ana es:{ocupacion_ana}")
    print(f"Luis es:{ocupacion_luis}")


