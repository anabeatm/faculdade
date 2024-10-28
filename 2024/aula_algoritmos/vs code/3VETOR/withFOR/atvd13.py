# Um esquema de sorteio precisa armazenar uma lista de 10 pessoas e ao final sortear uma delas aleatoriamente. 
# Faça um programa para este esquema.
from random import choice

listaNomes = [""] * 10
for i in range(0, len(listaNomes)):
    listaNomes[i] = input(f"Informe o {i + 1}° nome: ")

nomeEscolhido = choice(listaNomes)
print(f"A pessoa sorteada foi {nomeEscolhido}!")
