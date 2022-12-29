# A diferencia de Javascript, el metodo match() evalua la estructura de colecciones de datos, si la estructura corresponde de alguna manera pues ejecutara las sentencias que se hallen en ella. De esta forma, no solo compara el contenido, si no su estructura

cliente = {
   "nombre": "Fernando",
   "edad": 20,
   "ocupacion": "Docente Informatica"
}

pelicula = {
   "titulo": "Matriz",
   "ficha_tecnica": {
      "protagonista": "Keanu Reeves",
      "director": "Lana y Lily Wachowski"
   },
}

elementos = [cliente, pelicula, "libro"]

for e in elementos:
   match e:
      case { "nombre": nombre, "edad": edad, "ocupacion": ocupacion }:
         print("Es un cliente")
         print(nombre, edad, ocupacion)
      case { "titulo": titulo, "ficha_tecnica": { "protagonista": protagonista, "director": director } }:
         print('Esto es una pelicula')
         print(titulo, protagonista, director)
      case "_":
         print("No se que es esto")
