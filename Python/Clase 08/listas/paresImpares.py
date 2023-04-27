
def ordenarPrimeroLosPares(n):
    lista_aux = []
    lista_par = []
    lista_impar = []
    
    for i in n:
        if i % 2 == 0:
            lista_par.append(i)
            
    for x in n:
        if x % 2 != 0:
            lista_impar.append(x)
    lista_aux = lista_par + lista_impar 
    return lista_par

numeros = [4,5,1,2,9]

# numeros.sort()

lista_resultado = ordenarPrimeroLosPares(numeros)

# print(numeros)

print(lista_resultado)