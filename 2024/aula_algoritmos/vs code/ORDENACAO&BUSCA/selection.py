vetor = [10, 5, 3, 8, 2, 6]

for i in range(0, len(vetor) - 1):
    imenor = i
    for j in range(i + 1, len(vetor)):
        if(vetor[j] < vetor[imenor]):
            imenor = j

    aux = vetor[i]
    vetor[i] = vetor[imenor]
    vetor[imenor] = aux

# a ordenação de selection utiliza um for de indice que começa com 0 até len de vetor - 1.
# cria-se a variavel iMenor que receberá indice.
# após utiliza-se um for de j onde começa com i + 1 até len de vetor.
# acontecerá uma comparação em que se o valor no vetor de j é menor que o valor no vetor de iMenor,
# então iMenor receberá j.
# fora da comparação, acontecerá uma troca onde a variavel auxiliar recebe o valor de vetor em i,
# vetor de i recebe o valor de vetor de iMenor, e por ultimo, vetor de iMenor recebe o valor da 
#variavel auxiliar.