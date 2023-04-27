import tkinter as tk

windows = tk.Tk()

windows.geometry("500x500+200+120")

lbl_nombre = tk.Label(windows, text="nombre")
lbl_apellido = tk.Label(windows, text="Apellido")
lbl_dni = tk.Label(windows, text="DNI")

lbl_nombre.pack(side=tk.RIGHT)
lbl_apellido.pack(side=tk.LEFT)
lbl_dni.pack(side="top")

windows.mainloop()
