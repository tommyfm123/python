import copy

ciudades = ["yerba buena", "tafi del valle", "monteros", "tafi viejo"]
copia_ciudades = copy.copy(ciudades)
ciudades[0] = "San Miguel de Tucuman"
print(ciudades)
print(copia_ciudades)
print(id(ciudades))
print(id(copia_ciudades))

#-------- otra forma de hacerlo es asi --------

print("-------------- otra forma de hacerlo-----------------")

ciudades1 = ["yerba buena", "tafi del valle", "monteros", "tafi viejo"]
copia_ciudades2 = ciudades1.copy()
ciudades1[0] = "San Miguel de Tucuman"
print(ciudades1)
print(copia_ciudades2)
print(id(ciudades1))
print(id(copia_ciudades2))