# Faça um programa que gere e apresente na tela X números inteiros aleatórios no 
# intervalo de -100 a 100, de modo que o valor de X seja informado pelo usuário. 
# No final do programa, apresente na tela: 

# (1) a soma dos números gerados, 
# (2) quantos números são positivos, 
# (3) negativos, 
# (4) o maior número gerado, 
# (5) o menor número gerado, 
# (6) quantos são pares, 
# (7) ímpares e 
# (8) quantos são múltiplos de 3.

from random import randint

x = int(input("Informe o final: "))
for c in range(0, x):
    numAleatorio = randint(-100, 100)
    print(c, '-', numAleatorio)

print('Fiquei com preguiça de fazer :P')
