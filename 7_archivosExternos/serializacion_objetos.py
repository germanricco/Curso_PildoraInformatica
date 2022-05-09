import pickle
#Reutilizo codigo de clases anteriores
class Vehiculos():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False
    
    def arrancar(self):
        self.enmarcha = True
    
    def acelerar(self):
        self.acelera = True
    
    def frenar(self):
        self.frena = True

    def estado(self):
        print(f"marca: {self.marca} \nModelo: {self.modelo}\nEn Marcha: {self.enmarcha}",
        f"\nAcelerando: {self.acelera}\nFrenando: {self.frena}")

#Creo 3 objetos a partir de la clase vehiculos
coche1 = Vehiculos("Mazda","MX5")
coche2 = Vehiculos("Seat","Leon")
coche3 = Vehiculos("Renault","Megane")

#Hacemos una coleccion de objetos
coches=[coche1, coche2, coche3]
fichero=open("losCoches", "wb")
pickle.dump(coches, fichero)
fichero.close()
del (fichero)

ficheroApertura = open("losCoches","rb")
misCoches1 = pickle.load(ficheroApertura) #Que carge la info almacenada en la variable ficheroApertura
ficheroApertura.close()

#Ahora los recupero, usando el metodo estado en cada uno para mas info.
for i in misCoches1:
    print(i.estado())