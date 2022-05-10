from tkinter import *
from turtle import width

root=Tk()

miFrame=Frame(root, width=1000, height=800)

miFrame.pack()

#La label que se ejecuta primero hace de bg para la que se ejecuta despues
miImagen = PhotoImage(file="8_InterfacesGraficas/arduino PaP.png")
Label(miFrame, image=miImagen).place(x=0,y=0)

#NOTAS SOBRE LABEL (Googlear Tkinter Label para mas)
#.place() ubica la distancia a la esquina superior izquierda
#bd indica tamaño de el borde, .place ubica desde que empieza el borde
#height y width cambia la altura y ancho (Las unidades no son pixeles)
#padx y pady agregan espacio izq.der y arriba.abajo respectivamente
#relif pone un borde decorativo
#underline subraya UN caracter, el de la posicion que indico
miLabel = Label(miFrame, text="La primera Label que hago", fg="red",
font=("Comic Sans MS", 18), bg="black", bd="4", cursor="pirate", height="10",
padx=5, relief=RAISED, underline=11)

#Al empaquetar el label adapta el contenedor a las dimensiones del Label
#miLabel.pack()
#metodo place para indicar ubicacion del label dentro de miFrame
miLabel.place(x=100, y=200)


root.mainloop()