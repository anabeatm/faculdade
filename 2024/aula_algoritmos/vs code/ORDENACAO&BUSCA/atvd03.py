# Insertion

# Utilizando o algoritmo de ordenação por Inserção (Insertion Sort) onde um passo (ou ciclo) de 
# trocas corresponde a encontrar o local exato de um valor e deslocar todos os próximos valores uma casa para 
# frente. Considere o seguinte vetor: 

vetor = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1] 

# Considere ainda que o primeiro valor do vetor já se encontra em sua devida posição e o primeiro passo se 
# inicia com a busca pela posição correta do segundo valor do vetor. Considerando o “pior caso” (onde o vetor 
# está completamente desordenado, na ordem inversa a que se deseja), quantos passos serão necessários para 
# ordenar o vetor valores?

for i in range(1, len(vetor)):
    j = i - 1
    valor = vetor[i]
    while(j >= 0 and valor < vetor[j]):
        vetor[j + 1] = vetor[j]
        j -= 1
        vetor[j + 1] = valor
    print(i, vetor)
# Serão necessários 9 ciclos.
