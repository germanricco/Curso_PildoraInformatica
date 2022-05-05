# Video 17: Bucle While
# Mientras condicion sea verdadera se mantiene en el bucle

#i = 1
#while i<=10: # Mientras i es menor o igual a 10...
#    print(f"Ejecucion numero: {i}")
#    i=i+1


# Programa que pide la edad y verifica que este entre 1 y 100 años
#edad = int(input('Introduce tu edad: '))
#while edad < 0 or edad>100:
#    print("Edad Incorrecta, vuelva a intentarlo")
#    edad = int(input('Introduce tu edad: '))
#print(f"Gracias por colaborar, tu edad es de {edad} años")


# Programa para calcular la raiz cuadrada de un numero
import math
print("Programa de calcul de una raiz cuadrada")
numero = int(input("Introduce un numero por favor: "))

intentos = 0

while numero < 0:
    print("No existe la raiz cuadrada de un numero negativo")

    if intentos == 2:
        print("Has consumidos demasiados intentos, el programa ha finalizado")
        break  #Si el flujo lee el break sale del bucle while instantaneamente
    if numero < 0:
        intentos = intentos+1
    numero = int(input("Introduce un numero por favor: "))



if intentos < 2:
    solucion = math.sqrt(numero)
    print(f"la raiz cuadrada de {numero} es {solucion}")
