# Faça um programa que calcule o valor de imposto a ser pago a partir de um salário bruto.
#  Se o salário for um valor até R$1.903,98, a pessoa não precisa pagar imposto de renda.
#  Por outro lado, se o salário for menor que R$2.826,65 é cobrado 7,5% de imposto e se for
#  maior, cobra-se 15%. Faça um programa que receba o salário bruto, calcule e mostre o
#  valor a ser pago.
salarioBruto = float(input("Insira seu salario bruto: R$"))

if(salarioBruto <= 1903.98):
    print("Nao precisara pagar imposto de renda.")
if(salarioBruto < 2826.65):
    imposto = salarioBruto * (7.5 / 100)
    print(f"Seu imposto sera R${imposto}.")
if(salarioBruto > 2826.65):
    imposto = salarioBruto * (15 / 100)
    print(f"Seu imposto sera R${imposto}.")
    