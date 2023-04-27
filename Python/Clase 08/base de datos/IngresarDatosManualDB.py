import sqlite3 as sql

# establecer conexión a la base de datos
conn = sql.connect("universidad.db")
cursor = conn.cursor()

# definir valores a insertar en la tabla
legajo = 2
dni = "47432345"
apellido = "Carranza"
nombre = "Tiziano"

# ejecutar consulta SQL INSERT para agregar datos a la tabla
cursor.execute("INSERT INTO alumnos VALUES (?,?,?,?)", (legajo, dni, apellido, nombre))

# confirmar cambios en la base de datos
conn.commit()

# cerrar conexión
conn.close()

print("Datos agregados correctamente")
