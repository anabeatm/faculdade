# Para os exercícios abaixo, utilize o vetor criado no exercício anterior.
tamanhoVetor = int(input("Informa o tamanho do vetor: "))
vetor = [0] * tamanhoVetor
for i in range(0, len(vetor)):
    vetor[i] = int(input(f"Digite o {i+1}° valor do vetor: "))
print(vetor)

# a) Apresente os números do vetor em ordem inversa.

# for i in range(len(vetor) - 1, -1, -1):
#     print(vetor[i])

# b) Apresente a soma de todos os elementos. 

# soma = 0
# for i in range(0, len(vetor)):
#     soma += vetor[i]
# print(soma)

# c) Calcule a média aritmética dos valores.

# media = soma / len(vetor)
# print(media)

# d) Liste na tela somente os números do vetor que estão em posições (índices) pares.

# for i in range(0, len(vetor)):
#     if(i % 2 == 0):
#         print(vetor[i])

# e) Determinar um segmento informado pelo usuário (posição inicial e final) para apresentar os números na tela. 
# Por exemplo: 
# Na sequência [5, 2, -2, -7, 3, 14, 10, -3, 9, -6, 4, 1] o usuário teria que informar 4 (na posição inicial) 
# e 8 (posição final) para mostrar na tela somente:  3, 14, 10, -3, 9.

# posicaoInicial = int(input("Informa a posição inicial do vetor: "))
# posicaoFinal = int(input("Informa a posição final do vetor: "))
# for i in range(posicaoInicial, posicaoFinal + 1, 1):
#     print(vetor[i])

# f) Semelhante ao anterior, porém deve-se fazer a soma dos valores contidos no vetor conforme a posição e 
# inicial informada. Exemplo: 
# Na sequência [5, 2, -2, -7, 3, 14, 10, -3, 9, -6, 4, 1] , o usuário teria que informar 4 (na posição inicial)
# e 8 (posição final) para realizar a soma do segmento destacado que é 33.

# soma = 0
# posicaoInicial = int(input("Informa a posição inicial: "))
# posicaoFinal = int(input("Informa a posição final: "))
# for i in range(posicaoInicial, posicaoFinal + 1, 1):
#     soma += vetor[i]
# print(soma)

# g) Encontre qual é o maior e o menor número desta lista.
# h) Encontre qual é o maior e o menor número desta lista. Além disso, informe quais são os índices (posições) deles.
maior = vetor[0]
menor = vetor[0]

posicaoMaior = 0
posicaoMenor = 0

for i in range(0, len(vetor)):
    if(vetor[i] > maior):
        maior = vetor[i]
        posicaoMaior = i

    if(vetor[i] < menor):
        menor = vetor[i]
        posicaoMenor = i
print(f"O maior número é {maior} e sua posição é {posicaoMaior}\nO menor número é {menor} e sua posição é {posicaoMenor}")

# i) Informe quantos números pares e ímpares foram digitados (apenas a quantidade de cada).

# qntdPar = 0
# qntdImpar = 0

# for i in range(0, len(vetor)):
#     if(vetor[i] % 2 == 0):
#         qntdPar += 1
#     if(vetor[i] % 2 != 0):
#         qntdImpar += 1

# print(f"""A quantidade de pares é: {qntdPar}
# A quantidade de ímpares é: {qntdImpar}""")
