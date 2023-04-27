import sqlite3 as sql

# establecer conexión a la base de datos
conn = sql.connect("universidad.db")
cursor = conn.cursor()

# ejecutar consulta SQL DELETE para eliminar datos de la tabla
cursor.execute("DELETE FROM alumnos WHERE legajo=?", (2,))

# confirmar cambios en la base de datos
conn.commit()

# cerrar conexión
conn.close()

print("Datos eliminados correctamente")
