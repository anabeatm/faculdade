# Modifique a função busca_binaria para que ela conte e retorne o número de comparações realizadas durante a busca, 
# além do índice do elemento encontrado, ou -1 caso contrário.

valores = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

for i in range(0, len(valores) - 1):
    imenor = i
    for j in range(i + 1, len(valores)):
        if(valores[j] < valores[imenor]):
            imenor = j
    
    aux = valores[i]
    valores[i] = valores[imenor]
    valores[imenor] = aux

valorBuscado = int(input("Digite um valor que gostaria de procurar: "))

find = False
start = 0
end = len(valores) - 1
contador = 0

while(start <= end):
    middle = (start + end) // 2
    contador += 1
    if(valorBuscado == valores[middle]):
        find = True
        break
    else:
        contador += 1
        if(valorBuscado > valores[middle]):
            start = middle + 1
        else:
            end = middle - 1

if(find):
    print(f"Valor encontrado no índice: {middle} e houve {contador} comparações.")
else:
    print("Valor não encontrado! -1")
