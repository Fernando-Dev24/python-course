user = input("Escribe tu nombre ")
userSales = float(input("Digite el número de ventas realizadas "))

# Calculate rewards
reward = round(userSales * 0.13, 2)

# Output
print(f"Hey { user } un gusto verte de nuevo, actualmente tienes derecho a ${ reward } de comisión por tus ventas, un gusto ayudarte")