cadena = "hola a todos buenas tardes curso"

print(cadena.split("a")) 
print(cadena.split("a")[-1]) # el -1 muestra la ultima palabra

#esto separa la cadena , y por otro lado quita todas las letras 'a'

lista = ["tomas fernandez murga" , "felipe majul" , "agustin Perez Farhat"]

lista.sort(reverse=False)

# lista.sort(key=lambda nombre:nombre.split()[-1]) 
# #imprime los nombres ordenados alfabeticamente

print(lista)