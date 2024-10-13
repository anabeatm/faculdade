vetor = [10, 5, 3, 8, 2, 6]

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