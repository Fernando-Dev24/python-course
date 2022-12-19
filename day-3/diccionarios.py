""" dic = {
   1: "a",
   2: 'b',
}

dic[3] = 'c' # Se puede agregar valores a un diccionario cuando su clave no existe
dic[2] = 'B' # Cuando una clave ya existe, se puede sobreescribir los valores

print(dic.keys()) # Este metodo keys() devuelve las claves del diccionario
print(dic.values()) # Este metodo values() devuelve el valor de las claves de un diccionario
print(dic.items()) # Este metodo items() devuelve la clave y el valor de la clave en parentesis y separado por comas """

mi_dic = {
    "nombre":"Karen",
    "apellido":"Jurgens",
    "edad":35,
    "ocupacion":"Periodista"
}

mi_dic["edad"] = 36
mi_dic["ocupacion"] = "Editora"
mi_dic["pais"] = "Colombia"

print(mi_dic)