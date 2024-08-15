# Faça um Programa receba o valor de x, calcule e imprima o valor de
#  𝑓(𝑥) = 1 / 2 − 𝑥 se 𝑥 < 2
#  𝑓(𝑥) = 1 / 𝑥 − 2 se 𝑥 ≥ 2

valor = int(input("Insira um valor inteiro: "))

if(valor < 2):
    formula_menosDois = 1 / (2 - valor)
    print(formula_menosDois)
if(valor >= 2):
    formula_maisDois = 1 / (2 + valor)
    print(formula_maisDois)
