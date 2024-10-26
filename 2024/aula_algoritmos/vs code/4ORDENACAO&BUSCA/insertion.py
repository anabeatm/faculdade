vetor = [10, 5, 3, 8, 2, 6]

for i  in range(1, len(vetor)):
    j = i - 1
    valor = vetor[i]
    while(j >= 0 and valor < vetor[j]):
        vetor[j + 1] = vetor[j]
        j -= 1
        vetor[j + 1] = valor

# insertion utiliza um for de indice que começa da posição 1 até len de vetor. 
# é criado uma variavel chamada j que armazenará o valor de indice - 1.
# a variavel valor armazenará o valor de vetor de indice.
# cria-se um while onde se j é maior ou igaul a zero E a variavel 
# valor é menor que o valor vetor de j, então
# vetor de j + 1 irá receber o valor de vetor de j, após isso j é j - 1 e ao final,
# vetor de j + 1 recebe a variavel valor.