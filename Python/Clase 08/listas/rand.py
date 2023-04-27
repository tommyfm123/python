import random

lista = []

for i in range(10):
    lista.append(random.randint(0,50)) 
    # esto genera distintos valores aleatoreos
    
for i in lista:
    print(f"{i} - {i*i} - {i**3}")