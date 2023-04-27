import random as rnd

def adivinanza(n):
    numero_aleatorio = rnd.randint(1,n)
    adv = 0 #inicializo variable
    while adv != numero_aleatorio:
        adv = int(input(f"ingrese un numero entre 1 y {20}: ")) 
        if adv < numero_aleatorio:
            print("el numero ingresado es menor que el numero magico")
        if adv > numero_aleatorio:
            print("el numero ingresado es mayor que el numero magico")
        
print(f"el nuemero es :{numero_aleatorio}")
    
adivinanza(20)