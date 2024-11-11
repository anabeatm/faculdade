"""
Foi  realizada  uma  pesquisa  sobre  algumas  características  físicas  de  cinco  habitantes  de  uma 
região. Foram coletados os seguintes dados de cada habitante: sexo, cor dos olhos (A: azuis, C: castanhos), cor 
dos cabelos (L: louros, P: pretos, C: castanhos) e idade.

a) Implemente um procedimento que leia estes dados, armazenando-os em vetores (vetores declarados 
como variáveis globais)  

b) Faça uma função que determine e retorne ao programa principal a média de idade das pessoas com 
olhos castanhos e cabelos pretos

c) Faça uma função que calcule e retorne ao programa principal a maior idade entre os habitantes

d) Faça uma função que determine e devolva ao programa principal a quantidade de indivíduos de sexo 
feminino com idade entre 18 e 35 anos (inclusive) e que tenham olhos azuis e cabelos louros.
"""

def colocandoDadosVetor(sexo, corOlhos, corCabelos, idade):
    for i in range(0, 5):
        sexo[i] = input("Sexo [M/F]: ").lower()
        corOlhos[i] = input("Cor dos olhos [A: azuis/ C: castanhos]: ").lower()
        corCabelos[i] = input("Cor dos cabelos [L: loiros/ P: pretos/ C: castanhos] ").lower()
        idade[i] = input("Idade: ").lower()
    return sexo, corOlhos, corCabelos, idade

def mediaIdadeCastanhosPretos(idade, corOlhos, corCabelos):
    soma = 0
    cont = 0

    for i in range(0, len(idade)):
        if(corOlhos[i] == "c" and corCabelos[i] == "p"):
            soma += idade[i]
            cont += 1

    if(cont == 0):
        return 0
    
    mediaIdadeCastanhosPretos = soma / cont

    return mediaIdadeCastanhosPretos

def maiorIdade(idade):
    maiorIdade = idade[0]

    for i in range(1, len(idade)):
        if(maiorIdade < idade[i]):
            maiorIdade = idade[i]

    return maiorIdade

def qntdFemEntre18e35(sexo, corOlhos, corCabelos, idade):
    qntdFem = 0

    for i in range(0, len(idade)):
        if(sexo[i] == "f" and 18 <= idade[i] <= 35):
            if(corCabelos[i] == "l" and corOlhos[i] == "a"):
                qntdFem += 1
    
    return qntdFem

sexo = [""] * 5
corOlhos = [""] * 5
corCabelos = [""] * 5
idade = [0] * 5

resultado = colocandoDadosVetor(sexo, corOlhos, corCabelos, idade)
print(resultado)
media = mediaIdadeCastanhosPretos(idade, corOlhos, corCabelos)
print(f"A média da idade dos habitantes com olhos castanhos e cabelos pretos é: {media:.2f}")
idadeMaior = maiorIdade(idade)
print(f"A maior idade entre os habitantes é {maiorIdade} anos.")
qntdFem = qntdFemEntre18e35(sexo, corOlhos, corCabelos, idade)
print(f"A quantidade de pessoas do sexo feminino entr 18 e 35 anos, com cabelos loiros e olhos azuis são {qntdFem}")