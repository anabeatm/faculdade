import math

a = float(input("Me informe um numero: "))
b = float(input("Me informe outro numero: "))
c = float(input("Me informe um outro numero: "))

delta = (b ** 2) - (4 * a * c)
delta_raizQuadrada = math.sqrt(delta) # Ocorre um erro caso os valores derem negativo.

x1 = (- b + (delta_raizQuadrada)) / (2 * a)
x2 = (- b - (delta_raizQuadrada)) / (2 * a)

print(f"x1 = {x1}")
print(f"x2 = {x2}")
