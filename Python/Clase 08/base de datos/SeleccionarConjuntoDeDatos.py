import sqlite3 as sql

# establecer conexión a la base de datos
conn = sql.connect("universidad.db")
cursor = conn.cursor()

# ejecutar consulta SQL SELECT para obtener los registros que cumplen la condición
cursor.execute("SELECT * FROM alumnos WHERE dni < 46000000")

# recuperar los datos seleccionados
datos = cursor.fetchall()

# imprimir los datos seleccionados
for fila in datos:
    print(fila)

# cerrar conexión
conn.close()
