nota_alumno=int(input("Introduce la nota del alumno: ")) #Cualquier cosa que introducimos con input es texto

def evaluacion(nota):
	valoracion="aprobaste"
	if nota<6:
		valoracion="suspendiste"
	return valoracion
print(evaluacion(nota_alumno))