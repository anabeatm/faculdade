# Crie  um  procedimento  que  receba  um  valor  inteiro  positivo.  O  procedimento  deve  calcular  o 
# fatorial deste número e apresenta-lo ao usuário.
import math

def fatorial():
    num = int(input("Informe um número para calcular seu fatorial: "))
    resultado = math.factorial(num)
    print(f"O resultado do fatorial é: {resultado}")

fatorial()