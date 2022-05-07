class Vehiculos():
    #Creo un Constructor para las caracteristicas principales
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False
    
    #Creo 3 metodos para cambiar el estado de las propiedades
    def arrancar(self):
        self.enmarcha = True
    
    def acelerar(self):
        self.acelera = True
    
    def frenar(self):
        self.frena = True

    #Comportamiento para revisar el estado de nuestro objeto
    def estado(self):
        print(f"marca: {self.marca} \nModelo: {self.modelo}\nEn Marcha: {self.enmarcha}",
        f"\nAcelerando: {self.acelera}\nFrenando: {self.frena}")


#Creo la clase Auto que Heredara de la clase Vehiculos
class Motos(Vehiculos): #En el argumento coloco la clase de la cual Hereda
    hcaballito = ""
    def caballito(self): #Creo un metodo propio de la clase Moto
        self.hcaballito = "Voy haciendo el caballito"

    #Sobreescribimos el metodo estado de la clase vehiculo y lo especializamos un poco mas
    def estado(self):
        print(f"marca: {self.marca} \nModelo: {self.modelo}\nEn Marcha: {self.enmarcha}",
        f"\nAcelerando: {self.acelera}\nFrenando: {self.frena}\n{self.hcaballito}")

#Creo una segunda clase llamada Furgonetas
class Furgonetas(Vehiculos):

    def carga(self, cargar):
        self.cargado = cargar
        if (self.cargado):
            return "La furgoneta esta cargada"
        else:
            return "La furgoneta esta descargada"

#Creo una clase de vehiculos electricos que no hereda de ninguna otra (clase independiente)
class VElectricos(Vehiculos):
    def __init__(self, marca, modelo):
        #Utilizo funcion super para llamar al constructor de la clase padre
        super().__init__(marca, modelo)
        self.autonomia=100

    def cargarEnergia(self):
        self.cargando=True

#Clase con herencias multiples, hereda de Velectricos y Vehiculos
#El constructor se hereda del primero de los argumentos, en este caso de VElectricos
#Si las clases tienen metodos de mismo nombre heredara las del primero
class BicicletaElectrica(VElectricos, Vehiculos):
    pass

print("------Viene Codigo de la Moto------")
miMoto = Motos("Honda","CBR")
#Al llamar al metodo, estaremos llamando al de la clase Moto 
#porque se sobreescribe el metodo heredado de la clase padre
miMoto.caballito()
miMoto.estado()

print("-------Viene codigo sobre Furgoneta-------")
miFurgoneta = Furgonetas("Renault","Kangoo")
miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.carga(True))

print("-------Viene codigo de Bicicleta Electrica--------")
miBici=BicicletaElectrica("Orbea", "ModeloX")
miBici.estado()
