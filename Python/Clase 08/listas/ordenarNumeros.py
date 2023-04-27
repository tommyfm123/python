
def ordenarPrimeroLosPares(n):
    lista_aux = []
    for i in n:
        if i % 2 == 0:
            lista_aux.append(i)
            
    for x in n:
        if x % 2 != 0:
            lista_aux.append(x)
            
    return lista_aux

numeros = [4,5,1,2,9]

# numeros.sort()

lista_resultado = ordenarPrimeroLosPares(numeros)

# print(numeros)

print(lista_resultado)