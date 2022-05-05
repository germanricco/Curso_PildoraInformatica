# Video 20: Instruccion yield from
#Es una instruccion que simplifica el codigo del generador en el caso de tener bucles anidados


#Creo la funcion generadora
#Al colocar asterisco antes del argumento de una funcion indicamos que va a recibir un num indeterminado de elementos y ademas que los va a recibir en forma de tupla
def devuelve_ciudades(*ciudades):
    for elemento in ciudades:
        yield elemento

ciudades_devueltas=devuelve_ciudades("Buenos Aires", "Mendoza", "Cordoba", "Tierra del fuego")

print(next(ciudades_devueltas))

print(next(ciudades_devueltas))

#Hasta aca lo mismo que habiamos echo antes. Pero que pasa si ahora quiero acceder a los subelementos de cada elemento
#por ejemplo, el elemento "Buenos Aires" esta compuesto a la vez de subelementos (las letras), que puedo acceder con bucles anidados...
def devuelve_ciudades2(*ciudades):
    for elemento2 in ciudades:
        #for subelemento in elemento2:
        #    yield subelemento
        yield from elemento2  #Uso yield from para simplificar el bucle anidado

ciudades_devueltas2=devuelve_ciudades2("Buenos Aires", "Mendoza", "Cordoba", "Tierra del fuego")

print(next(ciudades_devueltas2))
print(next(ciudades_devueltas2))
print(next(ciudades_devueltas2))