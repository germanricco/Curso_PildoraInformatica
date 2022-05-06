#Video 23: Lanzamiento de excepciones. instruccion Raise para creacion de excepciones propias
#Veremos mas que todo sintaxis para darle utilidad despues

#Programa para evaluar nuestra edad
def evaluaEdad(edad):

    if edad<0: #La idea es que si se introduce una edad negativa, nuestro programa lance una excepcion propia
        raise TypeError("No se permiten edades negativas") #raise - tipo de error - msj personalizado
    if edad<20:
        return "Eres muy joven"
    elif edad<40:
        return "Eres joven"
    elif edad<65:
        return "Eres maduro"
    elif edad<100:
        return "Cuidate"

try: #Al capturar el error que genero, puedo mantener el flujo en el codigo
    print(evaluaEdad(-18))
except TypeError as ErrorPorEdadNegativa:
    print("Error por numero negativo") 

print("El programa ha finalizado")
#TypeError es una clase, se puede crear una clase para al lanzar una excepcion propia ejecutar cierto codigo