# Utilizando o seguinte vetor: 

precos = [1.99, 10.99, 10.50, 8.50, 7.49, 1599.45, 1400.00] 

# Apresente o “passo a passo” para a ordenação deste vetor utilizando o algoritmo Selection Sort.

for i in range(0, len(precos) - 1):
    iMenor = i
    for j in range(i + 1, len(precos)):
        if(precos[j] < precos[iMenor]):
            iMenor = j
    
    aux = precos[i]
    precos[i] = precos[iMenor]
    precos[iMenor] = aux

    print(precos)
    