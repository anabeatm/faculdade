# Utilizando o seguinte vetor: 

precos = [1.99, 10.99, 10.50, 8.50, 7.49, 1599.45, 1400.00] 

# Apresente o “passo a passo” para a ordenação deste vetor utilizando o algoritmo Bubble Sort. 

for ciclo in range(0, len(precos) - 1):
    for i in range(0, len(precos) - 1):
        if(precos[i] > precos[i + 1]):
            aux = precos[i]
            precos[i] = precos[i + 1]
            precos[i + 1] = aux
        print(ciclo, precos)