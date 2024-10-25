vetor = [10, 5, 3, 8, 2, 6]
# ordenar o vetor antes

# bubble for in for
for ciclo in range(0, len(vetor)):
    for i in range(0, len(vetor)):
        if(vetor[i] > vetor[i + 1]):
            aux = vetor[i]
            vetor[i] = vetor[i + 1]
            vetor[i + 1] = aux

# insertion while in for
for i in range(1, len(vetor)):
    j = i - 1
    valor = vetor[i]
    while(j >= 0 and valor < vetor[j]):
        vetor[j + 1] = vetor[j]
        j -= 1
        vetor[j + 1] = valor

# selection for in for
for i in range(0, len(vetor) - 1):
    imenor = i
    for j in range(i + 1, len(vetor)):
        if(vetor[j] < vetor[imenor]):
            imenor = j
    
    aux = vetor[i]
    vetor[i] = vetor[imenor]
    vetor[imenor] = aux

valorBuscado = int(input("Qual o número que está buscando? R: "))

find = False

for d in range(0, len(vetor)):
    if(valorBuscado == vetor[d]):
        find = True
        break

if(find):
    print("Valor encontrado!")
else:
    print(f"Valor não encontrado! Seu vetor tem os seguintes dados: {vetor}")