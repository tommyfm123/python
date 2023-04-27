from tkinter import * 
from tkinter.font import ITALIC

window = Tk()
window.geometry("500x500")
window.title("mi primer ventana")

var = StringVar()

lbl_nombre = Label(window,
    textvariable=var,
    foreground="red",
    background="yellow",
    font="Arial,22,ITALIC")

var.set("Ingrese su nombre")
lbl_nombre.pack()

window.mainloop()