#Video 22: Capturar varias excepciones y clausula finally
#Otro error que podriamos tener es que al introducir los datos, no sean numeros

#PRIMER EJEMPLO
#while True: #Este bucle infinito hace que hasta que no se coloquen los dos valores bien, no salga del bucle
#    try:
#        num1 = float(input("Introduzca el numerador: "))
#        num2 = float(input("Introduzca el denominador: "))
#        break
#    except ValueError:
#        print("Los valores introducidos no son correctos, intentalo de nuevo")
#
#def divide(num1,num2):
#    try:
#        return num1/num2
#    except ZeroDivisionError:
#        print("No se peude dividir por 0")
#        return "Operacion Erronea"
#
#print(divide(num1,num2))

#SEGUNDO EJEMPLO
def divide():
    try:
        op1=float(input("Introduzca el numerador: "))
        op2=float(input("Introduzca el denominador: "))
        print("La division es: " + str(op1/op2))
    except ZeroDivisionError:
        print("No se puede dividir por 0")
    except ValueError:
        print("El valor introducido es erroneo")
    finally:
        print("Calculo finalizado")  # Cuando queres que un codigo se ejecute siempre, ocurra lo que ocurra
