vetor = [10, 5, 3, 8, 2, 6]

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