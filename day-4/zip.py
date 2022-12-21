# La funcion zip mezclara dos listas en tuples que contendran un valor de cada lista que se ha pasado como parametro

# Zip llega a la lista mas corta, los elementos que no pueda agrupas en pares, simplemente los ignora

nombres = ["Ana", "Hugo", "Valeria"]
edades = [65, 29, 42]
ciudades = ["Lima", "Madrid", "Mexico"]

combinados = list(zip(nombres, edades, ciudades))

for name, edad, ciudad in combinados:
   print(f"{ name } tiene { edad } años y vive en { ciudad }")