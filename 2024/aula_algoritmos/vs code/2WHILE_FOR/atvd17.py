# Refaça o exercício anterior, porém utilize um laço “for” para limitar o número de tentativas a 10 
# (usuário tem 10 chances só para acertar).
from random import randint
numPcAleatorio = randint(1, 100)

contador = 0

for c in range(10, 0, -1):
    numUsu = int(input("Em que número estou pensando? R: "))
    contador += c
    if(numUsu == numPcAleatorio):
        print(f"Você acertou!\nSuas tentativas foram {contador} vezes.")
        break
    else:
        print(f"Uh-oh :( errou! Você ainda tem {c} tentativas.")
        if(numUsu > numPcAleatorio):
            print("Seu número é maior!")
        else:
            print("Seu número é menor!")