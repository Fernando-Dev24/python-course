precios_cafe = [('cappuchino', 1.5), ('expresso', 2.5), ('mocca', 1.9)]

def cafe_mas_caro(lista_precios):
   precio_mayor = 0
   cafe_mas_caro = ''

   for cafe, precio in lista_precios:
      if ( precio > precio_mayor ):
         precio_mayor = precio
         cafe_mas_caro = cafe
      else:
         pass

   return (cafe_mas_caro, precio_mayor)

cafe, precio = cafe_mas_caro(precios_cafe)

print(f"El cafe mas caro es { cafe }")
print(f"El precio del cafe { cafe } es ${ round(precio, 2) }")