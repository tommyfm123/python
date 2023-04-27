import tkinter as tk

windows = tk.Tk()

windows.geometry("500x500+200+120")

lbl_nombre = tk.Label(windows, text="nombre")
lbl_apellido = tk.Label(windows, text="Apellido")
lbl_dni = tk.Label(windows, text="DNI")

lbl_nombre.place(x=20 , y=5)
lbl_apellido.place(x=60, y=55)
lbl_dni.place(x=160, y=220)

windows.mainloop()
