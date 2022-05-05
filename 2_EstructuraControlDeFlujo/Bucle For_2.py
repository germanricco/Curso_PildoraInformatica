# Video 14 y 15: Primera parte de Bucle For

for i in ['German ', 'Ricco ', 'De Torrontegui']:
	print(i, end='')#el end es para que no haga saltos de linea cuando imprima

print('\n')

email=False
MiEmail=input('introduce tu direccion de email: ')
for i in MiEmail: #i toma valor de cada caracter
	if i=='@': #si en algun momento i=@ es un email, y lo chekeo
		email=True
if email==True: #Si yo pongo if email, seria lo mismo, toma el buleano
	print('El email es correcto')
else:
	print('El email es incorrecto')

print('\n')




