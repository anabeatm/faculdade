# Utilize a função gerar_lista para criar uma lista de 100 elementos com valores entre 1 e 1000. 
# Em seguida, utilize a função busca_binaria_com_contagem para encontrar um elemento na lista. 
# Anote o número de comparações realizadas e discuta a eficiência da busca binária em comparação com a busca sequencial.
from random import randint


vetor = [0] * 100

for indice in range(0, len(vetor)):
    vetor[indice] = randint(1, 1000)

print("Organizando o vetor . . . ")

for i in range(1, len(vetor)):
    j = i - 1
    valor = vetor[i]
    while(j >= 0 and valor < vetor[j]):
        vetor[j + 1] = vetor[j]
        j -= 1
        vetor[j + 1] = valor

print(vetor)

valorBuscado = int(input("Digite um número inteiro entre 1 a 1000 que gostaria de encontrar: "))

find = False
start = 0
end = len(vetor) - 1

contador = 0
cont = 0

while(start <= end):
    middle = (start + end) // 2
    contador += 1
    if(valorBuscado == vetor[middle]):
        find = True
        break
    else:
        if(valorBuscado > vetor[middle]):
            start = middle + 1
        else:
            end = middle - 1
        contador += 1

for c in range(0, len(vetor)):
    cont += 1
    if(valorBuscado == vetor[c]):
        find = True
        break


if(find):
    print(f"""Valor {valorBuscado} encontrado no índice {middle}.
Busca binária: {contador} comparações.
Busca Sequencial: {cont} comparações.""")

else:
    print("Valor não encontrado!")
