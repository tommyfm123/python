ciudades1 = ["yerba buena", "tafi del valle", "monteros"]
ciudades2 = ["yerba buena", "tafi del valle", "monteros"]

print(id(ciudades1)) #posicion en memoria principal
print(id(ciudades2)) #posicion en memoria principal

print("----------------------------------------------------------")

# ---------- copiar contenido ----------


copia_ciudades = ciudades3
ciudades3[0] = "San Miguel de Tucuman"
print(ciudades3)
print(copia_ciudades)
print(id(ciudades3)) #esto es para ver que el id es el mismo
print(id(copia_ciudades)) #esto es para ver que el id es el mismo