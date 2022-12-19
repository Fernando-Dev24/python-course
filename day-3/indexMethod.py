# El metodo Index devuelve el indice de un determinado string para saber su posicion. Así mismo si nosotros queremos saber que letra reside en un índice especifico basta con escribir la posición en la que se encuentra

# El metodo rindex busca el parametro enviado al metodo solamente de derecha a izquierda, el metodo index, lo hace como el ser humano, es decir, de izquierda a derecha.

# NOTA: Cuando Python detecta un error no compilara correctamente y esto devolvera un error

miTexto = 'Esta es una prueba'
resultado = miTexto.rindex("a")

print(resultado)