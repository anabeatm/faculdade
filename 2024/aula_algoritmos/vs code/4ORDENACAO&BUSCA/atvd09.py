from random import randint
#  Implemente um algoritmo que solicite ao usuário pelo tamanho de um vetor de números inteiros 
# e pelos limites inferior e superior (menor valor possível e maior valor possível para preencher este vetor). O 
# algoritmo deve ser capaz de criar este vetor e preenchê-lo com valores aleatórios entre os limites inferior e 
# superior. Exiba o vetor com os valores. Aplique o algoritmo de Ordenação por Seleção para ordenar os dados 
# deste vetor. Por fim, apresente o vetor ordenado ao usuário.

tamVetor = int(input("Informe o tamanho do vetor: "))

vetor = [0] * tamVetor

inferior = int(input("Informe o menor valor possível do vetor: "))
superior = int(input("Informe o maior valor possível do vetor: "))


for c in range(0, len(vetor)):
    vetor[c] = randint(inferior, superior)

print("Seu vetor tem esses valores:", vetor)
print("Organizaremos esse vetor . . .")

for i in range(0, len(vetor) - 1):
    iMenor = i
    for j in range(i + 1, len(vetor)):
        if(vetor[j] < vetor[iMenor]):
            iMenor = j
    
    aux = vetor[i]
    vetor[i] = vetor[iMenor]
    vetor[iMenor] = aux

print("Seu vetor organizado agora é este:", vetor)