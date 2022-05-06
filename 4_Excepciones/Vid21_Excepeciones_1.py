# Video 21: Excepciones_1
#Una excepcion es un error en tiempo de ejecucion, programa bien, pero algo inesperado pasa
#Provoca ruptura del programa y corte en la ejecucion que puede provocar que lineas no se ejecuten nunca 8/0 por ej.

# Lo podemos solucionar con Captura o control de excepciones

def division(num1,num2):

    try: 
        return num1/num2    #Error posible en num1/0
    
    except ZeroDivisionError:   #Excepcion y el nombre del error posible, si no esta el error en el except programa cae igual
        print("No se puede dividir entre 0")
        return "Operacion erronea"

num1 = int(input("Escriba el numerador: "))  
num2 = int(input("Escriba el denominador: "))

print(division(num1,num2))

