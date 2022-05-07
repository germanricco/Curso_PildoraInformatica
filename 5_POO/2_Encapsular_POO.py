#Video 27 y 28
#Reciclo codigo clase pasada y modificamos...

class Coche():
    #Estas son las propiedades en un ESTADO INICIAL
    #Especificamos en una clase el estado inicial con un CONSTRUCTOR
    #Es un metodo especial que le da estado inicial a los objetos
    def __init__(self) -> None:
        #Con doble guion se encapsula la propiedad para que no se pueda acceder desde afuera
        self.__largoChasis = 250 
        self.__anchoChasis = 120
        self.__ruedas = 4
        self.__enmarcha = False
   
    #Al agregar parametro arrancamos, hay que darle un valor True o False
    def arrancar(self,arrancamos):
        self.__enmarcha = arrancamos

        if(self.__enmarcha):
            chequeo=self.__chequeoInterno()

        if(self.__enmarcha and chequeo):
            return "El coche esta en marcha"

        elif(self.__enmarcha and chequeo==False):
            return "Algo ha ido mal en el chequeo, no puede arrancar"

        else:
            return "El coche esta parado"

    def estado(self):
        print(f"El coche tiene {self.__ruedas} ruedas y un ancho de {self.__anchoChasis}cm.")

    #Hago un metodo que antes de arrancar verifique que todo este bien
    #Encapsulo el metodo para no poder acceder desde fuera de la clase
    def __chequeoInterno(self):
        print("Realizando chequeo interno")
        self.gasolina="ok"
        self.aceite="ok"
        self.puertas="cerradas"

        if (self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):
            return True
        else:
            return False

miCoche=Coche() #Creamos una primera instancia
print(miCoche.arrancar(True))
#miCoche.__ruedas = 1  #Al estar encapsulado NO SE PERMITE MODIFICARLO DESDE FUERA
miCoche.estado()

print("---------A continuacion creamos el segundo objeto-----------")

miCoche2=Coche() #Creamos una segunda instancia
print(miCoche2.arrancar(False))
miCoche2.estado()