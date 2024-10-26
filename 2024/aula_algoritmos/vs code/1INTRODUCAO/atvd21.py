# Faça um programa em Python que receba o nome, o desconto (%) e o valor de um produto.
# Em seguida, apresente o nome, o valor atual, o desconto (em reais) e o valor final do produto.
produto = input("Insira o nome do produto: ")
valor = float(input("Insira o valor desse produto: R$"))
desconto = float(input("Por ultimo, insira seu desconto em %: "))

descontoReais = valor * (desconto / 100)
total = valor - descontoReais

print(f"Nome do produto: {produto}")
print("-" * 30)

print(f"Valor do produto: R${valor}")
print("-" * 30)

print(f"Seu desconto em reais: R${descontoReais}")
print("-" * 30)

print(f"Total a ser pago: R${total}")
