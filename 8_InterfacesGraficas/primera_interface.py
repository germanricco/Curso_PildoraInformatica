from tkinter import * #Primero importamos la libreria tkinter

#Construimos la raiz
raiz = Tk()

#Pongo titulo a la ventana
raiz.title("Ventana de pruebas") 

#Bloqueo redimensionar la ventan tanto en width(ancho) como height(alto)
raiz.resizable(1,1)  #pongo como argunmentos 0 False o 1 True

#Cambio la geometrica predeterminada de la ventana
#raiz.geometry("650x350")

#Cambio el background
raiz.config(bg="blue")

#una ventana para estar en ejecucion tiene que estar en un bucle infinito ya que tiene
#que estar a la escucha de lo que el usuario haga (eventos)
#mainloop() siempre al final

#Creo un frame
miFrame =Frame()

#empaqueto el frame, dejandolo anclado a la derecha de la raiz
#anchor y n,s,w,e (norte, sur, oeste, este)
#miFrame.pack(side="right", anchor="n")
miFrame.pack(fill="y", expand="True")

miFrame.config(bg="orange")
miFrame.config(width="650",height="350")

raiz.mainloop()
