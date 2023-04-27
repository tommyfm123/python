import sqlite3 as sql

# definir función para insertar datos en la tabla de la base de datos
def insert_data(legajo, dni, apellido, nombre):
    # establecer conexión a la base de datos
    conn = sql.connect("universidad.db")
    cursor = conn.cursor()

    # ejecutar consulta SQL INSERT para agregar datos a la tabla
    cursor.execute("INSERT INTO alumnos VALUES (?, ?, ?, ?)", (legajo, dni, apellido, nombre))

    # confirmar cambios en la base de datos
    conn.commit()

    # cerrar conexión
    conn.close()

    print("Datos agregados correctamente")

# definir función para pedir datos de un nuevo alumno y agregarlos a la base de datos
def alta_de_alumnos():
    print("Alta de Alumnos")
    print("--------------------")
    print()
    leg = int(input("Ingresar el legajo: "))
    dni = int(input("Ingrese su DNI: "))
    ap = input("Ingrese el Apellido: ")
    nom = input("Ingrese el nombre: ")

    insert_data(leg, dni, ap, nom)

# llamar a la función para agregar un nuevo alumno a la base de datos
alta_de_alumnos()

