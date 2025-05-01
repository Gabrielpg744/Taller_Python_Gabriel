import mariadb
def conectar_y_consultar():
    try:
        #establecre conexion a la base de datos
        conexion = mariadb.connect(
            host="localhost",
            database="almacen",
            user="root",
            password="",
            port=3306
        )
        print(type(conexion))#muestra el tipo de dato que tiene la conexion
        print("Conexion a la base de datos del servidor Ounus")

        #CREAR UN CURSOR Y EJECUTAR LA CONSULTA
        cursor = conexion.cursor()
        consulta = "SELECT * FROM usuarios"
        cursor.execute(consulta)

        #recuperar y mostrar  resultados
        resultados = cursor.fetchall()
        print("resultado: ", type(resultados))
        print("Datos en la tabla usuario: ")
        for fila in resultados:
            #print(fila)
            print(f"ID: {fila[0]}, \nnombre de usuario: {fila[1]}, \ncorreo electronico: {fila[2]}, \ncontraseña: {fila[3]}, \nid rol: {fila[4]}")

        print("\nDATOS DE ROLES")
        consulta = "SELECT * FROM roles"
        cursor.execute(consulta)

        resultados = cursor.fetchall()
        print("resultado: ", type(resultados))
        print("Datos en la tabla roles: ")
        for fila in resultados:
            # print(fila)
            print(
                f"ID: {fila[0]}, nombre de rol: {fila[1]}")

        print("\nDATOS DE PRIVILEGIOS")
        consulta = "SELECT * FROM privilegios"
        cursor.execute(consulta)

        resultados = cursor.fetchall()
        print("resultado: ", type(resultados))
        print("Datos en la tabla privilegios: ")
        for fila in resultados:
            # print(fila)
            print(
                f"ID: {fila[0]}, titulo privilegiado: {fila[1]}")

        print("\nDATOS DE ROLES_PERMISOS")
        consulta = "SELECT * FROM roles_permisos"
        cursor.execute(consulta)

        resultados = cursor.fetchall()
        print("resultado: ", type(resultados))
        print("Datos en la tabla permisos: ")
        for fila in resultados:
            # print(fila)
            print(
                f"ID rol: {fila[0]}, id privilegio: {fila[1]}, fecha asignacion: {fila[2]}")


    except mariadb.Error as e:
        print(f"Error al conectar la base de datos: {e}")

    finally:
        #cerrar la conexion y el cursos si estan abiertos
        if 'cursor' in locals() and cursor:
            cursor.close()
            print("Conexion cerrada. ")

if __name__ == '__main__':
    conectar_y_consultar()

