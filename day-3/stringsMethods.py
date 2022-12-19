# En esta leccion vamos a ver lo siguientes metodos: replace(), upper(), lower(), join(), split(), find()

# El metodo upper() y lower() transforman la cadena de texto en mayusculas o minusculas

# El metodo join() une las palabras que se pasan en su parentesis mediante un separador determinado por el dev

# El metodo split() separara la cadena de texto por el separador que le proporcionemos, por defecto, es un espacio en blanco

# El metodo find() realiza lo mismo que el metodo index() con la excepcion que si no encuentra la cadena de texto que buscaba retorna un valor de -1 y no genera un error que interrumpe el codigo

# El metodo replace() recibe dos valores, el string antiguo, y el string nuevo que reemplazara el antiguo

text = 'Este es el texto de Fernando'
result = text.find("g")

print(result)