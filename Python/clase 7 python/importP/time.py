import time


def cuenta_regresiva(t):
    while t != 0:
        mins, secs = divmod(t,60)
        timer = "{:02d}:{:02d}".format(mins,secs) #:02d es para poner un decimal de dos posiciones
        print(timer, end="\r") # \r es para que todo sea en una sola linea
        time.sleep(1) #se detiene un segundo, 
        t = t - 1
        
        
t = int(input("ingrese un tiempo en segundos: "))
cuenta_regresiva(t)