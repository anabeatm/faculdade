# Implemente um programa que, ao ser executado, solicite ao usuário pelo nome de dois arquivos 
# que contenham textos. O programa deve comparar se os dois arquivos são iguais. 

# arquivos = [""] * 2
# for i in range(0, len(arquivos)):
#     arquivos[i] = input("Escreva o nome do arquivo [arquivo.txt]: ")

# arquivo = open(arquivos[0], "r", encoding="UTF-8")
# listaArquivo = arquivo.readlines()

# segundoArquivo = open(arquivos[1], "r", encoding="UTF-8")
# listaArquivo2 = segundoArquivo.readlines()

# arquivo.close()
# segundoArquivo.close()

# if(listaArquivo == listaArquivo2):
#     print("Ambos arquivos são os mesmos.")
# else:
#     print("Esses arquivos não são os mesmos.")

# Implemente um programa que solicite ao usuário pelo nome de um arquivo. Apresente na tela 
# quantas linhas existem neste arquivo.

# arquivo = input("Escreva o nome do arquivo.txt: ")

# abrirArquivo = open(arquivo, "r", encoding="UTF-8")
# lendoArquivo = abrirArquivo.readlines()
# arquivo.close()

# linhasArquivo = len(lendoArquivo)
# print(f"Seu arquivo tem {linhasArquivo} linhas.")

#  Desenvolva  um  programa  que  solicite  faça  a  abertura  de  um  arquivo  e  faça  uma  cópia  do 
# conteúdo deste arquivo para um novo arquivo.

# def copiandoArquivo(nomeArquivo):
#     arquivo = open(nomeArquivo, "r", encoding="UTF-8")
#     linhasArquivo = arquivo.readlines()

#     novoArquivo = open("copia.txt", "w", encoding="UTF-8")

#     i = 0
#     while(i < len(linhasArquivo)):
#         novaLinha = linhasArquivo[i]
#         novoArquivo.write(novaLinha)
#         i += 1

#     arquivo.close()
#     novoArquivo.close()

# nomeArquivo = input("Escreva o nome do arquivo.txt: ")
# copiandoArquivo(nomeArquivo)

# Considere o seguinte requisito de software: Um sistema deve ser capaz de abrir um arquivo de 
# texto. O usuário deve informar um caractere e o sistema deve apresentar quantas vezes o caractere fornecido 
# aparece no texto. Desenvolva um aplicativo que seja capaz de representar este requisito.

# def verificandoCaracteres(nomeArquivo, caractere):
#     arquivo = open(nomeArquivo, "r", encoding="UTF-8")
#     linhasArquivo = arquivo.readlines()


#     contCaractere = 0
    
#     for i in range(0, len(linhasArquivo)):
#         linha = linhasArquivo[i]

#         for j in range(0, len(linha)):

#             if(caractere == linha[j]):
#                 contCaractere += 1
    
#     arquivo.close()

#     return contCaractere

# nomeArquivo = input("Escreva o nome do arquivo.txt: ")
# caractere = input("Qual caractere gostaria de verificar sua quantidade? R: ")

# retorno = verificandoCaracteres(nomeArquivo, caractere)

# print(f"Há {retorno} do caractere {caractere}.")

# Implemente um algoritmo que faça a leitura de um número N que representa quantos valores 
# devem  ser  sorteados  aleatoriamente  (entre  0  e  100).  O  algoritmo  deve  sortear  os  N  números  aleatórios 
# armazenando-os em um vetor. Por fim, os dados deste vetor devem ser salvos em um arquivo texto. Ao salvar 
# o arquivo texto, a primeira linha do arquivo deve conter a quantidade de números sorteados.
import random as r

numeroN = int(input("Escreva quantas vezes haverá sorteio de 0 a 100: "))
numerosSorteados = [0] * numeroN

for i in range(0, numeroN):
    numerosSorteados[i] = r.randint(0, 100)

arquivo = open("numerosSorteados.txt", "w", encoding="UTF-8")

arquivo.write("Quantidade de números sorteados: " + str(numeroN) + "\n")

for c in range(0, len(numerosSorteados)):
    linha = numerosSorteados[c]
    arquivo.write(str(linha) + "\n")

arquivo.close()