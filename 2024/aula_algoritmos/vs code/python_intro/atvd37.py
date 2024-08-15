#  Faça um programa que gera um número aleatório entre X e Y. Para isso, peça para o
#  usuário um valor para X, Y e um número entre X e Y. Gere um valor aleatório entre X e Y e
#  verifique se ele é igual ao número digitado pelo usuário. Se ele acertar, apresente na tela
#  “Acertou”, se não, “Errou”.
import random

x = int(input("Digite um numero x: "))
y = int(input("Digite um numero y: "))
numUsuario = int(input(f"Agora, insira um numero entre {x} e {y}: "))
numAleatorio = random.randint(x, y)

if(numUsuario == numAleatorio):
    print("Acertou.")
else:
    print(f"Errou. O numero era {numAleatorio}.")
