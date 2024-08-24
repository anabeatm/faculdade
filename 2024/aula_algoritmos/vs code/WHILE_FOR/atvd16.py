"""Crie um jogo simples onde o computador escolhe um número aleatório entre 1 e 100 e o usuário deve adivinhar o número.
 Use um laço “while” para permitir que o usuário continue tentando até acertar. Após cada tentativa, informe se o
   palpite é maior, menor ou igual ao número sorteado.
"""
from random import randint
numPcAleatorio = randint(1, 100)

contador = 0

while True:
    numUsu = int(input("Em que número estou pensando? R: "))
    contador += 1
    if(numUsu == numPcAleatorio):
        print(f"Você acertou!\nSuas tentativas foram {contador} vezes.")
        break
    else:
        print(f"Uh-oh :( errou! Tente novamente.")
        if(numUsu > numPcAleatorio):
            print("Seu número é maior!")
        else:
            print("Seu número é menor!")
