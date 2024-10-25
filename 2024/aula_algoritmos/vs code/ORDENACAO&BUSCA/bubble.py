vetor = [10, 5, 3, 8, 2, 6]

for ciclo in range(0, len(vetor) - 1):
    for i in range(0, len(vetor) - 1):
        if(vetor[i] > vetor[i + 1]):
            aux = vetor[i]
            vetor[i] = vetor[i + 1]
            vetor[i + 1] = aux

# o método de ordenação bubble utiliza um for de ciclo de 0 a len de vetor - 1, mais um for de
# indice que vai de 0 a len de vetor - 1.
# após isso ocorre uma comparação onde se vetor de indice é maior que o vetor indice + 1, ent
# criará uma variável auxiliar que receberá o valor de vetor de indice, após isso o vetor de indice
# armazenará o valor do vetor de indice + 1, e o vetor indice + 1 receberá o valor da variavel 
# auxiliar.