# Video 18: Instrucciones Continue, pass y else
# Else tambien tiene el mismo sentido que en bucle if, en for y while

#EXPLICACION DE INSTRUCCION CONTINUE
#Hace saltar a la siguiente iteracion de bucle directamente, ignorando el resto
for letra in "Python":

    if letra == "h":
        continue        
    print(f"Esta leyendo la letra: {letra}")


#Hago programa para contar letras de la variable nombre
nombre = "Pildoras Informaticas"
contador=0
for i in nombre:
    if i == " ": # Sirve para ignorar el espacio, y que cuente el resto de las letras
        continue

    contador+=1  #Es lo mismo que: contador = contador + 1

print(contador)

#EXPLICACION DE INSTRUCCION PASS
#lo que hace es devolver un null, como si el bucle no se ejecutase, o lo mismo para las funciones, para implementar mas tarde

email = input("Introduzca su email por favor: ")

for i in email:
    if i == "@":
        arroba = True
        break
else:                #Else forma parte del bucle for, se va a ejecutar siempre y cuando el bucle ya ha terminado quedando vacio
    arroba = False

print(arroba)
