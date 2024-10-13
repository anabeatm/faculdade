# Implemente a função busca_binaria que recebe uma lista ordenada e um valor a ser procurado na lista. 
# A função deve retornar o índice do valor na lista, se encontrado, ou -1 caso contrário.

valores = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

for i in range(0, len(valores) - 1):
    imenor = i
    for j in range(i + 1, len(valores)):
        if(valores[j] < valores[imenor]):
            imenor = j
    
    aux = valores[i]
    valores[i] = valores[imenor]
    valores[imenor] = aux

valorBuscado = int(input("Digite o valor que gostaria de buscar: "))

find = False
start = 0
end = len(valores) - 1

while(start <= end):
    middle = (start + end) // 2
    if(valorBuscado == valores[middle]):
        find = True
        break
    elif(valorBuscado > valores[middle]):
        start = middle + 1
    else:
        end = middle - 1

if(find):
    print("Valor encontrado no índice", middle)
else:
    print("Valor não encontrado! -1")
