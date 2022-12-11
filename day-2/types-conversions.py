## Conversiones implicitas, estas conversiones susceden automaticamente por Python, sin que nos demos cuenta

""" num1 = 20
num2 = 30.5

num1 = num1 + num2

print(type(num1))
print(type(num2)) """

## Conversiones explicitas, estas conversiones suceden a proposito, debido a que uno, como programador, asi lo escribe. Es decir, declararle a nuestro programa que convierta los valores si o si.

num1 = 5.8
num2 = int(num1) # La conversion de datos, int(), solamente elimina decimales, no aproxima

edad = input("Digita tu edad ")
edad = int(edad)

newEdad = 1 + edad

print("Tu edad el proxima sera " + str(newEdad)) ## Para imprimir tipos de datos numericos en pantalla, TODOS los valores deben de ser de tipo string o str, de lo contrario, arroja error