# Faça um programa para armazenar seis números inteiros para uma loteria, permitindo que o usuário informe os 
# números sorteados. Em seguida, peça para o usuário informar os seis números que ele apostou. Por fim, apresente 
# na tela quantos números ele acertou, informando se ele não ganhou nada (0 a 3 acertos), se acertou a quadra 
# (4 acertos), a quina (5 acertos) ou se ele nunca mais vai precisar trabalhar (6 acertos).

numerosSorteados = [0] * 6
for i in range(0, len(numerosSorteados)):
    numerosSorteados[i] = int(input("Informe os números do sorteio: "))

numerosApostados = [0] * 6
for c in range(0, len(numerosApostados)):
    numerosApostados[c] = int(input("Informe os números que você apostou: "))

cont = 0
for j in range(0, len(numerosSorteados)):
    for h in range(0, len(numerosApostados)):
        if(numerosApostados[h] == numerosSorteados[j]):
            cont += 1
        
print(f"Você fez {cont} acertos!")
if(cont == 6):
    print("Nunca mais precisará trabalhar!")
elif(cont == 5):
    print("É uma quina!")
elif(cont == 4):
    print("É uma quadra!")
elif(cont <= 3):
    print("Nenhum acerto!")
