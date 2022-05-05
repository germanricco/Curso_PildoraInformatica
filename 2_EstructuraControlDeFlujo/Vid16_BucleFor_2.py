#Video 16: Segunda parte de Bucle For

for i in range(5): #range en este bucle toma los valores 0,1,2,3 y 4
    print(f"valor de la variable {i}")  #Esta funcion de tipo f es una notacion especial que permite concatenar texto con el valor de la variable

for i in range(5,10): #Otra posibilidad es para poner desde el 5 hasta el 9
    print(i)

for i in range(3,31,3):  #comenzar en el 3, terminar en 30 y contar de 3 en 3
    print(i)

#funcion len nos devuelve la longitud de un string
#Vuelvo a hacer ejercicio de validacion de email distinto

valido = False
email=input("Introduce tu email: ")

for i in range(len(email)):  
    if email[i] == "@": #evaluo si en el email en la posicion i es un arroba
        valido = True
if valido:  #Si valido es verdadero...
    print('El email es valido')
else:
    print("El email no es valido")