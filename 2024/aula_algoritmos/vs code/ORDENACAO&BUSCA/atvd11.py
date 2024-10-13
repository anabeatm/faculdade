# Implemente a função busca_sequencial que recebe uma lista e um valor a ser procurado na lista. 
# A função deve retornar o índice do valor na lista, se encontrado, ou -1 caso contrário.

valores = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1] 

# bubble
for ciclo in range(0, len(valores) - 1):
    for i in range(0, len(valores) - 1):
        if(valores[i] > valores[i + 1]):
            aux = valores[i]
            valores[i] = valores[i + 1]
            valores[i + 1] = aux

valorBuscado = int(input("Digite o valor que deseja ser buscado: "))

find = False

for e in range(0, len(valores)):
    if(valorBuscado == valores[e]):
        find = True
        break

if(find):
    print("Índice:", e)
else:
    print(-1)
    