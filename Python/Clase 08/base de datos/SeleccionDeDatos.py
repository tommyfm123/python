import sqlite3 as sql

# establecer conexión a la base de datos
conn = sql.connect("universidad.db")
cursor = conn.cursor()

# ejecutar consulta SQL SELECT para obtener todos los registros de la tabla alumnos
cursor.execute("SELECT * FROM alumnos")

# recuperar los datos seleccionados
datos = cursor.fetchall()

# imprimir los datos seleccionados
for fila in datos:
    print(fila)

# cerrar conexión
conn.close()


# ESTO IMPRIME TODA LA TABLA