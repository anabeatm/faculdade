# Crie um vetor e armazene os números de 1 a 100. Cada número deve ocupar uma posição do vetor (lista).

# vetor = [0] * 100
# for i in range(0, len(vetor)):
#     vetor[i] = i + 1


# a) Mostre na tela todos os números do vetor em ordem crescente (1 a 100).

# for i in range(0, len(vetor)):
#     print(vetor[i])

# b) Mostre na tela todos os números do vetor em ordem decrescente (100 a 1)

# for i in range(len(vetor) - 1, -1, -1):
#     #         ultimo indice | ate o indice 0 | passo - de trás pra frente
#     print(vetor[i])

# c) Mostre na tela o dobro de todos os números.

# for i in range (0, len(vetor)):
#     dobro = vetor[i] * 2
#     print(dobro)

# d) Apresente na tela a soma de todos os números.

# soma = 0
# for i in range(0, len(vetor)):
#     soma = soma + vetor[i]
# print(soma)

# e) Apresente na tela a média geral dos valores contidos na lista.

# media = soma / len(vetor)
# print(media)

# f) Mostre na tela a quantidade de números pares.

# qntdPares = 0
# for i in range(0, len(vetor)):
#     if(vetor[i] % 2 == 0):
#         qntdPares += 1
# print(qntdPares)