vetor = [10, 5, 3, 8, 2, 6]
# ordernar o vetor antes

# método bubble:
# for ciclo in range(0, len(vetor) - 1):
#     for i in range(0, len(vetor) - 1):
#         if(vetor[i] > vetor[i + 1]):
#             aux = vetor[i]
#             vetor[i] = vetor[i + 1]
#             vetor[i + 1] = aux

# método insertion:
# for i in range(1, len(vetor)):
#     j = i - 1
#     valor = vetor[i]
#     while(j >= 0 and valor < vetor[j]):
#         vetor[j + 1] = vetor[j]
#         j -= 1
#         vetor[j + 1] = valor

# método selection
for i in range(0, len(vetor) - 1):
    iMenor = i
    for j in range(i + 1, len(vetor)):
        if(vetor[j] < vetor[iMenor]):
            iMenor = j
        
    aux = vetor[i]
    i = vetor[iMenor]
    vetor[iMenor] = aux



valorBuscado = int(input("Qual o número que está buscando? R: "))

find = False
start = 0
end = len(vetor) - 1

while(start <= end):
    middle = (start + end) // 2
    if(valorBuscado == vetor[middle]):
        find = True
        break

    else:
        if(valorBuscado > vetor[middle]):
            start = middle + 1
        else:
            end = middle - 1

if(find):
    print("Valor encontrado!")
else:
    print(f"Valor não encontrado! Seu vetor tem os seguintes dados: {vetor}")
