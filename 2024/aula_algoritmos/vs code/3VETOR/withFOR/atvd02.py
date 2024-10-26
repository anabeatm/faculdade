# Faça um programa para armazenar 6 números inteiros para uma loteria, permitindo que o usuário informe os números.
# Depois de preencher, informe uma mensagem e os números sorteados.

from random import choice

vetorLoteria = [0] * 6

for i in range(0, len(vetorLoteria)):
    vetorLoteria[i] = int(input("Informa um número para ser sorteado: "))
numSorteado = choice(vetorLoteria)
print(f"O número sorteado é: {numSorteado}")

# Outro jeito de fazer:
# from random import randint
# numeroLoteria = []
# for i in range(6):
#     numero = int(input(f"Informe o {i+1}° número da loteria: "))
#     numeroLoteria.append(numero)

# print(f"Os número da loteria são: {numeroLoteria}")

# indiceSorteado = randint(0, 5)
# numSorteado = numeroLoteria[indiceSorteado]

# print(f"O número sorteado é: {numSorteado}")
