#1~Defino una lista
#(Pueden tener cualquier tipo de datos)
milista=['Maria', 'Marta', 'German', 'Liliana']

       #indice 0, Indice 1, Indice 2, Indice 3

#TEMAS GENERALES DE POSICIONES DE ELEMENTOS EN LISTAS
print(milista[:]) #De esta manera imprimo la lista
print(milista[2])  #Imprimo lo que esta en el indice dos de la lista
print(milista[-2]) #Empieza a contar desde el final
print(milista[0:3]) #acceder a porcion de lista, 0 incluido 3 excluido
print(milista[:3])  #Forma abreviada de lo mismo
print(milista[1:]) #desde el indice 1 hasta el final
print(milista[3:]) #desde el indice 3 hasta el final

#AGREGAR ELEMENTOS A UNA LISTA
milista.append('Martin') #en el final
milista.insert(1,'Marcos') #con el 1 decimos en que posicion lo queremos
milista.extend(['Bruno','Pedro']) #Para agregar mas de una cosa a la vez
print(milista[:])

#BUSCAR EN QUE POSICION ESTA UN ELEMENTO EN UNA LISTA
Posicion=milista.index('Bruno') #Comdano ".index"
print(Posicion)  #si esta repetido lo que busco nos da el primer elemento

#COMPROBAR SI UN ELEMENTO SE ENCUENTRA EN LA LISTA (nos tira true o false)
print("German" in milista)
print("Graciela"in milista)

#ELIMINAR ELEMENTOS DE UNA LISTA
milista.remove('German') #eliminar un elemento determinado de la lista
print(milista[:])
milista.pop()
print(milista[:]) #eliminar el ultimo elemento de la lista

#SUMA DE LISTAS
lasegunda=[24, 20.1,'probando']
lista_de_sumadas=lasegunda + milista
print(lista_de_sumadas)

#multiplicar lista por un escalar es un repetidor
print(milista[2]*4)