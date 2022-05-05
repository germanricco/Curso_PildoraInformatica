#Programa para determinar si un alumno puede acceder a una beca
distancia=int(input("a cuantos 'km' vivis del colegio? "))
hermanos=int(input("Cuantos hermanos tenes? "))
salario_fam=int(input("Cual es tu salario familiar? "))

if distancia>40 and hermanos>3 or salario_fam<=20000: #Utilizo and y or
	print("Tenes derecho a acceder a una beca")
else:
	print("No puedes acceder a la beca")

#OTRO PROGRAMA
print('Este es un programa para eleccion de materias optativas')
optativas=['algebra', 'analisis matematico', 'introduccion a la ingenieria', 'Geometria analitica']

print('las materias optativas que puede tomar son: '+ str(optativas))
elegida=input('Cual materia de las anteriores elijes como optativa? ')
elegida_minuscula=elegida.lower() #El lower me pasa todo lo que pongo a minusculas
if elegida_minuscula in optativas:
	print('perfecto, se ha registrado correctamente')
else:
	print('no puede elegir esa materia')
