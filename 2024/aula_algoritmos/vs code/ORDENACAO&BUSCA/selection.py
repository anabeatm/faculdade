vetor = [10, 5, 3, 8, 2, 6]

for i in range(0, len(vetor) - 1):
    imenor = i
    for j in range(i + 1, len(vetor)):
        if(vetor[j] < vetor[imenor]):
            imenor = j

    aux = vetor[i]
    vetor[i] = vetor[imenor]
    vetor[imenor] = aux