import sqlite3 as sql

# establecer conexión a la base de datos
conn = sql.connect("universidad.db")
cursor = conn.cursor()

# ejecutar consulta SQL SELECT para obtener los datos de un alumno específico
legajo = 3 # -------> aca pongo el legajo especifico
cursor.execute("SELECT * FROM alumnos WHERE legajo = ?", (legajo,))

# recuperar los datos seleccionados
datos = cursor.fetchone()

# imprimir los datos seleccionados
print(datos)

# cerrar conexión
conn.close()
