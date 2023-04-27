import sqlite3 as sql

conn = sql.connect("Formulario.db")
cursor = conn.cursor()
tabla = 'CREATE TABLE clientes (\
         Nombre text,\
         apellido text,\
         DNI int)'

cursor.execute(tabla)
conn.close()
print("tabla creada correctamente")


