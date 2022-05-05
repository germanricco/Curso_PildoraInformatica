#los diccionarios son como listas, que peuden tener entre sus elementos
#incluso otras listas, tuplas, u otros diccionarios
#(los elementos almacenados no estan ordenados) ya que los valores se almacenan
#asociados a una clave, tipo: "clave:valor"

#DEFINO UN DICCIONARIO CON NOMBRE DE PAISES Y CAPITALES
mi_diccionario={"Alemania":"Berlin", "Francia":"Paris","Argentina":"Buenos Aires"}

#AGREGAR ELEMENTO A DICCIONARIO
mi_diccionario["Italia"] ="Roma"
print(mi_diccionario)
print(mi_diccionario["Francia"]) #cuando pongo el pais (clave) me da la capital (valor)

#ELIMINAR UN ELEMENTO DEL DICCIONARIO
del mi_diccionario["Alemania"]
print(mi_diccionario)

#los tipos de datos dentro del diccionario pueden ser cualquiera

#ASIGNAMOS CON UNA TUPLA EL VALOR DE CADA CLAVE
latupla=("Espagna", "Francia", 3)
mi_diccionario={latupla[0]:"Madrid",latupla[1]:"Paris",latupla[2]:"Mosqueteros"}

print(mi_diccionario)

#UN DICCIONARIO CON UNA TUPLA ADENTRO	
diccionario={10:"Messi", "German":"Programador","Familiares":["Marcos","Liliana","Bruno"]}
print(diccionario)
print(diccionario["Familiares"]) #tengo una lista como valores en el diccionarios

#SACAR DATOS DEL DICCIONARIO
print(diccionario.keys())  #claves del diccionario
print(diccionario.values())  #valores del diccionario
print(len(diccionario)) #longitud del diccionario


segunda ={'Nombre':'German'}
print(segunda)
segunda.setdefault('Apellido','Ricco')  #Para agregar elementos a un diccionario
print(segunda)

entero=int(round(0.6,0))
print(entero)