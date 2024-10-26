# Bubble

#  Utilizando o algoritmo de ordenação por Bolha (Bubble Sort) onde um ciclo de trocas corresponde 
# a fazer a comparação de todos os valores do vetor com os seus adjacentes. Considere o seguinte vetor: 

valores = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1] 

# Considere ainda que o vetor “valores” precise ser ordenado de forma crescente. Considerando o “pior caso” 
# (onde o vetor está completamente desordenado, na ordem inversa a que se deseja), quantos ciclos de troca 
# serão necessários para ordenar o vetor valores? 

for ciclo in range(0, len(valores) - 1):
    for i in range(0, len(valores) - 1):
        if(valores[i] > valores[i + 1]):
            aux = valores[i]
            valores[i] = valores[i + 1]
            valores[i + 1] = aux
    print(ciclo, valores)
# Serão necessários 8 ciclos.
