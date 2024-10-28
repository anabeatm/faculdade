# Fulano de Tal está organizando um campeonato de futebol para n times. Ele precisa armazenar o nome do time 
# e a pontuação final de cada time. Ao final, precisa saber qual foi o time campeão e o vice campeão. 
# Faça um programa para o Fulano de Tal.
tam = int(input("São quantos times? R: "))

nomesTimes = [""] * tam
pontuacaoTimes = [0.0] * tam

for i in range(0, tam):
    nomesTimes[i] = input(f"Coloque o nome do {i + 1}° time: ")
    pontuacaoTimes[i] = float(input(f"Coloque a pontuação do {i + 1}° time: "))

if(tam >= 2):
    if(pontuacaoTimes[0] > pontuacaoTimes[1]):
        campeao = 0
        vice = 1
    else:
        campeao = 1
        vice = 0

    for i in range(2, tam):
        if pontuacaoTimes[i] > pontuacaoTimes[campeao]:
            vice = campeao
            campeao = i
        elif pontuacaoTimes[i] > pontuacaoTimes[vice]:
            vice = i
    
    print(f"O campeão é {nomesTimes[campeao]} com {pontuacaoTimes[campeao]}!")
    print(f"O vice-campeão é {nomesTimes[vice]} com {pontuacaoTimes[vice]}!")
else:
    print("Não há times suficientes para determinar um campeão e um vice-campeão.")
