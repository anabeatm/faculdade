#  Faça um programa que gera um número aleatório entre 1 e 10. Em seguida, peça para o
#  usuário digitar um número. Se ele acertar, apresente na tela “Acertou”, se não, “Errou”.
import random

numAleatorio = random.randint(1, 10)
numUsu = int(input("Insira um número inteiro entre 1 a 10: "))

if (numUsu == numAleatorio):
    print("Acertou.")
else:
    print(f"Errou. O número certo era {numAleatorio}.")
