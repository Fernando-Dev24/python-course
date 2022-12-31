import unittest
import cambia_texto

class ProbarCambiarTexto(unittest.TestCase):
   # Las funciones de prueba que se definen dentro de la clase, deben de iniciar con la palabra "test"
   def test_mayusculas(self):
      palabra = 'buen dia'
      resultado = cambia_texto.todo_mayusculas(palabra)
      
      # Para verificar que el resultado sea el esperado, llamamos el metodo assertEqual([valor_a_verificar], [resultado_manual])
      self.assertEqual(resultado, 'Buen Dia')

# Antes de ejecutar las pruebas, debemos de escribir, SI O SI, este condicional
if ( __name__ == '__main__' ):
   unittest.main()