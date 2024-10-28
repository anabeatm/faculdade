# Considerando que uma palavra (string) pode ser percorrida como um vetor, faça um programa que peça o 
# nome de uma pessoa e o apresente de trás para frente.

nome = input("Informe seu primeiro nome: ")
nome_invertido = ""

for i in range(len(nome) - 1, -1, -1):
    nome_invertido += nome[i]

print(f"Seu nome invertido: {nome_invertido}")
