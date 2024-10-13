vetor = [10, 5, 3, 8, 2, 6]

for i  in range(1, len(vetor)):
    j = i - 1
    valor = vetor[i]
    while(j >= 0 and valor < vetor[j]):
        vetor[j + 1] = vetor[j]
        j -= 1
        vetor[j + 1] = valor