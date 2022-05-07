class Persona():

    def __init__ (self,nombre, edad, lugar_residencia):
        self.nombre = nombre
        self.edad = edad
        self.residencia = lugar_residencia

    def descripcion(self):
        print(f"Nombre: {self.nombre}\nEdad: {self.edad}\nLugar de residencia: {self.residencia}")
    
#La clase empleado heredara las propiedades de la clase persona y tendra tambien las propias
class Empleado(Persona):

    def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, residencia_empleado):
        #La funcion super() llama al metodo de la clase padre, el metodo __init__ en este caso
        #Y a ese metodo llamado hay que pasarle los argumentos necesarios
        super().__init__(nombre_empleado, edad_empleado, residencia_empleado)

        self.salario = salario
        self.antiguedad = antiguedad

    def descripcion(self):
        #Llamo al metodo descripcion de la clase Persona y lo ejecuto
        super().descripcion()
        print(f"Salario: {self.salario}\nAntiguedad: {self.antiguedad}")

German=Empleado(1500, 15, "German", 21, "Mendoza,Argentina")

German.descripcion()

print(isinstance(German, Persona))