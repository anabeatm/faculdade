#  Implemente um algoritmo que solicite ao usuário pelo tamanho de um vetor de números ponto
# flutuantes. O algoritmo deve ser capaz de criar este vetor e solicitar por todos os números ao usuário para o 
# preenchimento deste vetor. Aplique o algoritmo de Ordenação por Inserção para ordenar os dados deste 
# vetor. Por fim, apresente o vetor ordenado ao usuário.

tamVetor = int(input("Informe o tamanho do vetor: "))

vetor = [0.0] * tamVetor

for c in range(0, len(vetor)):
    vetor[c] = int(input(f"Coloque o {c + 1}° dado desse vetor: "))

for i in range(1, len(vetor)):
    j = i - 1
    valor = vetor[i]
    while(j >= 0 and valor < vetor[j]):
        vetor[j + 1] = vetor[j]
        j -= 1
        vetor[j + 1] = valor

print("Seu vetor é:", vetor)

