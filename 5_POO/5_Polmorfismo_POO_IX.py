class Coche():
    def desplazamiento(self):
        print("Me desplazo utilizando 4 ruedas")

class Moto():
    def desplazamiento(self):
        print("Me desplazo utilizando 2 ruedas")

class Camion():
    def desplazamiento(self):
        print("Me desplazo utilizando 8 ruedas")

#UTILIZANDO POLIMORFISMO
#Creo una funcion que tiene como parametro un vehiculo generico
def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()

#Creo el objeto miVehiculo de cualquier tipo
miVehiculo = Camion()

#Y ahora puedo pasarle al metodo como parametro el objeto que ya habia creado
desplazamientoVehiculo(miVehiculo)