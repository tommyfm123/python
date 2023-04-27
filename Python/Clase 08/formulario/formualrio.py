import sqlite3 as sql
from tkinter import *
from tkinter.font import BOLD

window = Tk()
window.geometry("900x500")
window.title("mi primer ventana")

label_nombre = Label(window, text="ingrese su nombre", font=("Arial",25,BOLD))
txt_nombre = Entry(window, width=50)

label_apellido = Label(window, text="ingrese su Apellido", font=("Arial",25,BOLD))
txt_apellido = Entry(window, width=50)

label_DNI = Label(window, text="ingrese su DNI", font=("Arial",25,BOLD))
txt_DNI = Entry(window, width=50)

btn_enviar = Button(window, text="Enviar")

label_nombre.pack()
txt_nombre.pack()
label_apellido.pack()
txt_apellido.pack()
label_DNI.pack()
txt_DNI.pack()
btn_enviar.pack()

window.mainloop()


# definir función para insertar datos en la tabla de la base de datos
def insert_data(nombre, apellido, DNI):
    
    # establecer conexión a la base de datos
    conn = sql.connect("Formulario.db")
    cursor = conn.cursor()

    # ejecutar consulta SQL INSERT para agregar datos a la tabla
    cursor.execute("INSERT INTO alumnos (nombre, apellido, dni) VALUES (?, ?, ?)", (nombre, apellido, DNI))

    # confirmar cambios en la base de datos
    conn.commit()

    # cerrar conexión
    conn.close()

    print("Datos agregados correctamente")

def insertar():
    btn_enviar = Button(window, text="Enviar")
    btn_enviar.configure(command=insertar)
    nombre = txt_nombre.get()
    apellido = txt_apellido.get()
    DNI = txt_DNI.get()
    insert_data(nombre, apellido, DNI)


