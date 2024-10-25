# Faça um programa para armazenar seis números inteiros para uma loteria, de modo que os seis números sejam criados 
# aleatoriamente pelo Python e que não sejam repetidos. Em seguida, peça para o usuário informar os seis números que 
# ele apostou. Por fim, apresente na tela quantos números ele acertou, informando se ele não ganhou nada (0 a 3 acertos), 
# se acertou a quadra (4 acertos), a quina (5 acertos) ou se ele nunca mais vai precisar trabalhar (6 acertos).
from random import sample

numerosSorteados = sample(range(101), 6)

print(numerosSorteados)

numerosApostados = [0] * 6
for aposta in range(0, len(numerosApostados)):
    numerosApostados[aposta] = int(input("Informe os números da sua aposta: "))

cont = 0
for i in range(0, len(numerosSorteados)):
    for j in range(0, len(numerosApostados)):
        if(numerosApostados[j] == numerosSorteados[i]):
            cont += 1


if(cont == 6):
    print("Nunca mais precisará trabalhar!")
elif(cont == 5):
    print("É uma quina!")
elif(cont == 4):
    print("É uma quadra!")
elif(cont <= 3):
    print("Nenhum acerto!")
