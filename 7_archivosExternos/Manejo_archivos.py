from io import open
from platform import architecture

#Metodo open crea archivo externo, entra de parametros el nombre del archivo y
#w para entrar en modo escritura de texto
#r para entrar en modo lectura (read)


#PARA ESCRIBIR EN EL ARCHIVO
#archivo_texto = open("archivo.txt","w")
#
#frase = "Tremendo dia para estudiar Python\n domingo a la tarde"
#
#Para escribir el archivo .write(de parametro lo que quiera agregar)
#archivo_texto.write(frase)
#
#Cerramos el archivo
#rchivo_texto.close()


#PARA LEER LO QUE HAY EN EL ARCHIVO
#archivo_texto = open("archivo.txt","r")
#lee lo que hay en el archivo y lo almacena en la variable texto
#texto = archivo_texto.read()
#Tambien existe readlines(), se puede elegir entre usar uno u otro ya que la posicion final del puntero queda al final
#lista = archivo_texto.readlines()
#
#archivo_texto.close()
#
#print(texto)
#print(lista)


#ABRIR UN ARCHIVO PARA AGREGAR INFORMACION
#archivo_texto = open("archivo.txt", "a")
#archivo_texto.write("\n siempre es una buena ocasion para estudiar Python")

archivo_texto = open("archivo.txt", "r+") #r+ lectura y escritura

print(archivo_texto.read(11))      #Leo el archivo hasta la posicion 11
archivo_texto.seek(0)              #Posiciono el puntero al principio
print(archivo_texto.readlines())   #Vuelvo a leer el archivo entero