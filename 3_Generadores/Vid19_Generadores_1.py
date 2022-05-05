# Video 19: Generadores parte 1
# Son estructuras que extraen valores de una funcion y se almacenan en objetos iterables de uno en uno. mientras tanto queda en suspension de estado

#Antes podiamos generar numeros pares y ponerlos en una lista asi...
def generaPares(limite):
    num=1
    miLista=[]

    while num<limite:
        miLista.append(num*2)
        num+=1
    return miLista

print(generaPares(10))


#Pero ahora puedo usar los generadores que tienen mucha mayor eficiencia
def generaPares2(limite):
    num1=1

    while num1<limite:
        yield num1*2   #Yield construye un objeto iterable con los valores de la lista en su interior, almacenandolos de 1 en 1
        num1+=1

#ahora necesito crear una variable objeto donde almaceno el objeto iterable que devuelve la funcion
devuelvePares=generaPares2(10)

#Esto me permite, por ejemplo, imprimir un numero a la vez, sin necesidad de generarlos todos (lo que gasta recursos) y despues
#tenerlos almacenados todos (gastando espacio en memoria). Disminuyendo mucho el consumo de recursos

print(next(devuelvePares))
print("Aca pueden haber muchas lineas de codigo... ")
print(next(devuelvePares))
print("Aca pueden haber muchas lineas de codigo... ")
print(next(devuelvePares))
print("Aca pueden haber muchas lineas de codigo... ")

