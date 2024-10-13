# Crie um experimento aleatório para testar a diferença entre a busca sequencial e binária em uma lista de inteiros.
from random import randint

tamVetor = int(input("Informe o tamanho do vetor: "))

vetor = [0] * tamVetor

inferior = int(input("Informe o menor valor possível do vetor: "))
superior = int(input("Informe o maior valor possível do vetor: "))

for c in range(0, len(vetor)):
    vetor[c] = randint(inferior, superior)


for i in range(0, len(vetor) - 1):
    iMenor = i
    for j in range(i + 1, len(vetor) - 1):
        if(vetor[j] < vetor[iMenor]):
            iMenor = j

    aux = vetor[i]
    vetor[i] = vetor[iMenor]
    vetor[iMenor] = aux

# print("Seu vetor é:", vetor)



# Busca Binária
valorBuscado = int(input("Qual o número que está buscando? R: "))

find = False
start = 0
end = len(vetor) - 1

while(start <= end):
    middle = (start + end) // 2
    if(valorBuscado == vetor[middle]):
        find = True
        break
    elif(valorBuscado > vetor[middle]):
        start = middle + 1
    else:
        end = middle - 1
if(find):
    print("Valor encontrado!")
else:
    print(f"Valor não encontrado! Seu vetor tem os seguintes dados: {vetor}")

# Busca Sequencial

find = False

for d in range(0, len(vetor)):
    if(valorBuscado == vetor[d]):
        find = True
        break

if(find):
    print("Valor encontrado!")
else:
    print(f"Valor não encontrado! Seu vetor tem os seguintes dados: {vetor}")