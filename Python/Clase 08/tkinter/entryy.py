from tkinter import *
from tkinter.font import BOLD

window = Tk()
window.geometry("500x400")
window.title("mi primer ventana")

lbl_nombre = Label(window, text="ingrese su nombre", font=("Arial",25,BOLD))
txt_nombre = Entry(window, width=50)
lbl_apellido = Label(window, text="ingrese su Apellido", font=("Arial",25,BOLD))
txt_apellido = Entry(window, width=50)
lbl_numero = Label(window, text="ingrese su Numero", font=("Arial",25,BOLD))
txt_numero = Entry(window, width=50)
btn_enviar = Button(window, text="Enviar")

lbl_nombre.pack()
txt_nombre.pack()
lbl_apellido.pack()
txt_apellido.pack()
lbl_numero.pack()
txt_numero.pack()
btn_enviar.pack()

def saludar():
    saludo = "Bienvenido Sr." + txt_nombre.get() + ". Mi nombre es J.A.R.V.I.S"
    lbl_nombre.config(text=saludo)
    cantidad = len(txt_nombre.get())
    txt_nombre.delete(0,END)

btn_saludo = Button(window, text="Saludo", command=saludar)
btn_saludo.pack()

window.mainloop()
