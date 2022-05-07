#Video 26:POO Crear clases, objetos y acceder a propiedades y comportamientos

class Coche(): #Construimos una clase. Primera letra del nombre Mayuscula
    #Contruimos propiedades de la clase coche
    largoChasis = 250 
    anchoChasis = 120
    ruedas = 4
    enmarcha = False
    #Construimos comportamientos (que es capaz de hacer el objeto) con metodos
    #Un metodo es una funcion que pertenece a una clase
    def arrancar(self): #Parametro self hace referencia a la instancia perteneciente a la clase
        self.enmarcha = True
    
    def estado(self):
        if(self.enmarcha):
            return "El coche esta en marcha"
        else:
            return "El coche esta parado"

#Instanciamos una clase, hacemos objeto que pertenezca a una clase
miCoche=Coche() #nombre de la instancia = clase a la que pertenece

#Para acceder a una propiedad del objeto. nomenclatura del punto
print(f"El largo de mi coche es de {miCoche.largoChasis}cm.")
print(f"El coche tiene {miCoche.ruedas} ruedas")

print(miCoche.estado())
miCoche.arrancar()
print(miCoche.estado())