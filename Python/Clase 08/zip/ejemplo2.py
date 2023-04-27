alumnos = ["Maria", "Jose", "Pedro", "Valentina"]
tps = ["1","2","3","1"]
notas = [7,8,4,9]

for a,t ,n in zip(alumnos,tps,notas):
    print(f" alumno: {a}, TP:{t}, Nota: {n}")
