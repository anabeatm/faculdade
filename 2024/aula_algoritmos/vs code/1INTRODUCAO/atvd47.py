# Construa um programa para receber quatro números e no final apresentar o maior e o
# menor.
num_1 = float(input("Insira um valor: "))
num_2 = float(input("Insira um valor: "))
num_3 = float(input("Insira um valor: "))
num_4 = float(input("Insira um valor: "))

maior = num_1
menor = num_1

if num_2 > maior:
    maior = num_2
elif num_2 < menor:
    menor = num_2

if num_3 > maior:
    maior = num_3
elif num_3 < menor:
    menor = num_3

if num_4 > maior:
    maior = num_4
elif num_4 < menor:
    menor = num_4

print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")

