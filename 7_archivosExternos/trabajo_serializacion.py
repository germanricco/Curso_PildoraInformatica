import pickle

#lista_nombres = ["Pedro","Ana","Maria","Isabel"]

#fichero_binario=open("lista_nombres","wb") #write binari

#parametros primero que archivo quiero volcar, despues a donde lo quiero mandar
#pickle.dump(lista_nombres, fichero_binario)

#fichero_binario.close()

#AHORA QUIERO LEER LO QUE TIENE EN EL INTERIOR
fichero=open("lista_nombres", "rb") #Read binari
#guardo la informacion que traje en una variable
lista=pickle.load(fichero)

print(lista)