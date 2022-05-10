from tkinter import *

root =Tk()
root.title("Practica de Entry y grid")

minombre = StringVar()

miFrame=Frame(root, width=1200, height=800)
miFrame.pack()

#ENTRY
#Asocio al entry cuadroNombre una variable tipo texto que es minombre
cuadroNombre=Entry(miFrame, textvariable=minombre)
cuadroNombre.grid(row=0, column=1, padx=8, pady=5)
cuadroNombre.config(fg="Blue")

cuadroPassword=Entry(miFrame)
cuadroPassword.grid(row=1, column=1, padx=8, pady=5)
cuadroPassword.config(show="*")

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=2, column=1, padx=8, pady=5)

cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=3, column=1, padx=8, pady=5)

#TEXT
textoComentario=Text(miFrame, width=16, height=5)
textoComentario.grid(row=4, column=1, padx=8, pady=5)

#Scroll
#Widget a donde pertenece, command = widget de texto al que pertenece y .yview para que sea vertical
scrollVert=Scrollbar(miFrame, command=textoComentario.yview)
#Colocamos el scrollback
#sticky="nsew" sirve para que el tamaño se adapte al tamaño del texto
scrollVert.grid(row=4, column=3, sticky="nsew")

#Configuracion para que la barra de scroll baje a la vez que bajamos mientras se escribe
textoComentario.config(yscrollcommand=scrollVert.set)

#LABELS
nombreLabel = Label(miFrame, text="Nombre: ")
nombreLabel.grid(row=0, column=0, sticky="E", padx=8, pady=5)

passwordLabel = Label(miFrame, text="Contraseña: ")
passwordLabel.grid(row=1, column=0, sticky="E", padx=8, pady=5)

apellidoLabel = Label(miFrame, text="Apellido: ")
apellidoLabel.grid(row=2, column=0, sticky="E", padx=8, pady=5)

direccionLabel = Label(miFrame, text="Direccion: ")
direccionLabel.grid(row=3, column=0, sticky="E", padx=8, pady=5)

comentariosLabel = Label(miFrame, text="Comentarios: ")
comentariosLabel.grid(row=4, column=0, sticky="E", padx=8, pady=5)

#BOTON
#Codigo que ejecuta el boton enviar, pone en la var minombre "German"
def codigoBotonEnviar():
    minombre.set("German")

botonEnvio=Button(root, text="Enviar", command=codigoBotonEnviar)
botonEnvio.pack()

root.mainloop()