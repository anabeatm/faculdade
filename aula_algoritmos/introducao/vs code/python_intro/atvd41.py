# Faça um programa para pedir um número inteiro. Se esse número for positivo, verifique e
#  informe se ele é par ou ímpar. Se ele for negativo, some 100 e apresente na tela.
num = int(input("Digite um numero inteiro: "))
par = num % 2 == 0

if(num > 0):
    if(par):
        print("Par.")
    else:
        print("Impar.")
else:
    maisCem = num + 100
    print(maisCem)
