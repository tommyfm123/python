import tkinter as tk
window = tk.Tk()
window.geometry("500x500") #500x200
window.resizable(True,False)
window.title("mi primer ventana")

var = tk.StringVar()

lbl_nombre = tk.Label(window,
    textvariable=var,
    foreground="red",
    background="yellow")

var.set("texto en variable")
lbl_nombre.pack()

window.mainloop()