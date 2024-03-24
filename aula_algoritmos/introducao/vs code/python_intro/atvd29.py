#  Faça um programa que recebe o salário do usuário. Se o usuário recebe menos que um
#  salário mínimo, apresente na tela uma mensagem informando isso a ele. Se o salário dele
#  for maior que o salário mínimo, calcule quantos salários mínimos ele ganha e informe na
#  tela. Considere o valor de R$1.212,00 para o salário mínimo neste exercício.
from math import floor

salario = float(input("Insira seu salário: "))
salMinimo = 1212.00
minimo = salario / salMinimo

if(salario < salMinimo):
    print("Você recebe menos que um salário mínimo.")
else:
    print(f"Você recebe {floor(minimo)} salários mínimos.")
