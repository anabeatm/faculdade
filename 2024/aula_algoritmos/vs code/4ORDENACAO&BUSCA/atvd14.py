# Escreva uma função gerar_lista que recebe dois parâmetros: o tamanho da lista e o intervalo dos valores 
# (por exemplo, entre 1 e 100). A função deve retornar uma lista contendo números aleatórios dentro do 
# intervalo especificado.
from random import randint

tamVetor = int(input("Tamanho do vetor: "))

vetor = [0] * tamVetor

intervaloMenor = int(input("Valor do menor intervalo: "))
intervaloMaior = int(input("Valor do maior intervalo: "))

for i in range(0, len(vetor)):
    vetor[i] = randint(intervaloMenor, intervaloMaior)

print(vetor)
