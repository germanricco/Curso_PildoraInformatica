edad=8
if 0<edad<100: #Se pueden concatenar mas de un operador de comparacion en un if
	print("La edad es correcta")
else:
	print("la edad es incorrecta")

#-----OTRO EJEMPLO-----:
sal_presi=int(input("Cual es el salario del presidente de la empresa? "))
sal_jefe_area=int(input("Cual es el salario del jefe de area? "))
sal_empleado=int(input("Cual es el salario del empleado? "))

if sal_empleado<sal_jefe_area<sal_presi: #Concateno mas de un operador
	print("Los salarios tienen logica")
else:
	print("no hay logica en los salarios")