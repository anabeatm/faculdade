#  Implemente um algoritmo que solicite ao usuário pelo tamanho de um vetor de números inteiros. 
# O algoritmo deve ser capaz de criar este vetor. O algoritmo deve solicitar ao usuário por todos os dados deste 
# vetor. Apresente os dados informados pelo usuário em ordem crescente. Utilize o algoritmo de ordenação por 
# Bolha.

tamVetor = int(input("Informe o tamanho do vetor: "))

vetor = [0] * tamVetor

for c in range(0, len(vetor)):
    vetor[c] = int(input("Coloque os dados desse vetor: "))

# odernação bubble

for ciclo in range(0, len(vetor) - 1):
    for i in range(0, len(vetor) - 1):
        if(vetor[i] > vetor[i + 1]):
            aux = vetor[i]
            vetor[i] = vetor[i + 1]
            vetor[i + 1] = aux
print("Seu vetor é:", vetor)