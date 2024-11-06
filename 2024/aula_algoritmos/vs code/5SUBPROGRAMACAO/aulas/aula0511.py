"""1) Implemente uma função chamada gerarVetor que recebe por parâmetro o tamanho do vetor e uma str indicando
o tipo de dado desse vetor (int, float, str). A função deverá retornar um vetor com valores aleatórios: gerarVetor(5, "int").

2) Implemente um método chamado ordenarBolha que recebe por parâmetro um vetor de números inteiros e retorna o vetor ordenado:
ordenarBolha(v)

2) Implemente uma função chamada exibirDados que recebe um vetor por parâmetros. Ela deve exibir na tela todos os valores
do vetor, um valor por linha: exibirDados(v)"""

import random

def gerarVetor(tamanho, tipo):
    if(tipo == "int"):
        vetor = [0] * tamanho
        for i in range(0, len(vetor)):
            vetor[i] = random.randint(0, 100)
    elif(tipo == "float"):
        vetor = [0.0] * tamanho
        for i in range(0, len(vetor)):
            vetor[i] = random.uniform(0, 100)
            #print(vetor[i])
            vetor[i] = float(f"{vetor[i]:.2f}")
            #print(vetor[i])
    else:
        print("Valor inválido.")
    return vetor

def ordenarBolha(vetor):
    for ciclo in range(0, len(vetor) - 1):
        for i in range(0, len(vetor) - 1):
            if(vetor[i] > vetor[i + 1]):
                aux = vetor[i]
                vetor[i] = vetor[i + 1]
                vetor[i + 1] = aux


def exibirDados(vetor):
    for i in range(0, len(vetor)):
        print(f"vetor[{i + 1}] = {vetor[i]}")
