# Debido a que unittest esta integrada en Python no es necesario instalarla utilizando pip
# La metodologia es simple:
# 1. Creamos el modulo / archivo que queremos evaluar
# 2. Creamos un modulo encargado de las pruebas
# 3. Importamos unittest en ese archivo de pruebas, e importamos el modulo a evaluar
# 4. Creamos una nueva clase que hereda los atributos y metodos de unittest.TestCase, dentro de esta clase ya podemos crear y evaluar tantas pruebas como queramos