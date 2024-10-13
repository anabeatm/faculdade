vetor = [10, 5, 3, 8, 2, 6]

for ciclo in range(0, len(vetor) - 1):
    for i in range(0, len(vetor) - 1):
        if(vetor[i] > vetor [i + 1]):
            aux = vetor[i]
            vetor[i] = vetor[i + 1]
            vetor[i + 1] = aux