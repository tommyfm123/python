n2 = [23, "hola" ,25, True , 1, 12, 23]


# for elemento in n2:
#     print(elemento)
#     # print(n2[::-1])
#     print(n2)
    
print("-------------------------")
print("concatenacion de listas")
print("-------------------------")
      
      
n1 = [1,2,3,4,5,6,7]
n3 = [8,9,10,11,12]
    
lista = n1 + n2
print(n1)
print(n2)
print(lista * 6) # multiplica la cantidad de veces que es mostrado el resultado

print(len(n1)) #imprime la longitud de la lista

print(max(n1)) #imprime el numero mayor de n1

print(sum(n1)) #suma todos los valores de la lista

print(n1.count(4)) #muestra cuantas veces se repite un valor

print(4 in n1) # pregunta si existe ese valor en la lista

print(3 not in n1)