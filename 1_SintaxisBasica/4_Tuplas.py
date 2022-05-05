#Las tuplas son listas inmutables
#no permiten agregar, eliminar, mover elementos,etc.
#si permiten extraer porciones pero el resultado es otra tupla

#DEFINO UNA TUPLA	
nombreTupla=(4,1.2,'German',4,'Programando',4) #ahora va con parentesis

#ACCEDER A UN ELEMENTO DE LA TUPLA
print(nombreTupla[1])

#CONVERTIR UNA TUPLA A UNA LISTA
mi_lista=list(nombreTupla) #comando list
print(mi_lista)
print(nombreTupla)
	#ahora convierto de lista a tupla
lista=[1,4,8]
ahoraTupla=tuple(lista) #comando tuple
print(ahoraTupla)

#BUSCAR ELEMENTO DENTRO DE UNA TUPLA
print('German'in nombreTupla)

#CUANTAS VECES ESTA EL ELEMENTO
print(nombreTupla.count(4)) #el elemento 4 esta 3 vez en la tupla

#LONGITUD DE UNA TUPLA (cuantos elementos tiene)
print(len(nombreTupla))  #comando len

#TUPLA UNITARIA	
tupla_unitaria=('martin',) #tengo que agregar la coma
print(tupla_unitaria)
#escribir una tupla se llama empaquetada

#DESEMAQUETADO DE tupla
nueva=(25, 10, 2000)
print(nueva[:])
dia, mes, agno=nueva  #asigno en orden cada variable el valor de la tupla
print(dia)
print(mes)
print(agno)