import tkinter as tk

# creacion de ventana
gui = tk.Tk()
gui.geometry("500x500") #500x200
gui.resizable(True,False)
gui.title("mi primer ventana")

#insertacion de texto

saludos = tk.Label(gui, text="Bienvenido a mi primera ventana!")
saludos.pack()

gui.mainloop()