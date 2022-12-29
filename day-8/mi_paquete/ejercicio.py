# Cuando estamos trabajando con paquetes, a la hora de importar y trabajar con las funciones debemos de acceder al paquete. En este caso, suma_y_resta. Seguido de un "." seguido de la funcion que queramos usar

# Cuando queramos hacer un subpaquete debemos de importar el paquete.[nombre_subpaquete]

from paquete_fer import suma_y_resta
from paquete_fer.subpaquete import saludo

suma_y_resta.suma(15, 2)
suma_y_resta.resta(20, 55)
saludo.hola()