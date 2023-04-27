n2 = [23, "hola" ,25, True , 1, 12, 23]
print(n2)

n2.append(255) # puedo agregar un valor mas con esto
print(n2)

n2.insert(1,99) #agrega en pos 1 valor 99
print(n2)

n2.pop(4) #elimina valores de la lista. sin valor borra ultimo
print(n2)

n2.reverse() #muestra la lista al revez
print(n2)

n2.remove("hola") #elimina lo que yo ponga . 25, true ,etc....
print(n2)

# ------------ funcion del ---------
del n2[1]
print(n2)

a = 10
b = 20 

print(a,b)

del a #elimina el valor "a" de la memoria
print(a,b)

n2.clear() #vacia la lista
print(n2)