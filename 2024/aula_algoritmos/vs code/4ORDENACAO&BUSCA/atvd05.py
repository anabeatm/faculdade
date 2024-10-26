# Selection

# Utilizando o algoritmo de ordenação por Seleção (Selection Sort) onde um passo de trocas 
# corresponde a encontrar o menor valor e colocar em sua posição atual representada pelo passo, trocando os 
# valores. Considere o seguinte vetor: 

vetor = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1] 

# Considerando o “pior caso” (onde o vetor está completamente desordenado, na ordem inversa a que se 
# deseja), quantos passos serão necessários para ordenar o vetor valores? 

for i in range(0, len(vetor) - 1):
    iMenor = i
    for j in range(i + 1, len(vetor)):
        if(vetor[j] < vetor[iMenor]):
            iMenor = j
    
    aux = vetor[i]
    vetor[i] = vetor[iMenor]
    vetor[iMenor] = aux
    
    print(vetor)
# Serão necessários 9 ciclos (?).