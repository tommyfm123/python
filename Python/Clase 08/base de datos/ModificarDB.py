import sqlite3 as sql

# establecer conexión a la base de datos
conn = sql.connect("universidad.db")
cursor = conn.cursor()

# ejecutar consulta SQL UPDATE para modificar datos en la tabla
cursor.execute("UPDATE alumnos SET dni=?, apellido=?, nombre=? WHERE legajo=?", ("45678009", "Majul", "Felipe", 2))
#En este caso, estamos actualizando las filas donde el legajo es igual a 2.

# confirmar cambios en la base de datos
conn.commit()

# cerrar conexión
conn.close()

print("Datos modificados correctamente")