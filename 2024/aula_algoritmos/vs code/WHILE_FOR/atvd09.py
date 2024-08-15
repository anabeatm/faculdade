# Faça um programa que leia 5 números e informe a soma e a média dos números.
soma = 0

for c in range(5):
    num = int(input("Informa um número: "))
    soma += num

mediaNum = soma / 5
print(f"A soma dos números é: {soma}\nE a média deles é: {mediaNum}")