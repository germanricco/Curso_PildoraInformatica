#La primera instruccion de un archivo setup es
from setuptools import setup

setup(
    name="paquetecalculos", #Nombre del paquete distribuible
    version= "1.0",
    description="Paquete de redondeo y potencia",
    author="German",
    author_email="germanricco97@gmail.com",
    url="www.paginawebdereferencia.es",

    #por ultimo la propiedad packages, donde tenemos que indicar donde se encuentra el packete que queremos empaquetar
    packages=["calculos","calculos.Calculos_complejos"]
)

#Luego hay que ir hasta el directorio donde esta el archivo setup.py desde la consola