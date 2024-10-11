#  Utilizando o seguinte vetor: 

precos = [1.99, 10.99, 10.50, 8.50, 7.49, 1599.45, 1400.00] 

# Apresente o “passo a passo” para a ordenação deste vetor utilizando o algoritmo Insertion Sort. 

for i in range(1, len(precos)):
    j = i - 1
    valor = precos[i]
    while(j >= 0 and valor < precos[j]):
        precos[j + 1] = precos[j]
        j -= 1
        precos[j + 1] = valor
    print(i, precos)