from random import choice


def generar_contrasena():
    minusculas = ["a","b","c","d","e","f","g"]
    mayusculas = ["A","B","C","D","E","F","G"]
    numeros = ["1","2","3","4","5","6","7"]
    simbolos = ["_","-","@","%","~","&","*"]
    
    caracteres = minusculas + mayusculas + numeros + simbolos
    
    password = []
    
    for i in range(15):
        caracter_random = choice(caracteres)
        password.append(caracter_random)
        
        password_resultado = "".join(password) #esto une todo
        
    return password_resultado
    
    

def run():
    contrasena = generar_contrasena()
    print(contrasena)


if __name__ == "__main__":
    run()