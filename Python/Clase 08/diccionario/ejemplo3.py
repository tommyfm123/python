poblacion_paises = {
    'Argentina' : '46 millones de personas',
    'Brasil' : '180 millones de personas',
    'Colombia' : '30 millones de personas',
}

for poblacion in poblacion_paises.keys():
    print(poblacion)
    
for pais in poblacion_paises.values():
    print(pais)
for pais, poblacion in poblacion_paises.items():
    print(pais + "tiene" + poblacion)
    
# .keys() : retorna la clave de nuestro elemento
# .value(): retorna una lista de elementos (valores del diccionario)
# items(): devuelve lista de tuplas (primero la clave y luego el valor)
#.clear(): elimina todos los items del diccionario
# .pop("n"): elimino el elemento ingresado