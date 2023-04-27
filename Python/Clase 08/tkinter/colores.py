import tkinter as tk

# creacion de ventana
window = tk.Tk()
window.geometry("500x500") #500x200
window.resizable(True,False)
window.title("mi primer ventana")

#insertacion de texto
lbl_nombre = tk.Label(window,
    text="ingrese su nombre",
    foreground="#F00",
    background="#AADDFF",
    width=15,
    height=15)
lbl_nombre.pack()

window.mainloop()